"""Business Partner A2 · 7.2 Services and subscriptions — EXTRA (practice of what is not in the main lesson).
1 Extra vocabulary practice (coursebook format: word box + 8 sentences, IT context)
2 Saying prices: a / an / per (€40 an hour, €8 per user per month) + listen and write the price
3 Price changes: go up / go down, from … to …, a 45% increase, save 15%
4 Speaking: a support chat — asking about fees (role cards A/B)
Usage: python3 build_a2_extra_7-2.py OUT.html [STUDENT_CODE]
"""
import sys, os
from bp_page import page, fb, sel, inp, ta, ctl, radios, SELF
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3b7dd8", "#e3eefb", "#2a5fb0", "#4f9be8"
K = {}
BOX = ["additional", "administration", "booking", "cancellation", "charge", "fixed", "include", "monthly"]
S1 = [("To keep your CloudBox account, there is a(n) ", " fee of €10, paid at the start of every month.", ["monthly"]),
      ("After you buy the Pro plan, you can add more storage at any time for a(n) ", " fee.", ["additional"]),
      ("If you want to leave before the end of your contract, you have to pay a(n) ", " fee.", ["cancellation"]),
      ("Our trainers’ fees ", " three online sessions, all materials and access to our Slack community.", ["include"]),
      ("All tickets for the tech conference bought online include a(n) ", " fee of €3.50.", ["booking"]),
      ("Our three-day UX course is available for a(n) ", " fee of €900. We don’t offer hourly rates.", ["fixed"]),
      ("The airline will ", " a fee for any changes to your flight details.", ["charge"]),
      ("There is a(n) ", " fee of €25 to open a business account.", ["administration"])]
for i, (_, _, a) in enumerate(S1): K["v1_%d" % (i + 1)] = a
s1 = ('<div class="bsec">Extra vocabulary practice</div><p class="ins"><b class="x">1</b>Complete the sentences with the words in the box.</p><div class="box">%s</div>' % " · ".join(BOX) +
      "".join('<div class="row">%d. %s%s%s%s</div>' % (i + 1, a, inp("v1_%d" % (i + 1), 130), b, fb("v1_%d" % (i + 1))) for i, (a, b, _) in enumerate(S1)) + ctl("v1"))

GB = ('<div class="gbox"><div class="gh">Saying prices</div>'
      '<p><b>€40 an hour</b> · <b>€300 a month</b> · <b>€80 a year</b> — we use <b>a / an</b> + time (= every hour / month / year).</p>'
      '<p><b>€8 per user per month</b> — <b>per</b> is more formal; it is common on pricing pages.</p>'
      '<p><b>free of charge</b> = free · <b>at no extra cost</b> = no additional fee</p>'
      '<p>Say: <i>€8</i> = eight euros · <i>$2.5 billion</i> = two point five billion dollars · <i>£399</i> = three hundred and ninety-nine pounds · <i>10–15%</i> = ten to fifteen percent</p></div>')
S2 = [("The designer charges €35", ["an hour", "a hour", "per a hour"]), ("Our plan costs €8 per user", ["per month", "a month per", "in month"]),
      ("The course costs €300 — books are included", ["at no extra cost", "with no extra cost", "for no extra cost"]), ("Delivery is free", ["of charge", "for charge", "in charge"])]
for i, (_, o) in enumerate(S2): K["p2_%d" % (i + 1)] = [o[0]]
import random
random.seed(7)
def shuf(o): o = o[:]; random.shuffle(o); return o
SAY = [("€8 per user per month", "eight euros per user per month", ["€8 per user per month", "8 euros per user per month", "€8 per user a month"]),
       ("$2.5 billion", "two point five billion dollars", ["$2.5 billion", "2.5 billion dollars", "$2,5 billion"]),
       ("£399", "three hundred and ninety-nine pounds", ["£399", "399 pounds", "399"]),
       ("10–15%", "ten to fifteen percent", ["10–15%", "10-15%", "10 to 15%", "10-15 percent", "10 to 15 percent"]),
       ("€159 a year", "one hundred and fifty-nine euros a year", ["€159 a year", "159 euros a year", "€159 per year"])]
