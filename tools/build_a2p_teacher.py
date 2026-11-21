"""Business Partner A2+ — Teacher's Book (Ukrainian). Unit 1 (bleisure / Barcelona, standard business English updated to 2026): 1.2 Events management.
Usage: python3 build_a2p_teacher.py OUTDIR [LESSON_BASE_URL]  -> OUTDIR/index.html, OUTDIR/1-2.html
Same format as the B1 / A2 Teacher's Books: сенс, як почати (фрази вчителя англійською), як вести, додаткові питання, відповіді.
"""
import sys, os
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
BASE = sys.argv[2] if len(sys.argv) > 2 else "../lessons/1-2/all/"
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

UNIT = ('<table class="tt"><tr><th>Урок</th><th>Крок поїздки «конференція в Барселоні + вихідні»</th></tr>'
        '<tr><td>1.1 Business travel</td><td>Їдемо: транспорт, житло; поради колезі, який теж залишається на вихідні</td></tr>'
        '<tr><td><b>1.2 Events management</b></td><td><b>Організатор конференції: порівнюємо площадки для вечірнього заходу</b></td></tr>'
        '<tr><td>1.3 Small talk</td><td>Знайомимося на конференції та вечірньому заході</td></tr>'
        '<tr><td>1.4 Dealing with problems</td><td>Проблеми в поїздці: Wi-Fi в готелі, проєктор, пошта</td></tr>'
        '<tr><td>1.5 Asking for information</td><td>Лист / повідомлення: чи можна продовжити поїздку</td></tr>'
        '<tr><td>Business workshop 1</td><td>Рейс скасовано — змінюємо плани</td></tr></table>')
overview = (
 blk("big", "Сенс уроку", "<p>Студентка вчиться <b>робити прості порівняння</b> (outcome книги: <i>Learners can make simple comparisons</i>) на темі організації подій. "
     "Усе, як у книзі: lead-in про події та якості організатора → інтерв’ю з Events Manager → comparatives / superlatives → вибір площадки → власні речення.</p>"
     "<p><b>Що оновлено:</b> події 2026 року (гібридні заходи, офсайти, запуск продукту), інтерв’ю звучить як 2026: Alicia працює в Барселоні, половина гостей лишається на вихідні (<i>bleisure</i>), реєстрація через QR-код, ШІ-планувальник, трансляція доповідей, ціни вищі, ніж 5 років тому. "
     "Площадки — для вечірнього заходу конференції в Барселоні. Без IT-зсуву: загальна ділова англійська.</p>") +
 blk("aim", "Сюжет юніту 1 (bleisure, Барселона)", UNIT) +
 blk("aim", "Мовні цілі", ul(["Граматика: comparatives / superlatives (-er / -est, more / most, less / least, good – better – the best, bad – worse – the worst).",
                              "Словник (зверху уроку, клік → картка з перекладом, коллокаціями, прикладом): <i>plan an event, attend a conference, product launch, team offsite, hybrid event, stay for the weekend, client, guest, venue, staff, entertainment, arrange, organise, manage a budget, pay attention to detail, get on with people</i>.",
                              "Вимова: буква <i>r</i> у британській і американській англійській."])) +
 blk("run", "Таймінг (60–75 хв)", '<table class="tt"><tr><th>Крок</th><th>Що</th><th>Час</th></tr><tr><td>1–2</td><td>Lead-in: події, якості організатора</td><td>8 хв</td></tr>'
     '<tr><td>3–6</td><td>Аудіювання 1.01 (інтерв’ю з Alicia)</td><td>15 хв</td></tr><tr><td>7–9</td><td>Граматика</td><td>20 хв</td></tr><tr><td>10–11</td><td>Порівнюємо площадки, пишемо речення, вимова</td><td>15 хв</td></tr></table>') +
 blk("watch", "Аудіо 1.01", "<p>Оновлений скрипт (2026), структура й ключі книги збережені; озвучено двома ШІ-голосами (Marek — ведучий подкасту, Alicia — Events Manager), 3 хв. Голоси американські. Скрипт — кнопка «Show script» в уроці.</p>"))

