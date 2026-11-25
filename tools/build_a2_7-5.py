"""Business Partner A2 · 7.5 Business workshop: The big contract — LESSON (Unit 7 review + online pitch). Updated: the trade show becomes an online pitch.
1 Phrases for presenting (coursebook Speaking box 7.4 + comparing language 7.1–7.3) · 1B Which phrase? · 2 Unit 7 words: the client's email
3 The case: GreenBox brief and three offers · 4 Prepare: compare the offers · 5 Present (deck with tasks under each slide) · 6 Q&A · Self-assessment.
Usage: python3 build_a2_7-5.py ROOT_LESSON_DIR [STUDENT_CODE]
"""
import sys, os, json, random
from bp_page import page, fb, sel, inp, ta, ctl, SELF
from vocab_a2 import lesson
ROOT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3b7dd8", "#e3eefb", "#2a5fb0", "#4f9be8"
K = {}
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_a2_7-2.py")).read()
CSS = _src[_src.index('CSS = r"""') + 10:_src.index('"""', _src.index('CSS = r"""') + 10)]
JS = _src[_src.index('JS = r"""') + 9:_src.index('"""', _src.index('JS = r"""') + 9)]
VITEMS, VOC = [], []
for num, keep in (("7.2", ["Fees", "Hidden fees"]), ("7.3", ["What is important?", "Superlatives"]), ("7.4", ["Presenting: phrases"])):
    for g, ws in lesson(num)[1]:
        if g not in keep: continue
        chips = []
        for en, uk, df, ex, co in ws:
            VITEMS.append({"en": en, "uk": uk, "df": df, "ex": ex, "co": co}); chips.append('<a class="vw" data-i="%d">%s</a>' % (len(VITEMS) - 1, en))
        VOC.append(("%s · %s" % (num, g), chips))
def spk(x): return '<button class="btn l" style="padding:2px 10px" onclick="say1(\'%s\')">🔊</button>' % x.replace("’", "\\'").replace("…", "")

# 1A Phrases (coursebook Speaking box 7.4 + comparing 7.1–7.3)
SB = [("Starting", ["Good morning / afternoon, everyone.", "My name is … and I’m … at …", "Thank you for attending this presentation."]),
      ("Giving the aim and the plan", ["The aim of today’s presentation is to …", "First, I’ll tell you … Then, I’ll explain … Finally, …", "We’ll have a question and answer session at the end."]),
      ("The main part", ["So, let’s start with …", "We’re based in … / We started in …", "We provide a range of … / We can …", "Let’s move on to …", "Now let’s talk about …"]),
      ("Presenting online", ["Let me share my screen.", "Can you all see my screen?", "As you can see on this slide, …"]),
      ("Ending", ["So, that’s the end of my presentation.", "Thank you for listening.", "Does anyone have any questions?"])]
CMP = [("Comparing two things (7.1)", ["Our price is higher than AppNova’s, but …", "We are faster than WebGiant.", "Their support is more expensive than ours."]),
       ("Comparing three or more (7.3)", ["We are the fastest.", "WebGiant is the biggest provider in Europe.", "We have the most satisfied customers.", "We offer the best value for money."]),
       ("Talking about price (7.2)", ["The fee includes …", "There’s an additional fee for …", "It’s a fixed fee — there are no hidden fees.", "Read the small print: …"])]
def box(title, groups, note=""):
    return ('<div class="gbox"><div class="gh">%s</div>%s' % (title, note) +
            "".join('<p style="margin:10px 0 2px"><b>%s</b></p>' % h + "".join('<div class="row">%s %s</div>' % (x, spk(x)) for x in xs) for h, xs in groups) + '</div>')
s1 = ('<div class="bsec">Speaking</div><p class="ins"><b class="x">1</b><b>A</b> Before the presentation: read and listen to the phrases. These are the phrases from the coursebook (Speaking box: <i>Presenting</i>). Repeat them.</p>' +
      box("Presenting", SB, '<p class="hint">Click 🔊 to listen and repeat.</p>') +
      '<p class="ins" style="margin-top:20px">In today’s presentation you will also <b>compare</b>. Use the language from 7.1–7.3:</p>' + box("Comparing", CMP))
# 1B Which phrase? (stage -> phrase)
ST = [("Start the presentation politely.", "Thank you for attending this presentation."), ("Say what the presentation is for.", "The aim of today’s presentation is to …"),
      ("Change to the next topic.", "Let’s move on to …"), ("Show something on the screen.", "As you can see on this slide, …"),
      ("Say where your company is.", "We’re based in …"), ("Finish and invite questions.", "Does anyone have any questions?"),
      ("Say what you sell or do.", "We provide a range of …"), ("Say that one company is number 1 for price.", "We offer the best value for money."),
      ("Explain that something costs extra.", "There’s an additional fee for …"), ("Start the first part.", "So, let’s start with …")]
