"""'Glass' design theme for the student home page (DESIGN TEMPLATE — not used on student sites yet).
Light frosted glass on a pastel lavender mesh, dark pill buttons, a hero with a business-English illustration in a glass frame
and floating stat badges. Applied by build_student_home.py with --theme=glass.
"""

# Illustration: a video call with colleagues + speech bubbles (inline SVG, no external images)
ILLU = r'''<svg viewBox="0 0 380 330" role="img" aria-label="Illustration: an English video call with colleagues" xmlns="http://www.w3.org/2000/svg">
<defs>
 <linearGradient id="gScr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#eef0ff"/></linearGradient>
 <linearGradient id="gLap" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#d9dcf5"/><stop offset="1" stop-color="#b9bde6"/></linearGradient>
 <linearGradient id="gA" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffd9c7"/><stop offset="1" stop-color="#ffb79a"/></linearGradient>
 <linearGradient id="gB" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#d7d2ff"/><stop offset="1" stop-color="#b3a9ff"/></linearGradient>
 <linearGradient id="gC" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#c9ecff"/><stop offset="1" stop-color="#9fd6f5"/></linearGradient>
 <linearGradient id="gD" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffe0ef"/><stop offset="1" stop-color="#ffbfdc"/></linearGradient>
 <filter id="fs" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="8" stdDeviation="9" flood-color="#5b55b8" flood-opacity=".16"/></filter>
</defs>
<ellipse cx="190" cy="300" rx="150" ry="14" fill="#7c74d9" opacity=".10"/>
<g filter="url(#fs)">
 <rect x="52" y="48" width="276" height="182" rx="16" fill="url(#gLap)"/>
 <rect x="62" y="58" width="256" height="162" rx="10" fill="url(#gScr)"/>
 <path d="M30 236 h320 l-18 30 H48 z" fill="url(#gLap)"/><rect x="160" y="240" width="60" height="6" rx="3" fill="#a9addc"/>
</g>
<g>
 <rect x="72" y="68" width="114" height="66" rx="9" fill="url(#gA)"/><circle cx="129" cy="94" r="13" fill="#fff" opacity=".9"/><rect x="108" y="111" width="42" height="15" rx="7.5" fill="#fff" opacity=".9"/>
 <rect x="194" y="68" width="114" height="66" rx="9" fill="url(#gB)"/><circle cx="251" cy="94" r="13" fill="#fff" opacity=".9"/><rect x="230" y="111" width="42" height="15" rx="7.5" fill="#fff" opacity=".9"/>
 <rect x="72" y="142" width="114" height="66" rx="9" fill="url(#gC)"/><circle cx="129" cy="168" r="13" fill="#fff" opacity=".9"/><rect x="108" y="185" width="42" height="15" rx="7.5" fill="#fff" opacity=".9"/>
 <rect x="194" y="142" width="114" height="66" rx="9" fill="url(#gD)"/><circle cx="251" cy="168" r="13" fill="#fff" opacity=".9"/><rect x="230" y="185" width="42" height="15" rx="7.5" fill="#fff" opacity=".9"/>
 <rect x="76" y="72" width="30" height="12" rx="6" fill="#fff" opacity=".85"/><text x="91" y="81" font-size="8" font-family="Inter,system-ui,sans-serif" font-weight="700" fill="#e0603a" text-anchor="middle">YOU</text>
</g>
<g filter="url(#fs)" font-family="Inter,system-ui,sans-serif">
 <rect x="8" y="14" width="150" height="40" rx="14" fill="#fff"/><path d="M40 54 l10 12 l6 -12z" fill="#fff"/>
 <text x="22" y="39" font-size="13" font-weight="600" fill="#1b2235">Let’s sync on Monday</text>
 <rect x="6" y="262" width="136" height="40" rx="14" fill="#14162b"/><path d="M96 262 l8 -12 l6 12z" fill="#14162b"/>
 <text x="22" y="287" font-size="13" font-weight="600" fill="#fff">Sounds great! 👍</text>
</g>
</svg>'''

