"""Business Partner A2 — Teacher's Book (Ukrainian). 7.5 Business workshop: The big contract (Unit 7 review + online pitch).
Usage: python3 build_a2_teacher_7-4.py OUTDIR [LESSON_BASE_URL]  -> OUTDIR/7-5.html
"""
import sys, os
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
BASE = sys.argv[2] if len(sys.argv) > 2 else "../lessons/7-5/all/"
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
def tbl(rows): return '<table class="tt">' + "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % c for c in r) for r in rows) + "</table>"
overview = (
 blk("big", "Сенс уроку", "<p>Це <b>повторення всього Unit 7</b> в одній реальній ситуації. Книжковий воркшоп 7.5 «The big contract» (виставка + презентація) ми робимо онлайн: "
     "IT-студія Павла <b>BrightCode</b> бореться за контракт з <b>GreenBox</b> (онлайн-доставка продуктів) проти двох конкурентів. Павло порівнює три пропозиції і презентує свою за 5 хвилин, а ви граєте клієнтку.</p>"
     "<p><b>Що повторюємо:</b> 7.1 порівняння (<i>cheaper than, faster than</i>) · 7.2 fees (<i>the fee includes, additional / monthly / hidden fee, early termination fee, the small print</i>) · "
     "7.3 superlatives і критерії вибору провайдера (<i>the fastest, the best value for money, satisfied customers</i>) · 7.4 фрази презентації.</p>"
     "<p><b>Куди ведемо:</b> Павло не читає текст, а <b>сам будує мову</b>: під кожним слайдом є завдання і підказка «Compare: …». Сценарію немає, є кнопка 💡 Example, якщо він застряг. "
     "Ви відмічаєте в чек-листі під слайдами слова, які він вжив, а сірі слова він використовує на етапі запитань.</p>") +
 blk("run", "Тайминг (60 хв)", tbl([["<b>Крок</b>", "<b>Що</b>", "<b>Час</b>"], ["1A–1B", "Фрази презентації (Speaking box книги) + мова порівняння; вправа «яку фразу сказати»", "10 хв"],
     ["2", "Слова Unit 7: лист від клієнтки, 12 пропусків + коротка розмова", "8 хв"], ["3A–3B", "Кейс і таблиця трьох пропозицій, підготовка: порівнюємо", "12 хв"],
     ["4", "Презентація онлайн (слайди із завданнями) — 5 хв + швидкий фідбек", "12 хв"], ["5", "Q&A: ви — клієнтка Olena, тиснете запитаннями", "10 хв"], ["—", "Підсумок, сірі слова, самооцінка, домашка", "8 хв"]])) +
 blk("tgt", "Матеріали", ul(["Урок: <a href='%slesson.html' target='_blank'>lesson.html</a> (7 екранів)" % BASE, "Слайди: <a href='%spresent.html' target='_blank'>present.html</a>. Павло шерить екран із цією сторінкою. Під слайдом: завдання, Compare, слова, 💡 Example. Нижче — ваш чек-лист слів Unit 7 і список запитань Q&A.",
                         "Компанії вигадані: BrightCode (Павло), GreenBox (клієнт), AppNova (дешево на папері, приховані платежі), WebGiant (найбільший, найдорожчий, найповільніший)."])))
S = []
S.append(("s1", "1A Фрази", step("s1", "1A · Phrases for presenting", "5 хв",
 "<p>Спершу знайомимося з фразами, які будуть потрібні: Speaking box книги <i>Presenting</i> (7.4) + мова порівняння з 7.1–7.3. Павло слухає 🔊 і повторює.</p>",
 ["Today you’re going to give a presentation to win a big contract.", "First, let’s look at the phrases. Listen and repeat.", "Which phrases do you remember from last lesson?"],
 ul(["Ідіть блоками: Starting → Aim and plan → Main part → Online → Ending.", "Після кожного блоку питайте: <i>When do you say this? At the start or at the end?</i>", "Блок Comparing: попросіть одразу скласти 1 речення про реальні компанії (Kyivstar vs lifecell, Zoom vs Meet)."]),
 ["What’s the difference between <i>cheaper</i> and <i>the cheapest</i>?", "How do you start a presentation in Ukrainian? And in English?"], "<p>Ключа немає — це введення.</p>")))
