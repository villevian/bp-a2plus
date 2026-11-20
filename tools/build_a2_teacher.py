"""Business Partner A2 — Teacher's Book (Ukrainian). Unit 7: 7.2 Services and subscriptions (hidden fees).
Usage: python3 build_a2_teacher.py OUTDIR [LESSON_BASE_URL]  -> OUTDIR/index.html, OUTDIR/7-2.html
Format = B1 Teacher's Book: for each step — сенс, як почати (фрази вчителя англійською), як вести, додаткові питання, відповіді.
"""
import sys, os
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
BASE = sys.argv[2] if len(sys.argv) > 2 else "../lessons/7-2/all/"
ACC, ACC2, DARK, GR2 = "#3b7dd8", "#e3eefb", "#2a5fb0", "#4f9be8"
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_b1_teacher.py")).read()
src = src[src.index("def ul("):src.index("TPL = TPL.replace")]
ns = {}; exec(src, ns)
TPL = ns["TPL"].replace("скажіть студентці", "скажіть студенту").replace("#f2a66e", GR2).replace("ACC2", ACC2).replace("ACC", ACC).replace("DARK", DARK)
ul, blk, say, step = ns["ul"], ns["blk"], ns["say"], ns["step"]
def pagef(num, title, url, overview, steps):
    nav = '<button data-s="s0" class="on">Огляд</button>' + "".join('<button data-s="%s">%s</button>' % (sid, lab) for sid, lab, _ in steps)
    body = '<section id="s0" class="sec on">%s</section>' % overview + "".join(h for _, _, h in steps)
    return TPL.replace("__NUM__", num).replace("__TITLE__", title).replace("__URL__", url).replace("__NAV__", nav).replace("__BODY__", body)

GLOSS = [("subscription", "підписка: платиш щомісяця або щороку, поки не скасуєш"),
         ("Adobe / Photoshop", "компанія і її програма для дизайну та фото; її знає кожен дизайнер"),
         ("Microsoft 365 / Copilot", "Word, Excel, Outlook + хмара OneDrive; Copilot — вбудований ШІ-асистент"),
         ("Amazon Prime", "платна підписка Amazon: безкоштовна доставка, відео, музика"),
         ("FTC", "Федеральна торгова комісія США — захищає права споживачів"),
         ("ACCC", "австралійський регулятор конкуренції та прав споживачів (аналог FTC)"),
         ("regulator / took to court", "державний орган, що наглядає за ринком / подав до суду"),
         ("pricing page", "сторінка з тарифами на сайті сервісу (Free / Pro / Business)"),
         ("per user per month", "ціна за одного користувача на місяць — так рахують більшість робочих сервісів (Slack, Jira, Figma)"),
         ("1 TB", "терабайт — обсяг хмарного сховища"),
         ("onboarding", "навчання / знайомство нових користувачів із сервісом")]
