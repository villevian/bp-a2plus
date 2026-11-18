"""Business Partner A2 · 7.2 Services and subscriptions — SPEAKING & GAMES (extra practice of the lesson vocabulary).
1 Talk for a minute (question cards + timer) · 2 Memory: word ↔ translation · 3 Definition race · 4 Unscramble · 5 Fair or hidden? · 6 Taboo · 7 Role-plays
Usage: python3 build_a2_games_7-2.py OUT.html [STUDENT_CODE]
"""
import sys, os, json
from bp_page import page, ta, SELF
from vocab_a2 import lesson
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3b7dd8", "#e3eefb", "#2a5fb0", "#4f9be8"
_, GROUPS = lesson("7.2")
W = [w for g, ws in GROUPS if g != "Services" for w in ws]
K = {}

TALK = ["Which subscriptions do you pay for? Which one is the best value for money?", "Have you ever paid a hidden fee? What happened?",
        "Do you prefer a monthly plan or an annual plan? Why?", "Have you ever forgotten to cancel a free trial?", "What do you think about the Adobe story? Is it fair?",
        "Your favourite app has a price increase of 30%. Do you pay or cancel?", "Which work tools does your company pay for? Do you use all of them?",
        "Do you read the small print? Why? / Why not?", "Should companies show the full price at the start? Why?", "What is the most useless subscription you know?",
        "Is a fixed fee better than paying per user per month? Why?", "How do you cancel a subscription? Is it easy or difficult?"]
s1 = ('<div class="bsec wr">Speaking</div><p class="ins"><b class="x">1</b>Talk for a minute. Take a card, start the timer and answer. Use words from the lesson!</p>'
      '<div class="tcard" id="tq">Click “New card”</div><div class="tbar"><button class="btn" onclick="newQ()">🔀 New card</button>'
      '<button class="btn l" onclick="startT()">⏱ Start 60 s</button><span class="tm" id="tm">60</span></div>'
      '<p class="hint">Useful: I pay … a month · The fee includes … · There’s a hidden fee for … · I think it’s (not) good value for money because …</p>')

s2 = ('<div class="bsec">Game</div><p class="ins"><b class="x">2</b>Memory. Find the pairs: English ↔ Ukrainian. Fewer moves = better!</p>'
      '<div class="tbar"><button class="btn l" onclick="memNew()">🔀 New game</button><span id="mm" class="tm"></span></div><div class="mem" id="mem"></div>')

s3 = ('<div class="bsec">Game</div><p class="ins"><b class="x">3</b>Definition race. Read the meaning and choose the word. 10 questions — how fast are you?</p>'
      '<div class="tbar"><button class="btn" onclick="raceNew()">▶ Start</button><span class="tm" id="rs"></span></div><div id="race"></div>')

s4 = ('<div class="bsec">Game</div><p class="ins"><b class="x">4</b>Unscramble the words. Click the letters in the right order.</p>'
      '<div class="tbar"><button class="btn l" onclick="unsNew()">🔀 New word</button><button class="btn l" onclick="unsHint()">💡 Hint</button><span class="tm" id="us"></span></div>'
      '<div id="uhint" class="hint"></div><div id="uout" class="uout"></div><div id="uletters" class="ulet"></div>')

FAIR = [("The website shows €12 a month. At the end, you see a €3 “service fee”.", "hidden"), ("A course costs €200. The fee includes all videos and a certificate.", "fair"),
        ("You can cancel any time, with no cancellation fee.", "fair"), ("The plan is “€8 a month” — but in the small print, you must stay for 12 months.", "hidden"),
        ("A cheaper plan exists, but you only see it when you try to cancel.", "hidden"), ("Extra storage costs €5 a month. It’s on the pricing page.", "fair"),
        ("A concert ticket is €60. On the last page, they add a €12 booking fee.", "hidden"), ("You pay €80 for the year and save 15%.", "fair")]
s5 = ('<div class="bsec wr">Speaking</div><p class="ins"><b class="x">5</b>Fair or hidden? Decide, then say <b>why</b> in one sentence.</p>' +
      "".join('<div class="fh"><span>%d. %s</span><span><button class="btn l" onclick="fh(this,%d,\'fair\')">👍 fair</button> <button class="btn l" onclick="fh(this,%d,\'hidden\')">🙈 hidden</button></span></div>' % (i + 1, t, i, i) for i, (t, _) in enumerate(FAIR)) +
      '<p class="hint">Say: It’s fair because the price includes … / It’s a hidden fee because they don’t show … at the start.</p>')

TABOO = [("refund", ["money", "back", "return"]), ("free trial", ["free", "days", "try"]), ("cancel", ["stop", "subscription", "end"]), ("small print", ["small", "read", "letters"]),
         ("annual fee", ["year", "pay", "once"]), ("price increase", ["more", "expensive", "up"]), ("booking fee", ["ticket", "hotel", "book"]), ("hidden fee", ["see", "secret", "extra"])]
