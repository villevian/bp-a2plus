"""B2 1.2 Employee retention — Teacher's Book page (EN / UK). Reuses helpers, CSS, JS from build_b2p_teacher_1-1.py.
Usage: python3 build_b2_teacher_1-2.py OUT.html
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, "build_b2p_teacher_1-1.py")).read()
head = base[:base.index("S = []")]
tail = base[base.index("NAV = ("):]
tail = tail[tail.index("CSS = "):]
tail = ('NAV = (\'<button data-s="s0" class="on">\' + T("Overview", "Огляд") + "</button>" + "".join(\'<button data-s="s%d">%s</button>\' % (i, l) for i, l in '
        '[(1, "1–2"), (2, "3"), (3, "4"), (4, "5A"), (5, "5B–C"), (6, "6"), (7, "7"), (8, "HW / Extra")]))\n\n' + tail)
tail = (tail.replace("<title>1.1 Research in tech — Teacher’s Book</title>", "<title>1.2 Employee retention — Teacher’s Book</title>")
        .replace('<div class="n">1.1</div><h1>Research in tech</h1>', '<div class="n">1.2</div><h1>Employee retention</h1>')
        .replace("../lessons/1-1/all/lesson.html", "../lessons/1-2/all/lesson.html")
        .replace("--c:#2f9a74;--c2:#dcf0e6", "--c:#5b5fc7;--c2:#e8e9fa").replace("#1f7d5c,#4fb58c", "#4044a8,#7b7fe0"))

content = r'''
S = []
def say(*lines):
    return block("tgt", T("How to start (say this)", "Як почати (скажіть це)"), "".join("<p><i>“%s”</i></p>" % l for l in lines))
def qs(xs):
    return block("out", T("Extra questions", "Додаткові питання"), "<ul>%s</ul>" % "".join("<li><i>%s</i></li>" % x for x in xs))

IDEA = block("aim", T("The big idea of the lesson", "Головна ідея уроку"), "<p>%s</p><p>%s</p>" % (
  T("<b>The cheapest employee is the one you keep.</b> In 2026 AI is the number one reason US companies give for layoffs — and more than half of the leaders who cut jobs for AI now say it was a mistake. The book’s topic (how banks keep young staff) becomes: <i>what really keeps people when everyone around is cutting jobs?</i>",
    "<b>Найдешевший працівник — той, якого ви втримали.</b> У 2026 році ІІ — причина №1, яку компанії США називають при скороченнях, і більше половини керівників, що скоротили людей «через ІІ», тепер визнають помилку. Тема книги (як банки втримують молодих) стає питанням: <i>що насправді втримує людей, коли навколо всіх звільняють?</i>"),
  T("<b>Where we lead the student:</b> from facts (IBM, Klarna, Commonwealth Bank, real numbers) → to the grammar of predictions (Future Continuous / Future Perfect: <i>by 2027 companies will have rehired…</i>) → to talking about <b>her own</b> future at work.",
    "<b>До чого ведемо студентку:</b> від фактів (IBM, Klarna, Commonwealth Bank, реальні цифри) → до граматики прогнозів (Future Continuous / Future Perfect: <i>by 2027 companies will have rehired…</i>) → до розмови про <b>її власне</b> майбутнє на роботі.")))
BG = block("run", T("Background you need (5-minute read)", "Що треба знати з теми (5 хвилин)"), ul([
  ("<b>IBM:</b> in 2023 the CEO said AI could replace about 7,800 back-office roles; in Feb 2026 the HR chief announced IBM is <b>tripling entry-level hiring</b> — “today’s entry-level employees are also tomorrow’s managers.” Without juniors you poach mid-level staff at ~30% more.",
   "<b>IBM:</b> у 2023 CEO казав, що ІІ може замінити ~7 800 бек-офісних ролей; у лютому 2026 HR-директорка оголосила, що IBM <b>утричі збільшує найм джунів</b>. Без джунів доведеться переманювати мідлів приблизно на 30% дорожче."),
  ("<b>Klarna:</b> in 2024 said its AI did the work of 700 support agents; in 2025 the CEO admitted cost had been too important and quality suffered — hiring humans again.",
   "<b>Klarna:</b> у 2024 заявляла, що ІІ виконує роботу 700 агентів підтримки; у 2025 CEO визнав, що надто зосередились на витратах, якість впала — знову наймають людей."),
  ("<b>Commonwealth Bank (Australia):</b> cut 45 call-centre jobs for a voice bot; calls went <b>up</b> by 2,000 a week, team leaders answered phones; the bank reversed the decision and admitted an “error”.",
   "<b>Commonwealth Bank (Австралія):</b> скоротив 45 місць у колцентрі заради голосового бота; дзвінків стало на 2 000 на тиждень <b>більше</b>, тимліди сиділи на телефонах; банк скасував рішення і визнав «помилку»."),
  ("<b>Numbers:</b> AI cited in 121,401 US job cuts in 2026 (to October); Orgvue: 55% of leaders who cut for AI regret it, ~1/3 rehired; Gartner: by 2027 half of companies that cut support staff will have rehired; Gallup: replacing an employee = 0.5–2× salary; Orgvue: $1.27 spent per $1 saved.",
   "<b>Цифри:</b> ІІ названо причиною 121 401 скорочення у США у 2026 (до жовтня); Orgvue: 55% керівників шкодують, ~1/3 вже найняли людей назад; Gartner: до 2027 половина компаній знову наймуть підтримку; Gallup: заміна працівника = 0,5–2 річні зарплати; Orgvue: $1,27 витрат на кожен заощаджений $1."),
  ("<b>Salesforce</b> (for the debate in 7B): cut support headcount from 9,000 to about 5,000 with AI agents (2025).",
   "<b>Salesforce</b> (для дебатів у 7B): скоротили підтримку з 9 000 до ~5 000 людей завдяки ІІ-агентам (2025).")]))
LEX = block("tgt", T("Lexical approach in this lesson", "Лексичний підхід у цьому уроці"), ul([
  ("Teach <b>chunks, not single words</b>: <i>lay off staff, reverse a decision, lose institutional knowledge, build the talent pipeline</i>. When the student says a single word, give back the chunk.",
   "Вчимо <b>блоки, а не окремі слова</b>: <i>lay off staff, reverse a decision, lose institutional knowledge, build the talent pipeline</i>. Коли студентка каже одне слово — поверніть їй цілий блок."),
  ("<b>Notice → practise → personalise:</b> notice chunks in the article (3–4) and comments (HW C), practise them (Extra 1–4), use them about her own company (Extra 5, HW E).",
   "<b>Помітити → потренувати → присвоїти:</b> помічаємо блоки в статті (3–4) і коментарях (HW C), тренуємо (Extra 1–4), вживаємо про свою компанію (Extra 5, HW E)."),
  ("<b>Nuance:</b> <i>fire</i> ≠ <i>lay off</i>. Fire = for bad performance; lay off = the company needs fewer people. A very common mistake in Ukrainian speakers’ English.",
   "<b>Нюанс:</b> <i>fire</i> ≠ <i>lay off</i>. Fire — за погану роботу; lay off — компанії потрібно менше людей. Дуже часта помилка українськомовних."),
  ("Recycle: start the next lesson with 5 chunks from this one (first letters on the board / in chat).",
   "Повторення: почніть наступний урок із 5 блоків цього (перші літери на дошці / в чаті).")]))
S.append("""<section id="s0" class="sec on"><div class="bsec">%s</div>%s%s%s%s%s</section>""" % (
 T("Overview", "Огляд уроку"), IDEA, BG, LEX,
 block("aim", T("Lesson outcome", "Outcome уроку"), "<p>%s</p>" % T(
  "Learners can use the Future Continuous and the Future Perfect Simple to talk about events that are taking place or that have finished at a point in the future.",
  "Студенти вживають Future Continuous і Future Perfect Simple, щоб говорити про події, які триватимуть або будуть завершені в певний момент у майбутньому.")),
 block("watch", T("Timing (60–75 min, 1:1)", "Таймінг (60–75 хв, індивідуально)"), ul([
  ("1–2 Lead-in — 8 min · 3–4 Reading — 15 min · 5A–C Grammar — 15 min · 6 — 7 min · 7 Speaking — 15 min.", "1–2 Lead-in — 8 хв · 3–4 Reading — 15 хв · 5A–C Граматика — 15 хв · 6 — 7 хв · 7 Speaking — 15 хв."),
  ("Homework: 6 Reddit-style comments (A–E). Extra: Lexical lab — as homework or a warm-up next lesson.", "Домашка: 6 коментарів у стилі Reddit (A–E). Extra: Lexical lab — як домашка або розминка наступного уроку.")]))))

S.append(step("s1", "Lead-in · 1–2", "8 min",
 ("Activate the coursebook vocabulary and the topic of keeping staff.", "Активувати лексику книги й тему утримання людей."),
 ("match five terms to definitions and say how each affects whether people stay.", "зіставити п’ять термінів із визначеннями й пояснити, як кожен впливає на те, чи залишаються люди."),
 chips(["diverse work", "menial tasks", "promotion", "sabbatical", "work-life balance"]),
 say("Imagine your company announces: ‘AI will do 30% of our work next year.’ What would make you stay? Let’s look at five things companies offer.") +
 ol([("1: the student matches alone, then checks. Ask for an example from her own work for each term.", "1: студентка зіставляє сама, потім Check. Попросіть приклад із її роботи до кожного терміна."),
     ("2: discuss — which of the five would keep her in a company that is cutting jobs? Push for reasons: <i>because… / unless…</i>", "2: обговорення — що з п’яти втримало б її в компанії, яка скорочує людей? Вимагайте причин: <i>because… / unless…</i>")]) +
 qs(["Have you ever done menial tasks that AI could do now?", "Would you take a sabbatical if your company offered one? What would you do?", "What matters more to you now: promotion or work-life balance?"]),
 ul([("<i>menial</i> /ˈmiːniəl/ — check pronunciation. <i>sabbatical</i> — stress on the 2nd syllable.", "<i>menial</i> /ˈmiːniəl/ — перевірте вимову. <i>sabbatical</i> — наголос на 2-му складі.")]),
 "<p>1 menial tasks · 2 sabbatical · 3 promotion · 4 work-life balance · 5 diverse work</p>"))

S.append(step("s2", "Reading · 3", "7 min",
 ("Read for gist: connect the article to the five terms and find other retention ideas.", "Читання для загального розуміння: зв’язати статтю з п’ятьма термінами й знайти інші ідеї утримання."),
 ("summarise the article’s main argument in one or two sentences.", "підсумувати головну думку статті в одному-двох реченнях."),
 chips(["lay off", "rehire", "reverse a decision", "AI washing", "institutional knowledge", "talent pipeline"]),
 say("This article is from 2026. Read it quickly — 3 minutes. Don’t stop at new words. Find the five words from Exercise 1 and one more idea for keeping people.") +
 ol([("Set a timer (3–4 min). Then ask for the main idea in one sentence.", "Таймер 3–4 хв. Потім — головна думка одним реченням."),
     ("Collect the chunks she noticed; give back full chunks (not <i>knowledge</i> but <i>lose institutional knowledge</i>).", "Зберіть блоки, які вона помітила; повертайте цілі блоки (не <i>knowledge</i>, а <i>lose institutional knowledge</i>).")]) +
 qs(["Which fact surprised you most?", "Is your company hiring juniors or cutting them?", "Have you seen ‘AI washing’ in the news or at work?"]),
 ul([("Students often think the article is ‘against AI’. It isn’t: the message is <i>augment, not replace</i>.", "Студенти часто думають, що стаття «проти ІІ». Ні: меседж — <i>посилювати, а не заміняти</i>.")]),
 "<p><b>Terms:</b> AI can take over menial tasks; young people want diverse work, clear promotion paths, work-life balance, sometimes a sabbatical.<br><b>Other ideas:</b> keep hiring juniors (IBM); learning and development; don’t lose institutional knowledge; AI should augment people; show staff the company will invest in them.</p>"))

S.append(step("s3", "Reading · 4", "8 min",
 ("Read for detail.", "Читання для деталей."),
 ("decide if statements are true or false and correct the false ones using the article.", "визначити, правдиві чи хибні твердження, і виправити хибні за статтею."),
 "",
 say("Now read again, more slowly. True or false? For every false one, show me the line in the text.") +
 ol([("After Check, ask her to correct false sentences orally with a chunk from the text.", "Після Check попросіть усно виправити хибні реченнями з блоком із тексту.")]) +
 qs(["Who do you agree with — the IBM HR chief or the critics of entry-level hiring?", "Why do you think the bank’s calls went up after the voice bot?"]),
 "",
 "<p>1 F (IBM is tripling entry-level hiring) · 2 T · 3 F (calls went up by 2,000 a week) · 4 F (55% say it was a mistake) · 5 T · 6 T</p>"))

S.append(step("s4", "Grammar · 5A", "7 min",
 ("Notice the meaning of Future Continuous vs Future Perfect Simple from the text.", "Помітити значення Future Continuous vs Future Perfect Simple з тексту."),
 ("say which form describes an action in progress and which one finished by a certain time.", "сказати, яка форма — про дію в процесі, а яка — завершену до певного моменту."),
 chips(["will be + -ing", "will have + past participle"]),
 say("Look at the timelines. The wavy line is an action in progress; the dot is an action that’s already finished. Now find the underlined forms in the article: which timeline is each one?") +
 ol([("Draw the two timelines in the chat or on paper. Use her calendar: <i>Next Friday at 5 I’ll be… / By Friday I’ll have…</i>", "Намалюйте дві шкали в чаті чи на папері. Використайте її календар: <i>Next Friday at 5 I’ll be… / By Friday I’ll have…</i>")]) +
 qs(["What will you be doing at this time tomorrow?", "What will you have finished by the end of this week?"]),
 ul([("Typical mistake: <i>By 2027 they will rehire</i> → <i>will have rehired</i> (finished before 2027).", "Типова помилка: <i>By 2027 they will rehire</i> → <i>will have rehired</i> (завершиться до 2027).")]),
 "<p>will be poaching — FC · will have rehired — FP · will have learnt — FP · will still be investing — FC · will be working — FC</p>"))

S.append(step("s5", "Grammar · 5B–C", "8 min",
 ("Notice time expressions and the form.", "Помітити маркери часу й будову форм."),
 ("find the time expression for each form and complete the form rules.", "знайти маркер часу до кожної форми й доповнити правило будови."),
 chips(["by 2027", "by the end of the decade", "in a few years", "in five years’ time", "by the time…"]),
 say("Which words near the verb tell you <i>when</i>? Look — <i>by</i> usually goes with the Future Perfect. Why do you think that is?") +
 ol([("5B: let her find the time expression in the text herself. 5C: she writes the rule, then you check.", "5B: нехай сама знайде маркер у тексті. 5C: вона формулює правило, потім ви перевіряєте.")]) +
 qs(["Can you say a sentence about your team with <i>by the end of the year</i>?"]),
 ul([("<i>by</i> = not later than (Future Perfect); <i>in five years’ time</i> = at that moment (often Future Continuous).", "<i>by</i> = не пізніше ніж (Future Perfect); <i>in five years’ time</i> = у той момент (часто Future Continuous).")]),
 "<p><b>5B:</b> will be poaching — in a few years · will have rehired — by 2027 · will have learnt — by the end of the decade · will still be investing — in five years’ time<br><b>5C:</b> will + be + present (-ing) participle · will + have + past participle</p>"))

S.append(step("s6", "Grammar · 6", "7 min",
 ("Controlled practice of the two forms in work contexts.", "Контрольована практика двох форм у робочих контекстах."),
 ("choose the right form depending on whether the action will be in progress or finished.", "вибрати правильну форму залежно від того, чи дія триватиме, чи буде завершена."),
 "",
 say("Same verbs as in the book, but now it’s about IT teams. For each sentence ask yourself: in progress or finished?") +
 ol([("After Check, ask her to change one sentence so it’s true for her company.", "Після Check попросіть змінити одне речення так, щоб воно було правдою для її компанії.")]) +
 qs(["What will your company have changed by next summer?", "What will you be doing in April?"]),
 ul([("3: <i>will have rested</i> is correct but sounds formal; in speech people say <i>I’ll have had a rest</i>.", "3: <i>will have rested</i> правильно, але звучить формально; у розмові кажуть <i>I’ll have had a rest</i>.")]),
 "<p>1 will be taking · 2 will have changed · 3 will have rested · 4 will have improved · 5 will be doing · 6 will have promoted</p>"))

S.append(step("s7", "Speaking · 7A–B", "15 min",
 ("Freer practice: use both forms to talk about her own future at work.", "Вільніша практика: обидві форми, щоб говорити про власне майбутнє на роботі."),
 ("ask and answer questions about her career using Future Continuous / Future Perfect and chunks from the lesson.", "ставити й відповідати на питання про кар’єру з Future Continuous / Future Perfect і блоками з уроку."),
 chips(["will be looking for", "will have reached", "talent pipeline", "work alongside AI", "augment, not replace"]),
 say("Complete the questions first. Then you ask me — and I ask you. Answer with real plans, not textbook answers.") +
 ol([("7A: complete the questions. 7B: real conversation; you answer too.", "7A: доповнити питання. 7B: справжня розмова; ви теж відповідаєте."),
     ("Finish with the debate: IBM (more juniors) vs Salesforce (4,000 fewer support staff). She takes one side, you take the other.", "Завершіть дебатами: IBM (більше джунів) vs Salesforce (на 4 000 менше підтримки). Вона бере одну сторону, ви — іншу.")]) +
 qs(["Will AI have changed your job by 2030? How?", "What will your company be doing to keep good people?", "Who made the smarter decision — IBM or Salesforce?"]),
 ul([("Note mistakes with the forms and with chunks; give feedback at the end, not during speaking.", "Записуйте помилки у формах і блоках; фідбек — у кінці, не під час говоріння.")]),
 "<p>1 will you be looking for · 2 will you have finished · 3 you won’t have finished · 4 will you be doing · 5 will you have reached</p>"))

S.append(step("s8", "Homework & Extra", "home",
 ("Homework: real people’s stories (6 comments, Reddit style). Extra: Lexical lab.", "Домашка: реальні історії людей (6 коментарів у стилі Reddit). Extra: Lexical lab."),
 ("notice chunks in authentic-style texts and use them in her own comment.", "помітити блоки в текстах автентичного стилю й ужити їх у власному коментарі."),
 "",
 ol([("HW A–D are checked automatically; read E (her comment) and comment in the admin.", "HW A–D перевіряються автоматично; прочитайте E (її коментар) і залиште відгук в адмінці."),
     ("Comments 1–4 are retold from real Reddit comments; 5–6 were written for the course. Tell the student this if she asks.", "Коментарі 1–4 — переказ реальних коментарів з Reddit; 5–6 написані для курсу. Скажіть студентці, якщо спитає."),
     ("Extra 5B (IBM vs Salesforce) = the warm-up for the next lesson.", "Extra 5B (IBM vs Salesforce) — розминка наступного уроку."),
     ("<b>In-lesson ★ screens</b> (after 4): Chunk hunt — she clicks 11 chunks in the article; Talk with a chunk — 60-second answers that must use a given chunk.", "<b>★ екрани в уроці</b> (після 4): Chunk hunt — клікає 11 блоків у статті; Talk with a chunk — відповідь 60 секунд з обов’язковим блоком."),
     ("<b>Speaking &amp; Games</b>: 1 Chunk tennis (you serve the first half, 5 s to return) · 2 Would you rather · 3 $1M budget simulation (fast-forward to 2028, then she presents with Future Perfect) · 4 Board meeting — she picks a role with a secret, you play the rest and draw a twist card every 2–3 min · 5 Stay interview — you hold the developer’s secret · 6 Rehire call negotiation · 7 Taboo.", "<b>Speaking &amp; Games</b>: 1 Chunk tennis (ви подаєте початок, 5 с на відповідь) · 2 Would you rather · 3 симуляція бюджету $1M (перемотка у 2028, потім презентація з Future Perfect) · 4 Board meeting — вона бере роль із секретом, ви граєте решту й тягнете twist-картку кожні 2–3 хв · 5 Stay interview — секрет розробниці знаєте ви · 6 переговори Rehire call · 7 Taboo.")]),
 "",
 "<p><b>HW A:</b> 1 friend · 2 friend · 3 lost own job · 4 lost own job · 5 manager · 6 customer<br><b>HW B:</b> 1 F · 2 T · 3 F · 4 F · 5 F · 6 T<br>"
 "<b>HW C:</b> was let go · was laid off · took him back as a consultant · was amazed by · legacy system · picked up<br><b>HW D:</b> 1 or 5 · 2 or 5 · 3 · 6<br>"
 "<b>Extra 2:</b> fired · let you go · made redundant · axes · laid off. Never say the bank staff were <i>fired</i> — they did nothing wrong.</p>"))
'''
exec(compile(head + content + tail, "build_b2_teacher_1-2", "exec"), {"__name__": "__main__"})
