"""Business Partner A2+ — Teacher's Book (Ukrainian) for 1.2 SPEAKING: business situations.
For each situation: хто ти / хто вона, твоя мета й таємні умови, перша фраза, приблизний діалог, «якщо вона скаже… → ти скажи…», як закінчити.
Usage: python3 build_a2p_teacher_speak_1-2.py OUTDIR  -> OUTDIR/1-2-speak.html
"""
import sys, os
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)

GEN = [
 "Ти завжди <b>Student B</b>: клієнтка, кейтеринг, асистент, менеджер майданчика. Лариса — <b>Student A</b>, у неї картка «You». Твої картки B видно лише у твоїй версії сторінки.",
 "Твоя головна задача — <b>не погоджуватися одразу</b>. Кожна ситуація триває 4–6 хвилин, поки вона не дійде до результату: ціни, рішення, дедлайну.",
 "Говори коротко, простими реченнями. Хай більше говорить вона: питай <i>Why? How much? When exactly?</i>",
 "Помилки не виправляй посеред розмови. Записуй 3–4 помилки на папірці й розбери їх після кожної ситуації за 1 хвилину.",
 "Після кожної ситуації вона пише в полі «Result», про що домовились. Це 30 секунд, потім наступна ситуація.",
 "План на 60 хв: ситуації 1–6 по 7–8 хв (розмова + розбір), лист (7) — вдома або в кінці уроку.",
]

