"""Business Partner A2+ · 1.2 Events management — BEFORE CLASS (flipped classroom).
The student does this at home BEFORE the lesson: meets the words, does all the listening (coursebook 3–5 + Extra A),
notices the grammar (7A–B, 8) and prepares ideas for speaking. Class time = speaking and vocabulary practice.
Instructions on how to work are in Ukrainian; tasks are in English.
Usage: python3 build_a2p_flip_1-2.py OUT.html [STUDENT_CODE]
"""
import sys, os, random, json
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

# A Words — five different task types: sort → pairs → odd one out → in context → about you
def hid(k): return '<input type="hidden" class="g" data-k="%s">' % k
SORT = [("Events", ["conference", "product launch", "team offsite", "hybrid event"]),
        ("People", ["client", "guest", "staff", "events manager"]),
        ("Places", ["venue", "rooftop", "winery", "hotel"]),
        ("Things you do", ["arrange", "organise", "attend", "manage"])]
SW = [w for _, ws in SORT for w in ws]; SG = {w: g for g, ws in SORT for w in ws}
s1 = ('<div class="bsec">A · Words</div>' +
      how('<p><b>Крок 1.</b> Відкрийте словничок уроку вгорі: натисніть на кожне слово, прочитайте переклад і приклад, послухайте 🔊.</p>'
          '<p><b>Крок 2.</b> Розкладіть слова по групах: натисніть на слово, потім на групу. Помилились — натисніть на слово в групі, воно повернеться.</p>') +
      '<p class="ins"><b class="x">A1</b>Sort the words into four groups.</p>'
      '<div class="pool" id="pool">%s</div><div class="bins">%s</div>' % (
          "".join('<span class="chip" data-w="%s">%s</span>' % (w, w) for w in shuf(SW)),
          "".join('<div class="bin" data-g="%s"><b>%s</b><div class="in"></div></div>' % (g, g) for g, _ in SORT)) +
      "".join(hid("srt_%d" % i) for i in range(len(SW))) +
      '<div class="ctl"><button class="btn" onclick="sortChk()">Check</button><span class="res" id="r_srt"></span></div>')

AGREE = [("After a work trip, it’s a good idea to <b>stay for the weekend</b>.", "stay"),
         ("It’s easy to <b>manage a budget</b> for a big party.", "manage"),
         ("An events manager must <b>pay attention to detail</b>: small things are very important.", "pay"),
         ("A party is better if you <b>invite three hundred guests</b>, not thirty.", "invite"),
         ("It’s more fun to <b>attend a conference</b> in another city than in your home town.", "attend"),
         ("For an events manager, it’s more important to <b>get on with people</b> than to be organised.", "get on"),
         ("I’d like to <b>plan an event</b> for three hundred people.", "plan"),
         ("At a team party, the boss should <b>arrange the food and the tables</b>, not the team.", "arrange")]
sAG = ('<div class="bsec">A · Words</div>' +
       how('<p>Прочитайте твердження. Ви згодні? Натисніть 👍 або 👎. Правильних відповідей тут немає, це ваша думка. Якщо хочете, допишіть коротко чому.</p>'
           '<p>Зверніть увагу на <b>виділені фрази</b>. Це колокації: слова, які завжди ходять разом. Запам’ятайте їх, у наступному завданні треба буде скласти ці пари <b>з пам’яті</b>.</p>') +
       '<p class="ins"><b class="x">A2</b>Do you agree? Click 👍 or 👎. Look at the phrases in <b>bold</b>.</p>' +
       "".join('<div class="agr" data-i="%d"><span class="q">%d.</span> <span class="st">%s</span><span class="th"><button data-v="up">👍</button><button data-v="down">👎</button></span>%s%s</div>' % (
           i, i + 1, t, hid("ag_%d" % i), inp("agw_%d" % i, 360, "Why? (optional)")) for i, (t, _) in enumerate(AGREE)))
PAIRS = [("plan", "an event"), ("attend", "a conference"), ("manage", "a budget"), ("pay", "attention to detail"),
         ("get on", "with people"), ("stay", "for the weekend"), ("arrange", "the food and the tables"), ("invite", "three hundred guests")]
