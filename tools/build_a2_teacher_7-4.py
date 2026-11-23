"""Business Partner A2 — Teacher's Book (Ukrainian). 7.4 Work skills: Presentations (as in the coursebook + online presentation with the Presentation kit).
Usage: python3 build_a2_teacher_7-4.py OUTDIR [LESSON_BASE_URL]  -> OUTDIR/7-4.html
"""
import sys, os
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
BASE = sys.argv[2] if len(sys.argv) > 2 else "../lessons/7-4/all/"
ACC, ACC2, DARK, GR2 = "#3b7dd8", "#e3eefb", "#2a5fb0", "#4f9be8"
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_b1_teacher.py")).read()
src = src[src.index("def ul("):src.index("TPL = TPL.replace")]
ns = {}; exec(src, ns)
TPL = ns["TPL"].replace("студентці", "студенту").replace("#f2a66e", GR2).replace("ACC2", ACC2).replace("ACC", ACC).replace("DARK", DARK)
ul, blk, step = ns["ul"], ns["blk"], ns["step"]
def pagef(num, title, url, overview, steps):
    nav = '<button data-s="s0" class="on">Огляд</button>' + "".join('<button data-s="%s">%s</button>' % (sid, lab) for sid, lab, _ in steps)
    body = '<section id="s0" class="sec on">%s</section>' % overview + "".join(h for _, _, h in steps)
    return TPL.replace("__NUM__", num).replace("__TITLE__", title).replace("__URL__", url).replace("__NAV__", nav).replace("__BODY__", body)

GLOSS = [("potential customers", "потенційні клієнти: ще не купують, ми їм себе презентуємо"), ("the aim", "мета презентації: The aim of today’s presentation is to …"),
         ("a session", "частина зустрічі: a question and answer session — блок запитань наприкінці"), ("e-commerce", "онлайн-торгівля: сайти, інтернет-магазини, онлайн-оплата"),
         ("a provider", "постачальник послуги (the biggest provider of e-commerce services)"), ("a range of", "різні види чогось: a range of services"),
         ("a payment system / a database", "платіжна система / база даних (з відео про Web Trade Builder)"),
         ("sprint review / demo", "зустріч у кінці спринту (1–2 тижні), де команда показує зроблене. Це коротка презентація для замовника або менеджера"),
         ("share my screen", "показати свій екран у Zoom / Meet: Let me share my screen. Can you all see it?")]
overview = (
 blk("big", "Сенс уроку", "<p>Студент учиться <b>робити коротку презентацію про компанію та її послуги</b> (outcome книги). Структура книги повністю збережена: Lead-in 1A–C → відео 7.4.1 (2A–B) → фрази з відео (3) → Speaking box <i>Presenting</i> → письмо й виступ (4).</p>"
     "<p><b>Що ми додали:</b> у вправі 4 (Updated) студент презентує <b>онлайн</b>: шерить екран і веде слайди з <b>Presentation kit</b> (5 готових колод: веб-студія, демо продукту, sprint review, рекомендація оператора, власна компанія). "
     "У Speaking box є блок <i>Presenting online</i>. Classic версія — завдання книги про Force Sport Cars.</p>"
     "<p><b>Куди ведемо:</b> до кінця уроку Павло вміє за 3–4 хвилини представити компанію за схемою «привітання → мета і план → компанія → послуги → питання» і не губиться у Zoom.</p>") +
 blk("aim", "Мовні цілі", ul(["Фрази книги: <i>Thank you for attending this presentation. · The aim of today’s presentation is to … · First, … Then, … Finally, … · So, let’s start with … · Let’s move on to … · We’re based in … · We provide a range of … · So that’s the end of my presentation. Does anyone have any questions?</i>",
                              "Додано (онлайн): <i>Let me share my screen. · Can you all see my screen? · As you can see on this slide, … · Sorry, I think I’m on mute. · I’ll put the link in the chat.</i>",
                              "Словник: усі слова й фрази зверху уроку; клік відкриває картку з перекладом і прикладами."])) +
 blk("run", "Тайминг (60 хв)", '<table class="tt"><tr><th>Крок</th><th>Що</th><th>Час</th></tr>'
     '<tr><td>1A–C</td><td>Розмова про презентації, що важливо, порядок етапів</td><td>10 хв</td></tr><tr><td>2A–B</td><td>Відео 7.4.1: питання + True/False</td><td>12 хв</td></tr>'
     '<tr><td>3</td><td>Фрази з відео</td><td>8 хв</td></tr><tr><td>Presenting</td><td>Speaking box: читаємо, слухаємо, повторюємо</td><td>5 хв</td></tr>'
     '<tr><td>4</td><td>Сценарій (10 хв) + презентація онлайн з шерінгом екрана (5 хв) + фідбек (5 хв)</td><td>20 хв</td></tr><tr><td>—</td><td>Домашка й Extra</td><td>5 хв</td></tr></table>') +
 blk("tgt", "Слова одним рядком", '<table class="tt">' + "".join("<tr><td><b>%s</b></td><td>%s</td></tr>" % g for g in GLOSS) + "</table>") +
 blk("watch", "Відео", "<p>Відео 7.4.1 — оригінальне з книги (Jonathan Potts, Sales Director of Web Trade Builder, 3:14, британський акцент). Відкривається на listeninenglish.com у новій вкладці. "
     "Якщо посилання не відкривається, увімкніть відео з MyEnglishLab або Pearson English Portal.</p>"))

