"""B2+ 1.1 Research in tech — Teacher's Book page (EN / UK toggle).
Usage: python3 build_b2p_teacher_1-1.py OUT.html
"""
import sys

OUT = sys.argv[1]

def T(en, uk):
    return '<span class="en">%s</span><span class="uk">%s</span>' % (en, uk)

def chips(xs):
    return '<div class="tl">' + "".join("<span>%s</span>" % x for x in xs) + "</div>"

def ul(items):
    return "<ul>" + "".join("<li>%s</li>" % T(*i) if isinstance(i, tuple) else "<li>%s</li>" % i for i in items) + "</ul>"

def ol(items):
    return "<ol>" + "".join("<li>%s</li>" % T(*i) for i in items) + "</ol>"

def block(cls, title, content):
    return '<div class="blk %s"><h3>%s</h3>%s</div>' % (cls, title, content)

def step(sid, sec, time, aim, outcome, target, run, watch, answers, extra=""):
    h = '<section id="%s" class="sec">' % sid
    h += '<div class="bsec">%s <span class="time">⏱ %s</span></div>' % (sec, time)
    h += '<div class="two">'
    h += block("aim", T("Aim", "Мета"), "<p>%s</p>" % T(*aim))
    h += block("out", T("Outcome — the student can…", "Outcome — студент може…"), "<p>%s</p>" % T(*outcome))
    h += "</div>"
    if target:
        h += block("tgt", T("Target language — the student must use", "Цільова мова — студент має вжити"), target)
    h += block("run", T("How to run it", "Як вести"), run)
    if watch:
        h += block("watch", T("Watch out for", "На що звернути увагу"), watch)
    h += block("ans", T("Answers and model answers", "Відповіді та зразки"), answers)
    h += extra
    return h + "</section>"

S = []

# ---------------- 0 · Overview ----------------
S.append('''<section id="s0" class="sec on">
<div class="bsec">%s</div>
%s
%s
%s
%s
%s
</section>''' % (
 T("Overview", "Огляд уроку"),
 block("aim", T("Lesson outcome", "Outcome уроку"), "<p>%s</p>" % T(
  "The student can use a range of vocabulary related to market and user research, explain how tech companies learn from their users, ask good interview questions and present findings.",
  "Студент вживає лексику про маркетингові та користувацькі дослідження, пояснює, як IT-компанії вчаться у своїх користувачів, ставить хороші питання в інтерв’ю і презентує висновки.")),
 block("run", T("Flipped classroom: what happens where", "Перевернутий клас: що вдома, що на уроці"), ul([
  ("<b>Before the lesson (home):</b> the student chooses Video A or Video B, watches the three parts and does Exercises 2–4 on the lesson page. They read the vocabulary box.",
   "<b>До уроку (вдома):</b> студент обирає Video A або Video B, дивиться три частини і робить вправи 2–4 на сторінці уроку. Читає блок лексики."),
  ("<b>In class:</b> quick check of 3–4, then speaking: 1, 5, 6–9, the project 10 and the self-assessment.",
   "<b>На уроці:</b> швидка перевірка 3–4, далі говоріння: 1, 5, 6–9, проєкт 10 і самооцінка."),
  ("<b>Base / ★ Level up:</b> Base = the coursebook tasks. Level up = extra tasks for a strong student or when Base is too easy. You can switch in the middle of an exercise.",
   "<b>Base / ★ Level up:</b> Base — завдання з книги. Level up — додаткові для сильного студента або коли Base занадто легко. Перемикати можна посеред вправи.")])),
 block("tgt", T("Timing (about 80 minutes)", "Таймінг (близько 80 хвилин)"),
  '<table class="tt"><tr><th>#</th><th>%s</th><th>%s</th></tr>' % (T("Stage", "Етап"), T("Time", "Час")) + "".join(
   "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (a, T(b, c), d) for a, b, c, d in [
    ("1", "Lead-in: discussion", "Lead-in: обговорення", "5–7 min"),
    ("2–4", "Video: check the homework", "Відео: перевірка домашки", "8–10 min"),
    ("5", "Discussion about the video", "Обговорення відео", "5–7 min"),
    ("6–8", "Vocabulary: collocations, definitions, explanations", "Лексика: колокації, визначення, пояснення", "12–15 min"),
    ("9", "Speaking with the target vocabulary", "Говоріння з цільовою лексикою", "5–7 min"),
    ("10", "Project A–D", "Проєкт A–D", "25–30 min"),
    ("✓", "Self-assessment and My phrases", "Самооцінка і My phrases", "3–5 min")]) + "</table>"),
 block("watch", T("Cheat sheet: how to talk about market research", "Шпаргалка: як говорити про маркетингові дослідження"),
  "<p>%s</p>" % T("The main idea of the unit: <b>business decisions should be based on data about people, not on the boss’s opinion.</b> In tech the same thing is called user research, product discovery or analytics.",
                  "Головна думка юніту: <b>бізнес-рішення мають спиратися на дані про людей, а не на думку керівника.</b> В IT це те саме, тільки називається user research, product discovery, analytics.") +
  '<table class="tt"><tr><th>%s</th><th>%s</th><th>%s</th></tr>' % (T("Pair", "Пара"), T("Meaning", "Значення"), T("Tech example", "Приклад з IT")) + "".join(
   "<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>" % (a, T(b, c), T(d, e)) for a, b, c, d, e in [
    ("primary vs secondary research", "new data you collect yourself vs data that already exists", "нові дані, які збираєш сам, vs дані, що вже є",
     "user interviews vs a Gartner report, competitors’ reviews, Reddit threads", "інтерв’ю з користувачами vs звіт Gartner, відгуки конкурентів, треди на Reddit"),
    ("quantitative vs qualitative", "numbers (how many?) vs opinions and reasons (why?)", "цифри (скільки?) vs думки й причини (чому?)",
     "analytics, A/B test, NPS vs interviews, usability tests", "аналітика, A/B-тест, NPS vs інтерв’ю, юзабіліті-тести"),
    ("survey vs focus group", "many people, short answers vs 6–10 people, a long discussion with a moderator", "багато людей, короткі відповіді vs 6–10 людей, довга розмова з модератором",
     "an in-app poll vs a call with 6 users", "опитування в застосунку vs дзвінок із 6 користувачами")]) + "</table>" +
  "<p>%s</p>" % T("<b>Easy way in:</b> everyone has filled in a survey after a flight or an app update. Start there: <i>Did anyone read your answers?</i> IT people do research every day — they just don’t call it that: metrics, support tickets, arguing about a feature with data.",
                  "<b>Як зайти в тему:</b> усі заповнювали анкету після перельоту чи оновлення застосунку. Почніть із цього: <i>Did anyone read your answers?</i> Айтішники роблять research щодня, просто не називають його так: метрики, тікети сапорту, суперечки про фічу з даними.")),
 block("ans", T("By the end of the lesson the student should…", "До кінця уроку студент має…"), ul([
  ("use at least <b>10 words or phrases</b> from the vocabulary box while speaking (check with the ✓ checklist);", "вжити щонайменше <b>10 слів або фраз</b> із блоку лексики в мовленні (перевірте чеклістом на кроці ✓);"),
  ("ask <b>5 good interview questions</b> about the past, not hypothetical ones (10B–10C);", "поставити <b>5 хороших питань для інтерв’ю</b> про минуле, а не гіпотетичних (10B–10C);"),
  ("present findings with <b>reporting verbs</b>: <i>admitted, suggested, raised concerns that</i> (10D) — this prepares 1.5 Writing.", "презентувати висновки з <b>reporting verbs</b>: <i>admitted, suggested, raised concerns that</i> (10D) — це підготовка до 1.5 Writing.")]))))