s6 = ('<div class="bsec wr">Speaking</div><p class="ins"><b class="x">6</b>Taboo. Explain the word to your teacher — but don’t say the word or the taboo words!</p>'
      '<div class="tcard" id="tb">Click “New card”</div><div class="tbar"><button class="btn" onclick="tabNew()">🔀 New card</button><button class="btn l" onclick="startT(\'tt\',45)">⏱ 45 s</button><span class="tm" id="tt">45</span><span class="tm" id="tbs">Points: 0</span><button class="btn l" onclick="tabPt()">✅ Guessed!</button></div>')

RP = [("📞 Price increase", "You use a design tool. The price went up from €10 to €15 a month. Call support.", "Ask: Why did the price go up? Is there a cheaper plan? Is there a cancellation fee? Can I get a refund for this month?",
       "Support agent: the new price includes an AI assistant. There is a ‘Basic’ plan for €9 (no AI). No refunds."),
      ("🧾 Team budget", "Your team pays for 5 tools. You must cut the budget by €100 a month.", "Decide together: Which tools do we really need? Which ones have hidden fees? Which plan is better value for money?",
       "Teacher: you love one of the tools and don’t want to cancel it. Give reasons!"),
      ("🤝 Setup fee", "A software company wants a €500 setup fee. Ask them to remove it.", "Say: We’re happy with the monthly fee, but … · Could you remove …? · If you remove the setup fee, we can sign an annual plan.",
       "Sales manager: you can remove half of the fee if they choose the annual plan.")]
