# -*- coding: utf-8 -*-
"""Grammar review: Present Simple vs Present Continuous + vocabulary of lessons 1.1–1.3.
Bloom's taxonomy ladder: Remember → Understand → Apply → Apply → Analyse → Evaluate → Create → Speak.
Two content sets: A2 (IT, lessons 1.1–1.3 of bp-a2) and A2+ (standard business, bleisure / Barcelona, bp-a2plus 1.1–1.3).
Usage: python3 build_review_ps_pc.py a2|a2plus OUT_FILE [STUDENT_CODE]
"""
import sys, random, re
from bp_page import page, fb, sel, inp, ta, ctl, SELF
LEVEL, OUT = sys.argv[1], sys.argv[2]; CODE = sys.argv[3] if len(sys.argv) > 3 else ""
random.seed(7)

def variants(s):
    """Accept full and short forms: is/'s, am/'m, are/'re, does not/doesn't, do not/don't, is not/isn't, are not/aren't."""
    out = {s}
    pairs = [(" am not ", "'m not "), (" am ", "'m "), (" is not ", " isn't "), (" are not ", " aren't "), (" does not ", " doesn't "), (" do not ", " don't "), (" is ", "'s "), (" are ", "'re ")]
    for a, b in pairs:
        for x in list(out):
            if a in " " + x + " ":
                out.add((" " + x + " ").replace(a, b if b.startswith(" ") else b, 1).strip().replace(" '", "'"))
    return sorted(out)

D = {}
D["a2"] = dict(
 num="1.1–1.3", title="Present Simple or Present Continuous?", key="BP A2 Review 1.1–1.3 · Present Simple vs Continuous",
 voc=[("Jobs and tasks", ["go to meetings", "answer messages", "analyse data", "write reports", "do research", "call customers"]),
      ("Meetings", ["book a meeting room", "send out the agenda", "create a brief", "prepare a presentation", "get an update", "calculate costs"]),
      ("The office", ["work from home", "take a break", "a quiet room", "a kitchen area", "working hours", "spend time at your desk"]),
      ("Time words", ["usually / often / never", "every day / on Mondays", "now / right now", "today / this week", "Look! / Listen!"])],
 s1=[("I usually go to meetings on Monday morning.", "Simple"), ("Look! Anna is booking the meeting room.", "Continuous"), ("Our developer works in a big team.", "Simple"),
     ("We’re working from home this week.", "Continuous"), ("The QA engineer never writes reports on Friday.", "Simple"), ("Sorry, I can’t talk. I’m preparing a presentation.", "Continuous"),
     ("Do you analyse data every day?", "Simple"), ("Is Max answering messages in Slack right now?", "Continuous")],
 s2=[("I check my emails every morning.", "a habit (usually)"), ("A recruiter finds new people for the company.", "a fact (always true)"),
     ("Shh! The PM is talking to the client.", "right now"), ("This month I’m doing research for a new app.", "for a short time (this week / these days)"),
     ("She rarely travels for work.", "a habit (usually)"), ("Designers create the look of an app.", "a fact (always true)"),
     ("Today I’m working in the quiet room.", "for a short time (this week / these days)"), ("Listen! Someone is calling customers.", "right now")],
 s3=[("Our PM", "(send out)", "the agenda every Friday.", "sends out"), ("Right now I", "(create)", "a brief for the designer.", "am creating"),
     ("Max", "(not / go)", "to meetings on Fridays.", "does not go"), ("This week we", "(calculate)", "costs for the new project.", "are calculating"),
     ("How often", "(you / take)", "a break?", "do you take"), ("Look! Olha", "(book)", "the meeting room again.", "is booking"),
     ("I", "(not / work)", "today — I’m on holiday.", "am not working"), ("", "(the office / have)", "a gym?", "does the office have")],
 s4=[("you / usually / go to meetings / on Monday", "S", "do you usually go to meetings on monday"), ("what / you / do / now", "C", "what are you doing now"),
     ("your team / work from home / this week", "C", "is your team working from home this week"), ("how often / she / get an update", "S", "how often does she get an update"),
     ("where / you / take a break", "S", "where do you take a break"), ("Max / prepare a presentation / right now", "C", "is max preparing a presentation right now")],
 s5=[("She don’t work on Fridays.", "She does not work on Fridays."), ("I am agree with you.", "I agree with you."), ("Look! He work in the quiet room.", "Look! He is working in the quiet room."),
     ("Do she analyse data every day?", "Does she analyse data every day?"), ("We usually are busy on Mondays.", "We are usually busy on Mondays."), ("Right now I write a report.", "Right now I am writing a report.")],
 s6=[("Are you free for a quick call?", "Sorry, I’m in a meeting right now. How about 3 p.m.?", "Sorry, I go to a meeting. How about 3 p.m.?"),
     ("What do you do? (= your job)", "I’m a UX/UI designer. I design apps for banks.", "I’m designing a new app."),
     ("What are you doing?", "I’m writing the weekly report — almost done!", "I usually write reports."),
     ("How often do you work from home?", "Twice a week, usually on Monday and Friday.", "I’m working from home.")],
 s7="Write a message to your team chat (5–7 sentences): what you usually do on Mondays and what you are doing this week.",
 s7m="Hi team! 👋 On Mondays I usually go to the planning meeting at 10 and answer messages. I often check our backlog after lunch. But this week is different: I’m working from home, and I’m preparing a presentation for a new client. Today I’m also creating a brief for the designer. Talk soon!",
 s7ph="Hi team! On Mondays I usually …",
 cards=["What do you usually do on Monday morning?", "What are you working on this week?", "How often do you go to meetings?", "What are you doing right now? (Look around you!)",
        "Where do you usually take a break?", "Are you working from home today?", "What does a QA engineer do?", "Who usually sends out the agenda in your team?",
        "What is your team doing this month?", "How often do you answer messages after work?", "What do you never do at work?", "Is anyone in your family working right now? What are they doing?"],
 out="I can talk about my usual work and what is happening now.", acc=("#e8894a", "#fbeadb", "#c4642a", "#f2a66e"))
