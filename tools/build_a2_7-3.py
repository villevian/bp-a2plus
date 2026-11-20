"""Business Partner A2 · 7.3 The best providers — LESSON (mobile operators for company eSIMs).
Structure mirrors the coursebook lesson 7.3: Lead-in 1A–B · Reading 2 (email: Strengths / Areas of improvement + good/bad table) · 3 Email phrases ·
Communicative grammar: Superlatives (+ Pronunciation bank /p/ /b/ /f/ /v/) · 4A–B · Writing 5 · Self-assessment.
Real operators (Kyivstar, Vodafone, lifecell) and real ratings only in the lead-in; in Reading/Writing the operators are invented (SkyMobile, Volt, LineUp, NovaTel).
Writing: Updated = Slack message recommending an operator; Classic = book task (email about Travel Care and two other travel companies).
Usage: python3 build_a2_7-3.py ROOT_LESSON_DIR [STUDENT_CODE]   e.g. ../../bp-a2/lessons/7-3
"""
import sys, os, json, re
from bp_page import page, fb, sel, inp, ta, ctl, SELF
from vocab_a2 import lesson
ROOT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3b7dd8", "#e3eefb", "#2a5fb0", "#4f9be8"
TITLE, GROUPS = lesson("7.3")
K = {}

# reuse chip/card CSS+JS from 7.2
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_a2_7-2.py")).read()
CSS = _src[_src.index('CSS = r"""') + 10:_src.index('"""', _src.index('CSS = r"""') + 10)]
JS = _src[_src.index('JS = r"""') + 9:_src.index('"""', _src.index('JS = r"""') + 9)]

VITEMS, VOC = [], []
for g, ws in GROUPS:
    chips = []
    for en, uk, df, ex, co in ws:
        VITEMS.append({"en": en, "uk": uk, "df": df, "ex": ex, "co": co})
        chips.append('<a class="vw" data-i="%d">%s</a>' % (len(VITEMS) - 1, en))
    VOC.append((g, chips))

def tf(k, q, opts):
    return '<div class="tf"><span class="q">%s</span>%s%s</div>' % (q, "".join('<label class="opt" style="display:inline;margin:0 12px 0 0"><input type="radio" name="%s" data-k="%s" value="%s"> %s</label>' % (k, k, v, l) for v, l in opts), fb(k))

# ---------- 1A ----------
BOX1 = ["mobile operator", "internet provider", "energy provider", "office cleaning service", "printer / photocopier contract", "cloud storage", "coworking space", "food delivery for the office"]
FACTS = ('<div class="dyk"><b>📊 Did you know?</b> Different reports — different “best” operators in Ukraine:'
         '<ul><li><b>Ookla Speedtest</b> (July–December 2024): Kyivstar had <b>the best coverage</b> and <b>the fastest network</b>. Speed score: Kyivstar 35.65 · Vodafone 33.38 · lifecell 29.42.</li>'
         '<li><b>nPerf</b> (2024): Vodafone had <b>the highest total score</b> (60,573), then Kyivstar (59,339) and lifecell (57,054). But lifecell had <b>the fastest average download speed</b> — 24.57 Mb/s.</li></ul>'
         '<i>So which is the best? It depends on the report!</i></div>')
s1 = ('<div class="bsec">Lead-in</div><p class="ins"><b class="x">1</b><b>A</b> Work in pairs. Which of these service providers do you or your company use? Are you happy with them?</p>'
      '<div class="chips">%s</div>' % "".join("<span>%s</span>" % b for b in BOX1) +
      '<div class="card">Example: <i>My company uses Kyivstar for our phones. I’m happy with the coverage, but the business tariff is expensive.</i></div>' +
      ta("l1a", "My company uses … I’m (not) happy with …", 80) + FACTS +
      '<p class="ins">Which operator do you use? Do you agree with the reports?</p>' + ta("l1a2", "I use … I think it has the best / the worst …", 50))

