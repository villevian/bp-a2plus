"""Business Partner B1 — Teacher's Book pages (Ukrainian) for 1.1, 4.2–4.5 + index.
Usage: python3 build_b1_teacher.py OUTDIR   -> OUTDIR/index.html, 4-2.html, 4-3.html
Each step: what & why (сенс), how to start (teacher's words in English), how to run, extra questions, answers.
"""
import sys, os
OUT = sys.argv[1]; os.makedirs(OUT, exist_ok=True)
ACC, ACC2, DARK = "#e8894a", "#fbeadb", "#c4642a"

def ul(xs): return "<ul>" + "".join("<li>%s</li>" % x for x in xs) + "</ul>"
def blk(cls, t, c): return '<div class="blk %s"><h3>%s</h3>%s</div>' % (cls, t, c)
def say(xs): return '<div class="say">' + "".join("<p>🗣 <i>%s</i></p>" % x for x in xs) + "</div>"
def step(sid, title, time, sense, start, run, extra, answers, note=""):
    h = '<section id="%s" class="sec"><div class="bsec">%s <span class="time">⏱ %s</span></div>' % (sid, title, time)
    h += blk("aim", "Сенс вправи — що робимо і навіщо", sense)
    h += blk("start", "Як почати (скажіть студентці)", say(start))
    h += blk("run", "Як вести", run)
    if extra: h += blk("tgt", "Додаткові питання", ul(extra))
    if answers: h += blk("ans", "Відповіді", answers)
    if note: h += blk("watch", "На що звернути увагу", note)
    return h + "</section>"
def vids(vs):
    return "".join('<div class="vrow"><b>%s</b> %s · <a href="https://www.youtube.com/watch?v=%s" target="_blank">▶ YouTube</a> <span class="d">%s</span></div>' % (n, t, y, d) for n, t, y, d in vs)

def pagef(num, title, lesson_url, overview, steps):
    nav = '<button data-s="s0" class="on">Огляд</button>' + "".join('<button data-s="%s">%s</button>' % (sid, lab) for sid, lab, _ in steps)
    body = '<section id="s0" class="sec on">%s</section>' % overview + "".join(h for _, _, h in steps)
    return TPL.replace("__NUM__", num).replace("__TITLE__", title).replace("__URL__", lesson_url).replace("__NAV__", nav).replace("__BODY__", body)

TPL = """<!DOCTYPE html><html lang="uk"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>__NUM__ __TITLE__ — Teacher’s Book</title>
<link href="https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&display=swap" rel="stylesheet"><style>
*{box-sizing:border-box}body{margin:0;font-family:"Fira Sans",system-ui,sans-serif;color:#231f20;background:#fff;font-weight:300;line-height:1.5;font-size:16.5px}
header{display:flex;border-bottom:3px solid ACC}header .n{background:linear-gradient(120deg,DARK,#f2a66e);color:#fff;font-weight:500;font-size:34px;padding:12px 22px}
header h1{margin:0;align-self:center;padding-left:18px;font-weight:500;font-size:26px;color:#4d4d4f}header .t{margin-left:auto;align-self:center;margin-right:16px;background:#f2b631;color:#3b2c00;font-weight:600;font-size:13px;padding:6px 12px;border-radius:4px}
.top{display:flex;gap:16px;padding:12px 22px 0;font-size:15px;flex-wrap:wrap}.top a{color:DARK;font-weight:500;text-decoration:none}
nav{display:flex;gap:6px;padding:12px 22px 0;flex-wrap:wrap}nav button{font:inherit;font-weight:500;min-width:44px;border:1.5px solid ACC;background:#fff;color:DARK;padding:5px 12px;border-radius:20px;cursor:pointer}nav button.on{background:ACC;color:#fff}
main{max-width:1000px;margin:0 auto;padding:16px 22px 40px}.sec{display:none}.sec.on{display:block}
.bsec{font-weight:600;font-size:21px;color:#77787b;margin:4px 0 14px}.time{font-size:14px;font-weight:500;color:DARK;background:ACC2;border-radius:12px;padding:2px 10px;margin-left:8px}
.blk{border-left:5px solid ACC;background:#f3f3f4;padding:10px 16px;margin:0 0 12px;border-radius:0 4px 4px 0}.blk h3{margin:0 0 6px;font-size:14.5px;font-weight:600;text-transform:uppercase;letter-spacing:.4px;color:#4d4d4f}
.blk p{margin:4px 0 8px}.blk ul,.blk ol{margin:4px 0 6px;padding-left:22px}.blk li{margin:3px 0}.blk h4{margin:10px 0 4px;color:DARK;font-size:15px}
.blk.aim{background:ACC2}.blk.big{background:#fff6ec;border-color:#f2b631}.blk.start{background:#e3eef8;border-color:#1f6f8b}.blk.run{background:#fff;border:1px solid #d5d6d7;border-left:5px solid ACC}
.blk.tgt{background:#fbeef5;border-color:#c4127a}.blk.ans{background:#eef6d3;border-color:#5c9e2f}.blk.watch{background:#fdf7e6;border-color:#f2b631}
.say p{margin:3px 0;color:#1f4f6b}table.tt{border-collapse:collapse;width:100%;background:#fff;font-size:15px}table.tt td,table.tt th{border:1px solid #ddd;padding:5px 8px;text-align:left;vertical-align:top}table.tt th{background:ACC2;font-weight:500}
.vrow{background:#fff;border:1px solid #eee;border-radius:6px;padding:6px 10px;margin:4px 0}.vrow a{color:#c2185b;font-weight:500}.vrow .d{color:#77787b;font-size:14px;display:block}
.chips span{display:inline-block;background:#fff;border:1px solid #f0c6dc;border-radius:12px;padding:2px 10px;margin:2px;font-size:14.5px}
footer{max-width:1000px;margin:0 auto;padding:0 22px 30px;font-size:12px;color:#77787b}</style></head><body>
<header><div class="n">__NUM__</div><h1>__TITLE__</h1><div class="t">TEACHER’S BOOK</div></header>
<div class="top"><a href="index.html">← Teacher’s Book: зміст</a><a href="__URL__" target="_blank">📄 Відкрити урок студента</a></div>
<nav>__NAV__</nav><main>__BODY__</main><footer>Valentyna Hordiienko · Middle Learning Architect</footer>
<script>document.querySelectorAll("nav button").forEach(b=>b.onclick=()=>{document.querySelectorAll("nav button,.sec").forEach(x=>x.classList.remove("on"));b.classList.add("on");document.getElementById(b.dataset.s).classList.add("on");scrollTo(0,0)});</script></body></html>"""
TPL = TPL.replace("ACC2", ACC2).replace("ACC", ACC).replace("DARK", DARK)