S = []
S.append(("s1", "1A", step("s1", "1A · Lead-in", "4 хв",
 "<p>З’ясовуємо досвід студента: чи презентує він на роботі, як почувається, онлайн чи наживо.</p>",
 ["Do you give presentations at work?", "How do you feel about it? Are you nervous?", "Do you present online or in a meeting room?"],
 ul(["Розпитайте про останню презентацію: про що, для кого, як пройшла.", "Друге питання на екрані: презентація, яку він бачив. Що сподобалось / не сподобалось. Це готує до 1B."]),
 ["What was the best presentation you have ever seen? Why?", "What is more difficult: presenting online or face to face?"], "<p>Відповіді особисті.</p>")))
S.append(("s2", "1B", step("s2", "1B · What is important?", "3 хв",
 "<p>Студент обирає три найважливіші речі в презентації для потенційних клієнтів. Перевірте, що він розуміє <i>potential customers</i>.</p>",
 ["You are presenting your company to potential customers. What is important?", "Choose three things. Why are they important?"],
 ul(["Галочки — тільки для зручності, вони не перевіряються.", "Попросіть пояснити: <i>For me, … is the most important because …</i>", "Пункт <i>a working microphone and screen share</i> — місток до онлайн-презентації."]),
 ["What is the worst thing a presenter can do?"], "<p>Ключа немає.</p>")))
S.append(("s3", "1C", step("s3", "1C · Stages", "3 хв",
 "<p>Порядок етапів презентації. Ця схема — каркас для вправи 4 і для колод у Presentation kit.</p>",
 ["Let’s put the stages of a presentation in order. What comes first?"],
 ul(["Студент ставить номери, натискає Check.", "Проговоріть схему вголос: <i>greet → aim → plan → company → how we can help → questions</i>."]), [],
 "<p>1 b · 2 f · 3 d · 4 e · 5 c · 6 a (ключ книги)</p>")))
S.append(("s4", "2A", step("s4", "2A · Video", "5 хв",
 "<p>Jonathan Potts із Web Trade Builder презентує компанію команді Sleek. Перший перегляд — загальне розуміння.</p>",
 ["You’re going to watch a presentation. Jonathan is the Sales Director of Web Trade Builder.", "Read the questions first. What do you need to listen for?"],
 ul(["Прочитайте питання до перегляду.", "Студент пише короткі нотатки під час перегляду.", "Перевірка: кнопка Show answers."]),
 ["Would you work with this company? Why / why not?"],
 "<p>1 to introduce the company and its services · 2 website building, online shops and payment systems / e-commerce services · 3 Yes, they are.</p>")))
S.append(("s5", "2B", step("s5", "2B · True or false", "7 хв",
 "<p>Деталі: історія, офіси, клієнти, послуги.</p>",
 ["Read the sentences. Which do you think are true?", "Let’s watch again and check."],
 ul(["Дайте прочитати речення до перегляду, поясніть незнайомі слова.", "Після перегляду — Check. Хибні: 1 (він Sales Director) і 7 (вони можуть зробити і повний сайт)."]),
 ["Where are their offices?", "How many clients do they have?"],
 "<p>1 F · 2 T · 3 T · 4 T · 5 T · 6 T · 7 F · 8 T (ключ книги)</p><p class='hint'>Речення 2B відтворено за змістом відео й ключем книги; формулювання можуть трохи відрізнятися від підручника.</p>")))
S.append(("s6", "3", step("s6", "3 · Phrases from the video", "8 хв",
 "<p>Ключові фрази презентації в контексті. Це матеріал для Speaking box і вправи 4.</p>",
 ["These are very useful phrases for presentations. Complete them, then we’ll watch again and check."],
 ul(["Сильніший студент: спершу заповнює, потім дивиться. Слабший: дивиться й заповнює.", "Після перевірки покажіть, який етап з 1C відкриває кожна фраза."]), ["Which phrase starts the main part? Which phrase changes the topic?"],
 "<p>1 morning · 2 aim, introduce · 3 tell · 4 Finally · 5 start · 6 biggest · 7 based · 8 move · 9 build · 10 can · 11 end · 12 questions (ключ книги)</p>")))
