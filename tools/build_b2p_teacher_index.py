"""Teacher's Book contents for B2+: lists lessons, links ready teacher pages (teacher/<n>.html)."""
import sys, os, importlib
OUT = sys.argv[1]; ROOT = os.path.dirname(os.path.abspath(OUT))
cfg = importlib.import_module(sys.argv[2] if len(sys.argv) > 2 else "cfg_b2plus")
CLIENT = getattr(cfg, "CLIENT", None)
rows = ""
for u, title, ls in cfg.U:
    ug = "unit-%s.html" % u
    gl = ' <a class="ug" href="%s">📘 Unit %s guide: логіка уроків і outcomes →</a>' % (ug, u) if os.path.exists(os.path.join(ROOT, ug)) else ""
    rows += '<h2>Unit %s · %s%s</h2><div class="g">' % (u, title, gl)
    for l in ls:
        n, t = l[0], l[1]
        f = n.replace(".", "-").lower() + ".html"
        ok = os.path.exists(os.path.join(ROOT, f))
        rows += ('<a class="c%s" %s><b>%s</b>%s</a>' % ("" if ok else " off", 'href="%s"' % f if ok else "", "Workshop " + n[1:] if n.startswith("W") else n, t.replace("Business workshop: ", "")))
    rows += "</div>"
CUR = "zv" if CLIENT else "it"
VERS = [("it", "IT / PM / marketing", "https://villevian.github.io/bp-b2plus/teacher/index.html"), ("zv", "Zvenyhora · cheese", "https://villevian.github.io/bp-zvenyhora/teacher/index.html")]
SW = '<div class="sw">' + "".join('<span>%s</span>' % n if k == CUR else '<a href="%s">%s</a>' % (u, n) for k, n, u in VERS) + "</div>"
html = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Business Partner B2+ — Teacher’s Book</title><link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>*{box-sizing:border-box}body{margin:0;font-family:"Fira Sans",system-ui,sans-serif;font-weight:300;color:#231f20;background:#fff}
header{display:flex;border-bottom:3px solid #2f9a74}header .n{background:linear-gradient(120deg,#1f7d5c,#4fb58c);color:#fff;font-weight:500;font-size:30px;padding:14px 22px}
header h1{margin:0;align-self:center;padding-left:18px;font-weight:500;font-size:26px;color:#4d4d4f}header .t{margin-left:auto;align-self:center;margin-right:18px;background:#f2b631;color:#3b2c00;font-weight:600;font-size:13px;padding:6px 12px;border-radius:4px}
main{max-width:1100px;margin:0 auto;padding:10px 22px 40px}h2{font-weight:600;font-size:17px;text-transform:uppercase;background:#4d4d4f;color:#fff;padding:7px 14px;margin:22px 0 0}
.g{display:grid;grid-template-columns:repeat(6,1fr);border:1px solid #d5d6d7}.c{padding:10px;border-right:1px solid #d5d6d7;text-decoration:none;color:#231f20;font-size:14px;line-height:1.3;background:#dcf0e6}
.c b{display:block;font-weight:600;color:#1f7d5c}.c.off{background:#fff;color:#b5b6b8}.c.off b{color:#b5b6b8}.top{padding:12px 22px 0;display:flex;flex-wrap:wrap;gap:10px;align-items:center}.sw{margin-left:auto;display:flex;border:1.5px solid #2f9a74;border-radius:20px;overflow:hidden}.sw a,.sw span{padding:4px 14px;font-size:14px}.sw span{background:#2f9a74;color:#fff;font-weight:500}h2 .ug{float:right;color:#fff;font-size:13px;text-transform:none;font-weight:400;text-decoration:underline}.top a{color:#2f9a74;font-weight:500;text-decoration:none}
footer{max-width:1100px;margin:0 auto;padding:0 22px 30px;font-size:12px;color:#77787b}@media(max-width:900px){.g{grid-template-columns:repeat(3,1fr)}}</style></head><body>
<header><div class="n">B2+</div><h1>Business Partner · Teacher’s Book""" + (" · " + CLIENT if CLIENT else "") + """</h1><div class="t">TEACHER</div></header>
<div class="top"><a href="../index.html">← Student Contents</a>""" + SW + """</div><main>""" + rows + """</main><footer>Valentyna Hordiienko · Middle Learning Architect</footer></body></html>"""
open(OUT, "w").write(html); print("ok")
