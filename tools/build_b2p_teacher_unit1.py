"""B2+ Unit 1 guide for teachers (Ukrainian): lesson logic, outcomes, vocabulary, adaptation.
Usage: python3 build_b2p_teacher_unit1.py OUT.html it|zv
Based on the doc "B2+ Unit 1 · Market research — логика уроков и outcomes".
"""
import sys
OUT, V = sys.argv[1], sys.argv[2]
ZV = V == "zv"

def P(t): return "<p>%s</p>" % t
def B(t): return "<b>%s</b>" % t
def I(t): return "<i>%s</i>" % t
def UL(xs): return "<ul>" + "".join("<li>%s</li>" % x for x in xs) + "</ul>"
def OL(xs): return "<ol>" + "".join("<li>%s</li>" % x for x in xs) + "</ol>"
def TAB(head, rows): return "<table><tr>" + "".join("<th>%s</th>" % h for h in head) + "</tr>" + "".join("<tr>" + "".join("<td>%s</td>" % c for c in r) + "</tr>" for r in rows) + "</table>"
def BOX(cls, title, body): return '<div class="box %s"><h4>%s</h4>%s</div>' % (cls, title, body)
def LESSON(id_, title, about, outcomes, logic, lang, adapt, link=None):
    h = '<section id="%s"><h2>%s</h2>' % (id_, title)
    if link: h += '<p class="go"><a href="%s">→ Детальний Teacher’s Book уроку</a></p>' % link
    h += P(B("Про що урок:") + " " + about)
    h += BOX("out", "Outcomes — до кінця уроку студент може:", UL(outcomes))
    h += BOX("log", "Логіка уроку в книзі", OL(logic))
    h += lang
    h += BOX("ad", "Як адаптуємо — " + ("сир, «Звени Гора»" if ZV else "IT / PM / маркетинг, робота зі США"), UL(adapt))
    return h + "</section>"

AUD = "сирному бізнесі" if ZV else "IT"
# ---------- cheat sheet ----------
ex4 = "Приклад для сиру" if ZV else "Приклад для IT"
rows = [
 [B("Primary vs secondary research"), "Збираємо нові дані самі vs аналізуємо те, що вже є", "Своє опитування vs звіт з інтернету (desk research)",
  "Власна дегустація в магазині vs звіт про ринок сиру, дані мережі" if ZV else "Інтерв’ю з користувачами vs звіт Gartner, відгуки конкурентів, гілки на Reddit"],
 [B("Quantitative vs qualitative"), "Цифри (скільки?) vs думки й причини (чому?)", "Розмір ринку vs думки у фокус-групі",
  "Продажі за SKU, оцінки дегустації vs інтерв’ю з шефами про смак і плавлення" if ZV else "Аналітика, A/B-тест, NPS vs інтерв’ю, юзабіліті-тест"],
 [B("Survey vs focus group"), "Багато людей, короткі відповіді vs 6–10 людей, довга розмова з модератором", "Анкета після перельоту vs дегустація",
  "QR-опитування на упаковці vs група, що порівнює три витримані сири" if ZV else "Опитування в застосунку vs дзвінок із 6 користувачами"],
]
cheat = '<section id="u0"><h2>Шпаргалка: як говорити про маркетингові дослідження</h2>'
cheat += P("Головна думка юніту: " + B("будь-яке бізнес-рішення має спиратися на дані про людей, а не на думку керівника.") +
           " Market research відповідає на питання «що людям насправді потрібно і чому». " +
           ("У сирному бізнесі це дегустації та сенсорні панелі, дані продажів мереж, перевірки в магазинах, скарги, розмови з категорійними менеджерами й шефами, цінові тести." if ZV
            else "В IT це те саме, тільки називається user research, product discovery, analytics."))
