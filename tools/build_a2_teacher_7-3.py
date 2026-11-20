"""Business Partner A2 — Teacher's Book (Ukrainian). 7.3 The best providers (mobile operators for company eSIMs).
Usage: python3 build_a2_teacher_7-3.py OUTDIR [LESSON_BASE_URL]  -> OUTDIR/7-3.html
Same format as build_a2_teacher.py (7.2): сенс, як почати (фрази вчителя), як вести, додаткові питання, відповіді.
"""
import sys, os
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
BASE = sys.argv[2] if len(sys.argv) > 2 else "../lessons/7-3/all/"
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

GLOSS = [("mobile operator", "мобільний оператор (Kyivstar, Vodafone, lifecell)"),
         ("eSIM", "вбудована електронна SIM-картка, без пластику; компанії видають eSIM співробітникам"),
         ("business tariff", "тариф для компанії: ціна «per user per month», тобто за одного співробітника на місяць"),
         ("network coverage", "покриття: де телефон ловить зв’язок (місто, села, метро)"),
         ("download speed / Mbps", "швидкість завантаження; Mbps = мегабіти за секунду"),
         ("Ookla Speedtest / nPerf", "сервіси, що міряють швидкість інтернету за тестами користувачів і роблять рейтинги операторів"),
         ("support chat", "чат техпідтримки в застосунку або на сайті"),
         ("coworking space", "коворкінг: офіс, де можна орендувати місце для команди (домашка)")]
overview = (
 blk("big", "Сенс уроку", "<p>Студент учиться <b>порівнювати послуги й постачальників і писати короткий звіт</b> (outcome книги: <i>Learners can compare services</i>). "
     "У книзі — лист маркетолога про страхову компанію зі Strengths / Areas of improvement. Ми зберігаємо всі вправи (1A–B, 2, 3, граматика, 4A–B, 5) і граматику superlatives, "
     "але контекст — <b>вибір мобільного оператора для 25 корпоративних eSIM</b>. Тема знайома кожному, IT-знань не потребує.</p>"
     "<p><b>Куди ведемо студента:</b> що важливо при виборі постачальника (1) → лист-звіт про одного оператора (2) → фрази ділового листа (3) → superlatives (4A–B) → власний звіт-рекомендація (5).</p>"
     "<p><b>Місце в юніті 7:</b> 7.1 порівнюємо два продукти (comparatives) → 7.2 рахуємо реальну ціну послуги (fees) → <b>7.3 обираємо найкращого з трьох (superlatives)</b> → 7.4 презентуємо → 7.5 обираємо інструмент для команди.</p>") +
 blk("aim", "Мовні цілі", ul(["Граматика книги: superlatives — <i>the cheapest, the biggest, the friendliest, the most reliable, the best, the worst</i>.",
                              "Словник книги (passive vocabulary): <i>internet / energy provider, mobile phone contract, value for money, service reliability, staff knowledge, problem solving, satisfied customers, quality of communication, easy to access</i>.",
                              "Фрази листа: <i>Please find attached … · Please find a summary below. · If you have any questions, please let me know. · Best regards,</i>",
                              "Додано: <i>mobile operator, network coverage, download speed, eSIM, business tariff, the longest wait</i>. Усі слова — зверху уроку, клік відкриває картку."])) +
 blk("run", "Тайминг (60 хв)", '<table class="tt"><tr><th>Крок</th><th>Що</th><th>Час</th></tr>'
     '<tr><td>1A–B</td><td>Lead-in: які провайдери в компанії, «Did you know?» про рейтинги, ранжування критеріїв</td><td>10 хв</td></tr>'
     '<tr><td>2</td><td>Читання: лист про SkyMobile + таблиця good / bad</td><td>10 хв</td></tr><tr><td>3</td><td>Фрази листа + Slack-версії</td><td>5 хв</td></tr>'
     '<tr><td>Grammar</td><td>Superlatives + вимова /p/ /b/ /f/ /v/</td><td>10 хв</td></tr><tr><td>4A–B</td><td>Вправи на superlatives + таблиця з зірочками</td><td>10 хв</td></tr>'
     '<tr><td>5</td><td>Письмо: Slack-рекомендація (Updated) / лист про Travel Care (Classic)</td><td>15 хв або вдома</td></tr></table>') +
 blk("tgt", "Слова одним рядком (щоб вести урок без підготовки)", '<table class="tt">' + "".join("<tr><td><b>%s</b></td><td>%s</td></tr>" % g for g in GLOSS) + "</table>") +
 blk("watch", "Реальні й вигадані назви", "<p><b>Реальні</b> Kyivstar, Vodafone, lifecell і цифри Ookla / nPerf є тільки в lead-in (1A), бо це перевірені опубліковані рейтинги. "
     "У читанні, вправах і письмі оператори <b>вигадані</b> (SkyMobile, Volt, LineUp, NovaTel), щоб не приписувати реальним брендам «найгіршу підтримку».</p>") +
 blk("ans", "Факти в lead-in (перевірено)", ul(["Ookla Speedtest, липень–грудень 2024: Kyivstar — найкраще покриття й найшвидша мережа; speed score Kyivstar 35,65 · Vodafone 33,38 · lifecell 29,42.",
                                              "nPerf, 2024: загальний бал Vodafone 60 573 (лідер), Kyivstar 59 339, lifecell 57 054; найвища середня швидкість завантаження — lifecell, 24,57 Мб/с.",
                                              "Висновок для розмови: <i>Which is the best? It depends on the report!</i>"])))