s2 = ('<div class="bsec">A · Words</div>' +
      how('<p>Тепер <b>з пам’яті</b>: не повертайтесь до A2. Натисніть дієслово зліва, потім його пару справа. Правильна пара стане зеленою. Усі ці пари ви почуєте в подкасті.</p>') +
      '<p class="ins"><b class="x">A3</b>From memory: make the pairs from A2. Click a verb, then the words that go with it.</p>'
      '<div class="pairs"><div class="pl">%s</div><div class="pr">%s</div></div>' % (
          "".join('<button class="pb" data-i="%d" data-s="L">%s</button>' % (i, a) for i, (a, _) in shuf(list(enumerate(PAIRS)))),
          "".join('<button class="pb" data-i="%d" data-s="R">%s</button>' % (i, b) for i, (_, b) in shuf(list(enumerate(PAIRS))))) +
      hid("prs") + '<p class="res" id="r_prs" style="margin-top:10px"></p>')

ODD = [(["guest", "venue", "client", "staff"], "venue", "The others are people. A venue is a place."),
       (["budget", "conference", "product launch", "team offsite"], "budget", "The others are events."),
       (["plan", "organise", "attend", "arrange"], "attend", "You arrange, organise and plan an event. You attend it as a guest."),
       (["a DJ", "tables and chairs", "live music", "a jazz band"], "tables and chairs", "The others are entertainment."),
       (["a winery", "a boat restaurant", "a rooftop", "a guest"], "a guest", "The others are venues."),
       (["expensive", "organised", "gets on with people", "pays attention to detail"], "expensive", "The others are skills of an events manager.")]
s3 = ('<div class="bsec">A · Words</div>' +
      how('<p>Яке слово «зайве»? Натисніть на нього — одразу побачите, чи правильно, і пояснення.</p>') +
      '<p class="ins"><b class="x">A4</b>Odd one out. Which word is different?</p>' +
      "".join('<div class="odd" data-i="%d" data-a="%s" data-e="%s"><span class="q">%d.</span> %s<div class="oe"></div></div>%s' % (
          i, a, e, i + 1, "".join('<button class="ob">%s</button>' % w for w in ws), hid("odd_%d" % i)) for i, (ws, a, e) in enumerate(ODD)))

CTX = [("Hi Larysa! Quick update about Barcelona 🇪🇸 We’re going to ", ["attend", "manage"], " a big tech conference there on 12–13 March."),
       ("It’s a ", ["hybrid event", "product launch"], ": 400 people in the room and 2,000 online."),
       ("The ", ["venue", "guest"], " is a new hotel near the beach. Our ", ["client", "staff"], " from Madrid is coming too!"),
       ("Alicia, the events manager, is ", ["organising", "attending"], " everything. She ", ["pays attention to detail", "gets on with people"], " — nothing goes wrong with her 😄"),
       ("On Thursday evening there’s a party on a rooftop with great ", ["entertainment", "staff"], ": a DJ and a jazz band."),
       ("The company pays for two nights, but I want to ", ["stay for the weekend", "plan an event"], ". Shall I ", ["arrange", "attend"], " a room for you for Saturday too?")]
CK = []
for _, o, *rest in CTX:
    CK.append(o[0])
    if len(rest) > 1: CK.append(rest[1][0])
def ctxline(parts, n0):
    out, n = "", n0
    for x in parts:
        if isinstance(x, list):
            out += '<span class="tg" data-n="%d">%s</span>' % (n, "".join('<button>%s</button>' % w for w in shuf(x))); n += 1
        else: out += x
    return out, n
CH, n = "", 0
for line in CTX:
    t, n = ctxline(line, n); CH += "<p>%s</p>" % t
s4 = ('<div class="bsec">A · Words</div>' +
      how('<p>Тепер ті самі слова в реальному повідомленні. Прочитайте повідомлення колеги в Slack і натисніть правильне слово в кожній парі. Потім — Check.</p>') +
      '<p class="ins"><b class="x">A5</b>Read the message from your colleague Marta. Choose the correct words.</p>'
      '<div class="slack"><div class="sh"><span class="av">M</span><b>Marta Vidal</b> <span>10:42</span></div>%s</div>' % CH +
      "".join(hid("ctx_%d" % i) for i in range(len(CK))) +
      '<div class="ctl"><button class="btn" onclick="ctxChk()">Check</button><span class="res" id="r_ctx"></span></div>')