S.append(("s2", "1B", step("s2", "1B · Which phrase?", "5 хв",
 "<p>Перевіряємо, чи Павло знає функцію кожної фрази. Після вибору він каже фразу з кінцем про свою компанію.</p>",
 ["Which phrase do you use when you want to change the topic?", "Now finish the phrase about your company."],
 ul(["Студент обирає з випадного списку, натискає Check.", "Друге коло — усно: <i>We’re based in … We provide a range of …</i> про свою реальну роботу."]), [],
 "<p>1 Thank you for attending this presentation. · 2 The aim of today’s presentation is to … · 3 Let’s move on to … · 4 As you can see on this slide, … · 5 We’re based in … · 6 Does anyone have any questions? · 7 We provide a range of … · 8 We offer the best value for money. · 9 There’s an additional fee for … · 10 So, let’s start with …</p>")))
S.append(("s3", "2 Слова", step("s3", "2 · Unit 7 words: the client’s email", "8 хв",
 "<p>Лист від клієнтки Olena — це і повторення слів 7.2–7.4, і вхід у кейс. Слова в рамці навмисно не в порядку словника.</p>",
 ["You got an email from the client. Read it and choose the missing words.", "Which words are from 7.2? Which are from 7.3?"],
 ul(["Після Check: <i>What is an early termination fee? What is the small print?</i> — нехай пояснить англійською простими словами.", "Розмова в кінці екрана: що важливо для його компанії при виборі провайдера."]),
 ["Have you ever paid a hidden fee?", "Do you read the small print?"],
 "<p>additional · small print · fee · monthly · termination · provider · value · coverage · payment · trial · aim · attending</p>")))
S.append(("s4", "3A Кейс", step("s4", "3A · The case", "4 хв",
 "<p>Павло розуміє ситуацію і таблицю. Важливо, щоб він побачив пастку: AppNova дешева лише на папері.</p>",
 ["You are Pavlo from BrightCode. GreenBox wants an app, an online shop and a payment system.", "Look at the table. What do you notice?"],
 ul(["Читає вголос кейс, ви перепитуєте деталі: <i>What’s their budget? When do they need it?</i>", "Не підказуйте про приховані платежі — нехай знайде сам на 3B."]),
 ["Which company would you choose if you were GreenBox?"], "<p>Бюджет ~€40,000 · перша версія за 10 тижнів (до весняного розпродажу).</p>")))
S.append(("s5", "3B Порівняння", step("s5", "3B · Prepare: compare", "8 хв",
 "<p>Підготовка аргументів. Тут уся граматика юніту: comparatives + superlatives + fees.</p>",
 ["Let’s compare the offers. Which company looks the cheapest?", "Is it really the cheapest? Let’s count."],
 ul(["Порахуйте разом AppNova за рік: 29,000 + 6,000 + 900×12 = <b>€45,800</b>.", "Вимагайте повні речення: <i>AppNova is cheaper than BrightCode, but …</i>", "Пункт 5 (слабке місце) — найважливіший для Q&A: <i>We aren’t the biggest, but …</i>"]),
 ["Is the biggest company always the best?", "What is more important for GreenBox: price or speed?"],
 "<p>Див. кнопку Show possible answers на екрані: AppNova €45,800 за перший рік; BrightCode найшвидша (8 тижнів); WebGiant не встигне (16 тижнів); аргументи — best value for money, the fastest, the most satisfied customers.</p>")))