S = []
S.append(("s1", "1A", step("s1", "1A · Lead-in", "5 хв",
 "<p>Активуємо тему: які постачальники послуг є в компанії студента і чи задоволений він ними. «Did you know?» дає реальні рейтинги й перші superlatives у контексті.</p>",
 ["Which of these service providers does your company use?", "Which mobile operator do you use? Are you happy with it?", "Look at the reports. Which operator is the best? Why do the reports say different things?"],
 ul(["Пройдіться по рамці слів; студент називає 2–3 провайдери своєї компанії.", "Прочитайте разом «Did you know?». Не пояснюйте граматику, просто зверніть увагу на <i>the best, the fastest, the highest</i>.", "Запитайте, чи згоден він з рейтингом за своїм досвідом."]),
 ["Have you ever changed your operator? Why?", "Is the metro coverage good where you live?"], "")))
S.append(("s2", "1B", step("s2", "1B · Ranking criteria", "5 хв",
 "<p>Студент ранжує критерії вибору оператора. Ці ж слова будуть у таблиці вправи 2 і в письмі.</p>",
 ["Your company needs 25 eSIMs. What is the most important thing for you?", "Why is that more important than the price?"],
 ul(["Перевірте розуміння: <i>value for money, problem solving, easy to access</i>.", "Студент ставить номери 1–8, потім пояснює топ-3: <i>For me, … is the most important because …</i>", "Можна не погоджуватися з ним: це дає більше мовлення."]),
 ["Is the cheapest operator always the best value for money?"], "<p>Відповіді особисті, ключа немає.</p>")))
S.append(("s3", "2", step("s3", "2 · Reading", "10 хв",
 "<p>Лист-звіт за моделлю книги: Strengths / Areas of improvement. Студент знаходить, де SkyMobile сильний, а де слабкий, і бачить superlatives у контексті (виділені жирним).</p>",
 ["Read Iryna’s email. Is SkyMobile good or bad at these things?", "Which part of the email shows the strengths?"],
 ul(["Перед читанням пройдіться по рядках таблиці.", "Студент позначає good / bad, потім натискає Check.", "Попросіть знайти доказ у тексті: <i>the longest wait for support → bad</i>."]),
 ["Would you choose SkyMobile? Why? / Why not?"], "<p>Good: network coverage, download speed, value for money · Bad: satisfied customers, time to answer support chats, problem solving</p>")))
S.append(("s4", "3", step("s4", "3 · Email phrases", "5 хв",
 "<p>Корисні фрази для ділового листа і їхні короткі версії для Slack.</p>",
 ["What do we say when we send a file with an email?", "How do you end a business email?"],
 ul(["Студент зіставляє фрази з функціями, потім Check.", "Покажіть Slack-версії: студент пише й у Slack, і в листах.", "Попросіть сказати кожну фразу вголос з правильною інтонацією."]),
 ["Do you write emails or Slack messages more at work?"], "<p>1 b · 2 d · 3 a · 4 c</p>")))
S.append(("s5", "Grammar", step("s5", "Grammar · Superlatives + Pronunciation", "10 хв",
 "<p>Порівняння одного з групи (3+). Правила: -est / -iest / подвоєння / the most / неправильні best, worst. Вимова /p/ /b/ /f/ /v/ (Pronunciation bank, с.100).</p>",
 ["In 7.1 we said ‘cheaper than’. What do we say for three or more operators?", "Look at the email. Find all the superlatives."],
 ul(["Зверніть увагу на <i>the</i>: без нього типова помилка.", "Порівняйте з 7.1: <i>cheaper than</i> → <i>the cheapest</i>.", "Вимова: студент повторює за 🔊; українці часто оглушують /b/ і /v/ в кінці слова."]),
 ["What’s the biggest city you know? The most expensive app?"], "<p>Grammar reference у книзі: с.111 Comparing (2): Superlatives.</p>")))
