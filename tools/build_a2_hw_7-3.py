"""Business Partner A2 · 7.3 The best providers — HOMEWORK (new context: coworking spaces and internet for a new office).
1 Write the superlatives · 2 Complete the collocations (first letter) · 3 Reading: three coworking spaces — which one? · 4 Correct the mistakes · 5 Writing: an email with Strengths / Areas of improvement · Self-assessment.
Usage: python3 build_a2_hw_7-3.py OUT.html [STUDENT_CODE]
"""
import sys, os
from bp_page import page, fb, sel, inp, ta, ctl, SELF
from vocab_a2 import lesson
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3b7dd8", "#e3eefb", "#2a5fb0", "#4f9be8"
_, GROUPS = lesson("7.3")
K = {}
VOC = [(g, [w[0] for w in ws]) for g, ws in GROUPS]

A1 = [("easy", "the easiest"), ("reliable", "the most reliable"), ("big", "the biggest"), ("good", "the best"), ("cheap", "the cheapest"), ("friendly", "the friendliest"),
      ("bad", "the worst"), ("expensive", "the most expensive"), ("quiet", "the quietest"), ("wide", "the widest")]
for i, (_, a) in enumerate(A1): K["h1_%d" % (i + 1)] = [a]
s1 = ('<div class="bsec">Grammar</div><p class="ins"><b class="x">1</b>Write the superlative form. Don’t forget <i>the</i>!</p><div class="two">' +
      "".join('<div class="row">%d. %s → %s%s</div>' % (i + 1, w, inp("h1_%d" % (i + 1), 190), fb("h1_%d" % (i + 1))) for i, (w, _) in enumerate(A1)) + '</div>' + ctl("h1"))

C2 = [("The internet here is very fast — the download s", "peed", "speed"), ("Our new tool is cheap and very good. It’s great value for m", "oney", "money"),
      ("The support team fixes everything quickly. Their problem s", "olving", "solving"), ("The operator works everywhere, even in the metro: great network c", "overage", "coverage"),
      ("91% of clients are happy. They have the most s", "atisfied customers", "satisfied customers"), ("The staff know a lot. Staff k", "nowledge", "knowledge"),
      ("You can write to them 24/7 in a chat. It’s easy to a", "ccess", "access")]
for i, (_, _, a) in enumerate(C2): K["h2_%d" % (i + 1)] = [a, a.split()[-1]]
s2 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">2</b>Complete the words from the lesson. The first letter is there.</p>' +
      "".join('<div class="row">%d. %s%s%s</div>' % (i + 1, a, inp("h2_%d" % (i + 1), 170, "…"), fb("h2_%d" % (i + 1))) for i, (a, _, _) in enumerate(C2)) + ctl("h2") +
      '<p class="hint">Write only the missing part of the word.</p>')
K.update({"h2_%d" % (i + 1): [b, c] for i, (_, b, c) in enumerate(C2)})

TXT3 = ('<div class="mail"><div class="mh"><b>From:</b> Daria (HR)<br><b>To:</b> the team<br><b>Subject:</b> Our new office: three coworking spaces</div>'
        '<p>Hi everyone,</p><p>We need a coworking space in Lviv for 12 people. I visited three. Please find a summary below.</p>'
        '<p><b>HubSpace</b> is in the city centre — it’s the nearest to the train station. It’s also the biggest: 400 m², with a big kitchen. But it’s the most expensive: €180 per person per month, and it’s very noisy.</p>'
        '<p><b>Green Desk</b> is the cheapest: €110 per person. It’s the quietest place — great for calls. The internet is the slowest (only 50 Mbps), and the kitchen is very small.</p>'
        '<p><b>Loft 21</b> costs €140. It has the fastest internet (1 Gbps) and the friendliest staff — they help with printers, post and everything. It isn’t in the centre: 20 minutes by tram.</p>'
        '<p>If you have any questions, please let me know.</p><p>Best regards,<br>Daria</p></div>')
Q3 = [("is the quietest?", "Green Desk"), ("has the fastest internet?", "Loft 21"), ("is the most expensive?", "HubSpace"), ("has the friendliest staff?", "Loft 21"),
      ("is the nearest to the train station?", "HubSpace"), ("has the slowest internet?", "Green Desk")]