SIT = [
 {"n": 1, "t": "Зустріч з клієнтом: вечірній захід", "who": "Ти — <b>Ana, HR-директорка юридичної фірми Vega Legal</b>. Вона — менеджерка агенції BCN Smart Events.",
  "goal": ["Отримати вечірній захід на 140 гостей (25 онлайн) у межах €8 000 за їжу й розваги.", "10 гостей — веганське меню, 4 — без глютену.",
           "CEO любить джаз, але човен (€90 з людини) тобі здається задорогим. Боїшся дощу на rooftop.", "Хай вона сама ставить питання й порівнює місця. Нічого не розповідай, поки не спитає."],
  "start": "Hi, thank you for meeting me. We have our conference in Barcelona on 14–15 May, and we need an evening event. Can you help us?",
  "dlg": [("L", "Yes, of course. How many guests do you expect?"), ("T", "About 140. And 25 people join online."), ("L", "OK. What is your budget?"),
          ("T", "About 8,000 euros for food and entertainment."), ("L", "Do you need special food?"), ("T", "Yes — 10 vegan and 4 gluten-free."),
          ("L", "We have three venues. The rooftop is the cheapest — 45 euros per person. The boat is the biggest, but it’s more expensive."),
          ("T", "Hmm. What happens if it rains on the rooftop?"), ("L", "We can put up a tent. / Then the boat is a better option."),
          ("T", "Our CEO loves jazz. Is there jazz on the rooftop?"), ("L", "No, there’s a DJ. The boat has a jazz band."), ("T", "But the boat is 90 euros per person. That’s 12,600 — too much!"),
          ("L", "How about the boat with a buffet? I can ask the caterer for a better price."), ("T", "OK, that sounds good. What’s the next step?"),
          ("L", "I’ll call the caterer and send you a summary by email."), ("T", "Perfect. Thank you!")],
  "if": [("рекомендує winery (там у неї знижка)", "<i>But the winery is only for 80 people. We are 140!</i> — хай шукає інше."),
         ("забула спитати бюджет", "Не кажи сама. Спитай: <i>How much is it all together?</i> Хай порахує й тоді спитає про бюджет."),
         ("одразу погоджується на все", "Додай проблему: <i>And 25 people are online — can they see the event?</i> (човен може стрімити)."),
         ("мовчить / не знає, що сказати", "Підкажи питанням: <i>Which venue is the best for 140 people? Why?</i>")],
  "end": "Вона підсумовує: <i>So, we agree on …</i> і називає наступний крок. У нотатках: venue, date, guests, food, budget, next step."},
 {"n": 2, "t": "Торг з кейтерингом", "who": "Ти — <b>кейтеринг на човні</b> (менеджер Marc). Вона — event-менеджерка, яка хоче знизити ціну.",
  "goal": ["Почни з €95 за людину (€13 300 за 140). Потім можна €85.", "Твій мінімум — <b>€62</b>, і лише за умов: буфет, вино 2 години, джаз-<b>дует</b> замість бенду.",
           "Наприкінці попроси депозит 30% до 1 травня."],
  "start": "Hello, Marc speaking. You got our quote, right? 95 euros per person.",
  "dlg": [("L", "Yes, thank you. But our budget is 8,000 euros. 95 euros is too expensive for us."), ("T", "I understand. But the price includes three courses, drinks and the jazz band."),
          ("L", "What if we have a buffet?"), ("T", "With a buffet it’s 85 euros."), ("L", "That’s still too much. Can you do it for 55?"), ("T", "No, sorry, 55 is impossible. Maybe 70."),
          ("L", "And if we have wine for two hours only, and a smaller band?"), ("T", "OK… buffet, wine for two hours and a jazz duo — 62 euros. That’s my best price."),
          ("L", "62 euros… OK, it’s a deal."), ("T", "Great. I need a 30% deposit by the 1st of May."), ("L", "No problem. I’ll send it next week.")],
  "if": [("одразу погоджується на 85 чи 95", "Запитай: <i>Are you sure? That’s over your budget, right?</i> — нагадай про €8 000."),
         ("просить дуже низьку ціну (€40)", "<i>Sorry, that’s impossible. The food costs more than that.</i>"),
         ("не пропонує, що прибрати", "Підкажи: <i>What can we change? Maybe the menu or the music?</i>")],
  "end": "Результат: €62 за людину; що входить (буфет, вино 2 год, дует); депозит 30% до 1 травня."},
 {"n": 3, "t": "Бриф асистента", "who": "Ти — <b>новий асистент</b>, трохи нервуєш. Вона — твоя керівниця, ставить задачі.",
  "goal": ["Постав 2–3 уточнювальні питання: <i>Which bus company? Who has the guest list? What if the streaming doesn’t work?</i>",
           "Скажи, що не встигнеш з бейджами до п’ятниці (у тебе тренінг). Хай вирішить, хто зробить або коли.",
           "Наприкінці повтори план <b>з однією помилкою</b>: наприклад, переплутай день. Вона має виправити."],
  "start": "Hi! I’m ready. What do I need to do for the event?",
  "dlg": [("L", "First, could you book the bus to the venue? The deadline is Friday."), ("T", "OK. Which bus company?"), ("L", "BCN Coaches. The number is in the email."),
          ("T", "Fine. What else?"), ("L", "Please send the guest list to the caterer and check the special menus — 10 vegan and 4 gluten-free."), ("T", "Who has the guest list?"),
          ("L", "I have it. I’ll send it to you today."), ("L", "And please test the streaming for the online guests next Tuesday."), ("T", "What if it doesn’t work?"), ("L", "Call me, and we’ll call the technician."),
          ("L", "And print the name badges by Friday."), ("T", "Sorry, I can’t do the badges by Friday — I’m on a training course on Thursday and Friday."),
          ("L", "OK, then by Monday."), ("T", "Let me check: I book the bus by Thursday, send the list…"), ("L", "No, not Thursday — Friday."), ("T", "Sorry — Friday. Got it!")],
  "if": [("дає задачі без дедлайнів", "Спитай: <i>When do you need it?</i>"), ("каже все дуже швидко", "<i>Sorry, can you say that again, slowly?</i>"),
         ("не помічає твою помилку", "Після розмови скажи: <i>Did you notice my mistake?</i> — і перевірте разом.")],
  "end": "Результат: 5 задач з дедлайнами (bus — Fri, guest list — today, menus, streaming test — Tue, badges — Mon)."},
 {"n": 4, "t": "Проблема з майданчиком", "who": "Ти — <b>менеджерка майданчика</b>. Вона телефонує, бо гостей стало 170, а не 140.",
  "goal": ["Варіант 1: сусідня тераса, +50 гостей, <b>€1 500</b>.", "Варіант 2: дві хвилі — 140 гостей з 19:00, ще 30 з 21:00 на вечірку.",
           "Потрібно ще 2 офіціанти (€400). Знижка 10%, якщо вона підтвердить сьогодні.", "У неї ліміт доплати €1 000. Будь привітна, але тримай ціну."],
  "start": "Good morning, this is the venue. How can I help you?",
  "dlg": [("L", "Hi. We have a problem. Our client now has 170 guests, not 140."), ("T", "Oh. Our maximum is 140 inside."), ("L", "What are our options?"),
          ("T", "We can open the terrace next door for 50 more people. It’s 1,500 euros."), ("L", "That’s more than our budget. Is there anything cheaper?"),
          ("T", "Or two sittings: 140 guests for dinner at 7, and 30 more people come at 9 for the party."), ("L", "How much is that?"), ("T", "You need two more staff — 400 euros."),
          ("L", "OK, the two sittings are better for us. Can you give us a discount?"), ("T", "10% if you confirm today."), ("L", "Great, let’s agree on that. I’ll confirm by email today.")],
  "if": [("одразу бере терасу за €1 500", "<i>Are you sure? You said your budget is 1,000.</i>"), ("не питає варіантів, а просить «зробіть щось»", "<i>What do you suggest?</i> — хай пропонує вона."),
         ("торгується за терасу", "Можна дати €1 300, але не менше.")],
  "end": "Результат: яке рішення, скільки доплата, до коли підтвердити."},
 {"n": 5, "t": "Скарга після заходу", "who": "Ти — <b>Ana, клієнтка</b> з ситуації 1, дзвониш наступного дня, незадоволена. Вона — агенція.",
  "goal": ["Скарги: вечеря запізнилась на 40 хвилин; онлайн-гостей не було чути 20 хвилин; бракувало веганських страв.",
           "Що було добре: місце й джаз — чудові.", "Ти хочеш повернути 20%. Погодься на 10% + безкоштовного фотографа наступного року, якщо вона професійна й спокійна."],
  "start": "Hello, it’s Ana from Vega Legal. I’m calling about last night. To be honest, I’m not happy.",
  "dlg": [("L", "I’m very sorry to hear that. Can you tell me exactly what happened?"), ("T", "Dinner was 40 minutes late. And our online guests couldn’t hear the speakers."),
          ("L", "I’m really sorry. The reason for the dinner was a problem in the kitchen. And the streaming — the microphone didn’t work for 20 minutes."),
          ("T", "Also, there weren’t enough vegan dishes."), ("L", "You’re right, that’s our mistake."), ("T", "I think we should pay 20% less."),
          ("L", "I understand. What we can do is give you 10% back, and a free photographer for your next event."), ("T", "Hmm… OK. And the venue and the jazz were great, by the way."),
          ("L", "Thank you! Can we work together next year?"), ("T", "Maybe. Send me your offer in January.")],
  "if": [("одразу пропонує 20% або більше", "Прийми, але потім скажи: <i>Wow, that’s generous!</i> Після розмови обговоріть, що можна було торгуватися."),
         ("виправдовується або звинувачує інших", "<i>I don’t need excuses. What can you do for us?</i>"), ("забуває вибачитися", "<i>Aren’t you going to say sorry?</i>")],
  "end": "Результат: що пішло не так, яка компенсація, наступний крок (оферта в січні)."},
 {"n": 6, "t": "Її власний бізнес", "who": "Тепер <b>клієнтка — вона</b>, про свою реальну фірму. Ти — <b>event-агенція</b>.",
  "goal": ["Хай вона говорить про <b>реальний</b> бізнес: хто вони, кого запрошують, навіщо захід.",
           "Питання агенції: <i>Why this event now? Who are the guests? What does success look like? Who makes the decision? Budget? Date? In person or online?</i>",
           "Заперечи в одному: замалий бюджет або закороткий термін.", "Наприкінці переказ її брифу в 3 реченнях з однією неточністю — хай виправить."],
  "start": "Hello! Thank you for contacting us. Tell me about your company and the event you want.",
  "dlg": [("L", "We are an accounting company in … We have about … clients."), ("T", "And what kind of event do you want?"), ("L", "A seminar about the new tax rules for our clients, and a small dinner after it."),
          ("T", "Why now?"), ("L", "Because the rules change in January and our clients have a lot of questions."), ("T", "How many guests?"), ("L", "About 40."),
          ("T", "And your budget?"), ("L", "About 2,000 euros."), ("T", "Hmm, for 40 people with dinner, that’s a small budget. Maybe without dinner — just coffee?"),
          ("L", "No, the dinner is important for us — we want to get on with our clients. Maybe a cheaper restaurant?"), ("T", "OK. What does success look like for you?"),
          ("L", "Clients understand the new rules and stay with us next year."), ("T", "So: 30 guests, a seminar in December…"), ("L", "No, 40 guests, and in January.")],
  "if": [("не знає, що відповісти про бізнес", "Спрости: <i>What does your company do? Who are your clients?</i>"),
         ("дає дуже короткі відповіді", "<i>Can you tell me more?</i> / <i>Why is that important?</i>"), ("погоджується прибрати вечерю", "Спитай: <i>Are you sure? Why did you want the dinner?</i>")],
  "end": "Результат: її бриф (мета, гості, дата, формат, бюджет, що найважливіше) і прохання надіслати 2 варіанти до певної дати."},
]