D["a2plus"] = dict(
 num="1.1–1.3", title="Present Simple or Present Continuous?", key="BP A2+ Review 1.1–1.3 · Present Simple vs Continuous",
 voc=[("Travel", ["book accommodation", "boarding pass", "delayed / on time", "departure / arrival", "take the train", "extend a trip"]),
      ("Events", ["plan an event", "attend a conference", "venue", "guests / staff", "manage a budget", "organise"]),
      ("Small talk", ["make small talk", "show interest", "change the subject", "Where do you come from?", "What are you doing in …?"]),
      ("Time words", ["usually / often / never", "every year / on Fridays", "now / at the moment", "today / this week", "Look! / Listen!"])],
 s1=[("I usually book accommodation two weeks before a trip.", "Simple"), ("Look! Our flight is boarding now.", "Continuous"), ("The company organises a conference every year.", "Simple"),
     ("This week I’m staying at a small hotel near the venue.", "Continuous"), ("Our events manager never pays for business class.", "Simple"), ("Sorry, I can’t talk — I’m checking in at the airport.", "Continuous"),
     ("Do you often attend conferences?", "Simple"), ("Is Marta still making small talk with the guests?", "Continuous")],
 s2=[("I take the train to work every day.", "a habit (usually)"), ("A venue is a place for an event.", "a fact (always true)"),
     ("Shh! The speaker is starting her talk.", "right now"), ("This month I’m planning a product launch.", "for a short time (this week / these days)"),
     ("She rarely travels long-haul.", "a habit (usually)"), ("Events managers manage the budget.", "a fact (always true)"),
     ("Today I’m working from the hotel lobby.", "for a short time (this week / these days)"), ("Listen! They’re calling our flight.", "right now")],
 s3=[("Our team", "(attend)", "a conference every spring.", "attends"), ("Right now I", "(look for)", "a venue for the party.", "am looking for"),
     ("Marta", "(not / like)", "long-haul flights.", "does not like"), ("This week we", "(stay)", "at a B&B in Barcelona.", "are staying"),
     ("How often", "(you / travel)", "for work?", "do you travel"), ("Look! The departure time", "(change)", "on the screen.", "is changing"),
     ("I", "(not / work)", "this weekend — I’m extending my trip.", "am not working"), ("", "(the hotel / have)", "a gym?", "does the hotel have")],
 s4=[("you / usually / travel / for work", "S", "do you usually travel for work"), ("what / you / do / in Barcelona", "C", "what are you doing in barcelona"),
     ("your flight / leave / on time", "C", "is your flight leaving on time"), ("how often / your company / organise / events", "S", "how often does your company organise events"),
     ("where / you / usually / stay", "S", "where do you usually stay"), ("the guests / arrive / now", "C", "are the guests arriving now")],
 s5=[("She don’t like long-haul flights.", "She does not like long-haul flights."), ("I am agree with you.", "I agree with you."), ("Look! The guests arrive now.", "Look! The guests are arriving now."),
     ("Do he organise the event every year?", "Does he organise the event every year?"), ("We usually are tired after a conference.", "We are usually tired after a conference."), ("At the moment I wait for my boarding pass.", "At the moment I am waiting for my boarding pass.")],
 s6=[("Can you talk now?", "Sorry, I’m at the airport — my flight is boarding. Can I call you tonight?", "Sorry, I board my flight. Can I call you tonight?"),
     ("What do you do? (= your job)", "I’m an events manager. I organise conferences for clients.", "I’m organising a conference."),
     ("What are you doing in Barcelona?", "I’m attending a conference, and I’m staying for the weekend.", "I attend conferences."),
     ("How often do you travel for work?", "About once a month, usually to Spain or Italy.", "I’m travelling for work.")],
 s7="You are on a business trip. Write a message to a colleague (5–7 sentences): what you usually do on a work trip and what you are doing on this trip.",
 s7m="Hi Anna! On work trips I usually stay in a business hotel and go to bed early. I never have time to see the city. But this trip is different! I’m staying in a small B&B near the venue, and I’m extending my trip for the weekend. Right now I’m sitting in a café and making notes for tomorrow’s talk. See you on Monday!",
 s7ph="Hi …! On work trips I usually …",
 cards=["How often do you travel for work?", "What are you doing this week?", "Where do you usually stay on a business trip?", "What are you doing right now?",
        "What do you usually do on the plane or train?", "Is your company planning an event this year?", "What does an events manager do?", "Who usually organises events in your company?",
        "What are you reading or watching these days?", "What do you never do on a business trip?", "Do you usually make small talk with people you don’t know?", "Where are you staying on your next trip?"],
 out="I can talk about my usual work trips and what is happening now.", acc=("#3fa9ad", "#e6f4f4", "#2b8185", "#5cc1c4"))