# ---------------- 1 · Lead-in ----------------
S.append(step("s1", "Lead-in · 1", "5–7 min",
 ("Activate the topic and the student’s own experience. Diagnose what vocabulary they already have.", "Активувати тему й власний досвід студента. Побачити, яку лексику він уже має."),
 ("talk for about one minute about market research from their own experience, giving reasons and examples.", "говорити близько хвилини про дослідження ринку з власного досвіду, з причинами і прикладами."),
 chips(["fill in / complete a survey", "give feedback", "users / customers", "find out", "make decisions", "competitors"]),
 ol([("Choose 3–4 Base questions. With a strong student go to ★ Level up after two questions.", "Оберіть 3–4 питання з Base. Із сильним студентом після двох питань переходьте на ★ Level up."),
     ("Ask for an example from their job each time: <i>Can you give me an example from your team?</i>", "Щоразу просіть приклад з роботи: <i>Can you give me an example from your team?</i>"),
     ("Write down the words they are missing — you will meet them in 6–7.", "Записуйте слова, яких бракує, — вони будуть у 6–7.")]),
 ul([("<b>fill in / fill out a survey</b> (= answer it), not <i>make a survey</i> (= create it).", "<b>fill in / fill out a survey</b> (= відповісти), а не <i>make a survey</i> (= створити)."),
     ("Present Perfect for experience: <i>Have you ever…? — Yes, I’ve filled in…</i>; Past Simple for the details: <i>Last week I got…</i>", "Present Perfect для досвіду: <i>Have you ever…? — Yes, I’ve filled in…</i>; Past Simple для деталей: <i>Last week I got…</i>"),
     ("Level up questions are opinion questions — accept any position but push for <i>because…</i> and <i>On the one hand… on the other hand…</i>", "Питання Level up — на думку: приймайте будь-яку позицію, але вимагайте <i>because…</i> і <i>On the one hand… on the other hand…</i>")]),
 ul(["<b>Why do companies need market research?</b> — <i>To make better decisions, understand their customers and see what competitors are doing.</i>",
     "<b>What do companies want to find out?</b> — <i>Who their users are, how satisfied they are, why they stop using the product, what they would pay for.</i>",
     "<b>Deleted app:</b> <i>I deleted it because it sent too many notifications. Nobody asked me why — a short exit survey could have told them.</i>"])))

