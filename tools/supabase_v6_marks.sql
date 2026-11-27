-- v6: teacher-only marks for single exercises ("done" + score out of max). The student never reads this table.
-- Written from the lesson page in teacher mode (?teacher, teacher key). Safe to run again.
create table if not exists public.exercise_marks (
  student_slug text not null references public.students(slug) on delete cascade,
  lesson text not null,            -- page key, e.g. 'BP B1 1.1 Transferable skills · Homework'
  ex text not null,                -- exercise label on the page, e.g. '4A'
  done boolean not null default false,
  score numeric, max numeric, note text,
  updated_at timestamptz not null default now(),
  primary key (student_slug, lesson, ex)
);
alter table public.exercise_marks enable row level security;
revoke all on public.exercise_marks from anon, authenticated;

-- Teacher: the student's answers on one page + the marks (by student code, so it works from the student's own site)
create or replace function public.admin_lesson_view(p_key text, p_code text, p_lesson text) returns jsonb
language plpgsql security definer set search_path = public as $$
declare s public.students; r jsonb;
begin
  if not exists(select 1 from public.admin_keys where key = p_key) then raise exception 'wrong teacher key'; end if;
  select * into s from public.students where code = p_code;
  if s.slug is null then raise exception 'unknown student code'; end if;
  select jsonb_build_object('name', s.name,
    'answers', (select h.answers from public.homework_answers h where h.student_slug = s.slug and h.lesson = p_lesson),
    'submitted', coalesce((select h.submitted from public.homework_answers h where h.student_slug = s.slug and h.lesson = p_lesson), false),
    'marks', coalesce((select jsonb_agg(jsonb_build_object('ex', m.ex, 'done', m.done, 'score', m.score, 'max', m.max, 'note', m.note, 'at', m.updated_at))
                       from public.exercise_marks m where m.student_slug = s.slug and m.lesson = p_lesson), '[]'::jsonb)) into r;
  return r;
end $$;

create or replace function public.admin_mark(p_key text, p_code text, p_lesson text, p_ex text, p_done boolean, p_score numeric, p_max numeric, p_note text)
returns timestamptz language plpgsql security definer set search_path = public as $$
declare s public.students; t timestamptz := now();
begin
  if not exists(select 1 from public.admin_keys where key = p_key) then raise exception 'wrong teacher key'; end if;
  select * into s from public.students where code = p_code;
  if s.slug is null then raise exception 'unknown student code'; end if;
  if p_score is not null and (p_score < 0 or (p_max is not null and p_score > p_max)) then raise exception 'score must be between 0 and max'; end if;
  insert into public.exercise_marks(student_slug, lesson, ex, done, score, max, note, updated_at)
  values (s.slug, p_lesson, p_ex, coalesce(p_done,false), p_score, p_max, nullif(p_note,''), t)
  on conflict (student_slug, lesson, ex) do update set done = excluded.done, score = excluded.score, max = excluded.max, note = excluded.note, updated_at = t;
  return t;
end $$;

revoke all on function public.admin_lesson_view(text,text,text) from public;
revoke all on function public.admin_mark(text,text,text,text,boolean,numeric,numeric,text) from public;
grant execute on function public.admin_lesson_view(text,text,text) to anon;
grant execute on function public.admin_mark(text,text,text,text,boolean,numeric,numeric,text) to anon;