# ======================= 4.2 =======================
O42 = ('<div class="bsec">Огляд уроку</div>' +
 blk("big", "Сенс уроку — яку ідею розкриваємо",
  "<p><b>«Out of sight, out of mind» — кого не видно, того не помічають.</b> Шість років після переходу на віддалену роботу офіс повертається, але не тому, що вдома погано працюється. "
  "Стаття показує п’ять реальних «болів» віддаленої роботи: самотність, невидимість для керівника (менше підвищень), робота без кінця, нескінченні дзвінки, «ти ж удома — значить вільна». "
  "Висновок автора — не «додому чи в офіс», а <b>розумний мікс</b>.</p>"
  "<p><b>Навіщо це Каті:</b> вона працює в IT/PM-середовищі, де Zoom, Slack, Notion і Jira — щоденна реальність. Тема дає їй мову, щоб говорити про свою команду, правила гібридної роботи і про те, як зробити віддалених людей «видимими».</p>"
  "<p><b>Граматичний сенс:</b> пасив тут не «для галочки». У робочих правилах (Notion, Slack-оголошення) важливо <i>що зроблено</i>, а не <i>хто</i>: <i>Tasks are created in Jira. Lunch is paid for by the company.</i> "
  "Саме тому пасив — природна мова регламентів, процесів і новин про компанії.</p>") +
 blk("aim", "Outcome", "<p>Студентка вживає Present Simple і Past Simple passive в усному та письмовому мовленні: описує правила команди, процеси (хто що робить у Jira/Slack), факти про компанії, пише Slack-повідомлення з пасивом.</p>") +
 blk("run", "Де ми з Катею зараз", ul([
  "<b>Зроблено на минулому уроці</b> (внесено в базу як її відповіді): 1.1 Jira/Slack/Notion/Zoom; 1.2 її список проблем; 2B заголовки 1C 2E 3D 4A 5B; 5A/B; 6 — усі 12 форм (виправлено <i>is payed → is paid for</i>, <i>arn’t → aren’t</i>).",
  "<b>Не зроблено:</b> 3 (питання до статті), 7 (факти про IT-компанії), 8 (Slack-повідомлення).",
  "<b>Сьогодні:</b> повторення лексики + пасиву і новий матеріал — <b>causative have</b> (сторінка <b>Extra</b>). Можна почати з 7A/B як розминки на пасив, потім Extra 1 → 2 → 3 → 4, а 8 дати додому."])) +
 blk("tgt", "Таймінг (≈ 60–80 хв)", '<table class="tt"><tr><th>Етап</th><th>Що</th><th>Час</th></tr>' + "".join("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % r for r in [
  ("1", "Lead-in: інструменти і проблеми віддаленої роботи", "8 хв"), ("2–3", "Читання: заголовки + питання", "15 хв"), ("4", "Обговорення", "7 хв"),
  ("5–6", "Граматика: пасив, Notion-угода", "12 хв"), ("7", "Факти про компанії (пасив) + T/F", "8 хв"), ("8", "Slack-повідомлення", "10 хв / вдома"),
  ("Extra", "Повторення лексики, пасиву + have something done", "25–30 хв")]) + "</table>") +
 blk("watch", "Типові помилки Каті", ul(["Неправильна форма V3: <i>payed</i> → <b>paid</b>; правопис <i>arn’t</i> → <b>aren’t</b>.", "Пасив vs актив у 6: <i>They <b>last</b></i>, <i>Everyone <b>updates</b></i>, <i>who <b>moves</b></i>, <i>we <b>meet</b></i> — тут актив, бо є хто діє.",
  "Плутанина -ing: <i>lasted</i> (Past Simple) vs <i>lasting</i>; герундій як підмет: <i>Smoking is dangerous</i>, після like: <i>I like reading</i> — це її нотатки з уроку, варто повторити."])))
S42 = []
S42.append(("s1", "1", step("s1", "1 · Lead-in", "8 хв",
 "<p>Активуємо знайому лексику інструментів (Zoom, Notion, Slack, Jira) і через опис інструментів одразу «підсвічуємо» пасив: <i>tasks <b>are created, assigned</b> and <b>moved</b></i>. Потім — особистий досвід: які проблеми віддаленої роботи вона знає. Пункт 3 — прогноз до статті: так читання стає перевіркою її гіпотез.</p>",
 ["Which of these tools do you use every day? Which one could you live without?", "What problems do people have when they work from home? Let’s make a list.", "The article is called ‘Who wants to go back to the office?’ What five problems do you expect to read about?"],
 ul(["1.1 — швидко, 1 хв.", "1.2 — список у полі на сторінці; доповнюйте її ідеї своїми (loneliness, burnout, too many meetings, invisible to managers).", "1.3 — нехай обере 5 і коротко пояснить <i>why</i>."]),
 ["Which tool causes the most stress in your team? Why?", "Do you prefer async communication (Slack) or calls (Zoom)?", "Is your team distributed? In how many cities/countries?"],
 "<p>a Jira · b Slack · c Notion · d Zoom</p><p><b>Відповідь Каті на 1.2</b> (у базі): impossible to work at home (chores, people); neurodivergency — difficulty working with other people around; low concentration; not predictable, unfinished working day.</p>")))
S42.append(("s2", "2", step("s2", "2 · Reading", "8 хв",
 "<p>Skimming: швидко зрозуміти структуру статті і перевірити прогнози. Заголовки 2B — це «ключ» до кожної проблеми, далі вони стануть опорою для обговорення.</p>",
 ["Read the article quickly — 2 minutes. Which of your predictions are there?", "Now match the headings with the sections. What words helped you?"],
 ul(["Обмежте час — це читання на загальне розуміння.", "Після 2B попросіть назвати <b>слово-підказку</b> в кожній секції: loneliness → <i>Alone at the desk</i>; promoted less often → <i>Out of sight</i>; 10 p.m. → <i>never closes</i>; seven meetings → <i>Back-to-back calls</i>; day off → <i>You’re at home…</i>"]),
 ["Which problem surprised you most?", "Which problem is NOT true for your team?"],
 "<p>1 C · 2 E · 3 D · 4 A · 5 B (Катя вже зробила правильно)</p>")))