OPT1 = sorted(p for _, p in ST)
for i, (_, p) in enumerate(ST): K["b1_%d" % i] = [p]
s2 = ('<div class="bsec">Speaking</div><p class="ins"><b>B</b> Which phrase do you use? Choose. Then say the phrase with an ending about <b>your</b> company.</p>' +
      "".join('<div class="row">%d. %s<br>%s%s</div>' % (i + 1, q, sel("b1_%d" % i, OPT1, 380), fb("b1_%d" % i)) for i, (q, _) in enumerate(ST)) + ctl("b1"))
# 2 Unit 7 words: the client's email
EM = [("Hi Pavlo, thank you for your offer. Before Friday I have some questions. AppNova’s price looks low, but I think there is an ", " fee for the payment system.", "additional"),
      ("Our lawyer always says: read the ", " before you sign!", "small print"), ("What does your ", " include? Is support after the launch included?", "fee"),
      ("At the moment we pay a ", " fee for our old website — €700 every month. It’s too much.", "monthly"),
      ("Can we stop the contract early? AppNova has an early ", " fee of €5,000.", "termination"),
      ("WebGiant says they are the biggest ", " of e-commerce services in Europe.", "provider"),
      ("For us, ", " for money is more important than a famous name.", "value"),
      ("Our couriers use the app in villages too, so good network ", " is important.", "coverage"),
      ("We need a simple ", " system: our customers pay by card or Apple Pay.", "payment"),
      ("Can you give us a free ", " of the AI chat assistant for two weeks?", "trial"),
      ("The ", " of Friday’s meeting is to choose one company.", "aim"), ("Thank you for ", " the meeting. See you on Friday! Olena", "attending")]
BOX2 = ["additional", "small print", "fee", "monthly", "termination", "provider", "value", "coverage", "payment", "trial", "aim", "attending"]
random.seed(75); BOX2S = BOX2[:]; random.shuffle(BOX2S)
for i, (_, _, a) in enumerate(EM): K["w2_%d" % i] = [a]
s3 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">2</b>Words from Unit 7. Read the email from the client, <b>Olena (GreenBox)</b>. Choose the missing words.</p>' +
      '<div class="card" style="max-width:720px;line-height:2.1"><b>📧 From:</b> Olena Bondar, Head of Digital, GreenBox<br><b>Subject:</b> Questions before Friday<hr>' +
      " ".join('%s%s%s%s' % (a, sel("w2_%d" % i, sorted(BOX2), 140), b, fb("w2_%d" % i)) for i, (a, b, _) in enumerate(EM)) + '</div>' + ctl("w2") +
      '<p class="ins" style="margin-top:18px">Speak: which of these things are important for <b>your</b> company when you choose a provider? <i>For us, … is the most important because …</i></p>')
# 3 The case
TAB = ('<table class="tb"><tr><th></th><th style="background:#fff1e6">BrightCode (you)</th><th>AppNova</th><th>WebGiant</th></tr>'
       '<tr><td>Based in · started</td><td>Kyiv · 2017</td><td>Warsaw · 2023</td><td>Berlin · 2006</td></tr>'
       '<tr><td>People · projects</td><td>45 · 140</td><td>12 · 40</td><td>900 · 2,000 — the biggest provider in Europe</td></tr>'
       '<tr><td>Price</td><td>€38,000 — fixed fee</td><td>€29,000</td><td>€55,000</td></tr>'
       '<tr><td>Payment system</td><td>included</td><td>additional fee €6,000</td><td>included</td></tr>'
       '<tr><td>Support</td><td>6 months included, 24/7 chat</td><td>€900 a month, email, weekdays</td><td>12 months included, phone + chat</td></tr>'
       '<tr><td>First version</td><td>8 weeks</td><td>10 weeks</td><td>16 weeks</td></tr>'
       '<tr><td>Customer rating</td><td>⭐ 4.8</td><td>⭐ 4.1</td><td>⭐ 4.5</td></tr>'
       '<tr><td>Cancel the contract</td><td>free in the first 14 days</td><td>early termination fee €5,000</td><td>annual contract only</td></tr></table>')
s4 = ('<div class="bsec">Business workshop</div><p class="ins"><b class="x">3</b><b>A</b> Read the situation and the three offers.</p>'
      '<div class="card" style="max-width:720px"><b>📌 The big contract</b><p>You are <b>Pavlo, a project manager at BrightCode</b>, an IT studio in Kyiv. '
      '<b>GreenBox</b> is an online grocery delivery company in Kyiv, Lviv and Odesa. They want a new <b>mobile app, an online shop and a payment system</b>. '
      'Their budget is about €40,000, and they need the first version <b>before the spring sale — in 10 weeks</b>.</p><p>Three companies sent offers. On Friday every company gives a <b>5-minute online presentation</b>. Then GreenBox chooses one.</p></div>' + TAB)
