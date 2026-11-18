"""Business Partner A2+ · 1.2 Events management — BEFORE CLASS (flipped classroom).
The student does this at home BEFORE the lesson: meets the words, does all the listening (coursebook 3–5 + Extra A),
notices the grammar (7A–B, 8) and prepares ideas for speaking. Class time = speaking and vocabulary practice.
Instructions on how to work are in Ukrainian; tasks are in English.
Usage: python3 build_a2p_flip_1-2.py OUT.html [STUDENT_CODE]
"""
import sys, os, random
from bp_page import page, fb, sel, inp, ta, ctl, SELF
from vocab_a2p import lesson
import vcard
from tts_dialog_text import A2P_101
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3fa9ad", "#e6f4f4", "#2b8185", "#5cc1c4"
_, GROUPS = lesson("1.2")
VOC, VJS = vcard.build(GROUPS, ACC, ACC2, DARK)
K = {}
random.seed(21)
def shuf(o): o = o[:]; random.shuffle(o); return o
def radio(k, opts):
    return "".join('<label class="opt" style="display:inline;margin:0 10px 0 0"><input type="radio" name="%s" data-k="%s" value="%s"> %s</label>' % (k, k, o, o) for o in opts)
def how(txt): return '<div class="how"><b>🇺🇦 Як працювати</b>%s</div>' % txt
def aud(src, label):
    return '<div class="aud"><span class="an">🔊 %s</span><audio controls preload="none" src="../audio/%s"></audio></div>' % (label, src)
PLAYERS = (aud("1-01.mp3", "1.01 full interview (3 min)") +
           '<div class="sub2">Listen again to one part: </div>' + aud("1-01a.mp3", "Part 1 · Clients, tech &amp; budgets") + aud("1-01b.mp3", "Part 2 · The rooftop party &amp; bleisure"))
SCRIPT = "".join("<p><b>%s:</b> %s</p>" % ({"M": "Marek", "A": "Alicia"}[s], t) for s, t in A2P_101)

# 0 Start
s0 = ('<div class="bsec">Before class</div><p class="ins">This is your homework <b>before</b> lesson 1.2. At home you meet the words and do all the listening. In class we will <b>speak</b> and use the words.</p>' +
      how('<ol><li><b>A · Words (10 хв).</b> Відкрийте словничок уроку вгорі сторінки: натисніть на кожне слово, прочитайте переклад і приклад, послухайте 🔊. Потім виконайте вправи A1–A3.</li>'
          '<li><b>B · Before you listen (3 хв).</b> Подумайте, про що буде інтерв’ю. Це налаштовує мозок на тему, і слухати стає легше.</li>'
          '<li><b>C · Listening 1 — загальне розуміння (5 хв).</b> Слухаємо <b>один раз</b>, без зупинок і без скрипта. Мета — зрозуміти, про що говорять, а не кожне слово.</li>'
          '<li><b>D · Listening 2 — деталі (8 хв).</b> Спочатку прочитайте речення, потім слухайте. Можна ставити на паузу.</li>'
          '<li><b>E · Listening 3 — слова (8 хв).</b> Слухаємо й вставляємо слова. Потім відкриваємо скрипт і робимо shadowing.</li>'
          '<li><b>F · Grammar (8 хв).</b> Знаходимо comparatives і superlatives в реченнях з інтерв’ю.</li>'
          '<li><b>G · Get ready to speak (5 хв).</b> Коротко нотатки — на уроці ми про це говоримо.</li></ol>'
          '<p>Разом ≈ 45 хв. Відповіді зберігаються автоматично, викладач їх бачить. Скрипт відкривайте <b>тільки після</b> C і D.</p>'))

# A Words
DEF = [(it[0], it[2]) for g in GROUPS for it in g[1]]
PICK = ["venue", "guest", "client", "staff", "entertainment", "product launch", "team offsite", "hybrid event", "arrange", "organise"]
DD = [(w, d) for w, d in DEF if w in PICK]
for i, (w, _) in enumerate(DD): K["a1_%d" % (i + 1)] = [w]
s1 = ('<div class="bsec">A · Words</div><p class="ins"><b class="x">A1</b>First open the lesson vocabulary at the top of the page. Then match the words to the meanings.</p>' +
      "".join('<div class="row">%d. %s %s%s</div>' % (i + 1, d, sel("a1_%d" % (i + 1), sorted(PICK), 170), fb("a1_%d" % (i + 1))) for i, (_, d) in enumerate(DD)) + ctl("a1"))

