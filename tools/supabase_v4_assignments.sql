-- v4: Assignments — homework the teacher approved and gave to a student (shown on the student home page).
-- Added by the assistant after Vale approves a homework (tools/assign.py), or by the teacher key from a page later.
-- Safe to run again.

create table if not exists public.student_assignments (
  student_slug text not null references public.students(slug) on delete cascade,
  id text not null,                 -- e.g. '1.1-flip'
  lesson text not null,             -- '1.1', 'W1'
  page text not null,               -- flip | lesson | hw | words | clean | extra | speak | …
  title text not null,
  url text,                         -- optional; by default the page of the lesson on the student's site
  due date,
  assigned_at date not null default current_date,
  primary key (student_slug, id)
);
alter table public.student_assignments enable row level security;
revoke all on public.student_assignments from anon, authenticated;

-- Student (by personal code): read only, newest first
create or replace function public.get_my_assignments(p_code text) returns jsonb
language sql security definer set search_path = public as $$
  select coalesce(jsonb_agg(jsonb_build_object('id', a.id, 'lesson', a.lesson, 'page', a.page, 'title', a.title, 'url', a.url,
                                               'due', a.due, 'assigned', a.assigned_at) order by a.assigned_at desc, a.id), '[]'::jsonb)
  from public.students s join public.student_assignments a on a.student_slug = s.slug
  where s.code = p_code;
$$;

-- Teacher (by key): add / update one assignment, or remove it
create or replace function public.admin_set_assignment(p_key text, p_code text, p_id text, p_lesson text, p_page text, p_title text, p_url text, p_due date)
returns void language plpgsql security definer set search_path = public as $$
declare s public.students;
begin
  if not exists(select 1 from public.admin_keys where key = p_key) then raise exception 'wrong teacher key'; end if;
  select * into s from public.students where code = p_code;
  if s.slug is null then raise exception 'unknown student code'; end if;
  insert into public.student_assignments(student_slug, id, lesson, page, title, url, due)
  values (s.slug, p_id, p_lesson, p_page, p_title, nullif(p_url,''), p_due)
  on conflict (student_slug, id) do update set lesson = excluded.lesson, page = excluded.page, title = excluded.title, url = excluded.url, due = excluded.due;
end $$;
create or replace function public.admin_remove_assignment(p_key text, p_code text, p_id text) returns void
language plpgsql security definer set search_path = public as $$
begin
  if not exists(select 1 from public.admin_keys where key = p_key) then raise exception 'wrong teacher key'; end if;
  delete from public.student_assignments a using public.students s where a.student_slug = s.slug and s.code = p_code and a.id = p_id;
end $$;

revoke all on function public.get_my_assignments(text) from public;
revoke all on function public.admin_set_assignment(text,text,text,text,text,text,text,date) from public;
revoke all on function public.admin_remove_assignment(text,text,text) from public;
grant execute on function public.get_my_assignments(text) to anon;
grant execute on function public.admin_set_assignment(text,text,text,text,text,text,text,date) to anon;
grant execute on function public.admin_remove_assignment(text,text,text) to anon;
