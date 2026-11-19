"""Teacher hub: one page with every level, student site, Teacher's Book and tool. Usage: python3 build_hub.py OUT.html"""
import sys, html
G = "https://villevian.github.io/"
LEVELS = [
 ("A1", "Business Partner A1", "bp-a1", None, [], False, False, "#e0a12b"),
 ("A2", "Business Partner A2 · IT", "bp-a2", "teacher/", [("1.1", "Daily tasks"), ("1.2", "A work plan"), ("7.2", "Services")], True, False, "#3b7dd8"),
 ("A2+", "Business Partner A2+ · standard business, bleisure", "bp-a2plus", "teacher/", [("1.1", "Business travel"), ("1.2", "Events management")], False, True, "#3fa9ad"),
 ("B1", "Business Partner B1 · IT", "bp-b1", "teacher/", [("4.2", "Back to the office?"), ("4.3", "Managing conversations"), ("4.4", "Building consensus"), ("4.5", "Confirming an order")], True, False, "#e8894a"),
 ("B2", "Business Partner B2 · IT", "bp-b2", "teacher/", [("1.2", "Employee retention"), ("6.1", "Ethical choices")], True, False, "#5b5fc7"),
 ("B2+", "Business Partner B2+ · IT", "bp-b2plus", "teacher/", [("1.1", "Research in tech")], False, False, "#2f9a74"),
 ("B2+ 🧀", "Business Partner B2+ · Zvenyhora (hard cheese)", "bp-zvenyhora", "teacher/", [], False, False, "#b07a2a"),
]
STUDENTS = [
 ("Kate", "B1", "bp-kate", "4.2–4.5", True, False),
 ("Maryna", "A2 (real A1)", "bp-maryna", "1.1, 1.2", True, False),
 ("Pavlo", "A2 · IT", "bp-pavlo", "7.2", True, False),
 ("Larysa", "A2+", "bp-larysa", "1.1, 1.2 (+ Before class)", True, True),
 ("Violeta", "B2", "bp-violeta", "6.1", True, False),
 ("Daria", "B2", "bp-daria", "1.2, 6.1", True, False),
]
GE = [("Anna", "General English B1", "ge-anna", "Gerund vs infinitive: Reddit drama"), ("Yana", "General English B2+", "ge-yana", "Pet peeves (+ extra homework)")]
OTHER = [("Outcomes Elementary (A1)", G + "outcomes-elementary-course/", "Interactive Outcomes materials, Unit 8"),
         ("Français A1", G + "francais-A1/", "French classroom tool"),
         ("B2 Unit 6 plan", "https://claude.ai/artifact/MctrHNzzRTjr5xortL5tM4", "Topics and changes for Unit 6")]

def a(href, txt, cls="b"): return '<a class="%s" href="%s" target="_blank">%s</a>' % (cls, href, txt)
cards = ""
for code, name, repo, tb, ready, vocab, gloss, col in LEVELS:
    base = G + repo + "/"
    links = a(base, "📚 Contents") + (a(base + tb, "📗 Teacher’s Book") if tb else "") + (a(base + "vocab.html", "🔤 Vocabulary") if vocab else "") + (a(base + "glossary.html", "📖 Glossary") if gloss else "")
    rd = "".join('<span class="chip">%s %s</span>' % (n, t) for n, t in ready) or '<span class="none">no lessons ready yet</span>'
    cards += ('<div class="card" style="--c:%s" data-s="%s"><div class="lv">%s</div><div class="bd"><h3>%s</h3><div class="ln">%s</div><div class="rd"><small>Ready:</small> %s</div></div></div>'
              % (col, html.escape((code + " " + name + " " + repo + " " + " ".join(t for _, t in ready)).lower()), code, name, links, rd))
studs = ""
for nm, lv, repo, rd, vocab, gloss in STUDENTS:
    base = G + repo + "/"
    links = a(base, "🏠 Site") + (a(base + "vocab.html", "🔤 Vocabulary") if vocab else "") + (a(base + "glossary.html", "📖 Glossary") if gloss else "") + a(G + "bp-admin/#s/" + repo[3:], "📊 Answers")
    studs += '<div class="st" data-s="%s"><div><b>%s</b> <span class="tag">%s</span><br><small>Open: %s</small></div><div class="ln">%s</div></div>' % (html.escape((nm + " " + lv + " " + rd).lower()), nm, lv, rd, links)