cheat += P(B("Уся тема тримається на трьох парах понять:")) + TAB(["Пара", "Що означає", "Приклад із книги", ex4], rows)
cheat += P(B("Інші ключові слова:") + " sample / sample size (вибірка: що більша, то надійніше), respondent (хто відповідає на опитування), target audience (цільова аудиторія), launch a product (запустити продукт), viable (життєздатний і прибутковий), data analysis, brand image (образ бренду в головах людей), reputation у соцмережах." +
           (" Для сиру: blind tasting, sensory panel, grader, maturation, rind, SKU, private label, PDO, shelf space, price point." if ZV else ""))
cheat += P(B("Як запустити розмову, якщо тема здається нудною.") + " Усі студенти заповнювали анкети після готелю чи перельоту, усі хоч раз лишали відгук. Починайте з них: " + I("Do you ever fill in these surveys? Do you think anyone reads them?") + " " +
           ("А працівники «Звени Гори» самі роблять research щодня, просто не називають його так: стоять на дегустаціях, читають скарги, домовляються з мережами про полицю, дивляться продажі за SKU." if ZV
            else "А айтівці й PM самі роблять research щодня, просто не називають його так: дивляться метрики, читають тікети від саппорту, сперечаються про фічу за даними."))
qs = (["How does your company find out what shoppers and chefs want?", "Have you ever launched a cheese or a pack that didn’t sell? Why did it happen?",
       "Data or gut feeling: what decides things in your team?", "Can AI replace a tasting with real shoppers?"] if ZV else
      ["How does your company find out what users want?", "Have you ever built a feature nobody used? Why did it happen?",
       "Data or gut feeling: what decides things in your team?", "Can AI replace talking to real users?"])
cheat += BOX("q", "Питання, які працюють у будь-якому уроці юніту", UL([I(q) for q in qs])) + "</section>"

S = [cheat]

# ---------- 1.1 ----------
S.append(LESSON("u11", "1.1 Market research methods",
 "які бувають способи дізнатися, що потрібно клієнтам, і навіщо бізнесу це робити перед запуском продукту. Це вступний урок: студент збирає лексику всього юніту.",
 ["зрозуміти головне й деталі у відео чи статті про методи досліджень;", "пояснити різницю між primary/secondary і quantitative/qualitative research;",
  "скласти невелике опитування (questionnaire) і провести його;", "презентувати продукт і пояснити, як дослідження вплинуло на рішення."],
 [B("Lead-in:") + " навіщо компаніям опитування, чи брали ви участь самі, що компанія отримує з відповідей.",
  B("Передбачення:") + " як компанія може дослідити ринок перед запуском продукту (ідеї на дошку).",
  B("Відео 1.1.1 «Types of market research»:") + " звірити ідеї, потім True/False. У відео: primary і secondary research, surveys, focus groups, in-depth interviews, desk research, можна зменшити sample size заради бюджету.",
  B("Обговорення:") + " плюси primary і secondary research.",
  B("Лексика:") + " колокації (типи adj+noun, verb+noun, noun+noun), зіставлення слів із визначеннями, пропуски.",
  B("Розмова:") + " яка інформація потрібна компанії перед запуском.",
  B("Project «How market research affects brands» (найдовша частина):") + " а) обрати продукт і два відомі бренди, описати їхній профіль (цільова аудиторія, ціна, visibility); б) придумати свій новий продукт і написати опитування; в) провести опитування з іншою групою; г) за відповідями доробити бренд, презентувати респондентам і отримати відгук: чи врахували їхні побажання."],
 P(B("Лексика:") + " online surveys, focus group, in-depth interviews, desk research, primary / secondary research, quantitative / qualitative research, customer satisfaction, target audience, sample size, launch a product, product tester, data analysis, gauge the impact, carry out research, gather data."),
 ([ "Відео книги замінено на «Why Parmesan Cheese Is So Expensive» (Food Insider): три фрагменти — ціна й виробництво, маркування походження й витримка, підробки та PDO.",
    "Кейс-файл із реальними дослідженнями покупців сиру: Oregon State (наліпка про нагороду vs опис смаку), опитування 1 821 людини (формати фасування), ринок сиру України 2024.",
    "До лексики книги додаємо: blind tasting, sensory panel, grader, maturation, rind, SKU, private label, PDO, counterfeit, retail audit.",
    "Project: замість двох брендів соку — два сирні бренди («Звени Гора» vs «Пирятин», Parmigiano vs Grana Padano, твердий сир vs «сирний продукт»). Персонажі для інтерв’ю: категорійна менеджерка, мама двох дітей, шеф італійських ресторанів."] if ZV else
  [ "Відео книги замінено на Y Combinator: Video A «Best founders learn from their users» або Video B на вибір студента, по три фрагменти з фразами й питаннями.",
    "До лексики книги додаємо: A/B test, user interview, insight, synthesis, metrics, churn.",
    "Розмова замість «перед запуском продукту»: " + I("How does your team decide what to build next? Who talks to users in your company?"),
    "Project: замість двох брендів соку — два застосунки однієї категорії (Notion vs Obsidian, Duolingo vs Babbel). Студент придумує свою фічу, пише 5–7 питань для опитування, ви відповідаєте як користувач, він презентує висновок. Для індивідуального уроку це зручніше, ніж робота двох груп."]),
 link="1-1.html"))

