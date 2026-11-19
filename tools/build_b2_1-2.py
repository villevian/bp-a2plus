"""Business Partner B2 · 1.2 Employee retention — LESSON (updated 2026: AI layoffs, rehiring, what keeps people).
Mirrors coursebook pp. 10–11: Lead-in 1–2 · Reading 3–4 · Grammar 5A–C, 6 (Future Continuous & Future Perfect Simple) · Speaking 7A–B · Self-assessment.
Usage: python3 build_b2_1-2.py OUT.html [STUDENT_CODE]
"""
import sys, os, random
from bp_page import page, fb, sel, inp, ta, ctl, SELF
from vocab_b2 import lesson
import vcard
from b2_1_2_data import *
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#5b5fc7", "#e8e9fa", "#4044a8", "#7b7fe0"
_, GROUPS = lesson("1.2")
VOC, VJS = vcard.build(GROUPS, ACC, ACC2, DARK)
K = {}
random.seed(102)
def radio(k, opts):
    return "".join('<label class="opt" style="display:inline;margin:0 10px 0 0"><input type="radio" name="%s" data-k="%s" value="%s"> %s</label>' % (k, k, o, o) for o in opts)
def alts(a): return [x.strip() for x in a.split("|")]
ART = ('<div class="art"><div class="ah">%s</div>%s<p class="src">%s</p></div>' % (TITLE, "".join("<p>%s</p>" % p for p in ARTICLE), SOURCES))

# 1–2 Lead-in
WORDS = [w for w, _ in EX1]
for i, (w, _) in enumerate(EX1): K["l1_%d" % (i + 1)] = [w]
s1 = ('<div class="bsec">Lead-in</div><p class="ins"><b class="x">1</b>Match the words and phrases in the box with the definitions.</p>'
      '<div class="box">%s</div>' % " · ".join(sorted(WORDS)) +
      "".join('<div class="row">%d. %s %s%s</div>' % (i + 1, d, sel("l1_%d" % (i + 1), sorted(WORDS), 170), fb("l1_%d" % (i + 1))) for i, (_, d) in enumerate(EX1)) + ctl("l1") +
      '<p class="ins" style="margin-top:22px"><b class="x">2</b>Work in pairs or small groups. Discuss the terms in Exercise 1 and what you think their effect might be on employee retention.</p>'
      '<div class="card">In 2026, many companies are cutting jobs “because of AI”. <b>Which of the five things in Exercise 1 would make you stay in a company like that? Which would not be enough?</b></div>' +
      ta("l2", "I think diverse work / a sabbatical … would (not) make people stay because …", 80))

# 3 Reading
s2 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">3</b>Read the article quickly. What details does it mention about the terms in Exercise 1? What other ideas for employee retention does the article mention?</p>'
      '<p class="eg"><i>The text says AI can take over menial tasks, so people can do more diverse work.</i></p>' + ART +
      ta("r3", "The text says … / Other ideas: …", 80) +
      '<button class="btn l" onclick="model(\'m3\')">Show possible answers</button><div class="model" id="m3">'
      '<b>Terms from Exercise 1:</b> AI can take over <i>menial tasks</i>; young people want <i>diverse work</i>, clear <i>promotion</i> paths, a healthy <i>work-life balance</i> and, at some firms, a paid <i>sabbatical</i>.<br>'
      '<b>Other ideas:</b> keep hiring juniors (IBM) so you have tomorrow’s managers; learning and development; don’t lose institutional knowledge; use AI to augment people, not replace them; show staff that the company will invest in them in the future.</div>')

# 4 True / False
for i, (_, a, _) in enumerate(TF): K["t4_%d" % (i + 1)] = [a]
s3 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">4</b>Read the article again and decide if these sentences are <i>true</i> (T) or <i>false</i> (F).</p>'
      '<details class="rd"><summary>📄 Open the article</summary>%s</details>' % ART +
      "".join('<div class="tf"><span class="q">%d. %s</span>%s%s</div>' % (i + 1, q, radio("t4_%d" % (i + 1), "TF"), fb("t4_%d" % (i + 1))) for i, (q, _, _) in enumerate(TF)) +
      ctl("t4", "chkRad") + '<button class="btn l" onclick="model(\'m4\')" style="margin-left:8px">Show explanations</button><div class="model" id="m4">%s</div>' %
      "<br>".join("%d %s %s" % (i + 1, a, c) for i, (_, a, c) in enumerate(TF)))

