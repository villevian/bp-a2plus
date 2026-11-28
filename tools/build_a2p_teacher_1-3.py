# -*- coding: utf-8 -*-
"""Business Partner A2+ — Teacher's Book (Ukrainian) for 1.3 Communication skills: Small talk.
Usage: python3 build_a2p_teacher_1-3.py OUTDIR [LESSON_BASE_URL] -> OUTDIR/1-3.html (and refreshes OUTDIR/index.html)
Same format as 1.2: сенс, як почати (фрази вчителя англійською), як вести, додаткові питання, відповіді.
1.3 is a video lesson: kept as in the coursebook (pp. 12–13), videos 1.3.1–1.3.4 are done at home (Before class).
"""
import sys, os
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
BASE = sys.argv[2] if len(sys.argv) > 2 else "../lessons/1-3/all/"
ACC, ACC2, DARK, GR2 = "#3fa9ad", "#e6f4f4", "#2b8185", "#5cc1c4"
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_b1_teacher.py")).read()
src = src[src.index("def ul("):src.index("TPL = TPL.replace")]
ns = {}; exec(src, ns)
TPL = ns["TPL"].replace("#f2a66e", GR2).replace("ACC2", ACC2).replace("ACC", ACC).replace("DARK", DARK)
ul, blk, step = ns["ul"], ns["blk"], ns["step"]
def pagef(num, title, url, overview, steps):
    nav = '<button data-s="s0" class="on">Огляд</button>' + "".join('<button data-s="%s">%s</button>' % (sid, lab) for sid, lab, _ in steps)
    body = '<section id="s0" class="sec on">%s</section>' % overview + "".join(h for _, _, h in steps)
    return TPL.replace("__NUM__", num).replace("__TITLE__", title).replace("__URL__", url).replace("__NAV__", nav).replace("__BODY__", body)
def dlg(lines): return '<table class="tt">' + "".join("<tr><td><b>%s</b></td><td><i>%s</i></td></tr>" % (w, t) for w, t in lines) + "</table>"
def ifthen(rows): return '<table class="tt"><tr><th>Якщо вона…</th><th>Ти…</th></tr>' + "".join("<tr><td>%s</td><td>%s</td></tr>" % r for r in rows) + "</table>"

UNIT = ('<table class="tt"><tr><th>Урок</th><th>Крок поїздки «конференція в Барселоні + вихідні»</th></tr>'
        '<tr><td>1.1 Business travel</td><td>Їдемо: транспорт, житло; поради колезі, який теж залишається на вихідні</td></tr>'
        '<tr><td>1.2 Events management</td><td>Організатор конференції: порівнюємо площадки для вечірнього заходу</td></tr>'
        '<tr><td><b>1.3 Small talk</b></td><td><b>Знайомимося на конференції та вечірньому заході</b></td></tr>'
        '<tr><td>1.4 Dealing with problems</td><td>Проблеми в поїздці: Wi-Fi в готелі, проєктор, пошта</td></tr>'
        '<tr><td>1.5 Asking for information</td><td>Лист / повідомлення: чи можна продовжити поїздку</td></tr>'
        '<tr><td>Business workshop 1</td><td>Рейс скасовано — змінюємо плани</td></tr></table>')

