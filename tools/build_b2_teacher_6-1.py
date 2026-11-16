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
IDEA = block("aim", T("The big idea of the lesson", "Головна ідея уроку"), "<p>%s</p><p>%s</p>" % (
  T("<b>A low price is never the whole price.</b> Someone always pays the rest: garment workers (long hours, pay per piece), the planet (clothes made not to last) and the shopper (apps designed to make us buy more than we need). The lesson asks: <i>who is responsible — the brand, the factory, the app designers or us?</i>",
    "<b>Низька ціна — ніколи не вся ціна.</b> Решту завжди хтось платить: швачки (довгі години, оплата за штуку), планета (одяг, зроблений не на довго) і покупець (застосунки, спроєктовані, щоб ми купували більше, ніж треба). Урок ставить питання: <i>хто відповідає — бренд, фабрика, дизайнери застосунку чи ми самі?</i>"),
  T("<b>Why it matters for an IT student:</b> the book’s fashion topic becomes a product-design topic. The same ethical question — <i>is it OK to make money this way?</i> — applies to the apps, interfaces and growth tactics that IT people build every day.",
    "<b>Чому це важливо для студентки з IT:</b> тема моди з книги стає темою продуктового дизайну. Те саме етичне питання — <i>чи нормально так заробляти?</i> — стосується застосунків, інтерфейсів і growth-тактик, які айтівці роблять щодня.")))
BG = block("run", T("Background you need (5-minute read)", "Що треба знати з теми (читання на 5 хвилин)"),
  "<h4>%s</h4>%s<h4>%s</h4>%s<h4>%s</h4>%s" % (
  T("1. Fast vs ultra-fast fashion", "1. Fast fashion vs ultra-fast fashion"),
  ul([("<b>Fast fashion</b> (Zara, H&M): new trends in shops every few weeks, cheap, made quickly.", "<b>Fast fashion</b> (Zara, H&M): нові тренди в магазинах кожні кілька тижнів, дешево, швидко."),
      ("<b>Ultra-fast fashion</b> (Shein, Temu): online only, thousands of new items every day, prices from about €4, delivery in a few days.", "<b>Ultra-fast fashion</b> (Shein, Temu): лише онлайн, тисячі нових речей щодня, ціни від приблизно €4, доставка за кілька днів.")]),
  T("2. How Shein’s model works (from the video)", "2. Як працює модель Shein (з відео)"),
  ol([("Shein owns no factories. It uses a network of <b>independent workshops</b> in Guangzhou (about 50,000 clothes businesses in the city).", "Shein не має власних фабрик. Працює з мережею <b>незалежних цехів</b> у Гуанчжоу (у місті близько 50 000 швейних бізнесів)."),
      ("<b>On-demand model:</b> small batches of 50–100 pieces are tested online; real-time sales data goes back to suppliers; items that sell are reordered at once.", "<b>On-demand модель:</b> малі партії по 50–100 штук тестують онлайн; дані продажів у реальному часі йдуть постачальникам; те, що продається, одразу дозамовляють."),
      ("When an item goes viral, Shein orders it from <b>several factories</b> → competition → lower prices → thin <b>profit margins</b> → low wages.", "Коли річ стає вірусною, Shein замовляє її в <b>кількох фабриках</b> → конкуренція → нижчі ціни → тонкі <b>profit margins</b> → низькі зарплати."),
      ("Workers are often <b>paid per piece</b> (6–24 cents per item, China Labor Watch). Busy months can bring €1,600, but only with work until midnight. Shein’s own limit is 60 hours a week; some work more than 75.", "Працівникам часто <b>платять за штуку</b> (6–24 центи за річ, China Labor Watch). У сезон можна заробити €1 600, але лише працюючи до опівночі. Власний ліміт Shein — 60 годин на тиждень; дехто працює понад 75."),
      ("Shein’s position: the on-demand model <b>reduces waste</b> (less unsold stock), and suppliers must follow local labour law.", "Позиція Shein: on-demand модель <b>зменшує відходи</b> (менше непроданого товару), а постачальники мусять дотримуватися місцевого трудового законодавства.")]),
  T("3. Dark patterns: the app side", "3. Dark patterns: бік застосунку"),
  "<p>%s</p>" % T("<b>Dark patterns</b> are interface tricks that push users to do what the company wants, not what they planned. Examples linked to Shein and Temu in EU complaints and decisions (2025–2026):", "<b>Dark patterns</b> — трюки інтерфейсу, які штовхають користувача робити те, що вигідно компанії, а не те, що він планував. Приклади, які у скаргах і рішеннях ЄС (2025–2026) пов’язують із Shein і Temu:") +
  '<table class="tt"><tr><th>Pattern</th><th>%s</th></tr>' % T("What it does", "Що робить") + "".join("<tr><td><b>%s</b></td><td>%s</td></tr>" % (a, T(b, c)) for a, b, c in [
   ("fake discount", "shows a ‘was’ price that never really existed", "показує «стару» ціну, якої насправді не було"),
   ("pressure selling / countdown timer", "‘Only 2 hours left!’ — a false deadline to make you buy now", "«Залишилось 2 години!» — фальшивий дедлайн, щоб купили зараз"),
   ("low-stock message", "‘Only 3 left!’ — may not be true", "«Лишилось 3 штуки!» — може бути неправдою"),
   ("endless scroll", "the feed never ends, so you never stop looking", "стрічка ніколи не закінчується, тож ви не зупиняєтесь"),
   ("gamification", "spin-the-wheel discounts, coins, daily rewards", "колесо знижок, монетки, щоденні бонуси"),
   ("confirm-shaming", "‘No thanks, I don’t like saving money’", "«Ні, дякую, я не люблю економити»")]) + "</table>" +
  "<p>%s</p>" % T("<b>What regulators did:</b> the EU told Shein to stop fake discounts and pressure selling (May 2025); France fined Shein €40 million for misleading discounts (July 2025); the EU fined Temu €200 million under the Digital Services Act for failing to assess the risk of illegal products (2026).",
                  "<b>Що зробили регулятори:</b> ЄС вимагав від Shein припинити фальшиві знижки й pressure selling (травень 2025); Франція оштрафувала Shein на €40 млн за оманливі знижки (липень 2025); ЄС оштрафував Temu на €200 млн за Digital Services Act — через неналежну оцінку ризику незаконних товарів (2026).")))