# ---------- 1.2 ----------
S.append(LESSON("u12", "1.2 Working with a focus group",
 "як проходить фокус-група. Студент слухає її на прикладі застосунку для замовлення обідів і вчить question tags: як уточнювати факти й підтримувати розмову.",
 ["стежити за дискусією кількох людей і розуміти позицію кожного;", "правильно будувати позитивні й негативні question tags, включно зі складними випадками (" + I("nobody… did they?") + ", " + I("Let’s… shall we?") + ");",
  "інтонацією показати, чи він справді питає (↗), чи лише уточнює (↘);", "ставити закриті питання, щоб перевірити факти;", "підтримати ввічливу розмову й вибудувати контакт (rapport)."],
 [B("Lead-in:") + " визначення focus group. Чи хотіли б ви взяти участь? Хто там працює: moderator, participants, criteria.",
  B("Listening 1.01:") + " модератор відкриває зустріч: навіщо зібралися, правила, можна сперечатися одне з одним, іде запис.",
  B("Listening 1.02:") + " учасники розповідають, як обідають на роботі (зручність, калорії, час на обід), і дивляться застосунок: меню, калорії, ресторани, доставка.",
  B("Listening 1.03:") + " модератор просить оцінити застосунок від 1 до 10 (rating questions). Пропуски зі словами: impression, appealing, features, expectations, honestly, convinced.",
  B("Обговорення:") + " чи користувалися б ви таким застосунком?",
  B("Граматика:") + " question tags з аудіо, студент сам виводить правила. Потім вимова (↗ питання / ↘ уточнення) і дві вправи.",
  B("Speaking «Catching up with an old friend»:") + " написати фрази з tags (" + I("We met at school, didn’t we?") + ") і розіграти зустріч зі старим знайомим."],
 P(B("Лексика:") + " diverse, participants, criteria, target customers, moderator, impression, appealing, features, expectations, honestly, convinced, rating questions.") +
 P(B("Граматика:") + " question tags. Правило: be / допоміжне / модальне дієслово + підмет; позитивне твердження → негативний tag і навпаки. Пастки: Present Simple → do/does; hardly/never → позитивний tag; that → it; someone/nobody → they; Let’s → shall we."),
 ([ "Аудіо можна лишити, але після нього — своя фокус-група: дегустація трьох твердих сирів (наш, конкурент, імпорт). Ви — модератор, студент — учасник, потім навпаки.",
    "Нестандартний хід: зв’язати граматику й методологію. Question tags — по суті навідні питання (" + I("You’d buy this cheese, wouldn’t you?") + "), а на дегустації чи в інтерв’ю такі питання псують дані. Принцип The Mom Test: питаємо про минулий досвід, а не «вам подобається наш сир?».",
    "Висновок для студента: tags із ↘ корисні, щоб звірити факти з мережею чи головним офісом (" + I("The delivery is on Monday, isn’t it?") + "), а з покупцем на дегустації їх краще уникати.",
    "Speaking: замість «старого друга» — смолтоку з колегою із Savencia на початку дзвінка чи на виставці (" + I("You were at the Paris meeting last month, weren’t you?") + ")."] if ZV else
  [ "Фокус-група про застосунок уже близька до IT, аудіо можна лишити. В IT частіше роблять не фокус-групи, а user interviews один на один у Zoom.",
    "Нестандартний хід: зв’язати граматику й методологію. Question tags — по суті навідні питання (" + I("You’d use this app, wouldn’t you?") + "), а в інтерв’ю з користувачем такі питання псують дані. Принцип The Mom Test: питаємо про минулий досвід, а не «вам подобається наша ідея?».",
    "Висновок для студента: tags із ↘ корисні, щоб звірити факти на дзвінку (" + I("The release is on Friday, isn’t it?") + "), а в інтерв’ю з користувачем їх краще уникати.",
    "Speaking: замість «старого друга» — смолтоку з колишнім колегою на початку дзвінка (" + I("You moved to the US team, didn’t you?") + ")."])))

