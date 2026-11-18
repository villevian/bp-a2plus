"""Business Partner A2+ · 1.2 Events management — LESSON (standard business English, updated 2026; unit story: bleisure, Barcelona).
Mirrors coursebook pp. 10–11: Lead-in 1, 2A–B · Listening 3–6 (audio 1.01, updated script, AI voices) · Grammar 7A–B, 8, 9 · Speaking and writing 10A–B, 11 · Pronunciation bank: the letter r.
Usage: python3 build_a2p_1-2.py LESSON_DIR [STUDENT_CODE]   e.g. ../lessons/1-2   -> LESSON_DIR/all/lesson.html (audio in LESSON_DIR/audio)
"""
import sys, os, random
from bp_page import page, fb, sel, inp, ta, ctl, SELF
from vocab_a2p import lesson
import vcard
from tts_dialog_text import A2P_101
ROOT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3fa9ad", "#e6f4f4", "#2b8185", "#5cc1c4"
_, GROUPS = lesson("1.2")
VOC, VJS = vcard.build(GROUPS, ACC, ACC2, DARK)
K = {}
random.seed(12)
def shuf(o): o = o[:]; random.shuffle(o); return o
def radio(k, opts):
    return "".join('<label class="opt" style="display:inline;margin:0 10px 0 0"><input type="radio" name="%s" data-k="%s" value="%s"> %s</label>' % (k, k, o, o) for o in opts)

# 1 Lead-in
LQ = ["What was the last event you attended? Was it a conference, a product launch, a team offsite or a party?", "Who organised it? Did they pay attention to detail?",
      "What was the venue like? Was it better or worse than other venues you know?", "How many guests were there? Did you get on with the other guests?",
      "Was there any entertainment? What was the best part?", "Have you ever attended a hybrid event? Do you prefer online or in the room? Why?",
      "Who arranges events in your company? Is there a budget for team events?", "Have you ever stayed for the weekend after a work trip? Where? What did you do?"]
EV = ["a conference", "a product launch", "a team offsite", "a hybrid event (in the room + online)", "a networking evening", "a company anniversary party", "a farewell party for a colleague", "a wedding"]
s1 = ('<div class="bsec">Lead-in</div><p class="ins"><b class="x">1</b>Work in pairs. Which of these events have you been to? Which was the best? Why?</p>'
      '<div class="chips">%s</div>' % "".join("<span>%s</span>" % e for e in EV) + ta("l1", "I went to a … in … It was …", 70) +
      '<div class="card"><b>Talk about it.</b> Use the words from the lesson vocabulary.<ol style="margin:6px 0 0;padding-left:22px">%s</ol></div>' % "".join("<li>%s</li>" % q for q in LQ) +
      '<p class="ins" style="margin-top:22px"><b class="x">2</b><b>A</b> Which of the skills and personal qualities below are useful for planning events? Why?</p>'
      '<p>You need to be: organised / able to cook food for a lot of people / good at telling jokes / able to pay attention to details / good with budgets / good with online tools / calm when plans change at the last minute</p>' +
      ta("l2a", "I think you need to be … because …", 60) +
      '<p class="ins"><b>B</b> Would you enjoy planning a big event, for example a two-day conference in Barcelona for 300 people? Why? / Why not?</p>' + ta("l2b", "Yes / No, because I’m (not) good at …", 50))

def player(i):
    sc = "".join("<p><b>%s:</b> %s</p>" % ({"M": "Marek", "A": "Alicia"}[s], t) for s, t in A2P_101)
    return ('<div class="aud"><span class="an">🔊 1.01</span><audio controls preload="none" src="../audio/1-01.mp3"></audio>'
            '<select class="g rate" onchange="document.querySelectorAll(\'audio\').forEach(a=>a.playbackRate=+this.value)"><option value="0.85">slower</option><option value="1" selected>normal</option></select>'
            '<button class="btn l" onclick="model(\'sc%d\')">Show script</button><div class="model" id="sc%d">%s</div></div>') % (i, i, sc)