C = D[LEVEL]; K = {}
def shuf(o): o = o[:]; random.shuffle(o); return o
def rad(k, opts): return "".join('<label class="opt" style="display:inline;margin:0 12px 0 0"><input type="radio" name="%s" data-k="%s" value="%s"> %s</label>' % (k, k, o, o) for o in opts)
def bloom(level, ua): return '<div class="bloom"><b>%s</b> · %s</div>' % (level, ua)
G = ('<div class="gbox"><div class="gh">Present Simple or Present Continuous?</div><div class="two">'
     '<div>🔁 <b>Present Simple</b> — <i>usually, always, every day, never</i><br>habits, routines, facts, schedules<br>'
     '<span class="ex">I <b>work</b> · She <b>works</b> · She <b class="a">doesn’t</b> work · <b class="a">Do</b> you work?</span></div>'
     '<div>▶️ <b>Present Continuous</b> — <i>now, at the moment, today, this week</i><br>actions in progress, temporary situations<br>'
     '<span class="ex">I<b class="a">’m</b> work<b>ing</b> · She<b class="a">’s</b> work<b>ing</b> · She <b class="a">isn’t</b> working · <b class="a">Are</b> you working?</span></div></div>'
     '<p class="hint">🇺🇦 Не вживаємо ‑ing з дієсловами стану: <b>know, like, want, need, agree, understand</b> → <i>I agree</i>, не <i>I am agree</i>.</p></div>')
S = []
# 1 Remember
rows = ""
for i, (t, a) in enumerate(C["s1"], 1):
    k = "r1_%d" % i; K[k] = [a]
    rows += '<div class="tf"><span class="q">%d. %s</span>%s%s</div>' % (i, t, rad(k, ["Simple", "Continuous"]), fb(k))
S.append(("1", bloom("Remember", "Впізнай форму") + G + '<p class="ins"><b class="x">1</b>Present Simple or Present Continuous? Look at the verb and choose.</p>' + rows + ctl("r1", "chkRad")))
# 2 Understand
MEAN = ["a habit (usually)", "a fact (always true)", "right now", "for a short time (this week / these days)"]
rows = ""
for i, (t, a) in enumerate(C["s2"], 1):
    k = "u2_%d" % i; K[k] = [a]
    rows += '<div class="row">%d. %s<br>%s%s</div>' % (i, t, sel(k, MEAN, 330), fb(k))
S.append(("2", bloom("Understand", "Зрозумій, навіщо ця форма") + '<p class="ins"><b class="x">2</b>Why does the speaker use this tense? Choose the meaning.</p>' + rows + ctl("u2")))
# 3 Apply: verb forms
rows = ""
for i, (a, v, b, ans) in enumerate(C["s3"], 1):
    k = "a3_%d" % i; K[k] = variants(ans)
    rows += '<div class="row">%d. %s %s <span class="hintv">%s</span> %s%s</div>' % (i, a, inp(k, 190, "…"), v, b, fb(k))
