-- Homework answers for Business Partner lessons
-- Run once in Supabase → SQL Editor

create table if not exists public.homework_answers (
  id          bigint generated always as identity primary key,
  student     text        not null,
  lesson      text        not null,
  answers     jsonb       not null default '{}'::jsonb,
  score       jsonb,
  submitted   boolean     not null default false,
  updated_at  timestamptz not null default now(),
  unique (student, lesson)
);

alter table public.homework_answers enable row level security;

-- The page uses the public anon key: it can read and write rows, but not delete them.
create policy "hw read"   on public.homework_answers for select to anon using (true);
create policy "hw insert" on public.homework_answers for insert to anon with check (true);
create policy "hw update" on public.homework_answers for update to anon using (true) with check (true);

-- Teacher view: latest homework first
-- select student, lesson, submitted, score, updated_at, answers
-- from public.homework_answers order by updated_at desc;