QS = [("c_1", "Which company looks the cheapest? Is it really the cheapest? Why / why not?", "AppNova looks the cheapest, but …"),
      ("c_2", "Which company is the fastest? Can every company finish before the spring sale?", "BrightCode is the fastest …"),
      ("c_3", "Which company is the biggest? Is the biggest always the best?", "WebGiant is the biggest provider, but …"),
      ("c_4", "What are BrightCode’s three best arguments?", "1 … 2 … 3 …"),
      ("c_5", "What is BrightCode’s weak point? What can you say about it?", "We aren’t the cheapest / the biggest, but …")]
s5 = ('<div class="bsec">Business workshop</div><p class="ins"><b>B</b> Prepare. Compare the three offers and answer the questions. Use comparatives and superlatives.</p>' +
      "".join('<p class="ins" style="margin-top:12px">%s</p>%s' % (q, ta(k, ph, 50)) for k, q, ph in QS) +
      '<button class="btn l" onclick="model(\'m5\')">Show possible answers</button><div class="model" id="m5">1 AppNova looks the cheapest (€29,000), but there is an additional fee for the payment system (€6,000) and a monthly fee for support (€900). In the first year it costs €45,800 — more than BrightCode. '
      '· 2 BrightCode is the fastest (8 weeks). AppNova needs 10 weeks — that’s very close to the sale. WebGiant needs 16 weeks, so they can’t finish before the sale. '
      '· 3 WebGiant is the biggest provider in Europe, but it is the most expensive and the slowest. · 4 the best value for money (fixed fee, no hidden fees) · the fastest · the most satisfied customers (4.8) '
      '· 5 We aren’t the cheapest on paper and we aren’t the biggest — but our fee includes everything, and we have more experience than AppNova.</div>')
# 4 Present
s6 = ('<div class="bsec wr">Presentation</div><p class="ins"><b class="x">4</b>Give your presentation online (5 minutes). Open the slides, <b>share your screen</b> and present BrightCode’s offer to Olena (your teacher). '
      'Under every slide there is a <b>task</b>: what to say, what to <b>compare</b> and which words to use. There is no script — speak!</p>'
      '<p><a class="btn" href="present.html" target="_blank">🎤 Open the presentation</a></p>'
      '<div class="ext"><b>Remember:</b> greet → the aim and the plan → the company → services → price → speed and quality → why us → questions. Use <i>First / Then / Let’s move on to / As you can see</i> and compare: <i>cheaper than, the fastest, the best value for money</i>.</div>' +
      '<p class="ins" style="margin-top:16px">After the presentation: write 2–3 things your teacher said you did well, and 1–2 things to improve.</p>' + ta("p_fb", "I did well: … Next time I want to …", 60))
# 5 Q&A
QA = ["Why should we pay more than AppNova’s price?", "WebGiant is the biggest provider in Europe. Why are you better?", "What does your fee include exactly?", "Are there any hidden fees?",
      "What happens if you are late?", "Can we cancel the contract?", "Can you give us a free trial or a discount?", "Who will be our contact person?"]
s7 = ('<div class="bsec">Speaking</div><p class="ins"><b class="x">5</b>Question and answer session. Olena asks you questions. Answer them — use the words you <b>didn’t</b> use in your presentation.</p>' +
      '<ol>' + "".join("<li style='margin:6px 0'>%s</li>" % q for q in QA) + '</ol>' +
      '<p class="hint">Useful: <i>That’s a good question. · Our fee includes … · There are no hidden fees. · We can … · If we are late, … · I’ll send you the details in an email.</i></p>' +
      '<p class="ins">Which question was the most difficult? Write your best answer to it.</p>' + ta("qa_1", "The most difficult question was … My answer: …", 70) +
      '<div style="margin-top:20px">%s</div>' % (SELF % "I can compare offers and give a short presentation to win a contract. How well can you do this now?"))
XJS = (CSS + JS.replace("__VI__", json.dumps(VITEMS, ensure_ascii=False))).replace("ACC2", ACC2).replace("ACC", ACC).replace("DARK", DARK)
OUT = "Learners can compare offers and give a short online presentation to win a contract, using the vocabulary of Unit 7."
secs = [("1A", s1), ("1B", s2), ("2", s3), ("3A", s4), ("3B", s5), ("4", s6), ("5", s7)]
h = page("7.5", "Business workshop: The big contract", "WORKSHOP · UNIT 7 REVIEW", OUT, "BP A2 7.5 The big contract · Lesson", CODE, secs, K, VOC, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2,
         footer="BrightCode, GreenBox, AppNova and WebGiant are invented companies. ", extra_js=XJS)
d = os.path.join(ROOT, "all"); os.makedirs(d, exist_ok=True); open(os.path.join(d, "lesson.html"), "w").write(h); print("ok", d, len(h))
