"""Zvenyhora (dairy) B2+ 1.1 — Teacher's Book page (EN / UK).
Reuses helpers, CSS and JS from build_b2p_teacher_1-1.py; the content is dairy-specific.
Usage: python3 build_zv_teacher_1-1.py OUT.html
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(HERE, "build_b2p_teacher_1-1.py")).read()
head = base[:base.index("S = []")]
tail = base[base.index("NAV = (") :]
tail = (tail.replace("<title>1.1 Research in tech — Teacher’s Book</title>", "<title>1.1 Market research: hard cheese — Teacher’s Book</title>")
            .replace("<h1>Research in tech</h1>", "<h1>Market research: hard cheese</h1>"))

content = r'''
S = []
S.append("""<section id="s0" class="sec on"><div class="bsec">%s</div>%s%s%s%s%s</section>""" % (
 T("Overview", "Огляд уроку"),
 block("aim", T("Lesson outcome", "Outcome уроку"), "<p>%s</p>" % T(
  "The student can use a range of vocabulary related to market research in the cheese business, explain what makes shoppers pay more for hard cheese, ask good questions to shoppers, retail buyers and chefs, and present findings.",
  "Студент вживає лексику про дослідження ринку в сирному бізнесі, пояснює, за що покупці готові платити більше за твердий сир, ставить хороші питання покупцям, байєрам мереж і шеф-кухарям і презентує висновки.")),
 block("run", T("Who the course is for", "Для кого курс"), ul([
  ("Staff of Zveni Hora (Savencia group): marketing, sales and key account managers, R&D / quality, production. Their customers are <b>shoppers</b>, <b>retail chains</b> (category managers) and <b>HoReCa</b> (restaurants). Many work with the French head office.",
   "Працівники «Звени Гора» (група Savencia): маркетинг, продажі та key account, R&D / якість, виробництво. Їхні клієнти — <b>покупці</b>, <b>торговельні мережі</b> (категорійні менеджери) і <b>HoReCa</b> (ресторани). Багато хто працює з французьким головним офісом."),
  ("<b>Before the lesson (home):</b> watch three parts of the parmesan video (about 6 minutes) and do Exercises 2–4. <b>In class:</b> speaking — 1, 5, 6–9, project 10, self-assessment.",
   "<b>До уроку (вдома):</b> подивитися три частини відео про пармезан (близько 6 хвилин) і зробити вправи 2–4. <b>На уроці:</b> говоріння — 1, 5, 6–9, проєкт 10, самооцінка."),
  ("<b>Base / ★ Level up:</b> Base = the coursebook tasks; Level up = extra cheese-industry tasks for strong students.",
   "<b>Base / ★ Level up:</b> Base — завдання з книги; Level up — додаткові завдання з сирної галузі для сильних студентів.")])),
 block("tgt", T("Timing (about 80 minutes)", "Таймінг (близько 80 хвилин)"),
  '<table class="tt"><tr><th>#</th><th>%s</th><th>%s</th></tr>' % (T("Stage", "Етап"), T("Time", "Час")) + "".join(
   "<tr><td>%s</td><td>%s</td><td>%s</td></tr>" % (a, T(b, c), d) for a, b, c, d in [
    ("1", "Lead-in", "Lead-in", "5–7 min"), ("2–4", "Video and case file: check", "Відео й кейс: перевірка", "8–10 min"),
    ("5", "Discussion: could a Ukrainian cheese sell a story?", "Обговорення: чи може український сир продавати історію?", "5–7 min"), ("6–8", "Vocabulary", "Лексика", "12–15 min"),
    ("9", "Speaking with the target vocabulary", "Говоріння з цільовою лексикою", "5–7 min"), ("10", "Project A–D", "Проєкт A–D", "25–30 min"),
    ("✓", "Self-assessment", "Самооцінка", "3–5 min")]) + "</table>"),
 block("watch", T("Cheat sheet: how to talk about market research for cheese", "Шпаргалка: як говорити про дослідження ринку сиру"),
  "<p>%s</p>" % T("The main idea: <b>a new cheese, format, pack or price should be based on data about shoppers, retail chains and chefs — not on the opinion of the boss.</b> In the cheese business, research means tastings and sensory panels, retail sales data, store checks, complaints, talking to category managers and chefs, and price tests.",
                  "Головна думка: <b>новий сир, формат, упаковка чи ціна мають спиратися на дані про покупців, мережі й шеф-кухарів — а не на думку керівника.</b> У сирному бізнесі дослідження — це дегустації та сенсорні панелі, дані продажів мереж, перевірки в магазинах, скарги, розмови з категорійними менеджерами й шефами, цінові тести.") +
  '<table class="tt"><tr><th>%s</th><th>%s</th><th>%s</th></tr>' % (T("Pair", "Пара"), T("Meaning", "Значення"), T("Cheese example", "Приклад із сиром")) + "".join(
   "<tr><td><b>%s</b></td><td>%s</td><td>%s</td></tr>" % (a, T(b, c), T(d, e)) for a, b, c, d, e in [
    ("primary vs secondary research", "new data you collect yourself vs data that already exists", "нові дані, які збираєш сам, vs дані, що вже є",
     "our own tasting in a supermarket vs a market report on Ukrainian cheese", "власна дегустація в супермаркеті vs звіт про ринок сиру в Україні"),
    ("quantitative vs qualitative", "numbers (how many?) vs opinions and reasons (why?)", "цифри (скільки?) vs думки й причини (чому?)",
     "sales by SKU, market share, tasting scores vs interviews with chefs about melting and saltiness", "продажі за SKU, частка ринку, оцінки дегустації vs інтерв’ю з шефами про плавлення й солоність"),
    ("survey vs focus group", "many people, short answers vs 6–10 people, a long discussion", "багато людей, короткі відповіді vs 6–10 людей, довга розмова",
     "a QR-code survey on the pack vs a group comparing three aged cheeses", "опитування за QR-кодом на упаковці vs група, що порівнює три витримані сири")]) + "</table>" +
  "<p>%s</p>" % T("<b>Easy way in:</b> everyone has tasted cheese at a promo stand. Ask: <i>Did you buy it afterwards? Why / why not?</i> Then: <i>Why do people pay $1,000 for a wheel of parmesan?</i>",
                  "<b>Як зайти в тему:</b> усі куштували сир на промостійці. Спитайте: <i>Did you buy it afterwards? Why / why not?</i> А потім: <i>Why do people pay $1,000 for a wheel of parmesan?</i>")),
 block("ans", T("By the end of the lesson the student should…", "До кінця уроку студент має…"), ul([
  ("use at least <b>10 words or phrases</b> from the vocabulary box while speaking (✓ checklist);", "вжити щонайменше <b>10 слів або фраз</b> із блоку лексики (чекліст на кроці ✓);"),
  ("ask <b>5 good questions</b> to a shopper, a category manager or a chef about real past behaviour (10B–10C);", "поставити <b>5 хороших питань</b> покупцю, категорійному менеджеру чи шефу про реальну поведінку в минулому (10B–10C);"),
  ("present findings with <b>reporting verbs</b> (10D).", "презентувати висновки з <b>reporting verbs</b> (10D).")]))))

S.append(step("s1", "Lead-in · 1", "5–7 min",
 ("Activate the topic through the student’s experience as a shopper and as a cheese professional.", "Активувати тему через досвід студента як покупця і як фахівця сирної галузі."),
 ("talk for about a minute, with reasons and an example from their company.", "говорити близько хвилини з причинами і прикладом зі своєї компанії."),
 chips(["fill in a survey", "a tasting / a promo stand", "shoppers", "retail chains", "chefs / HoReCa", "find out"]),
 ol([("Choose 3–4 Base questions; with a strong student switch to ★ Level up.", "Оберіть 3–4 питання Base; із сильним студентом перейдіть на ★ Level up."),
     ("Always ask for an example from their plant, brand or clients.", "Завжди просіть приклад зі свого заводу, бренду чи клієнтів.")]),
 ul([("<b>shopper</b> (in the shop) vs <b>consumer</b> (eats it) vs <b>customer</b> (pays — often the retail chain or a restaurant).", "<b>shopper</b> (у магазині) vs <b>consumer</b> (їсть) vs <b>customer</b> (платить — часто мережа чи ресторан)."),
     ("<b>hard cheese</b> (not <i>solid cheese</i>); <b>aged / matured cheese</b>; <b>a cheese product</b> = with vegetable fat, not real cheese.", "<b>hard cheese</b> (не <i>solid cheese</i>); <b>aged / matured cheese</b>; <b>a cheese product</b> — з рослинним жиром, не справжній сир.")]),
 ul(["<b>Why do cheese companies need research?</b> — <i>To reduce the risk of a launch, understand shoppers, chains and chefs, and see what competitors do.</i>",
     "<b>What do they want to know?</b> — <i>Who buys the cheese, why, which format and price point work, what they think about taste, texture and the pack.</i>"])))

S.append(step("s2", "VIDEO · 2", "home / 2 min",
 ("Prediction before watching.", "Прогноз перед переглядом."),
 ("make two lists: why parmesan is expensive; how a cheese company can learn what shoppers want.", "скласти два списки: чому пармезан дорогий; як сирна компанія дізнається, чого хочуть покупці."),
 chips(["tasting", "survey", "focus group", "sales data", "talk to retail buyers / chefs"]),
 ol([("At home the student writes the lists; in class compare with the video and the case file.", "Вдома студент пише списки; на уроці порівнює з відео та кейсом.")]),
 "",
 "<p><b>Why expensive:</b> <i>long ageing, a lot of milk, only one region, certified dairies, tradition, a protected name, strong demand.</i></p><p><b>How to learn:</b> <i>tastings and sensory panels, shopper surveys, focus groups, retail sales data, store checks, complaints and reviews, interviews with category managers and chefs, price tests.</i></p>"))

S.append(step("s3", "VIDEO · 3", "home + 5 min in class",
 ("Listening for specific information in three parts; reading a short research case; noticing useful phrases.", "Слухання конкретної інформації у трьох частинах; читання короткого дослідницького кейсу; помічати корисні фрази."),
 ("answer the questions in their own words, using at least <b>two phrases from “Listen for” per part</b>, and answer the case-file question.", "відповісти своїми словами, вживши щонайменше <b>дві фрази з «Listen for» у кожній частині</b>, і відповісти на питання кейсу."),
 chips(["more than double the price of", "be worth an eye-popping …", "one of the biggest exports", "a restricted area", "a mark of origin", "a master grader", "maturation", "make the price go higher", "counterfeit products", "fight copycats", "protected designation of origin"]),
 ol([("At home: watch each part, answer, check with <i>answer</i>; read the case file.", "Вдома: подивитися кожну частину, відповісти, звірити кнопкою <i>answer</i>; прочитати кейс."),
     ("In class: the case-file question is the bridge to their job — <i>What would you test first for a Ukrainian hard cheese?</i>", "На уроці: питання кейсу — міст до їхньої роботи: <i>What would you test first for a Ukrainian hard cheese?</i>")]),
 ul([("The video uses US units: <b>88 pounds ≈ 40 kg</b>, <b>131 gallons ≈ 500 litres</b>.", "У відео американські одиниці: <b>88 pounds ≈ 40 кг</b>, <b>131 gallons ≈ 500 літрів</b>."),
     ("The narrator is Italian — a good chance to talk about understanding non-native accents at work (like colleagues from Savencia).", "Ведуча — італійка: гарна нагода поговорити про розуміння акцентів неносіїв на роботі (як колеги з Savencia).")]),
 "<p class='fp'><b>Part 1 · 00:00–02:23</b></p><ol><li>Over $1,000; about 88 pounds (40 kg) — over $11 per pound.</li><li>More than double the price of average cheddar.</li><li>3.6 million wheels a year; €2.2 billion — one of Italy’s biggest exports.</li><li>Only in a restricted area of northern Italy; 329 certified dairies; three good bacteria that grow only there.</li><li>Cow’s milk, salt and rennet.</li></ol>"
 "<p class='fp'><b>Part 2 · 06:11–07:58</b></p><ol><li>The mark of origin — it’s the real thing.</li><li>Where and when it was produced.</li><li>A master grader inspects and brands the wheels.</li><li>Longer maturation (2 years on average, up to 10) gives a stronger, nuttier taste; ‘vecchio’ costs about €13 per pound.</li></ol>"
 "<p class='fp'><b>Part 3 · 07:58–09:46</b></p><ol><li>A black market of counterfeit products.</li><li>About €100 billion.</li><li>Protected in the EU as a PDO; struggles for recognition elsewhere.</li><li>The dotted stencil on the rind, or the official logo and PDO mark on the pack.</li></ol>"
 "<p><b>Case question — model:</b> <i>I’d start with a blind tasting and a price test. The Oregon study shows that it depends on the shopper: people who like familiar cheese react to a taste description, adventurous shoppers to an award sticker. And most shoppers buy pre-packed blocks or slices, so the format matters too.</i></p>"))

S.append(step("s4", "VIDEO · 4", "home + 3 min",
 ("Detail: check facts from the video; correct false sentences.", "Деталі: перевірити факти з відео; виправити хибні речення."),
 ("correct each false sentence aloud in a full sentence.", "виправити кожне хибне речення вголос повним реченням."),
 chips(["Actually, …", "According to the video, …", "In fact, it …"]),
 ol([("In class: only the F sentences, without looking at the explanations.", "На уроці: лише речення з F, не дивлячись на пояснення.")]),
 "",
 "<ol><li>F — more than double the price of cheddar.</li><li>F — only in a restricted area of northern Italy, by certified dairies.</li><li>T — milk, salt and rennet.</li><li>T — a plaque made from milk protein.</li><li>F — longer maturation makes the price higher.</li><li>F — protected in the EU, struggles elsewhere.</li></ol>"))

S.append(step("s5", "VIDEO · 5", "5–7 min",
 ("Critical thinking: origin, story and price; transfer to Ukrainian hard cheese.", "Критичне мислення: походження, історія і ціна; перенести на український твердий сир."),
 ("give an opinion with reasons and suggest how to research whether shoppers would pay more.", "висловити думку з аргументами і запропонувати, як дослідити, чи заплатять покупці більше."),
 chips(["a mark of origin", "maturation", "price point", "target audience", "gauge demand", "a test launch", "On the one hand… on the other hand…"]),
 ol([("Base: discuss the question. Push for concrete ideas: region, ageing, the story of the plant since 1982.", "Base: обговоріть питання. Вимагайте конкретики: регіон, витримка, історія заводу з 1982 року."),
     ("★ Level up: “Which method?” cards — method + primary/secondary + qualitative/quantitative.", "★ Level up: картки «Which method?» — метод + primary/secondary + qualitative/quantitative.")]),
 ul([("Students may say “Ukrainians only look at the price”. Ask: <i>How do you know? What data would prove it?</i>", "Студенти можуть казати «українці дивляться тільки на ціну». Спитайте: <i>How do you know? What data would prove it?</i>")]),
 "<p><b>Model:</b> <i>On the one hand, shoppers are price-sensitive right now. On the other hand, a clear story — a cheese aged for 12 months in Zvenyhorodka — could justify a higher price point. I’d gauge demand with a price test and a blind tasting, then a small test launch in a few stores.</i></p>"
 "<p><b>★ Which method?</b> 1 sales data + interviews · 2 blind tasting · 3 desk research · 4 in-store observation / shelf test · 5 interviews with chefs · 6 retail audit · 7 review analysis + sensory panel · 8 price test + test launch</p>"))

S.append(step("s6", "Vocabulary · 6A–B", "5–6 min",
 ("Key collocations of the lesson in a cheese context.", "Ключові колокації уроку в контексті сиру."),
 ("complete the sentences and make one sentence about their company with four collocations.", "заповнити речення і скласти речення про свою компанію з чотирма колокаціями."),
 chips(["online surveys", "focus group", "customer satisfaction", "in-depth interviews", "desk research", "launch a product", "target audience", "sample size"]),
 ol([("6A alone, then <i>Check</i>; 6B click the type. Ask: <i>Which of these does your company use?</i>", "6A самостійно, потім <i>Check</i>; 6B — клікнути тип. Спитайте: <i>Which of these does your company use?</i>")]),
 ul([("<b>research</b> is uncountable — no <i>researches</i>.", "<b>research</b> незлічуване — без <i>researches</i>.")]),
 "<p><b>6A:</b> 1 online · 2 focus · 3 customer · 4 in-depth · 5 desk · 6 launch · 7 target · 8 sample</p>"
 "<p><b>6B:</b> adjective + noun: online surveys, in-depth interviews · verb + noun: launch a product · noun + noun: focus groups, customer satisfaction, desk research, target audience, sample size</p>"))

S.append(step("s7", "Vocabulary · 7", "4–5 min",
 ("Meaning and pronunciation of ten key terms.", "Значення і вимова десяти ключових термінів."),
 ("match all words and pronounce them correctly.", "зіставити всі слова й правильно їх вимовити."),
 chips(["quantitative", "qualitative", "product tester", "impact", "respondent", "gauge", "researcher", "gather", "viable", "data analysis"]),
 ol([("Base: match, then <i>Check</i>. ★ Level up: research and cheese words — say the word and tell a story from work.", "Base: зіставити, потім <i>Check</i>. ★ Level up: слова з досліджень і сироваріння — назвати слово й розповісти історію з роботи.")]),
 ul(["<b>gauge</b> /ɡeɪdʒ/ · <b>qualitative</b> /ˈkwɒlɪtətɪv/ · <b>quantitative</b> /ˈkwɒntɪtətɪv/ · <b>viable</b> /ˈvaɪəbl/ · <b>rind</b> /raɪnd/",
     ("In cheese, a <b>product tester</b> is a <i>taster</i>, a <i>sensory panel member</i> or a <i>grader</i>.", "У сирі <b>product tester</b> — це <i>taster</i>, <i>sensory panel member</i> або <i>grader</i>.")]),
 "<p><b>7:</b> 1 g · 2 c · 3 f · 4 h · 5 a · 6 d · 7 e · 8 j · 9 b · 10 i</p>"
 "<p><b>★ Level up:</b> blind tasting · sensory panel · grader · maturation / ripening · rind · SKU · private label · PDO · counterfeit · retail audit</p>"))

S.append(step("s8", "Vocabulary · 8", "3–4 min",
 ("Deeper understanding of the underlined words.", "Глибше розуміння підкреслених слів."),
 ("choose the right option and explain why the other one is wrong.", "обрати варіант і пояснити, чому інший неправильний."),
 chips(["qualitative research", "primary research", "customer satisfaction", "viable", "sample size", "gauge"]),
 ol([("Ask <i>Why not the other one?</i> ★ Level up: verbs that go with the nouns, incl. <i>age / grade / grate cheese</i>.", "Питайте <i>Why not the other one?</i> ★ Level up: дієслова до іменників, зокрема <i>age / grade / grate cheese</i>.")]),
 "",
 "<p><b>8:</b> 1 information about why shoppers like or dislike a cheese · 2 collecting new data · 3 surveys, complaints and repeat-purchase data · 4 has · 5 people · 6 watch their reactions in a blind tasting</p>"
 "<p><b>★ Verbs:</b> research — carry out / conduct / commission / outsource · data — gather / collect / analyse / interpret · a survey — design / run / send out / fill in · feedback — get / collect / act on / ignore · a product — launch / test / roll out / withdraw / relaunch · cheese — make / age / grade / slice / grate / taste</p>"))

S.append(step("s9", "Vocabulary · 9", "5–7 min",
 ("Fluency with the target vocabulary.", "Вільне мовлення з цільовою лексикою."),
 ("speak for two minutes and use <b>at least six words from 6A and 7</b>.", "говорити дві хвилини й вжити <b>щонайменше шість слів із 6A і 7</b>."),
 chips(["launch a product", "target audience", "sample size", "gather data", "gauge", "viable", "customer satisfaction", "desk research"]),
 ol([("Tick the words used. If fewer than six, ask a question that needs a missing word: <i>How many shoppers would you ask?</i> → sample size.", "Відмічайте вжиті слова. Якщо менше шести — питання, що потребує пропущеного слова: <i>How many shoppers would you ask?</i> → sample size."),
     ("★ Level up: real cheese cases; you play a sceptical manager from head office or a retail buyer.", "★ Level up: реальні кейси із сиром; ви граєте скептичного менеджера з головного офісу чи байєра мережі.")]),
 "",
 "<p><b>Model:</b> <i>Before we launch a new cheese, we need to know if it’s viable. First, desk research on the Ukrainian cheese market and the chains’ sales data. Then we gather data from the target audience: an online survey to gauge interest and a blind tasting with a sample size of about 100 shoppers. After the launch we track customer satisfaction through repeat purchases and complaints.</i></p>"))

S.append(step("s10", "PROJECT · 10A–D", "25–30 min",
 ("Integrate all vocabulary and skills: brand profile → survey → interview → presentation, on hard cheese.", "Об’єднати лексику й навички: профіль бренду → опитування → інтерв’ю → презентація, на твердому сирі."),
 ("describe two cheese brands, write a balanced survey, interview a shopper, buyer or chef with good questions and present findings with reporting verbs.", "описати два сирні бренди, скласти збалансоване опитування, провести інтерв’ю з покупцем, байєром чи шефом і презентувати висновки з reporting verbs."),
 "",
 "<h4>10A · 5 min</h4>" + ol([("Two brands, fill in the table; the words under each row are compulsory. Target: <b>7/10</b>.", "Два бренди, заповнити таблицю; слова під рядками обов’язкові. Мета: <b>7/10</b>."),
                               ("“Our brand vs our main competitor” and “hard cheese vs a ‘cheese product’” work best with company staff.", "Найкраще з працівниками працюють «наш бренд vs головний конкурент» і «твердий сир vs сирний продукт».")]) +
 "<h4>10B · 7 min</h4>" + ol([("Fix the bad questions, then a six-question survey; <i>Check my mix</i> shows all four types.", "Виправити погані питання, потім опитування з шести питань; <i>Check my mix</i> показує всі чотири типи.")]) +
 "<h4>10C · 8 min</h4>" + ol([("Choose a persona: <b>Olena</b> (category manager) for sales / key account, <b>Iryna</b> (mother of two) for marketing / R&D, <b>Andrii</b> (chef, Italian restaurants) for HoReCa / B2B.", "Оберіть персонажа: <b>Olena</b> (категорійна менеджерка) для продажів / key account, <b>Iryna</b> (мама двох дітей) для маркетингу / R&D, <b>Andrii</b> (шеф італійських ресторанів) для HoReCa / B2B."),
                               ("Reward good questions with concrete details; answer bad ones with empty compliments, then ask <i>Was that useful data?</i> Use the bingo.", "На хороші питання — конкретні деталі; на погані — порожні компліменти, потім <i>Was that useful data?</i> Використовуйте бінго.")]) +
 "<h4>10D · 7 min</h4>" + ol([("Four boxes → <i>Build my script</i> → two-minute presentation without reading; feedback checklist.", "Чотири поля → <i>Build my script</i> → двохвилинна презентація без читання; чекліст фідбеку."),
                               ("★ Level up: read the challenges one by one — as a retail buyer or a manager from the French head office.", "★ Level up: читайте заперечення по одному — як байєр мережі чи менеджер французького головного офісу.")]),
 ul([("<i>suggest + -ing / that…</i>, not <i>suggest to do</i>; <i>admit that…</i>; <i>raise concerns that…</i>", "<i>suggest + -ing / that…</i>, а не <i>suggest to do</i>; <i>admit that…</i>; <i>raise concerns that…</i>"),
     ("Staff often defend their own cheese instead of listening. Stop them: <i>Are you asking or selling?</i>", "Працівники часто захищають свій сир замість слухати. Зупиняйте: <i>Are you asking or selling?</i>")]),
 "<h4>10A — model (Parmigiano Reggiano vs Grana Padano)</h4><p><i>Both brands attract customers with Italian tradition; their target audience is people who cook Italian food. Parmigiano promises a long maturation and a protected origin, so customer satisfaction comes from the strong, nutty taste. Grana Padano is a formidable competitor: it has a lot of shelf space and a lower price point. For the ideal customer the pain point is price — real parmesan is expensive, so many choose the cheaper option.</i></p>"
 "<h4>10B — better questions</h4><ol><li>Tell me about the last time you bought hard cheese. Which one did you choose and why?</li><li>What do you look at first when you choose cheese on the shelf?</li><li>Which cheeses have you tried recently? What didn’t you like about them?</li><li>How much do you usually pay for hard cheese? When do you choose a more expensive one? <i>(the question tag in the original biases the answer)</i></li></ol>"
 "<p><b>Good survey (12-month aged cheese, pre-grated):</b> 1 How often do you buy hard cheese? (multiple-choice, quant.) · 2 Do you buy pre-grated cheese? (yes/no, quant.) · 3 How satisfied are you with the hard cheese you buy now, 1–10? (rating, quant.) · 4 Tell us about the last time you cooked with hard cheese. (open-ended, qual.) · 5 Where do you usually buy cheese? (multiple-choice) · 6 What don’t you like about the cheese you buy now? (open-ended, qual.)</p>"
 "<h4>10D — model script</h4><p><i>Our target audience is people who cook Italian food at home and restaurants that can’t afford imported parmesan. Over half of the respondents admitted that they buy cheaper cheese because of the price, and several raised concerns that Ukrainian hard cheese melts badly. The burning problem is an affordable cheese that tastes and melts like parmesan, so it warrants a new product. As a next step, we’ll run a blind tasting with 100 shoppers and a test with five restaurants to get hard data.</i></p>"
 "<h4>★ Challenges — model replies</h4><ul>"
 "<li>Hard data or compliments? — <i>Not compliments: 60 of 100 shoppers chose our sample in the blind tasting.</i></li>"
 "<li>Fifteen people isn’t a sample size. — <i>Right, that was a pilot. Next we’ll test with 100 shoppers in three cities.</i></li>"
 "<li>Why more shelf space? — <i>Because the category is growing and we’ll support the launch with tastings in store.</i></li>"
 "<li>Shoppers won’t pay more. — <i>Our price point is between the cheese products and imported parmesan, and the 12-month maturation justifies it.</i></li>"
 "<li>Formidable competitor? — <i>Yes, so we focus on a pain point they ignore: stable quality for restaurants.</i></li></ul>"))

S.append(step("s11", "Self-assessment · ✓", "3–5 min",
 ("Reflection; see which words were used.", "Рефлексія; побачити, які слова вжито."),
 ("give an honest score, tick used words, write five phrases.", "чесно оцінити себе, відмітити слова, записати п’ять фраз."),
 "",
 ol([("Target: <b>10+</b> words ticked. Unused words go to My phrases — the homework list.", "Мета: <b>10+</b> відмічених слів. Невжиті слова йдуть у My phrases — список на домашку."),
     ("Homework idea: five sentences about Zveni Hora’s cheeses with the unused words.", "Ідея домашки: п’ять речень про сири «Звени Гора» з невжитими словами.")]),
 "",
 "<p>%s</p>" % T("No fixed answers. If the score is 0–2, repeat 6–8 next lesson.", "Фіксованих відповідей немає. Якщо оцінка 0–2, повторіть 6–8 на наступному уроці.")))
'''
exec(compile(head + content + tail, "build_zv_teacher_1-1", "exec"), {"__name__": "__main__"})
