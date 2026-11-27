"""Lessons and payments for private students (what Vale tells the assistant). Writes the same journal as bp-admin
(table lesson_log + student_cabinet.lessons_left), so the student home page shows the new count at once.
Needs the Supabase token (network secret for api.supabase.com, cloud environment "Vale courses").

  python3 lessons.py paid  taras 8 "8 lessons · 2026-11-27"   # payment: +8 lessons
  python3 lessons.py done  taras ["1.2 Career advice"] [--at 2026-11-30]   # lesson given: −1
  python3 lessons.py bonus taras ["free extra lesson"] [--at …]            # bonus lesson: count unchanged
  python3 lessons.py fix   taras -1 "correction"                           # manual correction
  python3 lessons.py status                                                 # every student: left, last lesson, last payment
  python3 lessons.py daily                                                  # morning report: lessons left ≤ 1, mismatches, overdue, sent in 24 h
  python3 lessons.py check                                                  # left == sum of the journal? (prints differences)
"""
import sys, json, urllib.request
PROJECT = "zuegojpfhgigsvyrnymt"

def sql(q):
    req = urllib.request.Request("https://api.supabase.com/v1/projects/%s/database/query" % PROJECT, data=json.dumps({"query": q}).encode(),
                                 headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r: return json.loads(r.read() or b"null")

TX = "%s"   # set to "begin; %s; rollback;" to try a command without saving

def lit(v): return "null" if v in (None, "") else "$q$%s$q$" % str(v).replace("$q$", "")

def log(slug, kind, delta, note, at=None):
    r = sql(TX % ("""insert into public.student_cabinet(slug) select slug from public.students where slug = %(s)s on conflict (slug) do nothing;
      with s as (select slug from public.students where slug = %(s)s),
      u as (update public.student_cabinet set lessons_left = coalesce(lessons_left,0) + %(d)d, updated_at = now() where slug = (select slug from s) returning lessons_left)
      insert into public.lesson_log(slug, kind, delta, note, at) select slug, %(k)s, %(d)d, %(n)s, coalesce(%(a)s::timestamptz, now()) from s
      returning (select lessons_left from u) as left_now""" % {"s": lit(slug), "k": lit(kind), "d": delta, "n": lit(note), "a": lit(at)}))
    if not r: sys.exit("unknown student: " + slug)
    print("%s %s %+d → lessons left: %s" % (slug, kind, delta, r[0]["left_now"]))

if __name__ == "__main__":
    a = sys.argv[1:]; at = None
    if "--at" in a: i = a.index("--at"); at = a[i + 1]; del a[i:i + 2]
    if not a: sys.exit(__doc__)
    cmd = a[0]
    if cmd == "paid":  log(a[1], "paid", int(a[2]), a[3] if len(a) > 3 else "", at)
    elif cmd == "done": log(a[1], "done", -1, a[2] if len(a) > 2 else "", at)
    elif cmd == "bonus": log(a[1], "bonus", 0, a[2] if len(a) > 2 else "bonus lesson", at)
    elif cmd == "fix": log(a[1], "fix", int(a[2]), a[3] if len(a) > 3 else "correction", at)
    elif cmd == "status":
        for r in sql("""select s.slug, s.name, c.lessons_left, coalesce(c.payment,'private') as payment,
              (select max(at)::date from public.lesson_log l where l.slug=s.slug and l.kind in ('done','bonus')) as last_lesson,
              (select max(at)::date from public.lesson_log l where l.slug=s.slug and l.kind='paid') as last_paid
              from public.students s left join public.student_cabinet c on c.slug=s.slug order by s.slug"""):
            print("%-15s %-8s left %-5s last lesson %-10s last payment %s" % (r["slug"], r["payment"], r["lessons_left"], r["last_lesson"], r["last_paid"]))
    elif cmd == "check":
        bad = sql("""select c.slug, c.lessons_left, coalesce(sum(l.delta),0) as journal from public.student_cabinet c
              left join public.lesson_log l on l.slug=c.slug group by c.slug, c.lessons_left
              having c.lessons_left is distinct from coalesce(sum(l.delta),0) and (c.lessons_left is not null or count(l.*) > 0)""")
        print("all counts match the journal" if not bad else json.dumps(bad, indent=1))
    elif cmd == "daily":   # morning report (scheduled task); also keeps the free Supabase project awake
        low = sql("""select s.name, c.lessons_left from public.students s join public.student_cabinet c on c.slug=s.slug
              where coalesce(c.payment,'private')='private' and c.lessons_left is not null and c.lessons_left <= 1 order by c.lessons_left, s.name""")
        bad = sql("""select c.slug from public.student_cabinet c left join public.lesson_log l on l.slug=c.slug group by c.slug, c.lessons_left
              having c.lessons_left is distinct from coalesce(sum(l.delta),0) and (c.lessons_left is not null or count(l.*) > 0)""")
        late = sql("""select s.name, a.title, a.due from public.student_assignments a join public.students s on s.slug=a.student_slug
              where a.due < current_date and not exists (select 1 from public.homework_answers h where h.student_slug=a.student_slug and h.submitted
                and h.lesson ilike '%' || a.lesson || '%' and h.lesson ilike '%' || (case a.page when 'flip' then 'Before class' when 'hw' then 'Homework' when 'words' then 'Video words'
                when 'clean' then 'Clean' when 'extra' then 'Extra' when 'speak' then 'Speaking' else 'Lesson' end) || '%') order by a.due""")
        new = sql("""select s.name, h.lesson from public.homework_answers h join public.students s on s.slug=h.student_slug
              where h.submitted and h.updated_at > now() - interval '24 hours' and h.lesson not like '%Vocabulary' order by s.name""")
        print("Lessons left ≤ 1:", ", ".join("%s (%s)" % (r["name"], r["lessons_left"]) for r in low) or "nobody")
        print("Counts differ from the journal:", ", ".join(r["slug"] for r in bad) or "none")
        print("Overdue assignments:", "; ".join("%s — %s (due %s)" % (r["name"], r["title"], r["due"]) for r in late) or "none")
        print("Sent in the last 24 h:", "; ".join("%s — %s" % (r["name"], r["lesson"].replace("BP ", "")) for r in new) or "nothing")
    else: sys.exit(__doc__)