# ---------------- 2 ----------------
S.append(step("s2", "VIDEO · 2", "home / 2 min",
 ("Prediction before watching: activate ideas and vocabulary so the video is easier to follow.", "Прогноз перед переглядом: активувати ідеї й лексику, щоб відео було легше зрозуміти."),
 ("list 4–6 ideas in English.", "скласти список із 4–6 ідей англійською."),
 chips(["talk to users", "interview", "survey", "ask questions"]),
 ol([("At home the student writes the list in the box.", "Вдома студент пише список у полі."),
     ("In class: 1 minute — ask them to read the list and tick what the video confirmed.", "На уроці: 1 хвилина — попросіть прочитати список і позначити, що підтвердило відео.")]),
 "",
 ul(["<b>Video A — who to talk to / what to ask:</b> <i>your network, former colleagues, online communities (LinkedIn, Slack, Discord), events; questions about their problems and how they do things now.</i>",
     "<b>Video B — mistakes:</b> <i>pitching your idea, asking hypothetical questions, talking too much instead of listening, trusting compliments.</i>"])))

# ---------------- 3 ----------------
FRAG = {
 "A": [("Part 1 · 00:42–03:23", [("When do great founders start talking to users?", "Before they even have a product — and they keep learning from users throughout the life of the company."),
                                 ("Why do users “keep you honest”?", "They are the only stakeholders who actually pay you, so they will tell you the truth."),
                                 ("Who are the only stakeholders who pay?", "Users and customers.")]),
       ("Part 2 · 05:58–09:42", [("Best format?", "A video or phone call (or in person)."),
                                 ("Why not pitch early?", "You get polite reactions to your idea instead of real information about their problems."),
                                 ("Your role?", "To listen, not to talk — and to ask open-ended follow-up questions.")]),
       ("Part 3 · 09:42–17:04", [("Questions to avoid?", "Yes/no questions, “Would you use this?”, “Which features do you want?”"),
                                 ("The one big danger?", "Focusing on features instead of problems."),
                                 ("Good problems, bad solutions?", "Users know their problems well, but their ideas for solutions are often bad. The solution is your job."),
                                 ("Is the problem valuable?", "People already pay for solutions; free tools like spreadsheets aren’t strong competitors; the audience is easy to sell to."),
                                 ("Prototype?", "Watch without giving instructions; ask them to think aloud."),
                                 ("Keep interviewees involved?", "A shared group chat, share progress, make them feel special.")])],
 "B": [("Part 1 · 00:27–02:43", [("What do the best founders do?", "They maintain a direct connection to their users throughout the life of the company."),
                                 ("The YC motto?", "Write code and talk to users.")]),
       ("Part 2 · 02:43–05:56", [("Three mistakes?", "Talking about your idea instead of their life; hypotheticals instead of specifics; talking instead of listening."),
                                 ("Why are hypotheticals dangerous?", "People are too optimistic about the future; answers don’t show what they will really do.")]),
       ("Part 3 · 05:56–14:16", [("Five questions?", "What’s the hardest part about…? When was the last time you encountered…? Why was it hard? What have you done to solve it? What don’t you love about the solutions you’ve tried?"),
                                 ("Which question shows the problem is real?", "“What have you done to solve it?” — if nothing, the problem may not be painful enough."),
                                 ("Why “the last time”, not “usually”?", "A real event gives facts; “usually” gives general, often inaccurate answers.")])]}
def frag_ans(k):
    return "".join("<p class='fp'><b>%s</b></p><ol>" % t + "".join("<li>%s — <i>%s</i></li>" % (q, a) for q, a in qs) + "</ol>" for t, qs in FRAG[k])
S.append(step("s3", "VIDEO · 3", "home + 4 min in class",
 ("Listening for gist and specific information; noticing real phrases from the video (the “Listen for” chips).", "Слухання на загальне розуміння і деталі; помічати живі фрази з відео (рядок «Listen for»)."),
 ("answer the questions in their own words and use at least <b>two “Listen for” phrases per part</b>.", "відповісти на питання своїми словами і вжити щонайменше <b>дві фрази з «Listen for» у кожній частині</b>."),
 chips(["keep you honest", "reach out to", "open up", "dive deep into", "derail the interview", "focus on problems, not features", "a formidable competitor",
        "the go-between", "easier said than done", "pitch your idea", "hard data", "pain points", "get at the root of", "a burning problem"]),
 ol([("At home: one watch per part, answer, then check with the <i>answer</i> button.", "Вдома: один перегляд на частину, відповісти, потім звірити кнопкою <i>answer</i>."),
     ("In class: ask 2 questions per part orally. The answer is accepted only with a phrase from “Listen for”.", "На уроці: по 2 питання на частину усно. Відповідь зараховується лише з фразою з «Listen for»."),
     ("If the student chose a different video from what you expected — no problem, the switch remembers the choice on 2–5.", "Якщо студент обрав інше відео — не страшно, перемикач пам’ятає вибір на кроках 2–5.")]),
 ul([("<b>pitch</b> an idea (not <i>present an idea to sell</i>); <b>stakeholder</b> — stress on the first syllable.", "<b>pitch</b> an idea; <b>stakeholder</b> — наголос на перший склад."),
     ("<b>focus on</b> + noun / -ing: <i>focus on problems</i>, not <i>focus to problems</i>.", "<b>focus on</b> + іменник / -ing: <i>focus on problems</i>, а не <i>focus to</i>."),
     ("Phrases come from transcripts — watch the parts yourself before the first lesson.", "Фрази взяті з розшифровок — перегляньте частини самі перед першим уроком.")]),
 "<h4>Video A — Gustaf Alströmer</h4>" + frag_ans("A") + "<h4>Video B — Eric Migicovsky</h4>" + frag_ans("B")))

