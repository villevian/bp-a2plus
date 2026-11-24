# -*- coding: utf-8 -*-
import re
src = open("/home/claude/bp-a2/teacher/7-2.html").read()
head = src[:src.index("<body")]
head = re.sub(r"<title>.*?</title>", "<title>1.3 A survey — Teacher’s Book</title>", head)

def blk(cls, h, body): return f'<div class="blk {cls}"><h3>{h}</h3>{body}</div>'
def say(*lines): return '<div class="say">' + "".join(f"<p>🗣 <i>{l}</i></p>" for l in lines) + "</div>"
def ul(*xs): return "<ul>" + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"
def step(title, time, aim, start, run, extra, answers=None, watch=None):
    h = f'<div class="bsec">{title}<span class="time">{time}</span></div>' + blk("aim", "Мета", f"<p>{aim}</p>") + blk("start", "Як почати", start) + blk("run", "Як вести", run)
    if extra: h += blk("tgt", "Додаткові питання", extra)
    if watch: h += blk("watch", "На що звернути увагу", watch)
    if answers: h += blk("ans", "Відповіді", f"<p>{answers}</p>")
    return h

S = []
S.append(("Огляд",
  blk("big", "Сенс уроку",
      "<p>Студент учиться <b>ставити й відповідати на питання для опитування про своє робоче місце</b> (outcome книги: <i>Learners can ask and answer questions for a survey about their workplace</i>). "
      "Усі вправи книги збережені (1A–5B). Контекст — IT-компанія з гібридним форматом: опитування в Google Forms від People &amp; Culture, open space, другий монітор, Zoom-зустрічі, тиха кімната.</p>"
      "<p><b>Куди ведемо студента:</b> назвати, що є в офісі (1) → прочитати справжнє опитування (2) → побачити, як будуються питання (граматика, 3–4) → написати власне опитування для команди (5) → вільно питати й відповідати (6, додано).</p>"
      "<p><b>Що додано на прохання:</b> повторення слів 1.1–1.2 всередині питань (6A) і більше говоріння: 🗣-блоки в 1A, 1B, 2C, 3, 4B, 6A та картки-питання 6B. Розділи книги не змінені.</p>"
      "<p><b>Місце в юніті 1 Working day:</b> 1.1 мої завдання (Present Simple) → 1.2 плануємо зустріч → <b>1.3 питаємо колег про роботу й офіс</b> → 1.4 говоримо про людей і ролі → 1.5 знайомимося з командою.</p>"),
  blk("aim", "Мовні цілі", ul("Питання: <i>What are…? Where is…? How do you…? When does…? How often do you…? Does your office have…?</i>",
      "Короткі відповіді: <i>Yes, I do. / No, I don’t. Yes, it does. / No, it doesn’t.</i>",
      "Словник: <i>a meeting room, a car park, an area for relaxing, a kitchen area, a workspace, a quiet room, the company gym, facilities, working hours, work from home, spend time at your desk, take a break</i>.",
      "Повторення 1.1–1.2: <i>go to meetings, send out the agenda, book a meeting room, get an update, create a brief, analyse data, calculate costs, available</i>.")),
  blk("run", "Тайминг (60 хв)", '<table class="tt"><tr><th>Крок</th><th>Що</th><th>Час</th></tr>'
      '<tr><td>1A–B</td><td>Lead-in: що є в офісі, як часто користуєшся</td><td>7 хв</td></tr>'
      '<tr><td>2A–C</td><td>Читання опитування + відповіді + питаємо одна одну</td><td>15 хв</td></tr>'
      '<tr><td>3, 4A–B</td><td>Граматика: питання</td><td>15 хв</td></tr>'
      '<tr><td>5A–B</td><td>Пишемо своє опитування (можна вдома) + обмін</td><td>10 хв</td></tr>'
      '<tr><td>6A–B</td><td>Повторення 1.1–1.2 + картки для говоріння</td><td>13 хв</td></tr></table>'),
  blk("watch", "Для студентки рівня A1 (Марина)", ul("Більшість відповідей — з вибору (select), письмо коротке. Не давай готових відповідей у 2C, 5A, 6B: нехай каже своє, навіть з помилками.",
      "Головна помилка буде <b>«Where you work?» / «Your office has a gym?»</b> — без do / does. Виправляй жестом «де допоміжне?» і проси повторити.",
      "Друга типова: <b>«Does you…»</b>. Нагадай: you → do; your office / he / she → does."))))

