"""Business Partner A2+ · 1.2 Events management — EXTRA (coursebook Extra activities 1.2 A–B, updated) + spelling + speaking: plan the bleisure weekend.
Usage: python3 build_a2p_extra_1-2.py OUT.html [STUDENT_CODE]
"""
import sys, os, random
from bp_page import page, fb, sel, inp, ta, ctl, SELF
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3fa9ad", "#e6f4f4", "#2b8185", "#5cc1c4"
K = {}
BOX = ["arrange", "clients", "guests", "manage", "organised", "plan", "staff", "venue"]
A = [("I help them ", " an event, like a big annual conference, a product launch, or a fun team offsite.", "plan"),
     ("About ninety percent of my corporate ", " are businesses.", "clients"),
     ("How do you ", " a budget?", "manage"),
     ("For a cheap event, we choose the least expensive ", " possible.", "venue"),
     ("We rented a fantastic rooftop and invited about three hundred ", ".", "guests"),
     ("You have to ", " all the food, tables and chairs.", "arrange"),
     ("… coordinate the ", ", and check every single thing.", "staff"),
     ("You have to be ", " and pay attention to detail.", "organised")]
for i, (_, _, a) in enumerate(A): K["a_%d" % (i + 1)] = [a]
s1 = ('<div class="bsec">Extra activities</div><p class="ins"><b class="x">A</b>Complete the sentences from Alicia’s interview with the words in the box. Then listen again and check.</p><div class="box">%s</div>' % " · ".join(BOX) +
      '<div class="aud"><span class="an">🔊 1.01</span><audio controls preload="none" src="../audio/1-01.mp3"></audio></div>' +
      "".join('<div class="row">%d. %s%s%s%s</div>' % (i + 1, a, inp("a_%d" % (i + 1), 130), b, fb("a_%d" % (i + 1))) for i, (a, b, _) in enumerate(A)) + ctl("a"))

B = [("option / want / cheapest / We / the", "We want the cheapest option."), ("is / A hotel for 50 / than / cheaper / a hotel for 500", "A hotel for 50 is cheaper than a hotel for 500."),
     ("need / conference room / We / biggest / the", "We need the biggest conference room."), ("want / the / We / to hire / staff / best", "We want to hire the best staff."),
     ("is / An online event / a hybrid event / easier / than", "An online event is easier than a hybrid event."), ("is / weather / Rain / the / for an outdoor party / worst", "Rain is the worst weather for an outdoor party."),
     ("is / A taxi / more / the metro / expensive / than", "A taxi is more expensive than the metro."), ("is / less / Managing three people / than / managing twenty people / difficult", "Managing three people is less difficult than managing twenty people.")]
for i, (_, a) in enumerate(B): K["b_%d" % (i + 1)] = [a, a.rstrip(".")]
s2 = ('<div class="bsec">Extra activities</div><p class="ins"><b class="x">B</b>Put the words in the correct order to make sentences.</p>' +
      "".join('<div class="row">%d. <i style="color:#6d6e70">%s</i><br>%s%s</div>' % (i + 1, w, inp("b_%d" % (i + 1), 560), fb("b_%d" % (i + 1))) for i, (w, _) in enumerate(B)) + ctl("b"))

random.seed(3)
C = [("big", ["bigger", "biger"]), ("easy", ["easier", "easyer"]), ("nice", ["nicer", "nicer than"]), ("hot", ["the hottest", "the hotest"]), ("busy", ["the busiest", "the busyest"]), ("late", ["later", "latter"])]
C[2] = ("nice", ["nicer", "niceer"])
for i, (_, o) in enumerate(C): K["c_%d" % (i + 1)] = [o[0]]
SP = ('<div class="gbox"><div class="gh">Spelling</div><p>big → bi<b>gg</b>er, the bi<b>gg</b>est (one vowel + one consonant → double it)<br>easy → eas<b>i</b>er, the eas<b>i</b>est (y → i)<br>nice → nice<b>r</b>, the nice<b>st</b> (e → + r / st)</p></div>')
s3 = ('<div class="bsec">Grammar</div><p class="ins"><b class="x">C</b>Read the box. Then choose the correct spelling.</p>' + SP +
      "".join('<div class="row">%d. %s → %s%s</div>' % (i + 1, w, sel("c_%d" % (i + 1), sorted(o), 150), fb("c_%d" % (i + 1))) for i, (w, o) in enumerate(C)) + ctl("c"))

WK = [("Montserrat day trip", "€45 (train + cable car)", "a full day", "mountains, monastery, great views", "busy on Saturday"),
      ("Beach + tapas tour", "€30–60", "half a day", "relaxing, the sea, local food", "very hot in summer"),
      ("Sagrada Família + Park Güell", "€26 + €18 (book online)", "a full day", "the most famous places in Barcelona", "a lot of tourists")]
TAB = ('<table class="tb"><tr><th></th><th>Price</th><th>Time</th><th>Good things</th><th>Problems</th></tr>' +
       "".join("<tr><td><b>%s</b></td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>" % w for w in WK) + "</table>")
s4 = ('<div class="bsec wr">Speaking</div><p class="ins"><b class="x">D</b>The conference finishes on Friday. You and a colleague are staying in Barcelona for the weekend. Compare the three options and decide what to do on Saturday and Sunday.</p>' + TAB +
      '<div class="chips"><span>… is cheaper / more expensive than …</span><span>… is the most interesting …</span><span>I think … is better because …</span><span>Let’s do … on Saturday.</span></div>' +
      ta("d", "On Saturday we want to … because it’s … than … On Sunday …", 90) +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you compare options now?"))
XJS = r"""document.head.insertAdjacentHTML("beforeend",`<style>.aud{display:flex;gap:10px;align-items:center;background:#e6f4f4;padding:8px 12px;border-radius:6px;margin:8px 0}.aud .an{font-weight:600;color:#2b8185}.aud audio{height:36px}
table.tb{border-collapse:collapse;width:100%;margin:10px 0;font-size:15px}table.tb th,table.tb td{border:1px solid #c8c9cb;padding:6px 10px;text-align:left;vertical-align:top}table.tb th{background:#f3f4f6;font-weight:600}</style>`);"""
h = page("1.2", "Events management", "EXTRA", "Extra practice: event vocabulary, comparatives and superlatives, spelling, planning the weekend.", "BP A2+ 1.2 Events management · Extra", CODE,
         [("A", s1), ("B", s2), ("C", s3), ("D", s4)], K, None, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, extra_js=XJS)
os.makedirs(os.path.dirname(OUT), exist_ok=True); open(OUT, "w").write(h); print("ok extra", len(h))
