-- v5: the student sees their own lesson history (lessons done, bonus lessons, payments) on the home page.
-- Records are written by the teacher side (admin_lessons in bp-admin, or tools/lessons.py). Safe to run again.
create or replace function public.get_my_lessons(p_code text) returns jsonb
language sql security definer set search_path = public as $$
  select coalesce(jsonb_agg(jsonb_build_object('kind', l.kind, 'delta', l.delta, 'note', l.note, 'at', l.at) order by l.at desc), '[]'::jsonb)
  from (select l.* from public.lesson_log l join public.students s on s.slug = l.slug where s.code = p_code order by l.at desc limit 12) l;
$$;
revoke all on function public.get_my_lessons(text) from public;
grant execute on function public.get_my_lessons(text) to anon;