# 3–4 Listening
CAT = ["The types of events she plans", "Important things to think about", "Important skills for an Events Manager", "What is new in her job in 2026"]
s2 = ('<div class="bsec">Listening</div>' + '<div class="card">🏠 You did this listening at home (Before class). In class: quick check — tell the teacher your answers and what you remember.</div>' + '<p class="ins"><b class="x">3</b>You are going to listen to an interview with Alicia, an Events Manager in Barcelona, on a podcast. Think of one or two things she will talk about for each category.</p>' +
      "".join('<p class="ins"><span class="q">•</span>%s</p>%s' % (c, ta("p3_%d" % (i + 1), "", 40)) for i, c in enumerate(CAT)) +
      '<p class="ins" style="margin-top:22px"><b class="x">4</b>Listen to the interview. Did Alicia talk about any of your ideas from Exercise 3? Did you hear any other ideas?</p>' + player(1) +
      '<button class="btn l" onclick="model(\'m4\')">Show answers</button><div class="model" id="m4">'
      '<b>Types of events:</b> events for companies (not weddings): conferences, product launches, team offsites, hybrid events, a company anniversary party<br>'
      '<b>Important things:</b> the budget, the location / venue, entertainment (a DJ), food (vegan, gluten-free), food, tables and chairs, staff, the weather (outdoor events)<br>'
      '<b>Skills:</b> get on with people, be organised, pay attention to detail; the top priority is client satisfaction<br>'
      '<b>New in 2026:</b> hybrid events, QR-code registration, an AI tool for the schedule, streaming the talks live, higher prices, guests stay for the weekend (bleisure)</div>')

TF5 = [("She helps people plan weddings.", "F", "She doesn’t plan weddings — wedding planners do those."), ("Most of her clients are businesses.", "T", ""),
       ("In the first meeting, she never talks about money.", "F", "She always talks about the budget at the first meeting."),
       ("Most guests go home right after the conference.", "F", "About half of the guests stay for the weekend."),
       ("She believes getting details right is very important.", "T", ""), ("She says her job is to make clients happy.", "T", "")]
for i, (_, a, _) in enumerate(TF5): K["t5_%d" % (i + 1)] = [a]
s3 = ('<div class="bsec">Listening</div><p class="ins"><b class="x">5</b>Listen again and decide if these sentences are <i>true</i> (T) or <i>false</i> (F). Correct the incorrect sentences.</p>' + player(2) +
      "".join('<div class="tf"><span class="q">%d. %s</span>%s%s</div>%s' % (i + 1, q, radio("t5_%d" % (i + 1), "TF"), fb("t5_%d" % (i + 1)), inp("c5_%d" % (i + 1), 520, "Correct it if it’s false") if a == "F" else "")
              for i, (q, a, c) in enumerate(TF5)) + ctl("t5", "chkRad") +
      '<button class="btn l" onclick="model(\'m5\')" style="margin-left:8px">Show corrections</button><div class="model" id="m5">%s</div>' % "<br>".join("%d %s" % (i + 1, c) for i, (_, a, c) in enumerate(TF5) if c) +
      '<p class="ins" style="margin-top:22px"><b class="x">6</b>Would you enjoy being an Events Manager? Why? / Why not?</p>' + ta("l6", "I would / wouldn’t enjoy it because …", 50))

# 7 Grammar
S7 = [("Weddings are <b>harder than</b> business lunches.", "comparative"), ("I try to find <b>the best</b> location for each event.", "superlative"),
      ("I can’t choose <b>the most expensive</b> hotel in Barcelona for a client with a small budget.", "superlative"), ("For a cheap event, we choose <b>the least expensive</b> venue possible.", "superlative"),
      ("Prices are <b>higher than</b> they were five years ago.", "comparative"), ("Planning an event outdoors is always <b>the biggest</b> challenge.", "superlative"),
      ("Was it <b>more difficult than</b> your usual events?", "comparative"), ("Are any of the skills more important — or <b>less important</b>?", "comparative")]
for i, (_, a) in enumerate(S7): K["g7_%d" % (i + 1)] = [a]
G7B = [("To form the ", " of most adjectives, we use <i>the</i> before the adjective and <i>-est</i> or <i>most / least</i>.", "superlative"),
       ("To form the ", " of most adjectives, we use <i>-er</i> or <i>more / less</i> and <i>than</i>.", "comparative"),
       ("Some common adjectives are ", ", e.g. <i>good – better than – the best</i>.", "irregular")]