overview = (
 blk("big", "Сенс уроку", "<p>Студентка вчиться <b>підтримувати small talk за простою моделлю</b> (outcome книги: <i>Learners can make small talk using a simple model</i>). "
     "Головне — модель <b>AAA</b>: <b>Answer</b> (відповісти) → <b>Add</b> (додати інформацію) → <b>Ask</b> (поставити зустрічне питання). Так розмова не обривається на «Yes» / «No».</p>"
     "<p>Це урок x.3 Communication skills: <b>усе як у книзі</b> (с. 12–13), відео з книги не змінюємо. Відео 1.3.1–1.3.4 студентка дивиться вдома (сторінка Before class, вправи 2–5), "
     "тому на уроці 2–5 — лише швидка перевірка, а основний час — мова й говоріння (7–10).</p>"
     "<p><b>Що оновлено:</b> у 10A додано дві ситуації 2026 року (перед початком відеодзвінка, сніданок у готелі в Барселоні); картки з питаннями й домашка — про конференцію в Барселоні (сюжет юніту).</p>") +
 blk("aim", "Сюжет юніту 1 (bleisure, Барселона)", UNIT) +
 blk("aim", "Мовні цілі", ul([
     "Питання для small talk: <i>Where do you…? · What do you think about…? · How long was your…? · What do you know about…? · Do you know…? · Which do you prefer, … or …? · What are you doing…?</i>",
     "Модель AAA: answer · add · ask.",
     "Безпечні й «небезпечні» теми: weather, travel, home town, food — так; personal finances, politics, religion — краще ні.",
     "Вимова: показуємо інтерес інтонацією — голос починає високо й іде вниз: <i>Really? · Oh, that’s interesting! · Lucky you!</i>"])) +
 blk("run", "Таймінг (60 хв)", '<table class="tt"><tr><th>Крок</th><th>Що</th><th>Час</th></tr>'
     '<tr><td>1A–C</td><td>Lead-in: що таке small talk, які теми</td><td>8 хв</td></tr>'
     '<tr><td>2–5</td><td>Перевірка відео (вдома)</td><td>8 хв</td></tr>'
     '<tr><td>6</td><td>Рефлексія: наскільки я добре це вмію</td><td>4 хв</td></tr>'
     '<tr><td>7A–C</td><td>Питання для small talk</td><td>12 хв</td></tr>'
     '<tr><td>8A–C</td><td>AAA у тексті відео</td><td>8 хв</td></tr>'
     '<tr><td>9</td><td>Тренуємо AAA + інтонація</td><td>8 хв</td></tr>'
     '<tr><td>10A–D</td><td>Task: small talk у ситуаціях</td><td>12 хв</td></tr></table>') +
 blk("watch", "Відео", "<p>YouTube, канал English with Daria (відео книги Business Partner A2+): 1.3.1 Jasmine запізнюється на вечерю TGC · 1.3.2 Video A (Orla, Azra, Shaun) · 1.3.3 Video B (Jasmine, Thiago, Azra, Alex) · 1.3.4 Conclusions. "
     "Усі вбудовані в Before class і в урок; субтитри вмикаються автоматично.</p>") +
 blk("tgt", "Перед уроком перевір", ul(["В адмінці — відповіді Лариси на Before class (2–5): що вона зрозуміла, де помилилась. Почни урок з цього.",
     "Якщо Before class не зроблено — відео 1.3.2 і 1.3.3 дивимося на уроці (по 1–2 хв), 1.3.1 і 1.3.4 переказуєш сама."])))

S = []
S.append(("s1", "1A–B", step("s1", "1A–B · Lead-in", "5 хв",
 "<p>Студентка формулює власне ставлення до small talk і згадує ситуації, де він буває. Це «розігрів» теми й мотивація: small talk — не дрібниця, а спосіб будувати стосунки.</p>",
 ["Read the comment. Do you agree? Is small talk really unimportant?", "Where do people make small talk? Let’s make a list together."],
 ul(["1A: хай обере agree / partly agree / disagree і скаже одне речення <i>I (don’t) agree because …</i>",
     "1B: збирайте список разом, ти дописуєш на екрані; підштовхни до робочих ситуацій: conference, coffee break, lift, before a meeting, before a video call.",
     "Акцент: люди роблять small talk, щоб познайомитися, зняти напругу, побудувати довіру перед справами."]),
 ["Do you like small talk? Is it easy for you in English?", "What do you talk about in a lift with a colleague?"],
 "<p>Відкриті відповіді. 1B1 (приклади): at a conference, at a business dinner, in a lift, at the coffee machine, on a plane / train, before a meeting or a video call, at a hotel breakfast. "
 "1B2: to be polite, to get to know people, to avoid silence, to build a relationship before business.</p>")))