S.append(("1A", step("1A Lead-in", "3 хв", "Активувати слова про офіс і зв’язати тему з її реальною роботою.",
  say("Let’s talk about your office. Do you have a kitchen area?", "What’s your favourite place in the office?"),
  ul("Студентка обирає Yes / No під кожною карткою.", "Потім каже 2–3 речення за зразком у 🗣-блоці.", "Якщо вона працює з дому — нехай говорить про офіс компанії або про коворкінг."),
  ul("<i>Is there a phone booth for calls?</i>", "<i>Do you work in an open space?</i>", "<i>What facility do you want in your office?</i>"),
  None, "<p>Слово <b>facilities</b> пояснюй через картки: «all these places = facilities».</p>")))
S.append(("1B", step("1B Lead-in", "4 хв", "Повторити прислівники частоти з 1.1 (always, usually, never) у новому контексті.",
  say("Which ones do you use? How often?", "I usually have lunch in the kitchen area. And you?"),
  ul("Обирає частоту для кожного місця.", "Говорить вголос за зразком, потім питає тебе: <i>Do you use…? How often?</i>", "Записує 2 речення в поле."),
  ul("<i>How often do you work from home?</i>", "<i>Do you use the car park? Why not?</i>"),
  None, "<p>Порядок слів: <i>I <b>usually</b> have…</i> (прислівник перед дієсловом) — це тема 1.1, перевір.</p>")))
S.append(("2A", step("2A Reading", "5 хв", "Зрозуміти структуру опитування (4 розділи) й побачити багато питань одразу.",
  say("This is an employee survey from People & Culture. What is it about?", "Read the questions. Which heading goes with A?"),
  ul("Спочатку лише заголовки: студентка читає питання розділу й обирає heading.", "Не пояснюй кожне слово — досить зрозуміти тему розділу.", "Натисни Check."),
  ul("<i>Does your company send surveys like this?</i>", "<i>Do you like Google Forms?</i>"),
  "A The work day · B The workplace · C Meetings and meeting rooms · D Other facilities")))
S.append(("2B", step("2B Reading", "4 хв", "Побачити зв’язок «питання → коротка відповідь».",
  say("Look at answer a: Development. Which question is it?"),
  ul("Опитування можна відкрити кнопкою «Show the survey».", "Студентка обирає номер питання для кожної відповіді.", "Після Check прочитайте пари «питання – відповідь» вголос по ролях."),
  None, "a 4 · b 2 · c 10 · d 11 · e 3 · f 12")))
S.append(("2C", step("2C Speaking", "6 хв", "Перше вільне використання питань: відповідати про себе й питати вчителя.",
  say("Now it’s your survey. Question 1: How do you get to work?", "Now you ask me."),
  ul("Студентка коротко пише свої відповіді (можна 1–3 слова).", "Ти ставиш їй питання 1–12, вона відповідає вголос повним реченням.", "Міняєтесь: вона питає тебе, записує одну цікаву річ про тебе."),
  ul("Після кожної її відповіді — одне уточнення: <i>Why? / Do you like it? / Every day?</i>"),
  None, "<p>Її питання до тебе: якщо пропускає do / does — не перебивай, повтори правильно (recast): <i>«Do I use the gym? Yes, I do.»</i></p>")))
S.append(("3", step("3 Communicative grammar", "6 хв", "Зрозуміти порядок слів у питаннях.",
  say("Look at the box. What comes first? What comes next?"),
  ul("Розберіть табличку: зліва — питання з question word, справа — Yes/No питання.", "Покажи схему з 🇺🇦-підказки: <b>(Where / What / How often) + do / does + you / your office + verb</b>; для <b>be</b>: <b>What + are + your hours</b>.",
     "Студентка натискає слова по черзі; ↺ — почати знову.", "Після Check — 🗣: вона ставить тобі питання 1–8."),
  None, "1 What are your working hours? · 2 Does your office have enough meeting rooms? · 3 Does your office have a quiet room? · 4 Do you use the gym? · 5 Where is the kitchen? · 6 What time do you start work? · 7 When does your day finish? · 8 Does your company have a car park?",
  "<p>Інтонація: Yes/No питання — голос вгору ↗, питання з question word — вниз ↘ (Pronunciation bank книги).</p>")))