def li(xs): return "<ul>%s</ul>" % "".join("<li>%s</li>" % x for x in xs)
def sec(s):
    dl = "".join('<p class="%s"><b>%s</b> %s</p>' % ("t" if w == "T" else "l", "Ти:" if w == "T" else "Лариса:", t) for w, t in s["dlg"])
    iff = "".join('<tr><td>%s</td><td>%s</td></tr>' % x for x in s["if"])
    return ('<section id="s%d" class="sec"><h2>%d · %s</h2>' % (s["n"], s["n"], s["t"]) +
            '<div class="blk who"><h3>Хто є хто</h3><p>%s</p></div>' % s["who"] +
            '<div class="blk goal"><h3>Твоя задача і таємні умови</h3>%s</div>' % li(s["goal"]) +
            '<div class="blk start"><h3>Почни так (скажи)</h3><p class="say">🗣 <i>%s</i></p></div>' % s["start"] +
            '<div class="blk dlg"><h3>Приблизний діалог (може йти інакше, це орієнтир)</h3>%s</div>' % dl +
            '<div class="blk iff"><h3>Якщо вона… → ти…</h3><table>%s</table></div>' % iff +
            '<div class="blk end"><h3>Як закінчити</h3><p>%s</p></div></section>' % s["end"])

nav = '<button data-s="s0" class="on">Як вести</button>' + "".join('<button data-s="s%d">%d</button>' % (s["n"], s["n"]) for s in SIT)
body = ('<section id="s0" class="sec on"><h2>Як вести розмовний урок 1.2</h2><div class="blk goal"><h3>Головне</h3>%s</div>'
        '<div class="blk who"><h3>Порядок</h3><table><tr><th>Ситуація</th><th>Ти граєш</th><th>Чого вона має досягти</th></tr>%s</table></div></section>' %
        (li(GEN), "".join("<tr><td>%d · %s</td><td>%s</td><td>%s</td></tr>" % (s["n"], s["t"], s["who"].split("—")[0].replace("Ти — ", "").replace("Тепер ", ""), s["end"].replace("Результат: ", "")) for s in SIT))) + "".join(sec(s) for s in SIT)