COL = [("", "an event for a new client", "plan"), ("", "a conference in Barcelona", "attend"), ("", "a budget", "manage"),
       ("", "attention to detail", "pay"), ("", "on with people", "get"), ("", "for the weekend after the conference", "stay"),
       ("", "the food, the tables and the chairs", "arrange")]
VERBS = sorted(set(c[2] for c in COL))
for i, (_, _, a) in enumerate(COL): K["a2_%d" % (i + 1)] = [a]
s2 = ('<div class="bsec">A · Words</div><p class="ins"><b class="x">A2</b>Collocations. Which verb goes with the words? You will hear all of them in the interview.</p>' +
      "".join('<div class="row">%d. %s <i>%s</i>%s</div>' % (i + 1, sel("a2_%d" % (i + 1), VERBS, 120), b, fb("a2_%d" % (i + 1))) for i, (_, b, _) in enumerate(COL)) + ctl("a2") +
      how('<p>Вчіть слова <b>разом із сусідами</b>: не «budget», а «manage a budget». Так ви одразу знаєте, як сказати це в реченні.</p>'))

A3 = ["What was the last event you attended? (a conference, a product launch, a team offsite, a party…)", "Was the venue good? Why? / Why not?",
      "How many guests were there? Was there any entertainment?", "Have you ever stayed for the weekend after a work trip? Where?"]
s3 = ('<div class="bsec">A · Words</div><p class="ins"><b class="x">A3</b>Answer about <b>you</b>. Use the words from A1 and A2. Short answers are OK. We will talk about this in class.</p>' +
      "".join('<p class="ins"><span class="q">%d.</span> %s</p>%s' % (i + 1, q, ta("a3_%d" % (i + 1), "", 45)) for i, q in enumerate(A3)))

# B Before you listen (coursebook 3)
CAT = ["The types of events she plans", "Important things to think about", "Important skills for an Events Manager", "What is new in her job in 2026"]
s4 = ('<div class="bsec">B · Before you listen</div><p class="ins"><b class="x">B</b>You are going to listen to a podcast interview with Alicia, an Events Manager in Barcelona. Think of one or two things she will talk about for each category. <span style="color:#6d6e70">(Coursebook 3)</span></p>' +
      "".join('<p class="ins"><span class="q">•</span>%s</p>%s' % (c, ta("b_%d" % (i + 1), "", 40)) for i, c in enumerate(CAT)))

# C Listening 1 — gist (coursebook 4)
TOP = [("hybrid events: people in the room and online", "Yes"), ("weddings — she plans a lot of them", "No"), ("QR-code registration", "Yes"),
       ("a party on a rooftop", "Yes"), ("a sound system for speeches", "No"), ("vegan and gluten-free food", "Yes"),
       ("the price of flights to Barcelona", "No"), ("the weather", "Yes"), ("guests who stay for the weekend", "Yes"), ("how to get a job as an events manager", "No")]
for i, (_, a) in enumerate(TOP): K["c_%d" % (i + 1)] = [a]
s5 = ('<div class="bsec">C · Listening 1</div>' +
      how('<p>Слухайте <b>один раз, повністю, без пауз і без скрипта</b>. Не перекладайте кожне слово — ловіть тему. Не зрозуміли слово? Слухайте далі.</p>'
          '<p>Після прослуховування позначте, про що говорила Alicia, і порівняйте зі своїми ідеями з B.</p>') +
      '<p class="ins"><b class="x">C</b>Listen to the interview. Did Alicia talk about these things? Choose <i>Yes</i> or <i>No</i>. Then compare with your ideas in B. <span style="color:#6d6e70">(Coursebook 4)</span></p>' +
      aud("1-01.mp3", "1.01") +
      "".join('<div class="tf"><span class="q">%d. %s</span>%s%s</div>' % (i + 1, t, radio("c_%d" % (i + 1), ["Yes", "No"]), fb("c_%d" % (i + 1))) for i, (t, _) in enumerate(TOP)) +
      ctl("c", "chkRad") + '<p class="ins" style="margin-top:16px">Which of your ideas from B did you hear? Any other ideas?</p>' + ta("c_ideas", "I heard … / I didn’t hear …", 50))