S.append(("s2", "1C", step("s2", "1C · Topics", "3 хв",
 "<p>Студентка розставляє теми на шкалі «точно говорила б ↔ точно ні». Готує до поради з відео Conclusions.</p>",
 ["Where would you put the weather? And politics? Why?"],
 ul(["Не виправляй вибір — це думка. Проси пояснення: <i>I’d talk about … because it’s a safe topic. I wouldn’t talk about … with a new client.</i>",
     "Порівняйте з відео: кнопка «What the video says»."]),
 ["Is it OK to talk about family with a new colleague? It depends — why?"],
 "<p>Немає однієї правильної відповіді. За відео: safe — the weather, travel, home town, the place you are in, sports, music; avoid — personal finances, politics, religion, health (дуже особисте).</p>")))
S.append(("s3", "2–5", step("s3", "2–5 · Video (вдома, перевірка)", "8 хв",
 "<p>Вдома студентка подивилась історію Jasmine і вивела модель AAA. На уроці — коротко перевірити розуміння і закріпити AAA, а не дивитися все заново.</p>",
 ["You watched the videos at home. Why was Jasmine late?", "What do you think about Shaun? Is he good at small talk?", "So what is the AAA model?"],
 ul(["Почни з її відповідей з адмінки: похвали, що вийшло, і уточни 1–2 місця, де помилилась.",
     "3B — ключовий момент: Shaun — приклад, <b>як не треба</b> (говорить про себе, не слухає).",
     "5 — запиши на екрані: Answer → Add → Ask. Це опора на весь урок."]),
 ["Who is better at small talk, Shaun or Azra? Why?", "Which tip from the Conclusions video is the most useful for you?"],
 "<p><b>2:</b> 1 She’s a trainee at TGC; she starts on Monday. 2 An HR consultancy — it advises companies on recruitment and strategy. 3 New recruits and TGC staff; a welcome dinner. 4 She’s stuck in traffic.<br>"
 "<b>3A:</b> 1 home town, the place you are in, travel. 2 From Turkey; she lives in Dublin. 3a Friday traffic is terrible, it can take him hours to get home. 3b LA: he was late and missed his presentation; Bangkok: the airline lost his luggage. <b>3B:</b> b.<br>"
 "<b>4A:</b> Jasmine — American, from Boston, went to university there, trip about an hour, met Orla at the interview. Thiago — Brazilian name (father from Brazil) but Italian; never been to Boston, would like to go. "
 "Azra — born in Istanbul, moved to London at five, goes back to see family, loves both cities. Alex — went to Turkey on holiday three years ago. <b>4B:</b> усі питають і відповідають; Jasmine, Azra, Alex додають інформацію; усі показують інтерес.<br>"
 "<b>5:</b> Answer the question, Add new information, Ask another question.</p>")))
S.append(("s4", "6", step("s4", "6 · Reflection", "4 хв",
 "<p>Студентка оцінює себе і ставить маленьку ціль. Це soft skill: усвідомити, що small talk — навичка, яку можна тренувати.</p>",
 ["How good are you at small talk — in Ukrainian and in English?", "What is difficult for you? What can you do to improve?"],
 ul(["Опори на екрані: <i>I’m good at … · I find it difficult to … · To improve, I can …</i>",
     "Запропонуй одну конкретну ціль на поїздку: підготувати 3 безпечні питання."]),
 ["Do you remember people’s names easily?"], "<p>Відкриті відповіді.</p>")))
