"""Business Partner A2 · 7.2 Services and subscriptions — HOMEWORK (IT version, hidden fees).
1 Choose the word · 2 Collocations · 3 Reading: a subscription check in Slack · 4 Gap text: a price increase · 5 Writing: a Slack message about a subscription · Self-assessment.
Usage: python3 build_a2_hw_7-2.py OUT.html [STUDENT_CODE]
"""
import sys, os, json
from bp_page import page, fb, sel, inp, ta, ctl, radios, SELF
from vocab_a2 import lesson
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3b7dd8", "#e3eefb", "#2a5fb0", "#4f9be8"
_, GROUPS = lesson("7.2")
K = {}
VOC = [(g, [w[0] for w in ws]) for g, ws in GROUPS if g != "Services"]

C1 = [("There is no", ["cancellation", "booking", "fixed"], "fee if you cancel in the first 14 days."),
      ("The online course costs €200. The fee", ["includes", "charges", "pays"], "all videos and a certificate."),
      ("Our agency", ["charges", "pays", "includes"], "a fee of €35 an hour for design work."),
      ("I always read the", ["small print", "big print", "hidden print"], "before I sign up for a plan."),
      ("The app has a 7-day free", ["trial", "fee", "refund"], ". After that, you pay €9 a month."),
      ("I paid for a year, but I cancelled after one month. Can I get a", ["refund", "fee", "trial"], "?"),
      ("We pay a", ["fixed", "hidden", "additional"], "fee of €300 a month — the price doesn’t change."),
      ("The price went up from €10 to €13 — a 30% price", ["increase", "fee", "plan"], ".")]
for i, (a, o, b) in enumerate(C1): K["c1_%d" % (i + 1)] = [o[0]]
import random
random.seed(72)
def shuf(o): o = o[:]; random.shuffle(o); return o
s1 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">1</b>Choose the correct word.</p>' +
      "".join('<div class="row">%d. %s %s %s%s</div>' % (i + 1, a, sel("c1_%d" % (i + 1), shuf(o), 150), b, fb("c1_%d" % (i + 1))) for i, (a, o, b) in enumerate(C1)) + ctl("c1"))

C2 = [("sign up", "for a plan"), ("cancel", "a subscription"), ("get", "a refund"), ("read", "the small print"), ("charge", "customers €5 for delivery"), ("start", "a free trial")]
ENDS = sorted(e for _, e in C2)
for i, (v, e) in enumerate(C2): K["c2_%d" % (i + 1)] = [e]
s2 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">2</b>Match the verbs (1–6) with the words to make collocations.</p>' +
      "".join('<div class="row"><span class="w" style="min-width:90px">%d. %s</span>%s%s</div>' % (i + 1, v, sel("c2_%d" % (i + 1), ENDS, 260), fb("c2_%d" % (i + 1))) for i, (v, e) in enumerate(C2)) + ctl("c2") +
      '<p class="ins" style="margin-top:20px">Now write two sentences about you with two of the collocations.</p>' + ta("c2w", "Last year I signed up for … / I never read …", 60))

SLACK = ('<div class="slack"><div><b>Olha (Team Lead)</b><span class="t">10:42</span></div>'
         '<p>Hi team! 👋 I checked our subscriptions this month. Here are the results:</p>'
         '<p>🟦 <b>BoardPro</b> (tasks): we pay a <b>fixed fee</b> of €120 a month for 15 users. The fee includes everything. No problems here ✅</p>'
         '<p>🟪 <b>DesignHub</b> (design software): the price looks low — €12 per user per month. But it is an <b>annual plan, paid monthly</b>. If we cancel before December, we pay an <b>early termination fee</b> of €340 😬</p>'
         '<p>🟩 <b>CloudBox</b> (cloud storage): €50 a month for 2 TB. Last month we used 2.4 TB, so they charged an <b>additional fee</b> of €25. We need to delete old files!</p>'
         '<p>🟧 <b>MeetNow</b> (video calls): we don’t use it any more — we use Google Meet. But nobody cancelled it, so we still pay €30 a month 🙈</p>'
         '<p>Please reply in the thread: which tools do you really need? Thanks!</p></div>')
Q3 = [("BoardPro has an early termination fee.", "F"), ("The price of BoardPro includes everything.", "T"), ("DesignHub is a monthly plan — the team can cancel at any time for free.", "F"),
      ("The team paid an additional fee for CloudBox because they used more storage.", "T"), ("The team still uses MeetNow every day.", "F"), ("Olha wants people to answer in the thread.", "T")]