# D Listening 2 — detail (coursebook 5)
TF5 = [("She helps people plan weddings.", "F", "She doesn’t plan weddings — wedding planners do weddings."), ("Most of her clients are businesses.", "T", ""),
       ("In the first meeting, she never talks about money.", "F", "She talks about the budget at the first meeting."),
       ("Most guests go home right after the conference.", "F", "About half of the guests stay for the weekend."),
       ("She believes getting details right is very important.", "T", ""), ("She says her job is to make clients happy.", "T", "")]
for i, (_, a, _) in enumerate(TF5): K["d_%d" % (i + 1)] = [a]
s6 = ('<div class="bsec">D · Listening 2</div>' +
      how('<ol><li><b>Спочатку прочитайте</b> всі 6 речень і підкресліть у голові ключові слова (<i>weddings, businesses, money, go home, details, happy</i>).</li>'
          '<li>Слухайте ще раз. Коли чуєте ключове слово — <b>пауза</b>, відповідайте.</li>'
          '<li>Пастка: в аудіо часто <b>інші слова з тим самим змістом</b>: <i>money → budget, make clients happy → client satisfaction</i>.</li>'
          '<li>Для False — напишіть правильне речення.</li></ol>') +
      '<p class="ins"><b class="x">D</b>Listen again. Are the sentences true (T) or false (F)? Correct the false sentences. <span style="color:#6d6e70">(Coursebook 5)</span></p>' + PLAYERS +
      "".join('<div class="tf"><span class="q">%d. %s</span>%s%s</div>%s' % (i + 1, q, radio("d_%d" % (i + 1), "TF"), fb("d_%d" % (i + 1)), inp("dc_%d" % (i + 1), 520, "Correct it if it’s false") if a == "F" else "")
              for i, (q, a, c) in enumerate(TF5)) + ctl("d", "chkRad") +
      '<button class="btn l" onclick="model(\'md\')" style="margin-left:8px">Show corrections</button><div class="model" id="md">%s</div>' % "<br>".join("%d %s" % (i + 1, c) for i, (_, a, c) in enumerate(TF5) if c))

# E Listening 3 — words (Extra A) + script + shadowing
BOX = ["arrange", "clients", "guests", "manage", "organised", "plan", "staff", "venue"]
A = [("I help them ", " an event, like a big annual conference, a product launch, or a fun team offsite.", "plan"),
     ("About ninety percent of my corporate ", " are businesses.", "clients"),
     ("How do you ", " a budget?", "manage"),
     ("For a cheap event, we choose the least expensive ", " possible.", "venue"),
     ("We rented a fantastic rooftop and invited about three hundred ", ".", "guests"),
     ("You have to ", " all the food, tables and chairs.", "arrange"),
     ("… coordinate the ", ", and check every single thing.", "staff"),
     ("You have to be ", " and pay attention to detail.", "organised")]
for i, (_, _, a) in enumerate(A): K["e_%d" % (i + 1)] = [a]
s7 = ('<div class="bsec">E · Listening 3</div>' +
      how('<ol><li>Спробуйте <b>спочатку вставити слова з пам’яті</b>, потім слухайте й перевіряйте.</li>'
          '<li>Натисніть Check. Потім відкрийте <b>скрипт</b> і слухайте ще раз, читаючи текст.</li>'
          '<li><b>Shadowing:</b> виберіть 3 речення Alicia. Пауза після речення — повторіть уголос з тією ж інтонацією. 2–3 рази. Це найкраща підготовка до говоріння на уроці.</li></ol>') +
      '<p class="ins"><b class="x">E</b>Complete the sentences from the interview with the words in the box. Then listen and check. <span style="color:#6d6e70">(Extra activities A)</span></p><div class="box">%s</div>' % " · ".join(BOX) + PLAYERS +
      "".join('<div class="row">%d. %s%s%s%s</div>' % (i + 1, a, inp("e_%d" % (i + 1), 130), b, fb("e_%d" % (i + 1))) for i, (a, b, _) in enumerate(A)) + ctl("e") +
      '<button class="btn l" onclick="model(\'sc\')" style="margin-left:8px">Show script</button><div class="model" id="sc">%s</div>' % SCRIPT +
      '<p class="ins" style="margin-top:16px">Shadowing: write the 3 sentences you repeated.</p>' + ta("e_shadow", "1 …\n2 …\n3 …", 70))