# ---------- 1.3 ----------
S.append(LESSON("u13", "1.3 Communication skills: Carrying out a needs analysis",
 "як з’ясувати, що потрібно клієнту, і водночас тримати розмову під контролем. Головне тут — різниця між " + B("open") + " і " + B("leading questions") + ". Відео книги лишається, сам урок не змінюємо.",
 ["відрізнити open question від leading і пояснити, коли який доречний;", "порівняти плюси й мінуси двох підходів;", "ставити уточнювальні питання, щоб зрозуміти деталі запиту;",
  "провести зустріч із клієнтом і погодити деталі;", "дати відгук про те, як пройшла зустріч."],
 [B("Lead-in:") + " два питання, студент визначає, яке з них open, а яке leading. Обговорення: чи це маніпуляція?",
  B("Відео 1.3.1:") + " підготовка до зустрічі й чому їм важливий контроль.",
  B("Вибір Option A або B,") + " відео 1.3.2 і 1.3.3, обговорення обох.",
  B("Відео 1.3.4:") + " висновки, рефлексія про свій стиль питань.",
  B("Функціональна мова:") + " фрази для open і leading questions, переробити один тип на інший.",
  B("Task:") + " зустріч івент-агенції та клієнта (дводенна конференція), відгук, потім помінятися ролями й провести другу зустріч."],
 BOX("plot", "Сюжет відео", P("Івент-агенція Happenings поки працює без прибутку. Prisha (Creative Director) і David (Accounts Director) ідуть на зустріч із Meghan, HR-менеджеркою нового клієнта Overlander. Їм вигідно провести захід у Hebden Hall: у них там спеціальний договір. Завдання: щоб клієнтка відчувала, що обирає сама, але розмову вели вони.") +
   UL([B("Option A (open questions):") + " клієнтці дають свободу, вона хоче готель вищого класу. Очікування ростуть швидше за бюджет, розмова їм уже непідконтрольна.",
       B("Option B (leading questions):") + " вони ведуть розмову і скеровують клієнтку (" + I("How would you feel about us bringing in our own caterers?") + "). Прибуток збережено, але клієнтка може відчути, що її не чують і «продавлюють».",
       B("Висновок відео:") + " найкраще поєднувати обидва типи питань."])) +
 P(B("Функціональна мова:")) + UL(["Open: " + I("What are your thoughts on…? Have you considered…? What do you think about…?"), "Leading: " + I("How would you feel about…? Would you be interested in…? How about…?"),
   "Та сама фраза стає навідною, коли в ній уже є ваша пропозиція: " + I("What do you think about a trip to Barcelona?")]) +
 P(B("Вимова:") + " Indian English, лише на слух, повторювати акцент не потрібно."),
 ([ "Відео не змінюємо. У Task студент обирає реальну ситуацію: зустріч key account менеджера з категорійним менеджером мережі (новий SKU, промо, полиця) або з шефом ресторану (постачання сиру для HoReCa).",
    "Мета та сама, що й у відео: з’ясувати потреби клієнта і не дати розмові піти в бік «знижка 30% і найкраща полиця». Leading questions тут — інструмент: " + I("How would you feel about a tasting week instead of a price promo?")] if ZV else
  [ "Відео не змінюємо. У Task студент сам обирає тип заходу: корпоративний офсайт IT-команди або kick-off нового проєкту з клієнтом.",
    "Для PM це по суті discovery call: з’ясовуємо вимоги і не даємо клієнту розширювати scope."])))

