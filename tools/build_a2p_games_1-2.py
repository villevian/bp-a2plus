"""Business Partner A2+ · 1.2 Events management — SPEAKING & GAMES (a speaking lesson to close 1.2).
Business meetings with role cards: the student uses the 1.2 vocabulary (venue, guests, budget, entertainment, hybrid event, stay for the weekend…)
and the grammar (comparatives / superlatives) to agree on things.
1 Warm-up: talk for a minute · 2 Collocation pairs (memory) · 3 Meeting phrases · 4 MEETING 1: plan the evening event (client meeting, notes sheet)
5 MEETING 2: a problem with the venue (negotiate a solution) · 6 MEETING 3: bleisure — ask your manager to stay for the weekend · 7 Follow-up message + self-assessment
Teacher = Student B (cards B are hidden under "Card B — for the teacher").
Usage: python3 build_a2p_games_1-2.py OUT.html [STUDENT_CODE]
"""
import sys, os, json, random
from bp_page import page, ta, inp, SELF
from vocab_a2p import lesson
import vcard
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3fa9ad", "#e6f4f4", "#2b8185", "#5cc1c4"
_, GROUPS = lesson("1.2")
VOC, VJS = vcard.build(GROUPS, ACC, ACC2, DARK)
K = {}

TALK = ["What was the best event you ever went to? Why was it the best?", "Do you prefer big conferences or small meetings? Why?",
        "What is more important for an event: the venue or the people?", "Have you ever organised a party or a business event? What did you arrange?",
        "Would you like to stay for the weekend after a work trip? Where?", "Hybrid events: do you prefer to join online or in person?",
        "What is the most expensive event you know about?", "Which is better for a team: a dinner in a restaurant or an offsite in a villa?",
        "Are you good at managing a budget? Give an example.", "Do you pay attention to detail at work? When is it important?",
        "What do you need to get on with clients?", "Barcelona, Kyiv or Lviv: which city is the best for a conference? Why?"]
s1 = ('<div class="bsec wr">Speaking</div><p class="ins"><b class="x">1</b>Warm-up. Talk for a minute. Take a card, start the timer and answer. Use words from 1.2!</p>'
      '<div class="tcard" id="tq">Click “New card”</div><div class="tbar"><button class="btn" onclick="newQ()">🔀 New card</button>'
      '<button class="btn l" onclick="startT(\'tm\',60)">⏱ Start 60 s</button><span class="tm" id="tm">60</span></div>'
      '<p class="hint">Useful: I think … is better than … · The best … was … · For me, the most important thing is …</p>')

PAIRS = [("plan", "an event"), ("attend", "a conference"), ("book", "a venue"), ("manage", "a budget"), ("pay attention", "to detail"), ("get on", "with people"),
         ("invite", "guests"), ("hire", "staff"), ("stream", "the talks"), ("stay", "for the weekend"), ("organise", "entertainment"), ("launch", "a new product")]
s2 = ('<div class="bsec">Game</div><p class="ins"><b class="x">2</b>Collocation pairs. Find the two halves. Then make a sentence about your work with each pair.</p>'
      '<div class="tbar"><button class="btn l" onclick="memNew()">🔀 New game</button><span id="mm" class="tm"></span></div><div class="mem" id="mem"></div>'
      '<p class="hint">Level up: after each pair, say a sentence in 10 seconds: <i>I booked a venue for our office party last year.</i></p>')

PH = [("Starting", ["Thank you for meeting me.", "Let’s start. We need to agree on …", "First, let’s talk about …"]),
      ("Suggesting", ["How about …?", "What about …?", "Why don’t we …?", "I suggest …"]),
      ("Comparing", ["The winery is cheaper than the boat.", "The rooftop is the best option for …", "It’s more / less expensive than …"]),
      ("Agreeing", ["I agree.", "That’s a good idea.", "That works for me.", "OK, let’s do that."]),
      ("Not agreeing (politely)", ["I’m not sure about that.", "I see your point, but …", "That’s a bit expensive for us.", "Can we find something cheaper?"]),
      ("Finishing", ["So, we agree on …", "Let me check: …", "I’ll send you a summary by email.", "Thank you. Speak soon!"])]
s3 = ('<div class="bsec">Phrases</div><p class="ins"><b class="x">3</b>Meeting phrases. Read and listen (click a phrase). Which ones do you already use? Tick them in your head — then use them in the meetings!</p>'
      '<div class="phg">' + "".join('<div class="ph"><h4>%s</h4>%s</div>' % (h, "".join('<p class="sp">%s</p>' % x for x in ps)) for h, ps in PH) + '</div>')

