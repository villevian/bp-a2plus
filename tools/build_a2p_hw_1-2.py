"""Business Partner A2+ · 1.2 Events management — HOMEWORK (2026, bleisure / Barcelona).
1 Vocabulary · 2 Forms · 3 Reading: three hotels near the conference centre · 4 Correct the mistakes · 5 Writing: a message recommending a hotel.
Usage: python3 build_a2p_hw_1-2.py OUT.html [STUDENT_CODE]
"""
import sys, os
from bp_page import page, fb, sel, inp, ta, ctl, SELF
from vocab_a2p import lesson
import vcard
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3fa9ad", "#e6f4f4", "#2b8185", "#5cc1c4"
VOC, VJS = vcard.build(lesson("1.2")[1], ACC, ACC2, DARK)
K = {}
BOX = ["arrange", "budget", "client", "entertainment", "guests", "organised", "staff", "venue"]
S1 = [("Our ", " is a big bank. They want a conference for 300 people.", "client"), ("The ", " is a hotel with a view of the sea.", "venue"),
      ("We invited 120 ", ", but only 95 came.", "guests"), ("The hotel has 25 ", " — waiters, cooks and a manager.", "staff"),
      ("For ", ", we have a DJ and a magician.", "entertainment"), ("We have a small ", ", so we can’t choose an expensive hotel.", "budget"),
      ("Can you ", " a bus from the airport to the hotel?", "arrange"), ("Alicia is very ", " — she plans everything in her calendar.", "organised")]
for i, (_, _, a) in enumerate(S1): K["v1_%d" % (i + 1)] = [a]
s1 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">1</b>Complete the sentences with the words in the box.</p><div class="box">%s</div>' % " · ".join(BOX) +
      "".join('<div class="row">%d. %s%s%s%s</div>' % (i + 1, a, inp("v1_%d" % (i + 1), 140), b, fb("v1_%d" % (i + 1))) for i, (a, b, _) in enumerate(S1)) + ctl("v1"))

F2 = [("cheap", "cheaper", "the cheapest"), ("big", "bigger", "the biggest"), ("easy", "easier", "the easiest"), ("hot", "hotter", "the hottest"),
      ("expensive", "more expensive", "the most expensive"), ("comfortable", "more comfortable", "the most comfortable"), ("good", "better", "the best"), ("bad", "worse", "the worst")]
for i, (a, c, s) in enumerate(F2): K["f2c_%d" % (i + 1)] = [c]; K["f2s_%d" % (i + 1)] = [s]
s2 = ('<div class="bsec">Grammar</div><p class="ins"><b class="x">2</b>Write the comparative and superlative forms.</p><table class="tb"><tr><th>adjective</th><th>comparative</th><th>superlative</th></tr>' +
      "".join('<tr><td>%s</td><td>%s%s</td><td>%s%s</td></tr>' % (a, inp("f2c_%d" % (i + 1), 170), fb("f2c_%d" % (i + 1)), inp("f2s_%d" % (i + 1), 190), fb("f2s_%d" % (i + 1))) for i, (a, _, _) in enumerate(F2)) +
      '</table>' + ctl("f2"))

HOT = [("A", "Hotel Diagonal Business", "€190 a night", "5 minutes on foot", "8.9", "meeting rooms, fast Wi-Fi, gym", "far from the beach (35 min)"),
       ("B", "Casa Gòtic Boutique", "€140 a night", "25 minutes by metro", "9.3", "rooftop bar, old town, quiet rooms", "small rooms, no gym"),
       ("C", "Barceloneta Beach Hostel", "€85 a night", "40 minutes by metro", "7.8", "next to the beach, free bikes", "noisy at night, shared kitchen")]
CARDS = '<div class="hot">' + "".join('<div class="hc"><div class="hh"><b>%s</b> %s <span class="rt">%s</span></div><p>💶 %s · 🚶 to the conference centre: %s</p><p>👍 %s</p><p>👎 %s</p></div>' % (l, n, r, p, d, plus, minus) for l, n, p, d, r, plus, minus in HOT) + '</div>'
Q3 = [("Which hotel is the cheapest?", "C"), ("Which hotel is the closest to the conference centre?", "A"), ("Which hotel has the best rating?", "B"),
      ("Which hotel is the best for a weekend at the beach?", "C"), ("Which hotel is better for working: A or B?", "A"), ("Which hotel is the most expensive?", "A")]
