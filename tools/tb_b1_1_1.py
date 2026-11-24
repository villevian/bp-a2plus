"""Teacher's Book B1 · 1.1 Transferable skills (UA). Imported by build_b1_teacher.py: O11, S11 = build(blk, ul, say, step)."""

def build(blk, ul, say, step):
    O = ('<div class="bsec">Огляд уроку</div>' +
     blk("big", "Сенс уроку — яку ідею розкриваємо",
      "<p><b>Навички, які переживуть ШІ.</b> Коли перший варіант коду пише ШІ, роботодавець дивиться вже не на те, який фреймворк ти знаєш, "
      "а на <b>transferable skills</b>: критичне мислення, вирішення проблем, командну роботу, комунікацію, чесність. Інструмент, який вивчив сьогодні, завтра може стати <i>old news</i>, а ці навички студент забирає з собою з роботи в роботу.</p>"
      "<p><b>Логіка юніту (Career choices):</b> 1.1 — що я вмію і як це назвати → 1.2 — як показати це іншим (поради, профіль) → 1.3 — перша зустріч, раппорт → 1.4 — нетворкінг → 1.5 — письмове представлення → Workshop — усе разом у ситуації найму.</p>"
      "<p><b>Навіщо це студенту:</b> він ІТ-фахівець і хоче працювати в міжнародній компанії. Технічну лексику він знає; йому потрібна мова, щоб <b>говорити про себе як про професіонала</b> — на співбесіді, в LinkedIn, у рекомендаціях. "
      "Soft skill уроку — самоаналіз: які мої навички переносяться і чим я цінний поза поточною роллю.</p>") +
     blk("aim", "Результат уроку", ul([
      "Студент називає 8 ключових transferable skills і пояснює їх на прикладах з ІТ (упр. 6).",
      "Утворює іменник ↔ прикметник: flexible → flexibility, confident → confidence… (упр. 7).",
      "Пише job description для remote-вакансії міжнародної компанії (упр. 10).",
      "Домашнє завдання: блок <i>About</i> для свого LinkedIn — show, don’t tell."])) +
     blk("run", "Як урок змінено порівняно з книгою", ul([
      "Структура 1–10 і нумерація збережені повністю.",
      "Відео 1.1.1 (2018) замінено статтею <i>The skills that survive AI</i> (2026) з тими ж навичками і тими ж трьома порадами — питання 3–4 працюють так само. Кнопка 🔊 читає статтю голосом браузера.",
      "Ситуації a–h в упр. 6 переписано під ІТ; ключ той самий, що в книзі: 1d 2b 3a 4c 5f 6g 7e 8h.",
      "Професії в упр. 9 — ІТ-ролі замість personal trainer / factory worker.",
      "Урок 1:1, тому <i>Work in pairs</i> = студент + ви."])) +
     blk("start", "Перевернутий клас: що студент робить ДО уроку (сторінка Before class)", ul([
      "<b>Відео</b> <i>Use Transferable Skills For a Career In IT</i> (University of Phoenix, 2025, 3:16, YouTube): порядок п’яти навичок, що каже спікерка про кожну, T/F про поради в кінці.",
      "<b>Лексика з відео</b> (Before class 2): значення (stakeholder, roll out, internal team, gap, cover letter…), колокації з дієсловами (manage a project, meet the needs, explain technical ideas…), словотвір (manage → management → manager), 4 речення про себе. На уроці почніть з 2D: попросіть прочитати його речення і поставте 2–3 follow-up питання.",
      "<b>Стаття</b> (≈450 слів, B1 з елементами B1+: double-check, justify, stay employable) <i>The skills that survive AI</i> + питання 4A (кнопки Show answer) + які навички є і у відео, і в статті.",
      "<b>Підготовка до говоріння:</b> три свої навички з реальним прикладом, навичка, яку хоче розвинути, 3–5 нових слів.",
      "На уроці 3–4 — лише швидка перевірка (3–4 хв): <i>What did you find? Which skills are in both?</i> Основний час — 1–2, 5–10: говоріння, лексика, проєкт.",
      "Відповіді студента зі сторінки Before class видно в адмінці — перегляньте перед уроком і візьміть його приклади як старт для упр. 5."])) +
     blk("tgt", "Цільова лексика", "<p>transferable skills · think outside the box · a can-do attitude · set goals · critical thinking · determination · team player · integrity · communication skills · problem-solving · "
      "adaptable/adaptability · flexible/flexibility · motivated/motivation · confident/confidence · dependable/dependability · resourceful/resourcefulness · independent/independence · ambitious/ambition · passionate/passion · enthusiastic/enthusiasm · honest/honesty · authentic/authenticity · "
      "+ 2026: AI literacy · async communication · ownership</p><p>Студент може натиснути будь-яке слово в блоці Vocabulary (переклад, приклад, 🔊) і виділити будь-який текст → «＋» → слово в його особистому словнику.</p>"))
    S = [
     ("s1", "1", step("s1", "1 Lead-in", "3 хв",
       "<p>Розігрів і персоналізація: студент одразу говорить про себе. Слова в рамці — база для всього уроку.</p>",
       ["What are you good at? Let’s start with you. Tick three words that describe you best.", "I’ll go first: I’m organised and good with people… but I’m not always calm!"],
       ul(["Студент ставить три галочки — сторінка не дасть поставити більше.", "Попросіть пояснити один вибір: <i>Why ‘resourceful’? Give me an example.</i>", "Нові слова (resourceful, reliable) поясніть через ІТ-приклад."]),
       ["Which word would your team lead use to describe you?", "Which word would you like to have in three years?"], "", "Не виправляйте граматику на цьому етапі — мета розговорити.")),
     ("s2", "2", step("s2", "2 Lead-in", "4 хв",
       "<p>Перехід від «що я вмію» до «що важливо в ІТ». Готуємо думку для статті.</p>",
       ["Is there anything in the box that definitely doesn’t describe you?", "Which is the most important skill for someone in tech? And the least important?"],
       ul(["Попросіть аргумент: <i>Why? Can you give me an example from your job?</i>", "Запишіть 2–3 його ідеї — повернетесь до них у 3B."]),
       ["Has AI changed which skills are important in your team?"], "<p>Відповіді вільні.</p>")),
     ("s3", "3", step("s3", "3A–B Reading (зроблено вдома)", "3 хв",
       "<p>Прогнозування + читання для загального розуміння (як <i>Watch the video</i> в книзі). Студент перевіряє, чи збіглися його ідеї з текстом.</p>",
       ["Employers want skills that can be applied to a range of tasks and roles – even when AI writes part of the code. What skills do you think they mean?", "Now read the article – or listen to it. Were any of your ideas mentioned?"],
       ul(["3A: 1–2 хв, приймайте будь-які відповіді.", "3B студент уже зробив удома (стаття + відео). Попросіть 2–3 ідеї, які збіглися, і одну, якої не було.",
           "Поясніть <i>old news</i>, <i>tech stack</i>, <i>break the build</i>, <i>ship a product</i>, якщо треба."]),
       ["Which idea in the article surprised you?", "Do you agree that critical thinking is more important now, not less?"], "", "Стаття навмисно містить усі навички з відео книги — у 4A вони знадобляться.")),
     ("s4", "4", step("s4", "4A–B Reading (перевірка)", "3 хв",
       "<p>Детальне читання: знайти навички, способи комунікації, три поради. 4B — перевернути: описати <i>unsuccessful</i> працівника (антоніми).</p>",
       ["Read again and answer the three questions.", "Now the opposite: what words describe an unsuccessful tech worker in 2026?"],
       ul(["Після кожного питання — кнопка Show answer.", "У 4B зверніть увагу на заперечні форми: <i>dishonest, unmotivated, inflexible, unable to set goals</i>."]),
       ["Have you ever worked with someone like that? What happened?"],
       "<p><b>1</b> team player, work well with others, think outside the box, set goals, flexibility, critical thinking, problem-solving, communication skills, honesty, integrity, being genuine, passionate, motivated, hard-working, can-do attitude, determination<br>"
       "<b>2</b> in person, on video calls, in writing (Slack, docs), one-to-one, in large groups (demo)<br><b>3</b> collect skills you can take to the next job/tool/team; be a team player; employers look at the person behind the CV and GitHub<br>"
       "<b>4B</b> lazy, dishonest, negative, unmotivated, inflexible, not a team player, copies AI code without checking</p>")),
     ("s5", "5", step("s5", "5 Speaking", "5 хв",
       "<p>Перенесення навичок у реальні ситуації студента — особистий зв’язок з лексикою.</p>",
       ["Choose one skill from 4A. When is it useful? Give me two situations.", "Which skills are the most important in your job right now?"],
       ul(["Модель від вас: <i>As a teacher, I need to be a good communicator: I explain grammar and I listen to your questions.</i>", "Підштовхуйте до конкретики: <i>When exactly? What did you do?</i>"]),
       ["Which skill would you like to develop this year? How?"], "")),
     ("s6", "6", step("s6", "6 Vocabulary", "7 хв",
       "<p>Ключова лексика уроку в контексті: кожна фраза ↔ конкретна поведінка. Студент бачить, що навичка = дія, а не прикметник у резюме.</p>",
       ["What do these phrases mean? Match each one with the best situation."],
       ul(["Спочатку 1–4 з a–d, потім 5–8 з e–h, як у книзі. Кнопка Check перевіряє.", "Після перевірки: <i>Which of these situations has happened to you?</i>",
           "<i>think outside the box</i> — походить від головоломки «9 крапок»: щоб з’єднати їх 4 лініями, треба вийти за межі квадрата."]),
       ["Tell me about a time you used critical thinking with an AI tool."], "<p>1 d · 2 b · 3 a · 4 c · 5 f · 6 g · 7 e · 8 h</p>")),
     ("s7", "7", step("s7", "7 Vocabulary", "6 хв",
       "<p>Словотвір прикметник ↔ іменник — те, що потрібно для резюме й співбесіди (<i>I’m flexible / Flexibility is one of my strengths</i>).</p>",
       ["Complete the tables. Then let’s check the stress."],
       ul(["Після Check — наголос: <b>FLEX</b>ible / flexi<b>BIL</b>ity, <b>CON</b>fident / <b>CON</b>fidence. Попросіть повторити.", "Міні-завдання: 3 речення про себе з іменниками: <i>My biggest strength is…</i>"]),
       ["Which of these nouns would you put in your LinkedIn headline?"],
       "<p>1 adaptable · 2 flexibility · 3 motivated · 4 confidence · 5 dependable · 6 resourcefulness · 7 independent · 8 ambition · 9 passionate · 10 enthusiasm · 11 honest · 12 authenticity</p>")),
     ("s8", "8", step("s8", "8 Vocabulary", "5 хв",
       "<p>Розширення: навички 2026 року. Студент як ІТ-фахівець тут експерт — дайте йому вести.</p>",
       ["What other skills are important in tech in 2026? And how can you show them at work?"],
       ul(["Якщо застряг — підкажіть: AI literacy, async communication, ownership, giving feedback.", "Show ideas — модель після його відповідей."]),
       ["Which of these skills is the hardest to show in an interview?"], "")),
     ("s9", "9", step("s9", "9 Project", "5 хв",
       "<p>Підготовка до письма: зв’язати навички з конкретними ролями.</p>",
       ["Look at these jobs. Which skills does each one need? Choose three jobs."],
       ul(["Студент обирає 3 ролі й пише коротко: <i>X needs … because …</i>", "Корисно взяти роль, яку він знає зсередини (його колеги)."]),
       ["Which job in the list would be the worst for you? Why?"], "<p>Модель — кнопка Show model answer.</p>")),
     ("s10", "10", step("s10", "10A–D Project", "12 хв + дома",
       "<p>Продукт уроку — job description. Студент збирає лексику уроку в реальний жанр (вакансія міжнародної компанії).</p>",
       ["Think of a job – maybe your dream job. What does the person do? What skills do they need?", "Now write a job description – 80 to 120 words. Then I’ll show you a real one."],
       ul(["10A в класі (3–4 хв).", "10B — можна почати в класі й дописати вдома; лічильник слів на сторінці.", "10C: ви надсилаєте реальну вакансію (LinkedIn / Djinni) — студент перевіряє її за чек-листом.",
           "10D: <i>Would you apply? Why / Why not?</i> — коротка дискусія."]),
       ["What is a red flag in a job description for you?"], "<p>Модель 10B — на сторінці уроку.</p>",
       "Перевіряйте, чи навички вжиті правильно: <i>be a team player</i> (не <i>be team player</i>), <i>set goals</i> (не <i>make goals</i>).")),
    ]
    return O, S