# F Grammar (coursebook 7A–B + 8)
S7 = [("Weddings are <b>harder than</b> business lunches.", "comparative"), ("I try to find <b>the best</b> location for each event.", "superlative"),
      ("I can’t choose <b>the most expensive</b> hotel in Barcelona for a client with a small budget.", "superlative"), ("For a cheap event, we choose <b>the least expensive</b> venue possible.", "superlative"),
      ("Prices are <b>higher than</b> they were five years ago.", "comparative"), ("Planning an event outdoors is always <b>the biggest</b> challenge.", "superlative"),
      ("Was it <b>more difficult than</b> your usual events?", "comparative"), ("Are any of the skills more important, or <b>less important</b>?", "comparative")]
for i, (_, a) in enumerate(S7): K["f7_%d" % (i + 1)] = [a]
G7B = [("To form the ", " of most adjectives, we use <i>the</i> before the adjective and <i>-est</i> or <i>most / least</i>.", "superlative"),
       ("To form the ", " of most adjectives, we use <i>-er</i> or <i>more / less</i> and <i>than</i>.", "comparative"),
       ("Some common adjectives are ", ", e.g. <i>good – better than – the best</i>.", "irregular")]
for i, (_, _, a) in enumerate(G7B): K["f7b_%d" % (i + 1)] = [a]
TBL = ('<div class="gbox"><div class="gh">Comparatives and superlatives</div><table class="tb"><tr><th>adjective</th><th>comparative</th><th>superlative</th></tr>'
       '<tr><td>cheap, high</td><td>cheaper than, higher than</td><td>the cheapest, the highest</td></tr><tr><td>big, hot</td><td>bigger than, hotter than</td><td>the biggest, the hottest</td></tr>'
       '<tr><td>easy, busy</td><td>easier than, busier than</td><td>the easiest, the busiest</td></tr><tr><td>expensive, difficult</td><td>more / less expensive than</td><td>the most / the least expensive</td></tr>'
       '<tr><td>good, bad</td><td>better than, worse than</td><td>the best, the worst</td></tr></table></div>')
s8 = ('<div class="bsec">F · Grammar</div>' +
      how('<p>Ці речення ви вже чули в інтерв’ю. Знайдіть, де <b>порівнюємо дві речі</b> (comparative: <i>-er than, more … than</i>), а де <b>найбільше / найменше з усіх</b> (superlative: <i>the -est, the most</i>). Правило B виведіть самі, потім подивіться таблицю.</p>') +
      '<p class="ins"><b class="x">F1</b>Which sentences are comparatives? Which are superlatives? <span style="color:#6d6e70">(Coursebook 7A)</span></p>' +
      "".join('<div class="row">%d. %s %s%s</div>' % (i + 1, s, sel("f7_%d" % (i + 1), ["comparative", "superlative"], 150), fb("f7_%d" % (i + 1))) for i, (s, _) in enumerate(S7)) + ctl("f7") +
      '<p class="ins" style="margin-top:22px"><b class="x">F2</b>Complete the rules with <i>comparative</i>, <i>superlative</i> or <i>irregular</i>. <span style="color:#6d6e70">(Coursebook 7B)</span></p>' +
      "".join('<div class="row">%d. %s%s%s%s</div>' % (i + 1, a, sel("f7b_%d" % (i + 1), ["comparative", "superlative", "irregular"], 150), b, fb("f7b_%d" % (i + 1))) for i, (a, b, _) in enumerate(G7B)) + ctl("f7b") + TBL)