A3Q = ["What was the last event you attended? (a conference, a product launch, a team offsite, a party…)", "Was the venue good? Why? / Why not?",
       "How many guests were there? Was there any entertainment?", "Have you ever stayed for the weekend after a work trip? Where?"]
s5 = ('<div class="bsec">A · Words</div>' +
      how('<p>Тепер про <b>вас</b>. Коротко, 1–2 речення. На уроці розмова почнеться саме з цих питань.</p>') +
      '<p class="ins"><b class="x">A6</b>Answer about you. Use the new words.</p>' +
      "".join('<p class="ins"><span class="q">%d.</span> %s</p>%s' % (i + 1, q, ta("a3_%d" % (i + 1), "", 45)) for i, q in enumerate(A3Q)))
WJS = "const SW=%s,SG=%s,PN=%d,CK=%s;" % (json.dumps(SW), json.dumps(SG), len(PAIRS), json.dumps(CK))

# B Before you listen (coursebook 3)
CAT = ["The types of events she plans", "Important things to think about", "Important skills for an Events Manager", "What is new in her job in 2026"]
sB = ('<div class="bsec">B · Before you listen</div><p class="ins"><b class="x">B</b>You are going to listen to a podcast interview with Alicia, an Events Manager in Barcelona. Think of one or two things she will talk about for each category. <span style="color:#6d6e70">(Coursebook 3)</span></p>' +
      "".join('<p class="ins"><span class="q">•</span>%s</p>%s' % (c, ta("b_%d" % (i + 1), "", 40)) for i, c in enumerate(CAT)))

# C Listening 1 — gist (coursebook 4)
TOP = [("hybrid events: people in the room and online", "Yes"), ("weddings — she plans a lot of them", "No"), ("QR-code registration", "Yes"),
       ("a party on a rooftop", "Yes"), ("a sound system for speeches", "No"), ("vegan and gluten-free food", "Yes"),
       ("the price of flights to Barcelona", "No"), ("the weather", "Yes"), ("guests who stay for the weekend", "Yes"), ("how to get a job as an events manager", "No")]