for i, (_, _, a) in enumerate(G7B): K["g7b_%d" % (i + 1)] = [a]
s4 = ('<div class="bsec">Grammar <span class="sub">Comparatives and superlatives</span></div><p class="ins"><b class="x">7</b><b>A</b> Look at the sentences from the interview. Which sentences are comparatives? Which are superlatives?</p>' +
      "".join('<div class="row">%d. %s %s%s</div>' % (i + 1, s, sel("g7_%d" % (i + 1), ["comparative", "superlative"], 150), fb("g7_%d" % (i + 1))) for i, (s, _) in enumerate(S7)) + ctl("g7") +
      '<p class="ins" style="margin-top:22px"><b>B</b> Complete the sentences with <i>comparative</i>, <i>superlative</i> or <i>irregular</i>.</p>' +
      "".join('<div class="row">%d. %s%s%s%s</div>' % (i + 1, a, sel("g7b_%d" % (i + 1), ["comparative", "superlative", "irregular"], 150), b, fb("g7b_%d" % (i + 1))) for i, (a, b, _) in enumerate(G7B)) + ctl("g7b") +
      '<div class="gbox"><div class="gh">Comparatives and superlatives</div><table class="tb"><tr><th>adjective</th><th>comparative</th><th>superlative</th></tr>'
      '<tr><td>cheap, high</td><td>cheaper than, higher than</td><td>the cheapest, the highest</td></tr><tr><td>big, hot</td><td>bigger than, hotter than</td><td>the biggest, the hottest</td></tr>'
      '<tr><td>easy, busy</td><td>easier than, busier than</td><td>the easiest, the busiest</td></tr><tr><td>expensive, difficult</td><td>more / less expensive than</td><td>the most / the least expensive</td></tr>'
      '<tr><td>good, bad</td><td>better than, worse than</td><td>the best, the worst</td></tr></table></div>')

S8 = [("The rooftop dinner is", ["the most", "more"], "expensive option on the list."), ("Organising a team lunch is", ["less difficult", "difficult less"], "than organising a conference."),
      ("Planning a conference for 300 people is", ["harder", "the hardest"], "than planning a meeting for 20."), ("Some reviews say this is", ["the worst", "worse"], "hotel near the conference centre."),
      ("A boat trip is", ["more", "the most"], "fun than a bus tour."), ("Managing an online event is", ["easier than", "the easiest"], "managing a hybrid event."),
      ("", ["The best", "Better"], "option is the hotel next to the conference centre."), ("", ["The least", "Less"], "popular day for a team event is Monday.")]
for i, (_, o, _) in enumerate(S8): K["g8_%d" % (i + 1)] = [o[0]]
s5 = ('<div class="bsec">Grammar</div><p class="ins"><b class="x">8</b>Choose the correct option to complete the sentences.</p>' +
      "".join('<div class="row">%d. %s %s %s%s</div>' % (i + 1, a, sel("g8_%d" % (i + 1), shuf(o), 150), b, fb("g8_%d" % (i + 1))) for i, (a, o, b) in enumerate(S8)) + ctl("g8"))

S9 = [("The Mar Bella Hotel has ", " (big) conference room in the city.", ["the biggest"]), ("Today’s weather is ", " (bad) yesterday’s weather — take an umbrella!", ["worse than"]),
      ("Is a video call ", " (easy) a face-to-face meeting for you?", ["easier than"]), ("We don’t have much money, so we want to choose ", " (expensive) option.", ["the least expensive"]),
      ("We need to choose ", " (cheap) hotel, because our budget is small.", ["the cheapest"]), ("For a small team, a dinner in the old town is ", " (good) an office party.", ["better than"]),
      ("With 40 seats, the Blue Room is ", " (small) the Main Hall, which has 200 seats.", ["smaller than"]), ("I think Friday is ", " (good) day for our team dinner.", ["the best"])]
for i, (_, _, a) in enumerate(S9): K["g9_%d" % (i + 1)] = a
s6 = ('<div class="bsec">Grammar</div><p class="ins"><b class="x">9</b>Complete the sentences with the comparative or superlative form of the word in brackets. Use <i>the</i> and <i>than</i> where necessary.</p>' +
      "".join('<div class="row">%d. %s%s%s%s</div>' % (i + 1, a, inp("g9_%d" % (i + 1), 170), b, fb("g9_%d" % (i + 1))) for i, (a, b, _) in enumerate(S9)) + ctl("g9"))

VEN = [("Rooftop terrace", "in the city centre", ["food (€€): tapas", "entertainment: DJ", "up to 120 guests", "staff: 8"]),
       ("Winery", "40 minutes by bus", ["food (€€€): Catalan menu + vegan options", "entertainment: live guitar, wine tasting", "up to 80 guests", "staff: 10"]),
       ("Boat restaurant", "in the old port", ["food (€€€€): seafood or vegetable paella", "entertainment: jazz band", "up to 200 guests", "staff: 18"])]