S.append(("3", bloom("Apply", "Застосуй: постав дієслово у правильну форму") + '<p class="ins"><b class="x">3</b>Complete the sentences. Use the verb in brackets in Present Simple or Present Continuous.</p>' + rows + ctl("a3")))
# 4 Apply: questions
rows = ""
for i, (w, t, ans) in enumerate(C["s4"], 1):
    k = "q4_%d" % i; K[k] = variants(ans)
    rows += '<div class="row">%d. <i>%s</i> <span class="tagt">%s</span><br>%s ?%s</div>' % (i, w, "🔁 usually" if t == "S" else "▶️ now", inp(k, 460, "Write the question"), fb(k))
S.append(("4", bloom("Apply", "Застосуй: склади питання") + '<p class="ins"><b class="x">4</b>Write questions. 🔁 = Present Simple, ▶️ = Present Continuous.</p>' + rows + ctl("q4") +
          '<div class="card">🗣 Now ask your teacher your questions 1–6. Then answer them about you.</div>'))
# 5 Analyse: mistakes
rows = ""
for i, (bad, good) in enumerate(C["s5"], 1):
    k = "m5_%d" % i; K[k] = variants(good)
    rows += '<div class="row">%d. <s style="text-decoration-color:#d9534f">%s</s><br>%s%s</div>' % (i, bad, inp(k, 460, "Write the correct sentence"), fb(k))
S.append(("5", bloom("Analyse", "Проаналізуй: знайди помилку") + '<p class="ins"><b class="x">5</b>Each sentence has one mistake. Find it and write the correct sentence.</p>' + rows + ctl("m5")))
# 6 Evaluate
rows = ""
for i, (q, good, bad) in enumerate(C["s6"], 1):
    k = "e6_%d" % i; K[k] = [good]
    rows += '<div class="row"><b>— %s</b><br>%s%s</div>' % (q, "".join('<label class="opt"><input type="radio" name="%s" data-k="%s" value="%s"> %s</label>' % (k, k, o, o) for o in shuf([good, bad])), fb(k))
S.append(("6", bloom("Evaluate", "Оціни: яка відповідь краща?") + '<p class="ins"><b class="x">6</b><b>A</b> Read the questions in a team chat. Which reply is better?</p>' + rows + ctl("e6", "chkRad") +
          '<p class="ins" style="margin-top:18px"><b>B</b> Choose one question. Why is the other reply wrong? Write 1–2 sentences (you can write in Ukrainian).</p>' + ta("e6b", "In question … the reply … is wrong because …", 60)))
# 7 Create
S.append(("7", bloom("Create", "Створи свій текст") + '<p class="ins"><b class="x">7</b>%s</p>' % C["s7"] +
          '<p class="hint">Use at least 3 verbs in Present Simple and 3 in Present Continuous, and 3 words from the vocabulary box.</p>' + ta("c7", C["s7ph"], 150) +
          '<p class="hint" id="c7n">0 words</p><button class="btn l" id="c7b" disabled onclick="model(\'c7m\')">Show a model (after 10 words)</button><div class="model" id="c7m">%s</div>' % C["s7m"]))
# 8 Speak
S.append(("8", bloom("Speak", "Говоримо на уроці") + '<p class="ins"><b class="x">8</b><b>A</b> Click <b>Next card</b>. Answer in 2–3 sentences with the right tense. Then ask your teacher the same question.</p>'
          '<div class="qcard" id="qc">Click “Next card” ▶</div><div class="ctl"><button class="btn" onclick="nextCard()">Next card ▶</button><span class="res" id="qn"></span></div>'
          '<p class="ins" style="margin-top:18px"><b>B</b> Usually vs this week. Tell your teacher about a normal week and about this week. Use the chart to help you.</p>'
          '<table class="tb"><tr><th>🔁 Usually</th><th>▶️ This week / today</th></tr><tr><td>I usually … on Mondays.<br>I never …<br>I often …</td><td>This week I’m …<br>Today I’m not …<br>At the moment I’m …</td></tr></table>'
          '<div style="margin-top:20px">%s</div>' % (SELF % (C["out"] + " How well can you do this now?"))))