S42.append(("s3", "3", step("s3", "3 · Reading for detail", "8–10 хв",
 "<p>Читання на деталі: цифри, причини, позиція автора. Питання 8 вчить бачити <b>позицію автора</b> — важлива навичка для статей і звітів.</p>",
 ["Let’s read again more carefully. Answer the questions — you can use the text."],
 ul(["Студентка пише короткі відповіді в полях; кнопка <i>Show answer</i> — для самоперевірки.", "Звертайте увагу на пасив у тексті: <i>are promoted, was chosen, are sent, are created, is added, was invited, are covered</i> — попросіть знайти 5 пасивів."]),
 ["What could Marta do to be more visible?", "Who should pay for electricity and heating — the company or the worker?", "Has your company had the ‘back to the office’ debate?"],
 ol_html := "<ol><li>b</li><li>≈3.2 days a week in the office (up from 2.7 in 2024); only 4% of US workers want the office full-time</li><li>younger employees — still building professional networks</li><li>the new team lead was in the office every day; nobody saw her results</li><li>they feel guilty if they don’t answer</li><li>managers — worried about losing touch with their teams</li><li>that they have the day off</li><li>neither completely — a smart mix of home and office</li></ol>")))
S42.append(("s4", "4", step("s4", "4 · Speaking", "7 хв",
 "<p>Перенести статтю на її реальність: її команда, її роль PM. Питання 2 — практичне: що вона як PM може зробити (demo days, public kudos в Slack, visible Jira boards, 1:1s).</p>",
 ["Which of the five problems is the biggest for you or your team?", "As a project manager, what can you do to make remote people more visible?"],
 ul(["Дайте 30 сек подумати, потім вільна розмова.", "Записуйте її помилки на пасив — розберіть після."]),
 ["How many meetings a day are too many for you?", "Do you answer messages after 7 p.m.? Why?", "What is your ideal hybrid schedule?"], "")))
S42.append(("s5", "5", step("s5", "5 · Grammar", "5 хв",
 "<p>Помітити форму пасиву в тексті й назвати час. Головне — <b>be + V3</b>, час показує be (are/were), а <b>by</b> — лише якщо важливо, хто.</p>",
 ["Look at the words in bold. Is it active or passive? What tense?", "Who creates the meetings? How do we show it?"],
 ul(["Намалюйте формулу: <b>am/is/are + V3</b> (зараз/завжди) · <b>was/were + V3</b> (минуле).", "Катя на уроці записала <i>be + Ved/3rd</i> — це те саме, закріпіть."]),
 ["Why do we say ‘Tasks are assigned in Jira’ and not ‘Somebody assigns tasks’?", "When is ‘by’ not needed?"],
 "<p>A: 1 Present Simple passive · 2 Past Simple passive. B: <b>by</b></p>")))
S42.append(("s6", "6", step("s6", "6 · Grammar: Notion agreement", "7 хв",
 "<p>Робочий контекст: «угода команди» в Notion. Сенс — вибір <b>актив чи пасив</b>: якщо є хто діє (they, everyone, who, we) — актив; якщо важливий процес — пасив.</p>",
 ["Here is a hybrid working agreement in Notion. Active or passive? Look who does the action."],
 ul(["Вона вже зробила — перевірте швидко, розберіть помилки 3, 12.", "Попросіть додати 2 власні правила своєї команди в пасиві."]),
 ["Write two rules from your real team: e.g. ‘Code is reviewed by…’, ‘Retros are held…’"],
 "<p>1 are held · 2 last · 3 are not accepted · 4 are sent · 5 are not expected · 6 updates · 7 are created · 8 is assigned · 9 moves · 10 are planned · 11 meet · 12 is paid for</p>",
 "<p>У Каті: <i>is payed</i> → <b>is paid for</b> (неправильне дієслово pay–paid–paid і прийменник for залишається!); <i>arn’t</i> → <b>aren’t</b>.</p>")))
S42.append(("s7", "7", step("s7", "7 · Grammar: facts about IT companies", "8 хв",
 "<p>Пасив для фактів і історії компаній (заснована, куплена, написана). Плюс квіз T/F — мотивує, бо Катя знає ці інструменти.</p>",
 ["Let’s check how much you know about the tools you use. Complete the sentences — then guess: true or false?"],
 ul(["7A: одне речення — одна форма; звертайте увагу на <i>was first developed</i>, <i>are usually held</i> (прислівник між be і V3).", "7B: спочатку здогадки, потім перевірка."]),
 ["What other facts do you know about Atlassian, Google or Microsoft? Say them in the passive."],
 "<p>A: 1 was founded · 2 was first developed · 3 was bought · 4 is made · 5 was taken · 6 was bought · 7 are usually held · 8 was written</p><p>B: 1 T · 2 T · 3 F (bought by Salesforce) · 4 F (Atlassian is Australian) · 5 T · 6 T · 7 T · 8 T</p>")))
S42.append(("s8", "8", step("s8", "8 · Writing: Slack message", "10 хв / вдома",
 "<p>Перенести пасив у реальне письмо PM: оголошення в Slack про нові офісні дні. Альтернатива — емпатична відповідь колезі, якого «не видно».</p>",
 ["Imagine you are the PM. Write a Slack message to the team about the new hybrid policy. Use at least three passive forms."],
 ul(["На сторінці є лічильник слів і пасивних форм (60–80 слів, мін. 3 пасиви).", "Модельна відповідь — під кнопкою <i>Show model answer</i>.", "Якщо часу мало — дайте додому."]),
 ["What would you add for people who can’t come to the office?"],
 "<p>Модель: Hi team! … Tuesday, Wednesday and Thursday <b>are planned</b> as office days. Sprint planning and retros <b>are held</b> in person, and lunch <b>is paid for</b> by the company. … no meetings <b>are scheduled</b> after 4 p.m. The full calendar <b>was shared</b> in Notion yesterday…</p>")))