# ---------- 1B ----------
CRIT = ["value for money", "network coverage", "service reliability", "staff knowledge", "problem solving", "satisfied customers", "quality of communication", "easy to access (24/7 chat)"]
s2 = ('<div class="bsec">Lead-in</div><p class="ins"><b>B</b> Your company needs a mobile operator for 25 company eSIMs. Put these things in order of importance (1 = the most important). Then compare with your teacher.</p>' +
      "".join('<div class="row">%s <span style="margin-left:8px">%s</span></div>' % (sel("r1b_%d" % (i + 1), [str(n) for n in range(1, 9)], 70), c) for i, c in enumerate(CRIT)) +
      '<p class="hint">Say: For me, … is the most important because … · … is not very important for our team.</p>' + ta("l1b", "For me, … is the most important because …", 60))

# ---------- 2 Reading ----------
EMAIL = ('<div class="mail"><div class="mh"><b>From:</b> Iryna Koval (Office Manager)<br><b>To:</b> Pavlo<br><b>Subject:</b> Mobile operator survey — SkyMobile</div>'
         '<p>Hi Pavlo,</p><p>Please find attached a copy of the customer survey you asked me to do. We compared SkyMobile with two other operators, Volt and LineUp, for our 25 company eSIMs. Please find a summary below.</p>'
         '<p><b>Strengths</b><br>SkyMobile has:</p><ul><li><b>the best</b> network coverage — it works in the metro and in small towns.</li>'
         '<li><b>the fastest</b> download speed: 31 Mbps on average.</li><li><b>the best</b> value for money: a business tariff for €9 per user per month with 40 GB.</li></ul>'
         '<p><b>Areas of improvement</b><br>SkyMobile has:</p><ul><li><b>the lowest</b> number of satisfied business clients (only 52%).</li>'
         '<li><b>the longest</b> wait for support: 25 minutes in the chat.</li><li><b>the worst</b> problem solving: they fix only 4 problems out of 10 on the first day.</li></ul>'
         '<p>If you have any questions, please let me know.</p><p>Best regards,<br>Iryna</p></div>')
T2 = [("Network coverage", "g"), ("Download speed", "g"), ("Satisfied customers (business clients)", "b"), ("Time to answer support chats", "b"), ("Problem solving", "b"), ("Value for money", "g")]
for i, (_, a) in enumerate(T2): K["t2_%d" % (i + 1)] = [a]
s3 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">2</b>Your company asked a colleague to compare mobile operators. Read her email about SkyMobile and tick (✓) <i>good performance</i> or <i>bad performance</i> in the table.</p>'
      + EMAIL + '<div class="gbt"><div class="gbh"><span></span><span>Good performance</span><span>Bad performance</span></div>' +
      "".join('<div class="gbr"><span>%s</span>%s</div>' % (c, "".join('<label><input type="radio" name="t2_%d" data-k="t2_%d" value="%s"> ✓</label>' % (i + 1, i + 1, v) for v in "gb") + fb("t2_%d" % (i + 1))) for i, (c, _) in enumerate(T2)) +
      '</div>' + ctl("t2", "chkRad") +
      '<p class="ins" style="margin-top:20px">Would you choose SkyMobile for your team? Why? / Why not?</p>' + ta("r2", "I would / wouldn’t choose SkyMobile because …", 50))

