"""Business Partner B2 · 1.2 Employee retention — SPEAKING & GAMES (simulations + vocabulary games).
1 Chunk tennis · 2 Would you rather? · 3 The $1M retention budget (simulation) · 4 Board meeting with twist cards (simulation) ·
5 Stay interview (secret cards) · 6 The rehire call (negotiation) · 7 Taboo
Usage: python3 build_b2_games_1-2.py OUT.html [STUDENT_CODE]
"""
import sys, os, json
from bp_page import page, ta, SELF
from vocab_b2 import lesson
import vcard
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#5b5fc7", "#e8e9fa", "#4044a8", "#7b7fe0"
_, GROUPS = lesson("1.2")
VOC, VJS = vcard.build(GROUPS, ACC, ACC2, DARK)
K = {}

TENNIS = [("lay off", "staff"), ("reverse a", "decision"), ("admit a", "mistake"), ("cut", "headcount"), ("lose institutional", "knowledge"),
          ("build the talent", "pipeline"), ("poach", "staff from rivals"), ("a cost-cutting", "exercise"), ("face a", "backlash"), ("take a", "sabbatical"),
          ("rehire", "staff"), ("triple entry-level", "hiring"), ("augment people, not", "replace them"), ("be up for a", "promotion"), ("take over menial", "tasks"),
          ("a healthy work-life", "balance"), ("maintain a legacy", "system"), ("bring somebody back as a", "consultant"), ("make somebody", "redundant"), ("stay out of fear, not", "loyalty")]
RATHER = [("a 4-week paid sabbatical every 3 years", "a 15% pay rise now"), ("work for IBM (hiring juniors)", "work for Salesforce (AI-first support)"),
          ("a clear promotion path", "a fully remote job"), ("an AI tool that does your menial tasks", "a mentor for one hour a week"),
          ("stay in a safe but boring job (job hugging)", "join a risky AI start-up"), ("a learning budget of €3,000 a year", "a four-day week"),
          ("be laid off with 6 months’ pay", "stay and train the AI that replaces your team"), ("manage 10 people", "manage 10 AI agents")]
TABOO = [("institutional knowledge", ["know", "company", "experience", "leave"]), ("AI washing", ["AI", "excuse", "cut", "money"]),
         ("job hugging", ["stay", "fear", "job", "leave"]), ("talent pipeline", ["junior", "future", "manager", "hire"]),
         ("sabbatical", ["break", "holiday", "long", "paid"]), ("menial tasks", ["boring", "simple", "routine", "skill"]),
         ("reverse a decision", ["change", "opposite", "back", "mind"]), ("poach staff", ["steal", "rival", "offer", "money"]),
         ("legacy system", ["old", "software", "code", "computer"]), ("a backlash", ["angry", "reaction", "negative", "people"])]
TWISTS = ["📈 Breaking: after the AI pilot, calls went UP by 2,000 a week. Team leaders are answering phones.",
          "📉 Customer satisfaction has dropped by 12 points since the chatbot launch.",
          "📨 Your best senior engineer has an offer from a rival: +30% salary. She leaves on Friday unless…",
          "🏛 The union has filed a complaint: ‘AI washing — job cuts dressed up as innovation.’",
          "💹 Investors love the plan: the share price is up 4% this morning.",
          "🤖 The AI vendor admits the agent can only handle 40% of tickets, not 70%.",
          "📰 A journalist calls: ‘Is it true you’re cutting 300 jobs because of AI?’",
          "🎓 HR data: 60% of juniors say learning and development is why they joined."]
ROLES = [("CFO", "You want to cut support headcount by 40% and save $4M a year. You love numbers. Secret: the board expects savings this quarter."),
         ("Head of Customer Experience", "You think the AI agent isn’t ready. Secret: two big clients have already complained about the chatbot."),
         ("HR Director", "Retention is your job. Secret: replacing one engineer costs up to $150,000, and three seniors are interviewing elsewhere."),
         ("CTO", "You built the AI agent and want it used. Secret: it works well for simple tickets but fails on complex ones.")]
