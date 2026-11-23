"""Business Partner A2 · 7.4 Presentations — EXTRA (coursebook Extra activities 7.4 A/B + Photocopiable 7.4 ideas + Atlassian sprint review video).
1 A: complete the opening (morning, aim, First, Then, Finally) · 2 B: complete the presentation (look, start, move, provider, can, based, Finally, questions)
3 Complete with the words in the box (photocopiable-style, new sentences) · 4 Video: a sprint review (Atlassian) · 5 Speed-presenting cards (speaking)
Usage: python3 build_a2_extra_7-4.py OUT.html [STUDENT_CODE]
"""
import sys, os
from bp_page import page, fb, inp, ta, ctl, SELF
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3b7dd8", "#e3eefb", "#2a5fb0", "#4f9be8"
K = {}
def gap(k, w=120): return inp(k, w) + fb(k)
# 1 (book key A: morning aim First Then Finally) — new text: a cloud-storage provider
A = ["morning", "aim", "First", "Then", "Finally"]
for i, a in enumerate(A): K["x1_%d" % (i + 1)] = [a, a.lower()]
s1 = ('<div class="bsec">Extra practice</div><p class="ins"><b class="x">1</b>Complete the start of a presentation. Use one word in each gap.</p><div class="card" style="line-height:2.3">'
      'Good <sup>1</sup>%s, everyone. My name is Marta and I’m the Head of Sales at CloudNest. The <sup>2</sup>%s of today’s presentation is to tell you about our new storage plan for teams. '
      '<sup>3</sup>%s, I’ll tell you about our company. <sup>4</sup>%s, I’ll show you the new plan. <sup>5</sup>%s, we’ll have ten minutes for your questions.</div>' % tuple(gap("x1_%d" % (i + 1)) for i in range(5)) + ctl("x1") +
      '<p class="hint">First letters: m · a · F · T · F</p>')
# 2 (book key B: look start move provider can based Finally questions)
B = [("Let’s ", " at our company in numbers.", "look"), ("So, let’s ", " with our history.", "start"), ("Now let’s ", " on to our services.", "move"),
     ("We’re the biggest ", " of cloud storage for small businesses in Poland.", "provider"), ("We ", " also help you move your old files.", "can"),
     ("We’re ", " in Kraków, and we have an office in Lviv.", "based"), ("", ", I’d like to thank you for your time.", "Finally"), ("Does anyone have any ", "?", "questions")]
for i, (_, _, a) in enumerate(B): K["x2_%d" % (i + 1)] = [a, a.lower()]
BOX = sorted(b[2] for b in B)
s2 = ('<div class="bsec">Extra practice</div><p class="ins"><b class="x">2</b>Complete the sentences from the same presentation with the words in the box.</p>'
      '<div class="ext">%s</div>' % " · ".join(BOX) +
      "".join('<div class="row">%d. %s%s%s</div>' % (i + 1, a, gap("x2_%d" % (i + 1)), b) for i, (a, b, _) in enumerate(B)) + ctl("x2"))
# 3 photocopiable-style box (about aim based everyone finally have move provider) — new sentences
C = [("So, good morning, ", ".", "everyone"), ("The ", " of today’s demo is to show you our new dashboard.", "aim"), ("Let’s ", " on to our prices.", "move"),
     ("I’ll talk ", " what we do and where we work.", "about"), ("We ", " offices in Lviv, Kraków and Berlin.", "have"), ("We’re ", " in Odesa.", "based"),
     ("We’re the main ", " of IT support for hotels in the region.", "provider"), ("", ", I can answer your questions at the end.", "Finally")]
for i, (_, _, a) in enumerate(C): K["x3_%d" % (i + 1)] = [a, a.lower()]
s3 = ('<div class="bsec">Extra practice</div><p class="ins"><b class="x">3</b>Complete the sentences from different presentations. Use: <i>about · aim · based · everyone · finally · have · move · provider</i>.</p>' +
      "".join('<div class="row">%d. %s%s%s</div>' % (i + 1, a, gap("x3_%d" % (i + 1)), b) for i, (a, b, _) in enumerate(C)) + ctl("x3"))
# 4 video
VID = "https://www.youtube.com/watch?v=InXAS_zRvqQ"
s4 = ('<div class="bsec">Video</div><p class="ins"><b class="x">4</b>In IT teams, a <b>sprint review</b> (or sprint demo) is a short presentation: the team shows what they did in the last two weeks. Watch the video from Atlassian (the company that makes Jira) and answer the questions.</p>'
      '<p><a class="btn" href="%s" target="_blank">▶ Watch: What is a sprint review?</a> <span class="hint">opens YouTube · you can turn on subtitles</span></p>' % VID +
      "".join('<div class="row">%d. %s<br>%s</div>' % (i + 1, q, ta("x4_%d" % (i + 1), "", 40)) for i, q in enumerate(
          ["Who comes to a sprint review?", "What does the team show?", "Is it a long, formal presentation or a short, friendly meeting?", "Do you have meetings like this at work? Who presents?"])) +
      '<p class="ins">Imagine you are presenting a sprint review. Write 3–4 sentences with phrases from the lesson.</p>' +
      ta("x4_s", "Good morning, everyone. The aim of today’s demo is to show you … First, … Then, … Let me share my screen.", 70))
# 5 speed-presenting cards
CARDS = ["I’m …, a … at …", "The aim of today’s presentation is to …", "Let’s start with …", "Let’s move on to …", "First, … Then, … Finally, …", "I’ll tell you about …", "We’re based in …", "We provide …"]
s5 = ('<div class="bsec wr">Speaking</div><p class="ins"><b class="x">5</b>Speed-presenting. Think of a company you know well (or would like to work for). Answer the questions in notes. Then click a card, finish the sentence about your company and say it to your teacher. Click the next card. Give as much information as you can in 2 minutes.</p>'
      '<div class="two">' + "".join('<div class="row">%s<br>%s</div>' % (q, ta("x5_%d" % (i + 1), "", 34)) for i, q in enumerate(
          ["How old is your company? Where are you based?", "What do you do? How big is your company?", "What are your main products and services?", "What else can you do? Where can you deliver?"])) + '</div>'
      '<div class="cards">' + "".join('<button class="pcard" onclick="this.classList.toggle(\'on\')">%s</button>' % c for c in CARDS) + '</div>'
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you present a company now?"))
XJS = r"""document.head.insertAdjacentHTML("beforeend",`<style>.two{display:grid;grid-template-columns:1fr 1fr;gap:8px}@media(max-width:700px){.two{grid-template-columns:1fr}}
.cards{display:flex;flex-wrap:wrap;gap:10px;margin:14px 0}.pcard{border:2px dashed #3b7dd8;background:#fff;border-radius:10px;padding:14px 16px;font-size:15.5px;cursor:pointer;min-width:200px;text-align:left}
.pcard.on{background:#e3eefb;border-style:solid;text-decoration:line-through;color:#6b7280}</style>`);"""
h = page("7.4", "Work skills: Presentations", "EXTRA", "Extra practice: presentation phrases, a sprint review video and speed-presenting.", "BP A2 7.4 Presentations · Extra", CODE,
         [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5)], K, None, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, extra_js=XJS)
os.makedirs(os.path.dirname(OUT), exist_ok=True); open(OUT, "w").write(h); print("ok", OUT, len(h))