# ---------------- 4 ----------------
TFA = [("Only very young start-ups need to talk to users.", "F", "the best founders learn from users throughout the life of the company."),
       ("You can start with people you know and former colleagues.", "T", ""),
       ("Interviews work best by email or online forms.", "F", "use video or phone calls."),
       ("It’s a good idea to pitch your idea at the start.", "F", "don’t pitch early; listen more than you talk."),
       ("“Would you use this?” is a useful question.", "F", "avoid yes/no and hypothetical questions; focus on problems."),
       ("If people already pay for solutions, the problem is probably valuable.", "T", "")]
TFB = [("Founders should leave user conversations to sales.", "F", "keep a direct connection to users."),
       ("Main advice: write code and talk to users.", "T", ""),
       ("Ask about things that have already happened.", "T", ""),
       ("Talk more than the user so they understand your product.", "F", "listen, don’t talk; take notes."),
       ("“What’s the hardest part about doing this?” is one of the five questions.", "T", ""),
       ("Compliments are useful data.", "F", "discard compliments and hypotheticals.")]
def tf_ans(L):
    return "<ol>" + "".join("<li>%s — <b>%s</b>%s</li>" % (s, a, (": <i>" + c + "</i>") if c else "") for s, a, c in L) + "</ol>"
S.append(step("s4", "VIDEO · 4", "home + 3 min in class",
 ("Listening for detail; correcting false information in full sentences.", "Слухання деталей; виправлення хибної інформації повними реченнями."),
 ("correct every false sentence aloud in a full sentence.", "виправити кожне хибне речення вголос повним реченням."),
 chips(["It’s false, because he says…", "Actually, …", "According to the speaker, …"]),
 ol([("At home: the page shows a short explanation after each click.", "Вдома: після кожного кліку сторінка показує коротке пояснення."),
     ("In class: only the F sentences. The student corrects them without looking at the explanation.", "На уроці: лише речення з F. Студент виправляє їх, не дивлячись на пояснення.")]),
 "",
 "<h4>Video A</h4>" + tf_ans(TFA) + "<h4>Video B</h4>" + tf_ans(TFB)))

# ---------------- 5 ----------------
S.append(step("s5", "VIDEO · 5", "5–7 min",
 ("Personal and critical response to the video; transfer the ideas to the student’s job.", "Особиста й критична реакція на відео; перенести ідеї на роботу студента."),
 ("explain an idea from the video and connect it to a real situation from work, using 2–3 phrases from the video.", "пояснити ідею з відео і пов’язати її з реальною ситуацією з роботи, вживши 2–3 фрази з відео."),
 chips(["What he means is…", "In my experience…", "focus on problems, not features", "a burning problem", "pain points", "the hardest part about…"]),
 ol([("Base: discuss the question for the chosen video. Ask for one real story.", "Base: обговоріть питання до обраного відео. Попросіть одну реальну історію."),
     ("Video B: role-play — the student asks you the five questions about a real work problem, then you swap.", "Video B: рольова гра — студент ставить вам п’ять питань про реальну робочу проблему, потім міняєтесь."),
     ("★ Level up: “Which method?” cards — the student chooses a method and says if it’s primary/secondary, qualitative/quantitative.", "★ Level up: картки «Which method?» — студент обирає метод і каже, primary/secondary, qualitative/quantitative.")]),
 ul([("Students often retell instead of explaining. Ask: <i>So what does that mean for your team?</i>", "Студенти часто переказують замість пояснювати. Питайте: <i>So what does that mean for your team?</i>")]),
 "<p><b>Model (A):</b> <i>What he means is that users are experts in their problems, not in solutions. For example, a client asked us for a dashboard with 30 charts, but the real pain point was that he needed one number for his weekly report.</i></p>"
 "<p><b>★ Which method?</b></p><ol>"
 "<li>Cancel after a month → <i>in-depth interviews (qualitative, primary)</i></li>"
 "<li>Which button gets more clicks → <i>A/B test (quantitative)</i></li>"
 "<li>Market size in Germany → <i>desk research (secondary, quantitative)</i></li>"
 "<li>Can new users set up a project → <i>usability test (qualitative)</i></li>"
 "<li>Satisfaction of 20,000 customers → <i>online survey, rating questions, NPS (quantitative)</i></li>"
 "<li>Competitors’ premium plans → <i>desk research (secondary)</i></li>"
 "<li>1-star reviews after an update → <i>analyse reviews (AI can cluster them) + follow-up interviews</i></li></ol>"))

