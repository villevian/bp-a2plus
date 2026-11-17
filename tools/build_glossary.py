"""Glossary page (updated 2026), by unit and lesson: word, part of speech, UA translation, meaning, collocations, example, word family (toggle), 🔊.
Usage: python3 build_glossary.py OUT.html [glossary_module] [LEVEL] [ACC] [ACC2] [DARK]
   e.g. python3 build_glossary.py ../glossary.html glossary_a2p A2+ "#3fa9ad" "#e6f4f4" "#2b8185"
"""
import sys, json, importlib
OUT = sys.argv[1]; MOD = sys.argv[2] if len(sys.argv) > 2 else "glossary_a2p"; LVL = sys.argv[3] if len(sys.argv) > 3 else "A2+"
ACC, ACC2, DARK = (sys.argv[4:7] + ["#3fa9ad", "#e6f4f4", "#2b8185"][len(sys.argv[4:7]):])[:3]
G = importlib.import_module(MOD).UNITS
data = [{"u": u, "ut": ut, "lessons": [{"n": n, "t": t, "w": [dict(zip(["en", "pos", "uk", "df", "ex", "co", "fam", "new"], e)) for e in items]} for n, t, items in ls]} for u, ut, ls in G]
total = sum(len(l["w"]) for u in data for l in u["lessons"])
HTML = r"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Business Partner __LVL__ — Glossary</title>
<link href="https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&display=swap" rel="stylesheet"><style>
*{box-sizing:border-box}body{margin:0;font-family:"Fira Sans",system-ui,sans-serif;color:#231f20;background:#fff;font-weight:300;line-height:1.45}
header{display:flex;border-bottom:3px solid __ACC__}header .n{background:linear-gradient(120deg,__DARK__,__ACC__);color:#fff;font-weight:500;font-size:30px;padding:12px 22px}
header h1{margin:0;align-self:center;padding-left:18px;font-weight:500;font-size:26px;color:#4d4d4f}header .c{margin-left:auto;align-self:center;margin-right:18px;font-size:14px;color:#77787b}
main{max-width:1060px;margin:0 auto;padding:14px 22px 40px}.top a{color:__DARK__;font-weight:500;text-decoration:none;font-size:15px}
.bar{position:sticky;top:0;background:#fff;z-index:5;padding:10px 0;border-bottom:1px solid #eee;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.bar select,.bar input[type=search]{font:inherit;font-size:15px;padding:6px 10px;border:1.5px solid #c8c9cb;border-radius:6px}.bar input[type=search]{flex:1;min-width:180px}
.bar label{font-size:14.5px;background:__ACC2__;padding:5px 10px;border-radius:14px;cursor:pointer;user-select:none}.bar label input{margin-right:5px}
.ls{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0}.ls button{font:inherit;font-size:14px;font-weight:500;border:1.5px solid __ACC__;background:#fff;color:__DARK__;padding:4px 12px;border-radius:16px;cursor:pointer}.ls button.on{background:__ACC__;color:#fff}
h2{font-weight:500;font-size:22px;margin:26px 0 4px;color:#4d4d4f;border-bottom:2px solid __ACC__;padding-bottom:4px}h3{font-weight:600;font-size:16px;color:__DARK__;margin:18px 0 6px;text-transform:uppercase;letter-spacing:.3px}
.e{display:grid;grid-template-columns:230px 1fr;gap:4px 18px;padding:10px 4px;border-bottom:1px solid #eee}.e:hover{background:#fafbfb}
.hw{font-weight:500;font-size:18px}.hw .p{font-weight:300;font-style:italic;color:#8a8b8d;font-size:14px;margin-left:4px}.hw .nw{font-size:11px;font-weight:600;background:#fff3c7;color:#7a5a00;border-radius:8px;padding:1px 6px;margin-left:6px;vertical-align:middle}
.uk{color:__DARK__;font-size:15.5px;margin-top:2px}.df{font-size:15.5px}.co{margin:3px 0}.co span{display:inline-block;background:__ACC2__;border-radius:10px;padding:1px 9px;margin:2px 3px 2px 0;font-size:14px}
.ex{font-style:italic;color:#4d4d4f;font-size:15px}.fam{font-size:14.5px;color:#6b2a8c;margin-top:2px}.fam:before{content:"word family: ";color:#8a8b8d}
.sp{border:0;background:none;cursor:pointer;font-size:15px;padding:0 4px}body.nouk .uk{display:none}body.nofam .fam{display:none}
.empty{color:#8a8b8d;padding:20px 0}footer{max-width:1060px;margin:0 auto;padding:0 22px 30px;font-size:12px;color:#77787b}
@media(max-width:700px){.e{grid-template-columns:1fr}}@media print{.bar,.ls,.top,.sp{display:none}.e{break-inside:avoid}}
</style></head><body>
<header><div class="n">__LVL__</div><h1>Glossary · updated 2026</h1><div class="c">__TOTAL__ words</div></header>
<main><div class="top"><a href="index.html">← Contents</a></div>
<div class="bar"><select id="u"></select><input type="search" id="q" placeholder="🔍 search a word or translation">
<label><input type="checkbox" id="tuk" checked>UA translation</label><label><input type="checkbox" id="tfam" checked>word families</label><label><input type="checkbox" id="tnew">only new 2026 words</label></div>
<div class="ls" id="ls"></div><div id="out"></div></main>
<footer><span class="nw" style="background:#fff3c7;color:#7a5a00;border-radius:8px;padding:1px 6px;font-weight:600">NEW</span> = word from the updated (2026) lessons, not in the coursebook glossary. Click 🔊 to listen. Valentyna Hordiienko · Middle Learning Architect</footer>
<script>
const D=__DATA__;let L="all";
function say(t){try{speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(t);u.lang="en-GB";u.rate=.9;const v=speechSynthesis.getVoices().find(x=>/^en/i.test(x.lang));if(v)u.voice=v;speechSynthesis.speak(u)}catch(e){}}
const esc=s=>s.replace(/'/g,"\\'");
function initU(){const s=document.getElementById("u");s.innerHTML=D.map((u,i)=>`<option value="${i}">Unit ${u.u} · ${u.ut}</option>`).join("");let h=(location.hash||"").replace("#unit-","");const i=D.findIndex(u=>u.u===h);if(i>=0)s.value=i}
function lessons(){const u=D[+document.getElementById("u").value];document.getElementById("ls").innerHTML=`<button data-l="all" class="${L==="all"?"on":""}">All lessons</button>`+u.lessons.map(l=>`<button data-l="${l.n}" class="${L===l.n?"on":""}">${l.n} ${l.t}</button>`).join("");
 document.querySelectorAll("#ls button").forEach(b=>b.onclick=()=>{L=b.dataset.l;render()})}
function render(){lessons();const u=D[+document.getElementById("u").value],q=document.getElementById("q").value.trim().toLowerCase(),nw=document.getElementById("tnew").checked;let h=`<h2>Unit ${u.u} · ${u.ut}</h2>`,n=0;
 u.lessons.forEach(l=>{if(L!=="all"&&L!==l.n)return;const ws=l.w.filter(w=>(!nw||w.new)&&(!q||(w.en+" "+w.uk+" "+w.co.join(" ")).toLowerCase().includes(q)));if(!ws.length)return;n+=ws.length;
  h+=`<h3>${l.n} ${l.t}</h3>`+ws.map(w=>`<div class="e"><div><div class="hw">${w.en}<span class="p">${w.pos}</span>${w.new?'<span class="nw">NEW</span>':""} <button class="sp" onclick="say('${esc(w.en)}')">🔊</button></div><div class="uk">${w.uk}</div></div>`+
  `<div><div class="df">${w.df}</div><div class="co">${w.co.map(c=>"<span>"+c+"</span>").join("")}</div><div class="ex">${w.ex} <button class="sp" onclick="say('${esc(w.ex)}')">🔊</button></div>${w.fam?`<div class="fam">${w.fam}</div>`:""}</div></div>`).join("")});
 document.getElementById("out").innerHTML=n?h:h+'<p class="empty">No words found.</p>'}
initU();document.getElementById("u").onchange=()=>{L="all";render()};document.getElementById("q").oninput=render;document.getElementById("tnew").onchange=render;
document.getElementById("tuk").onchange=e=>document.body.classList.toggle("nouk",!e.target.checked);document.getElementById("tfam").onchange=e=>document.body.classList.toggle("nofam",!e.target.checked);render();
</script></body></html>"""
h = HTML.replace("__DATA__", json.dumps(data, ensure_ascii=False)).replace("__LVL__", LVL).replace("__TOTAL__", str(total)).replace("__ACC2__", ACC2).replace("__ACC__", ACC).replace("__DARK__", DARK)
open(OUT, "w").write(h); print("ok glossary", total, "words")
