"""General English B2+ · Pet peeves — EXTRA HOMEWORK: collocations from the Cut video (100 People Tell Us Their Pet Peeves). English only.
1 Verb + collocation · 2 Prepositions · 3 Complete the sentences · 4 Odd one out · 5 Your pet peeves (writing).
Usage: python3 build_ge_peeves_extra.py OUT.html [STUDENT_CODE]
"""
import sys, os, random
from bp_page import page, fb, sel, inp, ta, ctl, SELF
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GRAD2 = "#c2416b", "#fbe7ee", "#9e2d55", "#ef7fa0"
K = {}
random.seed(42)
def shuf(o): o = o[:]; random.shuffle(o); return o

VIDEO = ('<div class="vbox"><div class="vt"><span class="vn">▶</span> Cut · 100 People Tell Us Their Pet Peeves <span class="vd">3:40</span> '
         '<a href="https://www.youtube.com/watch?v=sAvIKc3dxug" target="_blank">open on YouTube</a></div>'
         '<div class="fr"><iframe src="https://www.youtube-nocookie.com/embed/sAvIKc3dxug?rel=0&cc_load_policy=1&cc_lang_pref=en&hl=en" allowfullscreen loading="lazy"></iframe></div></div>')
VOCAB = [("From the video", ["cut in line", "cut someone off", "flake out on someone", "leave the cap off", "pop your gum", "chew with your mouth open", "pick your nose",
                             "roll your eyes at someone", "keep to the right", "use your indicator", "brake for no reason", "respect personal space", "brag about something", "comment on everything", "overreact to something"])]

C1 = [("cut", "in line at a coffee shop"), ("flake", "out on your friends"), ("leave", "the cap off the toothpaste"), ("pop", "your gum"), ("pick", "your nose"),
      ("roll", "your eyes at someone"), ("keep", "to the right on the escalator"), ("respect", "other people’s personal space"), ("knock", "before you come in"), ("flush", "the toilet")]
ENDS = sorted(e for _, e in C1)
for i, (v, e) in enumerate(C1): K["c1_%d" % (i + 1)] = [e]
s1 = ('<div class="bsec">Collocations</div><p class="ins"><b class="x">1</b>All these collocations are in the video. Match the verbs (1–10) with the right endings.</p>' + VIDEO +
      "".join('<div class="row"><span class="w" style="min-width:90px">%d. %s</span>%s%s</div>' % (i + 1, v, sel("c1_%d" % (i + 1), ENDS, 320), fb("c1_%d" % (i + 1))) for i, (v, _) in enumerate(C1)) + ctl("c1"))

P2 = [("People who flake out", "on", "you at the last minute drive me mad."), ("I hate it when people complain", "about", "things they do themselves."),
      ("Don’t roll your eyes", "at", "me — I’m just asking!"), ("On the escalator, please keep", "to", "the right."), ("He always comments", "on", "every single scene in the film."),
      ("She’s always bragging", "about", "her new car."), ("Some people stare", "at", "you at the gym."), ("A guy cut in front", "of", "me in the queue."),
      ("Why do you always point", "out", "that I’m sweaty?"), ("Be careful not to step", "on", "the snails!")]
PREPS = ["about", "at", "of", "on", "out", "to"]
for i, (_, p, _) in enumerate(P2): K["p2_%d" % (i + 1)] = [p]
s2 = ('<div class="bsec">Prepositions</div><p class="ins"><b class="x">2</b>Choose the correct preposition.</p>' +
      "".join('<div class="row">%d. %s %s %s%s</div>' % (i + 1, a, sel("p2_%d" % (i + 1), PREPS, 90), b, fb("p2_%d" % (i + 1))) for i, (a, _, b) in enumerate(P2)) + ctl("p2"))

BOX3 = ["brakes", "brag", "cut me off", "flaked out", "overreacts", "personal space", "pops", "use their indicator"]
G3 = [("My colleague ", " her gum all day. It’s so loud!", ["pops"]), ("A car ", " on the motorway and I nearly crashed.", ["cut me off"]),
      ("My friend ", " on me again — she cancelled our dinner an hour before.", ["flaked out"]), ("Half the drivers in this city never ", ". How am I supposed to know where they’re going?", ["use their indicator"]),
      ("He always ", " — you say one small thing and he starts shouting.", ["overreacts"]), ("Please don’t stand so close. I need some ", ".", ["personal space"]),
      ("I can’t stand people who ", " about how much money they make.", ["brag"]), ("The driver in front of me ", " for no reason, even when there’s no traffic.", ["brakes"])]