S.append(("s5", "7A–C", step("s5", "7A–C · Small talk questions", "12 хв",
 "<p>Головна мова уроку — сім форм питань. 7A — розпізнати, 7B — комбінувати, 7C — створити свої.</p>",
 ["Match the questions with the answers. Look at the words in bold — we can use them again and again.", "Listen and repeat the questions."],
 ul(["7A: після перевірки — 🔊 Listen and repeat, звертай увагу на інтонацію питань.",
     "7B: хай складе мінімум 6 питань; правильних варіантів кілька.",
     "7C: тема — конференція / поїздка / її місто. Одразу <b>постав їй 2–3 її ж питання</b> — хай почує, що вони працюють."]),
 ["Which question is the most useful for you at a conference?"],
 "<p><b>7A:</b> 1 g · 2 a · 3 d · 4 b · 5 f · 6 h · 7 c · 8 e<br>"
 "<b>7B (можливі):</b> Where do you live? · What do you think about Angelina’s Pizzeria / the food / the town / the project? · How long was your flight? · What do you know about the company / the project / fashion? · "
 "Do you know David / the town / Angelina’s Pizzeria? · Which do you prefer, Prague or Barcelona? · What are you doing in Boston?<br><b>7C:</b> відкриті.</p>")))
S.append(("s6", "8A–C", step("s6", "8A–C · AAA in the video", "8 хв",
 "<p>Бачимо модель AAA в реальному діалозі, а потім продовжуємо його самі.</p>",
 ["Complete the dialogue. Then find the Answer, the Add and the Ask in Jasmine’s reply."],
 ul(["8B2: хай продовжить за Thiago вголос, а ти відповідаєш як Jasmine — коротка міні-розмова.",
     "8C: якщо часу мало — дай знайти один приклад, другий покажи сама."]),
 ["What else could Jasmine add about Boston?"],
 "<p><b>8A:</b> you from · That’s right · to university · you know it · I’d like to<br>"
 "<b>8B:</b> 1 Yes: answer — <i>That’s right. I’m from Boston.</i> add — <i>I went to university there.</i> ask — <i>Do you know it?</i> 2 Yes, e.g. <i>…but I’d like to. I’ve only been to New York. What’s Boston like in the summer?</i><br>"
 "<b>8C:</b> Azra: <i>I was born in Istanbul</i> (answer), <i>my parents moved to London… we go back quite often</i> (add), <i>Do you know Turkey?</i> (ask). Alex: <i>A little</i> (answer), <i>I went there on holiday…</i> (add), <i>Which do you prefer, London or Istanbul?</i> (ask).</p>")))

# 9 — speaking with the teacher's role
role9 = (blk("tgt", "Твоя роль", "<p>Ти — колега на кавовій перерві конференції в Барселоні. Задача: витягнути з неї повну AAA-відповідь і зустрічне питання. Сама відповідай теж за AAA — ти модель.</p>") +
 blk("tgt", "Приблизний діалог", dlg([
     ("Ти", "So, where do you come from?"),
     ("Вона", "I’m from Ukraine. I live in … Do you know it?"),
     ("Ти", "Not really, but I’d love to go. I’m from Italy, I live near Genoa. What do you think about the conference?"),
     ("Вона", "It’s interesting. I liked the first talk. Which talk did you like?"),
     ("Ти", "The one about AI. Really useful! Are you staying for the weekend?")])) +
 blk("tgt", "Якщо вона… → ти…", ifthen([
     ("відповідає одним словом («Ukraine.»)", "чекай 2 секунди, потім: <i>Oh, nice! Which city?</i> — і покажи на екрані слово <b>Add</b>"),
     ("не ставить зустрічне питання", "мовчки покажи на <b>Ask</b> або спитай: <i>And what about me?</i>"),
     ("каже «Really?» рівним голосом", "повтори з інтонацією (високо → вниз), хай повторить; кнопки Pronunciation bank"),
     ("переходить на погане / негатив («The hotel is terrible»)", "<i>Oh no! What happened?</i> — і після вправи нагадай пораду: don’t be too negative"),
     ("питає про особисте / гроші", "м’яко зміни тему: <i>Hmm… anyway, what do you think about the food here?</i> — потім обговоріть, чому")])))