PHR = ["I see your point, but…", "Let’s look at the numbers.", "What will happen if…?", "By 2027 we will have…", "In a year we’ll be dealing with…",
       "Can we agree on a pilot first?", "That’s a cost-cutting exercise, not a strategy.", "We can’t afford to lose institutional knowledge."]
BUDGET = [("juniors", "Hire & train juniors", "talent pipeline"), ("ai", "AI tools for menial tasks", "productivity"), ("learn", "Learning budget & mentors", "growth"),
          ("sab", "Sabbatical programme", "work-life balance"), ("pay", "Pay rises for seniors", "keep key people"), ("cut", "Severance for layoffs (cut 20%)", "short-term savings")]

s1 = ('<div class="bsec">Game</div><p class="ins"><b class="x">1</b>Chunk tennis. Your teacher “serves” the first part — you “return” the rest of the chunk before the ball lands (5 seconds). Then click to check.</p>'
      '<div class="court"><div class="serve" id="tsv">Click “Serve”</div><div class="ret" id="trt">…</div></div>'
      '<div class="tbar"><button class="btn" onclick="serve()">🎾 Serve</button><button class="btn l" onclick="tReveal(1)">✓ Got it</button><button class="btn l" onclick="tReveal(0)">✗ Missed</button>'
      '<span class="tm" id="tcd">5</span><span class="tm" id="tsc">0 : 0</span></div><p class="hint">Level up: after you return the chunk, make a sentence with it in 10 seconds.</p>')
s2 = ('<div class="bsec wr">Speaking</div><p class="ins"><b class="x">2</b>Would you rather…? Choose one, then defend your choice for 45 seconds. Your teacher will try to change your mind!</p>'
      '<div class="wyr"><button id="wa" onclick="wyrPick(this)">…</button><span>or</span><button id="wb" onclick="wyrPick(this)">…</button></div>'
      '<div class="tbar"><button class="btn" onclick="wyrNew()">🔀 New dilemma</button><button class="btn l" onclick="startT(\'wt\',45)">⏱ 45 s</button><span class="tm" id="wt">45</span></div>'
      '<p class="hint">I’d rather … because … · In five years I’ll be … · By then I’ll have … · Honestly, it depends on …</p>')
s3 = ('<div class="bsec wr">Simulation</div><p class="ins"><b class="x">3</b>The $1,000,000 retention budget. You are the new Head of People at a 400-person tech company. Your engineers are leaving and the CEO wants to “use AI”. Share out the budget, then press <b>Fast-forward to 2028</b>.</p>'
      '<div class="bud">%s</div><div class="tbar"><span class="tm" id="bleft">$1,000,000 left</span><button class="btn" onclick="budRun()">⏩ Fast-forward to 2028</button><button class="btn l" onclick="budReset()">↺ Reset</button></div>'
      '<div id="bout" class="bout"></div>' % "".join('<div class="br"><label>%s <small>%s</small></label><input type="range" min="0" max="500" step="50" value="0" data-b="%s" oninput="budUpd()"><b id="bv_%s">$0</b></div>' % (t, s, k, k) for k, t, s in BUDGET) +
      '<p class="ins" style="margin-top:14px">Now present your plan to the CEO (2 minutes). Use: <i>By 2028 we will have… · Next year we will be… · This will help us keep / build / avoid…</i></p>' + ta("bud_pres", "My plan: …", 90))
s4 = ('<div class="bsec wr">Simulation</div><p class="ins"><b class="x">4</b>Board meeting: <i>“Should we replace 40%% of customer support with an AI agent?”</i> Choose your role and read your <b>secret</b>. Your teacher plays the other roles. Every 2–3 minutes, draw a <b>twist card</b> — the situation changes!</p>'
      '<div class="roles">%s</div><div class="secret" id="rsec">Choose a role to see your secret.</div>' % "".join('<button class="btn l" onclick="pickRole(%d,this)">%s</button>' % (i, r) for i, (r, _) in enumerate(ROLES)) +
      '<div class="tbar"><button class="btn" onclick="twist()">🃏 Draw a twist card</button><button class="btn l" onclick="startT(\'mt\',600)">⏱ 10-min meeting</button><span class="tm" id="mt">600</span></div>'
      '<div class="twist" id="tw"></div><div class="phr">%s</div>' % "".join("<span>%s</span>" % p for p in PHR) +
      '<p class="ins" style="margin-top:14px">After the vote: write the decision as a 3-line Slack message to the whole company.</p>' + ta("board_slack", "📣 Decision: … · Why: … · What happens next: by … we will have …", 80))