S42.append(("sx", "Extra", step("sx", "Extra · Повторення + have something done", "25–30 хв",
 "<p>Сьогоднішня частина. <b>1</b> — лексика статті (значення + контекст). <b>2</b> — пасив Present/Past і трансформація актив → пасив. "
 "<b>3</b> — новий матеріал: <b>causative have</b> = хтось інший робить це для нас (<i>I had my laptop repaired</i>). Логічний місток: пасив каже <i>що сталося</i>, каузатив — <i>я це організувала</i>. <b>4</b> — говоріння з обома структурами.</p>",
 ["Let’s review the words from the article first.", "Now — a new structure. If a technician fixes my laptop, I don’t say ‘I fixed my laptop’. I say: ‘I <b>had</b> my laptop <b>fixed</b>.’ Why?"],
 ul(["Пояснення каузативу — через контраст: <i>I cut my hair</i> (сама) vs <i>I had my hair cut</i> (перукар).", "3A: хто виконав роботу — швидкий тест розуміння.", "3B: форма <b>have</b> змінюється за часом (have / had / has / are having), V3 — незмінний.", "3C: переписати речення.", "4: усні питання — вимагайте повні відповіді з have + object + V3."]),
 ["What do you have done at home that you could do yourself?", "What tasks would you have done by AI?", "Have you ever had your CV checked?"],
 "<p><b>1A</b>: за значеннями на сторінці. <b>1B</b>: distributed team · back-to-back calls · burnout · promoted · touch · have the day off · small talk · cover</p>"
 "<p><b>2A</b>: is reviewed · was approved · are usually reported · was cancelled · are not sent · was opened · were hired · is updated</p>"
 "<p><b>3A</b>: 1 someone else · 2 the person · 3 someone else · 4 the person · 5 someone else · 6 the person</p>"
 "<p><b>3B</b>: have it cleaned · had it repaired · had her CV checked · had the new logo designed · have our servers tested · had it translated · has the meeting notes written · have your hair cut</p>",
 "<p>Типові помилки: <i>I had repaired my laptop</i> (це Past Perfect!) → <b>I had my laptop repaired</b>; <i>I have my hair cutted</i> → <b>cut</b>.</p>")))

# ======================= 4.3 =======================
V43 = [("4.3.1", "Alex і Beata обговорюють поїздку в Ріо", "rNaJdDuQXSA", "≈2 хв · Alex попереджає: Mateo любить говорити, multitask, порада — go with the flow"),
       ("4.3.2", "Option A — Beata намагається тримати тему", "8GaoWS-02Gg", "≈3 хв · Beata постійно повертає до Diabsensor, Mateo стає холоднішим"),
       ("4.3.3", "Option B — Beata «пливе за течією»", "U-ejfUrC5Rw", "≈2.5 хв · Beata підтримує розмову, Diabsensor не обговорили, але стосунки теплі"),
       ("4.3.4", "Conclusions", "vT7vrxUVTwE", "≈1.3 хв · висновок: обидва підходи мають ціну")]
O43 = ('<div class="bsec">Огляд уроку</div>' +
 blk("big", "Сенс уроку — яку ідею розкриваємо",
  "<p><b>Тримати тему чи пливти за течією?</b> Beata (молода менеджерка з Польщі) їде до клієнта Mateo (досвідчений, домінантний, бразилець) обговорити продукт Diabsensor. Mateo говорить про все, крім справи. "
  "У Beata два шляхи: <b>A — наполегливо повертати до порядку денного</b> (економить час, але псує стосунки) або <b>B — go with the flow</b> (будує стосунки, але є ризик втратити контроль).</p>"
  "<p>Ключова думка (4.3.4): <b>немає правильної відповіді — є ціна кожного вибору.</b> Люди відрізняються культурою, віком, статусом, характером; хороший комунікатор помічає це й адаптує стиль.</p>"
  "<p><b>Навіщо Каті як PM:</b> щоденні мітинги, клієнти, стейкхолдери, які «відпливають» від теми. Їй потрібні ввічливі фрази, щоб <b>змінити тему</b> (<i>Can we move to…?</i>) і <b>тримати фокус</b> (<i>We’ll come to that later</i>) — і розуміння, коли краще поступитися заради стосунків.</p>") +
 blk("aim", "Outcome", "<p>Студентка усвідомлює різні підходи до ведення розмови і вживає фрази, щоб змінити тему і повернути розмову до порядку денного.</p>") +
 blk("start", "До чого ведемо студента",
  "<h4>1. Розуміння: немає одного правильного стилю — у кожного вибору своя ціна</h4>"
  "<p>Beata їде до клієнта обговорити продукт, а Mateo говорить про все, крім справи. Два шляхи:</p>" +
  ul(["<b>тримати тему</b> (Option A) — економить час, але псує стосунки, Mateo стає холоднішим;",
      "<b>пливти за течією</b> (Option B) — стосунки теплі, але до продукту справа так і не доходить."]) +
  "<p>Висновок відео 4.3.4: люди відрізняються культурою, віком, статусом і характером. Хороший комунікатор це помічає і сам вирішує, що зараз важливіше — <b>результат чи стосунки</b>.</p>"
  "<h4>2. Навичка: ввічливо змінювати тему і повертати розмову до порядку денного</h4>" +
  ul(["<b>змінити тему:</b> <i>Can we move to…? · Is this a good moment to start talking about…? · I really think we should get to… · That reminds me… · Before I forget…</i>",
      "<b>утримати фокус / відкласти тему:</b> <i>We’ll come to that later. · We’ll get to… in a moment. · There will be plenty of time for that later.</i>"]) +
  "<h4>Як урок до цього веде</h4>" +
  "<ol><li><b>Lead-in (1)</b> — згадуємо, якими бувають «інші» люди на роботі.</li>"
  "<li><b>Відео 4.3.1 (2)</b> — знайомимося з проблемою: Mateo любить себе послухати, робить кілька справ одночасно, а Alex радить <i>go with the flow</i>.</li>"
  "<li><b>Вибір A чи B (3)</b> — Катя сама обирає стратегію і бачить, до чого вона веде. Це центр уроку.</li>"
  "<li><b>Обговорення, висновок відео і рефлексія (4–6)</b> — з історії виводимо принцип і переносимо на себе: «а я більше A чи B?»</li>"
  "<li><b>Фрази (7–8)</b> — сортуємо: змінити тему чи утримати її. Потім діалог.</li>"
  "<li><b>Практика (9)</b> — ви постійно відводите розмову вбік, вона повертає її фразами з 7.</li>"
  "<li><b>TASK (10)</b> — зустріч постачальника з клієнтом, який весь час відволікається: тут вона застосовує і стратегію, і фрази.</li></ol>"
  "<h4>Що це дає Каті як PM</h4><p>Упевненість на дзвінках зі стейкхолдерами і клієнтами, які йдуть від теми: вона може повернути розмову до справи без грубості і розуміє, коли краще поступитися заради стосунків.</p>"
  "<h4>Результат уроку</h4><p>Катя може провести коротку зустріч, де співрозмовник відволікається, і довести її до продукту, ціни або наступного кроку, вживаючи щонайменше 4 фрази з вправи 7.</p>") +
 blk("run", "Відео (YouTube)", vids(V43) + "<p style='font-size:14px;color:#77787b'>Усі чотири вбудовані в урок студента. Субтитри: CC на YouTube.</p>") +
 blk("tgt", "Таймінг (≈ 70–80 хв)", '<table class="tt"><tr><th>Етап</th><th>Що</th><th>Час</th></tr>' + "".join("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % r for r in [
  ("1", "Lead-in: зустрічі з «іншими» людьми", "7 хв"), ("2", "Відео 4.3.1", "8 хв"), ("3", "Вибір опції + відео A і B", "15 хв"), ("4–6", "Висновки, Conclusions, рефлексія", "10 хв"),
  ("7–8", "Функціональні фрази + діалог", "10 хв"), ("9", "Практика в парах + вимова -(e)s", "10 хв"), ("10", "TASK: зустріч supplier–client", "15 хв")]) + "</table>") +
 blk("watch", "Персонажі (для контексту)", ul(["<b>EvroMed</b> — британська фармкомпанія, продукт <b>Diabsensor</b> (сенсор для діабетиків).", "<b>Beata</b> — нова менеджерка проєкту; <b>Alex</b> — колега; <b>Daniel</b> — бос Beata.",
  "<b>Mateo</b> — бразильський дистриб’ютор, клієнт: багато говорить, multitask (бере дзвінки на зустрічі)."])))
