"""B2 6.1 Ethical choices — Teacher's Book page (EN / UK). Reuses helpers, CSS, JS from build_b2p_teacher_1-1.py.
Usage: python3 build_b2_teacher_6-1.py OUT.html
"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, "build_b2p_teacher_1-1.py")).read()
head = base[:base.index("S = []")]
tail = base[base.index("NAV = ("):]
tail = (tail.replace("<title>1.1 Research in tech — Teacher’s Book</title>", "<title>6.1 Ethical choices — Teacher’s Book</title>")
        .replace('<div class="n">1.1</div><h1>Research in tech</h1>', '<div class="n">6.1</div><h1>Ethical choices</h1>')
        .replace("../lessons/1-1/all/lesson.html", "../lessons/6-1/all/lesson.html")
        .replace("--c:#2f9a74;--c2:#dcf0e6", "--c:#5b5fc7;--c2:#e8e9fa").replace("#1f7d5c,#4fb58c", "#4044a8,#7b7fe0"))

content = r'''
S = []
S.append("""<section id="s0" class="sec on"><div class="bsec">%s</div>%s%s%s%s</section>""" % (
 T("Overview", "Огляд уроку"),
 block("aim", T("Lesson outcome", "Outcome уроку"), "<p>%s</p>" % T(
  "The student can use language related to ethics in business: talk about working conditions, supply chains and manipulative app design, ask and answer questions about ethical choices, run a short survey and report the findings.",
  "Студент вживає мову про етику в бізнесі: говорить про умови праці, ланцюги постачання та маніпулятивний дизайн застосунків, ставить і відповідає на питання про етичний вибір, проводить коротке опитування і пише звіт про результати.")),
 block("run", T("Where the lesson is going", "До чого йдемо"), ol([
  ("<b>Facts (2–4):</b> the video shows the real cost of a €4 Shein dress; the case file adds the app side — fake discounts, countdown timers, endless scroll, EU fines.", "<b>Факти (2–4):</b> відео показує справжню ціну сукні за €4 у Shein; кейс додає бік застосунку — фальшиві знижки, таймери, нескінченний скрол, штрафи ЄС."),
  ("<b>Words (5–8):</b> the student gets the language to talk about it: collocations, verbs with prepositions, a campaign text.", "<b>Слова (5–8):</b> студент отримує мову, щоб про це говорити: колокації, дієслова з прийменниками, текст кампанії."),
  ("<b>Own data (9–10):</b> the student asks real people and writes a report — the words are used for a real purpose.", "<b>Свої дані (9–10):</b> студент опитує реальних людей і пише звіт — слова працюють на реальну задачу."),
  ("<b>Link to IT:</b> Violeta works in IT. Every discussion ends with <i>“What does this mean for the people who design and build apps?”</i>", "<b>Зв’язок з IT:</b> Віолета працює в IT. Кожне обговорення закінчуйте питанням <i>«Що це означає для тих, хто проєктує і робить застосунки?»</i>")])),
 block("tgt", T("Timing for a 1:1 lesson (about 90 minutes)", "Таймінг для індивідуального уроку (близько 90 хвилин)"),
  '<table class="tt"><tr><th>#</th><th>%s</th><th>%s</th></tr>' % (T("Stage", "Етап"), T("Time", "Час")) + "".join(
   "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (a, T(b, c), d) for a, b, c, d in [
    ("1", "Lead-in", "Lead-in", "5–7 min"), ("2–3", "Video: who said what, summary", "Відео: хто що сказав, summary", "15 min"),
    ("4", "Case file and discussion", "Кейс і обговорення", "10 min"), ("5–8", "Vocabulary", "Лексика", "20–25 min"),
    ("9A", "Survey questions", "Питання для опитування", "10 min"), ("9B–10", "Survey and report (homework)", "Опитування і звіт (домашка)", "home"),
    ("✓", "Self-assessment", "Самооцінка", "3–5 min")]) + "</table>"),
 block("watch", T("1:1 tips", "Поради для індивідуального уроку"), ul([
  ("You are the partner in all pair tasks. In 9B the student surveys colleagues or friends at home (5–10 people, a Google Form or a Slack poll is fine).", "Ви — партнер у всіх парних завданнях. У 9B студент опитує колег чи друзів удома (5–10 людей; можна Google Form або опитування в Slack)."),
  ("Don’t moralise. The goal is language for a professional discussion, not to make the student feel guilty about buying on Shein.", "Не моралізуйте. Мета — мова для професійної дискусії, а не почуття провини за покупки в Shein."),
  ("The case file facts are dated; if the student asks “what happened next?”, it’s a good research mini-task.", "Факти в кейсі мають дати; якщо студент питає «а що далі?», це гарне міні-завдання на пошук.")]))))

S.append(step("s1", "Lead-in · 1", "5–7 min",
 ("Activate the topic through the student’s own shopping habits.", "Активувати тему через власні звички студента як покупця."),
 ("talk about where and how they buy clothes and say what makes a brand ethical or unethical.", "розповісти, де і як купує одяг, і сказати, що робить бренд етичним чи неетичним."),
 chips(["fast fashion", "brand", "label", "ethical / unethical", "made in…"]),
 ol([("Base = the 5 coursebook questions. Ask 3–4, then switch to ★ Level up: apps.", "Base — 5 питань книги. Поставте 3–4, потім перейдіть на ★ Level up: apps."),
     ("Ask the student to check a label on what they are wearing (Q3) — it makes the topic personal at once.", "Попросіть подивитися етикетку на тому, що зараз на студентові (Q3) — тема одразу стає особистою.")]),
 ul([("<i>fast fashion</i> = cheap, trendy clothes made quickly; <i>ultra-fast fashion</i> = Shein / Temu, thousands of new items a day.", "<i>fast fashion</i> — дешевий трендовий одяг, зроблений швидко; <i>ultra-fast fashion</i> — Shein / Temu, тисячі нових речей щодня.")]),
 "<p>%s</p>" % T("No fixed answers. A good answer has a reason and an example.", "Фіксованих відповідей немає. Хороша відповідь має причину і приклад.")))

S.append(step("s2", "VIDEO · 2", "8 min",
 ("Listening for gist and for who says what.", "Слухання загального змісту і того, хто що каже."),
 ("identify five speakers and what each of them says.", "впізнати п’ятьох мовців і що каже кожен."),
 chips(["the job seeker", "the clothing producer", "the garment worker", "the expert from Redress", "Shein (statement)"]),
 ol([("Before watching: <i>A Shein dress costs €4. Who pays the rest of the price?</i> Let the student guess.", "До перегляду: <i>Сукня Shein коштує €4. Хто платить решту ціни?</i> Нехай студент припустить."),
     ("Play the whole video (6:10) with subtitles. The student chooses the person for each question; the time codes help to re-watch.", "Увімкніть усе відео (6:10) із субтитрами. Студент вибирає людину для кожного питання; таймкоди допомагають переглянути ще раз.")]),
 ul([("The names in the video are hard to catch, so the box uses roles, not names.", "Імена у відео важко розчути, тому в рамці ролі, а не імена."),
     ("Speakers have Chinese and British accents — a good chance to practise understanding non-native English.", "У мовців китайський і британський акценти — гарна нагода потренувати розуміння неносіїв.")]),
 "<ol><li>the job seeker (0:41)</li><li>the clothing producer (1:40)</li><li>the garment worker (3:15)</li><li>the expert from Redress (4:48)</li><li>Shein (statement) (5:21)</li></ol>"))

S.append(step("s3", "VIDEO · 3", "7 min",
 ("Listening for detail: numbers, facts, collocations.", "Слухання деталей: числа, факти, колокації."),
 ("complete a summary of the video with key facts and words.", "доповнити summary відео ключовими фактами і словами."),
 chips(["independent workshops", "on-demand model", "reorder", "drive prices down", "paid per piece", "disposability"]),
 ol([("Let the student read the summary first and guess the gaps. Then watch again (with subtitles if needed).", "Нехай студент спершу прочитає summary і спробує вгадати пропуски. Потім перегляд ще раз (за потреби із субтитрами)."),
     ("After checking, ask: <i>Which fact surprised you most?</i>", "Після перевірки спитайте: <i>Який факт здивував найбільше?</i>")]),
 ul([("The checker accepts small variants (e.g. <i>6,000 / 6,000 new items</i>).", "Перевірка приймає невеликі варіанти (напр., <i>6,000 / 6,000 new items</i>).")]),
 "<p>1 50,000 · 2 independent workshops · 3 6,000 new items · 4 on-demand · 5 reordered · 6 multiple factories · 7 prices down · 8 paid per piece · 9 60 hours a week · 10 75 hours a week · 11 volume</p>"))

S.append(step("s4", "VIDEO · 4", "10 min",
 ("Critical thinking: link the factory side and the app side; transfer to the student’s job in IT.", "Критичне мислення: поєднати бік фабрик і бік застосунку; перенести на роботу студента в IT."),
 ("give an opinion with reasons and say who in a tech company is responsible for ethical design.", "висловити думку з аргументами і сказати, хто в IT-компанії відповідає за етичний дизайн."),
 chips(["dark patterns", "fake discount", "pressure selling", "countdown timer", "endless scroll", "be responsible for", "On the one hand… on the other hand…"]),
 ol([("The student reads the case file (2 min) and finds one problem from the factories and three from the app.", "Студент читає кейс (2 хв) і знаходить одну проблему фабрик і три проблеми застосунку."),
     ("Base: 4 questions. ★ Level up: work dilemmas — you play the client who wants a countdown timer.", "Base: 4 питання. ★ Level up: робочі дилеми — ви граєте клієнта, який хоче таймер зворотного відліку.")]),
 ul([("If the student says “everyone does it”, ask <i>Does that make it ethical? Where is the line?</i>", "Якщо студент каже «всі так роблять», спитайте <i>Чи робить це етичним? Де межа?</i>")]),
 "<p><b>Model:</b> <i>On the one hand, cheap clothes help people with low incomes. On the other hand, someone pays the real price: workers who are paid per piece and work 75 hours a week. And the app makes it worse, because fake discounts and countdown timers push people to buy more than they need. I think designers and product managers are responsible for this — they choose these patterns.</i></p>"))

S.append(step("s5", "Vocabulary · 5", "3 min",
 ("Notice a key word and its collocations.", "Помітити ключове слово і його колокації."),
 ("find the word and make sentences with two collocations.", "знайти слово і скласти речення з двома колокаціями."),
 chips(["fashion designer", "fashion industry", "fashion retailer", "fashion show", "fast fashion", "fast delivery"]),
 ol([("After the answer, ask for one sentence about Shein with two of the collocations.", "Після відповіді попросіть одне речення про Shein із двома колокаціями.")]),
 "",
 "<p>fashion · ★ fast</p>"))

S.append(step("s6", "Vocabulary · 6", "5–7 min",
 ("Build strong collocations for talking about business ethics.", "Зібрати сильні колокації для розмови про етику в бізнесі."),
 ("use at least four of the collocations in sentences about the video.", "вжити щонайменше чотири колокації в реченнях про відео."),
 chips(["moral approach", "unethical conduct", "tough conditions", "low pay", "ethically sourced", "clothing brands", "sweatshops", "fair-trade cotton", "on-demand model", "profit margins", "labour law", "supplier factories"]),
 ol([("The example dial is already solved. The student turns the other dials until all four pairs are right.", "Приклад уже розв’язаний. Студент крутить інші диски, доки всі чотири пари не стануть правильними."),
     ("Then: <i>Describe the Shein video using four of these.</i>", "Потім: <i>Опишіть відео про Shein, вживши чотири з них.</i>")]),
 ul([("<i>sweatshop</i> is one word; <i>fair-trade</i> has a hyphen before a noun.", "<i>sweatshop</i> — одне слово; <i>fair-trade</i> пишеться через дефіс перед іменником.")]),
 "<p><b>Dial 1:</b> moral approach · unethical conduct · tough conditions · low pay<br><b>Dial 2:</b> ethically sourced · clothing brands · sweatshops · fair-trade cotton<br><b>Dial 3:</b> on-demand model · profit margins · labour law · supplier factories</p>"))

S.append(step("s7", "Vocabulary · 7", "7 min",
 ("Verbs with prepositions in a natural discussion.", "Дієслова з прийменниками в живій розмові."),
 ("complete the questions correctly and then answer them with their own opinion.", "правильно доповнити питання і відповісти на них своєю думкою."),
 chips(["be accused of", "be aware of", "be responsible for", "campaign against", "have an impact on", "look across", "take responsibility for"]),
 ol([("Complete and check. Then ask the student the questions; you answer one or two too, so it is a real conversation.", "Доповнити і перевірити. Потім поставте студентові ці питання; на одне-два відповідайте й ви, щоб була справжня розмова.")]),
 ul([("Typical mistakes: <i>responsible <s>of</s></i>, <i>aware <s>about</s></i>, <i>impact <s>to</s></i>.", "Типові помилки: <i>responsible <s>of</s></i>, <i>aware <s>about</s></i>, <i>impact <s>to</s></i>.")]),
 "<p>1 look across · 2 have been accused of · 3 is responsible for · 4 take responsibility for · 5 is aware of · 6 campaign against … have an impact on</p>"))

S.append(step("s8", "Vocabulary · 8", "5 min",
 ("Grammar and vocabulary accuracy in context (prepositions, word forms).", "Точність граматики й лексики в контексті (прийменники, форми слів)."),
 ("choose the correct forms and explain two of the choices.", "вибрати правильні форми і пояснити два вибори."),
 chips(["aware / beware", "ethical / ethically", "addicted / addictive", "responsibly / responsibility"]),
 ol([("The student chooses, checks, then reads the five-point plan aloud. Ask: <i>Which point is the most realistic for an app company?</i>", "Студент вибирає, перевіряє, потім читає вголос план із п’яти пунктів. Спитайте: <i>Який пункт найреалістичніший для IT-компанії?</i>")]),
 ul([("<i>addicted</i> = a person; <i>addictive</i> = a thing that makes you addicted.", "<i>addicted</i> — про людину; <i>addictive</i> — про річ, що викликає залежність.")]),
 "<p>1 across · 2 conditions · 3 supply chains · 4 against · 5 aware · 6 industry · 7 of · 8 for · 9 ethically · 10 addictive · 11 responsibility · 12 on</p>"))

S.append(step("s9", "PROJECT · 9A–B", "10 min + home",
 ("Turn the topic into real data: design and run a short survey.", "Перетворити тему на реальні дані: скласти і провести коротке опитування."),
 ("write 8–11 clear survey questions of different types and collect answers from real people.", "написати 8–11 чітких питань різних типів і зібрати відповіді реальних людей."),
 chips(["Have you ever…?", "How often do you…?", "Where…?", "Why / Why not?"]),
 ol([("9A in class: the student writes questions for the items; you correct the form (<i>Have you ever bought…?</i> not <i>Did you ever buy…?</i>).", "9A на уроці: студент пише питання до пунктів; ви виправляєте форму (<i>Have you ever bought…?</i>, а не <i>Did you ever buy…?</i>)."),
     ("Ask the questions to the student first — she is respondent number 1.", "Спершу поставте питання самій студентці — вона респондент №1."),
     ("9B at home: 5–10 people (colleagues, friends, a Slack poll). The table counts the percentages.", "9B удома: 5–10 людей (колеги, друзі, опитування в Slack). Таблиця сама рахує відсотки.")]),
 ul([("Leading questions (<i>You don’t buy on Shein, do you?</i>) spoil the data.", "Навідні питання (<i>You don’t buy on Shein, do you?</i>) псують дані.")]),
 "<p><b>Model questions:</b> 1 Do you own anything made of organic or fair-trade cotton? · 2 Do you ever wear vintage or second-hand clothes? · 6 How often do you buy fast fashion items? a) every month b) every few months c) once a year d) never · 8 Have you ever bought clothes in an app like Shein or Temu? · 9 Have you ever bought something because of a countdown timer or a ‘low stock’ message?</p>"))

S.append(step("s10", "PROJECT · 10", "home + 10 min feedback",
 ("Report findings in writing using reporting language and unit vocabulary.", "Написати звіт про результати з мовою звітування та лексикою юніту."),
 ("write a clear 160–180-word report (or an 80–100-word Slack summary) with numbers and a conclusion.", "написати чіткий звіт на 160–180 слів (або Slack-summary на 80–100 слів) з цифрами й висновком."),
 chips(["the majority of respondents", "over half of those surveyed", "just over a quarter", "none of the participants", "the findings suggest that", "admitted that", "raised concerns about"]),
 ol([("Homework. Next lesson: the student reads the report aloud; you give feedback on structure, numbers and 3 language points.", "Домашка. На наступному уроці студент читає звіт уголос; ви даєте фідбек про структуру, цифри й 3 мовні моменти.")]),
 ul([("Numbers must match the tally. <i>The majority</i> = more than 50%.", "Цифри мають збігатися з таблицею. <i>The majority</i> — більше 50%.")]),
 "<p><b>Model (opening):</b> <i>The aim of this survey was to find out how ethical our clothes and shopping habits are. Ten colleagues took part. The majority of respondents (70%) have bought clothes in an app like Shein or Temu, and over half admitted that they had bought something because of a countdown timer. However, none of the participants knew where most of their clothes were made…</i></p>"))

S.append(step("s11", "Self-assessment · ✓", "3–5 min",
 ("Reflection on the lesson outcome.", "Рефлексія щодо outcome уроку."),
 ("give an honest score from 0 to 5 and choose five phrases to keep.", "чесно оцінити себе від 0 до 5 і вибрати п’ять фраз на згадку."),
 "",
 ol([("Ask for the score with a reason. Words not ticked go into the next lesson’s warm-up.", "Попросіть оцінку з поясненням. Невідмічені слова — у розминку наступного уроку.")]),
 "",
 "<p>%s</p>" % T("No fixed answers. If the score is 0–2, repeat 6–7 next lesson.", "Фіксованих відповідей немає. Якщо 0–2 — повторіть 6–7 на наступному уроці.")))
'''
exec(compile(head.replace("OUT = sys.argv[1]", "OUT = sys.argv[1]") + content + tail, "build_b2_teacher_6-1", "exec"), {"__name__": "__main__"})