# ---------- 3 Phrases ----------
P3 = [("Please find attached …", "b"), ("Please find a summary below.", "d"), ("If you have any questions, please let me know.", "a"), ("Best regards,", "c")]
F3 = [("a", "offer more help"), ("b", "send a document with the email"), ("c", "end the email"), ("d", "introduce the main information")]
for i, (_, a) in enumerate(P3): K["p3_%d" % (i + 1)] = [a]
s4 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">3</b>Match the phrases from the email (1–4) with their uses (a–d).</p>'
      '<div class="chips">%s</div>' % "".join("<span><b>%s</b> %s</span>" % (l, t) for l, t in F3) +
      "".join('<div class="row">%d. <i>%s</i> %s%s</div>' % (i + 1, p, sel("p3_%d" % (i + 1), ["a", "b", "c", "d"], 70), fb("p3_%d" % (i + 1))) for i, (p, _) in enumerate(P3)) + ctl("p3") +
      '<p class="ins" style="margin-top:22px">In a Slack message you can say it shorter. Match: </p><div class="two">'
      '<div class="card">📎 <i>Please find attached …</i> → <b>Attached is …</b> / <b>Here’s the file 👇</b></div>'
      '<div class="card">📋 <i>Please find a summary below.</i> → <b>Quick summary:</b></div>'
      '<div class="card">❓ <i>If you have any questions, please let me know.</i> → <b>Any questions — just ping me!</b></div>'
      '<div class="card">👋 <i>Best regards,</i> → <b>Thanks!</b> (or nothing)</div></div>')

# ---------- Grammar + 4A ----------
GB = ('<div class="gbox"><div class="gh">Comparing (2): Superlatives</div>'
      '<p>We use superlatives to compare one thing with <b>two or more</b> things in the same group.</p>'
      '<table class="tb"><tr><th>adjective</th><th>superlative</th><th>example</th></tr>'
      '<tr><td>short: cheap, fast, low, long</td><td><b>the</b> cheap<b>est</b>, <b>the</b> fast<b>est</b></td><td>Volt is <b>the cheapest</b> operator.</td></tr>'
      '<tr><td>-e: wide, safe</td><td><b>the</b> wid<b>est</b></td><td>SkyMobile has <b>the widest</b> coverage.</td></tr>'
      '<tr><td>-y: friendly, easy</td><td><b>the</b> friendl<b>iest</b></td><td>LineUp has <b>the friendliest</b> staff.</td></tr>'
      '<tr><td>one vowel + consonant: big, hot</td><td><b>the</b> big<b>gest</b></td><td>Kyivstar is <b>the biggest</b> operator in Ukraine.</td></tr>'
      '<tr><td>long: reliable, knowledgeable, expensive</td><td><b>the most</b> reliable</td><td>It’s <b>the most reliable</b> provider.</td></tr>'
      '<tr><td>irregular: good / bad / far</td><td><b>the best</b> / <b>the worst</b> / <b>the furthest</b></td><td>They have <b>the worst</b> support.</td></tr></table>'
      '<p class="hint">Compare: 7.1 comparatives — Volt is <i>cheaper than</i> SkyMobile (2 things). 7.3 superlatives — Volt is <i>the cheapest</i> (3 or more).</p></div>')
PRON = ('<div class="gbox"><div class="gh">Pronunciation bank: /p/, /b/, /f/ and /v/</div><p>Listen and repeat. Click 🔊.</p><div class="two">' +
        "".join('<div class="row">%s <i style="color:#6d6e70">%s</i> <button class="btn l" style="padding:2px 10px" onclick="say1(\'%s\')">🔊</button></div>' % (w, s, w)
                for w, s in [("price", "/p/"), ("best", "/b/"), ("fast", "/f/"), ("value", "/v/"), ("provider", "/p/ /v/"), ("problem", "/p/ /b/"), ("the fastest provider", "/f/ /p/ /v/"), ("the best value for money", "/b/ /v/ /f/")]) +
        '</div></div>')
G4A = [("LineUp has ", " (short) wait for support: only 2 minutes.", ["the shortest"]), ("Volt’s business tariff is ", " (cheap): €6 per user.", ["the cheapest"]),
       ("SkyMobile is ", " (reliable) operator — no problems in three years.", ["the most reliable"]), ("Volt has ", " (knowledgeable) support staff. They know everything about eSIMs.", ["the most knowledgeable"]),
       ("The people at LineUp are ", " (friendly) — they always smile on video calls.", ["the friendliest"]), ("SkyMobile has ", " (wide) network coverage in the country.", ["the widest"]),
       ("LineUp has ", " (high) number of satisfied customers: 91%.", ["the highest"]), ("Volt offers ", " (good) value for money.", ["the best"])]