ARG = block("tgt", T("Both sides — so you can play devil’s advocate", "Обидві сторони — щоб ви могли грати «адвоката диявола»"),
  '<table class="tt"><tr><th>%s</th><th>%s</th></tr>' % (T("For ultra-fast fashion", "За ultra-fast fashion"), T("Against", "Проти")) + "".join("<tr><td>%s</td><td>%s</td></tr>" % (T(a, b), T(c, d)) for a, b, c, d in [
   ("Fashion becomes affordable for people with low incomes.", "Мода стає доступною людям із невисокими доходами.", "Someone pays the real price: workers with 75-hour weeks and pay per piece.", "Реальну ціну платить хтось інший: працівники з 75-годинним тижнем і оплатою за штуку."),
   ("On-demand production means less unsold stock and waste.", "On-demand виробництво — менше непроданого товару й відходів.", "Low quality + huge volume = clothes that are thrown away fast (disposability).", "Низька якість + величезний обсяг = одяг, який швидко викидають (disposability)."),
   ("Jobs for thousands of people in Guangzhou; some earn double the average wage.", "Робота для тисяч людей у Гуанчжоу; дехто заробляє вдвічі більше за середнє.", "Those wages need work until midnight; the brand’s own 60-hour limit is broken.", "Такі гроші — лише з роботою до опівночі; власний ліміт бренду в 60 годин порушують."),
   ("Users choose freely; nobody forces them to buy.", "Користувачі вибирають самі; ніхто не змушує купувати.", "Dark patterns are designed to weaken free choice.", "Dark patterns саме для того й створені, щоб послабити вільний вибір.")]) + "</table>" +
  "<p>%s</p>" % T("The expert in the video says <b>responsibility is shared</b>: brands produce, but consumers in the West drive the demand. This is the key idea for the final discussion.", "Експертка у відео каже, що <b>відповідальність спільна</b>: бренди виробляють, але попит створюють споживачі на Заході. Це ключова думка для фінальної дискусії."))