# ---------------- 6 ----------------
S.append(step("s6", "Vocabulary · 6A–B", "5–6 min",
 ("Learn the key collocations of the lesson and notice their structure.", "Вивчити ключові колокації уроку і помітити їхню будову."),
 ("complete the sentences and make one own sentence about their company with at least four collocations.", "заповнити речення і скласти власне речення про свою компанію щонайменше з чотирма колокаціями."),
 chips(["online surveys", "focus group", "customer satisfaction", "in-depth interviews", "desk research", "launch a product", "target audience", "sample size"]),
 ol([("6A: the student does it alone, then <i>Check</i>. Don’t show answers before they try.", "6A: студент робить сам, потім <i>Check</i>. Не показуйте відповіді, поки не спробує."),
     ("6B: click the type. Then ask: <i>Which of these does your company use?</i>", "6B: клікнути тип. Потім спитайте: <i>Which of these does your company use?</i>"),
     ("Extension: one sentence about their company with each collocation they got wrong.", "Розширення: речення про свою компанію з кожною колокацією, де була помилка.")]),
 ul([("<b>research</b> is uncountable: <i>do / carry out research</i>, not <i>researches</i>.", "<b>research</b> — незлічуване: <i>do / carry out research</i>, а не <i>researches</i>."),
     ("<b>focus group</b>, not <i>focusing group</i>; <b>in-depth</b> with a hyphen.", "<b>focus group</b>, а не <i>focusing group</i>; <b>in-depth</b> через дефіс.")]),
 "<p><b>6A:</b> 1 online · 2 focus · 3 customer · 4 in-depth · 5 desk · 6 launch · 7 target · 8 sample</p>"
 "<p><b>6B:</b> adjective + noun: <i>online surveys, in-depth interviews</i> (also primary / secondary research) · verb + noun: <i>launch a product</i> · noun + noun: <i>focus groups, customer satisfaction, desk research, target audience, sample size</i></p>"))

# ---------------- 7 ----------------
S.append(step("s7", "Vocabulary · 7", "4–5 min",
 ("Understand the meaning of ten key terms.", "Зрозуміти значення десяти ключових термінів."),
 ("match all words with definitions and pronounce them correctly.", "зіставити всі слова з визначеннями і правильно їх вимовити."),
 chips(["quantitative", "qualitative", "product tester", "impact", "respondent", "gauge", "researcher", "gather", "viable", "data analysis"]),
 ol([("Base: match, then <i>Check</i>.", "Base: зіставити, потім <i>Check</i>."),
     ("Drill the pronunciation of the tricky words (see below).", "Відпрацюйте вимову складних слів (див. нижче)."),
     ("★ Level up: tech words — the student says the word and tells a short story from work.", "★ Level up: IT-слова — студент називає слово і розповідає коротку історію з роботи.")]),
 ul(["<b>gauge</b> /ɡeɪdʒ/ · <b>qualitative</b> /ˈkwɒlɪtətɪv/ · <b>quantitative</b> /ˈkwɒntɪtətɪv/ · <b>viable</b> /ˈvaɪəbl/",
     ("<b>data</b> in tech is usually uncountable: <i>the data shows</i>.", "<b>data</b> в IT зазвичай незлічуване: <i>the data shows</i>."),
     ("Remind: <b>product tester</b> in tech is usually <i>beta tester</i> (see the table in the vocabulary box).", "Нагадайте: <b>product tester</b> в IT зазвичай <i>beta tester</i> (таблиця в блоці лексики).")]),
 "<p><b>7:</b> 1 g · 2 c · 3 f · 4 h · 5 a · 6 d · 7 e · 8 j · 9 b · 10 i</p>"
 "<p><b>★ Level up:</b> A/B test · churn rate · user interview · usability test · insight · synthesis · NPS · MVP</p>"))

# ---------------- 8 ----------------
S.append(step("s8", "Vocabulary · 8", "3–4 min",
 ("Check deeper understanding of the underlined words.", "Перевірити глибше розуміння підкреслених слів."),
 ("choose the right option and explain why the other one is wrong.", "обрати правильний варіант і пояснити, чому інший неправильний."),
 chips(["qualitative research", "primary research", "customer satisfaction", "viable", "sample size", "gauge"]),
 ol([("Ask <i>Why not the other one?</i> after each answer.", "Після кожної відповіді питайте <i>Why not the other one?</i>"),
     ("★ Level up: verbs that go with the nouns — the student lists as many as possible, then makes a sentence.", "★ Level up: дієслова до іменників — студент називає якомога більше і складає речення.")]),
 "",
 "<p><b>8:</b> 1 information about why people like or dislike a product · 2 collecting new data · 3 using research tools such as surveys and ratings · 4 has · 5 people · 6 watch their reactions to a prototype</p>"
 "<p><b>★ Verbs:</b> research — carry out / conduct / commission / outsource · data — gather / collect / analyse / interpret · a survey — design / run / send out / fill in · feedback — get / collect / act on / ignore · a product — launch / test / roll out / pull · the impact — gauge / measure / assess</p>"))

