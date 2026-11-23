"""Business Partner A2 · 7.4 Presentations — HOMEWORK (new context: a Lviv courier start-up presents to an online shop).
1 Order the presentation (1–8) · 2 Choose the correct word · 3 Reading: the script — answer the questions · 4 Online presentation: match the problem and the phrase · 5 Writing: your own presentation script.
Usage: python3 build_a2_hw_7-4.py OUT.html [STUDENT_CODE]
"""
import sys, os
from bp_page import page, fb, sel, inp, ta, ctl, SELF
from vocab_a2 import lesson
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3b7dd8", "#e3eefb", "#2a5fb0", "#4f9be8"
_, GROUPS = lesson("7.4")
K = {}
VOC = [(g, [w[0] for w in ws]) for g, ws in GROUPS]
def radios(k, opts): return "".join('<label class="opt" style="display:inline;margin:0 12px 0 0"><input type="radio" name="%s" data-k="%s" value="%s"> %s</label>' % (k, k, o, o) for o in opts)

# 1 order (shuffled display)
P1 = ["Good afternoon, everyone. I’m Iryna, the Sales Manager at QuickBox.", "Thank you for joining this call. The aim of today’s presentation is to show you our delivery services.",
      "First, I’ll tell you about the company. Then I’ll explain our services. Finally, we’ll have time for questions.", "So, let’s start with the company. We’re based in Lviv and we started in 2021.",
      "Let’s move on to our services. We provide same-day delivery in the city.", "We can also pick up returns from your customers.",
      "So, that’s the end of my presentation. Thank you for listening.", "Does anyone have any questions?"]
SH = [4, 0, 6, 2, 7, 1, 5, 3]
LET = "abcdefgh"
for pos, idx in enumerate(SH): K["h1_" + LET[pos]] = [str(idx + 1)]
s1 = ('<div class="bsec">Presenting</div><p class="ins"><b class="x">1</b>Iryna from <b>QuickBox</b>, a courier company, presents online to an online shop. Put her sentences in the correct order (1–8).</p>' +
      "".join('<div class="row">%s <b>%s</b> %s%s</div>' % (sel("h1_" + LET[pos], [str(i) for i in range(1, 9)], 70), LET[pos], P1[idx], fb("h1_" + LET[pos])) for pos, idx in enumerate(SH)) + ctl("h1"))
# 2 choose
C2 = [("The ___ of this presentation is to introduce our app.", ["aim", "end", "plan"], "aim"), ("___, I’ll tell you about our history.", ["Finally", "First", "Then"], "First"),
      ("We’re ___ in Kyiv, with an office in Warsaw.", ["started", "based", "provided"], "based"), ("Let’s ___ on to our prices.", ["go", "move", "start"], "move"),
      ("We ___ a range of services for small shops.", ["provide", "attend", "share"], "provide"), ("Thank you for ___ this presentation.", ["attending", "giving", "making"], "attending"),
      ("We are the biggest ___ of online payments in Ukraine.", ["customer", "provider", "session"], "provider"), ("Does anyone have any ___?", ["question", "questions", "answer"], "questions")]
for i, (_, _, a) in enumerate(C2): K["h2_%d" % (i + 1)] = [a]
s2 = ('<div class="bsec">Phrases</div><p class="ins"><b class="x">2</b>Choose the correct word.</p>' +
      "".join('<div class="tf"><span class="q">%d. %s</span>%s%s</div>' % (i + 1, q, radios("h2_%d" % (i + 1), o), fb("h2_%d" % (i + 1))) for i, (q, o, _) in enumerate(C2)) + ctl("h2", "chkRad"))
# 3 reading
TXT = ('<div class="card" style="line-height:1.7"><p><b>🎤 Script — QuickBox</b></p><p>Good afternoon, everyone. I’m Iryna, the Sales Manager at QuickBox. Thank you for joining this call. The aim of today’s presentation is to show you how we can deliver your orders.</p>'
       '<p>So, let’s start with the company. We’re based in Lviv, and we started in 2021 with five couriers on bikes. Today we have 120 couriers and offices in Lviv and Ivano-Frankivsk. We deliver more than 3,000 orders a day.</p>'
       '<p>Let’s move on to our services. We provide same-day delivery in the city: you get an order at 10, the customer gets it at 4. We can also pick up returns, and your customers can follow the courier on a map in our app.</p>'
       '<p>Our prices start at 80 hryvnias per order. For shops with more than 500 orders a month, the price is 65 hryvnias.</p>'
       '<p>So, that’s the end of my presentation. Thank you for listening. Does anyone have any questions?</p></div>')
