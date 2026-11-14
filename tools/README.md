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