VEN = ('<table class="tb"><tr><th></th><th>Rooftop terrace<br><span>city centre</span></th><th>Winery<br><span>40 min by bus</span></th><th>Boat restaurant<br><span>old port</span></th></tr>'
       '<tr><td>Guests</td><td>up to 120</td><td>up to 80</td><td>up to 200</td></tr><tr><td>Food</td><td>tapas · €45 per person</td><td>Catalan menu + vegan · €70</td><td>paella (seafood / vegetable) · €90</td></tr>'
       '<tr><td>Entertainment</td><td>DJ</td><td>live guitar, wine tasting</td><td>jazz band</td></tr><tr><td>Staff</td><td>8</td><td>10</td><td>18</td></tr>'
       '<tr><td>Free dates</td><td>Thu 14 or Fri 15 May</td><td>Fri 15 May only</td><td>Thu 14 May only</td></tr><tr><td>Extra</td><td>no roof — weather!</td><td>bus €600</td><td>can stream the talks (hybrid)</td></tr></table>')
NOTES = [("venue", "Venue"), ("date", "Date"), ("guests", "Number of guests"), ("food", "Food (vegan / gluten-free?)"), ("ent", "Entertainment"),
         ("budget", "Budget / price per person"), ("extra", "Transport / online guests / other"), ("next", "Next step")]
s4 = ('<div class="bsec wr">Meeting 1</div><p class="ins"><b class="x">4</b>Client meeting: plan the evening event. You work for <b>BCN Smart Events</b>. Your teacher is the client. '
      'Meet (on a video call), ask questions, compare the venues and agree on the plan. Fill in your meeting notes.</p>'
      '<div class="rp"><div class="rh">🧑‍💼 Card A — you (event manager, BCN Smart Events)</div><ul>'
      '<li>Your client is a company with a two-day conference in Barcelona, 14–15 May.</li><li>Find out: how many guests? budget? special food? online guests?</li>'
      '<li>Present the three venues. Compare them: <i>cheaper than, the biggest, the best option for …</i></li>'
      '<li>Your company wants a good result — but also a happy client. Try to sell the winery: you have a good discount there (10%).</li>'
      '<li>At the end, check the plan and agree on the next step.</li></ul></div>' + VEN +
      '<details class="tch"><summary>🔒 Card B — for the teacher (client)</summary><ul><li>You are the HR director of a law firm, <b>Vega Legal</b>. 140 guests, 25 of them join online.</li>'
      '<li>Budget: about €8,000 for the evening (food + entertainment). 10 guests are vegan, 4 need gluten-free food.</li>'
      '<li>Your CEO loves jazz, but you think the boat is too expensive. You are worried about rain on the rooftop.</li>'
      '<li>Ask difficult questions: <i>What happens if it rains? Can you stream the talks? Is the price per person with drinks?</i></li>'
      '<li>Possible agreement: the boat restaurant with vegetable paella and a smaller jazz band, or the rooftop with a plan B (tent).</li></ul></details>'
      '<p class="ins">📝 Your meeting notes</p><div class="notes">' + "".join('<label>%s</label>%s' % (l, inp("n1_" + k, 420)) for k, l in NOTES) + '</div>')

s5 = ('<div class="bsec wr">Meeting 2</div><p class="ins"><b class="x">5</b>A problem! It’s two weeks before the event. You call the venue manager (your teacher). Explain the problem and agree on a solution.</p>'
      '<div class="rp"><div class="rh">📞 Card A — you (event manager)</div><ul><li>The client now has <b>170 guests</b>, not 140.</li><li>You booked the rooftop (max 120) — or the venue from Meeting 1.</li>'
      '<li>Ask what the venue can do. Suggest solutions: <i>How about …? Why don’t we …?</i></li><li>You can’t pay more than €1,000 extra.</li><li>Agree on a solution and on a date to confirm.</li></ul></div>'
      '<details class="tch"><summary>🔒 Card B — for the teacher (venue manager)</summary><ul><li>You can use the terrace next door (+50 guests) for €1,500.</li>'
      '<li>Or: two sittings — 120 guests from 19:00, 50 more from 21:00 for the DJ party.</li><li>You need 2 more staff (€400). You can give a 10% discount if they confirm today.</li>'
      '<li>Be friendly but firm about the price.</li></ul></details>'
      '<p class="hint">Useful: We have a problem with … · We need space for … more guests. · Is it possible to …? · What’s the best you can do? · OK, let’s agree on …</p>' +
      ta("m2", "Our solution: …", 60))