S = []
S.append(("s1", "1–2", step("s1", "1–2 · Lead-in", "8 хв", "<p>Активуємо тему подій і особистий досвід; 2A–B — словник якостей, які потім прозвучать в інтерв’ю.</p>",
 ["What was the last event you went to? Was it well organised?", "Look at the box. Which of these events have you been to? Which was the best?"],
 ul(["1: студентка називає 2–3 події, де була; підштовхніть до <i>It was the best / the most interesting …</i> — перший неформальний superlative.", "2A: попросіть пояснити кожну якість своїми словами; зверніть увагу на нові: <i>good with online tools, calm when plans change</i>.", "2B: опори: <i>I’m (not) good at … / I (don’t) like … / I can’t …</i>"]),
 ["What was the worst event you went to? Why?", "Have you ever stayed for the weekend after a work trip?"],
 "<p>2A (можливі відповіді): organised, able to pay attention to details, good with budgets, good with online tools, calm when plans change.</p>")))
S.append(("s2", "3–4", step("s2", "3–4 · Listening for gist", "7 хв", "<p>Прогнозування перед слуханням і загальне розуміння: про що говорить Alicia.</p>",
 ["You’re going to hear Alicia, an events manager in Barcelona. What will she talk about?", "Listen. Did she talk about your ideas?"],
 ul(["3: 2–3 хв на ідеї для кожної категорії, запишіть їх; нова категорія — «що нового у 2026».", "4: одне прослуховування, порівняйте з ідеями. Якщо важко — швидкість «slower»."]), ["What is bleisure?", "How does technology help Alicia?"],
 "<p><b>Types of events:</b> conferences, product launches, team offsites, hybrid events, events for companies (not weddings), a company anniversary party. <b>Important things:</b> budget, location / venue, entertainment (a DJ), food (vegan, gluten-free), tables and chairs, staff, the weather for outdoor events. "
 "<b>Skills:</b> get on with people, be organised, pay attention to detail; top priority — client satisfaction. <b>New in 2026:</b> hybrid events, QR-code registration, AI tool for the schedule, streaming the talks live, higher prices, guests stay for the weekend (bleisure).</p>")))
S.append(("s3", "5–6", step("s3", "5–6 · Listening for detail", "8 хв", "<p>Детальне розуміння + виправлення хибних тверджень (як у книзі).</p>",
 ["Read the sentences first. Then listen again: true or false? Correct the false ones."],
 ul(["Слабшій студентці — два прослуховування: спершу T/F, потім виправлення.", "6 — коротка розмова: опори <i>I would / wouldn’t … because I’m (not) …</i>"]), ["Would you like to plan a conference in Barcelona? Why?"],
 "<p>1 F — she doesn’t plan weddings (wedding planners do). 2 T. 3 F — she always talks about the budget at the first meeting. 4 F — about half of the guests stay for the weekend. 5 T. 6 T.</p>")))
S.append(("s4", "7", step("s4", "7 · Grammar: comparatives & superlatives", "8 хв", "<p>Виводимо правило з речень інтерв’ю.</p>",
 ["Look: harder than, the best. Which compares two things? Which compares one thing with all the others?"],
 ul(["Перед 7A напишіть: <i>A business lunch is easier than a wedding. A small party is the easiest event.</i> Підкресліть, поясніть.", "Після 7B — таблиця форм у рамці; зверніть увагу на bigger / hotter, easier, better / worse."]), [],
 "<p>7A: comparatives — 1, 5, 7, 8; superlatives — 2, 3, 4, 6. 7B: 1 superlative 2 comparative 3 irregular.</p>")))
S.append(("s5", "8", step("s5", "8 · Choose the option", "5 хв", "<p>Контрольована практика форми.</p>", ["Choose the correct option. Why is it correct?"],
 ul(["Просіть пояснити: <i>than</i> → comparative; <i>the … on the list</i> → superlative."]), [],
 "<p>1 the most 2 less difficult 3 harder 4 the worst 5 more 6 easier than 7 The best 8 The least</p>")))
S.append(("s6", "9", step("s6", "9 · Gap fill", "7 хв", "<p>Утворення форм + <i>the / than</i>.</p>", ["Complete with the correct form. Do you need the or than?"],
 ul(["Перевірте правопис: bigger, easier, cheapest."]), [], "<p>1 the biggest 2 worse than 3 easier than 4 the least expensive 5 the cheapest 6 better than 7 smaller than 8 the best</p>")))