Q3 = [("Where is QuickBox based?", ["Lviv", "in Lviv"]), ("When did the company start?", ["2021", "in 2021"]), ("How many couriers does it have today?", ["120"]),
      ("How many orders does it deliver a day?", ["3000", "3,000", "more than 3,000", "more than 3000"]), ("What is the price per order for a big shop (500+ orders a month)?", ["65", "65 hryvnias", "65 UAH"])]
for i, (_, a) in enumerate(Q3): K["h3_%d" % (i + 1)] = a
s3 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">3</b><b>A</b> Read Iryna’s script. Answer the questions.</p>' + TXT +
      "".join('<div class="row">%d. %s %s%s</div>' % (i + 1, q, inp("h3_%d" % (i + 1), 200), fb("h3_%d" % (i + 1))) for i, (q, _) in enumerate(Q3)) + ctl("h3") +
      '<p class="ins" style="margin-top:20px"><b>B</b> Find and write the three “signpost” phrases Iryna uses to start each part.</p>' + ta("h3b", "Let’s start with … / Let’s move on to … / So, that’s the end …", 50))
# 4 online problems
M4 = [("Your audience can’t see your slides.", "Let me share my screen. Can you all see it now?"), ("You start talking, but your microphone is off.", "Sorry, I think I was on mute."),
      ("You want to send a link to everybody.", "I’ll put the link in the chat."), ("You want to show a number on the slide.", "As you can see on this slide, …"),
      ("The internet is slow and they can’t hear you well.", "Can you hear me OK?"), ("You finish and want to hear from people.", "Does anyone have any questions?")]
OPTS = sorted(b for _, b in M4)
for i, (_, b) in enumerate(M4): K["h4_%d" % (i + 1)] = [b]
s4 = ('<div class="bsec">Online</div><p class="ins"><b class="x">4</b>You are presenting on Zoom. What do you say? Choose the best phrase.</p>' +
      "".join('<div class="row">%d. %s<br>%s%s</div>' % (i + 1, a, sel("h4_%d" % (i + 1), OPTS, 420), fb("h4_%d" % (i + 1))) for i, (a, _) in enumerate(M4)) + ctl("h4"))
# 5 writing
MODEL5 = ("Good morning, everyone. I’m Pavlo, a project manager at PixelForge. Thank you for joining this call. The aim of today’s presentation is to introduce our studio.\n"
          "First, I’ll tell you about the company. Then I’ll show you our services. Finally, we’ll have time for questions.\n"
          "So, let’s start with the company. We’re based in Lviv and we started in 2019. We have 25 people.\n"
          "Let’s move on to our services. We provide websites and mobile apps for small businesses. We can also support your app after the launch.\n"
          "So, that’s the end of my presentation. Does anyone have any questions?")
s5 = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">5</b>Write a short script (80–120 words) about <b>your company</b> or a company you know. Use the five stages and the phrases from the lesson. Next lesson you will present it online.</p>'
      '<div class="ext"><ul style="margin:0;padding-left:20px"><li>Start: Good morning, everyone. I’m … Thank you for joining this call.</li><li>Aim and plan: The aim of today’s presentation is to … First, … Then, … Finally, …</li>'
      '<li>Company: So, let’s start with … We’re based in … We started in …</li><li>Services: Let’s move on to … We provide … We can …</li><li>End: So, that’s the end of my presentation. Does anyone have any questions?</li></ul></div>' +
      ta("w5", "Good morning, everyone. I’m …", 190) + '<p class="hint" id="w5c"></p>'
      '<button class="btn l" onclick="model(\'m5\')">Show a model answer</button><div class="model" id="m5">%s</div>' % MODEL5 +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you write a short presentation now?"))
XJS = r"""function wc(){const t=document.querySelector('.g[data-k="w5"]');if(!t)return;const n=(t.value.trim().match(/\S+/g)||[]).length;document.getElementById("w5c").textContent=n+" words (aim: 80–120)"}
document.addEventListener("input",e=>{if(e.target.dataset&&e.target.dataset.k==="w5")wc()});window.afterFill=wc;"""
h = page("7.4", "Work skills: Presentations", "HOMEWORK", "Learners can give a short presentation about a company and its products and services.", "BP A2 7.4 Presentations · Homework", CODE,
         [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5)], K, VOC, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, extra_js=XJS)
os.makedirs(os.path.dirname(OUT), exist_ok=True); open(OUT, "w").write(h); print("ok", OUT, len(h))