s6 = ('<div class="bsec wr">Meeting 3</div><p class="ins"><b class="x">6</b>Bleisure. The conference finishes on Friday. You want to <b>stay for the weekend</b> in Barcelona. Ask your manager (your teacher).</p>'
      '<div class="rp"><div class="rh">🌴 Card A — you</div><ul><li>Explain why the weekend is a good idea: the hotel is cheaper on Sunday, the flight is cheaper on Sunday too.</li>'
      '<li>You can visit a new venue for next year’s event on Saturday morning (work!).</li><li>You pay for your hotel on Saturday night yourself.</li>'
      '<li>Use comparatives: <i>The Sunday flight is cheaper than the Friday flight.</i></li></ul></div>'
      '<details class="tch"><summary>🔒 Card B — for the teacher (manager)</summary><ul><li>You are not sure: there is an important client meeting on Monday at 9:00.</li>'
      '<li>Ask: Who pays for the hotel? Are you back on Monday morning? Can you send me the report on Friday?</li><li>Agree if the student has good answers — maybe the Sunday morning flight, not the evening one.</li></ul></details>'
      '<p class="hint">Useful: Is it OK if I …? · It’s cheaper / better for the company because … · I promise I’ll … · Thank you, that’s great!</p>' + ta("m3", "We agreed that …", 50))

MODEL = ("Hi Ana,\nThank you for the meeting today. Let me confirm what we agreed:\n• Venue: the boat restaurant in the old port, Thursday 14 May, 19:00.\n"
         "• 140 guests (25 join online — we stream the talks).\n• Food: vegetable paella; 10 vegan and 4 gluten-free menus.\n• Entertainment: a jazz trio.\n"
         "• Budget: €8,000 — I’ll send the final price by Friday.\nNext step: please confirm the number of guests by 1 May.\nBest regards,\nLarysa")