overview = (
 blk("big", "Сенс уроку", "<p>Студент учиться <b>пояснювати, скільки коштує послуга і з чого складається ціна</b> (outcome книги: <i>Learners can explain the cost of a service</i>). "
     "У книзі це реклами агентств і словник fees. Ми зберігаємо всі вправи й весь словник, але контекст — <b>підписки та приховані платежі</b>, з якими джуніор в IT стикається щодня: "
     "робочі сервіси за «per user per month», річні плани з щомісячною оплатою, підвищення ціни через ШІ.</p>"
     "<p><b>Куди ведемо студента:</b> від «я плачу за …» (1) → розуміння реальних історій (2) → точний словник fees (3) → слухання порівняння двох послуг з фокусом на <i>загальну</i> ціну (4) → "
     "власний чесний текст про ціну без прихованих платежів (5).</p>"
     "<p><b>Місце в юніті 7 Competition:</b> 7.1 порівнюємо продукти (comparatives) → <b>7.2 рахуємо, скільки реально коштує послуга</b> → 7.3 обираємо найкращого постачальника (superlatives) → 7.4 презентуємо → 7.5 обираємо інструмент для команди.</p>") +
 blk("aim", "Мовні цілі", ul(["Словник книги: <i>charge / pay a fee, the fee includes, fixed, monthly, annual, additional, administration, booking, cancellation fee</i>.",
                              "Додано (A2+, коллокації): <i>hidden fee, early termination fee, the small print, sign up for, cancel a subscription, annual plan paid monthly, price increase, get a refund, free trial</i>.",
                              "Усі слова — зверху уроку; клік на слово відкриває картку: переклад, значення, коллокації, приклад, 🔊."])) +
 blk("run", "Тайминг (60–75 хв)", '<table class="tt"><tr><th>Крок</th><th>Що</th><th>Час</th></tr>'
     '<tr><td>1</td><td>Lead-in: підписки й сервіси</td><td>5 хв</td></tr><tr><td>2A–C</td><td>Читання: Adobe, Microsoft, Amazon + коментарі</td><td>15 хв</td></tr>'
     '<tr><td>3A–C</td><td>Spidergram, matching, пропуски + вимова</td><td>15 хв</td></tr><tr><td>4A–D</td><td>Аудіювання 7.02: два агентства</td><td>15 хв</td></tr>'
     '<tr><td>5</td><td>Письмо: чесна сторінка тарифів (Updated) / реклама кур’єрської служби (Classic)</td><td>10–15 хв або вдома</td></tr></table>') +
 blk("tgt", "IT-слова одним рядком (щоб вести урок без підготовки)", '<table class="tt">' + "".join("<tr><td><b>%s</b></td><td>%s</td></tr>" % g for g in GLOSS) + "</table>") +
 blk("watch", "Аудіо 7.02", "<p>Це <b>оригінальний скрипт книги</b>, озвучений двома ШІ-голосами (Ellie — жіночий, Tom — чоловічий). Слова й цифри збігаються з ключами 4B–4D. "
     "Голоси американські, а в книзі британський акцент; інтонація рівніша, ніж у живих людей, без пауз-вагань. Якщо маєте оригінальний mp3 із MyEnglishLab, його можна поставити замість цього файлу (той самий шлях <i>audio/7-02.mp3</i>).</p>") +
 blk("ans", "Факти в історіях (перевірено)", ul(["Adobe: позов FTC/Мін’юсту США, червень 2024 — прихована плата за дострокове розірвання (50% платежів до кінця року) у плані «Annual, paid monthly».",
                                              "Microsoft: позов ACCC, жовтень 2025 — після додавання Copilot Microsoft 365 Personal подорожчав з A$109 до A$159 (+45%), дешевший план «Classic» показували тільки при скасуванні; історію розкрили користувачі Reddit.",
                                              "Amazon: вересень 2025 — $2,5 млрд за врегулюванням з FTC ($1 млрд штраф + $1,5 млрд повернень, до $51 на людину), обов’язкова зрозуміла кнопка відмови й просте скасування."])))

S = []
S.append(("s1", "1", step("s1", "1 · Lead-in", "5 хв",
 "<p>Активуємо тему й особистий досвід: у кожного є підписки. Студент одразу вживає <i>pay for</i> — основу уроку.</p>",
 ["What services or subscriptions do you pay for? And your company?", "For example, I pay for Spotify and iCloud. What about you?"],
 ul(["Покажіть рамку зі словами, попросіть назвати 2–3, за які платить він сам і його компанія.", "Підштовхніть до моделі: <i>My company pays for … I pay for …</i>", "Запишіть на дошці 2–3 назви сервісів, які він згадав, — повернемося до них у 3C."]),
 ["How many subscriptions do you have? Do you use all of them?", "Which subscription is the most useful for your work?", "Did you ever forget to cancel a free trial?"], "")))
S.append(("s2", "2A–B", step("s2", "2A–B · Reading: three stories", "10 хв",
 "<p>Знайомимо з темою прихованих платежів на реальних історіях. 2A — загальне розуміння (який сервіс), 2B — здогадатися, яка компанія (Photoshop → Adobe, Word/Copilot → Microsoft, Prime → Amazon).</p>",
 ["Read the three stories quickly. What does each company sell?", "Now look at the clues: Photoshop, Copilot, Prime. Which company is it?"],
 ul(["Перше читання — на швидкість (2–3 хв), не пояснюйте слова наперед: жирні слова — словник 3A.", "2B студент вписує назву в поле біля літери й тисне Check.",
     "Після історій — блок коментарів у стилі Reddit: прочитайте разом, тут booking, administration, cancellation, fixed fee для spidergram."]),
 ["Which story is the worst for the customer? Why?", "Did something like this happen to you?"],
 "<p>2A: A — design software; B — office software / cloud storage / AI assistant; C — online shopping &amp; delivery.<br>2B: A Adobe, B Microsoft, C Amazon.</p>")))
S.append(("s3", "2C", step("s3", "2C · Reading for detail", "5 хв",
 "<p>Детальне читання: студент шукає в тексті конкретну інформацію (як 2C у книзі «Which company …?»).</p>",
 ["Read again. Which company … ? Find the line in the story."],
 ul(["Просіть показати рядок у тексті, де відповідь (історії відкриваються кнопкою «Open the stories»)."]),
 ["What is an early termination fee in your own words?", "Why is the Microsoft story connected with Reddit?"],
 "<p>1 A · 2 B · 3 C · 4 C · 5 A · 6 B</p>")))