for i, (_, _, a) in enumerate(SAY): K["l2_%d" % (i + 1)] = a
s2 = ('<div class="bsec">Prices</div><p class="ins"><b class="x">2</b><b>A</b> Read the box. Then choose the correct option.</p>' + GB +
      "".join('<div class="row">%d. %s %s.%s</div>' % (i + 1, a, sel("p2_%d" % (i + 1), shuf(o), 200), fb("p2_%d" % (i + 1))) for i, (a, o) in enumerate(S2)) + ctl("p2") +
      '<p class="ins" style="margin-top:24px"><b>B</b> Listen 🔊 and write the price. Then say it aloud.</p>' +
      "".join('<div class="row">%d. <button class="btn l" style="padding:2px 10px" onclick="say1(\'%s\')">🔊</button> %s%s</div>' % (i + 1, s, inp("l2_%d" % (i + 1), 240, "e.g. €20 a month"), fb("l2_%d" % (i + 1))) for i, (_, s, _) in enumerate(SAY)) + ctl("l2"))

S3 = [("The price of Microsoft 365 Personal in Australia went", ["up", "down", "on"], "from A$109 to A$159."), ("That is a 45% price", ["increase", "increasing", "grow"], "."),
      ("If you pay for a year, you", ["save", "safe", "spend"], "15%."), ("In January the price went", ["down", "up", "off"], "from €20 to €15 — a 25% discount."),
      ("The price will go up", ["from", "since", "of"], "€60 to €72 a year.")]
for i, (_, o, _) in enumerate(S3): K["p3_%d" % (i + 1)] = [o[0]]
s3 = ('<div class="bsec">Prices</div><p class="ins"><b class="x">3</b><b>A</b> Choose the correct word.</p>' +
      "".join('<div class="row">%d. %s %s %s%s</div>' % (i + 1, a, sel("p3_%d" % (i + 1), shuf(o), 130), b, fb("p3_%d" % (i + 1))) for i, (a, o, b) in enumerate(S3)) + ctl("p3") +
      '<p class="ins" style="margin-top:22px"><b>B</b> Think of a subscription you pay for (Netflix, Spotify, ChatGPT, iCloud …). Did the price go up? Write 2–3 sentences.</p>' +
      ta("p3w", "I pay for … The price went up from … to … I think it is / isn’t good value for money because …", 70))

CARD_A = ('<div class="card"><b>Student A — customer</b><br>You use a design tool, PixelPro (€15 a month). You want to <b>cancel</b>. Ask the support agent:'
          '<ul><li>Is there a cancellation fee?</li><li>Is it a monthly plan or an annual plan?</li><li>Can I get a refund for this month?</li><li>What does the cheaper plan include?</li></ul></div>')
CARD_B = ('<div class="card"><b>Student B — support agent</b><br>Answer with this information:'
          '<ul><li>It is an <b>annual plan, paid monthly</b>. Early termination fee: 50% of the remaining payments.</li><li>No refund for this month.</li>'
          '<li>Cheaper option: <b>Basic plan</b>, €6 a month, monthly, no cancellation fee. Includes 10 projects, no AI tools.</li><li>Try to keep the customer: offer 2 months free.</li></ul></div>')
PHR = ["Is there a cancellation fee?", "What does the price include?", "Are there any hidden fees?", "Can I get a refund?", "I’d like to cancel my subscription.", "I’m afraid there is a fee of …", "We can offer you …"]
s4 = ('<div class="bsec wr">Speaking</div><p class="ins"><b class="x">4</b>Work in pairs. Role-play a support chat on a video call. Then swap roles. (With your teacher: your teacher is Student B.)</p>'
      '<div class="chips">%s</div>' % "".join("<span>%s</span>" % p for p in PHR) + '<div class="two">' + CARD_A + CARD_B + '</div>' +
      '<p class="ins">After the role-play: Did you cancel or keep the plan? Why?</p>' + ta("s4", "I decided to … because …", 60) +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you talk about prices and fees now?"))
XJS = r"""function say1(t){try{speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(t);u.lang="en-GB";u.rate=.85;const v=speechSynthesis.getVoices().find(x=>/^en/i.test(x.lang));if(v)u.voice=v;speechSynthesis.speak(u)}catch(e){}}"""
h = page("7.2", "Services and subscriptions", "EXTRA", "Extra practice: fees vocabulary, saying prices, price changes, asking about fees.", "BP A2 7.2 Services · Extra", CODE,
         [("1", s1), ("2A–B", s2), ("3", s3), ("4", s4)], K, None, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, extra_js=XJS)
os.makedirs(os.path.dirname(OUT), exist_ok=True); open(OUT, "w").write(h); print("ok", OUT, len(h))