S.append(("4A", step("4A Communicative grammar", "4 хв", "Обрати правильне допоміжне слово.",
  say("Is it ‘is’, ‘are’, ‘do’ or ‘does’? Why?"),
  ul("Після кожної відповіді питай «чому?»: <i>the gym → is; the office → does; you → do; hours → are</i>."),
  None, "1 is · 2 Does · 3 do · 4 are · 5 is · 6 Do · 7 Does · 8 How")))
S.append(("4B", step("4B Communicative grammar", "5 хв", "Короткі відповіді й перенос на своє життя.",
  say("Question 1: Where is the gym? Which answer?", "Now about your office: Where is the gym?"),
  ul("Студентка зіставляє відповіді.", "🗣: ти ставиш питання 1–8 про ЇЇ офіс, вона відповідає, потім навпаки."),
  ul("<i>Yes, it does / No, it doesn’t</i> — вимагай короткої відповіді, а не просто «Yes»."),
  "a 3 · b 6 · c 1 · d 4 · e 2 · f 5 · g 8 · h 7")))
S.append(("5A", step("5A Writing", "7 хв або вдома", "Створити власне опитування з 8 питань.",
  say("You want to make your office better. What do you want to ask your team?"),
  ul("Студентка обирає 4–5 ідей зі списку.", "Підказки в полях: <i>Do you…? Does your office have…? How often…?</i>", "Перевір кожне питання на do / does, перш ніж іти далі."),
  None, None, "<p>Не пиши за неї питання. Якщо застрягла — дай тему («Zoom meetings?»), а питання вона формує сама.</p>")))
S.append(("5B", step("5B Writing / Speaking", "5 хв", "Використати своє опитування в реальній розмові.",
  say("Ask me your survey questions. I answer.", "Now I ask you my questions."),
  ul("Вона питає тебе вголос, записує твої відповіді коротко.", "Ти питаєш її 4–5 своїх питань (див. нижче), вона пише відповіді."),
  "<p>Твої питання: <i>How many meetings do you have a week? · Do you have a quiet place for calls? · What time do you usually take a break? · How often do you go to the office? · What do you want to change in your office?</i></p>")))
S.append(("6A", step("6A Review 1.1–1.2 (додано)", "5 хв", "Повторити словник 1.1–1.2 всередині нової граматики.",
  say("Do you remember ‘send out the agenda’? Who sends out the agenda in your team?"),
  ul("Студентка обирає слово.", "Звертай увагу на ‑s після Who: <i>Who sends / creates / calculates</i>.", "🗣: ставить питання тобі, потім відповідає сама."),
  None, "1 go · 2 sends · 3 book · 4 get · 5 creates · 6 analyse · 7 calculates · 8 available")))
S.append(("6B", step("6B Speaking cards (додано)", "8 хв", "Вільне говоріння: швидко відповідати на питання про роботу й офіс.",
  say("Click ‘Next card’. Answer in 2–3 sentences. Then ask me."),
  ul("Картка озвучується; студентка відповідає 2–3 реченнями.", "Ти відповідаєш на те саме питання — так вона чує модель.", "Записуй собі 3–4 помилки, розберіть наприкінці (не під час)."),
  ul("Ускладнення: після відповіді вона ставить тобі ще одне власне питання на ту саму тему."),
  None, "<p>Закінчити self-assessment і кнопкою Send to my teacher.</p>")))