S.append(("s4", "3A", step("s4", "3A · Spidergram", "5 хв",
 "<p>Збираємо словник fees у систему: дієслова з fee, «the fee includes», типи fee. Як у книзі, група 3 — у будь-якому порядку.</p>",
 ["Let’s collect all the fees from the stories and the comments. What can we do with a fee?", "What types of fees did you see?"],
 ul(["Спершу усно: «What verbs go with fee?» → pay, charge. Потім студент заповнює сам.", "Покажіть, що клік на слово зверху відкриває картку з перекладом і прикладом."]),
 [], "<p>1 includes · 2 pay / charge · 3 (additional), monthly or <b>annual</b>, <b>hidden</b>, <b>cancellation</b>, <b>early termination</b>, <b>booking</b>, <b>administration</b>, <b>fixed</b> (будь-який порядок)</p>",
 "<p><i>charge</i> — компанія бере гроші, <i>pay</i> — клієнт платить. Типова помилка: «I charge a fee» про себе як клієнта.</p>")))
S.append(("s5", "3B", step("s5", "3B · Matching + Pronunciation", "5 хв",
 "<p>Перевіряємо значення через дефініції англійською (книга, 8 пунктів + 2 нові: hidden, early termination).</p>",
 ["Read the explanation. Which fee is it?"],
 ul(["Студент обирає зі списку, Check показує правильне.", "Pronunciation bank: /əʊ/ (go, no) vs /aʊ/ (now, how). Нехай натисне 🔊 і повторить; додайте його слова: <i>account, discount</i>."]),
 ["Which fee do you hate the most?"],
 "<p>1 charge · 2 fixed · 3 monthly · 4 additional · 5 cancellation · 6 includes · 7 hidden · 8 booking · 9 early termination · 10 administration</p>")))
S.append(("s6", "3C", step("s6", "3C · Gap fill + personalisation", "5 хв",
 "<p>Слова в нових реченнях (курси, ШІ-інструмент, вебстудія) + форма (<i>charges, includes</i>).</p>",
 ["Complete the sentences. Be careful with the form: he/she/it + -s."],
 ul(["Зверніть увагу на 1 і 4: <i>charges</i>, <i>includes</i> (Present Simple, 3-тя особа).", "Наприкінці — особисте питання: яку приховану плату платив він сам?"]),
 ["Have you ever paid a booking fee? For what?"],
 "<p>1 charges · 2 additional · 3 monthly · 4 includes · 5 annual · 6 cancellation · 7 booking · 8 fixed</p>")))
S.append(("s7", "4A–B", step("s7", "4A–B · Listening for gist", "7 хв",
 "<p>Перехід від підписок до B2B-послуги: компанія обирає рекрутингове агентство. Головна думка: дешевша фіксована ціна + <b>additional fees</b> може виявитися не дешевшою — треба рахувати <i>overall</i>. Це той самий «прихований платіж», але в бізнес-рішенні.</p>",
 ["Your company needs three new people. What services do you want from a recruitment agency?", "Listen. Which agency do Tom and Ellie choose? Why?"],
 ul(["4A — 2 хв розмови: background checks, guarantee, interviews, price.", "4B — перше прослуховування, лише головне питання. Якщо важко — швидкість «slower»."]),
 ["What is a six-month guarantee?", "Why can a percentage fee be expensive?"],
 "<p>4B: They will use Jones if Jones is cheaper overall — first they need to know Jones’ fee for background checks.</p>")))
S.append(("s8", "4C", step("s8", "4C · Listening for detail", "5 хв",
 "<p>Слухаємо конкретну інформацію: місто, цифри, відсотки, ціна.</p>",
 ["Look at the two webpages first. What kind of information is missing — a number, a city, a word?", "Listen again and complete the gaps."],
 ul(["Перед слуханням — передбачення: біля кожного пропуску «number / word / place».", "Після — скрипт (кнопка «Show script») для самоперевірки."]),
 [], "<p>1 London · 2 six · 3 three · 4 professional · 5 interviews · 6 10–15% · 7 399 · 8 additional</p>")))
S.append(("s9", "4D", step("s9", "4D · True / False", "3 хв",
 "<p>Порівняння двох послуг за таблицею — підготовка до 7.3 (superlatives).</p>",
 ["Use the webpages. True or false?"], ul(["Просіть пояснити кожне F: «It’s false because …»."]),
 ["Which agency would you choose for your company? Why?"], "<p>1 T · 2 F · 3 F · 4 F · 5 T</p>")))