CSS = r'''
<style id="glass">
:root{--ink:#14162b;--ink2:#4a4f6a;--mut:#757a95;--lil:#7c6cf0;--lil2:#efedff;--line:rgba(255,255,255,.8);
 --glass:rgba(255,255,255,.62);--glass2:rgba(255,255,255,.78);--r:24px;--r2:16px;
 --sh:0 1px 0 rgba(255,255,255,.9) inset,0 12px 40px rgba(70,60,150,.08),0 2px 6px rgba(70,60,150,.04)}
body{background:#f2f1fa}
body:before{content:"";position:fixed;inset:-15%;z-index:-1;pointer-events:none;
 background:radial-gradient(35% 40% at 85% 10%,#e3defd 0,transparent 70%),radial-gradient(40% 45% at 10% 30%,#f8f2ff 0,transparent 70%),
 radial-gradient(35% 40% at 90% 85%,#dfe8ff 0,transparent 70%),radial-gradient(30% 35% at 20% 95%,var(--acc2) 0,transparent 70%),linear-gradient(170deg,#fbfbfe,#f1f0fa)}
body:after{content:"";position:fixed;width:300px;height:300px;right:-80px;bottom:-60px;z-index:-1;pointer-events:none;border-radius:50%;
 background:radial-gradient(circle at 30% 30%,#fff,rgba(214,208,255,.55) 45%,rgba(160,150,255,.25) 70%,transparent 72%);filter:blur(1px)}
.card,.unit,.rt div,.pl .dy,.tch{background:var(--glass)!important;border:1px solid var(--line)!important;box-shadow:var(--sh);
 -webkit-backdrop-filter:blur(20px) saturate(1.4);backdrop-filter:blur(20px) saturate(1.4)}
.card{border-radius:var(--r)}.card h3{color:var(--lil);font-size:11px;letter-spacing:.9px}
.app{grid-template-columns:260px minmax(0,1fr)}
aside{background:var(--glass2);border:1px solid var(--line);border-radius:28px;margin:18px 0 18px 18px;height:calc(100vh - 36px);top:18px;box-shadow:var(--sh);
 -webkit-backdrop-filter:blur(24px) saturate(1.5);backdrop-filter:blur(24px) saturate(1.5)}
.me{border-bottom:1px solid rgba(110,100,190,.12)}.nvsep{background:rgba(110,100,190,.12)}
.av{border-radius:14px;background:var(--ink);box-shadow:0 6px 16px rgba(20,22,43,.25)}
.nv{border-radius:999px;color:var(--ink2)}.nv:hover{background:rgba(255,255,255,.7)}
.nv[aria-current="true"]{background:#fff;color:var(--ink);font-weight:600;box-shadow:0 4px 14px rgba(70,60,150,.10)}
.nv[aria-current="true"]:after{content:"";width:6px;height:6px;border-radius:50%;background:var(--lil);margin-left:auto}
.tch{border-radius:20px;margin:8px 2px 0}.tbtn{background:#fff;border:1px solid var(--line);border-radius:999px}
main{padding-top:28px}
.top{display:none}
.btn{border-radius:999px;background:var(--ink);box-shadow:0 8px 20px rgba(20,22,43,.18);padding:11px 20px}
.btn:after{content:"↗";font-weight:500;opacity:.8}
.btn.l{background:rgba(255,255,255,.85);color:var(--ink);border:1px solid var(--line);box-shadow:0 3px 10px rgba(70,60,150,.06)}
.btn.l:after{content:none}.btn.l:hover{background:#fff;color:var(--ink)}
.pill{border-radius:999px;padding:3px 11px}
.bar{background:rgba(110,100,190,.12);height:8px}
.bar i{background:linear-gradient(90deg,var(--lil),#a99bff 60%,var(--acc));box-shadow:0 0 10px rgba(124,108,240,.35)}
.num,.sk .v{color:var(--ink)}
h2.sec{font-size:24px;letter-spacing:-.5px;margin:30px 0 14px}
h2.sec[data-e]:before{content:attr(data-e);display:block;font-size:11px;letter-spacing:1.1px;text-transform:uppercase;color:var(--lil);font-weight:600;margin-bottom:4px}
.mid{grid-template-columns:minmax(0,1fr)}
.stats{grid-template-columns:repeat(3,minmax(0,1fr))!important}.stats>.card:first-child{display:none}.mid>div:first-child{display:none}
.uh .ub,.ls .l .ln{background:#fff;color:var(--lil);box-shadow:0 4px 12px rgba(70,60,150,.08)}
.uh:hover{background:rgba(255,255,255,.45)}.ls{border-top:1px solid rgba(110,100,190,.1)}.ls .l{border-top:1px solid rgba(110,100,190,.07)}
.ls .l .pg a{background:rgba(255,255,255,.8);border-radius:999px;border:1px solid var(--line)}
.pl .dy{border-radius:18px}.pl .dy.td{background:#fff!important;box-shadow:0 0 0 2px var(--lil2),var(--sh)}
.rt div{border-radius:16px}.rt div.now{background:#fff!important;color:var(--lil)}.rt div.now b{color:var(--ink)}
.q{background:var(--lil2);border:0;color:var(--ink)}
#speakCard polyline{stroke:var(--lil)!important}#speakCard circle{stroke:var(--lil)!important}#speakCard circle:last-of-type{fill:var(--lil)!important}
.bd span{background:rgba(110,100,190,.16)}.bd span.on{background:var(--lil)}
.warn{border-radius:999px;background:rgba(255,255,255,.7);border:1px solid var(--line);color:var(--ink2);-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px);text-align:center}
.tb{background:rgba(20,22,43,.86);border-radius:18px;-webkit-backdrop-filter:blur(14px);backdrop-filter:blur(14px)}
.modal{background:rgba(255,255,255,.9);-webkit-backdrop-filter:blur(24px);backdrop-filter:blur(24px);border:1px solid var(--line);border-radius:26px}
input,select{background:rgba(255,255,255,.8);border-color:rgba(110,100,190,.18);border-radius:12px}
/* hero */
.gh{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:24px;align-items:center;margin-bottom:22px;padding:30px 34px;border-radius:30px;
 background:linear-gradient(135deg,rgba(255,255,255,.8),rgba(255,255,255,.45));border:1px solid var(--line);box-shadow:var(--sh);-webkit-backdrop-filter:blur(20px);backdrop-filter:blur(20px)}
.gh .eb{font-size:12px;letter-spacing:1.2px;text-transform:uppercase;color:var(--lil);font-weight:600}
.gh h1{margin:6px 0 2px;font-size:46px;line-height:1.05;letter-spacing:-1.5px;color:var(--ink)}
.gh h2{margin:0 0 12px;font-size:26px;letter-spacing:-.6px;background:linear-gradient(90deg,var(--lil),#a58bff 55%,var(--acc));-webkit-background-clip:text;background-clip:text;color:transparent}
.gh p{margin:0 0 18px;color:var(--ink2);max-width:460px}
.gh .bs{display:flex;flex-wrap:wrap;gap:10px}
.gh .nl{display:flex;align-items:center;gap:12px;flex-wrap:wrap;margin-top:22px;padding-top:16px;border-top:1px solid rgba(110,100,190,.12);font-size:13.5px;color:var(--mut)}
.gh .nl b{color:var(--ink);font-weight:600}
.gh .note{margin-top:14px;background:var(--lil2);border-radius:16px;padding:10px 14px;font-size:13.5px;color:var(--ink)}
.gf{position:relative;min-height:300px;display:flex;align-items:center;justify-content:center}
.gf .frame{width:100%;max-width:420px;border-radius:34px;padding:18px;background:linear-gradient(160deg,rgba(255,255,255,.85),rgba(236,233,255,.55));
 border:1px solid var(--line);box-shadow:0 30px 60px rgba(70,60,150,.14),inset 0 1px 0 #fff}
.gf svg{width:100%;height:auto;display:block}
.fb{position:absolute;background:rgba(255,255,255,.88);border:1px solid var(--line);border-radius:18px;padding:10px 14px;box-shadow:0 12px 30px rgba(70,60,150,.14);
 -webkit-backdrop-filter:blur(16px);backdrop-filter:blur(16px);font-size:11.5px;color:var(--mut)}
.fb b{display:block;font-size:26px;color:var(--ink);letter-spacing:-.8px;line-height:1.1}
.fb.t{top:-6px;right:-6px;text-align:center}.fb.b{bottom:-10px;right:10px;min-width:150px}.fb.b b{font-size:18px}
.fb svg{width:120px;height:28px;margin-top:4px}
.spark{position:absolute;left:-14px;top:44%;width:54px;height:54px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:22px;
 background:radial-gradient(circle at 35% 30%,#fff,rgba(214,208,255,.7));box-shadow:0 10px 26px rgba(124,108,240,.3);color:var(--lil)}
@media(max-width:1060px){.gh{grid-template-columns:1fr}.gf{min-height:0;margin-top:8px}}
@media(max-width:760px){.stats{grid-template-columns:repeat(2,minmax(0,1fr))!important}aside{margin:8px;height:auto;top:8px;border-radius:22px}.app{grid-template-columns:minmax(0,1fr)}main{padding-top:12px}
 .gh{padding:22px 18px;border-radius:24px}.gh h1{font-size:36px}.gh h2{font-size:21px}.fb.t{right:0}.spark{display:none}}
@media(prefers-reduced-transparency:reduce){.card,.unit,aside,.gh,.tch,.rt div,.pl .dy{background:#fff!important;-webkit-backdrop-filter:none;backdrop-filter:none}}
</style>'''