for i, (q, a) in enumerate(Q3): K["r3_%d" % (i + 1)] = [a]
WH3 = [("Which tool has a hidden fee for cancelling?", "DesignHub (early termination fee of €340)"), ("How can the team save money? Give two ideas.", "Cancel MeetNow (€30 a month). Delete old files in CloudBox to stop the additional fee. Don’t renew DesignHub in December.")]
s3 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">3</b><b>A</b> Read the Slack message. Are the sentences <i>true</i> (T) or <i>false</i> (F)?</p>' + SLACK +
      "".join('<div class="tf"><span class="q">%d. %s</span>%s%s</div>' % (i + 1, q, "".join('<label class="opt" style="display:inline;margin:0 10px 0 0"><input type="radio" name="r3_%d" data-k="r3_%d" value="%s"> %s</label>' % (i + 1, i + 1, x, x) for x in "TF"), fb("r3_%d" % (i + 1))) for i, (q, a) in enumerate(Q3)) +
      ctl("r3", "chkRad") +
      '<p class="ins" style="margin-top:20px"><b>B</b> Answer the questions.</p>' +
      "".join('<p class="ins"><span class="q">%d</span>%s</p>%s<button class="btn l" onclick="model(\'m3_%d\')" style="margin-top:6px">Show answer</button><div class="model" id="m3_%d">%s</div>' % (i + 1, q, ta("q3_%d" % (i + 1), "", 46), i + 1, i + 1, a) for i, (q, a) in enumerate(WH3)))

BOX4 = ["annual", "cancel", "hidden", "includes", "increase", "monthly", "refund", "sign up"]
T4 = [("annual", "annual"), ("increase", "increase"), ("includes", "includes"), ("monthly", "monthly"), ("cancel", "cancel"), ("refund", "refund"), ("hidden", "hidden"), ("sign up", "sign up")]
for i, (a, _) in enumerate(T4): K["g4_%d" % (i + 1)] = [a]
g = lambda n: '<sup>%d</sup>%s' % (n, inp("g4_%d" % n, 110))
TXT4 = ('<div class="slack"><div><b>NoteFlow</b> <span class="t">email · Your plan is changing</span></div><p>Dear customer,</p>'
        '<p>Thank you for using NoteFlow! From 1 March, the %s fee for NoteFlow Pro will go up from €60 to €72 a year. This price %s is because we added an AI assistant. '
        'The new price %s the AI assistant, 100 GB of cloud storage and support in a chat.</p>'
        '<p>Don’t want to pay for a year? You can choose our %s plan: €7 a month. You can %s it any time, with no cancellation fee. '
        'If you cancel in the first 14 days, you get a full %s.</p>'
        '<p>We don’t have any %s fees — everything is on our pricing page. You don’t need to %s again: your plan changes automatically.</p><p>The NoteFlow team</p></div>'
        % tuple(g(i + 1) for i in range(8)))
s4 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">4</b>Complete the email with the words in the box.</p><div class="box">%s</div>' % " · ".join(BOX4) + TXT4 +
      "".join(fb("g4_%d" % (i + 1)) for i in range(8)) + ctl("g4") +
      '<p class="ins" style="margin-top:20px">Is this an honest email? Why? / Why not?</p>' + ta("y4", "I think it is / isn’t honest because …", 50))

MODEL5 = ("Hi Olha! About Notion: we pay €10 per user per month. The fee includes unlimited pages and the AI assistant. "
          "There are no hidden fees, and we can cancel any time with no cancellation fee. I use it every day for meeting notes, so I think we need it. "
          "But we pay an additional fee for 5 guest users — I think we can stop that. Thanks!")
s5 = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">5</b>Reply to Olha in the thread. Write about <b>one</b> tool or subscription you use at work (or invent one). 50–80 words.</p>'
      '<div class="ext"><ul style="margin:0;padding-left:20px"><li>How much do you pay? (a fixed / monthly / annual fee, per user per month)</li><li>What does the fee include?</li>'
      '<li>Are there any additional or hidden fees? Is there a cancellation fee?</li><li>Do you need it? Why? / Why not?</li></ul></div>' +
      ta("w5", "Hi Olha! About … we pay …", 160) + '<p class="hint" id="w5c"></p>'
      '<button class="btn l" onclick="model(\'m5\')">Show a model answer</button><div class="model" id="m5">%s</div>' % MODEL5 +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you explain the cost of a service now?"))
XJS = r"""function wc(){const t=document.querySelector('.g[data-k="w5"]');if(!t)return;const n=(t.value.trim().match(/\S+/g)||[]).length;document.getElementById("w5c").textContent=n+" words (aim: 50–80)"}
document.addEventListener("input",e=>{if(e.target.dataset&&e.target.dataset.k==="w5")wc()});window.afterFill=wc;"""
h = page("7.2", "Services and subscriptions", "HOMEWORK", "Learners can explain the cost of a service.", "BP A2 7.2 Services · Homework", CODE,
         [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5)], K, VOC, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, extra_js=XJS)
os.makedirs(os.path.dirname(OUT), exist_ok=True); open(OUT, "w").write(h); print("ok", OUT, len(h))