ge = "".join('<div class="st" data-s="%s"><div><b>%s</b> <span class="tag">%s</span><br><small>%s</small></div><div class="ln">%s</div></div>' % (
    html.escape((n + " " + l + " " + t).lower()), n, l, t, a(G + r + "/", "🏠 Site")) for n, l, r, t in GE)
oth = "".join('<div class="st" data-s="%s"><div><b>%s</b><br><small>%s</small></div><div class="ln">%s</div></div>' % (html.escape((n + " " + d).lower()), n, d, a(u, "Open")) for n, u, d in OTHER)

page = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Teacher hub — all levels and students</title><link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>*{box-sizing:border-box}body{margin:0;font-family:"Fira Sans",system-ui,sans-serif;font-weight:300;color:#231f20;background:#f7f8fa}
header{background:#fff;border-bottom:3px solid #5b5fc7;padding:18px 24px;display:flex;flex-wrap:wrap;gap:14px;align-items:center}header h1{margin:0;font-weight:500;font-size:26px;color:#4d4d4f}header h1 span{color:#5b5fc7}
header input{margin-left:auto;font:inherit;font-size:16px;padding:8px 14px;border:1.5px solid #c8c9cb;border-radius:20px;min-width:260px}
main{max-width:1100px;margin:0 auto;padding:10px 20px 50px}h2{font-weight:500;color:#4044a8;margin:26px 0 10px;font-size:20px}
.top{display:flex;flex-wrap:wrap;gap:10px;margin-top:16px}.top a{background:#5b5fc7;color:#fff;text-decoration:none;border-radius:8px;padding:10px 16px;font-weight:500}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:12px}
.card{display:flex;background:#fff;border:1px solid #e1e3e8;border-radius:10px;overflow:hidden}.card .lv{background:var(--c);color:#fff;font-weight:600;font-size:22px;min-width:78px;display:flex;align-items:center;justify-content:center;padding:6px;text-align:center}
.card .bd{padding:10px 14px;flex:1}.card h3{margin:0 0 6px;font-size:16px;font-weight:500}.ln{display:flex;flex-wrap:wrap;gap:6px}
a.b{text-decoration:none;color:#4044a8;border:1.5px solid #d9dbf5;background:#f6f6fe;border-radius:6px;padding:4px 10px;font-size:14px;font-weight:500}a.b:hover{background:#e8e9fa}
.rd{margin-top:8px;font-size:13px}.chip{display:inline-block;background:#eef0f3;border-radius:12px;padding:2px 9px;margin:2px 2px 0 0}.none{color:#999}
.st{display:flex;flex-wrap:wrap;gap:10px;justify-content:space-between;align-items:center;background:#fff;border:1px solid #e1e3e8;border-radius:10px;padding:10px 14px;margin-bottom:8px}
.tag{background:#e8e9fa;color:#4044a8;border-radius:10px;padding:1px 8px;font-size:13px;font-weight:500}small{color:#777}
footer{text-align:center;color:#999;font-size:13px;padding:20px}.hide{display:none!important}</style></head><body>
<header><h1>Teacher hub · <span>all levels &amp; students</span></h1><input id="q" placeholder="🔍 Search: Daria, B2, retention…" oninput="flt()"></header>
<main><div class="top"><a href="__G__bp-admin/" target="_blank">📊 Admin — answers &amp; comments</a></div>
<h2>Business Partner — levels (templates)</h2><div class="grid">__CARDS__</div>
<h2>Business Partner — students</h2>__STUDS__
<h2>General English — students</h2>__GE__
<h2>Other courses and plans</h2>__OTH__</main>
<footer>Valentyna Hordiienko · Middle Learning Architect</footer>
<script>function flt(){const q=document.getElementById("q").value.trim().toLowerCase();document.querySelectorAll("[data-s]").forEach(e=>e.classList.toggle("hide",q&&!e.dataset.s.includes(q)))}</script>
</body></html>"""
page = page.replace("__G__", G).replace("__CARDS__", cards).replace("__STUDS__", studs).replace("__GE__", ge).replace("__OTH__", oth)
open(sys.argv[1], "w").write(page); print("ok", len(page))
