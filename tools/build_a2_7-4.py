"""Business Partner A2 · 7.4 Work skills: Presentations — LESSON (as in the coursebook + online presentation).
1A–C Lead-in · 2A–B Video 7.4.1 (Jonathan Potts, Web Trade Builder; video on listeninenglish.com) · 3 Phrases from the video · Speaking box: Presenting
4 Writing + speaking: Classic = coursebook task (Force Sport Cars notes); Updated = online presentation on a video call with the Presentation kit.
Keys: Teacher's Book (1C, 2A, 2B, 3). Usage: python3 build_a2_7-4.py ROOT_LESSON_DIR [STUDENT_CODE]
"""
import sys, os, json
from bp_page import page, fb, sel, inp, ta, ctl, SELF
from vocab_a2 import lesson
ROOT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3b7dd8", "#e3eefb", "#2a5fb0", "#4f9be8"
TITLE, GROUPS = lesson("7.4")
K = {}
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_a2_7-2.py")).read()
CSS = _src[_src.index('CSS = r"""') + 10:_src.index('"""', _src.index('CSS = r"""') + 10)]
JS = _src[_src.index('JS = r"""') + 9:_src.index('"""', _src.index('JS = r"""') + 9)]
VITEMS, VOC = [], []
for g, ws in GROUPS:
    chips = []
    for en, uk, df, ex, co in ws:
        VITEMS.append({"en": en, "uk": uk, "df": df, "ex": ex, "co": co}); chips.append('<a class="vw" data-i="%d">%s</a>' % (len(VITEMS) - 1, en))
    VOC.append((g, chips))
def radios(k, opts): return "".join('<label class="opt" style="display:inline;margin:0 12px 0 0"><input type="radio" name="%s" data-k="%s" value="%s"> %s</label>' % (k, k, v, l) for v, l in opts)
VIDEO = "https://listeninenglish.com/business-partner-a2-741.php"

# 1A
s1 = ('<div class="bsec">Lead-in</div><p class="ins"><b class="x">1</b><b>A</b> Do you give presentations at work? How do you feel about it? Do you present online or in a meeting room?</p>' +
      ta("l1a", "I give presentations … I feel … I usually present on Zoom / Google Meet …", 80) +
      '<p class="ins">Think of a presentation you watched. What did you like / not like about it?</p>' + ta("l1a2", "", 50))
# 1B
BOX = ["clear structure", "short and simple slides", "a good start", "examples and numbers", "speaking slowly and clearly", "eye contact / looking at the camera", "time for questions", "a working microphone and screen share"]
s2 = ('<div class="bsec">Lead-in</div><p class="ins"><b>B</b> You are presenting your company or product to <b>potential customers</b>. What is important? Choose the three most important things and say why.</p>' +
      '<div class="chips">%s</div>' % "".join('<label class="chip"><input type="checkbox"> %s</label>' % b for i, b in enumerate(BOX)) +
      ta("l1b", "For me, … is the most important because …", 60))
# 1C (key 1b 2f 3d 4e 5c 6a)
ST = [("a", "Finish and ask for questions."), ("b", "Greet the audience and introduce yourself."), ("c", "Explain how you can help the customer."),
      ("d", "Give the plan: first, then, finally."), ("e", "Talk about the company: where it is based, when it started."), ("f", "Say the aim of the presentation.")]
ORD = {"b": 1, "f": 2, "d": 3, "e": 4, "c": 5, "a": 6}
for l, _ in ST: K["c1_" + l] = [str(ORD[l])]
s3 = ('<div class="bsec">Lead-in</div><p class="ins"><b>C</b> Put the stages of a presentation in the correct order (1–6).</p>' +
      "".join('<div class="row">%s <b>%s</b> %s%s</div>' % (sel("c1_" + l, [str(i) for i in range(1, 7)], 70), l, t, fb("c1_" + l)) for l, t in ST) + ctl("c1"))
# 2A
s4 = ('<div class="bsec">Video</div><p class="ins"><b class="x">2</b><b>A</b> Watch Jonathan Potts, the Sales Director of Web Trade Builder, giving a presentation to the team at Sleek. Answer the questions.</p>'
      '<p><a class="btn" href="%s" target="_blank">▶ Watch video 7.4.1 (3:14)</a> <span class="hint">opens in a new tab · British accent</span></p>' % VIDEO +
      '<div class="row">1. What is the aim of the presentation?<br>%s</div>' % inp("v2a_1", 520) +
      '<div class="row">2. What services does the company provide?<br>%s</div>' % inp("v2a_2", 520) +
      '<div class="tf"><span class="q">3. Is Web Trade Builder the biggest e-commerce provider in Europe?</span>%s%s</div>' % (radios("v2a_3", [("yes", "Yes"), ("no", "No")]), fb("v2a_3")) +
      '<button class="btn l" onclick="model(\'m2a\')">Show answers</button><div class="model" id="m2a">1 to introduce the company and its services · 2 website building, online shops and payment systems (e-commerce services) · 3 Yes, they are.</div>')