HTML = """<!DOCTYPE html><html lang="uk"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Teacher’s Book · A2+ 1.2 Speaking: business situations</title>
<link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>*{box-sizing:border-box}body{margin:0;font-family:"Fira Sans",system-ui,sans-serif;font-weight:300;color:#231f20;background:#fff;font-size:16.5px;line-height:1.5}
header{display:flex;border-bottom:3px solid #3fa9ad}header .n{background:linear-gradient(120deg,#2b8185,#5cc1c4);color:#fff;font-weight:500;font-size:32px;padding:10px 22px}
header h1{margin:0;align-self:center;padding-left:16px;font-weight:500;font-size:26px;color:#4d4d4f}header .tag{margin-left:auto;align-self:center;margin-right:16px;background:#f2b631;color:#231f20;font-weight:600;font-size:12px;padding:5px 10px;border-radius:4px}
.wrap{max-width:980px;margin:0 auto;padding:12px 20px 40px}.top a{color:#2b8185;text-decoration:none;font-weight:500;font-size:15px;margin-right:16px}
nav{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0}nav button{border:1.5px solid #3fa9ad;background:#fff;color:#2b8185;border-radius:20px;padding:6px 16px;font:500 15px "Fira Sans";cursor:pointer}nav button.on{background:#3fa9ad;color:#fff}
.sec{display:none}.sec.on{display:block}h2{font-weight:500;color:#2b8185;font-size:22px;margin:10px 0}
.blk{border-left:5px solid #3fa9ad;background:#e6f4f4;border-radius:6px;padding:8px 16px;margin:10px 0}.blk h3{margin:2px 0 6px;font-size:13px;text-transform:uppercase;letter-spacing:.4px;color:#2b8185;font-weight:600}
.blk.goal{background:#fff8e6;border-color:#f2b631}.blk.goal h3{color:#a07a10}.blk.start{background:#fff;border:1px solid #d5d6d7;border-left:5px solid #3fa9ad}
.blk.dlg{background:#fff;border:1px solid #d5d6d7;border-left:5px solid #8e5bd8}.blk.dlg h3{color:#6b3fb0}.dlg p{margin:4px 0}.dlg p.t{color:#6b3fb0}.dlg p.l{padding-left:22px}
.blk.iff{background:#fdf0f4;border-color:#c4127a}.blk.iff h3{color:#a00f64}.blk.end{background:#eef7e6;border-color:#5a9e2f}.blk.end h3{color:#3f7a1c}
table{border-collapse:collapse;width:100%;font-size:15px}td,th{border:1px solid #ddd;padding:6px 10px;vertical-align:top;text-align:left;background:#fff}th{background:#f3f4f6;font-weight:500}
.blk ul{margin:4px 0;padding-left:20px}.say{font-size:17px}footer{text-align:center;font-size:12px;color:#77787b;margin:30px 0}</style></head><body>
<header><div class="n">1.2</div><h1>Speaking: business situations</h1><div class="tag">TEACHER’S BOOK</div></header>
<div class="wrap"><div class="top"><a href="index.html">← Teacher’s Book: зміст</a><a href="../lessons/1-2/all/speak.html">📄 Сторінка уроку (з картками B)</a></div>
<nav>__NAV__</nav>__BODY__</div><footer>Valentyna Hordiienko · Middle Learning Architect</footer>
<script>document.querySelectorAll("nav button").forEach(b=>b.onclick=()=>{document.querySelectorAll("nav button,.sec").forEach(x=>x.classList.remove("on"));b.classList.add("on");document.getElementById(b.dataset.s).classList.add("on");scrollTo(0,0)})</script></body></html>"""
open(os.path.join(OUT, "1-2-speak.html"), "w").write(HTML.replace("__NAV__", nav).replace("__BODY__", body))
print("ok", OUT)