# ---------- 1.4 ----------
qtab = TAB(["Тип питання", "Приклад відповіді"], [
 ["Не зрозумів питання", "Could you clarify what you mean by…?"], ["Не на тему", "I’m afraid that’s outside the scope of today’s presentation."],
 ["Не для загального обговорення", "If you email me that question, I’ll respond directly."], ["Краще відповість колега", "Let me put you in touch with a colleague who knows more about it."],
 ["Злe питання", "I understand your frustration. As a solution, I suggest…"], ["Уже відповідали", "I touched upon that at the beginning when I talked about…"],
 ["Занадто довго питає", "Sorry to interrupt, but could I ask what your main question is?"], ["Не знаю відповіді", "To be perfectly honest, I don’t know. I’ll find out and get back to you."],
 ["Не розчув", "Sorry, the connection is bad. Could you repeat that?"], ["Делікатне питання", "That’s a delicate topic. Maybe we could discuss it one-to-one."]])
S.append(LESSON("u14", "1.4 Business skills: Dealing with questions",
 "як відповідати на питання під час і після презентації та не втратити контроль: питання не на тему, зле питання, питання без відповіді, поганий зв’язок. Зв’язок із юнітом: презентують результати опитування.",
 ["зрозуміти презентацію і позицію доповідача;", "оцінити, наскільки вдало доповідач відповів на питання;", "ввічливо відповісти на 10 типів складних питань;",
  "поставити уточнювальне чи критичне питання іншому доповідачу;", "презентувати зміну й відповісти на питання аудиторії."],
 [B("Lead-in:") + " коли краще відповідати на питання — під час чи в кінці? Що відповісти в шести ситуаціях (не знаю, не на тему, уже говорили, скажу пізніше).",
  B("Listening 1.05:") + " Джон презентує опитування про пластикове пакування їжі: 85% покупців хочуть менше пластику, супермаркети обіцяють мінус 50%, фермерам байдуже. Три питання із зали: кого опитували (ввічливо перебив), чи реалістичні 12 місяців («хороше питання, повернемося пізніше»), поганий зв’язок («передзвоніть»). Студент оцінює, наскільки хороші відповіді.",
  B("Listening 1.06:") + " ще 5 питань і стратегії: уточнити, hedging на делікатній темі, чесно визнати «не знаю», послатися на сказане раніше.",
  B("Функціональна мова:") + " таблиця з 10 типів питань і фрази до них.",
  B("Тренування:") + " дизайн-агенція робить сайт для нового клієнта, клієнт ставить 6 складних питань, студент відповідає.",
  B("Task:") + " міні-презентація про зміну (що змінюємо, навіщо, яка користь), аудиторія ставить питання, потім відгук про те, як студент упорався."],
 P(B("Функціональна мова (10 типів питань):")) + qtab,
 ([ "Тема пакування з аудіо близька до сиру — аудіо лишаємо. Task: презентація для французького головного офісу Savencia або для байєра мережі (нова упаковка, новий SKU, зміна ціни).",
    "Типові питання: " + I("Why are sales down in Q3? Can you lower the price? What did shoppers say in the tasting? Why should we give you more shelf space?"),
    "Біль: «завмираю, коли питають на дзвінку з Парижем». Додаємо фрази, щоб виграти час: " + I("Good question — let me make sure I understand. / Let me check the figures and get back to you by Friday."),
    "Ви граєте незручного стейкхолдера: скептичного менеджера з головного офісу або жорсткого категорійного менеджера."] if ZV else
  [ "Замість презентації про пластик: " + B("sprint review або демо для американських стейкхолдерів") + ". Типові питання: " + I("Why is this late? Will it scale? Can we add X by Friday? What did users say?"),
    "Біль: «завмираю, коли питають на дзвінку». Додаємо фрази, щоб виграти час: " + I("Good question — let me make sure I understand. / Let me check and get back to you by EOD."),
    "Ситуація з поганим зв’язком з аудіо актуальна як є.",
    "Task: студент презентує реальну зміну у своєму проєкті (нова фіча, перехід на інший інструмент), ви граєте незручного стейкхолдера."])))