# ---------------- 9 ----------------
S.append(step("s9", "Vocabulary · 9", "5–7 min",
 ("Fluency practice with the new vocabulary.", "Практика вільного мовлення з новою лексикою."),
 ("speak for two minutes and use <b>at least six words from 6A and 7</b>.", "говорити дві хвилини і вжити <b>щонайменше шість слів із 6A і 7</b>."),
 chips(["launch a product", "target audience", "sample size", "gather data", "gauge", "viable", "qualitative / quantitative", "customer satisfaction"]),
 ol([("Base: the student answers; you tick the words used (the chips under the task).", "Base: студент відповідає, ви відмічаєте вжиті слова (чипи під завданням)."),
     ("If fewer than six — ask a follow-up that needs a missing word: <i>How many people would you ask?</i> → sample size.", "Якщо менше шести — поставте питання, що потребує пропущеного слова: <i>How many people would you ask?</i> → sample size."),
     ("★ Level up: real-life cases — two minutes to plan, then defend the plan; you play a sceptical stakeholder.", "★ Level up: реальні кейси — дві хвилини на план, потім захист; ви граєте скептичного стейкхолдера.")]),
 "",
 "<p><b>Model:</b> <i>Before you launch a product, you need to know if it’s viable. First, I’d do some desk research to see what competitors offer. Then I’d gather data from the target audience: an online survey to gauge interest — quantitative data — and a few in-depth interviews to understand why. The sample size depends on the budget, but five interviews already show the main pain points.</i></p>"))

# ---------------- 10 ----------------
S.append(step("s10", "PROJECT · 10A–D", "25–30 min",
 ("Bring together all the vocabulary and skills of the lesson in one realistic task: profile → survey → interview → presentation.", "Зібрати всю лексику й навички уроку в одному реалістичному завданні: профіль → опитування → інтерв’ю → презентація."),
 ("describe two brands, write a balanced survey, run an interview with good questions and present findings with reporting verbs.", "описати два бренди, скласти збалансоване опитування, провести інтерв’ю з хорошими питаннями і презентувати висновки з reporting verbs."),
 "",
 "<h4>10A · 5 min</h4>" + ol([
   ("The student chooses two apps and fills in the table. The words under each row are compulsory.", "Студент обирає два застосунки й заповнює таблицю. Слова під кожним рядком обов’язкові."),
   ("Then they speak from the table; you click the words in the checklist when used. Target: <b>7/10</b>.", "Потім розповідає за таблицею; ви клікаєте слова в чеклісті, коли вони звучать. Мета: <b>7/10</b>.")]) +
 "<h4>10B · 7 min</h4>" + ol([
   ("Step 1 — the student rewrites the four bad questions, then compares. Ask <i>What was wrong with the original?</i>", "Крок 1 — студент переписує чотири погані питання, потім порівнює. Питайте <i>What was wrong with the original?</i>"),
   ("Step 2 — six questions; <i>Check my mix</i> must show all four types and both qualitative and quantitative.", "Крок 2 — шість питань; <i>Check my mix</i> має показати всі чотири типи і якісні, і кількісні дані.")]) +
 "<h4>10C · 8 min</h4>" + ol([
   ("Open “For the teacher” and choose a persona close to the student’s job.", "Відкрийте «For the teacher» і оберіть персонажа, близького до роботи студента."),
   ("<b>Reward good questions</b> with rich, concrete details. Answer bad questions (hypothetical, leading) with empty compliments: <i>Sure, sounds great!</i> — then ask: <i>Was that useful data?</i>", "<b>На хороші питання</b> відповідайте детально й конкретно. На погані (гіпотетичні, навідні) — порожніми компліментами: <i>Sure, sounds great!</i> — а потім спитайте: <i>Was that useful data?</i>"),
   ("Click the bingo squares as you hear them. Then swap roles: you interview the student about their real work problem.", "Клікайте клітинки бінго, коли чуєте фрази. Потім міняйтесь ролями: ви інтерв’юєте студента про його реальну робочу проблему.")]) +
 "<h4>10D · 7 min</h4>" + ol([
   ("The student fills in the four boxes and clicks <i>Build my script</i>, then presents without reading for two minutes.", "Студент заповнює чотири поля, натискає <i>Build my script</i>, потім презентує дві хвилини, не читаючи."),
   ("You tick the feedback checklist as the respondent.", "Ви як респондент відмічаєте чекліст фідбеку."),
   ("★ Level up: read the stakeholder challenges one by one; the student must answer each with a lesson phrase.", "★ Level up: читайте заперечення стейкхолдера по одному; студент відповідає на кожне фразою з уроку.")]),
 ul([("Reporting verbs: <i>suggest + -ing / that…</i>, not <i>suggest to do</i>; <i>admit + -ing / that…</i>; <i>raise concerns that…</i>", "Reporting verbs: <i>suggest + -ing / that…</i>, а не <i>suggest to do</i>; <i>admit + -ing / that…</i>; <i>raise concerns that…</i>"),
     ("Question tags in an interview are leading questions (link to 1.2): <i>You’d pay for this, wouldn’t you?</i>", "Question tags в інтерв’ю — навідні питання (зв’язок з 1.2): <i>You’d pay for this, wouldn’t you?</i>"),
     ("Students tend to pitch in the interview. Stop them: <i>Are you asking or selling?</i>", "Студенти схильні «продавати» в інтерв’ю. Зупиняйте: <i>Are you asking or selling?</i>")]),
 "<h4>10A — model (Duolingo vs Babbel)</h4><p><i>Duolingo attracts customers with a free app and games; its target audience is people who want to learn a little every day. Its promise is that learning is fun, and customer satisfaction is high because of streaks. It’s memorable because of the green owl — that’s real impact on social media. Babbel is a formidable competitor for serious learners: it’s viable as a paid product because its ideal customer has a clear pain point — they need a language for work.</i></p>"
 "<h4>10B — better questions</h4><ol><li>Tell me about the last meeting you had to summarise. How did you do it?</li><li>What’s the hardest part about … at the moment?</li><li>What have you tried so far to solve this? What don’t you love about it?</li><li>What are you paying for tools like this right now? <i>(the original question tag biases the answer)</i></li></ol>"
 "<p><b>Good survey (AI meeting summary in Slack):</b> 1 How many meetings do you have in a typical week? (multiple-choice, quant.) · 2 Do you write meeting notes yourself? (yes/no, quant.) · 3 How satisfied are you with your current notes, 1–10? (rating, quant.) · 4 Tell us about the last time a decision from a meeting got lost. (open-ended, qual.) · 5 What tools do you use for notes now? (multiple-choice) · 6 What don’t you love about them? (open-ended, qual.)</p>"
 "<h4>10D — model script</h4><p><i>Our target audience is product managers in remote teams. Over half of the respondents admitted that they lose decisions after meetings, and two of them raised concerns that AI notes are not accurate. The burning problem is not taking notes — it’s finding decisions later, so it warrants solving. As a next step, we’ll roll out an MVP in Slack and run an A/B test with 50 users to get hard data.</i></p>"
 "<h4>★ Stakeholder challenges — model replies</h4><ul>"
 "<li>Hard data or compliments? — <i>This isn’t a compliment — it’s what they actually did: three of five had lost a decision last week.</i></li>"
 "<li>Five people isn’t a sample size. — <i>It’s a small sample, but the pattern was clear. Next we’ll run a survey with 200 respondents.</i></li>"
 "<li>Features instead of problems? — <i>No, we started from the pain point; the feature comes second.</i></li>"
 "<li>Is it a burning problem? — <i>Yes — they already pay for two tools and still lose decisions.</i></li>"
 "<li>Can’t AI do this research? — <i>AI can speed up synthesis, but it can’t replace talking to real users.</i></li>"
 "<li>Formidable competitor? — <i>Moving users off their tool is notoriously difficult, so we’ll integrate with it, not replace it.</i></li></ul>"))