# 5A–C Grammar
for i, (_, a) in enumerate(UNDERLINED): K["g5_%d" % (i + 1)] = [a]
TL = ('<div class="tl"><div><b>1</b> We use the <b>Future Continuous</b> to talk about an event that will be taking place at a particular moment in the future.'
      '<div class="ax">now ────────── <span>〰〰<b>✕</b>〰〰</span> ────► future</div><i>Next Friday at 5 p.m. I’ll be presenting the release.</i></div>'
      '<div><b>2</b> We use the <b>Future Perfect Simple</b> to talk about events in the future which will be finished by a certain time.'
      '<div class="ax">now ──── <b>●</b> ───── <b>✕</b> ────► future</div><i>By next Friday I’ll have finished the release.</i></div></div>')
s4 = ('<div class="bsec">Grammar <span class="sub">Future Continuous and Future Perfect Simple</span></div>'
      '<p class="ins"><b class="x">5</b><b>A</b> Look at the underlined verb forms in the article and match them with the definitions of the Future Continuous (1) and Future Perfect Simple (2).</p>' + TL +
      "".join('<div class="row">%d. <u>%s</u> %s%s</div>' % (i + 1, f, sel("g5_%d" % (i + 1), ["FC", "FP"], 90), fb("g5_%d" % (i + 1))) for i, (f, _) in enumerate(UNDERLINED)) + ctl("g5") +
      '<p class="hint">FC = Future Continuous (definition 1) · FP = Future Perfect Simple (definition 2)</p>')
for i, (_, a) in enumerate(TIME): K["g5b_%d" % (i + 1)] = [a]
TOPT = sorted(set(a for _, a in TIME))
C = [("The Future Continuous is formed with", ["will"], "+", ["be"], "+", ["present|-ing|present (-ing)"], "participle."),
     ("The Future Perfect Simple is formed with", ["will"], "+", ["have"], "+", ["past"], "participle.")]
n = 0
crow = ""
for parts in C:
    row = ""
    for x in parts:
        if isinstance(x, list):
            n += 1; K["g5c_%d" % n] = alts(x[0]); row += " " + inp("g5c_%d" % n, 95) + fb("g5c_%d" % n) + " "
        else: row += x
    crow += '<div class="row">%s</div>' % row
s5 = ('<div class="bsec">Grammar</div><p class="ins"><b class="x">5</b><b>B</b> What information can you find near the underlined verb forms in the article that tells you when each action will take place?</p>'
      '<p class="eg"><i><u>In a few years</u> they will be poaching mid-level staff …</i></p>' +
      "".join('<div class="row">%d. <u>%s</u> → %s%s</div>' % (i + 1, f, sel("g5b_%d" % (i + 1), TOPT, 210), fb("g5b_%d" % (i + 1))) for i, (f, _) in enumerate(TIME)) + ctl("g5b") +
      '<p class="ins" style="margin-top:22px"><b>C</b> How are the Future Continuous and the Future Perfect Simple formed?</p>' + crow + ctl("g5c"))

# 6
BOXV = ["change", "do", "improve", "promote", "rest", "take"]
for i, (_, a, _) in enumerate(EX6): K["g6_%d" % (i + 1)] = alts(a)
s6 = ('<div class="bsec">Grammar</div><p class="ins"><b class="x">6</b>Complete the sentences with the Future Continuous or Future Perfect Simple forms of the verbs in the box. Consider if they will be in progress or will be finished.</p>'
      '<div class="box">%s</div>' % " · ".join(BOXV) +
      "".join('<div class="row">%d. %s %s %s%s</div>' % (i + 1, a, inp("g6_%d" % (i + 1), 190), b, fb("g6_%d" % (i + 1))) for i, (a, _, b) in enumerate(EX6)) + ctl("g6"))