S43 = []
S43.append(("s1", "1", step("s1", "1 · Lead-in", "7 хв",
 "<p>Підвести до ідеї уроку: людей розділяють культура, вік, освіта, корпоративна культура, професія — і це впливає на те, <b>як вони ведуть розмову</b>.</p>",
 ["Think of someone at work who is very different from you. How is he or she different?", "What was easy or difficult about talking to them?"],
 ul(["Попросіть конкретний приклад з її роботи (клієнт, розробник, топменеджер).", "Підкресліть різницю: з друзями ми не думаємо про стиль, з бізнес-партнерами — думаємо."]),
 ["Have you ever worked with people from another country? What surprised you?", "Is it harder to talk to someone older or younger than you?", "How is the culture of an IT start-up different from a big corporation?"], "")))
S43.append(("s2", "2", step("s2", "2 · Video 4.3.1", "8 хв",
 "<p>Знайомимося з ситуацією і з «проблемою» — Mateo. Відео дає ключові вирази <b>stay on track, go with the flow, likes the sound of his own voice, domineering, multitask</b>.</p>",
 ["Beata is going to Rio to meet a client, Mateo. Her colleague Alex knows him. Watch and find out what Alex thinks about Mateo."],
 ul(["Перед переглядом поясніть: <i>like the sound of your own voice</i> (багато говорить, впевнений), <i>go with the flow</i> (розслабитись і робити, як іде).", "Перегляд 1 → питання 2A; перегляд 2 → 2B."]),
 ["Would you follow Alex’s advice? Why?", "Do you know someone like Mateo at work?", "How do you prepare for a meeting with a difficult client?"],
 "<p>1 Yes, he has. · 2 He has met him twice, on trips with Daniel. · 3 Mateo likes to talk about other topics. · 4 She has done some background reading. · 5 Mateo likes the sound of his own voice, can be domineering, likes to multitask; it’ll be like any other trip; go with the flow.</p><p>2B: she feels there won’t be enough time to learn about the market, get to know Mateo and build a good relationship.</p>")))
S43.append(("s3", "3", step("s3", "3 · Video: Option A / Option B", "15 хв",
 "<p>Серце уроку. Студентка <b>сама обирає стратегію</b> — і бачить її наслідки. Порівняння A і B показує: та сама зустріч, різний стиль — різний результат для стосунків.</p>",
 ["What should Beata do: stay on the topic or go with the flow? Choose — and we’ll watch your option first.", "Watch and notice: how does Mateo react?"],
 ul(["Хай аргументує вибір (поле на сторінці).", "Дивимося обрану опцію, питання 1–5, потім іншу.", "Після обох: <i>Which Mateo is friendlier? Which Beata reached her goal?</i>"]),
 ["What phrases does Beata use to change the topic in Option A?", "What would YOU do in her place? Is there an Option C?", "Is it rude to take a phone call during a meeting in your culture?"],
 "<p><b>Option A:</b> 1 family, Mateo’s trips to Poland · 2 she tries to change the subject at every chance · 3 ignores her / ‘we’ll discuss it later’ · 4 takes a phone call · 5 she doesn’t manage to talk about the Diabsensor</p>"
 "<p><b>Option B:</b> 1 family, trips to Poland · 2 answers his questions and asks her own · 3 no — she goes with the flow and waits · 4 takes a phone call · 5 goes with the flow, no Diabsensor talk, but a good relationship</p>")))
S43.append(("s4", "4–6", step("s4", "4–6 · Discussion, Conclusions, Reflection", "10 хв",
 "<p>Перехід від історії до принципу: <b>результат vs стосунки</b>. 4.3.4 дає висновок, 6 — переносить на неї саму.</p>",
 ["So what did Beata win and what did she lose in each option?", "Watch the conclusion. Do you agree?", "Are you more like Beata in Option A or in Option B?"],
 ul(["4 — у парі/з вами; 5 — відео + одна головна думка; 6 — особистий досвід.", "Підштовхніть до нюансу: у культурах, орієнтованих на стосунки (Бразилія, Італія, Україна часто теж), small talk — це частина роботи, а не втрата часу."]),
 ["When is ‘going with the flow’ dangerous for a PM?", "How do you stop a stakeholder who talks too much in a meeting?", "How long should small talk last before a business meeting?"],
 "<p>4: 1 she doesn’t discuss her agenda, but may build a better relationship · 2 her attempts affect the relationship — Mateo is less friendly in A.</p><p>5: going with the flow builds the relationship but takes more time; focusing on the task saves time but may affect the relationship.</p>")))