S.append(("s7", "10", step("s7", "10 · Speaking: venues", "8 хв", "<p>Вільніше вживання: порівнюємо три площадки для вечірнього заходу конференції в Барселоні.</p>",
 ["You’re planning the evening event of a conference in Barcelona. Compare the three venues.", "Which is the best for 150 guests? And for a team of 20?"],
 ul(["Студентка говорить 6–8 речень, ви записуєте помилки форми й розбираєте наприкінці.", "Опорні прикметники: cheap, expensive, big, small, formal, fun, far, good."]),
 ["Which venue would you choose for your own company? Why?"],
 "<p>Можливі відповіді: The boat restaurant is the most expensive. The rooftop is the least expensive. The boat restaurant is the biggest. The winery is the smallest. The boat restaurant has the most staff. 10B: 150 guests → the boat restaurant (the only one for more than 120); team of 20 → the winery or the rooftop.</p>")))
S.append(("s8", "11", step("s8", "11 · Writing + Pronunciation", "7 хв / вдома", "<p>Три comparative + три superlative речення про площадки свого міста (або Барселони). Вимова: <i>r</i> UK vs US.</p>",
 ["Think of three places in your town for an event. Write sentences about them."],
 ul(["Можна дати вдома, якщо бракує часу.", "Вимова: послухайте UK і US; у британській <i>r</i> не звучить у кінці слова й перед приголосною: cheaper, park, worst."]), [], "")))
S.append(("s9", "HW", step("s9", "Homework · ключі", "", "<p>Словник, форми, читання (три готелі в Барселоні), виправлення помилок, повідомлення колезі з рекомендацією готелю (60–90 слів).</p>",
 ["For homework, choose a hotel for the conference and the weekend, and write to a colleague."], ul(["Закриті завдання перевіряються автоматично; повідомлення (5) прокоментуйте в адмінці."]), [],
 "<p>1: 1 client 2 venue 3 guests 4 staff 5 entertainment 6 budget 7 arrange 8 organised<br>2: cheaper / the cheapest · bigger / the biggest · easier / the easiest · hotter / the hottest · more expensive / the most expensive · more comfortable / the most comfortable · better / the best · worse / the worst<br>"
 "3A: 1 C 2 A 3 B 4 C 5 A 6 A<br>4: 1 cheaper than 2 the best 3 hotter 4 than 5 biggest 6 easier</p>")))
S.append(("s10", "Extra", step("s10", "Extra · ключі", "", "<p>A–B — Extra activities книги (оновлені), C — правопис, D — розмова: план вихідних у Барселоні (ви — колега студентки).</p>",
 ["Let’s plan our weekend in Barcelona. What do you want to do on Saturday?"], ul(["D: студентка порівнює три варіанти й вирішує; ви заперечуєте, щоб вона аргументувала: <i>But Montserrat is more expensive …</i>"]), [],
 "<p>A: 1 plan 2 client 3 venue 4 guests 5 arrange 6 organise 7 staff 8 manage<br>B: 1 We want the cheapest option. 2 A hotel for 50 is cheaper than a hotel for 500. 3 We need the biggest conference room. 4 We want to hire the best staff. 5 An online event is easier than a hybrid event. 6 Rain is the worst weather for an outdoor party. 7 A taxi is more expensive than the metro. 8 Managing three people is less difficult than managing twenty people.<br>"
 "C: 1 bigger 2 easier 3 nicer 4 the hottest 5 the busiest 6 later</p>")))

open(os.path.join(OUT, "1-2.html"), "w").write(pagef("1.2", "Events management", BASE + "lesson.html", overview, S))
idx = ('<section id="s0" class="sec on"><div class="bsec">Business Partner A2+ · Teacher’s Book</div>' +
       blk("aim", "Unit 1 Travelling for work (bleisure, Barcelona)", ul(['<a href="1-2.html">1.2 Events management — Lesson · Homework · Extra</a>', '<a href="1-2-speak.html">1.2 Speaking: business situations — твоя роль, приблизний діалог, «якщо вона… → ти…»</a>'])) + "</section>")
open(os.path.join(OUT, "index.html"), "w").write(TPL.replace("__NUM__", "A2+").replace("__TITLE__", "Teacher’s Book").replace("__URL__", "../index.html").replace("__NAV__", "").replace("__BODY__", idx))
print("ok", OUT)