for i, (_, _, a) in enumerate(G4A): K["g4a_%d" % (i + 1)] = a
s5 = ('<div class="bsec">Communicative grammar</div>' + GB + PRON)
s6 = ('<div class="bsec">Communicative grammar</div><p class="ins"><b class="x">4</b><b>A</b> Complete the sentences with the superlative form of the adjectives in brackets.</p>'
      '<div class="card">Example: <i>LineUp has <b>the shortest</b> wait for support.</i></div>' +
      "".join('<div class="row">%d. %s%s%s%s</div>' % (i + 1, a, inp("g4a_%d" % (i + 1), 190), b, fb("g4a_%d" % (i + 1))) for i, (a, b, _) in enumerate(G4A)) + ctl("g4a"))

# ---------- 4B ----------
TAB4 = ('<table class="tb stars"><tr><th></th><th>SkyMobile</th><th>Volt</th><th>LineUp</th></tr>'
        '<tr><td>Reliability</td><td>★★★</td><td>★★</td><td>★</td></tr><tr><td>Customer service</td><td>★★</td><td>★★★</td><td>★</td></tr>'
        '<tr><td>Staff knowledge</td><td>★</td><td>★★</td><td>★★★</td></tr><tr><td>Price per user</td><td>€9</td><td>€6</td><td>€11</td></tr>'
        '<tr><td>Problem solving</td><td>★</td><td>★★</td><td>★★★</td></tr><tr><td>Business clients</td><td>4,000</td><td>7,500</td><td>12,000</td></tr></table>')
G4B = [("SkyMobile is ", " operator.", ["the most reliable"]), ("Volt has ", " customer service.", ["the best"]), ("LineUp has ", " staff.", ["the most knowledgeable"]),
       ("Volt has ", " prices.", ["the lowest"]), ("SkyMobile has ", " problem solving.", ["the worst"]), ("LineUp has ", " number of business clients.", ["the biggest", "the highest", "the largest"])]
for i, (_, _, a) in enumerate(G4B): K["g4b_%d" % (i + 1)] = a
s7 = ('<div class="bsec">Communicative grammar</div><p class="ins"><b>B</b> Look at the table. Complete the sentences with superlatives.</p>' + TAB4 +
      "".join('<div class="row">%d. %s%s%s%s</div>' % (i + 1, a, inp("g4b_%d" % (i + 1), 200), b, fb("g4b_%d" % (i + 1))) for i, (a, b, _) in enumerate(G4B)) + ctl("g4b") +
      '<p class="ins" style="margin-top:22px">Your turn: which operator would you choose for your team? Use two superlatives.</p>' + ta("y4b", "I would choose … because it has the … and the …", 50))

# ---------- 5 Writing ----------
TAB_UP = ('<table class="tb stars"><tr><th></th><th>Volt</th><th>LineUp</th><th>NovaTel</th></tr>'
          '<tr><td>Network coverage</td><td>★★</td><td>★★★</td><td>★</td></tr><tr><td>Download speed</td><td>22 Mbps</td><td>27 Mbps</td><td>30 Mbps</td></tr>'
          '<tr><td>Price per user per month</td><td>€6</td><td>€11</td><td>€8</td></tr><tr><td>Wait for support (chat)</td><td>5 min</td><td>2 min</td><td>20 min</td></tr>'
          '<tr><td>Satisfied business clients</td><td>78%</td><td>91%</td><td>60%</td></tr><tr><td>eSIM set-up</td><td>in the app</td><td>in the app</td><td>only in a shop</td></tr></table>')
MODEL_UP = ("Hi Olha! 👋 Attached is the operator comparison for our 25 eSIMs. Quick summary:\n"
            "I recommend LineUp. Strengths: LineUp has the best network coverage, the shortest wait for support (2 minutes in the chat) and the most satisfied business clients (91%). You can set up an eSIM in the app.\n"
            "Areas of improvement: LineUp has the highest price — €11 per user per month. Volt is the cheapest, and NovaTel has the fastest download speed, but NovaTel has the worst support.\n"
            "Any questions — just ping me! Thanks!")