# 7 Speaking
for i, (_, a, _) in enumerate(EX7): K["s7_%d" % (i + 1)] = alts(a)
s7 = ('<div class="bsec wr">Speaking</div><p class="ins"><b class="x">7</b><b>A</b> Complete the questions with the Future Continuous or Future Perfect Simple forms of the verbs in brackets.</p>' +
      "".join('<div class="row">%d. %s %s %s%s</div>' % (i + 1, a, inp("s7_%d" % (i + 1), 210), b, fb("s7_%d" % (i + 1))) for i, (a, _, b) in enumerate(EX7)) + ctl("s7") +
      '<p class="ins" style="margin-top:22px"><b>B</b> In pairs or small groups, ask and answer the questions in Exercise 7A.</p>'
      '<div class="card">🎮 After this, open <b>Speaking &amp; Games</b> for the board-meeting simulation and the $1M budget game.</div><div class="card"><b>Extra questions:</b> Will AI have changed your job by 2030? How? · Who made the smarter decision — IBM (more juniors) or Salesforce (4,000 fewer support staff)? Why? · What will your company be doing to keep good people?</div>' +
      ta("s7b", "Notes for your answers …", 80) + '<div style="margin-top:20px">%s</div>' % (SELF % "I can use the Future Continuous and Future Perfect Simple to talk about the future. How well can you do this now?"))


# ★ In-lesson vocabulary + speaking (extra, after the coursebook reading)
import re, html as _h
HUNT = ["pause hiring", "tripling its entry-level hiring", "poaching mid-level staff", "let 45 call-centre staff go", "reversed its decision",
        "made people redundant", "rehired staff", "a cost-cutting exercise", "institutional knowledge leaves with them", "menial tasks", "augment people, not replace them"]
def hunt_html():
    out = ""
    for p in ARTICLE:
        p = re.sub(r"</?u>", "", p)
        for i, c in enumerate(HUNT):
            p = p.replace(c, "\x00%d\x00" % i)
        parts = re.split("\x00", p); res = ""
        for j, part in enumerate(parts):
            if j % 2 == 1: res += '<span class="ck" data-c="%s">%s</span>' % (part, HUNT[int(part)])
            else: res += re.sub(r"(\S+)", r'<span class="wd">\1</span>', part)
        out += "<p>%s</p>" % res
    return out
for c in HUNT: assert any(c in re.sub(r"</?u>", "", p) for p in ARTICLE), c
sCH = ('<div class="bsec">★ Vocabulary</div><p class="ins"><b class="x">★</b>Chunk hunt. Find <b>%d chunks</b> in the article about <i>cutting jobs</i>, <i>bringing people back</i> or <i>keeping people</i>. Click on a chunk — if it’s a target, it turns green.</p>' % len(HUNT) +
       '<div class="art hunt">%s</div><div class="tbar"><span class="tm" id="hs">0 / %d found</span><button class="btn l" onclick="huntHint()">💡 Hint</button><button class="btn l" onclick="huntShow()">Show all</button></div>' % (hunt_html(), len(HUNT)) +
       '<p class="hint" id="hh"></p>')
TALKQ = [("Would you stay in a company that has just laid off 20% of its staff?", "stay out of fear, not loyalty"),
         ("Is it smart to stop hiring juniors because AI can do their tasks?", "build the talent pipeline"),
         ("Your company replaced support agents with a bot. Customers are angry. What now?", "reverse a decision"),
         ("What do experienced people take with them when they leave?", "institutional knowledge"),
         ("What would you do with a month-long paid sabbatical?", "take a sabbatical"),
         ("Which menial tasks in your job could AI take over tomorrow?", "take over menial tasks"),
         ("Is ‘we’re cutting jobs because of AI’ always true?", "AI washing"),
         ("A rival offers your best developer +30%. What do you do?", "poach staff")]
sTK = ('<div class="bsec wr">★ Speaking</div><p class="ins"><b class="x">★</b>Talk with a chunk. Take a card and answer for 60 seconds. You <b>must</b> use the chunk on the card — and try to add one more from the lesson.</p>'
       '<div class="qc"><div id="tkq">Click “New card”</div><div class="must" id="tkm"></div></div>'
       '<div class="tbar"><button class="btn" onclick="tkNew()">🔀 New card</button><button class="btn l" onclick="tkT()">⏱ 60 s</button><span class="tm" id="tkt">60</span></div>')