S8 = [("The rooftop dinner is", ["the most", "more"], "expensive option on the list."), ("Organising a team lunch is", ["less difficult", "difficult less"], "than organising a conference."),
      ("Planning a conference for 300 people is", ["harder", "the hardest"], "than planning a meeting for 20."), ("Some reviews say this is", ["the worst", "worse"], "hotel near the conference centre."),
      ("A boat trip is", ["more", "the most"], "fun than a bus tour."), ("Managing an online event is", ["easier than", "the easiest"], "managing a hybrid event."),
      ("", ["The best", "Better"], "option is the hotel next to the conference centre."), ("", ["The least", "Less"], "popular day for a team event is Monday.")]
for i, (_, o, _) in enumerate(S8): K["f8_%d" % (i + 1)] = [o[0]]
s9 = ('<div class="bsec">F · Grammar</div><p class="ins"><b class="x">F3</b>Choose the correct option to complete the sentences. <span style="color:#6d6e70">(Coursebook 8)</span></p>' +
      "".join('<div class="row">%d. %s %s %s%s</div>' % (i + 1, a, sel("f8_%d" % (i + 1), shuf(o), 150), b, fb("f8_%d" % (i + 1))) for i, (a, o, b) in enumerate(S8)) + ctl("f8"))

# G Get ready to speak
G = ["Would you enjoy being an Events Manager? Why? / Why not? (Coursebook 6)", "Which skill do you think is the most important: organised, pay attention to detail or get on with people? Why?",
     "Think of two venues for events in your town. Which one is better? Why?"]
s10 = ('<div class="bsec wr">G · Get ready to speak</div>' +
       how('<p>Не пишіть довгих текстів — тільки <b>ключові слова й короткі фрази</b>. На уроці ви будете говорити, а не читати.</p>') +
       '<p class="ins"><b class="x">G</b>Make notes. We will talk about these questions in class.</p>' +
       "".join('<p class="ins"><span class="q">%d.</span> %s</p>%s' % (i + 1, q, ta("g_%d" % (i + 1), "", 50)) for i, q in enumerate(G)) +
       '<div style="margin-top:20px">%s</div>' % (SELF % "How well did you understand the interview?"))

XJS = VJS + r"""
document.head.insertAdjacentHTML("beforeend",`<style>.aud{display:flex;flex-wrap:wrap;gap:10px;align-items:center;background:#e6f4f4;padding:8px 12px;border-radius:6px;margin:8px 0}.aud .an{font-weight:600;color:#2b8185}.aud audio{height:36px}
.sub2{font-size:14px;color:#6d6e70;margin-top:6px}
.how{background:#fff8e6;border-left:4px solid #f2b631;border-radius:6px;padding:10px 16px;margin:10px 0 16px;font-size:15px}.how>b{display:block;margin-bottom:4px;color:#9a6b00}.how ol{margin:4px 0;padding-left:20px}.how li{margin:3px 0}.how p{margin:4px 0}
table.tb{border-collapse:collapse;width:100%;margin:10px 0;font-size:15px}table.tb th,table.tb td{border:1px solid #c8c9cb;padding:6px 10px;vertical-align:top;text-align:left}table.tb th{background:#f3f4f6;font-weight:600}</style>`);"""
secs = [("Start", s0), ("A1", s1), ("A2", s2), ("A3", s3), ("B", s4), ("C", s5), ("D", s6), ("E", s7), ("F1–2", s8), ("F3", s9), ("G", s10)]
h = page("1.2", "Events management", "BEFORE CLASS", "At home: meet the words, listen to the interview, notice comparatives and superlatives, prepare to speak.",
         "BP A2+ 1.2 Events management · Before class", CODE, secs, K, VOC, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2,
         footer="Flipped classroom: do this before the lesson. Audio 1.01: AI voices. ", extra_js=XJS)
os.makedirs(os.path.dirname(OUT), exist_ok=True); open(OUT, "w").write(h); print("ok before-class", len(h))