# ---------- 1.5 ----------
S.append(LESSON("u15", "1.5 Writing: Reports — Summary findings",
 "як коротко викласти результати опитування чи фокус-групи: хто що сказав, скільки людей і який висновок. Це підсумок юніту: дослідження провели, тепер пишемо висновки.",
 ["знайти ключові дані у звіті;", "написати summary на ~120 слів, а потім детальнішу, розбиту на абзаци;", "точно передати цифри (the majority, just over a quarter, none of…);",
  "правильно вживати reporting verbs (suggest, insist, admit, raise concerns);", "помітити й виправити помилки в чужому тексті."],
 [B("Lead-in:") + " виправити помилки (орфографія, граматика, зайві й неправильні слова) у summary опитування про зміну логотипа й упаковки люксового бренду.",
  B("Функціональна мова:") + " структура речення " + B("Who/What → Opinion/Action → Finding") + " (" + I("Over half of those surveyed felt that…") + "), скласти свої речення.",
  B("Граматика (за бажанням):") + " reporting verb patterns.",
  B("Task 3A:") + " у парі написати коротке summary опитування про підвищення цін (~120 слів).",
  B("Task 3B:") + " самостійно написати детальне summary опитування задоволеності клієнтів (якість, ціна, асортимент, сервіс), можна вдома.",
  B("Peer check:") + " перевірити текст партнера: чи правильні цифри й фрази."],
 P(B("Мова:") + " according to the survey, the majority of respondents, were in agreement that, raised concerns that, just over one quarter, none of the participants, over half of those surveyed, the findings indicate / demonstrate / confirm that, should be minimal.") +
 P(B("Reporting verbs:") + " suggest that we (should) do / suggest doing; insist that; admit that / admit doing; demand that; believe / feel / indicate that."),
 ([ "Основний формат: " + B("короткий звіт для команди й головного офісу") + " (email або Teams): TL;DR в один рядок, 3–4 пункти з цифрами, next steps. Та сама структура речень, ті самі reporting verbs.",
    "Дані: замість логотипа й цін беремо результати дегустації нового твердого сиру або опитування покупців про новий формат (тертий, нарізка).",
    "Крок з ІІ: чернетку пише ІІ, студент її перевіряє. Це нова версія Lead-in: шукати треба не одруківки, а перебільшення («покупці хочуть X» за 4 інтерв’ю) і забутий розмір вибірки.",
    "Тема підвищення цін із Task 3A для сиру актуальна як є — лишаємо."] if ZV else
  [ "Основний формат: " + B("пост у Slack або сторінка в Notion") + " з підсумками дослідження для команди: TL;DR в один рядок, 3–4 пункти з цифрами, next steps. Та сама структура речень, ті самі reporting verbs.",
    "Дані: замість логотипа й цін беремо опитування користувачів застосунку про нову фічу чи онбординг.",
    "Крок з ІІ: чернетку пише ІІ, студент її перевіряє. Це нова версія Lead-in: шукати треба не одруківки, а перебільшення («користувачі хочуть X» за 4 інтерв’ю) і забутий розмір вибірки.",
    "Класичний звіт із книги (Task 3B) іде в Extra."])))