XJS_ADD = r"""
const HUNT=__HUNT__,TALKQ=__TALKQ__;let hf=new Set();
document.addEventListener("click",e=>{const c=e.target.closest(".hunt .ck");if(c){c.classList.add("got");hf.add(c.dataset.c);document.getElementById("hs").textContent=hf.size+" / "+HUNT.length+" found"+(hf.size===HUNT.length?" ✓ Well done!":"");return}
 const w=e.target.closest(".hunt .wd");if(w){w.classList.add("miss");setTimeout(()=>w.classList.remove("miss"),500)}});
function huntHint(){const left=HUNT.map((c,i)=>[c,i]).filter(([c,i])=>!hf.has(String(i)));if(!left.length)return;const[c]=left[Math.floor(Math.random()*left.length)];document.getElementById("hh").textContent="💡 Look for a chunk that starts with “"+c.split(" ")[0]+" …”"}
function huntShow(){document.querySelectorAll(".hunt .ck").forEach(c=>c.classList.add("show"))}
let tki=-1,tkq=[...TALKQ].sort(()=>Math.random()-.5),tkI=null;function tkNew(){tki=(tki+1)%tkq.length;document.getElementById("tkq").textContent=tkq[tki][0];document.getElementById("tkm").innerHTML="Must use: <b>"+tkq[tki][1]+"</b>"}
function tkT(){clearInterval(tkI);let t=60;const el=document.getElementById("tkt");el.textContent=t;tkI=setInterval(()=>{t--;el.textContent=t;if(t<=0){clearInterval(tkI);el.textContent="⏰"}},1000)}
document.head.insertAdjacentHTML("beforeend",`<style>.hunt span{cursor:pointer;border-radius:3px}.hunt .wd.miss{background:#fdecec}.hunt .ck.got{background:#c9f0d6;font-weight:600}.hunt .ck.show:not(.got){background:#fff3c4}
.tbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:10px 0}.tm{font-weight:600;color:#4044a8;background:#e8e9fa;border-radius:6px;padding:4px 12px}
.qc{background:#4044a8;color:#fff;border-radius:12px;padding:22px;text-align:center;font-size:21px;margin:10px 0}.qc .must{margin-top:10px;font-size:16px;color:#ffe08a}</style>`);"""

XJS = VJS + XJS_ADD.replace('__HUNT__', __import__('json').dumps(HUNT)).replace('__TALKQ__', __import__('json').dumps(TALKQ, ensure_ascii=False)) + r"""
document.head.insertAdjacentHTML("beforeend",`<style>
.art{background:#fdf6ec;border:1px solid #f0dcc0;border-radius:8px;padding:14px 22px;margin:12px 0;font-family:Georgia,serif;font-size:16.5px;line-height:1.6}
.art .ah{font-size:24px;font-weight:700;line-height:1.25;margin-bottom:8px}.art p{margin:8px 0}.art u{text-decoration-color:#4044a8;text-decoration-thickness:2px}.art .src{font-family:"Fira Sans",sans-serif;font-size:13px;color:#888}
details.rd summary{cursor:pointer;color:#4044a8;font-weight:500;margin:6px 0}
.tl{display:grid;grid-template-columns:1fr 1fr;gap:16px;border:1.5px solid #c8c9cb;border-radius:8px;padding:12px 16px;margin:10px 0;font-size:15px}@media(max-width:700px){.tl{grid-template-columns:1fr}}
.tl .ax{font-family:monospace;color:#4044a8;margin:8px 0;white-space:nowrap;overflow:auto}.tl i{color:#4044a8}
.eg{color:#4044a8}.box{border:1.5px solid #c8c9cb;border-radius:6px;padding:6px 12px;display:inline-block;margin:6px 0 10px}</style>`);"""
secs = [("1–2", s1), ("3", s2), ("4", s3), ("★ Chunks", sCH), ("★ Talk", sTK), ("5A", s4), ("5B–C", s5), ("6", s6), ("7", s7)]
h = page("1.2", "Employee retention", "LESSON", "Learners can use the Future Continuous and the Future Perfect Simple to talk about events that are taking place or that have finished at a point in the future.",
         "BP B2 1.2 Employee retention · Lesson", CODE, secs, K, VOC, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2,
         footer="Article written for this course from 2025–2026 news reports. ", extra_js=XJS)
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True); open(OUT, "w").write(h); print("ok lesson", len(h))
