"""Business Partner A2 · 1.2 A work plan — EASY HOMEWORK (A1-friendly). No ready-made answers in the writing task.
Usage: python3 build_a2_hw_1-2_easy.py OUT.html [STUDENT_CODE]
"""
import sys, os
from bp_page import page, fb, sel, inp, ta, ctl, SELF
from vocab_a2 import lesson
import vcard
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3b7dd8", "#e3eefb", "#2a5fb0", "#4f9be8"
_, GROUPS = lesson("1.2")
VOC, VJS = vcard.build(GROUPS, ACC, ACC2, DARK, show_uk=True)
def ua(t): return '<span class="ua">🇺🇦 %s</span>' % t
K = {}
# A words ↔ Ukrainian
A = [("отримати оновлення (новини)", "get an update"), ("забронювати переговорну", "book a meeting room"), ("розрахувати витрати", "calculate costs"),
     ("підготувати презентацію", "prepare a presentation"), ("розіслати порядок денний", "send out the agenda"), ("створити бриф", "create a brief")]
OPT = sorted(e for _, e in A)
for i, (_, e) in enumerate(A): K["a_%d" % (i + 1)] = [e]
s1 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">A</b>Match. ' + ua("Знайди англійську фразу.") + '</p>' +
      "".join('<div class="row">%d. %s → %s%s</div>' % (i + 1, u, sel("a_%d" % (i + 1), OPT, 220), fb("a_%d" % (i + 1))) for i, (u, _) in enumerate(A)) + ctl("a"))
# B choose
B = [("I have a ___ meeting on Monday. We talk about money.", ["budget", "brief"], "budget"), ("Can you ___ a meeting room for Friday?", ["book", "make"], "book"),
     ("I ___ out the agenda before the meeting.", ["send", "get"], "send"), ("Are you ___ on Tuesday?", ["available", "busy"], "available"),
     ("Sorry, I’m ___ then. I have a client meeting.", ["busy", "fine"], "busy"), ("How ___ Thursday at 2 p.m.?", ["about", "is"], "about"),
     ("___ we meet on Zoom?", ["Shall", "Are"], "Shall"), ("OK, Friday at one. See you ___!", ["then", "fine"], "then")]
for i, (_, _, a) in enumerate(B): K["b_%d" % (i + 1)] = [a]
s2 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">B</b>Choose the correct word. ' + ua("Обери правильне слово.") + '</p>' +
      "".join('<div class="row">%d. %s%s</div>' % (i + 1, q.replace("___", sel("b_%d" % (i + 1), o, 120)), fb("b_%d" % (i + 1))) for i, (q, o, _) in enumerate(B)) + ctl("b"))
# C order the chat
C = [("A", "Olha", "Monday is fine. How about 11 a.m.?"), ("B", "You", "Hi Olha! Are you available on Monday?"), ("C", "Olha", "Hi! Yes, I’m available after 10 a.m."),
     ("D", "You", "Perfect. See you then!")]
CA = {"A": "3", "B": "1", "C": "2", "D": "4"}
for L, a in CA.items(): K["c_" + L] = [a]
s3 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">C</b>Put the Slack messages in order (1–4). ' + ua("Розстав повідомлення по порядку.") + '</p>' +
      "".join('<div class="row"><b>%s</b> · <i>%s:</i> %s %s%s</div>' % (L, w, t, sel("c_" + L, ["1", "2", "3", "4"], 60), fb("c_" + L)) for L, w, t in C) + ctl("c"))
# D calendar true/false
CAL = [("Mon", "10:00 budget meeting"), ("Tue", "free"), ("Wed", "9:00–17:00 workshop"), ("Thu", "14:00 client meeting"), ("Fri", "free in the morning")]
D = [("Olha is busy on Wednesday.", "T"), ("Olha is available on Tuesday.", "T"), ("Olha has a budget meeting on Thursday.", "F"),
     ("Olha is available on Friday morning.", "T"), ("Olha has a client meeting on Monday.", "F")]
for i, (_, a) in enumerate(D): K["d_%d" % (i + 1)] = [a]
def radio(k): return "".join('<label class="opt" style="display:inline;margin:0 10px 0 0"><input type="radio" name="%s" data-k="%s" value="%s"> %s</label>' % (k, k, o, o) for o in "TF")
s4 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">D</b>Look at Olha’s calendar. True (T) or false (F)? ' + ua("Правда чи ні?") + '</p>'
      '<div class="cal">%s</div>' % "".join('<div class="cd"><b>%s</b>%s</div>' % c for c in CAL) +
      "".join('<div class="tf"><span class="q">%d. %s</span>%s%s</div>' % (i + 1, q, radio("d_%d" % (i + 1)), fb("d_%d" % (i + 1))) for i, (q, _) in enumerate(D)) + ctl("d", "chkRad"))
# E writing — prompts only, no ready answers
s5 = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">E</b>Your colleague writes: <i>“Hi! We need a project meeting this week. Are you available on Wednesday?”</i> Write your answer (3–4 sentences). ' +
      ua("Напиши відповідь: 1) привітайся; 2) скажи, чи ти вільна в середу; 3) запропонуй інший день і час (How about…?); 4) запропонуй місце (Shall we meet…?).") + '</p>' +
      ta("e", "", 110) + '<div style="margin-top:20px">%s</div>' % (SELF % "I can schedule a meeting. How well can you do this now?"))
XJS = VJS + r"""document.head.insertAdjacentHTML("beforeend",`<style>.ua{display:block;font-size:14px;color:#6d6e70;font-weight:400;margin-top:2px}
.cal{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;margin:10px 0}.cd{border:1px solid #d6dbe4;border-radius:8px;padding:6px 8px;font-size:14px}.cd b{display:block;color:#2a5fb0}@media(max-width:700px){.cal{grid-template-columns:1fr 1fr}}</style>`);"""
secs = [("A", s1), ("B", s2), ("C", s3), ("D", s4), ("E", s5)]
h = page("1.2", "A work plan", "HOMEWORK", "Words for work tasks and phrases to schedule a meeting.", "BP A2 1.2 A work plan · Homework (easy)", CODE, secs, K, VOC,
         acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, extra_js=XJS)
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True); open(OUT, "w").write(h); print("ok hw", len(h))