# JS: fills the hero (#gh); runs after every render()
JS = r'''
const ILLU=__ILLU__;
function glassHero(){ const el=$("gh"); if(!el)return;
 const cur=OPEN.find(l=>CAB.current_lesson&&String(CAB.current_lesson).startsWith(l.n))||OPEN[OPEN.length-1];
 const h=new Date().getHours(), nx=nextLesson();
 const sp=D.progress.speech.slice().sort(byDate).filter(s=>s.wpm), last=sp[sp.length-1];
 const pts=sp.map(s=>s.wpm), lo=Math.min(...pts,100), hi=Math.max(...pts,150);
 const line=pts.length>1?pts.map((v,i)=>(i*(116/(pts.length-1))+2)+","+(26-((v-lo)/(hi-lo))*22)).join(" "):"";
 const when=nx?`<span>Next lesson</span><b>${nx.toLocaleDateString("en-GB",{weekday:"long",day:"numeric",month:"short"})} · ${hm(nx)}</b>`:(CAB.schedule?`<span>Lessons</span><b>${esc(CAB.schedule)}</b>`:"");
 el.innerHTML=`<div><div class="eb">${h<12?"Good morning":h<18?"Good afternoon":"Good evening"} 👋</div><h1>${esc(first)}</h1>
  ${cur?`<h2>Lesson ${esc(cur.n)} · ${esc(cur.t)}</h2><p>${esc(cur.d)}</p>
  <div class="bs">${cur.pages.slice(0,3).map((p,j)=>`<a class="btn ${j?"l":""}" href="${path(cur.n,cur.tr,p)}">${NM[p]||p}</a>`).join("")}${cur.pages.length>3?`<a class="btn l" href="#course">All pages · ${cur.pages.length}</a>`:""}</div>`:"<p>Your first lesson will appear here.</p>"}
  ${when?`<div class="nl">${when}${nx?`<span class="pill p-new">${(()=>{const ms=nx-new Date(),d0=new Date();d0.setHours(0,0,0,0);const dd=Math.round((new Date(nx).setHours(0,0,0,0)-d0)/864e5);return ms<0?"now":ms<36e5?"in "+Math.max(1,Math.round(ms/6e4))+" min":dd===0?"today":dd===1?"tomorrow":"in "+dd+" days"})()}</span>`:""}</div>`:""}
  ${CAB.note?`<div class="note">💬 <b>From your teacher:</b> ${esc(CAB.note)}</div>`:""}</div>
  <div class="gf"><div class="frame">${ILLU}</div><div class="spark" aria-hidden="true">✦</div>
   ${CAB.lessons_left!=null&&(CAB.payment||"private")==="private"?`<div class="fb t"><b>${CAB.lessons_left}</b>lessons left</div>`:""}
   ${last?`<div class="fb b">Speaking pace<b>${last.wpm} wpm${pts.length>1?` <span style="font-size:12px;color:var(--ok)">+${last.wpm-pts[0]}</span>`:""}</b>${line?`<svg viewBox="0 0 120 28" aria-hidden="true"><polyline points="${line}" fill="none" style="stroke:var(--lil)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>`:""}</div>`:""}</div>`; }
const _rG=render; render=function(){ _rG(); glassHero(); };
'''

SECTIONS = [  # (markup in the base page, glass version with an eyebrow)
    ('<h2 class="sec" id="progress">📊 My progress</h2>', '<h2 class="sec" id="progress" data-e="Your growth">My progress</h2>'),
    ('<h2 class="sec" id="course">📘 My course</h2>', '<h2 class="sec" id="course" data-e="All units">My course</h2>'),
    ('<h2 class="sec" id="myplan">📆 My plan</h2>', '<h2 class="sec" id="myplan" data-e="This week">My plan</h2>'),
]

def apply(h):
    import json
    h = h.replace("</head>", CSS + "</head>", 1)
    h = h.replace('<div class="warn" id="offline" role="status"></div>', '<section class="gh" id="gh" aria-label="Welcome"></section>\n <div class="warn" id="offline" role="status"></div>', 1)
    h = h.replace("if(D.demo){", JS.replace("__ILLU__", json.dumps(ILLU)) + "if(D.demo){", 1)
    for a, b in SECTIONS:
        assert a in h, a
        h = h.replace(a, b, 1)
    return h