S43.append(("s7", "7–8", step("s7", "7–8 · Functional language", "10 хв",
 "<p>Готові «інструменти»: фрази, щоб <b>змінити тему (C)</b> і <b>тримати фокус (S)</b>. У діалозі 8 — правильно вставити фразу в контекст і відпрацювати інтонацію.</p>",
 ["Here are phrases from the video. Which ones change the subject and which ones keep the conversation on track?", "Now read the dialogue with me. You are A, I am B."],
 ul(["7 — перевірка кнопкою Check.", "8 — після заповнення читаємо в ролях двічі: спочатку з текстом, потім «look up and say» (подивилась — підняла очі — сказала).",
     "Звертайте увагу на ввічливу інтонацію: <i>Can we move to…?</i> — підйом наприкінці."]),
 ["Which phrase is the most polite? Which is the strongest?", "Which phrases do you already use in your meetings?", "How would you say ‘давайте повернемось до питання’ in a meeting?"],
 "<p>7: 1 S · 2 C · 3 C · 4 S · 5 C · 6 S · 7 C · 8 C</p><p>8: 1 can we move to · 2 this a good moment to start talking about the · 3 get to the · 4 in a moment · 5 reminds me · 6 will be plenty of time for that later</p>",
 "<p>«I really think we should get to…» — у книзі це <b>C</b> (змінити тему на свою), хоча студенти часто кажуть S. Поясніть: Beata змінює тему розмови Mateo на свою.</p>")))
S43.append(("s9", "9", step("s9", "9 · Practice + Pronunciation", "10 хв",
 "<p>Автоматизація фраз у грі: одна людина тримає тему, інша постійно її змінює. Потім — письмово закріпити діалог. Вимова -(e)s: зайвий склад /ɪz/ лише після шиплячих/свистячих.</p>",
 ["Let’s play. You want to talk about your plans for next week. I will keep changing the subject. Try to stay on track!", "Now swap roles."],
 ul(["Ви — «Mateo»: перебивайте, розпитуйте про інше. Вона мусить вживати фрази з 7.", "9B — 1–2 короткі діалоги письмово.", "Pronunciation: проговоріть buses, offices, manages, choices — 2 склади; clients, talks — 1."]),
 ["Change topic to: a new smartphone / a trip abroad / a surprise party."],
 "<p>Pronunciation: extra syllable — buses, choices, manages, offices · no extra syllable — agendas, clients, decides, talks</p>")))
S43.append(("s10", "10", step("s10", "10 · TASK: supplier meets client", "15 хв",
 "<p>Підсумкова симуляція: справжня бізнес-зустріч, де одна сторона «відпливає», а інша має ввічливо повернути розмову до продукту. Тут вона застосовує і стратегію (A чи B), і фрази.</p>",
 ["You are the supplier. You have 40 minutes and you need to present the app. I am the client — and I have a lot to talk about!", "Afterwards: how did it go? What was easy, what was difficult?"],
 ul(["Рольові картки — на сторінці уроку (кнопки Role card S / C). У книзі вони на с.128/131; на сайті ми написали свої за тим самим сценарієм.", "Перший раунд: Катя — Supplier (S), ви — Client (C). Другий (10D): навпаки.",
     "Після раунду — 10C: обговорення + запишіть 3 фрази, які спрацювали."]),
 ["Did you go with the flow or stay on track? Why?", "What would you do differently next time?", "In your real job, who is your ‘Mateo’?"],
 "<p>Відкрита відповідь. Критерії: вжито ≥ 4 фрази з 7; ввічлива інтонація; зустріч дійшла до продукту/ціни/наступного кроку.</p>")))


# ======================= 4.4 =======================
O44 = ('<div class="bsec">Огляд уроку</div>' +
 blk("big", "Сенс уроку — яку ідею розкриваємо",
  "<p><b>Консенсус — це не «всі погодились з менеджером», а рішення, яке група може прийняти разом.</b> Менеджер у записі ставить дві умови: <b>кожен залучений і має шанс говорити</b>, і <b>думка кожного має однакову вагу</b>. "
  "Далі група вирішує навіть не «що», а «як» (process): один великий гурт, малі групи чи пари — і поступово <b>звужує варіанти</b> (narrowing down).</p>"
  "<p><b>Навіщо Каті як PM:</b> ретро, планування спринту, вибір інструменту, домовленості про гібридний графік — це щоденне «будування консенсусу». Їй потрібні м’які фрази для згоди/незгоди і пропозицій, щоб не тиснути, але довести обговорення до рішення.</p>"
  "<p><b>Ключ до мови:</b> ввічлива незгода (<i>I’m afraid I disagree / I’m not sure I agree with you on that</i>) і «м’яка» реакція на пропозицію (<i>That’s not a bad idea, but…</i>).</p>") +
 blk("aim", "Outcome", "<p>Студентка вживає вирази згоди, незгоди, пропозиції та реакції на пропозицію, щоб дійти згоди в обговоренні знайомої теми.</p>") +
 blk("run", "Аудіо", "<p>Записів 4.01 і 4.02 у нас немає, тому на сторінці уроку кнопка <b>▶ Listen</b> читає аудіоскрипт голосами браузера (різні голоси для Manager, Jose, Tanya, Sam, Dorothy; є швидкість «slower») і <b>Show script</b>. Якщо маєте оригінальні mp3 — надішліть, вставлю.</p>") +
 blk("tgt", "Таймінг (≈ 60–70 хв)", '<table class="tt"><tr><th>Етап</th><th>Що</th><th>Час</th></tr>' + "".join("<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % r for r in [
  ("1", "Lead-in: що таке консенсус", "7 хв"), ("2–3", "Аудіо 4.01: принципи", "8 хв"), ("4–5", "Аудіо 4.02: зустріч", "10 хв"), ("6–7", "Фрази: порядок діалогу, категорії, linking", "15 хв"), ("8", "TASK: дійти згоди", "15–20 хв")]) + "</table>"))