S.append(("s7", "9", step("s7", "9 · Practise AAA", "8 хв",
 "<p>Контрольована практика: картка з питанням → студентка відповідає за AAA → ставить тобі те саме питання. Плюс інтонація інтересу.</p>",
 ["I ask a question, you answer with AAA: answer, add, ask. Then ask me the same question."],
 ul(["Кнопка «New question» — питання з’являється й озвучується. 5–6 карток.", "Найкращу відповідь хай запише в три поля Answer / Add / Ask.",
     "Pronunciation bank: клік → слухає → повторює з тією ж інтонацією. Потім вставляй ці реакції в розмову."]) + role9,
 [], "<p>Відкриті відповіді. Перевіряй структуру: є answer, є 1+ речення add, є питання ask.</p>")))

role10 = (blk("tgt", "Твоя роль", "<p>Ти — партнер у вибраній ситуації (кнопка «Roll» дає ситуацію + 2 теми). Говоримо 3 хвилини (таймер). Твоя задача — щоб вона вела: ти відповідаєш, додаєш, але інколи «забуваєш» поставити питання, щоб ініціативу брала вона.</p>") +
 blk("tgt", "Приблизний діалог (at the hotel breakfast in Barcelona · food + the weather)", dlg([
     ("Ти", "Good morning! Is this seat free?"),
     ("Вона", "Yes, please. Are you here for the conference?"),
     ("Ти", "Yes, I am. It’s my first time in Barcelona."),
     ("Вона", "Me too! What do you think about the food here?"),
     ("Ти", "The coffee is great, but the croissants… not so much! And the weather is amazing. It’s raining at home."),
     ("Вона", "Lucky you! In Kyiv it’s cold now. Which do you prefer, summer or winter?")])) +
 blk("tgt", "Якщо вона… → ти…", ifthen([
     ("замовкає", "дай підказку-питання з 7A на екрані або: <i>So… what are you doing after the conference?</i>"),
     ("тільки питає, нічого про себе не каже (як інтерв’ю)", "відповідай і спитай: <i>And you?</i> — щоб вона додала про себе"),
     ("говорить лише про себе (як Shaun)", "після 3 хв спитай: <i>What did you learn about me?</i> — і порівняйте з 3B"),
     ("робить граматичні помилки", "не перебивай; записуй і розбери 2–3 після розмови")])))
S.append(("s8", "10", step("s8", "10A–D · Task", "12 хв",
 "<p>Вільна практика: справжній small talk у ділових ситуаціях. Студентка поєднує питання з 7A, модель AAA й інтонацію інтересу.</p>",
 ["Let’s roll: here is our situation and two topics. You start. Three minutes.", "Now a different situation — and this time I start."],
 ul(["10A–B: 1-ша розмова — вона починає; 10C: нова ситуація — починаєш ти.",
     "Ситуації 2026: before a video call starts — розумно для неї (онлайн), hotel breakfast in Barcelona — сюжет юніту.",
     "10D: хай розкаже, що дізналась про тебе (3–4 речення в third person: <i>She is from … She likes …</i>) — перевіряє, чи слухала.",
     "Наприкінці — самооцінка (зірочки) і 2–3 виправлення з твоїх нотаток."]) + role10,
 ["What was the most difficult moment? What will you say next time?"],
 "<p>Відкриті відповіді.</p>")))

S.append(("s9", "HW", step("s9", "Homework · ключі", "",
 "<p>Повторення: питання й відповіді на кавовій перерві в Барселоні, порядок слів у питаннях, вибір Add / Ask, безпечні теми, власний діалог (8–10 реплік, AAA двічі).</p>",
 ["For homework, practise the questions and write a short small talk conversation at the conference dinner."],
 ul(["1–4 перевіряються автоматично. 5 (діалог) прокоментуй в адмінці: чи є AAA двічі, чи є 2 питання з уроку."]), [],
 "<p><b>1:</b> 1 I’m from Lviv… · 2 It’s very nice, and the breakfast is great. · 3 About three hours. · 4 Not much. I think she works for Google. · 5 A little. I was here for a conference two years ago. · 6 The mountains. I love hiking. · 7 Yes, we met at the welcome dinner. · 8 I’m staying for the weekend…<br>"
 "<b>2:</b> 1 Where do you come from? 2 How long was your trip? 3 What do you think about the food? 4 Do you know Madrid? 5 Which do you prefer, trains or planes? 6 What are you doing in Barcelona?<br>"
 "<b>3:</b> Add — 1 I live in Kyiv, but I was born in Odesa. 2 The flight was on time, and the view was amazing. 3 The first talk about AI was great. Ask — 1 Do you know it? 2 How was yours? 3 Which talk did you like?<br>"
 "<b>4:</b> OK — the weather, your trip to the conference, the food at the event, your home town; avoid — your salary, politics, religion, how much your flat cost.</p>")))