S.append(("s6", "4 Презентація", step("s6", "4 · The presentation (5 min)", "12 хв",
 "<p>Павло шерить екран (present.html) і веде 9 слайдів. Сценарію немає: під кожним слайдом — завдання, що порівняти, які слова вжити. Ви слухаєте як клієнтка і ведете чек-лист.</p>",
 ["Please share your screen. Can I see your slides?", "You have five minutes. I’m Olena from GreenBox. Go ahead!"],
 ul(["<b>Ваша роль:</b> Olena Bondar, Head of Digital у GreenBox. Під час презентації <b>не перебивайте</b> — лише кивайте, нотуйте помилки.",
     "Клікайте слова в чек-листі під слайдами, коли Павло їх вживає. Лічильник покаже, скільки слів юніту прозвучало.",
     "Якщо Павло мовчить понад 10 секунд — скажіть: <i>Click 💡 Example, read it, then say it in your own words.</i>",
     "Після презентації — 2 хв фідбеку: 2 речі добре, 1 виправити (найчастіше: <i>more cheaper</i>, <i>the most fast</i>, <i>include</i> без -s)."]),
 ["Which slide was the easiest? Which was the most difficult?"],
 tbl([["<b>Слайд</b>", "<b>Що має прозвучати (орієнтир)</b>"], ["1 Title", "Good morning, everyone. My name is Pavlo, I’m a project manager at BrightCode. Thank you for attending."],
      ["2 Agenda", "The aim of today’s presentation is to … First … Then … Finally, a question and answer session."],
      ["3 About us", "We’re based in Kyiv … We aren’t the biggest provider, but we have more experience than AppNova."],
      ["4 Services", "Let’s move on to … We provide a range of e-commerce services … payment system … secure database."],
      ["5 Price", "As you can see, AppNova looks the cheapest, WebGiant is the most expensive. Our fee is fixed."],
      ["6 What’s included", "Our fee includes … AppNova charges an additional fee … a monthly fee … the small print … early termination fee → best value for money."],
      ["7 Speed & quality", "We are the fastest … AppNova is slower … WebGiant can’t finish before the sale … the most satisfied customers."],
      ["8 Why us", "the best value for money · the fastest · the most satisfied customers · guarantee"], ["9 End", "That’s the end of my presentation. Thank you for listening. Any questions?"]]))))
QAT = [("Why should we pay more than AppNova’s price?", "Our fee includes the payment system and support. AppNova has additional fees, so in the first year they are more expensive.", "«Because we are better» без цифр", "<i>Better how? Show me the numbers.</i>"),
       ("WebGiant is the biggest provider in Europe. Why are you better?", "They are the biggest, but we are faster and cheaper. They can’t finish before the sale.", "погоджується, що WebGiant кращі", "<i>So maybe we should choose them?</i> — дайте шанс виправитись"),
       ("What does your fee include exactly?", "The fee includes design, the app, the online shop, the payment system and six months of support.", "забуває support або payment system", "<i>And support? Do we pay extra for support?</i>"),
       ("Are there any hidden fees?", "No, there are no hidden fees. It’s a fixed fee.", "«No» і все", "<i>What about after six months? How much is support then?</i> (хай імпровізує: a monthly fee of …)"),
       ("What happens if you are late?", "We give a guarantee: if we are late, support is free for one more year.", "не знає", "підкажіть слово <i>guarantee</i> з 7.2"),
       ("Can we cancel the contract?", "Yes, you can cancel for free in the first 14 days. There is no cancellation fee.", "«Yes» без деталей", "<i>Is there a cancellation fee? What about AppNova?</i>"),
       ("Can you give us a free trial or a discount?", "We can give you a free trial of the AI chat assistant for two weeks.", "одразу дає знижку 30%", "<i>Wow, why was the price so high then?</i> 😄 — урок переговорів"),
       ("Who will be our contact person?", "I will be your contact person. I’ll send you the details in an email.", "—", "Завершіть: <i>Thank you, Pavlo. We’ll let you know on Monday.</i>")]
S.append(("s7", "5 Q&A", step("s7", "5 · Question and answer session — ви клієнтка", "10 хв",
 "<p>Найживіша частина: ви тиснете як справжній клієнт, Павло захищає пропозицію. Мета — щоб він використав <b>сірі слова</b> з чек-листа.</p>",
 ["Thank you, Pavlo. I have some questions.", "Let’s start with the price."],
 ul(["Ставте запитання по одному (список є і в уроці, і під слайдами). Не ставте всі 8 — оберіть 5–6, залежно від часу.",
     "Перед запитанням подивіться на чек-лист: якщо сіре <i>hidden fee</i> — питайте №4; сіре <i>guarantee</i> — №5.",
     "Тримайте роль: будьте ввічливо-скептичною. Посміхайтесь, але не погоджуйтесь одразу."]) +
 "<p><b>Якщо він каже X → ви кажете Y</b></p>" + tbl([["<b>Ви питаєте</b>", "<b>Хороша відповідь</b>", "<b>Якщо він…</b>", "<b>…ви кажете</b>"]] + [[a, b, c, d] for a, b, c, d in QAT]),
 ["Which question was the most difficult for you?"], "<p>Наприкінці: Павло записує найкращу відповідь на найважче запитання (поле на екрані), самооцінка, Send to my teacher.</p>")))
open(os.path.join(OUT, "7-5.html"), "w").write(pagef("7.5", "Business workshop: The big contract", BASE + "lesson.html", overview, S).replace("студентці", "студенту"))
print("ok", OUT)