for i, (_, a) in enumerate(Q3): K["r3_%d" % (i + 1)] = [a]
s3 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">3</b><b>A</b> You are going to a conference in Barcelona (Thursday–Friday) and you want to stay for the weekend. Read about three hotels and answer the questions.</p>' + CARDS +
      "".join('<div class="tf"><span class="q">%d. %s</span>%s%s</div>' % (i + 1, q, "".join('<label class="opt" style="display:inline;margin:0 10px 0 0"><input type="radio" name="r3_%d" data-k="r3_%d" value="%s"> %s</label>' % (i + 1, i + 1, x, x) for x in "ABC"), fb("r3_%d" % (i + 1))) for i, (q, _) in enumerate(Q3)) +
      ctl("r3", "chkRad") + '<p class="ins" style="margin-top:20px"><b>B</b> Which hotel would you choose for the conference and the weekend? Why?</p>' + ta("r3b", "I would choose … because it’s … than …", 50))

E4 = [("This hotel is more cheaper than the other one.", ["This hotel is cheaper than the other one."]), ("The rooftop is the most good place for the party.", ["The rooftop is the best place for the party."]),
      ("Barcelona is hoter than London in July.", ["Barcelona is hotter than London in July."]), ("A boat trip is more fun that a bus tour.", ["A boat trip is more fun than a bus tour."]),
      ("This is the bigest conference in Spain.", ["This is the biggest conference in Spain."]), ("The metro is easyer than a taxi.", ["The metro is easier than a taxi."])]
for i, (_, a) in enumerate(E4): K["e4_%d" % (i + 1)] = a
s4 = ('<div class="bsec">Grammar</div><p class="ins"><b class="x">4</b>Correct the mistake in each sentence. Write the correct sentence.</p>' +
      "".join('<div class="row">%d. <s style="color:#8a8b8d">%s</s><br>%s%s</div>' % (i + 1, w, inp("e4_%d" % (i + 1), 520), fb("e4_%d" % (i + 1))) for i, (w, _) in enumerate(E4)) + ctl("e4"))

MODEL = ("Hi Marta! I’m looking at hotels for the Barcelona conference. Hotel Diagonal is the closest to the conference centre and it’s better for working, but it’s the most expensive. "
         "Casa Gòtic is cheaper and it has the best rating. It’s further from the conference, but the old town is more interesting for the weekend. "
         "I think Casa Gòtic is the best option for us. What do you think?")
s5 = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">5</b>Write a message to a colleague who is going to the same conference. Recommend one hotel from Exercise 3. Use at least three comparatives and two superlatives. 60–90 words.</p>' +
      ta("w5", "Hi …! I’m looking at hotels for the conference. …", 160) + '<p class="hint" id="w5c"></p>'
      '<button class="btn l" onclick="model(\'m5\')">Show a model answer</button><div class="model" id="m5">%s</div>' % MODEL +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you make simple comparisons now?"))
XJS = VJS + r"""
document.head.insertAdjacentHTML("beforeend",`<style>table.tb{border-collapse:collapse;width:100%;margin:10px 0;font-size:15px}table.tb th,table.tb td{border:1px solid #c8c9cb;padding:6px 10px;text-align:left}table.tb th{background:#f3f4f6;font-weight:600}
.hot{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:10px 0}.hc{border:1px solid #d5d6d7;border-radius:8px;background:#fff;font-size:15px}.hc p{margin:6px 12px}.hh{background:#e6f4f4;padding:6px 12px;border-radius:8px 8px 0 0}.hh .rt{float:right;background:#2b8185;color:#fff;border-radius:6px;padding:0 6px;font-weight:600}
@media(max-width:800px){.hot{grid-template-columns:1fr}}</style>`);
function wc(){const t=document.querySelector('.g[data-k="w5"]');if(!t)return;const n=(t.value.trim().match(/\S+/g)||[]).length;document.getElementById("w5c").textContent=n+" words (aim: 60–90)"}
document.addEventListener("input",e=>{if(e.target.dataset&&e.target.dataset.k==="w5")wc()});window.afterFill=wc;"""
h = page("1.2", "Events management", "HOMEWORK", "Learners can make simple comparisons.", "BP A2+ 1.2 Events management · Homework", CODE,
         [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5)], K, VOC, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, extra_js=XJS)
os.makedirs(os.path.dirname(OUT), exist_ok=True); open(OUT, "w").write(h); print("ok hw", len(h))