s7 = ('<div class="bsec wr">After the meeting</div><p class="ins"><b class="x">7</b>Write a short follow-up email to the client (Meeting 1). Confirm what you agreed (60–100 words). Use your meeting notes.</p>'
      '<div class="ext"><ul style="margin:0;padding-left:20px"><li>Thank you for the meeting today.</li><li>Let me confirm what we agreed: …</li><li>Next step: …</li><li>Best regards,</li></ul></div>' +
      ta("w7", "Hi …, Thank you for the meeting today. Let me confirm what we agreed: …", 180) + '<p class="hint" id="w7c"></p>'
      '<button class="btn l" onclick="model(\'m7\')">Show a model email</button><div class="model" id="m7">%s</div>' % MODEL +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you plan an event and agree on things in a meeting?"))

DATA = {"talk": TALK, "pairs": PAIRS}
XJS = VJS + r"""
document.head.insertAdjacentHTML("beforeend",`<style>
.tcard{border:2px solid ACC;background:ACC2;border-radius:12px;padding:26px 22px;font-size:21px;font-weight:500;text-align:center;min-height:110px;display:flex;align-items:center;justify-content:center;margin:10px 0}
.tbar{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:8px 0}.tm{font-weight:600;font-size:19px;color:DARK;margin-left:4px}
.mem{display:grid;grid-template-columns:repeat(6,1fr);gap:8px;margin-top:8px}.mc{border:1.5px solid ACC;border-radius:8px;min-height:62px;display:flex;align-items:center;justify-content:center;text-align:center;padding:6px;cursor:pointer;font-size:15px;background:#fff;user-select:none}
.mc.h{color:transparent;background:ACC2}.mc.h::after{content:"?";color:DARK;font-weight:600;font-size:20px}.mc.ok{background:#eaf7ee;border-color:#3a9d5d;cursor:default}
.phg{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.ph{border:1px solid #d5d6d7;border-radius:8px;padding:8px 12px}.ph h4{margin:2px 0 6px;color:DARK;font-size:14px;text-transform:uppercase}.sp{margin:4px 0;cursor:pointer}.sp:hover{color:DARK}
.rp{border:1.5px solid ACC;border-radius:10px;padding:10px 16px;margin:10px 0;background:#fff}.rh{font-weight:600;color:DARK;margin-bottom:4px}.rp ul,.tch ul{margin:4px 0;padding-left:20px}.rp li,.tch li{margin:3px 0}
.tch{background:#fff8e6;border:1px dashed #e0b43c;border-radius:10px;padding:8px 14px;margin:10px 0}.tch summary{cursor:pointer;font-weight:500}
table.tb{border-collapse:collapse;width:100%;margin:10px 0;font-size:15px}table.tb th,table.tb td{border:1px solid #c8c9cb;padding:6px 8px;text-align:center}table.tb th{background:ACC2;color:DARK}table.tb th span{font-weight:300;font-size:13px}table.tb td:first-child{text-align:left;font-weight:500}
.notes{display:grid;grid-template-columns:220px 1fr;gap:6px 12px;align-items:center;max-width:720px}.notes label{font-size:15px;color:#4d4d4f}.notes input{max-width:100%}
@media(max-width:800px){.mem{grid-template-columns:repeat(3,1fr)}.phg{grid-template-columns:1fr}.notes{grid-template-columns:1fr}}
</style>`.replace(/ACC2/g,"__ACC2__").replace(/ACC/g,"__ACC__").replace(/DARK/g,"__DARK__"));
const G=__DATA__;let qi=-1,TT={};
function newQ(){qi=(qi+1+Math.floor(Math.random()*(G.talk.length-1)))%G.talk.length;document.getElementById("tq").textContent=G.talk[qi]}
function startT(id,s){clearInterval(TT[id]);let t=s;const el=document.getElementById(id);el.textContent=t;TT[id]=setInterval(()=>{t--;el.textContent=t>0?t:"⏰ Time!";if(t<=0)clearInterval(TT[id])},1000)}
let MO=[],MV=0,MF=0;
function memNew(){const c=[];G.pairs.forEach((p,i)=>{c.push({t:p[0],i});c.push({t:p[1],i})});c.sort(()=>Math.random()-.5);MO=[];MV=0;MF=0;
 const box=document.getElementById("mem");box.innerHTML=c.map(x=>'<div class="mc h" data-i="'+x.i+'">'+x.t+'</div>').join("");document.getElementById("mm").textContent="";
 box.querySelectorAll(".mc").forEach(el=>el.onclick=()=>{if(!el.classList.contains("h")||MO.length===2)return;el.classList.remove("h");MO.push(el);
  if(MO.length===2){MV++;const[a,b]=MO;if(a.dataset.i===b.dataset.i){a.classList.add("ok");b.classList.add("ok");MO=[];MF++;
   document.getElementById("mm").textContent="Moves: "+MV+" · Pairs: "+MF+"/"+G.pairs.length+(MF===G.pairs.length?" 🎉":"");if("speechSynthesis" in window){speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(a.textContent+" "+b.textContent);u.lang="en-GB";speechSynthesis.speak(u)}}
   else setTimeout(()=>{a.classList.add("h");b.classList.add("h");MO=[];document.getElementById("mm").textContent="Moves: "+MV},900)}})}
memNew();
document.querySelectorAll(".sp").forEach(p=>p.onclick=()=>{if(!("speechSynthesis" in window))return;speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(p.textContent.replace("…",""));u.lang="en-GB";u.rate=.9;speechSynthesis.speak(u)});
function wc(){const t=document.querySelector('.g[data-k="w7"]');if(!t)return;const n=(t.value.trim().match(/\S+/g)||[]).length;document.getElementById("w7c").textContent=n+" words (aim: 60–100)"}
document.addEventListener("input",e=>{if(e.target.dataset&&e.target.dataset.k==="w7")wc()});window.afterFill=wc;
""".replace("__DATA__", json.dumps(DATA, ensure_ascii=False)).replace("__ACC2__", ACC2).replace("__ACC__", ACC).replace("__DARK__", DARK)
h = page("1.2", "Events management", "SPEAKING & GAMES", "Use the 1.2 vocabulary in business meetings: plan an event, solve a problem, agree on things.",
         "BP A2+ 1.2 Events · Games", CODE, [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5), ("6", s6), ("7", s7)], K, VOC,
         acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, footer="Speaking lesson to close 1.2. Teacher = Student B. ", extra_js=XJS)
if CODE:  # student site: hide the teacher's secret cards
    import re
    h = re.sub(r'<details class="tch">.*?</details>', '', h, flags=re.S)
os.makedirs(os.path.dirname(OUT), exist_ok=True); open(OUT, "w").write(h); print("ok", OUT, len(h))
