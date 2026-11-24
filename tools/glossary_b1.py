"""Business Partner B1 — updated glossary (2026), by unit and lesson.
Entry: (en, pos, uk, meaning, example, [collocations], word family, new)   new=True → word from the updated (IT/2026) lessons, not in the coursebook.
Unit 1 written in full; Unit 4 converted from vocab_b1 (lessons 4.2–4.5 already taught to Kate) — collocations / families to be added.
"""
U1_1 = [
 # --- Transferable skills (coursebook) ---
 ("transferable skills", "n. pl.", "навички, що переносяться", "skills you can use in many different jobs and roles", "Critical thinking is one of the most valuable transferable skills.", ["develop / demonstrate transferable skills", "a range of transferable skills"], "transfer (v) → transferable (adj)", False),
 ("think outside the box", "v. phr.", "мислити нестандартно", "have new, creative ideas", "She thought outside the box and replaced the 40-page spec with a demo video.", ["the ability to think outside the box"], "", False),
 ("can-do attitude", "n.", "позитивний настрій «я зможу»", "being positive and ready to try difficult things", "He took the old project with a real can-do attitude.", ["have / show a can-do attitude"], "attitude (n) — ставлення", False),
 ("set goals", "v. phr.", "ставити цілі", "decide what you want to achieve", "I set realistic goals for every sprint.", ["set realistic / ambitious goals", "achieve / reach a goal"], "", False),
 ("critical thinking", "n. [U]", "критичне мислення", "checking information carefully before you accept it", "Use critical thinking when AI suggests a solution.", ["use / apply critical thinking", "critical thinking skills"], "critic (n) → critical (adj) → criticise (v)", False),
 ("determination", "n. [U]", "рішучість, наполегливість", "not giving up when something is difficult", "It took real determination to pass the interview on the third try.", ["show / have a lot of determination"], "determine (v) → determined (adj) → determination (n)", False),
 ("team player", "n.", "командний гравець", "someone who works well with others", "Nobody ships a product alone – be a team player.", ["a real / good team player"], "", False),
 ("integrity", "n. [U]", "чесність, порядність", "being honest and doing what is right", "If you broke the build, say so – that’s integrity.", ["have / show integrity", "a person of integrity"], "", False),
 ("communication skills", "n. pl.", "комунікативні навички", "the ability to explain things clearly and listen well", "Communication skills are tested every day in a distributed team.", ["good / strong communication skills", "improve your communication skills"], "communicate (v) → communication (n) → communicator (n)", False),
 ("problem-solving", "n. [U]", "вирішення проблем", "finding solutions to difficult situations", "AI suggests ten solutions; problem-solving is choosing the right one.", ["problem-solving skills", "be good at problem-solving"], "solve (v) → solution (n)", False),
 # --- Adjective ↔ noun (coursebook ex. 7) ---
 ("adaptable", "adj.", "здатний пристосовуватися", "able to change when the situation changes", "You need to be adaptable – our priorities change every sprint.", ["highly adaptable"], "adapt (v) → adaptable (adj) → adaptability (n)", False),
 ("flexible", "adj.", "гнучкий", "able to change plans or ways of working easily", "We need someone flexible about working hours.", ["flexible hours / working"], "flexible (adj) → flexibility (n) · ≠ inflexible", False),
 ("motivated", "adj.", "вмотивований", "wanting to do something well", "We’re looking for a motivated backend engineer.", ["highly motivated", "self-motivated"], "motivate (v) → motivated (adj) → motivation (n) · ≠ unmotivated", False),
 ("confident", "adj.", "впевнений", "sure about your abilities", "He feels more confident in meetings now.", ["feel / sound confident"], "confident (adj) → confidence (n)", False),
 ("dependable", "adj.", "надійний", "someone you can trust to do what they promise", "Our team lead is very dependable.", ["a dependable colleague"], "depend (v) → dependable (adj) → dependability (n) · ≈ reliable", False),
 ("resourceful", "adj.", "винахідливий", "good at finding ways to solve problems", "She’s resourceful: she always finds a workaround.", [], "resource (n) → resourceful (adj) → resourcefulness (n)", False),
 ("independent", "adj.", "самостійний", "able to work without help", "We need an independent engineer who can work without a manager.", ["work independently"], "depend (v) → independent (adj) → independence (n)", False),
 ("ambitious", "adj.", "амбітний", "wanting to be very successful", "Her goals for the quarter are ambitious but realistic.", ["ambitious goals / plans"], "ambition (n) → ambitious (adj)", False),
 ("passionate", "adj.", "захоплений, пристрасний", "loving what you do", "She’s passionate about clean code.", ["passionate about sth"], "passion (n) → passionate (adj)", False),
 ("enthusiastic", "adj.", "сповнений ентузіазму", "showing a lot of interest and energy", "The new junior is very enthusiastic.", ["enthusiastic about sth"], "enthusiasm (n) → enthusiastic (adj)", False),
 ("honest", "adj.", "чесний", "telling the truth", "Be honest in your profile – don’t list tools you don’t know.", ["to be honest"], "honest (adj) → honesty (n) · ≠ dishonest", False),
 ("authentic", "adj.", "справжній, автентичний", "real, not pretending", "Recruiters value authentic stories, not buzzwords.", [], "authentic (adj) → authenticity (n) ≈ genuine", False),
 # --- From the article (NEW) ---
 ("be applied to a range of tasks", "v. phr.", "застосовуватися до різних задач", "be useful in many different situations", "Transferable skills can be applied to a range of tasks and roles.", ["apply sth to sth"], "apply (v) → application (n)", True),
 ("old news", "n. phr.", "застаріле, вже не новина", "not new or interesting any more", "A framework you master today may be old news by next year.", [], "", True),
 ("tech stack", "n.", "технологічний стек", "the tools and technologies a team uses", "Our tech stack changes almost every year.", ["a modern / legacy tech stack"], "", True),
 ("double-check", "v.", "перепровірити", "check something again to be sure it is correct", "A good engineer double-checks the output of AI tools.", ["double-check the output / the numbers"], "", True),
 ("justify a choice", "v. phr.", "обґрунтувати вибір", "explain why your decision is right", "Someone has to choose the right solution and justify that choice.", ["justify a decision"], "justify (v) → justification (n)", True),
 ("distributed team", "n.", "розподілена команда", "a team whose members work in different places", "Most products are built by distributed teams.", ["work in a distributed team"], "", True),
 ("time zone", "n.", "часовий пояс", "an area of the world with the same time", "Our team is spread across several time zones.", ["in different time zones", "time-zone difference"], "", True),
 ("demo", "v. / n.", "показати (демо) / демонстрація", "show what you have built to other people", "Every Friday we demo our work to the whole company.", ["demo your work", "a product demo", "give a demo"], "", True),
 ("break the build", "v. phr.", "«зламати» збірку", "push code that makes the project fail to build or test", "If you broke the build, admit it.", [], "", True),
 ("admit", "v.", "визнати", "say that something bad is true, often about yourself", "She admitted that AI wrote half of her code.", ["admit a mistake", "admit (that)…"], "admit (v) → admission (n)", True),
 ("hard to automate", "adj. phr.", "важко автоматизувати", "difficult for machines or AI to do instead of people", "Honesty and integrity are hard to automate.", [], "automate (v) → automation (n)", True),
 ("ship a product", "v. phr.", "випустити продукт", "release a product to users", "Nobody ships a successful product alone.", ["ship a feature / a release"], "", True),
 ("stay employable", "v. phr.", "залишатися затребуваним", "keep the skills that employers want", "Collect transferable skills if you want to stay employable.", [], "employ (v) → employer / employee (n) → employable (adj)", True),
 ("AI literacy", "n. [U]", "грамотність у роботі з ШІ", "knowing how to use AI tools well and check their results", "AI literacy is now in half of all tech job ads.", ["develop AI literacy"], "", True),
 ("async communication", "n. [U]", "асинхронна комунікація", "communicating in writing so people can answer later", "Good async communication means fewer meetings.", [], "asynchronous (adj) → asynchronously (adv)", True),
 ("ownership", "n. [U]", "відповідальність за результат", "taking a task from start to finish and caring about the result", "We want people who take ownership.", ["take ownership of sth"], "own (v) → owner (n) → ownership (n)", True),
 ("job description", "n.", "опис вакансії", "a text that explains a job and the skills it needs", "Write a job description for a remote role.", ["write / read a job description"], "", False),
 # --- Coursebook video 1.1.1 (Before class) ---
 ("fit into the team", "v. phr.", "вписатися в команду", "work well and feel comfortable with the other people in a team", "Employers ask: can this candidate fit into the team well?", ["fit in well"], "", False),
 ("influence people", "v. phr.", "впливати на людей", "change what other people think or do", "The ability to influence people is an important skill.", ["have an influence on sb"], "influence (v / n) → influential (adj)", False),
 ("internship", "n.", "стажування", "a short period of work to get experience, often for students", "She did a three-month internship at a software company.", ["do an internship", "a paid / unpaid internship"], "intern (n) → internship (n)", False),
 ("part-time job", "n.", "робота на неповний день", "a job for only some hours of the day or week", "A part-time job shows that you can manage your time.", ["have / get a part-time job"], "≠ full-time job", False),
 ("volunteer work", "n. [U]", "волонтерська робота", "work you do without pay to help people", "Volunteer work can show your communication skills.", ["do volunteer work"], "volunteer (n / v) → voluntary (adj)", False),
 ("the whole person behind the CV", "n. phr.", "людина повністю, а не лише резюме", "who you really are – skills, qualities and experience together", "Employers hire the whole person behind the CV.", [], "", False),
 # --- From the IT video (★ Advanced, NEW) ---
 ("stakeholder", "n.", "стейкхолдер, зацікавлена сторона", "a person or group affected by a project who cares about the result", "Talk to every stakeholder before you change the plan.", ["key stakeholders", "stakeholder management"], "", True),
 ("roll out", "phr. v.", "впровадити, розгорнути", "introduce a new system to all the people who will use it", "We rolled out the new CRM to all departments.", ["roll out a system / a feature"], "roll out (v) → rollout (n)", True),
 ("project management", "n. [U]", "управління проєктами", "planning and organising work so a project finishes on time", "IT work is almost always organised as projects.", ["project management tools"], "manage (v) → management (n) → manager (n)", True),
 ("internal team", "n.", "внутрішня команда", "a team inside your own company", "IT solves problems for customers and for internal teams.", [], "", True),
 ("plain business language", "n. phr.", "проста ділова мова", "simple words that non-technical people understand", "Explain the bug in plain business language.", ["in plain English"], "", True),
 ("gap", "n.", "прогалина", "something you don’t know or haven’t done yet", "Don’t worry too much about the gaps in your knowledge.", ["a gap in your knowledge / CV", "fill a gap"], "", True),
 ("cover letter", "n.", "супровідний лист", "a short letter you send together with your CV", "Connect your skills to real examples in your cover letter.", ["write a cover letter"], "", False),
 ("collaboration", "n. [U]", "співпраця", "working together with other people or teams", "IT projects need collaboration across departments.", ["close collaboration", "in collaboration with"], "collaborate (v) → collaboration (n) → collaborator (n)", False),
]
U1_1X = [  # Extra: portfolio career
 ("portfolio career", "n.", "портфельна кар’єра", "working for several clients or projects instead of one employer", "More and more engineers build a portfolio career.", ["have / build a portfolio career"], "", True),
 ("contractor", "n.", "контрактор, підрядник", "a person who works under a contract, not as an employee", "He works with all three clients as a contractor.", ["an independent contractor", "work as a contractor"], "contract (n) → contractor (n)", True),
 ("client", "n.", "клієнт", "a company or person who pays you for your work", "He has three clients in three countries.", ["a new / regular client"], "", False),
 ("rate", "n.", "ставка", "the money you charge per hour or per day", "He reviews his rate once a year.", ["an hourly / daily rate", "raise your rate"], "", True),
 ("invoice", "n. / v.", "інвойс, рахунок / виставити рахунок", "a document that asks a client to pay for your work", "I’ll send you the invoice on Friday.", ["send / pay an invoice"], "", True),
 ("scope", "n. [U]", "обсяг робіт", "exactly what work is included in a task or project", "Let’s agree the scope before I start.", ["agree / change the scope", "out of scope"], "", True),
 ("onboarding", "n. [U]", "онбординг, адаптація", "the first days when you learn how a new team or project works", "Onboarding fast is the most important skill.", ["onboarding process", "onboard a new client"], "onboard (v) → onboarding (n)", True),
 ("manage expectations", "v. phr.", "керувати очікуваннями", "make sure people know what you can and can’t do, and when", "Tell the client early – manage expectations.", [], "expect (v) → expectation (n)", True),
 ("availability", "n. [U]", "доступність, вільний час", "the times when you are free to work or talk", "My availability this week: Monday to Wednesday.", ["check sb’s availability"], "available (adj) → availability (n)", True),
 ("side project", "n.", "власний (сайд-)проєкт", "something you build in your free time, not for a client", "He adds every side project to his portfolio.", ["work on a side project"], "", True),
]

def _unit4():
    from vocab_b1 import VOCAB
    out = []
    for n, t, groups in VOCAB:
        if not n.startswith("4."): continue
        out.append((n, t, [(e[0], "", e[1], e[2], e[3], [], "", False) for _, ws in groups for e in ws]))
    return out

UNITS = [
 ("1", "Career choices", [
  ("1.1", "Transferable skills", U1_1),
  ("1.1 Extra", "Portfolio career", U1_1X),
 ]),
 ("4", "Global markets", _unit4()),
]