S.append(("HW", '<div class="bsec">Homework (easy)</div>' + blk("aim", "Що в домашці", ul("A — 7 слів (укр → англ)", "B — do / does / is / are / how", "C — порядок слів у питаннях (плитки)", "D — читання: відповіді Ольги на опитування", "E — відповіді про себе повними реченнями (без готових зразків)")) +
  blk("ans", "Відповіді", "<p>A: 1 a meeting room · 2 a car park · 3 a kitchen area · 4 a workspace · 5 take a break · 6 working hours · 7 work from home<br>"
      "B: 1 Do · 2 is · 3 Does · 4 are · 5 How · 6 does<br>C: 1 Do you use the gym? · 2 Where is the kitchen? · 3 What time do you start work? · 4 Does your office have a car park? · 5 How often do you work from home?<br>"
      "D: a 3 · b 5 · c 1 · d 4 · e 2<br>E: відповіді студентки — перевір повні речення й do / does у її питаннях до тебе.</p>")))

S.append(("Extra", '<div class="bsec">Extra: Present Simple vs Continuous</div>' + blk("aim", "Мета", "<p>Розуміння <b>сенсу</b>: Simple = зазвичай (звичка, факт), Continuous = зараз / цього тижня. Спочатку сенс (A, D), потім маркери (B) і форма (C, E), наприкінці — своє мовлення (F).</p>") +
  blk("start", "Як почати", say("What do you usually do in the morning? — And what are you doing right now?")) +
  blk("run", "Як вести", ul("A: після кожної пари питай «usually чи now? як ти зрозуміла?» — шукаємо ‑ing і am / is / are.", "C: статуси Slack = що відбувається зараз; «usually / every morning / on Mondays» = Simple.", "D: лист Макса — звичайний тиждень vs цей тиждень (тимчасово → Continuous).", "F: її власні речення; після цього вона питає тебе <i>What are you doing today?</i>")) +
  blk("ans", "Відповіді", "<p>A: 1 usually · 2 now · 3 now · 4 usually · 5 usually · 6 now · 7 now · 8 usually<br>B: Simple — every day, usually, on Mondays, never, always; Continuous — now, at the moment, right now, this week, Look!<br>C: 1 starts · 2 is having · 3 checks · 4 is fixing · 5 are working · 6 work · 7 is talking · 8 have<br>D: 1 F · 2 T · 3 T · 4 F · 5 F · 6 T<br>E: 1 She knows the answer. · 2 I agree with you. · 3 He is working now. · 4 Do you work on Fridays? · 5 Look! It’s raining. · 6 She doesn’t like meetings.</p>")))
S = [(t[0], "".join(t[1:])) for t in S]
nav = "<nav>" + "".join(f'<button data-s="s{i}"{" class=\"on\"" if i == 0 else ""}>{t}</button>' for i, (t, _) in enumerate(S)) + "</nav>"
main = "<main>" + "".join(f'<section id="s{i}" class="sec{" on" if i == 0 else ""}">{b}</section>' for i, (_, b) in enumerate(S)) + "</main>"
body = ('<body>\n<header><div class="n">1.3</div><h1>A survey</h1><div class="t">TEACHER’S BOOK</div></header>\n'
        '<div class="top"><a href="index.html">← Teacher’s Book: зміст</a><a href="../lessons/1-3/all/lesson.html" target="_blank">📄 Відкрити урок студента</a><a href="../lessons/1-3/all/hw.html" target="_blank">📝 Домашка</a><a href="../lessons/1-3/all/extra.html" target="_blank">➕ Extra</a></div>\n'
        + nav + main + '<footer>Valentyna Hordiienko · Middle Learning Architect</footer>\n'
        '<script>document.querySelectorAll("nav button").forEach(b=>b.onclick=()=>{document.querySelectorAll("nav button,.sec").forEach(x=>x.classList.remove("on"));b.classList.add("on");document.getElementById(b.dataset.s).classList.add("on");scrollTo(0,0)});</script></body></html>')
open("/home/claude/bp-a2/teacher/1-3.html", "w").write(head + body)

ix = open("/home/claude/bp-a2/teacher/index.html").read()
if "1-3.html" not in ix:
    m = re.search(r'<li><a href="7-2.html">', ix)
    ix = ix[:m.start()] + '<li><a href="1-3.html">1.3 A survey — IT employee survey (Google Form), questions + review 1.1–1.2 + speaking cards</a> · Lesson · Homework · Extra</li>' + ix[m.start():]
    open("/home/claude/bp-a2/teacher/index.html", "w").write(ix)
print("ok")
