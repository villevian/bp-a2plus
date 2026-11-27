"""Put an approved homework into a student's Assignments (home page), or remove it.
Needs the Supabase access token as a network secret for api.supabase.com (cloud environment "Vale courses").
Usage:
  python3 assign.py taras 1.2 flip "Before class 1.2: watch the video and take notes" [YYYY-MM-DD due] [url]
  python3 assign.py taras --remove 1.2-flip
  python3 assign.py taras --list
Pages: flip (Before class) · lesson · hw · words · clean · extra · speak · review …  The id is "<lesson>-<page>".
Only after Vale approves the homework ("Подготовь домашку" ≠ "опубликуй").
"""
import sys, json, importlib, urllib.request
PROJECT = "zuegojpfhgigsvyrnymt"

def sql(q):
    req = urllib.request.Request("https://api.supabase.com/v1/projects/%s/database/query" % PROJECT, data=json.dumps({"query": q}).encode(),
                                 headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=60) as r: return json.loads(r.read() or b"null")

def lit(v): return "null" if v in (None, "") else "$q$%s$q$" % v.replace("$q$", "")

if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: sys.exit(__doc__)
    code = importlib.import_module("cfg_" + a[0]).STUDENT["code"]
    slug = "(select slug from public.students where code = %s)" % lit(code)
    if a[1:2] == ["--list"]:
        print(json.dumps(sql("select public.get_my_assignments(%s) as a" % lit(code))[0]["a"], ensure_ascii=False, indent=1))
    elif a[1:2] == ["--remove"]:
        sql("delete from public.student_assignments where student_slug = %s and id = %s" % (slug, lit(a[2]))); print("removed", a[2])
    else:
        lesson, page, title = a[1], a[2], a[3]; due = a[4] if len(a) > 4 else None; url = a[5] if len(a) > 5 else None
        sql("insert into public.student_assignments(student_slug,id,lesson,page,title,url,due) values (%s,%s,%s,%s,%s,%s,%s) "
            "on conflict (student_slug,id) do update set lesson=excluded.lesson,page=excluded.page,title=excluded.title,url=excluded.url,due=excluded.due"
            % (slug, lit(lesson + "-" + page), lit(lesson), lit(page), lit(title), lit(url), lit(due) + ("::date" if due else "")))
        print("assigned", lesson + "-" + page, "to", a[0])
