"""Business Partner A2 · 7.3 The best providers — EXTRA (coursebook Extra activities 7.3 A/B + Photocopiable 7.3 ideas, new contexts).
1 A: complete the advert with superlatives (adjectives in brackets) · 2 B: write sentences from prompts (We / have / good / customer service)
3 Superlative questions about you (speaking prep) · 4 Speaking: provider cards — find the best provider (teacher = Student B)
Usage: python3 build_a2_extra_7-3.py OUT.html [STUDENT_CODE]
"""
import sys, os
from bp_page import page, fb, inp, ta, ctl, SELF
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3b7dd8", "#e3eefb", "#2a5fb0", "#4f9be8"
K = {}
# keys as in the Teacher's Book (Extra activities 7.3 A), text adapted to an AI-assistant subscription
A = [("reliable", "most reliable"), ("knowledgeable", "most knowledgeable"), ("good", "best"), ("long", "longest"), ("friendly", "friendliest"), ("high", "highest"), ("satisfied", "most satisfied"), ("quick", "quickest")]
for i, (_, a) in enumerate(A): K["x1_%d" % (i + 1)] = [a, "the " + a]
g = lambda n: '<sup>%d</sup> the %s <span class="hint">(%s)</span>' % (n, inp("x1_%d" % n, 160), A[n - 1][0])
ADV = ('<div class="mail"><div class="mh">🤖 <b>WriteMate Business</b> — AI writing assistant for teams · Why choose us?</div>'
       '<p>WriteMate is %s AI assistant for business texts: it works 99.9%% of the time. Our support team is %s in the market — they know every feature. '
       'We offer %s price for teams of 10 or more. We have %s free trial: 30 days, not 7! Our chat agents are %s — people love talking to them. '
       'WriteMate has %s rating in the app store: 4.9. Our customers are %s in the industry, and we give %s answers: in under 2 minutes.</p></div>'
       % tuple(g(i + 1) for i in range(8)))
s1 = ('<div class="bsec">Extra practice</div><p class="ins"><b class="x">1</b>Complete the advert with the superlative form of the adjectives in brackets.</p>' + ADV +
      "".join(fb("x1_%d" % (i + 1)) for i in range(8)) + ctl("x1"))

B = [("We / have / good / customer service", "We have the best customer service."), ("Our service / be / reliable", "Our service is the most reliable."),
     ("We / have / knowledgeable / staff", "We have the most knowledgeable staff."), ("We / provide / good / value for money", "We provide the best value for money."),
     ("We / have / big / number of business clients", "We have the biggest number of business clients."), ("Our tariff / be / cheap", "Our tariff is the cheapest."),
     ("Our customers / be / satisfied / in the industry", "Our customers are the most satisfied in the industry."), ("We / have / high / levels of positive feedback", "We have the highest levels of positive feedback.")]
EX, B = B[0], B[1:]
for i, (_, a) in enumerate(B): K["x2_%d" % (i + 1)] = [a, a.replace("We have", "We’ve")]
s2 = ('<div class="bsec">Extra practice</div><p class="ins"><b class="x">2</b>You work in sales at an IT company. Write sentences for your sales presentation. Use superlatives.</p>'
      '<div class="card">Example: <i>%s</i> → <b>%s</b></div>' % EX +
      "".join('<div class="row">%d. <i>%s</i><br>%s%s</div>' % (i + 1, p, inp("x2_%d" % (i + 1), 480), fb("x2_%d" % (i + 1))) for i, (p, _) in enumerate(B)) + ctl("x2"))

Q3 = ["What is the best app on your phone? Why?", "Which is the most useful tool at your work?", "What is the most expensive subscription you pay for?",
      "Who is the most knowledgeable person in your team?", "What is the worst thing about your internet at home?", "Which is the fastest way to get to your office?"]
s3 = ('<div class="bsec wr">Speaking</div><p class="ins"><b class="x">3</b>Answer the questions about you. Write short notes, then tell your teacher. Use superlatives.</p>' +
      "".join('<div class="row">%d. %s<br>%s</div>' % (i + 1, q, ta("x3_%d" % (i + 1), "", 40)) for i, q in enumerate(Q3)))

CARDS = [("📱 Operator", "SkyMobile", "coverage ★★★ · speed 31 Mbps · €9 per user · support: 25 min"), ("☁️ Cloud storage", "BoxCloud", "2 TB · €12 a month · support 24/7 · the easiest app"),
         ("🖨 Printer contract", "PrintPro", "€40 a month · repairs in 1 day · the oldest printers"), ("🧹 Office cleaning", "CleanTeam", "€300 a month · the friendliest staff · only on Mondays")]
s4 = ('<div class="bsec wr">Speaking</div><p class="ins"><b class="x">4</b>Provider cards. Your company needs a new provider. Your teacher has cards for two other companies. '
      'Ask questions and decide which company is the best. Use: <i>Which one is the cheapest? Which has the best …? Is it the most reliable?</i></p><div class="two">' +
      "".join('<div class="card"><b>%s: %s</b><br>%s</div>' % c for c in CARDS) + '</div>'
      '<p class="ins">What did you decide? Write 2–3 sentences.</p>' + ta("x4", "We chose … because it is the … and it has the …", 70) +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you use superlatives now?"))
XJS = r"""document.head.insertAdjacentHTML("beforeend",`<style>.mail{border:1px solid #d5d6d7;border-radius:8px;padding:6px 18px;background:#fff;margin:10px 0;line-height:2.2}.mail .mh{background:#f3f4f6;margin:4px -18px 8px;padding:8px 18px;line-height:1.5}
.two{display:grid;grid-template-columns:1fr 1fr;gap:8px}@media(max-width:700px){.two{grid-template-columns:1fr}}</style>`);"""
h = page("7.3", "The best providers", "EXTRA", "Extra practice: superlatives in adverts and sales sentences, superlative questions, choosing a provider.", "BP A2 7.3 Providers · Extra", CODE,
         [("1", s1), ("2", s2), ("3", s3), ("4", s4)], K, None, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, extra_js=XJS)
os.makedirs(os.path.dirname(OUT), exist_ok=True); open(OUT, "w").write(h); print("ok", OUT, len(h))