# ---------- Workshop ----------
S.append(LESSON("uw", "Business workshop 1: Improving the image",
 "кейс, де збирається весь юніт. У мережі одягу Wear It! чудова репутація: добре ставляться до працівників, етичні постачальники. Вони випускають невдалу рекламу, у соцмережах закликають до бойкоту, продажі падають. Найсильніше відпали мілленіали. Студенти планують дослідження, щоб зрозуміти, як повернути довіру.",
 ["описати графік продажів і зробити висновки (rise, decrease, fluctuation, shoot up);", "зрозуміти обговорення на кризовій зустрічі й текст про методи дослідження;",
  "обрати метод і скласти 10 питань різних типів (open, closed, multiple-choice, ranking, rating);", "переконливо презентувати свій план і дібрати тон;", "написати коротке обґрунтування свого підходу."],
 [B("Background:") + " прочитати про компанію: репутація, CSR, що пішло не так. Слова: source ethically, trigger, boycott.",
  B("Customer reaction:") + " коментарі в соцмережах. Що робити? Два графіки продажів за віковими групами: що помітили, що здивувало?",
  B("Listening BW 1.01:") + " кризова зустріч у CEO. Jane дивиться продажі (найсильніше впали мілленіали), Peter — маркетинг, Giorgio — витрати. Barbara збере дані для нової кампанії.",
  B("Reading:") + " нотатка Barbara про види досліджень (primary/secondary, опитування і типи питань, фокус-групи 6–10 людей, спостереження за реакцією). Підкреслити найцікавіше і найскладніше.",
  B("Task:") + " обрати метод (опитування чи фокус-група) → 10 питань від загальних до чутливих → презентація плану → голосування за найкращий.",
  B("Writing:") + " коротко пояснити обраний підхід. У зразку відповіді телефонне опитування (застаріло)."],
 P(B("Лексика:") + " reputation, corporate social responsibility (CSR), well thought of, source ethically, boycott, trigger, demographics, опис графіків (rise, decrease, fluctuation, shoot up, reach, a quarter, slightly), типи питань (open, closed, multiple-choice, ranking, rating)."),
 ([ "Структура лишається, змінюємо кейс (вигаданий, для навчання): " + B("сирний бренд змінив рецептуру й упаковку, щоб утримати ціну") + ". У відгуках і соцмережах пишуть «смак уже не той», «це вже сирний продукт», продажі серед молодих покупців падають.",
    "Замість коментарів про рекламу: відгуки на сайтах мереж, пости в Instagram і TikTok, скарги на гарячу лінію. Замість графіка продажів: продажі за SKU і частка ринку по місяцях (та сама лексика для графіків).",
    "Кризова зустріч: маркетинг, продажі (key account), R&D / якість, виробництво; на дзвінку — менеджер із головного офісу Savencia.",
    "Task: план дослідження з кількох методів (сліпа дегустація старої й нової рецептури + опитування покупців + аналіз відгуків за допомогою ІІ). Writing: короткий апдейт керівництву та головному офісу замість телефонного опитування."] if ZV else
  [ "Структура лишається, змінюємо кейс: " + B("оновлення застосунку обвалило рейтинг") + '. Реальний приклад 2026 року: MyFitnessPal замінив основний екран Diary, і рейтинг упав із 3.24 до 1.54 (<a href="https://mwm.ai/articles/myfitnesspal-v26-16-0-replaces-diary-with-new-ui-sparking-rating-drop-in-april-2026">джерело</a>).',
    "Замість коментарів про рекламу: відгуки в App Store і гілка на Reddit. Замість графіка продажів: рейтинг, DAU і churn по тижнях (та сама лексика для графіків).",
    "Кризова зустріч проходить у Zoom: PM, дизайнер, аналітик, саппорт.",
    "Task: план дослідження з кількох методів (in-app survey + 5 інтерв’ю + аналіз відгуків за допомогою ІІ). Writing: апдейт керівництву в Slack замість телефонного опитування."])))