K["v2a_3"] = ["yes"]
# 2B (1F 2T 3T 4T 5T 6T 7F 8T)
TF = [("Jonathan Potts is the Marketing Director.", "F"), ("The company started in 2001.", "T"), ("It is the biggest provider of e-commerce services in Europe.", "T"),
      ("The company is based in Birmingham, in the UK.", "T"), ("It also has offices in Madrid and Frankfurt.", "T"), ("It has more than 20,000 clients.", "T"),
      ("They can only add an online shop to a website you already have.", "F"), ("They say their payment database is very secure.", "T")]
for i, (_, a) in enumerate(TF): K["v2b_%d" % (i + 1)] = [a]
s5 = ('<div class="bsec">Video</div><p class="ins"><b>B</b> Watch again. Are the sentences true (T) or false (F)?</p><p><a class="btn l" href="%s" target="_blank">▶ Video 7.4.1</a></p>' % VIDEO +
      "".join('<div class="tf"><span class="q">%d. %s</span>%s%s</div>' % (i + 1, q, radios("v2b_%d" % (i + 1), [("T", "T"), ("F", "F")]), fb("v2b_%d" % (i + 1))) for i, (q, _) in enumerate(TF)) +
      ctl("v2b", "chkRad"))
# 3 (keys TB: 1 morning 2 aim, introduce 3 tell 4 Finally 5 start 6 biggest 7 based 8 move 9 build 10 can 11 end 12 questions)
G3 = [("Good ", ", everyone.", "morning"), ("The ", " of today’s presentation is to introduce our company and services.", "aim"),
      ("The aim of today’s presentation is to ", " our company and services.", "introduce"), ("First, I’ll ", " you a bit more about the company’s history.", "tell"),
      ("", ", we’ll have a question and answer session at the end.", "Finally"), ("So, let’s ", " with more information about the company.", "start"),
      ("We are the ", " provider of e-commerce services in Europe.", "biggest"), ("We’re ", " in Birmingham, in the UK.", "based"),
      ("So, let’s ", " on to our products and services.", "move"), ("If you don’t have a website, we can ", " a complete website.", "build"),
      ("We ", " design a system that allows your customers to pay faster.", "can"), ("So that’s the ", " of my presentation.", "end"),
      ("Does anyone have any ", "?", "questions")]