s5 = ('<div class="bsec wr">Role-play</div><p class="ins"><b class="x">5</b>Stay interview. A great developer has a job offer from a rival. You are the manager and want to keep her. Your teacher is the developer and has a <b>secret reason</b> for leaving — find it with good questions!</p>'
      '<div class="card"><b>Manager (you):</b> budget for a 10% pay rise OR a learning budget OR a 4-week sabbatical (only one!). Find out what she really wants before you offer anything.<br><br>'
      '<b>Good questions:</b> What would make you stay? · What will you be doing there that you can’t do here? · Where do you see yourself in two years? · What would you need to have achieved by next year to feel happy here?</div>'
      '<details class="tch"><summary>🔒 Teacher only: the developer’s secret</summary>Choose one: (a) she is tired of menial tasks and wants AI work; (b) she wants a sabbatical to travel; (c) she is afraid of layoffs (“job hugging” the wrong way); (d) her manager never talks about promotion.</details>'
      '<p class="ins">What did you offer? Did she stay?</p>' + ta("stay_notes", "I found out that … so I offered …", 60))
s6 = ('<div class="bsec wr">Role-play</div><p class="ins"><b class="x">6</b>The rehire call. Six months ago your company let an expert go (“AI can do this”). Now nobody understands the legacy system. Call her and bring her back. She knows her knowledge is expensive now!</p>'
      '<div class="two2"><div class="card"><b>A · Head of Engineering (you)</b><br>Max budget: $150/hour or a full-time job at the old salary +10%. Admit the mistake, but don’t lose face. Try to agree on a start date.</div>'
      '<div class="card"><b>B · The ex-employee (teacher)</b><br>Wants $300/hour, remote, and a written apology to the team. Will accept less if they offer something she cares about.</div></div>'
      '<p class="hint">We made a mistake when we… · We’d like to bring you back as… · What would it take…? · Let’s meet halfway. · Could we agree on a three-month contract?</p>' + ta("rehire_deal", "The deal: …", 50))
