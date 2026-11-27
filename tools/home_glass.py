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
/* ===== Liquid Glass · crisp lines — spec: drafts/DESIGN-glass.md =====
   Two materials (as in Apple's Liquid Glass): GLASS for navigation & controls that float above content,
   FROST (almost opaque) for content cards so text always reads. Edges: 1px hairline + brighter top edge.
   Radii are concentric: inner = outer − padding. Spacing on an 8px grid. */
:root{--ink:#11132a;--ink2:#454a66;--mut:#6c7190;--lil:#6d5ce8;--lil2:#efecff;
 --hair:rgba(17,19,42,.08);--hair2:rgba(17,19,42,.05);
 --frost:rgba(255,255,255,.86);--glass:rgba(255,255,255,.46);
 --edge:linear-gradient(180deg,rgba(255,255,255,.98),rgba(255,255,255,.35) 38%,rgba(17,19,42,.10));
 --r:24px;--r2:16px;--r3:12px;--pad:20px;
 --sh:0 1px 1px rgba(17,19,42,.04),0 6px 20px -6px rgba(17,19,42,.08);
 --sh2:0 1px 1px rgba(17,19,42,.05),0 18px 40px -16px rgba(60,50,150,.22)}
body{background:#f4f4f9;font-feature-settings:"cv11","ss01"}
body:before{content:"";position:fixed;inset:0;z-index:-1;pointer-events:none;
 background:radial-gradient(60% 50% at 90% 0%,#e9e5ff 0,transparent 65%),radial-gradient(50% 45% at 0% 100%,var(--acc2) 0,transparent 65%),linear-gradient(180deg,#fafafd,#f3f3f9)}
.num,.sk .v,.big,.fb b,table.g{font-variant-numeric:tabular-nums}
/* FROST: content cards */
.card,.unit,.pl .dy,.rt div{background:var(--frost)!important;border:1px solid var(--hair)!important;box-shadow:var(--sh),inset 0 1px 0 rgba(255,255,255,.9);
 -webkit-backdrop-filter:blur(24px) saturate(1.3);backdrop-filter:blur(24px) saturate(1.3)}
.card{border-radius:var(--r);padding:var(--pad) calc(var(--pad) + 2px)}
.card h3{color:var(--lil);font-size:11px;letter-spacing:1px;margin-bottom:12px}
/* GLASS: navigation, hero frame, floating badges, controls — gradient edge brightest at the top */
aside,.gf .frame,.fb,.tb,.warn{border:1px solid transparent!important;
 background:linear-gradient(var(--glass),var(--glass)) padding-box,var(--edge) border-box!important;
 -webkit-backdrop-filter:blur(30px) saturate(1.8);backdrop-filter:blur(30px) saturate(1.8);box-shadow:var(--sh2),inset 0 1px 0 rgba(255,255,255,.8)}
.app{grid-template-columns:264px minmax(0,1fr)}
aside{border-radius:28px;margin:16px 0 16px 16px;height:calc(100vh - 32px);top:16px;padding:12px}
.me{padding:8px 8px 16px;border-bottom:1px solid var(--hair2)}.nvsep{background:var(--hair2)}
.av{border-radius:var(--r2);background:var(--ink)}
.nv{border-radius:16px;color:var(--ink2);min-height:44px;padding:8px 12px}        /* 28 − 12 = 16: concentric with the sidebar */
.nv:hover{background:rgba(255,255,255,.55)}
.nv[aria-current="true"]{background:#fff;color:var(--ink);font-weight:600;box-shadow:0 0 0 1px var(--hair),0 2px 6px rgba(17,19,42,.06)}
.nv[aria-current="true"]:after{content:"";width:6px;height:6px;border-radius:50%;background:var(--lil);margin-left:auto}
.tch{background:rgba(255,255,255,.7)!important;border:1px solid var(--hair)!important;border-radius:16px;margin:8px 0 0;box-shadow:none}
.tbtn{background:#fff;border:1px solid var(--hair);border-radius:999px}
main{padding:24px 32px 56px}.top{display:none}
/* controls: capsules, crisp 1px edges */
.btn{border-radius:999px;background:var(--ink);color:#fff;box-shadow:0 1px 0 rgba(255,255,255,.15) inset,0 6px 14px -6px rgba(17,19,42,.45);padding:10px 18px;min-height:44px}
.btn:after{content:"↗";font-weight:500;opacity:.75}
.btn.l{background:rgba(255,255,255,.9);color:var(--ink);border:1px solid var(--hair);box-shadow:0 1px 2px rgba(17,19,42,.05)}
.btn.l:after{content:none}.btn.l:hover{background:#fff;border-color:rgba(17,19,42,.16);color:var(--ink)}
:focus-visible{outline:2px solid var(--lil);outline-offset:2px}
.pill{border-radius:999px;padding:2px 10px;box-shadow:inset 0 0 0 1px rgba(17,19,42,.04)}
.bar{background:rgba(17,19,42,.06);height:6px;border-radius:999px}.bar i{background:var(--lil);border-radius:999px}
h2.sec{font-size:22px;letter-spacing:-.4px;margin:40px 0 16px;padding-bottom:12px;border-bottom:1px solid var(--hair)}
h2.sec[data-e]:before{content:attr(data-e);display:block;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--lil);font-weight:600;margin-bottom:4px}
.stats,.pg4,.pg2,.mid{gap:16px}.stats{margin-bottom:16px}
.mid{grid-template-columns:minmax(0,1fr)}.mid>div:first-child{display:none}
.stats{grid-template-columns:repeat(3,minmax(0,1fr))!important}.stats>.card:first-child{display:none}
.hw{border-top:1px solid var(--hair2)}
.uh .ub,.ls .l .ln{background:#fff;color:var(--lil);box-shadow:0 0 0 1px var(--hair)}
.ls{border-top:1px solid var(--hair2)}.ls .l{border-top:1px solid var(--hair2)}
.ls .l .pg a{background:#fff;border-radius:999px;border:1px solid var(--hair)}
.pl .dy{border-radius:var(--r2)}.pl .dy.td{background:#fff!important;box-shadow:0 0 0 2px var(--lil)}
.rt div{border-radius:var(--r2)}.rt div.now{background:#fff!important;box-shadow:0 0 0 2px var(--lil2)}.rt div.now,.rt div.now b{color:var(--ink)}
.q{background:var(--lil2);color:var(--ink);border-radius:var(--r3)}
.bd span{background:rgba(17,19,42,.08)}.bd span.on{background:var(--lil)}
#speakCard polyline{stroke:var(--lil)!important}#speakCard circle{stroke:var(--lil)!important}#speakCard circle:last-of-type{fill:var(--lil)!important}
.warn{border-radius:999px;color:var(--ink2);text-align:center}
.tb{background:linear-gradient(rgba(17,19,42,.86),rgba(17,19,42,.86)) padding-box,var(--edge) border-box!important;border-radius:var(--r2)}
.modal{background:rgba(255,255,255,.92);-webkit-backdrop-filter:blur(30px);backdrop-filter:blur(30px);border:1px solid var(--hair);border-radius:28px}
input,select{background:#fff;border:1px solid var(--hair);border-radius:var(--r3)}
/* hero: next step first (actionable), then plan for the week */
.gh{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:32px;align-items:center;margin-bottom:16px;padding:32px;border-radius:32px;
 background:var(--frost);border:1px solid var(--hair);box-shadow:var(--sh),inset 0 1px 0 #fff;-webkit-backdrop-filter:blur(24px);backdrop-filter:blur(24px)}
.gh .eb{font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--lil);font-weight:600}
.gh h1{margin:8px 0 4px;font-size:44px;line-height:1.05;letter-spacing:-1.6px;color:var(--ink)}
.gh h2{margin:0 0 8px;font-size:22px;letter-spacing:-.5px;color:var(--lil);font-weight:600}
.gh p{margin:0 0 20px;color:var(--ink2);max-width:460px}
.gh .ns{display:flex;align-items:center;gap:12px;padding:12px 12px 12px 16px;border-radius:20px;background:#fff;border:1px solid var(--hair);margin-bottom:16px;max-width:520px}
.gh .ns small{display:block;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:var(--mut);font-weight:600}
.gh .ns b{display:block;font-weight:600;line-height:1.3}.gh .ns .btn{margin-left:auto;flex:none}
.gh .bs{display:flex;flex-wrap:wrap;gap:8px}
.wk7{display:flex;gap:6px;margin-top:20px;padding-top:16px;border-top:1px solid var(--hair2);flex-wrap:wrap;align-items:center}
.wk7 span{width:40px;text-align:center;padding:6px 0;border-radius:var(--r3);font-size:12px;color:var(--mut);border:1px solid transparent}
.wk7 span b{display:block;font-size:14px;color:var(--ink2)}
.wk7 span.on{border-color:var(--hair);background:#fff}.wk7 span.on b{color:var(--ink)}
.wk7 span.td{border-color:var(--lil);box-shadow:0 0 0 1px var(--lil)}
.wk7 em{font-style:normal;font-size:13px;color:var(--mut);margin-left:8px}
.gh .note{margin-top:16px;background:var(--lil2);border-radius:var(--r2);padding:12px 16px;font-size:13.5px;color:var(--ink)}
.gf{position:relative;display:flex;align-items:center;justify-content:center;padding:16px}
.gf .frame{position:relative;width:100%;max-width:420px;border-radius:32px;padding:16px;overflow:hidden}
.gf .frame:before{content:"";position:absolute;inset:0;pointer-events:none;border-radius:inherit;   /* specular sheen */
 background:linear-gradient(115deg,rgba(255,255,255,.55) 0,rgba(255,255,255,0) 32%,rgba(255,255,255,0) 70%,rgba(255,255,255,.25))}
.gf svg{width:100%;height:auto;display:block;border-radius:16px}                  /* 32 − 16 = 16 */
.fb{position:absolute;border-radius:20px;padding:10px 14px;font-size:11.5px;color:var(--mut)}
.fb b{display:block;font-size:24px;color:var(--ink);letter-spacing:-.6px;line-height:1.1}
.fb.t{top:0;right:0;text-align:center}.fb.b{bottom:0;right:24px;min-width:150px}.fb.b b{font-size:18px}
.fb svg{width:120px;height:28px;margin-top:4px}
@media(max-width:1060px){.gh{grid-template-columns:1fr}}
@media(max-width:760px){.stats{grid-template-columns:repeat(2,minmax(0,1fr))!important}aside{margin:8px;height:auto;top:8px;border-radius:22px;padding:6px}
 .app{grid-template-columns:minmax(0,1fr)}main{padding:12px 16px 44px}.gh{padding:20px 16px;border-radius:24px;gap:16px}.gh h1{font-size:34px}.gh h2{font-size:19px}
 .gh .ns{flex-wrap:wrap}.gh .ns .btn{margin-left:0;width:100%;justify-content:center}.wk7 span{width:36px}}
@media(prefers-reduced-transparency:reduce){.card,.unit,aside,.gh,.gf .frame,.fb,.tch,.rt div,.pl .dy,.warn{background:#fff!important;-webkit-backdrop-filter:none;backdrop-filter:none}}
@media(prefers-contrast:more){:root{--hair:rgba(17,19,42,.35);--hair2:rgba(17,19,42,.2)}}
</style>'''

# JS: fills the hero (#gh); runs after every render()
JS = r'''
const ILLU=__ILLU__;
function glassHero(){ const el=$("gh"); if(!el)return;
 const cur=OPEN.find(l=>CAB.current_lesson&&String(CAB.current_lesson).startsWith(l.n))||OPEN[OPEN.length-1];
 const h=new Date().getHours(), nx=nextLesson(), P=D.plan||{};
 // lesson days: from the plan, or read from the cabinet text ("Wed, Fri 18:00", "Mon–Thu …")
 const DS=["sun","mon","tue","wed","thu","fri","sat"]; let days=P.days||null;
 if(!days&&CAB.schedule){ const t=String(CAB.schedule).toLowerCase(), r=t.match(/\b(mon|tue|wed|thu|fri|sat|sun)[a-z]*\s*[–-]\s*(mon|tue|wed|thu|fri|sat|sun)/);
  if(r){ days=[]; for(let i=DS.indexOf(r[1]);;i=(i+1)%7){ days.push(i); if(i===DS.indexOf(r[2])||days.length>7)break; } }
  else { const m=t.match(/\b(mon|tue|wed|thu|fri|sat|sun)/g); if(m) days=[...new Set(m.map(x=>DS.indexOf(x)))]; } }
 const next=assignList().find(a=>!a.sent);                                    // the one actionable next step
 const sp=D.progress.speech.slice().sort(byDate).filter(s=>s.wpm), last=sp[sp.length-1];
 const pts=sp.map(s=>s.wpm), lo=Math.min(...pts,100), hi=Math.max(...pts,150);
 const line=pts.length>1?pts.map((v,i)=>(i*(116/(pts.length-1))+2)+","+(26-((v-lo)/(hi-lo))*22)).join(" "):"";
 const rel=d=>{const ms=d-new Date(),d0=new Date();d0.setHours(0,0,0,0);const dd=Math.round((new Date(d).setHours(0,0,0,0)-d0)/864e5);return ms<0?"now":ms<36e5?"in "+Math.max(1,Math.round(ms/6e4))+" min":dd===0?"today":dd===1?"tomorrow":"in "+dd+" days"};
 // this week: Mon..Sun, lesson days from the plan, today outlined
 const now=new Date(), mon=new Date(now); mon.setHours(0,0,0,0); mon.setDate(mon.getDate()-((mon.getDay()+6)%7));
 const wk=[0,1,2,3,4,5,6].map(i=>{const d=new Date(mon);d.setDate(mon.getDate()+i);const isL=(days||[]).includes(d.getDay()),isT=d.toDateString()===now.toDateString();
  return `<span class="${isL?"on":""} ${isT?"td":""}" title="${isL?"Lesson day":""}">${d.toLocaleDateString("en-GB",{weekday:"short"}).slice(0,2)}<b>${d.getDate()}</b></span>`}).join("");
 el.innerHTML=`<div><div class="eb">${h<12?"Good morning":h<18?"Good afternoon":"Good evening"}</div><h1>${esc(first)}</h1>
  ${cur?`<h2>Lesson ${esc(cur.n)} · ${esc(cur.t)}</h2><p>${esc(cur.d)}</p>`:"<p>Your first lesson will appear here.</p>"}
  ${next?`<div class="ns"><div><small>Your next step${next.due?" · due "+fdate(next.due):""}</small><b>${esc(next.title)}</b></div><a class="btn" href="${esc(next.url)}">Start</a></div>`:""}
  ${cur?`<div class="bs">${cur.pages.slice(0,next?3:4).map((p,j)=>`<a class="btn ${next||j?"l":""}" href="${path(cur.n,cur.tr,p)}">${NM[p]||p}</a>`).join("")}<a class="btn l" href="#course">All pages</a></div>`:""}
  ${days||nx||CAB.schedule?`<div class="wk7" aria-label="This week">${days?wk:""}${nx?`<em>Next lesson: <b style="color:var(--ink)">${nx.toLocaleDateString("en-GB",{weekday:"short",day:"numeric",month:"short"})} · ${hm(nx)}</b> · ${rel(nx)}</em>`:CAB.schedule?`<em>Lessons: <b style="color:var(--ink)">${esc(CAB.schedule)}</b></em>`:""}</div>`:""}
  ${CAB.note?`<div class="note">💬 <b>From your teacher:</b> ${esc(CAB.note)}</div>`:""}</div>
  <div class="gf"><div class="frame">${ILLU}</div>
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