S.append(("s7", "Presenting", step("s7", "Speaking box · Presenting", "5 хв",
 "<p>Фрази за етапами. Блок <i>Presenting online</i> додано для Zoom / Meet.</p>",
 ["Let’s read the phrases. Listen and repeat.", "Which phrases do you already use at work?"],
 ul(["Кнопка 🔊 читає фразу (голос браузера).", "Зверніть увагу на вимову: <i>aim /eɪm/, based /beɪst/, provider /prəˈvaɪdə/, range /reɪndʒ/</i>.", "Розіграйте онлайн-проблеми: ви «не бачите екран», студент реагує фразою."]),
 ["What do you say if your camera doesn’t work?"], "")))
S.append(("s8", "4", step("s8", "4 · Writing & speaking", "20 хв",
 "<p><b>Updated:</b> студент обирає колоду в Presentation kit (A PixelForge, B TaskFlow demo, C Sprint review FoodGo, D мобільний оператор, E власна компанія з форми), пише сценарій по етапах, шерить екран і презентує вам 3–4 хв. "
 "<b>Classic:</b> письмо за нотатками про Force Sport Cars, як у книзі, потім прочитати вголос.</p>",
 ["Choose a presentation in the kit. You’re going to present it online.", "Write a short script for each stage. Use the Speaking box.", "OK, share your screen when you’re ready. I’m your potential customer.",
  "Thank you! I have a question: …"],
 ul(["10 хв на сценарій. Допомагайте, але не пишіть за студента.", "Під час виступу ставте таймер 4 хв (є в kit). Записуйте 2–3 помилки й 2–3 вдалі фрази.",
     "Наприкінці поставте 2 питання як клієнт: <i>How much does it cost? Can you help us with …?</i>", "Сильнішому студенту: виступ за короткими нотатками, без повного тексту."]),
 ["What was the easiest stage for you? The most difficult?", "What will you do differently next time?"],
 "<p>Модель Classic (Force Sport Cars) є на сторінці за кнопкою Show a model answer: компанія з Spa (Бельгія), 1987, двигуни для перегонів, власне спортивне авто з 1992 року, ремонт і заміна двигунів.</p>")))
S.append(("s9", "HW", step("s9", "Homework · ключі", "",
 "<p>Новий контекст: кур’єрська компанія QuickBox (Львів) презентує себе онлайн-магазину. 1 порядок речень · 2 вибір слова · 3 читання сценарію · 4 онлайн-проблеми у Zoom · 5 власний сценарій 80–120 слів.</p>",
 ["For homework, write your own presentation. Next lesson you’ll present it online."], ul(["Вправа 5 — заготовка для наступного уроку: почніть із неї розминку."]), [],
 "<p>1: a 5 · b 1 · c 7 · d 3 · e 8 · f 2 · g 6 · h 4<br>"
 "2: aim · First · based · move · provide · attending · provider · questions<br>3A: Lviv · 2021 · 120 · more than 3,000 · 65 hryvnias<br>"
 "4: 1 Let me share my screen… · 2 Sorry, I think I was on mute. · 3 I’ll put the link in the chat. · 4 As you can see on this slide… · 5 Can you hear me OK? · 6 Does anyone have any questions?</p>")))
S.append(("s10", "Extra", step("s10", "Extra · ключі", "",
 "<p>Extra activities 7.4 A/B з книги (нові речення, ключі книги) + вправа у форматі Photocopiable 7.4 + відео Atlassian про sprint review + speed-presenting з картками.</p>",
 ["Let’s do speed-presenting: open a card and finish the sentence about your company."],
 ul(["1–3 студент робить сам. 4 (відео) можна вдома.", "5: як у Photocopiable — студент відкриває картку, закінчує речення про свою компанію; 2 хвилини, потім ви ставите питання."]), [],
 "<p>1: morning · aim · First · Then · Finally (ключ книги A)<br>2: look · start · move · provider · can · based · Finally · questions (ключ книги B)<br>"
 "3: everyone · aim · move · about · have · based · provider · Finally</p>")))
open(os.path.join(OUT, "7-4.html"), "w").write(pagef("7.4", "Work skills: Presentations", BASE + "lesson.html", overview, S).replace("студентці", "студенту"))
print("ok", OUT)