s7 = ('<div class="bsec">Game</div><p class="ins"><b class="x">7</b>Taboo. Explain the chunk without saying the word or the forbidden words. 60 seconds — how many can you do?</p>'
      '<div class="tcard" id="tb">Click “Next card”</div><div class="tbar"><button class="btn" onclick="tabNew()">🃏 Next card</button><button class="btn l" onclick="tabPt()">✓ Guessed (+1)</button>'
      '<button class="btn l" onclick="startT(\'tt\',60)">⏱ 60 s</button><span class="tm" id="tt">60</span><span class="tm" id="tbs">Points: 0</span></div>' +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How confident do you feel talking about keeping and losing staff?"))

G = {"tennis": TENNIS, "rather": RATHER, "taboo": TABOO, "twists": TWISTS, "roles": ROLES}
JS = r"""
const G=__G__;const sh=a=>{a=[...a];for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};const $g=id=>document.getElementById(id);
let tmr=null;function startT(id,s){clearInterval(tmr);let t=s;$g(id).textContent=t;tmr=setInterval(()=>{t--;$g(id).textContent=t;if(t<=0){clearInterval(tmr);$g(id).textContent="⏰"}},1000)}
/* tennis */
let tq=sh(G.tennis),ti=-1,tw=0,tl=0,tcd=null;function serve(){ti=(ti+1)%tq.length;$g("tsv").textContent=tq[ti][0]+" …";$g("trt").textContent="…";$g("trt").className="ret";let t=5;$g("tcd").textContent=t;clearInterval(tcd);
 tcd=setInterval(()=>{t--;$g("tcd").textContent=t;if(t<=0){clearInterval(tcd);$g("tcd").textContent="🎾";$g("trt").textContent=tq[ti][1]}},1000)}
function tReveal(ok){if(ti<0)return;clearInterval(tcd);$g("trt").textContent=tq[ti][1];$g("trt").className="ret "+(ok?"y":"n");ok?tw++:tl++;$g("tsc").textContent=tw+" : "+tl}
/* would you rather */
let wq=sh(G.rather),wi=-1;function wyrNew(){wi=(wi+1)%wq.length;$g("wa").textContent=wq[wi][0];$g("wb").textContent=wq[wi][1];$g("wa").className=$g("wb").className=""}
function wyrPick(b){$g("wa").className=$g("wb").className="";b.className="on";startT("wt",45)}
/* budget */
function bvals(){const v={};document.querySelectorAll(".bud input").forEach(i=>v[i.dataset.b]=+i.value*1000);return v}
function budUpd(){const v=bvals();let tot=0;for(const k in v){tot+=v[k];$g("bv_"+k).textContent="$"+(v[k]/1000)+"k"}const left=1e6-tot;$g("bleft").textContent=(left<0?"⚠ over budget by $":"$")+Math.abs(left).toLocaleString("en")+(left<0?"":" left");$g("bleft").className="tm"+(left<0?" bad":"")}
function budReset(){document.querySelectorAll(".bud input").forEach(i=>i.value=0);budUpd();$g("bout").innerHTML=""}
function budRun(){const v=bvals();let tot=0;for(const k in v)tot+=v[k];if(tot>1e6){$g("bout").innerHTML="<p>⚠ You are over budget. Move some money first.</p>";return}
 const s=k=>Math.sqrt(v[k]/1000);let ret=30+0.45*(1.6*s("juniors")+2.2*s("learn")+1.4*s("sab")+2.4*s("pay")+0.8*s("ai")-2.6*s("cut"));ret=Math.max(5,Math.min(98,Math.round(ret)));
 const L=[];
 L.push(v.juniors<150000?"❌ By 2028 you will have hired almost no juniors. You will be poaching mid-level engineers from rivals at +30%.":"✅ By 2028 your juniors will have become mid-level engineers. Your talent pipeline is full.");
 L.push(v.cut>0?"⚠ The layoffs saved money in 2026, but by 2027 you will have rehired "+Math.max(1,Math.round(v.cut/60000))+" people for similar roles — and lost institutional knowledge.":"✅ No layoffs: the team trusts you, and institutional knowledge stayed.");
 L.push(v.ai>=200000&&v.learn<100000?"⚠ Lots of AI tools, but nobody trained people to use them. Productivity is only slightly higher.":v.ai>=100000?"✅ AI is taking over menial tasks, and people are doing more diverse work.":"• Your engineers are still doing a lot of menial tasks by hand.");
 L.push(v.sab>=100000?"✅ The sabbatical programme is a top reason people stay. Burnout is down.":"• No sabbaticals: some seniors are burning out.");
 L.push(v.pay<100000?"⚠ Two key seniors will have left for rivals by 2028.":"✅ Your key people are staying — for now.");
 if(tot<1e6)L.push("💰 You still have $"+(1e6-tot).toLocaleString("en")+". The CFO is happy, but was that the best use?");
 $g("bout").innerHTML=`<div class="rep"><b>📊 2028 report · retention score: ${ret}/100</b><ul>${L.map(x=>"<li>"+x+"</li>").join("")}</ul><p class="hint">Do you agree with the report? What would you do differently?</p></div>`}
/* board meeting */
let twq=sh(G.twists),twi=-1;function twist(){twi=(twi+1)%twq.length;$g("tw").innerHTML="<b>🃏 Twist!</b> "+twq[twi]+"<br><i>How does this change your position?</i>";$g("tw").classList.add("show")}
function pickRole(i,b){document.querySelectorAll(".roles button").forEach(x=>x.classList.remove("on"));b.classList.add("on");$g("rsec").innerHTML="<b>"+G.roles[i][0]+":</b> "+G.roles[i][1]}
/* taboo */
let tbq=sh(G.taboo),tbi=-1,tbp=0;function tabNew(){tbi=(tbi+1)%tbq.length;const[w,f]=tbq[tbi];$g("tb").innerHTML="<b>"+w+"</b><div class='fb'>"+f.map(x=>"<span>"+x+"</span>").join("")+"</div>"}
function tabPt(){tbp++;$g("tbs").textContent="Points: "+tbp;tabNew()}
document.head.insertAdjacentHTML("beforeend",`<style>
.tbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:10px 0}.tm{font-weight:600;color:#4044a8;background:#e8e9fa;border-radius:6px;padding:4px 12px}.tm.bad{color:#b52b27;background:#fdecec}
.court{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:10px 0}.serve,.ret{border-radius:12px;padding:22px;font-size:24px;text-align:center;font-weight:500}.serve{background:#4044a8;color:#fff}.ret{background:#f3f3fb;color:#4044a8;border:2px dashed #7b7fe0}.ret.y{background:#e7f6ec;border-color:#2e9b57}.ret.n{background:#fdecec;border-color:#d9534f}
.wyr{display:flex;gap:12px;align-items:center;flex-wrap:wrap;margin:10px 0}.wyr button{flex:1 1 260px;min-height:90px;font:inherit;font-size:18px;border:2px solid #c8c9cb;border-radius:12px;background:#fff;cursor:pointer;padding:12px}.wyr button.on{border-color:#5b5fc7;background:#e8e9fa;font-weight:500}.wyr span{font-weight:600;color:#888}
.bud{border:1px solid #dcdde0;border-radius:10px;padding:8px 14px}.br{display:grid;grid-template-columns:1.4fr 1.6fr 70px;gap:10px;align-items:center;padding:6px 0;border-bottom:1px solid #f0f0f2}.br small{display:block;color:#888;font-size:13px}.br input{width:100%;accent-color:#5b5fc7}
.rep{background:#fafaff;border:1.5px solid #5b5fc7;border-radius:10px;padding:10px 18px;margin-top:10px}.rep li{margin:5px 0}
.roles{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0}.roles .on{background:#5b5fc7;color:#fff;border-color:#5b5fc7}.secret{background:#fff8e6;border-left:4px solid #f2b631;padding:10px 14px;border-radius:6px}
.twist{display:none;background:#fdecec;border:2px solid #d9534f;border-radius:10px;padding:12px 16px;font-size:17px;margin:8px 0}.twist.show{display:block;animation:pop .3s}@keyframes pop{from{transform:scale(.95);opacity:0}to{transform:none;opacity:1}}
.phr{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0}.phr span{background:#e8e9fa;color:#4044a8;border-radius:14px;padding:3px 11px;font-size:14px}
.tcard{background:#4044a8;color:#fff;border-radius:12px;padding:24px;text-align:center;font-size:22px;margin:10px 0}.tcard .fb{margin-top:10px;display:flex;gap:8px;justify-content:center;flex-wrap:wrap}.tcard .fb span{background:#fff;color:#b52b27;text-decoration:line-through;border-radius:12px;padding:2px 10px;font-size:15px}
.two2{display:grid;grid-template-columns:1fr 1fr;gap:12px}@media(max-width:700px){.two2,.court{grid-template-columns:1fr}.br{grid-template-columns:1fr}}
details.tch summary{cursor:pointer;color:#9a6b00;font-weight:500;margin:8px 0}</style>`);"""
XJS = VJS + JS.replace("__G__", json.dumps(G, ensure_ascii=False))
secs = [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5), ("6", s6), ("7", s7)]
h = page("1.2", "Employee retention", "SPEAKING & GAMES", "Simulations and games: use the lesson chunks and future forms to make real decisions about keeping people.",
         "BP B2 1.2 Employee retention · Games", CODE, secs, K, VOC, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, extra_js=XJS)
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True); open(OUT, "w").write(h); print("ok games", len(h))