S.append(("s10", "Review", step("s10", "Grammar review 1.1–1.3", "",
 "<p>Окрема сторінка повторення: Present Simple чи Present Continuous на матеріалі юніту (поїздка, конференція, small talk: <i>Where do you live? · What are you doing in Barcelona?</i>).</p>",
 ["Why do we say “What are you doing in Barcelona?” but “Where do you live?”"],
 ul(["Можна дати разом із домашкою або як warm-up на 1.4. Закриті завдання перевіряються автоматично."]), [], "")))


# ---------- Твій скрипт + навідні питання (додаються в кожен крок) ----------
def scr(lines): return '<div class="say">' + "".join("<p>%s</p>" % l for l in lines) + "</div>"
def guide(rows): return '<table class="tt"><tr><th>Навідне питання</th><th>Правильна відповідь / куди ведемо</th></tr>' + "".join("<tr><td><i>%s</i></td><td>%s</td></tr>" % r for r in rows) + "</table>"
T = "🗣 "
SG = {
 "s1": ([T + "<i>Today our topic is small talk. Look at this comment: ‘Small talk is an unimportant conversation about unimportant things.’</i>",
         T + "<i>Do you agree? Choose: agree, partly agree or disagree. Why?</i>",
         "(вислухай) " + T + "<i>Interesting! Now — where do people make small talk? Let’s make a list. I’ll start: in a lift.</i>",
         T + "<i>And why do people do it? Why don’t we just say ‘Hello’ and start business?</i>",
         T + "<i>When you meet someone for the first time, what do you usually talk about?</i>"],
        [("Is small talk about important or unimportant things?", "The topics are simple, but the <b>goal</b> is important: to build a relationship / trust."),
         ("Where do you wait with other people at a conference?", "at the coffee break, in the queue, in the lift, before a talk starts"),
         ("What do people do before an online meeting starts?", "they chat: <i>How are you? How’s the weather?</i> → small talk online too"),
         ("Why do we talk about the weather with a new client?", "to be polite, to avoid silence, to feel relaxed before business"),
         ("Is it easier to work with someone you know a little?", "yes → that’s why small talk matters")]),
 "s2": ([T + "<i>Look at these topics. Where would you put them on the line — ‘definitely would’ or ‘definitely wouldn’t’?</i>",
         T + "<i>Let’s start with the weather. And politics?</i>",
         T + "<i>Why? Explain: I’d talk about… because… I wouldn’t talk about… because…</i>",
         T + "<i>Now let’s see what the video says.</i>"],
        [("Can the weather make anyone angry?", "no → it’s a safe topic"),
         ("Can politics or religion start an argument?", "yes → avoid them with people you don’t know well"),
         ("Would you tell a new colleague your salary?", "no → personal finances: avoid"),
         ("Is family OK?", "it depends: ‘Do you have children?’ is OK in many cultures, but don’t ask too much"),
         ("Is ‘the place you are in’ a good topic? Why?", "yes — you both are there: <i>What do you think about this hotel?</i>")]),
 "s3": ([T + "<i>You watched the videos at home — great job! Let’s check quickly.</i>",
         T + "<i>Who is Jasmine? Where is she going? Why is she late?</i>",
         T + "<i>In Video A she talks to Shaun. What do you think about Shaun? Is he good at small talk?</i>",
         T + "<i>And in Video B — what do we learn about Thiago, Azra and Alex?</i>",
         T + "<i>So what is the AAA model? Let’s write it here: Answer — Add — Ask.</i>"],
        [("Does Shaun ask Jasmine about herself?", "almost no → he talks about himself (3B = b)"),
         ("What are Shaun’s stories about?", "traffic, a missed presentation, lost luggage → all negative"),
         ("What does Azra do after she answers?", "she adds information (Istanbul → London) and asks <i>Do you know Turkey?</i>"),
         ("Why does the conversation in Video B go well?", "everyone answers, adds and asks; they smile and listen"),
         ("What happens if you only answer ‘Yes’ or ‘No’?", "the conversation stops → so we Add and Ask")]),
 "s4": ([T + "<i>Now think about yourself. How good are you at small talk — in Ukrainian? And in English?</i>",
         T + "<i>What is difficult for you?</i>",
         T + "<i>What can you do to improve? Let’s choose one goal for your next conference.</i>"],
        [("What do you do when there is a silence?", "відкрита; веди до: <i>ask a question from the list</i>"),
         ("Do you prepare questions before an event?", "ідея: prepare three safe questions"),
         ("Is it easier when you ask or when you answer?", "відкрита; ціль — і питати, і відповідати (AAA)")]),
 "s5": ([T + "<i>Here are eight questions from the video. Match them with the answers.</i>",
         "(після перевірки) " + T + "<i>Look at the words in bold. They are like a template — we can change the end. ‘What do you think about…’ — the hotel? the food? the talk?</i>",
         T + "<i>Listen and repeat the questions.</i>",
         T + "<i>Now 7B: make new questions with the words in the box.</i>",
         T + "<i>7C: write your own questions for a conference in Barcelona. Then ask me!</i>"],
        [("‘How long was your…?’ — what can be long?", "trip, flight, journey, meeting"),
         ("Which question asks for an opinion?", "<i>What do you think about…?</i>"),
         ("Which question gives two options?", "<i>Which do you prefer, … or …?</i>"),
         ("‘Do you know Turkey?’ — can we say ‘Do you know David?’", "yes — a place or a person"),
         ("Answer ‘Not much.’ — which question?", "4 <i>What do you know about working at TGC?</i> (b)"),
         ("Answer ‘About an hour.’ — which question?", "3 <i>How long was your trip?</i> (d)")]),
 "s6": ([T + "<i>Here is a short dialogue from the video. Complete it with the phrases in the box.</i>",
         T + "<i>Now look at Jasmine’s answer. Can you find the Answer? The Add? The Ask?</i>",
         T + "<i>Thiago says ‘No, I’ve never been, but I’d like to.’ Can he continue? You are Thiago — continue!</i>",
         T + "<i>Watch Video B again. Find two more examples of AAA.</i>"],
        [("What is Jasmine’s Answer?", "<i>That’s right. I’m from Boston.</i>"),
         ("What new information does she add?", "<i>I went to university there.</i>"),
         ("What is her question back?", "<i>Do you know it?</i>"),
         ("Does Thiago ask a question?", "no → he can add: <i>I’ve been to New York</i> and ask: <i>What’s Boston like?</i>"),
         ("Who else uses AAA in Video B?", "Azra (Istanbul → London → <i>Do you know Turkey?</i>) and Alex (<i>A little… holiday… Which do you prefer?</i>)")]),
 "s7": ([T + "<i>Let’s practise. I ask, you answer with AAA: answer, add, ask. Ready?</i>",
         "(клік New question) " + T + "<i>Where do you come from?</i>",
         "(після відповіді) " + T + "<i>Great — what was your Add? And your Ask?</i>",
         T + "<i>Now listen: ‘Really?’ — my voice goes high, then down. Repeat. ‘Oh, that’s interesting!’</i>",
         T + "<i>Next question — and use one of these reactions when I answer you.</i>"],
        [("You said ‘I’m from Ukraine.’ What can you add?", "city, how long you live there, something interesting about it"),
         ("Now what can you ask me?", "<i>Do you know it? / And you? / Where are you from?</i>"),
         ("I said ‘I went to Bali last year.’ How do you react?", "<i>Lucky you! How was it?</i>"),
         ("I said ‘My flight was cancelled.’ How do you react?", "<i>Oh no! What happened?</i>"),
         ("Does ‘Really?’ sound interested if your voice is flat?", "no → start high, go down")]),
 "s8": ([T + "<i>Now a real situation. Click ‘Roll’: here is our place and two topics.</i>",
         T + "<i>You start. Three minutes — I’ll start the timer. Remember: AAA and show interest.</i>",
         "(3 хв) " + T + "<i>Great! Now a different situation — this time I start.</i>",
         T + "<i>Tell me: what did you learn about me?</i>",
         T + "<i>Here are two or three things from my notes.</i> (виправлення)"],
        [("How do you start? Nobody knows you.", "a safe question about the place: <i>Is this seat free? / What do you think about…?</i>"),
         ("I gave a short answer. What do you do?", "ask a follow-up question: <i>Really? Which…?</i>"),
         ("We are talking only about you. What’s missing?", "Ask → <i>And you?</i>"),
         ("How do you finish small talk politely?", "<i>It was nice talking to you. See you at the next talk!</i>"),
         ("Was it more like Shaun or like Azra? Why?", "самооцінка: слухала, питала → like Azra")]),
 "s9": ([T + "<i>For homework: questions and answers from a coffee break in Barcelona, and write your own small talk conversation.</i>",
         T + "<i>Use AAA at least twice and two questions from today.</i>"],
        [("In your dialogue, where is your Add?", "після кожної відповіді має бути ще 1 речення інформації"),
         ("Is ‘how much your flat cost’ OK?", "avoid — personal finances")]),
 "s10": ([T + "<i>Look: ‘Where do you live?’ but ‘What are you doing in Barcelona?’ Why different?</i>",
          T + "<i>Which one is always true, and which one is now, for this trip?</i>"],
         [("Do you live in Kyiv only this week?", "no, always → Present Simple: <i>Where do you live?</i>"),
          ("Are you in Barcelona every day of your life?", "no, only now → Present Continuous: <i>What are you doing here?</i>"),
          ("‘I usually take the train’ — which tense? Why?", "Present Simple — a habit (usually)"),
          ("‘I’m staying at the Hotel Arts this week’ — why -ing?", "temporary, this week")]),
}
for i, (sid, lab, h) in enumerate(S):
    if sid in SG:
        lines, rows = SG[sid]
        extra = blk("start", "Твій скрипт (по порядку)", scr(lines)) + blk("tgt", "Навідні питання → правильна відповідь", guide(rows))
        h = h.replace('<div class="blk run">', extra + '<div class="blk run">', 1)
        S[i] = (sid, lab, h)

open(os.path.join(OUT, "1-3.html"), "w").write(pagef("1.3", "Small talk", BASE + "lesson.html", overview, S))
idx = ('<section id="s0" class="sec on"><div class="bsec">Business Partner A2+ · Teacher’s Book</div>' +
       blk("aim", "Unit 1 Travelling for work (bleisure, Barcelona)", ul([
           '<a href="1-2.html">1.2 Events management — Lesson · Homework · Extra</a>',
           '<a href="1-2-speak.html">1.2 Speaking: business situations — твоя роль, приблизний діалог, «якщо вона… → ти…»</a>',
           '<a href="1-3.html">1.3 Small talk — Before class · Lesson · Homework · Grammar review (твоя роль у 9–10)</a>'])) + "</section>")
open(os.path.join(OUT, "index.html"), "w").write(TPL.replace("__NUM__", "A2+").replace("__TITLE__", "Teacher’s Book").replace("__URL__", "../index.html").replace("__NAV__", "").replace("__BODY__", idx))
print("ok", OUT)
