# Tools (generators)

- `build_contents.py` — builds a Contents page.
  - Template A2+: `python3 build_contents.py ../index.html`
  - Other level: `python3 build_contents.py OUT.html cfg_b1` (config module: LEVEL, ACC, ACC2, VARIANTS, U)
  - Student page: `python3 build_contents.py OUT.html cfg_larysa` (adds STUDENT, ASSIGNED {lesson: {track, pages}}, SHOW_ALL)
- `build_hw_1-1.py` + `expl.py` — homework 1.1 (Supabase sync, bilingual feedback)
- `build_extra_1-1.py` — Extra 1.1
- `build_ppc_extra.py` — Present Perfect Continuous block injected into Larysa's Extra
- `base.css` — shared Business Partner style
- `supabase.sql` — table homework_answers (project "Business Partner")

Note: scripts were written in a Claude session; paths inside point to /home/claude/... — adjust when reusing.

## Assignments (homework given to a student)
- Table `student_assignments` (SQL: `supabase_v4_assignments.sql`, already run). The student home page shows them under **Assignments**.
- After Vale approves a homework: `python3 assign.py taras 1.2 flip "Before class 1.2: …" 2026-12-01` (id = `<lesson>-<page>`; due date optional). `--list`, `--remove 1.2-flip`.
- Needs the Supabase token (network secret for api.supabase.com in the "Vale courses" cloud environment).

## Lessons and payments (private students)
- Vale says "урок проведён" / "бонусный урок" / sends payments → `python3 lessons.py done taras "1.2"`, `bonus taras "speaking club"`, `paid taras 8`.
- Same journal as bp-admin (`lesson_log` + `student_cabinet.lessons_left`); the home page shows the count and the last 3 entries (SQL `supabase_v5_lessons.sql`, already run).
- `python3 lessons.py status` — all students; `check` — counts vs journal. A daily scheduled check runs at ~05:00 Europe/Rome.
- No streaks / freezes on student pages (Vale's decision 27.11.2026).

## Student home design
- Default theme is **glass** (`home_glass.py`, spec `drafts/DESIGN-glass.md`). `--theme=classic` = the previous look.
