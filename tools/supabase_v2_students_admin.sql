-- v2: students with personal codes, closed table, RPC access, admin by key
create table if not exists public.students (
  slug text primary key,
  name text not null,
  level text not null,
  track text not null default 'all',
  code text unique not null default md5(random()::text || clock_timestamp()::text),
  created_at timestamptz not null default now()
);
alter table public.students enable row level security;

create table if not exists public.admin_keys (key text primary key);
alter table public.admin_keys enable row level security;

alter table public.homework_answers add column if not exists student_slug text references public.students(slug);
alter table public.homework_answers add column if not exists teacher_comment text;
alter table public.homework_answers add column if not exists comment_at timestamptz;
create unique index if not exists hw_slug_lesson on public.homework_answers(student_slug, lesson);

-- close direct access for the public key
drop policy if exists "hw read" on public.homework_answers;
drop policy if exists "hw insert" on public.homework_answers;
drop policy if exists "hw update" on public.homework_answers;
revoke all on public.homework_answers from anon;
revoke all on public.students from anon;
revoke all on public.admin_keys from anon;
revoke all on public.homework_answers from authenticated;
revoke all on public.students from authenticated;
revoke all on public.admin_keys from authenticated;

-- ===== student functions (by personal code) =====
create or replace function public.save_hw(p_code text, p_lesson text, p_answers jsonb, p_score jsonb, p_submitted boolean)
returns timestamptz language plpgsql security definer set search_path = public as $$
declare s public.students; t timestamptz := now();
begin
  select * into s from public.students where code = p_code;
  if s.slug is null then raise exception 'unknown student code'; end if;
  insert into public.homework_answers(student, student_slug, lesson, answers, score, submitted, updated_at)
  values (s.name, s.slug, p_lesson, coalesce(p_answers,'{}'::jsonb), p_score, coalesce(p_submitted,false), t)
  on conflict (student_slug, lesson) do update
    set answers = excluded.answers, score = excluded.score,
        submitted = public.homework_answers.submitted or excluded.submitted, updated_at = t;
  return t;
end $$;

create or replace function public.get_my_hw(p_code text, p_lesson text)
returns table(name text, answers jsonb, submitted boolean, teacher_comment text)
language sql security definer set search_path = public as $$
  select s.name, h.answers, h.submitted, h.teacher_comment
  from public.students s left join public.homework_answers h on h.student_slug = s.slug and h.lesson = p_lesson
  where s.code = p_code;
$$;

create or replace function public.get_my_progress(p_code text)
returns table(lesson text, submitted boolean, score jsonb, has_comment boolean)
language sql security definer set search_path = public as $$
  select h.lesson, h.submitted, h.score, h.teacher_comment is not null
  from public.homework_answers h join public.students s on s.slug = h.student_slug
  where s.code = p_code;
$$;

-- ===== admin functions (by admin key) =====
create or replace function public.is_admin(p_key text) returns boolean
language sql security definer set search_path = public as $$
  select exists(select 1 from public.admin_keys where key = p_key);
$$;

create or replace function public.admin_students(p_key text)
returns table(slug text, name text, level text, track text, code text)
language plpgsql security definer set search_path = public as $$
begin
  if not public.is_admin(p_key) then raise exception 'not allowed'; end if;
  return query select s.slug, s.name, s.level, s.track, s.code from public.students s order by s.level, s.name;
end $$;

create or replace function public.admin_overview(p_key text)
returns table(slug text, lesson text, submitted boolean, score jsonb, updated_at timestamptz, has_comment boolean)
language plpgsql security definer set search_path = public as $$
begin
  if not public.is_admin(p_key) then raise exception 'not allowed'; end if;
  return query select h.student_slug, h.lesson, h.submitted, h.score, h.updated_at, h.teacher_comment is not null
  from public.homework_answers h where h.student_slug is not null;
end $$;

create or replace function public.admin_get(p_key text, p_slug text, p_lesson text)
returns table(answers jsonb, score jsonb, submitted boolean, updated_at timestamptz, teacher_comment text)
language plpgsql security definer set search_path = public as $$
begin
  if not public.is_admin(p_key) then raise exception 'not allowed'; end if;
  return query select h.answers, h.score, h.submitted, h.updated_at, h.teacher_comment
  from public.homework_answers h where h.student_slug = p_slug and h.lesson = p_lesson;
end $$;

create or replace function public.admin_comment(p_key text, p_slug text, p_lesson text, p_comment text)
returns void language plpgsql security definer set search_path = public as $$
begin
  if not public.is_admin(p_key) then raise exception 'not allowed'; end if;
  update public.homework_answers set teacher_comment = nullif(p_comment,''), comment_at = now()
  where student_slug = p_slug and lesson = p_lesson;
end $$;

create or replace function public.admin_add_student(p_key text, p_slug text, p_name text, p_level text, p_track text)
returns text language plpgsql security definer set search_path = public as $$
declare c text;
begin
  if not public.is_admin(p_key) then raise exception 'not allowed'; end if;
  insert into public.students(slug, name, level, track) values (lower(p_slug), p_name, p_level, coalesce(nullif(p_track,''),'all'))
  on conflict (slug) do update set name = excluded.name, level = excluded.level, track = excluded.track
  returning code into c;
  return c;
end $$;

revoke all on function public.is_admin(text) from anon, public;
grant execute on function public.save_hw(text,text,jsonb,jsonb,boolean) to anon;
grant execute on function public.get_my_hw(text,text) to anon;
grant execute on function public.get_my_progress(text) to anon;
grant execute on function public.admin_students(text) to anon;
grant execute on function public.admin_overview(text) to anon;
grant execute on function public.admin_get(text,text,text) to anon;
grant execute on function public.admin_comment(text,text,text,text) to anon;
grant execute on function public.admin_add_student(text,text,text,text,text) to anon;

-- data
insert into public.admin_keys(key) values ('__ADMIN_KEY__') on conflict do nothing;
insert into public.students(slug, name, level, track, code) values ('larysa','Larysa','A2+','all','__LARYSA_CODE__')
  on conflict (slug) do nothing;
update public.homework_answers set student_slug = 'larysa' where student_slug is null and lower(student) = 'larysa';