s7 = ('<div class="bsec wr">Speaking</div><p class="ins"><b class="x">7</b>Role-plays. Choose a card. You are A, your teacher is B. Then swap.</p><div class="rps">' +
      "".join('<div class="rp"><div class="rh">%s</div><p>%s</p><p class="hint">%s</p><details><summary>Card B</summary><p>%s</p></details></div>' % r for r in RP) +
      '</div><p class="ins">After the role-play: what did you agree?</p>' + ta("rp", "We agreed to … because …", 60) +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you talk about prices and fees now?"))

DATA = {"w": [{"en": w[0], "uk": w[1], "df": w[2]} for w in W], "talk": TALK, "fair": [a for _, a in FAIR], "taboo": TABOO,
        "uns": ["refund", "booking", "hidden", "cancel", "annual", "monthly", "fixed", "include", "charge", "trial", "increase", "print"]}
XJS = r"""
document.head.insertAdjacentHTML("beforeend",`<style>
.tcard{background:#e3eefb;border-radius:12px;padding:26px 22px;font-size:21px;font-weight:500;text-align:center;min-height:90px;display:flex;align-items:center;justify-content:center;margin:8px 0;color:#1d3c6e}
.tcard small{display:block;font-size:15px;font-weight:400;color:#b3261e;margin-top:8px}.tbar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:8px 0}.tm{font-weight:600;color:#2a5fb0;font-size:17px}
.mem{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:10px 0}.mc{min-height:70px;border-radius:10px;background:#3b7dd8;color:#fff;display:flex;align-items:center;justify-content:center;text-align:center;padding:6px;cursor:pointer;font-size:15px;user-select:none}
.mc.o{background:#fff;color:#231f20;border:2px solid #3b7dd8}.mc.ok{background:#e6f5ea;color:#1e6b35;border:2px solid #5bb974;cursor:default}
.rq{font-size:18px;margin:10px 0}.ro{display:grid;grid-template-columns:1fr 1fr;gap:8px}.ro button{font:inherit;padding:10px;border:1.5px solid #c8c9cb;border-radius:8px;background:#fff;cursor:pointer;text-align:left}
.ro button.y{background:#e6f5ea;border-color:#5bb974}.ro button.n{background:#fdecea;border-color:#e57373}
.uout{font-size:26px;letter-spacing:4px;min-height:40px;font-weight:600;color:#2a5fb0;margin:8px 0}.ulet button{font:inherit;font-size:20px;width:44px;height:44px;margin:3px;border-radius:8px;border:1.5px solid #3b7dd8;background:#fff;cursor:pointer}
.ulet button:disabled{opacity:.25}.fh{display:flex;justify-content:space-between;gap:12px;align-items:center;border-bottom:1px solid #eee;padding:8px 0;flex-wrap:wrap}.fh .y{background:#e6f5ea}.fh .n{background:#fdecea}
.rps{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.rp{border:1px solid #d5d6d7;border-radius:10px;padding:10px 12px;background:#fff}.rp .rh{font-weight:600;color:#2a5fb0;margin-bottom:4px}
@media(max-width:800px){.mem{grid-template-columns:repeat(2,1fr)}.rps,.ro{grid-template-columns:1fr}}</style>`);
const G=__DATA__;const sh=a=>a.map(x=>[Math.random(),x]).sort((a,b)=>a[0]-b[0]).map(x=>x[1]);
let qi=-1,tmr=null;function newQ(){qi=(qi+1)%G.talk.length;if(qi===0)G.talk=sh(G.talk);document.getElementById("tq").textContent=G.talk[qi]}
function startT(id,s){id=id||"tm";s=s||60;clearInterval(tmr);let t=s;const el=document.getElementById(id);el.textContent=t;tmr=setInterval(()=>{t--;el.textContent=t>0?t:"⏰ Time!";if(t<=0)clearInterval(tmr)},1000)}
let mf=[],mv=0,mok=0;function memNew(){const ps=sh(G.w).slice(0,8);const cs=sh(ps.flatMap((w,i)=>[{t:w.en,i},{t:w.uk,i}]));mf=[];mv=0;mok=0;
 document.getElementById("mem").innerHTML=cs.map((c,k)=>`<div class="mc" data-i="${c.i}" data-k="${k}"><span style="visibility:hidden">${c.t}</span></div>`).join("");document.getElementById("mm").textContent="Moves: 0";
 document.querySelectorAll(".mc").forEach(e=>e.onclick=()=>{if(e.classList.contains("ok")||e.classList.contains("o")||mf.length===2)return;e.classList.add("o");e.firstChild.style.visibility="visible";mf.push(e);
  if(mf.length===2){mv++;document.getElementById("mm").textContent="Moves: "+mv;const[a,b]=mf;if(a.dataset.i===b.dataset.i){a.classList.add("ok");b.classList.add("ok");mf=[];mok++;if(mok===8)document.getElementById("mm").textContent="🎉 Done in "+mv+" moves!"}
  else setTimeout(()=>{[a,b].forEach(x=>{x.classList.remove("o");x.firstChild.style.visibility="hidden"});mf=[]},900)}})}
let rq=[],ri=0,rsc=0,rt0=0;function raceNew(){rq=sh(G.w).slice(0,10);ri=0;rsc=0;rt0=Date.now();raceShow()}
function raceShow(){const R=document.getElementById("race");if(ri>=rq.length){const s=Math.round((Date.now()-rt0)/1000);R.innerHTML=`<div class="tcard">🏁 ${rsc} / 10 in ${s} seconds</div>`;document.getElementById("rs").textContent="";return}
 const w=rq[ri];const opts=sh([w,...sh(G.w.filter(x=>x!==w)).slice(0,3)]);document.getElementById("rs").textContent=`Question ${ri+1} / 10 · Score ${rsc}`;
 R.innerHTML=`<div class="rq">${w.df}</div><div class="ro">${opts.map(o=>`<button data-c="${o===w?1:0}">${o.en}</button>`).join("")}</div>`;
 R.querySelectorAll("button").forEach(b=>b.onclick=()=>{const ok=b.dataset.c==="1";b.classList.add(ok?"y":"n");if(!ok)R.querySelector('button[data-c="1"]').classList.add("y");if(ok)rsc++;R.querySelectorAll("button").forEach(x=>x.disabled=true);setTimeout(()=>{ri++;raceShow()},ok?600:1400)})}
let uw="",ug="",usc=0;function unsNew(){uw=sh(G.uns)[0];ug="";document.getElementById("uhint").textContent="";document.getElementById("uout").textContent="";
 document.getElementById("uletters").innerHTML=sh(uw.split("")).map(c=>`<button>${c}</button>`).join("")+' <button style="width:auto;padding:0 10px" onclick="unsNew2()">↺</button>';
 document.querySelectorAll("#uletters button:not([onclick])").forEach(b=>b.onclick=()=>{ug+=b.textContent;b.disabled=true;document.getElementById("uout").textContent=ug;if(ug.length===uw.length){if(ug===uw){usc++;document.getElementById("uout").textContent="✅ "+uw;document.getElementById("us").textContent="Score: "+usc}else{document.getElementById("uout").textContent="❌ "+ug+" — try again";setTimeout(unsNew2,900)}}})}
function unsNew2(){ug="";document.getElementById("uout").textContent="";document.querySelectorAll("#uletters button").forEach(b=>b.disabled=false)}
function unsHint(){const w=G.w.find(x=>x.en.includes(uw));document.getElementById("uhint").textContent=w?("💡 "+w.df):("💡 starts with “"+uw[0]+"”")}
function fh(b,i,a){const row=b.parentNode;row.querySelectorAll("button").forEach(x=>x.disabled=true);const ok=G.fair[i]===a;b.classList.add(ok?"y":"n");if(!ok)b.parentNode.insertAdjacentHTML("beforeend"," <b style='color:#b3261e'>→ "+G.fair[i]+"</b>")}
let ti=-1,tpt=0;function tabNew(){ti=(ti+1)%G.taboo.length;if(ti===0)G.taboo=sh(G.taboo);const[w,t]=G.taboo[ti];document.getElementById("tb").innerHTML=w+`<small>🚫 ${t.join(" · ")}</small>`}
function tabPt(){tpt++;document.getElementById("tbs").textContent="Points: "+tpt;tabNew()}
memNew();unsNew();
""".replace("__DATA__", json.dumps(DATA, ensure_ascii=False))
h = page("7.2", "Services and subscriptions", "SPEAKING & GAMES", "Speak and play with the words of the lesson: fees, hidden fees, subscriptions.", "BP A2 7.2 Services · Games", CODE,
         [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5), ("6", s6), ("7", s7)], K, None, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, extra_js=XJS)
os.makedirs(os.path.dirname(OUT), exist_ok=True); open(OUT, "w").write(h); print("ok games", len(h))