# ---------------- ✓ ----------------
S.append(step("s11", "Self-assessment · ✓", "3–5 min",
 ("Reflection and consolidation; the student sees which words they used and which still need practice.", "Рефлексія і закріплення: студент бачить, які слова вжив, а які ще треба відпрацювати."),
 ("give an honest score, tick the words used and write five phrases to remember.", "чесно оцінити себе, відмітити вжиті слова й записати п’ять фраз для запам’ятовування."),
 "",
 ol([("The student ticks the words they really used today. Target: <b>10+</b>.", "Студент відмічає слова, які справді вжив сьогодні. Мета: <b>10+</b>."),
     ("The button puts unused words into My phrases — that becomes their homework list.", "Кнопка переносить невжиті слова в My phrases — це їхній список на домашку."),
     ("Homework idea: five sentences about their own company with the unused words; next lesson — 1.2.", "Ідея домашки: п’ять речень про свою компанію з невжитими словами; наступний урок — 1.2.")]),
 "",
 "<p>%s</p>" % T("No fixed answers. If the score is 0–2, repeat 6–8 at the start of the next lesson.", "Фіксованих відповідей немає. Якщо оцінка 0–2, повторіть 6–8 на початку наступного уроку.")))

NAV = ('<button data-s="s0" class="on">' + T("Overview", "Огляд") + "</button>" +
       "".join('<button data-s="s%d">%d</button>' % (i, i) for i in range(1, 11)) + '<button data-s="s11">✓</button>')