SW = '<span class="sw">' + "".join('<b>%s</b>' % n if k == V else '<a href="https://villevian.github.io/%s/teacher/unit-1.html">%s</a>' % (r, n) for k, r, n in [("it", "bp-b2plus", "IT / PM / marketing"), ("zv", "bp-zvenyhora", "Zvenyhora · cheese")]) + "</span>"
nav = [("u0", "Шпаргалка"), ("u11", "1.1"), ("u12", "1.2"), ("u13", "1.3"), ("u14", "1.4"), ("u15", "1.5"), ("uw", "Workshop")]
TITLE = "Market research: hard cheese" if ZV else "Market research"
html = """<!DOCTYPE html><html lang="uk"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Unit 1 · %s — Teacher’s Book</title><link href="https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&display=swap" rel="stylesheet">
<style>*{box-sizing:border-box}body{margin:0;font-family:"Fira Sans",system-ui,sans-serif;font-weight:300;color:#231f20;background:#fff;line-height:1.5}
header{display:flex;border-bottom:3px solid #2f9a74;position:sticky;top:0;background:#fff;z-index:2}header .n{background:linear-gradient(120deg,#1f7d5c,#4fb58c);color:#fff;font-weight:500;font-size:26px;padding:12px 20px}
header h1{margin:0;align-self:center;padding-left:16px;font-weight:500;font-size:22px;color:#4d4d4f}header .t{margin-left:auto;align-self:center;margin-right:16px;background:#f2b631;color:#3b2c00;font-weight:600;font-size:12px;padding:5px 10px;border-radius:4px}
nav{display:flex;flex-wrap:wrap;gap:6px;padding:12px 22px;max-width:1000px;margin:0 auto}nav a{border:1.5px solid #2f9a74;color:#1f7d5c;border-radius:20px;padding:4px 14px;text-decoration:none;font-weight:500;font-size:14px}nav a:hover{background:#dcf0e6}
.top{max-width:1000px;margin:0 auto;padding:10px 22px 0}.top{display:flex;flex-wrap:wrap;gap:10px;align-items:center}.top a{color:#2f9a74;font-weight:500;text-decoration:none}.sw{margin-left:auto;display:flex;border:1.5px solid #2f9a74;border-radius:20px;overflow:hidden}.sw a,.sw b{padding:4px 14px;font-size:14px}.sw b{background:#2f9a74;color:#fff}
main{max-width:1000px;margin:0 auto;padding:0 22px 40px}section{scroll-margin-top:70px}h2{font-weight:600;font-size:17px;text-transform:uppercase;background:#4d4d4f;color:#fff;padding:7px 14px;margin:28px 0 10px}
b{font-weight:500}.box{border-left:4px solid #2f9a74;background:#f4faf7;padding:6px 14px;margin:12px 0}.box h4{margin:6px 0;font-weight:600;color:#1f7d5c;font-size:15px}
.box.log{border-color:#4d4d4f;background:#f6f6f6}.box.log h4{color:#4d4d4f}.box.ad{border-color:#f2b631;background:#fff8e6}.box.ad h4{color:#8a6100}.box.q,.box.plot{border-color:#c2185b;background:#fcf1f5}.box.q h4,.box.plot h4{color:#c2185b}
table{border-collapse:collapse;width:100%%;margin:8px 0;font-size:14px}th,td{border:1px solid #d5d6d7;padding:6px 9px;text-align:left;vertical-align:top}th{background:#dcf0e6;font-weight:500}
li{margin:3px 0}.go a{color:#c2185b;font-weight:500}footer{max-width:1000px;margin:0 auto;padding:0 22px 30px;font-size:12px;color:#77787b}</style></head><body>
<header><div class="n">Unit 1</div><h1>%s · гід для викладача</h1><div class="t">TEACHER</div></header>
<div class="top"><a href="index.html">← Teacher’s Book</a>%s</div><nav>%s</nav><main>%s</main>
<footer>Valentyna Hordiienko · Middle Learning Architect</footer></body></html>""" % (TITLE, TITLE, SW, "".join('<a href="#%s">%s</a>' % n for n in nav), "".join(S))
open(OUT, "w").write(html); print("ok", len(html))