S44 = []
S44.append(("s1", "1", step("s1", "1 · Lead-in", "7 хв",
 "<p>Розібрати саме поняття: консенсус ≠ більшість ≠ рішення менеджера. Питання 4 — про культури (у когось «так» означає «я почув», а не «я згоден»).</p>",
 ["How do you usually make decisions in your team — does the manager decide, do you vote, or do you discuss until everyone agrees?", "Is a majority enough for consensus?"],
 ul(["Спершу її приклади з роботи, потім питання з книги.", "Розігрів з TB: поставте питання, де немає однозначної відповіді (best tool: Jira or Trello?), і покажіть, що таке <i>majority</i>."]),
 ["When was the last time your team couldn’t agree? What happened?", "Is it the PM’s job to decide or to facilitate?", "Have you worked with a culture where ‘yes’ doesn’t mean ‘I agree’?"], "")))
S44.append(("s2", "2–3", step("s2", "2–3 · Listening 4.01", "8 хв",
 "<p>Почути ідею уроку з уст фасилітатора: група важливіша за індивідуальні бажання; meet halfway / find the middle ground; дві базові умови консенсусу.</p>",
 ["Listen to a manager starting a meeting. What does she want to do today?"],
 ul(["2 — один раз слухаємо, 2 питання.", "3 — заповнити пропуски, потім ще раз слухати. Поясніть <i>of equal weight</i> = однаково важливо."]),
 ["What does ‘meet halfway’ mean? Give an example from your work.", "Which principle is hardest in real meetings?"],
 "<p>2: 1 focus on ways of building consensus · 2 finding what the group wants to do, not what each individual wants.</p><p>3: 1 involved, chance · 2 respected, important</p>")))
S44.append(("s4", "4–5", step("s4", "4–5 · Listening 4.02", "10 хв",
 "<p>Живий приклад: група обирає формат роботи. Показує, як звучить незгода і як ідея (talking sticks) змінює хід обговорення. Група ще <b>не</b> дійшла консенсусу — але <b>звузила варіанти</b>.</p>",
 ["Now listen to the meeting. Have they reached a consensus?"],
 ul(["4 — загальне розуміння + обґрунтування цитатою.", "5 — деталі; слова <i>process</i>, <i>narrowing down</i>, <i>talking sticks</i>."]),
 ["Would talking sticks work in your team?", "Who dominates meetings in your team? How do you deal with it?"],
 "<p>4: No — ‘we’re already narrowing down the options and moving towards consensus. Not everybody has spoken…’</p><p>5: 1 one large group, small groups, pairs · 2 a way of controlling who speaks · 3 how they will reach consensus · 4 getting closer by removing options</p>")))
S44.append(("s6", "6–7", step("s6", "6–7 · Functional language", "15 хв",
 "<p>Структурувати фрази за функціями: згода, незгода, пропозиція, реакція на пропозицію. 7B додає сильніші/м’якші варіанти. Linking (Pronunciation bank) — щоб фрази звучали природно: <i>not‿a bad‿idea</i>.</p>",
 ["Put the conversation in order — who speaks after whom?", "Now look at the phrases in bold. Which ones agree, disagree, suggest or react?"],
 ul(["6 — порядок 1–11, потім ▶ Listen для перевірки.", "7A/7B — категорії, кнопка Check.", "Linking: кнопки 🔊 у блоці вимови; попросіть повторити 3–4 фрази."]),
 ["Which phrase is the most polite way to disagree?", "Make a suggestion for your next retro using ‘How about if…’."],
 "<p>6: Manager 1 · Jose 2 · Tanya 3 · Sam 4 · Dorothy 5 · Jose 6 · Sam 7 · Jose 8 · Sam 9 · Jose 10 · Dorothy 11</p>"
 "<p>7A: agreement — Yes, I agree, too / I agree that / I agree with · disagreement — I’m afraid I disagree · suggestion — I think we should · reacting — So we need to / I don’t think / that’s not a bad idea</p>"
 "<p>7B: agreement 1 · disagreement 2, 5 · suggestion 3, 6 · reacting 4</p>",
 "<p>«I don’t think my idea is that bad» — це реакція на чужу реакцію; студенти часто плутають з «disagreement». Обидва варіанти можна прийняти, якщо пояснить.</p>")))
S44.append(("s8", "8", step("s8", "8 · TASK", "15–20 хв",
 "<p>Пройти всю процедуру консенсусу: ідеї → нотатки → вподобання → обговорення → рішення. 1:1 — ви граєте «групу» з різними позиціями.</p>",
 ["Choose a topic. Take two minutes to write your ideas. Then we follow the four steps and try to agree."],
 ul(["Для Каті краще власна тема: <i>the best hybrid schedule</i>, <i>max number of meetings a day</i>.", "Ви навмисно не погоджуйтесь 2–3 рази — вона має вжити фрази з 6–7.", "8C — рефлексія: які фрази вжила."]),
 ["What compromise did we reach?", "What would you do if one person still says no?"], "")))
# ======================= 4.5 =======================
O45 = ('<div class="bsec">Огляд уроку</div>' +
 blk("big", "Сенс уроку — яку ідею розкриваємо",
  "<p><b>Підтвердження замовлення — це «страховка» для обох сторін:</b> письмово фіксуємо, що саме, скільки, за якою ціною, коли й куди, і як оплачується. Якщо деталі розмиті («скоро», «знижка як домовлялись»), саме тут з’являються конфлікти.</p>"
  "<p><b>Дві версії:</b> <b>Classic</b> — лист з книги (формальна структура: Greeting → Opening → Order → Delivery → Payment → Enclosures → Ending → Closing). <b>Updated</b> — та сама структура в сучасному форматі: повідомлення клієнту в спільному Slack-каналі (Slack Connect) або шаблон з CRM. Інформація та сама — змінюється тон і форма (короткі рядки, буліти, «attached 📎»).</p>"
  "<p><b>Навіщо Каті:</b> вона пише клієнтам і підрядникам у чатах; вправа вчить писати коротко, але без втрати важливих деталей.</p>") +
 blk("aim", "Outcome", "<p>Classic: студентка пише лист-підтвердження замовлення. Updated: пише професійне повідомлення-підтвердження клієнту в Slack / CRM.</p>") +
 blk("run", "Порядок", ul(["Рекомендую: <b>Updated</b> на уроці, <b>Classic</b> (або тільки 3B) — додому. Або навпаки, якщо їй потрібні формальні листи.", "Сторінки 129/130 книги (поганий лист і бланк замовлення) на сайті замінені нашими: «поганий» лист / чат-повідомлення і бланк замовлення WT3488 для Ms Liang — дані збігаються з модельною відповіддю TB.", "На 3B є лічильник слів і перевірка, чи є всі частини листа (Greeting… Closing)."])))