CSS = """
:root{--c:#2f9a74;--c2:#dcf0e6;--mag:#c4127a;--grey:#77787b;--lg:#eeeff0;--ink:#231f20;--gold:#f2b631}
*{box-sizing:border-box}body{margin:0;font-family:"Fira Sans",system-ui,sans-serif;color:var(--ink);background:#fff;font-weight:300;line-height:1.5}
header{display:flex;align-items:stretch;border-bottom:3px solid var(--c)}
header .n{background:linear-gradient(120deg,#1f7d5c,#4fb58c);color:#fff;font-weight:500;font-size:34px;padding:14px 22px}
header h1{margin:0;align-self:center;padding-left:18px;font-weight:500;font-size:26px;color:#4d4d4f}
header .t{margin-left:auto;align-self:center;margin-right:12px;background:var(--gold);color:#3b2c00;font-weight:600;font-size:13px;padding:6px 12px;border-radius:4px}
.lang{align-self:center;margin-right:18px;display:inline-flex;border:1.5px solid var(--c);border-radius:20px;overflow:hidden}
.lang button{font:inherit;font-weight:600;border:0;background:#fff;color:var(--c);padding:5px 14px;cursor:pointer}.lang button.on{background:var(--c);color:#fff}
.top{display:flex;gap:14px;align-items:center;padding:12px 22px 0;flex-wrap:wrap;font-size:15px}.top a{color:var(--c);font-weight:500;text-decoration:none}
nav{display:flex;gap:6px;padding:12px 22px 0;flex-wrap:wrap}
nav button{font:inherit;font-weight:500;font-size:16px;min-width:46px;border:1.5px solid var(--c);background:#fff;color:var(--c);padding:6px 14px;border-radius:20px;cursor:pointer}
nav button.on{background:var(--c);color:#fff}
main{max-width:1000px;margin:0 auto;padding:16px 22px 40px}
.sec{display:none}.sec.on{display:block}
.bsec{font-weight:600;font-size:21px;color:var(--grey);margin:4px 0 14px}.time{font-size:14px;font-weight:500;color:var(--c);background:var(--c2);border-radius:12px;padding:2px 10px;margin-left:8px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.blk{border-left:5px solid var(--c);background:var(--lg);padding:10px 16px;margin:0 0 12px;border-radius:0 4px 4px 0}
.blk h3{margin:0 0 6px;font-size:15px;font-weight:600;text-transform:uppercase;letter-spacing:.4px;color:#4d4d4f}
.blk p{margin:4px 0 8px}.blk ul,.blk ol{margin:4px 0 6px;padding-left:22px}.blk li{margin:3px 0}
.blk h4{margin:12px 0 4px;font-size:15px;font-weight:600;color:var(--c)}
.blk.aim{border-color:var(--c);background:var(--c2)}.blk.out{border-color:#1f6f8b;background:#e3eef8}
.blk.tgt{border-color:var(--mag);background:#fbeef5}.blk.watch{border-color:var(--gold);background:#fdf7e6}.blk.ans{border-color:#5c9e2f;background:#eef6d3}
.blk.run{background:#fff;border:1px solid #d5d6d7;border-left:5px solid var(--c)}
.tl{display:flex;flex-wrap:wrap;gap:6px}.tl span{background:#fff;border:1px solid #f0c6dc;border-radius:12px;padding:2px 10px;font-size:14.5px;font-weight:400}
table.tt{border-collapse:collapse;width:100%;font-size:14.5px;background:#fff;margin:6px 0}table.tt th,table.tt td{border:1px solid #c9cacc;padding:5px 8px;text-align:left;vertical-align:top}table.tt th{background:#e3e4e5;font-weight:600}
.fp{margin:8px 0 2px}
.uk{display:none}body.ua .uk{display:inline}body.ua .en{display:none}
footer{max-width:1000px;margin:0 auto;padding:0 22px 30px;font-size:12px;color:var(--grey)}
@media(max-width:760px){.two{grid-template-columns:1fr}}
@media print{nav,.lang,.top{display:none}.sec{display:block!important;page-break-after:always}}
"""

JS = """
const $=id=>document.getElementById(id);
document.querySelectorAll("nav button").forEach(b=>b.onclick=()=>{document.querySelectorAll("nav button,.sec").forEach(x=>x.classList.remove("on"));b.classList.add("on");$(b.dataset.s).classList.add("on");window.scrollTo(0,0)});
function setLang(l,b){document.body.classList.toggle("ua",l=="uk");document.querySelectorAll(".lang button").forEach(x=>x.classList.remove("on"));b.classList.add("on");try{localStorage.setItem("tbLang",l)}catch(e){}}
try{if(localStorage.getItem("tbLang")=="uk")setLang("uk",document.querySelectorAll(".lang button")[1])}catch(e){}
"""

html = ('<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>1.1 Research in tech — Teacher’s Book</title>'
        '<link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">'
        '<style>' + CSS + '</style></head><body>'
        '<header><div class="n">1.1</div><h1>Research in tech</h1><div class="t">TEACHER’S BOOK</div>'
        '<div class="lang"><button class="on" onclick="setLang(\'en\',this)">EN</button><button onclick="setLang(\'uk\',this)">УКР</button></div></header>'
        '<div class="top"><a href="index.html">← Teacher’s Book contents</a><a href="../lessons/1-1/all/lesson.html" target="_blank">Open the student lesson ↗</a></div>'
        '<nav>' + NAV + '</nav><main>' + "".join(S) + '</main>'
        '<footer>Valentyna Hordiienko · Middle Learning Architect</footer><script>' + JS + '</script></body></html>')
open(OUT, "w").write(html)
print("ok", len(html))