TAB = '<table class="tb"><tr>%s</tr><tr>%s</tr></table>' % ("".join("<th>%s <span style='font-weight:300'>(%s)</span></th>" % (n, w) for n, w, _ in VEN), "".join("<td><ul style='margin:0;padding-left:18px'>%s</ul></td>" % "".join("<li>%s</li>" % x for x in l) for _, _, l in VEN))
s7 = ('<div class="bsec wr">Speaking and writing</div><p class="ins"><b class="x">10</b><b>A</b> Work in pairs. You are planning the evening event of a conference in Barcelona. Look at the information about the venues. Make sentences comparing them.</p>' + TAB +
      '<div class="card"><i>The rooftop is cheaper than the boat restaurant.<br>The winery is the smallest.<br>The boat restaurant is probably more formal than the other venues.</i></div>' + ta("s10a", "The … is … than … / The … is the …", 90) +
      '<button class="btn l" onclick="model(\'m10\')">Show possible answers</button><div class="model" id="m10">The boat restaurant is the most expensive. The rooftop is the least expensive. The boat restaurant is the biggest. The rooftop is bigger than the winery. The boat restaurant has the most staff. The winery is further from the city than the rooftop. The rooftop is probably the most fun for young guests.</div>'
      '<p class="ins" style="margin-top:20px"><b>B</b> Which venue would be the best choice for a conference with 150 guests? And for your team of 20? Why?</p>' + ta("s10b", "For 150 guests, the best choice is … because …", 60))
PR = ["A hotel for fifty people is cheaper than a hotel for five hundred.", "The better option is a rooftop near the park.", "Some people think this is the worst hotel in town.", "Our venue is bigger than the restaurant."]
s8 = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">11</b>Think of three possible event venues in your town (or in Barcelona), or imagine them. Write three comparative and three superlative sentences about them.</p>' +
      ta("w11", "1 … is bigger than …\n2 …\n3 …\n4 … is the most …\n5 …\n6 …", 170) + '<p class="hint" id="w11c"></p>'
      '<div class="gbox"><div class="gh">Pronunciation bank: the letter <i>r</i></div><p>In British English, we pronounce <i>r</i> before a vowel (<i>restaurant, price</i>), but not at the end of a word or before a consonant (<i>cheaper, park, worst</i>). In American English, we always pronounce <i>r</i>. Listen and compare. Then repeat the British version.</p>' +
      "".join('<div class="row">%d. %s<br><button class="btn l" style="padding:2px 10px" onclick="new Audio(\'../audio/pr_uk%d.mp3\').play()">🔊 UK</button> <button class="btn l" style="padding:2px 10px" onclick="new Audio(\'../audio/pr_us%d.mp3\').play()">🔊 US</button></div>' % (i + 1, s, i + 1, i + 1) for i, s in enumerate(PR)) +
      '</div><div style="margin-top:20px">%s</div>' % (SELF % "I can make simple comparisons. How well can you do this now?"))

XJS = VJS + r"""
document.head.insertAdjacentHTML("beforeend",`<style>.aud{display:flex;flex-wrap:wrap;gap:10px;align-items:center;background:#e6f4f4;padding:8px 12px;border-radius:6px;margin:8px 0}.aud .an{font-weight:600;color:#2b8185}.aud audio{height:36px}.aud .model{flex-basis:100%}
table.tb{border-collapse:collapse;width:100%;margin:10px 0;font-size:15px}table.tb th,table.tb td{border:1px solid #c8c9cb;padding:6px 10px;vertical-align:top;text-align:left}table.tb th{background:#f3f4f6;font-weight:600}</style>`);
function wc(){const t=document.querySelector('.g[data-k="w11"]');if(!t)return;const n=(t.value.trim().match(/\S+/g)||[]).length;document.getElementById("w11c").textContent=n+" words"}
document.addEventListener("input",e=>{if(e.target.dataset&&e.target.dataset.k==="w11")wc()});window.afterFill=wc;"""
secs = [("1–2", s1), ("3–4", s2), ("5–6", s3), ("7", s4), ("8", s5), ("9", s6), ("10", s7), ("11", s8)]
h = page("1.2", "Events management", "LESSON", "Learners can make simple comparisons.", "BP A2+ 1.2 Events management · Lesson", CODE, secs, K, VOC,
         acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, footer="Audio 1.01: updated interview (2026), AI voices. ", extra_js=XJS)
d = os.path.join(ROOT, "all"); os.makedirs(d, exist_ok=True); open(os.path.join(d, "lesson.html"), "w").write(h); print("ok lesson", len(h))
