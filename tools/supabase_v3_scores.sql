-- v3: progress scores (teacher grading + speaking assessment) for the student home page "My progress".
-- Run once in Supabase → SQL Editor → New query → paste → Run. Safe to run again.
-- Teacher key = the same key as bp-admin (table admin_keys). The key is checked here, never in the page.

create table if not exists public.student_scores (
  student_slug text not null references public.students(slug) on delete cascade,
  kind text not null check (kind in ('task','speech')),
  id text not null,
  data jsonb not null,
  updated_at timestamptz not null default now(),
  primary key (student_slug, kind, id)
);
alter table public.student_scores enable row level security;
revoke all on public.student_scores from anon, authenticated;   -- no direct access: only the functions below

-- Is this a valid teacher key? (the page asks before showing Teacher mode)
create or replace function public.admin_check(p_key text) returns boolean
language sql security definer set search_path = public as $$
  select exists(select 1 from public.admin_keys where key = p_key);
$$;

-- Student (by personal code): read only
create or replace function public.get_my_scores(p_code text) returns jsonb
language sql security definer set search_path = public as $$
  select jsonb_build_object(
    'tasks',  coalesce((select jsonb_agg(sc.data order by sc.data->>'date', sc.id) from public.student_scores sc where sc.student_slug = s.slug and sc.kind = 'task'), '[]'::jsonb),
    'speech', coalesce((select jsonb_agg(sc.data order by sc.data->>'date', sc.id) from public.student_scores sc where sc.student_slug = s.slug and sc.kind = 'speech'), '[]'::jsonb),
    -- automatic results: Check scores of every page + skill tags the page saved in answers._meta
    'auto',   coalesce((select jsonb_agg(jsonb_build_object('lesson', h.lesson, 'score', h.score, 'meta', h.answers->'_meta', 'at', h.updated_at))
                        from public.homework_answers h where h.student_slug = s.slug and h.answers ? '_meta'), '[]'::jsonb),
    -- vocabulary trainer (vocab.html): known / learning / total
    'vocab',  (select h.score || jsonb_build_object('at', h.updated_at) from public.homework_answers h
               where h.student_slug = s.slug and h.lesson like 'BP % Vocabulary' order by h.updated_at desc limit 1))
  from public.students s where s.code = p_code;
$$;

-- Teacher (by key): replace the student's grading and speaking rows with the lists sent from the page
create or replace function public.admin_set_scores(p_key text, p_code text, p_tasks jsonb, p_speech jsonb) returns timestamptz
language plpgsql security definer set search_path = public as $$
declare s public.students; r jsonb; t timestamptz := now();
begin
  if not exists(select 1 from public.admin_keys where key = p_key) then raise exception 'wrong teacher key'; end if;
  select * into s from public.students where code = p_code;
  if s.slug is null then raise exception 'unknown student code'; end if;
  if jsonb_typeof(coalesce(p_tasks,'[]')) <> 'array' or jsonb_typeof(coalesce(p_speech,'[]')) <> 'array' then raise exception 'tasks and speech must be lists'; end if;

  for r in select * from jsonb_array_elements(coalesce(p_tasks,'[]')) loop
    if coalesce(r->>'id','') = '' then raise exception 'task without id'; end if;
    if (r->>'date') !~ '^\d{4}-\d{2}-\d{2}$' then raise exception 'task %: date must be YYYY-MM-DD', r->>'id'; end if;
    if (r->>'pct') !~ '^\d+(\.\d+)?$' or (r->>'pct')::numeric > 100 then raise exception 'task %: percent must be 0–100', r->>'id'; end if;
    if coalesce(r->>'stage','') not in ('first','review') then raise exception 'task %: stage must be first or review', r->>'id'; end if;
    if coalesce(r->>'skill','') = '' then raise exception 'task %: skill is empty', r->>'id'; end if;
  end loop;
  for r in select * from jsonb_array_elements(coalesce(p_speech,'[]')) loop
    if coalesce(r->>'id','') = '' then raise exception 'speaking row without id'; end if;
    if (r->>'date') !~ '^\d{4}-\d{2}-\d{2}$' then raise exception 'speaking %: date must be YYYY-MM-DD', r->>'id'; end if;
    if (r->>'wpm') is not null and ((r->>'wpm') !~ '^\d+$' or (r->>'wpm')::int not between 40 and 260) then raise exception 'speaking %: WPM must be 40–260', r->>'id'; end if;
    if exists(select 1 from unnest(array['fluency','accuracy','range','pron']) b
              where (r->>b) is not null and ((r->>b) !~ '^[1-5]$')) then raise exception 'speaking %: bands must be 1–5', r->>'id'; end if;
  end loop;

  delete from public.student_scores where student_slug = s.slug;
  insert into public.student_scores(student_slug, kind, id, data, updated_at)
    select s.slug, 'task', x->>'id', x, t from jsonb_array_elements(coalesce(p_tasks,'[]')) x
    union all
    select s.slug, 'speech', x->>'id', x, t from jsonb_array_elements(coalesce(p_speech,'[]')) x;
  return t;
end $$;

revoke all on function public.admin_check(text) from public;
revoke all on function public.get_my_scores(text) from public;
revoke all on function public.admin_set_scores(text,text,jsonb,jsonb) from public;
grant execute on function public.admin_check(text) to anon;
grant execute on function public.get_my_scores(text) to anon;
grant execute on function public.admin_set_scores(text,text,jsonb,jsonb) to anon;