VMAP = block("watch", T("Video map (FRANCE 24, 6:10)", "Карта відео (FRANCE 24, 6:10)"),
  '<table class="tt"><tr><th>⏱</th><th>%s</th></tr>' % T("What happens", "Що відбувається") + "".join("<tr><td>%s</td><td>%s</td></tr>" % (a, T(b, c)) for a, b, c in [
   ("0:00–0:58", "Guangzhou morning: workers look for jobs; they choose by the price per piece.", "Ранок у Гуанчжоу: люди шукають роботу; вибирають за ціною за штуку."),
   ("0:58–2:25", "Shein’s network of independent workshops; a producer shows stretchy clothes; the on-demand model.", "Мережа незалежних цехів Shein; виробник показує одяг, що тягнеться; on-demand модель."),
   ("2:25–3:47", "Viral items, competition between factories, thin margins, pay per piece, work until midnight, 60 vs 75 hours.", "Вірусні речі, конкуренція фабрик, тонкі маржі, оплата за штуку, робота до опівночі, 60 vs 75 годин."),
   ("3:47–5:07", "Delivery in days, €4 items; the expert from Redress: low quality, disposability, shared responsibility.", "Доставка за кілька днів, речі за €4; експертка з Redress: низька якість, disposability, спільна відповідальність."),
   ("5:07–6:10", "Shein’s statement: less waste, suppliers follow local law. Night: factory lights still on.", "Заява Shein: менше відходів, постачальники дотримуються закону. Ніч: у цехах досі світло.")]) + "</table>")
GLOS = block("ans", T("Glossary", "Глосарій"),
  '<table class="tt"><tr><th>Word</th><th>%s</th></tr>' % T("Meaning", "Значення / переклад") + "".join("<tr><td><b>%s</b></td><td>%s</td></tr>" % (a, T(b, c)) for a, b, c in [
   ("garment", "a piece of clothing", "предмет одягу"), ("supplier / supplier factory", "a company that makes goods for a brand", "постачальник / фабрика-постачальник"),
   ("supply chain", "all the steps and companies from raw material to the shopper", "ланцюг постачання"), ("sweatshop", "a factory with very long hours, low pay and bad conditions", "потогонне виробництво"),
   ("paid per piece", "money for each item you make, not for hours", "оплата за штуку (відрядна)"), ("profit margin", "the part of the price that is profit", "маржа, прибуток з одиниці"),
   ("on-demand model", "producing only what customers are buying now", "виробництво під попит"), ("labour law", "laws about working hours, pay and rights", "трудове законодавство"),
   ("ethically sourced", "made or bought in a fair, responsible way", "етично закуплений / вироблений"), ("fair-trade cotton", "cotton bought at a fair price from farmers", "бавовна fair trade (справедлива торгівля)"),
   ("unethical conduct", "wrong, dishonest behaviour", "неетична поведінка"), ("disposability", "the idea that things are cheap and can be thrown away", "одноразовість, «викинути не шкода»"),
   ("polluter", "a company that damages the environment", "забруднювач"), ("dark patterns", "design tricks that push users to act against their interests", "маніпулятивні патерни інтерфейсу"),
   ("pressure selling", "making people buy quickly with false urgency", "продаж під тиском"), ("be accused of", "people say you did something wrong", "бути звинуваченим у")]) + "</table>")
S.append("""<section id="s0" class="sec on"><div class="bsec">%s</div>%s%s%s%s%s%s%s%s%s</section>""" % (
 T("Overview", "Огляд уроку"), IDEA, BG, VMAP, ARG, GLOS,
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