NAMES = ["HubSpace", "Green Desk", "Loft 21"]
for i, (_, a) in enumerate(Q3): K["h3_%d" % (i + 1)] = [a]
s3 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">3</b><b>A</b> Read the email. Which coworking space …</p>' + TXT3 +
      "".join('<div class="tf"><span class="q">%d. … %s</span>%s%s</div>' % (i + 1, q, "".join('<label class="opt" style="display:inline;margin:0 12px 0 0"><input type="radio" name="h3_%d" data-k="h3_%d" value="%s"> %s</label>' % (i + 1, i + 1, n, n) for n in NAMES), fb("h3_%d" % (i + 1)))
              for i, (q, a) in enumerate(Q3)) + ctl("h3", "chkRad") +
      '<p class="ins" style="margin-top:20px"><b>B</b> Your team does a lot of video calls. Which space would you choose? Why?</p>' + ta("h3b", "I would choose … because it’s the … and it has the …", 60))

E4 = [("Volt is the most cheap operator.", "Volt is the cheapest operator."), ("LineUp has the better support of the three.", "LineUp has the best support of the three."),
      ("This is the most fast internet in our office.", "This is the fastest internet in our office."), ("SkyMobile is most reliable provider.", "SkyMobile is the most reliable provider."),
      ("They have the baddest problem solving.", "They have the worst problem solving."), ("Kyivstar is the bigest operator in Ukraine.", "Kyivstar is the biggest operator in Ukraine.")]
for i, (_, a) in enumerate(E4): K["h4_%d" % (i + 1)] = [a]
s4 = ('<div class="bsec">Grammar</div><p class="ins"><b class="x">4</b>Each sentence has one mistake. Write the correct sentence.</p>' +
      "".join('<div class="row">%d. <span style="color:#b3261e">%s</span><br>%s%s</div>' % (i + 1, q, inp("h4_%d" % (i + 1), 470), fb("h4_%d" % (i + 1))) for i, (q, _) in enumerate(E4)) + ctl("h4"))

MODEL5 = ("Dear Olha,\nPlease find attached the offers from three internet providers for our new office. Please find a summary below.\n"
          "I recommend FiberNet. Strengths: FiberNet has the fastest internet and the best support — they answer in 5 minutes.\n"
          "Areas of improvement: it is the most expensive provider, €90 a month.\nIf you have any questions, please let me know.\nBest regards,\nPavlo")
s5 = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">5</b>Your company is choosing an <b>internet provider</b> for the new office. Write an email to your manager (50–80 words). Recommend one provider.</p>'
      '<table class="tb stars"><tr><th></th><th>FiberNet</th><th>CityLink</th><th>OptiNet</th></tr><tr><td>Speed</td><td>1 Gbps</td><td>500 Mbps</td><td>300 Mbps</td></tr>'
      '<tr><td>Price a month</td><td>€90</td><td>€60</td><td>€45</td></tr><tr><td>Support answers in</td><td>5 min</td><td>1 hour</td><td>1 day</td></tr><tr><td>Generator / works without electricity</td><td>✓</td><td>✓</td><td>✗</td></tr></table>'
      '<div class="ext"><ul style="margin:0;padding-left:20px"><li>Please find attached … / Please find a summary below.</li><li>Strengths: … has the …</li><li>Areas of improvement: …</li><li>If you have any questions, please let me know. Best regards,</li></ul></div>' +
      ta("w5", "Dear …, Please find attached …", 170) + '<p class="hint" id="w5c"></p>'
      '<button class="btn l" onclick="model(\'m5\')">Show a model answer</button><div class="model" id="m5">%s</div>' % MODEL5 +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you compare services now?"))
XJS = r"""document.head.insertAdjacentHTML("beforeend",`<style>.mail{border:1px solid #d5d6d7;border-radius:8px;padding:6px 18px;background:#fff;margin:10px 0}.mail .mh{background:#f3f4f6;margin:4px -18px 8px;padding:8px 18px;font-size:14.5px;line-height:1.6}
.two{display:grid;grid-template-columns:1fr 1fr;gap:4px 24px}table.tb{border-collapse:collapse;width:100%;margin:10px 0;font-size:15px}table.tb th,table.tb td{border:1px solid #c8c9cb;padding:6px 10px;text-align:center}table.tb td:first-child{text-align:left}table.tb th{background:#f3f4f6}
@media(max-width:700px){.two{grid-template-columns:1fr}}</style>`);
function wc(){const t=document.querySelector('.g[data-k="w5"]');if(!t)return;const n=(t.value.trim().match(/\S+/g)||[]).length;document.getElementById("w5c").textContent=n+" words (aim: 50–80)"}
document.addEventListener("input",e=>{if(e.target.dataset&&e.target.dataset.k==="w5")wc()});window.afterFill=wc;"""
h = page("7.3", "The best providers", "HOMEWORK", "Learners can compare services.", "BP A2 7.3 Providers · Homework", CODE,
         [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5)], K, VOC, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, extra_js=XJS)
os.makedirs(os.path.dirname(OUT), exist_ok=True); open(OUT, "w").write(h); print("ok", OUT, len(h))