S45 = []
S45.append(("s1", "1", step("s1", "1 · Lead-in", "7 хв",
 "<p>Прочитати зразок і помітити, яку інформацію він підтверджує (товар, кількість, графік доставки, ціна зі знижкою, оплата).</p>",
 ["When do you get confirmations? (booking a flight, an online order…) What information do they always have?", "Read the letter/message. What exactly does it confirm?"],
 ul(["Classic: лист; Updated: Slack-повідомлення з тими самими даними.", "Поясніть <i>hesitate</i> = вагатися, <i>enclose</i> (лист) vs <i>attach</i> (email/чат)."]),
 ["What could go wrong if the confirmation is not sent?", "Do you confirm orders or agreements in writing at work?"],
 "<p>Classic: 1 order · 2 received · 3 agreed · 4 Payment · 5 enclose · 6 thank · 7 hesitate · 8 sincerely</p><p>Updated: 1 order · 2 received · 3 agreed · 4 Payment · 5 attached · 6 Thanks · 7 hesitate · 8 regards</p>")))
S45.append(("s2", "2", step("s2", "2 · Functional language", "10 хв",
 "<p>Структура підтвердження: 8 функцій. В Updated — таблиця «лист → чат»: що змінюється, а що лишається (усі деталі!). Граматика: verbs + prepositions з листа.</p>",
 ["Which part of the letter is this phrase from — the greeting, the payment terms, the ending…?"],
 ul(["Перевірка кнопкою Check.", "Правило: <b>Dear Mr X → Yours sincerely</b>, <b>Dear Sir/Madam → Yours faithfully</b>.", "Пояснити: cash on delivery, payment in advance, T&Cs."]),
 ["Which phrases would sound too formal in Slack?", "Which emoji are OK with a client, and which are not?"],
 "<p>Greeting: Dear Mr Chahal, Dear Sir/Madam · Opening: we are writing to confirm / this is to confirm / we are pleased to confirm · Order details: order number…, order no 01 for five chairs · Delivery: to your factory in Mumbai, first delivery 05/11, to your head office · Payment: $4,000 monthly, 30 days after invoice, cash on delivery, payment in advance · Enclosures: we enclose T&Cs, details of our new range are enclosed · Ending: we thank you…, do not hesitate…, we look forward to supplying you… · Closing: Yours sincerely / faithfully</p>")))
S45.append(("s3", "3", step("s3", "3 · TASK", "20 хв / вдома",
 "<p>3A — побачити типові помилки (занадто неформально, без деталей). 3B — написати власне підтвердження за бланком. 3C — порівняти мову.</p>",
 ["What’s wrong with this letter/message? Let’s make a list.", "Now use the order form and write your own confirmation to Ms Liang."],
 ul(["3A — обговорення, потім Show ideas.", "3B — Classic ~150 слів, Updated 60–90 слів; лічильник частин підсвічує, чого бракує.", "3C — 1:1: ви пишете свою версію, обмінюєтесь і порівнюєте."]),
 ["Which version is better for a new client, and which for a client you know well?"],
 "<p>Модель Classic (TB): Dear Ms Liang, We are writing to confirm your order number WT3488 for 100 PR765 printers, which we received this morning. The unit price is €230. … discount of 8 percent for any orders over 80 units. We will deliver the goods to your warehouse in Felton Business Park on 5 May. … payment terms are 30 days after the date of the invoice. We enclose our business terms and conditions… Yours sincerely,</p><p>Модель Updated — на сторінці уроку (Show model answer).</p>")))

import tb_b1_1_1
O11, S11 = tb_b1_1_1.build(blk, ul, say, step)
open(os.path.join(OUT, "1-1.html"), "w").write(pagef("1.1", "Transferable skills", "../lessons/1-1/all/lesson.html", O11, S11))
open(os.path.join(OUT, "4-2.html"), "w").write(pagef("4.2", "Back to the office?", "../lessons/4-2/all/lesson.html", O42, S42))
open(os.path.join(OUT, "4-3.html"), "w").write(pagef("4.3", "Managing conversations", "../lessons/4-3/all/lesson.html", O43, S43))
open(os.path.join(OUT, "4-4.html"), "w").write(pagef("4.4", "Building consensus", "../lessons/4-4/all/lesson.html", O44, S44))
open(os.path.join(OUT, "4-5.html"), "w").write(pagef("4.5", "Confirming an order", "../lessons/4-5/all/lesson.html", O45, S45))
IDX = ('<div class="bsec">Business Partner B1 · Teacher’s Book</div>' + blk("aim", "Готові уроки", ul([
  '<a href="1-1.html"><b>1.1 Transferable skills</b></a> — Skills that survive AI · лексика навичок · job description для remote-вакансії',
  '<a href="4-2.html"><b>4.2 Back to the office?</b></a> — віддалена робота vs офіс · Present & Past Simple passive · Extra: have something done',
  '<a href="4-3.html"><b>4.3 Managing conversations</b></a> — змінити тему і тримати фокус · відео Beata & Mateo (YouTube)',
  '<a href="4-3-speak.html"><b>4.3 Speaking practice</b></a> — твої перебивання, секретні картки ситуацій, «якщо вона каже X → ти Y»',
  '<a href="4-4.html"><b>4.4 Building consensus</b></a> — згода, незгода, пропозиції · аудіо 4.01/4.02 (голосом браузера)',
  '<a href="4-5.html"><b>4.5 Confirming an order</b></a> — Classic: лист · Updated: Slack Connect / CRM'])))
open(os.path.join(OUT, "index.html"), "w").write(TPL.replace("__NUM__", "B1").replace("__TITLE__", "Teacher’s Book").replace("__URL__", "../index.html").replace("__NAV__", "")
                                                  .replace("__BODY__", '<section class="sec on">%s</section>' % IDX).replace('<a href="index.html">← Teacher’s Book: зміст</a>', '').replace("📄 Відкрити урок студента", "← Contents"))
print("ok")
