"""Zvenyhora (dairy) B2+ 1.1 — Teacher's Book page (EN / UK).
Reuses helpers, CSS and JS from build_b2p_teacher_1-1.py; the content is dairy-specific.
Usage: python3 build_zv_teacher_1-1.py OUT.html
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, "build_b2p_teacher_1-1.py")).read()
head = base[:base.index("S = []")]
tail = base[base.index("NAV = (") :]
tail = (tail.replace("<title>1.1 Research in tech — Teacher’s Book</title>", "<title>1.1 Market research in dairy — Teacher’s Book</title>")
            .replace("<h1>Research in tech</h1>", "<h1>Market research in dairy</h1>"))

content = r'''
S = []

# ---------------- Overview ----------------
S.append("""<section id="s0" class="sec on"><div class="bsec">%s</div>%s%s%s%s%s</section>""" % (
 T("Overview", "Огляд уроку"),
 block("aim", T("Lesson outcome", "Outcome уроку"), "<p>%s</p>" % T(
  "The student can use a range of vocabulary related to market research in the dairy business, explain how a dairy brand finds out what shoppers and retail chains want, ask good interview questions and present findings.",
  "Студент вживає лексику про дослідження ринку в молочному бізнесі, пояснює, як молочний бренд дізнається, чого хочуть покупці й торговельні мережі, ставить хороші питання в інтерв’ю і презентує висновки.")),
 block("run", T("Who the course is for", "Для кого курс"), ul([
  ("Staff of a dairy producer: marketing, sales and key account managers, R&D / quality, production managers. Their customers are both <b>shoppers</b> and <b>retail chains</b> (category managers).",
   "Працівники молочного заводу: маркетинг, продажі та key account менеджери, R&D / якість, керівники виробництва. Їхні клієнти — і <b>покупці</b>, і <b>торговельні мережі</b> (категорійні менеджери)."),
  ("<b>Before the lesson (home):</b> watch the 2.5-minute Chobani video and do Exercises 2–4. <b>In class:</b> speaking — 1, 5, 6–9, project 10, self-assessment.",
   "<b>До уроку (вдома):</b> подивитися 2,5-хвилинне відео про Chobani і зробити вправи 2–4. <b>На уроці:</b> говоріння — 1, 5, 6–9, проєкт 10, самооцінка."),
  ("<b>Base / ★ Level up:</b> Base = the coursebook tasks; Level up = extra dairy-industry tasks for strong students.",
   "<b>Base / ★ Level up:</b> Base — завдання з книги; Level up — додаткові завдання з молочної галузі для сильних студентів.")])),
 block("tgt", T("Timing (about 80 minutes)", "Таймінг (близько 80 хвилин)"),
  '<table class="tt"><tr><th>#</th><th>%s</th><th>%s</th></tr>' % (T("Stage", "Етап"), T("Time", "Час")) + "".join(
   "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (a, T(b, c), d) for a, b, c, d in [
    ("1", "Lead-in", "Lead-in", "5–7 min"), ("2–4", "Video and case file: check", "Відео й кейс: перевірка", "8–10 min"),
    ("5", "Discussion: data or instinct?", "Обговорення: дані чи інтуїція?", "5–7 min"), ("6–8", "Vocabulary", "Лексика", "12–15 min"),
    ("9", "Speaking with the target vocabulary", "Говоріння з цільовою лексикою", "5–7 min"), ("10", "Project A–D", "Проєкт A–D", "25–30 min"),
    ("✓", "Self-assessment", "Самооцінка", "3–5 min")]) + "</table>"),
 block("watch", T("Cheat sheet: how to talk about market research in dairy", "Шпаргалка: як говорити про дослідження ринку в молочці"),
  "<p>%s</p>" % T("The main idea: <b>a new product, flavour or pack should be based on data about shoppers and retail partners, not on the opinion of the boss.</b> In dairy and FMCG, research means taste tests, retail sales data, store checks, complaints and talking to category managers.",
                  "Головна думка: <b>новий продукт, смак чи упаковка мають спиратися на дані про покупців і торговельних партнерів, а не на думку керівника.</b> У молочці та FMCG дослідження — це дегустації, дані продажів мереж, перевірки в магазинах, скарги і розмови з категорійними менеджерами.") +
  '<table class="tt"><tr><th>%s</th><th>%s</th><th>%s</th></tr>' % (T("Pair", "Пара"), T("Meaning", "Значення"), T("Dairy example", "Приклад з молочки")) + "".join(
   "<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>" % (a, T(b, c), T(d, e)) for a, b, c, d, e in [
    ("primary vs secondary research", "new data you collect yourself vs data that already exists", "нові дані, які збираєш сам, vs дані, що вже є",
     "our own tasting in a supermarket vs a market report or a chain’s sales data", "власна дегустація в супермаркеті vs звіт про ринок чи дані продажів мережі"),
    ("quantitative vs qualitative", "numbers (how many?) vs opinions and reasons (why?)", "цифри (скільки?) vs думки й причини (чому?)",
     "sales by SKU, market share, ratings in a taste test vs interviews with mothers about kids’ yoghurt", "продажі за SKU, частка ринку, оцінки в дегустації vs інтерв’ю з мамами про дитячий йогурт"),
    ("survey vs focus group", "many people, short answers vs 6–10 people, a long discussion", "багато людей, короткі відповіді vs 6–10 людей, довга розмова",
     "a QR-code survey on the pack vs a group discussing three new flavours", "опитування за QR-кодом на упаковці vs група, що обговорює три нові смаки")]) + "</table>" +
  "<p>%s</p>" % T("<b>Easy way in:</b> everyone has tried free samples in a supermarket. Ask: <i>Did you buy the product afterwards? Why / why not?</i> Then ask what their own company does to learn what shoppers think.",
                  "<b>Як зайти в тему:</b> усі куштували безкоштовні зразки в супермаркеті. Спитайте: <i>Did you buy the product afterwards? Why / why not?</i> А потім — що робить їхня компанія, щоб дізнатися думку покупців.")),
 block("ans", T("By the end of the lesson the student should…", "До кінця уроку студент має…"), ul([
  ("use at least <b>10 words or phrases</b> from the vocabulary box while speaking (✓ checklist);", "вжити щонайменше <b>10 слів або фраз</b> із блоку лексики (чекліст на кроці ✓);"),
  ("ask <b>5 good questions</b> to a shopper or a category manager about real past behaviour (10B–10C);", "поставити <b>5 хороших питань</b> покупцю чи категорійному менеджеру про реальну поведінку в минулому (10B–10C);"),
  ("present findings with <b>reporting verbs</b> (10D).", "презентувати висновки з <b>reporting verbs</b> (10D).")]))))

S.append(step("s1", "Lead-in · 1", "5–7 min",
 ("Activate the topic through the student’s experience as a shopper and as a dairy professional.", "Активувати тему через досвід студента як покупця і як фахівця молочної галузі."),
 ("talk for about a minute, with reasons and an example from their company.", "говорити близько хвилини з причинами і прикладом зі своєї компанії."),
 chips(["fill in a survey", "a tasting / free samples", "shoppers", "retail chains", "find out", "make decisions"]),
 ol([("Choose 3–4 Base questions; with a strong student switch to ★ Level up.", "Оберіть 3–4 питання Base; із сильним студентом перейдіть на ★ Level up."),
     ("Always ask for an example from their plant or brand.", "Завжди просіть приклад зі свого заводу чи бренду."),
     ("Note missing words — they come in 6–7.", "Записуйте слова, яких бракує, — вони будуть у 6–7.")]),
 ul([("<b>shopper</b> (the person in the shop) vs <b>consumer</b> (the person who eats it) vs <b>customer</b> (who pays — often the retail chain). Use them precisely.", "<b>shopper</b> (хто купує в магазині) vs <b>consumer</b> (хто їсть) vs <b>customer</b> (хто платить — часто мережа). Вимагайте точності."),
     ("<b>fill in a survey</b>, not <i>make a survey</i>; Present Perfect for experience: <i>I’ve taken part in a tasting.</i>", "<b>fill in a survey</b>, а не <i>make a survey</i>; Present Perfect для досвіду: <i>I’ve taken part in a tasting.</i>")]),
 ul(["<b>Why do food companies need research?</b> — <i>To reduce the risk of a launch, understand shoppers and retail chains, and see what competitors do.</i>",
     "<b>What do dairy companies want to know?</b> — <i>Who buys the product, why they choose it, which price point is acceptable, how they feel about taste, shelf life and the pack.</i>"])))

S.append(step("s2", "VIDEO · 2", "home / 2 min",
 ("Prediction before watching.", "Прогноз перед переглядом."),
 ("list 4–6 ways a dairy company can learn what shoppers want.", "назвати 4–6 способів, як молочна компанія дізнається, чого хочуть покупці."),
 chips(["taste test", "survey", "focus group", "sales data", "talk to retail buyers"]),
 ol([("At home the student writes the list; in class compare it with the video and the case file.", "Вдома студент пише список; на уроці порівнює з відео та кейсом.")]),
 "",
 "<p><i>Taste tests and free samples, shopper surveys (online, QR code on the pack), focus groups, retail sales data, store checks / retail audits, complaints and social media comments, interviews with category managers.</i></p>"))

S.append(step("s3", "VIDEO · 3", "home + 4 min in class",
 ("Listening for specific information; reading a short case; noticing useful phrases.", "Слухання конкретної інформації; читання короткого кейсу; помічати корисні фрази."),
 ("answer the questions in their own words and use at least <b>three phrases from “Listen for”</b>.", "відповісти своїми словами і вжити щонайменше <b>три фрази з «Listen for»</b>."),
 chips(["shut a factory down", "grow into a $1 billion business", "change what people eat", "nearly non-existent", "a niche market", "price point", "the dairy aisle", "specialty stores", "word of mouth"]),
 ol([("At home: watch once, answer, check with <i>answer</i>; read the case file.", "Вдома: подивитися раз, відповісти, звірити кнопкою <i>answer</i>; прочитати кейс."),
     ("In class: ask the case-file question — <i>Why were the price point and the place on the shelf so important?</i> This is the key idea of the lesson.", "На уроці: поставте питання з кейсу — <i>Why were the price point and the place on the shelf so important?</i> Це ключова ідея уроку.")]),
 ul([("The video is from 2012 — check it plays and matches the questions before the first lesson.", "Відео 2012 року — перевірте, що воно відтворюється і відповідає питанням, перед першим уроком."),
     ("US spelling <i>yogurt</i>, UK spelling <i>yoghurt</i> — both are correct.", "Американське <i>yogurt</i>, британське <i>yoghurt</i> — обидва правильні.")]),
 "<ol><li>A small feta cheese company in upstate New York.</li><li>A 100-year-old yogurt factory that was being shut down.</li><li>2007; it grew into a $1 billion business.</li><li>Greek yogurt sales were nearly non-existent; now more than a third of the yogurt Americans eat is Greek.</li><li>More than 1,300 jobs and $193 million invested in the old factory.</li></ol>"
 "<p><b>Case question — model:</b> <i>They chose a price point between normal and premium yogurt, so it felt affordable but special. And they insisted on the normal dairy aisle, not specialty stores, so ordinary shoppers could find it.</i></p>"))

S.append(step("s4", "VIDEO · 4", "home + 3 min",
 ("Detail: check facts from the video and the case file; correct false sentences.", "Деталі: перевірити факти з відео й кейсу; виправити хибні речення."),
 ("correct each false sentence aloud in a full sentence.", "виправити кожне хибне речення вголос повним реченням."),
 chips(["Actually, …", "According to the report, …", "In fact, they …"]),
 ol([("In class: only the F sentences, without looking at the explanations.", "На уроці: лише речення з F, не дивлячись на пояснення.")]),
 "",
 "<ol><li>T</li><li>F — he bought an old factory that was being shut down.</li><li>T</li><li>F — Greek yogurt sales were nearly non-existent.</li><li>F — about $1 a cup, between normal (65 cents) and premium Greek ($1.34).</li><li>T — mass supermarkets, not specialty stores.</li></ol>"))

S.append(step("s5", "VIDEO · 5", "5–7 min",
 ("Critical thinking: data vs instinct; transfer to the Ukrainian dairy market.", "Критичне мислення: дані vs інтуїція; перенести на український ринок молочки."),
 ("give an opinion with reasons and suggest one ‘niche’ product and how to research it.", "висловити думку з аргументами і запропонувати один «нішевий» продукт та як його дослідити."),
 chips(["a niche market", "gauge demand", "a test launch", "target audience", "price point", "On the one hand… on the other hand…"]),
 ol([("Base: discuss the question. Push for a concrete Ukrainian example.", "Base: обговоріть питання. Вимагайте конкретний український приклад."),
     ("★ Level up: “Which method?” cards — method + primary/secondary + qualitative/quantitative.", "★ Level up: картки «Which method?» — метод + primary/secondary + qualitative/quantitative.")]),
 ul([("Students may say “data is always right”. Challenge: <i>The data in 2006 said Greek yogurt was under 1% of the market.</i>", "Студенти можуть казати «дані завжди праві». Заперечте: <i>The data in 2006 said Greek yogurt was under 1% of the market.</i>")]),
 "<p><b>Model:</b> <i>On the one hand, the data said it was a niche market. On the other hand, the founder knew real shoppers wanted better yogurt. In Ukraine, high-protein kefir could be a niche that grows — I’d gauge demand with a concept test and a small test launch in a few stores.</i></p>"
 "<p><b>★ Which method?</b> 1 sales data + interviews · 2 blind taste test · 3 desk research · 4 in-store observation / shelf test · 5 survey of category managers + calls · 6 retail audit · 7 review analysis + sensory panel · 8 concept test + test launch</p>"))

S.append(step("s6", "Vocabulary · 6A–B", "5–6 min",
 ("Key collocations of the lesson in a dairy context.", "Ключові колокації уроку в контексті молочки."),
 ("complete the sentences and make one sentence about their company with four collocations.", "заповнити речення і скласти речення про свою компанію з чотирма колокаціями."),
 chips(["online surveys", "focus group", "customer satisfaction", "in-depth interviews", "desk research", "launch a product", "target audience", "sample size"]),
 ol([("6A alone, then <i>Check</i>; 6B click the type.", "6A самостійно, потім <i>Check</i>; 6B — клікнути тип."),
     ("Ask: <i>Which of these does your company use? Give an example.</i>", "Спитайте: <i>Which of these does your company use? Give an example.</i>")]),
 ul([("<b>research</b> is uncountable — no <i>researches</i>.", "<b>research</b> незлічуване — без <i>researches</i>.")]),
 "<p><b>6A:</b> 1 online · 2 focus · 3 customer · 4 in-depth · 5 desk · 6 launch · 7 target · 8 sample</p>"
 "<p><b>6B:</b> adjective + noun: online surveys, in-depth interviews · verb + noun: launch a product · noun + noun: focus groups, customer satisfaction, desk research, target audience, sample size</p>"))

S.append(step("s7", "Vocabulary · 7", "4–5 min",
 ("Meaning and pronunciation of ten key terms.", "Значення і вимова десяти ключових термінів."),
 ("match all words and pronounce them correctly.", "зіставити всі слова й правильно їх вимовити."),
 chips(["quantitative", "qualitative", "product tester", "impact", "respondent", "gauge", "researcher", "gather", "viable", "data analysis"]),
 ol([("Base: match, then <i>Check</i>.", "Base: зіставити, потім <i>Check</i>."),
     ("★ Level up: dairy research words — say the word and tell a story from work.", "★ Level up: слова молочної галузі — назвати слово й розповісти історію з роботи.")]),
 ul(["<b>gauge</b> /ɡeɪdʒ/ · <b>qualitative</b> /ˈkwɒlɪtətɪv/ · <b>quantitative</b> /ˈkwɒntɪtətɪv/ · <b>viable</b> /ˈvaɪəbl/",
     ("In dairy a <b>product tester</b> is usually a <i>taster</i> or a <i>sensory panel member</i>.", "У молочці <b>product tester</b> — зазвичай <i>taster</i> або <i>sensory panel member</i>.")]),
 "<p><b>7:</b> 1 g · 2 c · 3 f · 4 h · 5 a · 6 d · 7 e · 8 j · 9 b · 10 i</p>"
 "<p><b>★ Level up:</b> blind tasting · sensory panel · shelf life · SKU · private label · retail audit · market share · category manager · mystery shopping</p>"))

S.append(step("s8", "Vocabulary · 8", "3–4 min",
 ("Deeper understanding of the underlined words.", "Глибше розуміння підкреслених слів."),
 ("choose the right option and explain why the other one is wrong.", "обрати варіант і пояснити, чому інший неправильний."),
 chips(["qualitative research", "primary research", "customer satisfaction", "viable", "sample size", "gauge"]),
 ol([("Ask <i>Why not the other one?</i> after each item. ★ Level up: verbs that go with the nouns.", "Після кожного пункту питайте <i>Why not the other one?</i> ★ Level up: дієслова до іменників.")]),
 "",
 "<p><b>8:</b> 1 information about why shoppers like or dislike a product · 2 collecting new data · 3 surveys, complaints and repeat-purchase data · 4 has · 5 people · 6 watch their reactions in a taste test</p>"
 "<p><b>★ Verbs:</b> research — carry out / conduct / commission / outsource · data — gather / collect / analyse / interpret · a survey — design / run / send out / fill in · feedback — get / collect / act on / ignore · a product — launch / test / roll out / withdraw / relaunch · a taste test — run / carry out / take part in / pass</p>"))

S.append(step("s9", "Vocabulary · 9", "5–7 min",
 ("Fluency with the target vocabulary.", "Вільне мовлення з цільовою лексикою."),
 ("speak for two minutes and use <b>at least six words from 6A and 7</b>.", "говорити дві хвилини й вжити <b>щонайменше шість слів із 6A і 7</b>."),
 chips(["launch a product", "target audience", "sample size", "gather data", "gauge", "viable", "customer satisfaction", "desk research"]),
 ol([("Tick the words as the student uses them. If fewer than six, ask a question that needs a missing word: <i>How many shoppers would you ask?</i> → sample size.", "Відмічайте вжиті слова. Якщо менше шести — питання, що потребує пропущеного слова: <i>How many shoppers would you ask?</i> → sample size."),
     ("★ Level up: real dairy cases; you play a sceptical CEO or retail buyer.", "★ Level up: реальні кейси з молочки; ви граєте скептичного CEO чи байєра мережі.")]),
 "",
 "<p><b>Model:</b> <i>Before we launch a product, we need to know if it’s viable. First, desk research: market reports and the chains’ sales data. Then we gather data from the target audience — an online survey to gauge interest and a blind taste test with a sample size of about 100 shoppers. Customer satisfaction after the launch we track through repeat purchases and complaints.</i></p>"))

S.append(step("s10", "PROJECT · 10A–D", "25–30 min",
 ("Integrate all vocabulary and skills: brand profile → survey → interview → presentation, on dairy products.", "Об’єднати лексику й навички: профіль бренду → опитування → інтерв’ю → презентація, на молочних продуктах."),
 ("describe two dairy brands, write a balanced survey, interview a shopper or a buyer with good questions and present findings with reporting verbs.", "описати два молочні бренди, скласти збалансоване опитування, провести інтерв’ю з покупцем чи байєром і презентувати висновки з reporting verbs."),
 "",
 "<h4>10A · 5 min</h4>" + ol([("Two brands, fill in the table; the words under each row are compulsory. Target: <b>7/10</b> in the checklist.", "Два бренди, заповнити таблицю; слова під рядками обов’язкові. Мета: <b>7/10</b> у чеклісті."),
                               ("Encourage “Our brand vs our main competitor” — very motivating for company staff.", "Заохочуйте варіант «Our brand vs our main competitor» — для працівників компанії це дуже мотивує.")]) +
 "<h4>10B · 7 min</h4>" + ol([("Fix the bad questions, then a six-question survey; <i>Check my mix</i> shows all four types.", "Виправити погані питання, потім опитування з шести питань; <i>Check my mix</i> показує всі чотири типи.")]) +
 "<h4>10C · 8 min</h4>" + ol([("Choose a persona: <b>Olena</b> (category manager) for sales / key account staff, <b>Iryna</b> (mother of two) for marketing / R&D, <b>Andrii</b> (coffee shops) for B2B / HoReCa.", "Оберіть персонажа: <b>Olena</b> (категорійна менеджерка) для продажів / key account, <b>Iryna</b> (мама двох дітей) для маркетингу / R&D, <b>Andrii</b> (кав’ярні) для B2B / HoReCa."),
                               ("Reward good questions with concrete details; answer bad ones with empty compliments, then ask <i>Was that useful data?</i> Use the bingo.", "На хороші питання — конкретні деталі; на погані — порожні компліменти, потім <i>Was that useful data?</i> Використовуйте бінго.")]) +
 "<h4>10D · 7 min</h4>" + ol([("Four boxes → <i>Build my script</i> → two-minute presentation without reading; feedback checklist.", "Чотири поля → <i>Build my script</i> → двохвилинна презентація без читання; чекліст фідбеку."),
                               ("★ Level up: read the buyer’s / CEO’s challenges one by one.", "★ Level up: читайте заперечення байєра / CEO по одному.")]),
 ul([("<i>suggest + -ing / that…</i>, not <i>suggest to do</i>; <i>admit that…</i>; <i>raise concerns that…</i>", "<i>suggest + -ing / that…</i>, а не <i>suggest to do</i>; <i>admit that…</i>; <i>raise concerns that…</i>"),
     ("Staff often defend their own product instead of listening. Stop them: <i>Are you asking or selling?</i>", "Працівники часто захищають свій продукт замість слухати. Зупиняйте: <i>Are you asking or selling?</i>")]),
 "<h4>10A — model (Halychyna vs Yahotynske kefir)</h4><p><i>Both brands attract customers with a familiar, traditional product; their target audience is families who buy dairy several times a week. The promise is freshness and a natural taste, so shelf life and customer satisfaction are key. Both are formidable competitors because they get good shelf space in big chains. For the ideal customer the main pain point is trust in quality, and the price point must stay affordable.</i></p>"
 "<h4>10B — better questions</h4><ol><li>Tell me about the last time you bought kefir. Which one did you choose and why?</li><li>What do you look at first when you choose yoghurt on the shelf?</li><li>Which flavours have you tried recently? What didn’t you like about them?</li><li>How much do you usually pay for milk? When do you choose a more expensive one? <i>(the question tag in the original biases the answer)</i></li></ol>"
 "<p><b>Good survey (high-protein kefir):</b> 1 How often do you buy kefir? (multiple-choice, quant.) · 2 Do you check the protein content on the label? (yes/no, quant.) · 3 How satisfied are you with the kefir you buy now, 1–10? (rating, quant.) · 4 Tell us about the last time you looked for a high-protein snack. (open-ended, qual.) · 5 Where do you usually buy dairy? (multiple-choice) · 6 What don’t you like about high-protein products you’ve tried? (open-ended, qual.)</p>"
 "<h4>10D — model script</h4><p><i>Our target audience is people aged 25–40 who go to the gym. Over half of the respondents admitted that they buy protein snacks every week, and several raised concerns that these products contain too much sugar. The burning problem is a healthy, affordable protein snack, so it warrants a new product. As a next step, we’ll run a blind taste test with 100 shoppers and a test launch in ten stores to get hard data.</i></p>"
 "<h4>★ Challenges — model replies</h4><ul>"
 "<li>Hard data or compliments? — <i>Not compliments: 60 of 100 shoppers chose our sample in the blind tasting.</i></li>"
 "<li>Fifteen people isn’t a sample size. — <i>Right, that was a pilot. Next we’ll test with 100 shoppers in three cities.</i></li>"
 "<li>Why should a chain give us shelf space? — <i>Because the category is growing and we’ll support the launch with promotions and tastings in store.</i></li>"
 "<li>Shoppers won’t pay more. — <i>Our price point is between the standard and the premium kefir — like Chobani’s strategy.</i></li>"
 "<li>Our competitor is formidable. — <i>Yes, so we won’t copy them; we focus on a pain point they ignore: sugar.</i></li></ul>"))

S.append(step("s11", "Self-assessment · ✓", "3–5 min",
 ("Reflection; see which words were used.", "Рефлексія; побачити, які слова вжито."),
 ("give an honest score, tick used words, write five phrases.", "чесно оцінити себе, відмітити слова, записати п’ять фраз."),
 "",
 ol([("Target: <b>10+</b> words ticked. Unused words go to My phrases — that is the homework list.", "Мета: <b>10+</b> відмічених слів. Невжиті слова йдуть у My phrases — це список на домашку."),
     ("Homework idea: five sentences about their company’s products with the unused words.", "Ідея домашки: п’ять речень про продукти своєї компанії з невжитими словами.")]),
 "",
 "<p>%s</p>" % T("No fixed answers. If the score is 0–2, repeat 6–8 next lesson.", "Фіксованих відповідей немає. Якщо оцінка 0–2, повторіть 6–8 на наступному уроці.")))
'''
exec(compile(head + content + tail, "build_zv_teacher_1-1", "exec"), {"__name__": "__main__"})