s8 = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">5</b>Your team lead, Olha, asks you in Slack: <i>“Which operator for our company eSIMs?”</i> Look at the table and write a message (60–100 words). '
      'Recommend one operator. Use <b>Strengths</b> / <b>Areas of improvement</b>, superlatives and phrases from Exercise 3.</p>' + TAB_UP +
      '<div class="slack"><div><b>Olha (Team Lead)</b><span class="t">09:15</span></div><p>Hi! Which operator for our company eSIMs? We need to decide by Friday 🙏</p></div>' +
      ta("w5", "Hi Olha! Attached is … Quick summary: I recommend … Strengths: … has the best … Areas of improvement: …", 200) + '<p class="hint" id="w5c"></p>'
      '<button class="btn l" onclick="model(\'m5\')">Show a model answer</button><div class="model" id="m5">%s</div>' % MODEL_UP +
      '<div style="margin-top:20px">%s</div>' % (SELF % "I can compare services. How well can you do this now?"))

TAB_CL = ('<table class="tb stars"><tr><th></th><th>Travel Care</th><th>Sun Tours</th><th>Go Travel</th></tr>'
          '<tr><td>Staff knowledge</td><td>★★★</td><td>★★</td><td>★</td></tr><tr><td>Friendly staff</td><td>★★★</td><td>★</td><td>★★</td></tr>'
          '<tr><td>Customer service</td><td>★★★</td><td>★★</td><td>★★</td></tr><tr><td>Prices</td><td>£££</td><td>££</td><td>£</td></tr><tr><td>Value for money</td><td>★</td><td>★★</td><td>★★★</td></tr></table>')
MODEL_CL = ("Dear …\nPlease find attached a copy of the customer satisfaction survey you asked me to perform.\nWe compared Travel Care and two other travel companies. Please find a summary below.\n"
            "Strengths:\nTravel Care has:\n• the most knowledgeable staff.\n• the friendliest staff.\n• the best customer service.\n"
            "Areas of improvement:\nTravel Care has:\n• the highest prices.\n• the worst value for money.\nLet me know if you have any questions.\nBest regards,\nMartina")
s8c = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">5</b>You work for a marketing research company. You compared a travel company, Travel Care, with two other travel companies. '
       'Look at the table and write an email to your manager about Travel Care. Use the email in Exercise 2 as a model: <b>Strengths</b> / <b>Areas of improvement</b>, superlatives and phrases from Exercise 3.</p>' + TAB_CL +
       ta("w5", "Dear … Please find attached … Please find a summary below. Strengths: Travel Care has …", 200) + '<p class="hint" id="w5c"></p>'
       '<button class="btn l" onclick="model(\'m5\')">Show a model answer</button><div class="model" id="m5">%s</div>' % MODEL_CL +
       '<div style="margin-top:20px">%s</div>' % (SELF % "I can compare services. How well can you do this now?"))