NUM3 = ["1", "2", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
for i, (_, _, a) in enumerate(G3): K["p3_%d" % (i + 1)] = [a]
s6 = ('<div class="bsec">Video</div><p class="ins"><b class="x">3</b>Complete the phrases from the presentation. Then watch again and check.</p>' +
      "".join('<div class="row">%s. %s%s%s%s</div>' % (NUM3[i], a, inp("p3_%d" % (i + 1), 120), b, fb("p3_%d" % (i + 1))) for i, (a, b, _) in enumerate(G3)) + ctl("p3"))
# Speaking box
SB = [("Starting", ["Good morning / afternoon, everyone.", "I’m … I’m Sales Director at …", "Thank you for attending this presentation."]),
      ("Giving the aim and the plan", ["The aim of today’s presentation is to …", "First, I’ll tell you … Then, I’ll explain … Finally, …", "We’ll have a question and answer session at the end."]),
      ("The main part", ["So, let’s start with …", "We’re based in … / We started in …", "We provide a range of … / We can …", "Let’s move on to …", "Now let’s talk about …"]),
      ("Presenting online", ["Let me share my screen.", "Can you all see my screen?", "As you can see on this slide, …", "Sorry, I think I’m on mute.", "I’ll put the link in the chat."]),
      ("Ending", ["So, that’s the end of my presentation.", "Thank you for listening.", "Does anyone have any questions?"])]
s7 = ('<div class="bsec">Speaking</div><div class="gbox"><div class="gh">Presenting</div><p class="hint">Click 🔊 to listen and repeat.</p>' +
      "".join('<p style="margin:10px 0 2px"><b>%s</b></p>' % h + "".join('<div class="row">%s <button class="btn l" style="padding:2px 10px" onclick="say1(\'%s\')">🔊</button></div>' % (x, x.replace("’", "\\'").replace("…", "")) for x in xs) for h, xs in SB) + '</div>')
# 4 Updated: online presentation with the kit
KIT = "present.html"
STG = [("w4_start", "Start: greet and introduce yourself", "Good morning, everyone. My name is … and I’m … at …"), ("w4_aim", "The aim and the plan", "The aim of today’s presentation is to … First, … Then, … Finally, …"),
       ("w4_co", "The company: where, when, how big", "So, let’s start with the company. We’re based in … We started in …"), ("w4_prod", "Products and services / how you can help", "Let’s move on to … We provide … We can …"),
       ("w4_end", "Ending and questions", "So, that’s the end of my presentation. Thank you for listening. Does anyone have any questions?")]
s8 = ('<div class="bsec wr">Writing &amp; speaking</div><p class="ins"><b class="x">4</b>Give a short presentation <b>online</b> (3–4 minutes). Choose a presentation in the <b>Presentation kit</b> — a web studio, a product demo, a sprint review, a recommendation, or <b>your own company</b>. '
      'Write your script for each stage, then share your screen on the video call and present to your teacher.</p>'
      '<p><a class="btn" href="%s" target="_blank">🎤 Open the Presentation kit</a></p>' % KIT +
      '<p class="ins">My presentation:</p>' + sel("w4_deck", ["A · PixelForge — our company", "B · TaskFlow — product demo", "C · Sprint review — FoodGo app", "D · Our new mobile operator", "E · My own company"], 320) +
      "".join('<p class="ins" style="margin-top:14px">%s</p>%s' % (l, ta(k, ph, 60)) for k, l, ph in STG) +
      '<div class="ext"><b>Checklist:</b> ✓ the aim ✓ First / Then / Finally ✓ Let’s move on to … ✓ We’re based in … ✓ We provide … ✓ Let me share my screen ✓ Any questions?</div>' +
      '<div style="margin-top:20px">%s</div>' % (SELF % "I can give a short presentation about a company and its services. How well can you do this now?"))
MODEL_CL = ("Good morning, everyone. I’m Sabine, the Sales Director of Force Sport Cars. Thank you for attending this presentation. The aim of today’s presentation is to introduce our company and services. "
            "First, I’ll tell you about the company history. Then I’ll explain our products and services. Finally, we’ll have a question and answer session at the end.\n"
            "So, let’s start with the company. We’re based in Spa, in Belgium, and we started the business in 1987. At the beginning we fixed motor racing engines. In 1992 we launched our own sports car. Today we also provide parts and hand-built engines for motor sport teams.\n"
            "Let’s move on to our main products: our engines. They are the most reliable and the lightest in the industry, and they last the longest.\n"
            "Now let’s talk about our services. We can fix your racing cars and motorcycles and replace engines and parts. Our team has over thirty years’ experience.\n"
            "So, that’s the end of my presentation. Does anyone have any questions?")
NOTES_CL = ('<div class="card" style="max-width:600px"><b>🏎 Force Sport Cars — notes</b><ul style="margin:6px 0;padding-left:20px"><li>Sabine — Sales Director</li><li>Based in Spa, Belgium · started in 1987</li>'
            '<li>Start: fixing motor racing engines · 1992: our own sports car for public roads</li><li>Today: parts and hand-built engines for motor sport teams (main business)</li>'
            '<li>Engines: the most reliable, the quickest to build, the lightest, last the longest</li><li>Services: fix motorsport cars and motorcycles, replace engines and parts · team: 30+ years’ experience</li><li>End: questions</li></ul></div>')
s8c = ('<div class="bsec wr">Writing &amp; speaking</div><p class="ins"><b class="x">4</b>Read the notes about Force Sport Cars. Write a short presentation about the company. Use phrases from the Speaking box. Then give your presentation.</p>' + NOTES_CL +
       ta("w4_cl", "Good morning. I’m Sabine, the Sales Director of Force Sport Cars. …", 200) +
       '<button class="btn l" onclick="model(\'m4\')">Show a model answer</button><div class="model" id="m4">%s</div>' % MODEL_CL +
       '<div style="margin-top:20px">%s</div>' % (SELF % "I can give a short presentation about a company and its services. How well can you do this now?"))

EXTRA_CSS = r"""document.head.insertAdjacentHTML("beforeend",`<style>.chips .chip{display:inline-flex;gap:6px;align-items:center;border:1.5px solid ACC;border-radius:16px;padding:4px 12px;margin:4px;cursor:pointer;background:#fff}
.chips .chip input{accent-color:ACC}</style>`);"""
XJS = (CSS + EXTRA_CSS + JS.replace("__VI__", json.dumps(VITEMS, ensure_ascii=False))).replace("ACC2", ACC2).replace("ACC", ACC).replace("DARK", DARK)
OUT = "Learners can give a short presentation about a company and its products and services."
FOOT = "Video 7.4.1: Business Partner A2 (Pearson), via listeninenglish.com. "
def build(sub, last, tag, ks):
    secs = [("1A", s1), ("1B", s2), ("1C", s3), ("2A", s4), ("2B", s5), ("3", s6), ("Presenting", s7), ("4", last)]
    h = page("7.4", "Work skills: Presentations", tag, OUT, "BP A2 7.4 Presentations · " + ks, CODE, secs, K, VOC, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, footer=FOOT, extra_js=XJS)
    d = os.path.join(ROOT, sub); os.makedirs(d, exist_ok=True); open(os.path.join(d, "lesson.html"), "w").write(h); print("ok", sub, len(h))
build("all", s8.replace('href="present.html"', 'href="present.html"'), "LESSON · UPDATED", "Lesson")
build("all-classic", s8c, "LESSON · CLASSIC", "Classic")