for i, (_, a) in enumerate(TOP): K["c_%d" % (i + 1)] = [a]
sC = ('<div class="bsec">C · Listening 1</div>' +
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
.agr{display:flex;flex-wrap:wrap;align-items:center;gap:6px 10px;padding:9px 0;border-bottom:1px solid #eee}.agr .st{flex:1 1 380px}.agr .st b{color:#2b8185}.agr .th button{font-size:18px;padding:2px 10px;margin-left:4px;border:1.5px solid #c8c9cb;border-radius:16px;background:#fff;cursor:pointer;filter:grayscale(1);opacity:.7}.agr .th button.on{filter:none;opacity:1;border-color:#3fa9ad;background:#e6f4f4}.agr input{flex-basis:100%}
.pool{display:flex;flex-wrap:wrap;gap:8px;min-height:44px;padding:10px;border:1.5px dashed #c8c9cb;border-radius:8px;margin:8px 0 12px}
.chip{background:#fff;border:1.5px solid #3fa9ad;color:#2b8185;border-radius:18px;padding:5px 13px;cursor:pointer;font-size:15px;user-select:none}.chip.sel{background:#3fa9ad;color:#fff}.chip.ok{border-color:#2e9b57;background:#e7f6ec;color:#1e7a43}.chip.no{border-color:#d9534f;background:#fdecec;color:#b52b27}
.bins{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}@media(max-width:700px){.bins{grid-template-columns:1fr}}.bin{border:1.5px solid #c8c9cb;border-radius:8px;padding:8px;min-height:120px;cursor:pointer;background:#fafbfb}.bin:hover{border-color:#3fa9ad}.bin b{display:block;color:#2b8185;margin-bottom:6px}.bin .in{display:flex;flex-wrap:wrap;gap:6px}
.pairs{display:grid;grid-template-columns:1fr 1.6fr;gap:10px 24px;max-width:640px}.pl,.pr{display:flex;flex-direction:column;gap:8px}.pb{font:inherit;font-size:15px;text-align:left;padding:7px 12px;border:1.5px solid #c8c9cb;border-radius:8px;background:#fff;cursor:pointer}.pb.sel{border-color:#3fa9ad;background:#e6f4f4}.pb.done{border-color:#2e9b57;background:#e7f6ec;color:#1e7a43;cursor:default}.pb.bad{border-color:#d9534f;background:#fdecec}
.odd{padding:8px 0;border-bottom:1px solid #eee}.ob{font:inherit;font-size:15px;margin:3px 6px 3px 0;padding:5px 12px;border:1.5px solid #c8c9cb;border-radius:18px;background:#fff;cursor:pointer}.ob.ok{border-color:#2e9b57;background:#e7f6ec}.ob.no{border-color:#d9534f;background:#fdecec}.oe{font-size:14px;color:#2b8185;margin-top:4px;min-height:1px}
.slack{border:1px solid #ddd;border-radius:10px;padding:12px 16px;background:#fff;max-width:720px;line-height:2}.slack .sh{display:flex;align-items:center;gap:8px;margin-bottom:4px}.slack .sh span:last-child{color:#888;font-size:13px}.slack .av{width:30px;height:30px;border-radius:6px;background:#e8894a;color:#fff;display:inline-flex;align-items:center;justify-content:center;font-weight:600}.slack p{margin:2px 0}
.tg{display:inline-flex;gap:4px;margin:0 3px}.tg button{font:inherit;font-size:14px;padding:1px 9px;border:1.5px solid #c8c9cb;border-radius:14px;background:#f7f8f8;cursor:pointer}.tg button.on{border-color:#3fa9ad;background:#e6f4f4;font-weight:600}.tg.ok button.on{border-color:#2e9b57;background:#e7f6ec}.tg.no button.on{border-color:#d9534f;background:#fdecec}
table.tb{border-collapse:collapse;width:100%;margin:10px 0;font-size:15px}table.tb th,table.tb td{border:1px solid #c8c9cb;padding:6px 10px;vertical-align:top;text-align:left}table.tb th{background:#f3f4f6;font-weight:600}</style>`);""" + WJS + r"""
const $q=(s,r=document)=>r.querySelector(s),$a=(s,r=document)=>[...r.querySelectorAll(s)];
function hv(k){const e=$q(`.g[data-k="${k}"]`);return e?e.value:""}
function setH(k,v){const e=$q(`.g[data-k="${k}"]`);if(e){e.value=v;e.dispatchEvent(new Event("input",{bubbles:true}))}}
/* A1 sort */
let csel=null;
function chipTo(c,g){c.classList.remove("sel","ok","no");if(g){$q(`.bin[data-g="${g}"] .in`).appendChild(c)}else $q("#pool").appendChild(c)}
document.addEventListener("click",e=>{const c=e.target.closest(".chip");if(c){e.stopPropagation();const w=c.dataset.w;
  if(c.closest(".bin")&&csel&&csel!==c){const g=c.closest(".bin").dataset.g;chipTo(csel,g);setH("srt_"+SW.indexOf(csel.dataset.w),g);csel=null;return}
  if(c.closest(".bin")){chipTo(c,null);setH("srt_"+SW.indexOf(w),"");return}
  $a(".chip.sel").forEach(x=>x!==c&&x.classList.remove("sel"));c.classList.toggle("sel");csel=c.classList.contains("sel")?c:null;return}
 const b=e.target.closest(".bin");if(b&&csel){const w=csel.dataset.w;chipTo(csel,b.dataset.g);setH("srt_"+SW.indexOf(w),b.dataset.g);csel=null}},true);
function sortChk(){let n=0,left=$a("#pool .chip").length;$a(".bin .chip").forEach(c=>{const ok=SG[c.dataset.w]===c.closest(".bin").dataset.g;c.classList.add(ok?"ok":"no");if(ok)n++});
 $q("#r_srt").textContent=n+" / "+SW.length+(left?" · "+left+" words are not sorted yet":n===SW.length?" ✓ Well done!":" · Red words are in the wrong group")}
/* A2 agree */
document.addEventListener("click",e=>{const b=e.target.closest(".agr .th button");if(!b)return;const r=b.closest(".agr");$a(".th button",r).forEach(x=>x.classList.toggle("on",x===b));setH("ag_"+r.dataset.i,b.dataset.v)});
/* A2 pairs */
let psel=null,pdone=new Set();
function prSave(){setH("prs",[...pdone].join(","));$q("#r_prs").textContent=pdone.size+" / "+PN+(pdone.size===PN?" ✓ Well done!":"")}
function prMark(i){pdone.add(+i);$a(`.pb[data-i="${i}"]`).forEach(b=>{b.classList.remove("sel");b.classList.add("done")})}
document.addEventListener("click",e=>{const b=e.target.closest(".pb");if(!b||b.classList.contains("done"))return;
 if(b.dataset.s==="L"){$a(".pb.sel").forEach(x=>x.classList.remove("sel"));b.classList.add("sel");psel=b;return}
 if(!psel){$q("#r_prs").textContent="First click a verb on the left.";return}
 if(psel.dataset.i===b.dataset.i){prMark(b.dataset.i);psel=null;prSave()}else{b.classList.add("bad");setTimeout(()=>b.classList.remove("bad"),600)}});
/* A3 odd one out */
function oddShow(row,w){$a(".ob",row).forEach(x=>{x.classList.remove("ok","no");if(x.textContent===w)x.classList.add(w===row.dataset.a?"ok":"no")});
 $q(".oe",row).textContent=w===row.dataset.a?"✓ "+row.dataset.e:"Not quite — try again."}
document.addEventListener("click",e=>{const b=e.target.closest(".ob");if(!b)return;const r=b.closest(".odd");oddShow(r,b.textContent);setH("odd_"+r.dataset.i,b.textContent)});
/* A4 context */
document.addEventListener("click",e=>{const b=e.target.closest(".tg button");if(!b)return;const g=b.parentNode;$a("button",g).forEach(x=>x.classList.remove("on"));b.classList.add("on");g.classList.remove("ok","no");setH("ctx_"+g.dataset.n,b.textContent)});
function ctxChk(){let n=0,t=0;$a(".tg").forEach(g=>{const v=hv("ctx_"+g.dataset.n);if(!v)return;t++;const ok=v===CK[+g.dataset.n];if(ok)n++;g.classList.add(ok?"ok":"no")});
 $q("#r_ctx").textContent=n+" / "+CK.length+(n===CK.length?" ✓ Well done!":t<CK.length?" · choose all the words":"")}
/* restore saved answers */
function wRestore(){SW.forEach((w,i)=>{const g=hv("srt_"+i),c=$q(`.chip[data-w="${w}"]`);if(c)chipTo(c,g||null)});
 (hv("prs")||"").split(",").filter(Boolean).forEach(prMark);pdone.size&&($q("#r_prs").textContent=pdone.size+" / "+PN);
 $a(".agr").forEach(r=>{const v=hv("ag_"+r.dataset.i);$a(".th button",r).forEach(x=>x.classList.toggle("on",x.dataset.v===v))});
 $a(".odd").forEach(r=>{const v=hv("odd_"+r.dataset.i);if(v)oddShow(r,v)});
 $a(".tg").forEach(g=>{const v=hv("ctx_"+g.dataset.n);$a("button",g).forEach(x=>x.classList.toggle("on",x.textContent===v))})}
window.afterFill=wRestore;
"""
secs = [("Start", s0), ("A1", s1), ("A2", sAG), ("A3", s2), ("A4", s3), ("A5", s4), ("A6", s5), ("B", sB), ("C", sC), ("D", s6), ("E", s7), ("F1–2", s8), ("F3", s9), ("G", s10)]
h = page("1.2", "Events management", "BEFORE CLASS", "At home: meet the words, listen to the interview, notice comparatives and superlatives, prepare to speak.",
         "BP A2+ 1.2 Events management · Before class", CODE, secs, K, VOC, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2,
         footer="Flipped classroom: do this before the lesson. Audio 1.01: AI voices. ", extra_js=XJS)
os.makedirs(os.path.dirname(OUT), exist_ok=True); open(OUT, "w").write(h); print("ok before-class", len(h))