EXTRA_CSS = r"""
document.head.insertAdjacentHTML("beforeend",`<style>
.dyk{background:#fff8e6;border-left:5px solid #f0b429;padding:10px 16px;margin:14px 0;font-size:15.5px}.dyk ul{margin:6px 0;padding-left:20px}
.mail{border:1px solid #d5d6d7;border-radius:8px;padding:6px 18px;background:#fff;margin:10px 0;font-size:16px}.mail .mh{background:#f3f4f6;margin:4px -18px 8px;padding:8px 18px;font-size:14.5px;line-height:1.6}
.mail ul{margin:4px 0;padding-left:22px}.gbt{max-width:640px;margin:12px 0;border:1px solid #d5d6d7}.gbh,.gbr{display:grid;grid-template-columns:1fr 130px 130px;align-items:center}
.gbh{background:ACC2;font-weight:600;color:DARK;font-size:14px}.gbh span,.gbr span,.gbr label{padding:7px 10px}.gbr{border-top:1px solid #eee}.gbr label{text-align:center;cursor:pointer}.gbr .fb{grid-column:1/4;padding:0 10px}
table.stars td{text-align:center}table.stars td:first-child{text-align:left;font-weight:500}
.slack{border:1px solid #d5d6d7;border-left:5px solid #4a154b;border-radius:6px;padding:8px 14px;margin:10px 0;background:#fff}.slack .t{color:#8a8b8d;font-size:13px;margin-left:8px}.slack p{margin:4px 0}
.two{display:grid;grid-template-columns:1fr 1fr;gap:8px}@media(max-width:700px){.two{grid-template-columns:1fr}.gbh,.gbr{grid-template-columns:1fr 90px 90px}}
</style>`);
"""
XJS = (CSS + EXTRA_CSS + JS.replace("__VI__", json.dumps(VITEMS, ensure_ascii=False))).replace("ACC2", ACC2).replace("ACC", ACC).replace("DARK", DARK).replace("aim: 60–100", "aim: 60–100")
OUT = "Learners can compare services."
FOOT = "Lead-in data: Ookla Speedtest (H2 2024), nPerf (2024). SkyMobile, Volt, LineUp and NovaTel are invented companies. "

def build(sub, s_last, tag, key_suffix):
    secs = [("1A", s1), ("1B", s2), ("2", s3), ("3", s4), ("Grammar", s5), ("4A", s6), ("4B", s7), ("5", s_last)]
    h = page("7.3", "The best providers", tag, OUT, "BP A2 7.3 Providers · " + key_suffix, CODE, secs, K, VOC,
             acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, footer=FOOT, extra_js=XJS)
    d = os.path.join(ROOT, sub); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "lesson.html"), "w").write(h); print("ok", sub, len(h))

build("all", s8, "LESSON · UPDATED", "Lesson")
build("all-classic", s8c, "LESSON · CLASSIC", "Classic")
PREV = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>BP A2 7.3 The best providers — preview</title>
<link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>body{margin:0;font-family:"Fira Sans",system-ui,sans-serif;font-weight:300;color:#231f20;background:#fff}
header{display:flex;border-bottom:3px solid #3b7dd8}header .n{background:linear-gradient(120deg,#2a5fb0,#4f9be8);color:#fff;font-weight:500;font-size:34px;padding:10px 24px}
header h1{margin:0;align-self:center;padding-left:18px;font-weight:500;font-size:30px;color:#4d4d4f}
main{max-width:760px;margin:30px auto;padding:0 20px}a.c{display:block;border:1.5px solid #3b7dd8;border-radius:10px;padding:16px 20px;margin:12px 0;text-decoration:none;color:#231f20}
a.c b{display:block;color:#2a5fb0;font-weight:600;font-size:19px}a.c:hover{background:#e3eefb}p.h{color:#6d6e70;font-size:14px}footer{text-align:center;font-size:12px;color:#77787b;margin:40px 0}</style>
</head><body><header><div class="n">7.3</div><h1>The best providers</h1></header><main><p>Business Partner A2 · Unit 7 Competition · template preview</p>
<a class="c" href="all/lesson.html"><b>Lesson · Updated</b>Mobile operators for company eSIMs · Superlatives · Writing: a Slack message recommending an operator</a>
<a class="c" href="all-classic/lesson.html"><b>Lesson · Classic</b>Same lesson · Writing: an email about Travel Care (coursebook task)</a>
<a class="c" href="all/hw.html"><b>Homework</b></a><a class="c" href="all/extra.html"><b>Extra</b></a><a class="c" href="all/games.html"><b>Speaking &amp; Games</b></a>
<p class="h">Preview: answers are not sent anywhere. The “← Contents” link works on the student site.</p></main>
<footer>Valentyna Hordiienko · Middle Learning Architect</footer></body></html>"""
open(os.path.join(ROOT, "index.html"), "w").write(PREV)