JS = r"""document.head.insertAdjacentHTML("beforeend",`<style>
.bloom{display:inline-block;background:#f3f4f6;border-radius:14px;padding:3px 12px;font-size:13.5px;color:#5b6478;margin:14px 0 2px}.bloom b{color:#231f20}
.gbox .two{display:grid;grid-template-columns:1fr 1fr;gap:12px}.gbox .two>div{background:#fff;border-radius:8px;padding:10px 12px}.gbox .ex{font-size:15px;color:#4d4d4f}
@media(max-width:640px){.gbox .two{grid-template-columns:1fr}}
.hintv{color:#8a8b8d;font-size:14.5px}.tagt{font-size:12.5px;background:#f3f4f6;border-radius:8px;padding:1px 8px;margin-left:6px}
.card{background:#fff7e0;border:1.5px dashed #f2b631;border-radius:8px;padding:10px 14px;margin:12px 0}
.qcard{font-size:24px;font-weight:500;text-align:center;background:#f3f4f6;border-radius:12px;padding:26px 16px;margin:10px 0;min-height:110px;display:flex;align-items:center;justify-content:center}
table.tb{border-collapse:collapse;width:100%;margin:10px 0;font-size:15.5px}table.tb th,table.tb td{border:1px solid #c8c9cb;padding:8px 12px;vertical-align:top;text-align:left}table.tb th{background:#f3f4f6}
textarea.g{overflow:hidden;resize:vertical}
</style>`);
// shuffle select options on every load (first "—" stays)
document.querySelectorAll("main select.g").forEach(s=>{const o=[...s.options].slice(1);o.sort(()=>Math.random()-.5);o.forEach(x=>s.appendChild(x))});
document.querySelectorAll("main .row,main .tf").forEach(r=>{const L=[...r.querySelectorAll(":scope>label.opt")];if(L.length>2){const f=r.querySelector(".fb");L.sort(()=>Math.random()-.5).forEach(l=>r.insertBefore(l,f))}});
// answers: highlight first, show the right answer only on the 2nd try
const TRIES={};let REVEAL=false;
function fbk(k,ok,txt){const f=$("fb_"+k);if(!f)return;f.className="fb show "+(ok?"ok":"no");f.querySelector(".h").innerHTML=ok?"✓":(REVEAL?txt:"✗ Try again")}
const _cs=chkSet,_cr=chkRad;
window.chkSet=function(p){TRIES[p]=(TRIES[p]||0)+1;REVEAL=TRIES[p]>1;_cs(p)};window.chkRad=function(p,w){TRIES[p]=(TRIES[p]||0)+1;REVEAL=TRIES[p]>1;_cr(p,w)};
// auto-grow textareas + word counter + model unlock
function grow(t){t.style.height="auto";t.style.height=Math.max(t.scrollHeight+2,60)+"px"}
function wc(){const t=document.querySelector('.g[data-k="c7"]');if(!t)return;const n=(t.value.trim().match(/\S+/g)||[]).length;$("c7n").textContent=n+" words";$("c7b").disabled=n<10}
document.addEventListener("input",e=>{if(e.target.tagName==="TEXTAREA")grow(e.target);wc()});
window.afterFill=()=>{document.querySelectorAll("textarea.g").forEach(grow);wc()};
// speaking cards
const CARDS=__CARDS__;let cd=[],cn=0;
function nextCard(){if(!cd.length)cd=CARDS.slice().sort(()=>Math.random()-.5);const q=cd.pop();cn++;$("qc").textContent=q;$("qn").textContent="Card "+cn;try{const u=new SpeechSynthesisUtterance(q);u.lang="en-GB";u.rate=.9;speechSynthesis.cancel();speechSynthesis.speak(u)}catch(e){}}
// before sending: warn about empty answers; after: "Sent ✓ · Send again"
(()=>{const b=$("submit");if(!b)return;const orig=b.onclick;let warned=false;
 b.onclick=async()=>{const empty=[...document.querySelectorAll("main .g[data-k]")].filter(x=>x.dataset.k!=="q"&&!x.value).length+[...new Set([...document.querySelectorAll("main input[type=radio][data-k]")].map(x=>x.dataset.k))].filter(k=>!document.querySelector(`input[data-k="${k}"]:checked`)).length;
  if(empty&&!warned){warned=true;b.textContent=empty+" tasks without an answer. Send anyway?";return}
  await orig();b.textContent="Sent ✓ · Send again";warned=false}})();
"""
js = JS.replace("__CARDS__", __import__("json").dumps(C["cards"], ensure_ascii=False))
acc, acc2, dark, gr = C["acc"]
html = page(C["num"], C["title"], "GRAMMAR REVIEW", "Present Simple (usually) and Present Continuous (now) with the words from lessons 1.1–1.3.",
            C["key"], CODE, S, K, C["voc"], acc=acc, acc2=acc2, dark=dark, grad2=gr, footer="", extra_js=js)
open(OUT, "w").write(html); print("ok", OUT, len(html))