S.append(("s6", "4A", step("s6", "4A · Superlatives", "5 хв",
 "<p>Контрольована практика форм.</p>", ["Complete with the superlative. Don’t forget ‘the’!"],
 ul(["Студент робить сам, потім Check.", "Попросіть прочитати речення вголос."]), [],
 "<p>1 the shortest · 2 the cheapest · 3 the most reliable · 4 the most knowledgeable · 5 the friendliest · 6 the widest · 7 the highest · 8 the best (ключ книги)</p>")))
S.append(("s7", "4B", step("s7", "4B · Table with stars", "5 хв",
 "<p>Читаємо таблицю й формулюємо superlatives: підготовка до письма.</p>", ["Look at the table. Which operator is the most reliable?"],
 ul(["Студент робить сам, потім Check.", "«Your turn»: студент обирає оператора і пояснює двома superlatives."]), ["Which one would you choose for our team? Why?"],
 "<p>1 the most reliable · 2 the best · 3 the most knowledgeable · 4 the lowest · 5 the worst · 6 the biggest (ключ книги)</p>")))
S.append(("s8", "5", step("s8", "5 · Writing", "15 хв / вдома",
 "<p><b>Updated:</b> Slack-повідомлення тимліду з рекомендацією оператора (Strengths / Areas of improvement + superlatives + фрази з 3). "
 "<b>Classic:</b> завдання книги, лист про Travel Care і дві інші туристичні компанії.</p>",
 ["Olha asks: ‘Which operator for our company eSIMs?’ Write your answer in Slack."],
 ul(["Нагадайте структуру з вправи 2.", "Лічильник слів: 60–100.", "Перевірте: є рекомендація, щонайменше 4 superlatives, фрази з 3."]),
 ["Is the cheapest operator the best choice for a team? Why?"],
 "<p><b>Модель (Updated):</b> Hi Olha! Attached is the operator comparison for our 25 eSIMs. Quick summary: I recommend LineUp. Strengths: LineUp has the best network coverage, the shortest wait for support (2 minutes in the chat) and the most satisfied business clients (91%). You can set up an eSIM in the app. Areas of improvement: LineUp has the highest price — €11 per user per month. Volt is the cheapest, and NovaTel has the fastest download speed, but NovaTel has the worst support. Any questions — just ping me! Thanks!</p>"
 "<p><b>Модель (Classic, ключ книги):</b> Please find attached a copy of the customer satisfaction survey … Strengths: Travel Care has the most knowledgeable staff, the friendliest staff, the best customer service. Areas of improvement: the highest prices, the worst value for money.</p>")))
S.append(("s9", "HW", step("s9", "Homework · ключі", "",
 "<p>Новий контекст: коворкінги у Львові та інтернет-провайдер для офісу. Завдання різних типів: форми, слова з першою літерою, читання, виправлення помилок, лист.</p>",
 ["For homework, read Daria’s email about three coworking spaces."], ul(["Закриті завдання перевіряються автоматично; лист (5) прокоментуйте в адмінці."]), [],
 "<p>1: the easiest · the most reliable · the biggest · the best · the cheapest · the friendliest · the worst · the most expensive · the quietest · the widest<br>"
 "2: speed · money · solving · coverage · satisfied customers · knowledge · access<br>"
 "3A: 1 Green Desk · 2 Loft 21 · 3 HubSpace · 4 Loft 21 · 5 HubSpace · 6 Green Desk<br>"
 "4: the cheapest · the best · the fastest · the most reliable · the worst · the biggest</p>")))
S.append(("s10", "Extra", step("s10", "Extra · ключі", "",
 "<p>Extra activities 7.3 A/B з книги в новому контексті (реклама ШІ-асистента, речення для sales-презентації) + питання з superlatives про себе + картки постачальників (ви — Student B).</p>",
 ["Let’s write sentences for a sales presentation."], ul(["1–2 студент робить сам; 3–4 — розмова на уроці."]), [],
 "<p>1: most reliable · most knowledgeable · best · longest · friendliest · highest · most satisfied · quickest (ключ книги)<br>"
 "2: Our service is the most reliable. · We have the most knowledgeable staff. · We provide the best value for money. · We have the biggest number of business clients. · Our tariff is the cheapest. · Our customers are the most satisfied in the industry. · We have the highest levels of positive feedback.</p>")))
S.append(("s11", "Games", step("s11", "Speaking & Games", "",
 "<p>Окрема сторінка: розмова за картками (60 с), Memory, Definition race, Unscramble, Strength or area of improvement?, Taboo, 3 рольові ігри (продаж оператора, вибір коворкінгу, скарга).</p>",
 ["Let’s play! Take a card and talk for a minute."], ul(["У рольових іграх картка B — ваша."]), [], "")))
open(os.path.join(OUT, "7-3.html"), "w").write(pagef("7.3", "The best providers", BASE + "lesson.html", overview, S).replace("студентці", "студенту"))
print("ok", OUT)