for i, (_, _, a) in enumerate(G3): K["g3_%d" % (i + 1)] = a
s3 = ('<div class="bsec">Collocations</div><p class="ins"><b class="x">3</b>Complete the sentences with the words in the box. Change the form if necessary.</p><div class="box">%s</div>' % " · ".join(BOX3) +
      "".join('<div class="row">%d. %s%s%s%s</div>' % (i + 1, a, inp("g3_%d" % (i + 1), 170), b, fb("g3_%d" % (i + 1))) for i, (a, b, _) in enumerate(G3)) + ctl("g3"))

O4 = [("cut", ["in line", "someone off", "in front of someone", "your eyes"], "your eyes"), ("pop", ["your gum", "a balloon", "bubble wrap", "the toilet"], "the toilet"),
      ("keep", ["to the right", "your distance", "a secret", "your nose"], "your nose"), ("leave", ["the cap off", "the lights on", "the door open", "your eyes at someone"], "your eyes at someone"),
      ("roll", ["your eyes", "your sleeves up", "the dice", "the queue"], "the queue"), ("respect", ["personal space", "other people’s time", "the rules", "your gum"], "your gum")]
for i, (_, o, a) in enumerate(O4): K["o4_%d" % (i + 1)] = [a]
s4 = ('<div class="bsec">Collocations</div><p class="ins"><b class="x">4</b>Odd one out. Which word or phrase does NOT go with the verb?</p>' +
      "".join('<div class="row">%d. <b>%s</b> … %s%s</div>' % (i + 1, v, sel("o4_%d" % (i + 1), shuf(o), 230), fb("o4_%d" % (i + 1))) for i, (v, o, _) in enumerate(O4)) + ctl("o4"))

MODEL = ("1 It really gets on my nerves when people cut in line at the supermarket.\n2 I can’t stand people who flake out on me at the last minute.\n"
         "3 What really gets me is drivers who don’t use their indicator.\n4 My flatmate always leaves the cap off the toothpaste — it drives me up the wall.\n"
         "5 I wish people would respect my personal space on the metro.")
s5 = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">5</b>Write five sentences about <b>your</b> pet peeves. In each sentence, use one collocation from this page and one expression from the lesson '
      '(<i>It gets on my nerves when … · I can’t stand people who … · What really gets me is … · It drives me up the wall when … · I wish people would …</i>).</p>' +
      ta("w5", "1 It really gets on my nerves when people …\n2 …", 170) + '<p class="hint" id="w5c"></p>' +
      '<button class="btn l" onclick="model(\'m5\')" style="margin-top:6px">Show a model answer</button><div class="model" id="m5">%s</div>' % MODEL.replace("\n", "<br>") +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you use these collocations now?"))
XJS = r"""document.head.insertAdjacentHTML("beforeend",`<style>.vbox{margin:10px 0 16px;border:1px solid #eee;border-radius:10px;overflow:hidden}.vbox .vt{padding:8px 12px;background:#fbe7ee;font-size:15px}.vbox .vt a{float:right;color:#9e2d55;font-size:14px}
.vbox .vn{color:#c2416b}.vbox .vd{color:#77787b;font-size:13px;margin-left:6px}.vbox .fr{position:relative;padding-top:56.25%}.vbox iframe{position:absolute;inset:0;width:100%;height:100%;border:0}</style>`);
function wc(){const t=document.querySelector('.g[data-k="w5"]');if(!t)return;const n=(t.value.trim().match(/\S+/g)||[]).length;document.getElementById("w5c").textContent=n+" words"}
document.addEventListener("input",e=>{if(e.target.dataset&&e.target.dataset.k==="w5")wc()});window.afterFill=wc;"""
h = page("😤", "Pet peeves · collocations", "EXTRA HOMEWORK", "Practise the collocations from the video ‘100 People Tell Us Their Pet Peeves’.",
         "GE B2+ Pet peeves: extra homework (collocations)", CODE, [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5)], K, VOCAB,
         acc=ACC, acc2=ACC2, dark=DARK, grad2=GRAD2, footer="Video: Cut (YouTube). ", extra_js=XJS)
h = h.replace('<a href="../../../index.html">← Contents</a>', '<a href="../index.html">← My lessons</a>')
os.makedirs(os.path.dirname(OUT), exist_ok=True); open(OUT, "w").write(h); print("ok extra", len(h))