S.append(("s10", "5", step("s10", "5 · Writing", "10–15 хв / вдома",
 "<p><b>Updated:</b> студент пише «чесну» сторінку тарифів для свого інструмента TaskFlow — використовує всю мову уроку і робить навпаки до історій A–C: <i>no hidden fees, no cancellation fee</i>. "
 "<b>Classic:</b> завдання книги — реклама кур’єрської служби AP Couriers.</p>",
 ["Now you are the company. Write a pricing page with no hidden fees.", "Answer the five questions — use full sentences."],
 ul(["Опори біля кожного питання: <i>We offer … We charge … Our fixed fee includes …</i>", "Лічильник слів (60–100). Після — «Show a model answer» для порівняння.", "Перевірте: всі 5 питань, повні речення, щонайменше 4 слова з уроку."]),
 ["Is your pricing better than Adobe’s? Why?"],
 "<p><b>Модель (Updated):</b> TaskFlow is a simple task manager for small teams. We offer three plans: Free, Pro and Business. The Free plan is for up to three users. The Pro plan costs €8 per user per month. You can also pay €80 per user per year and save money. For bigger teams, we charge a fixed fee of €300 a month for up to 50 users. All plans include unlimited projects, Slack and Jira integration and support in a chat. There is an additional fee of €5 a month for extra storage over 100 GB. We also offer onboarding training for €150 — it is optional. There is no cancellation fee. You can cancel any time in two clicks.</p>"
 "<p><b>Модель (Classic, ключ книги):</b> We provide local and national delivery of parcels and large and/or heavy items. We offer same-day or next-day delivery. We charge a £22 fixed fee for same-day delivery. We charge £10–20 for next-day delivery for items between 1 kg and 5 kg. … There is an additional fee for items over 5 kg.</p>")))
S.append(("s11", "HW", step("s11", "Homework · ключі", "",
 "<p>Домашка: словник (1–2, 4), читання повідомлення тімліда в Slack про перевірку підписок (3), відповідь у треді (5, 50–80 слів).</p>",
 ["For homework, read Olha’s message about the team’s subscriptions and reply in the thread."], ul(["Закриті завдання перевіряються автоматично; відповідь у треді (5) прокоментуйте в адмінці — студент побачить коментар угорі сторінки."]), [],
 "<p>1: 1 cancellation · 2 includes · 3 charges · 4 small print · 5 trial · 6 refund · 7 fixed · 8 increase<br>"
 "2: 1 sign up for a plan · 2 cancel a subscription · 3 get a refund · 4 read the small print · 5 charge customers €5 for delivery · 6 start a free trial<br>"
 "3A: 1 F · 2 T · 3 F · 4 T · 5 F · 6 T; 3B: DesignHub; cancel MeetNow, delete old files in CloudBox, don’t renew DesignHub<br>"
 "4: 1 annual · 2 increase · 3 includes · 4 monthly · 5 cancel · 6 refund · 7 hidden · 8 sign up</p>")))
S.append(("s12", "Extra", step("s12", "Extra · ключі", "",
 "<p>Extra — те, чого немає в основному уроці: формат Extra vocabulary practice книги (1), як читати ціни <i>a / an / per</i> (2), зміни ціни <i>go up from … to …</i> (3), рольова гра «support chat» (4: ви — Student B).</p>",
 ["Let’s practise saying prices. How do you say €8 per user per month?"], ul(["1–3 студент робить сам; 4 — на уроці: ви Student B (support agent), потім міняєтесь ролями."]), [],
 "<p>1: 1 monthly · 2 additional · 3 cancellation · 4 include · 5 booking · 6 fixed · 7 charge · 8 administration<br>"
 "2A: 1 an hour · 2 per month · 3 at no extra cost · 4 of charge; 2B: €8 per user per month · $2.5 billion · £399 · 10–15% · €159 a year<br>"
 "3A: 1 up · 2 increase · 3 save · 4 down · 5 from</p>")))

open(os.path.join(OUT, "7-2.html"), "w").write(pagef("7.2", "Services and subscriptions", BASE + "lesson.html", overview, S))
idx = ('<section id="s0" class="sec on"><div class="bsec">Business Partner A2 · Teacher’s Book</div>'
       + blk("aim", "Unit 7 Competition", ul(['<a href="7-2.html">7.2 Services and subscriptions — hidden fees (Adobe, Microsoft, Amazon)</a> · Lesson · Homework · Extra', '<a href="7-3.html">7.3 The best providers — mobile operators for company eSIMs (superlatives)</a> · Lesson · Homework · Extra · Games']))
       + "</section>")
open(os.path.join(OUT, "index.html"), "w").write(TPL.replace("__NUM__", "A2").replace("__TITLE__", "Teacher’s Book").replace("__URL__", "../index.html").replace("__NAV__", "").replace("__BODY__", idx))
print("ok", OUT)
