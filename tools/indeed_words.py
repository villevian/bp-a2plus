"""Vocabulary from Indeed · Job Search Stories — "How to Change Careers Using Transferable Skills You Already Have" (YouTube FRFb_JMB5g0, June 2026).
Approved by Vale 24.11.2026. Tier: core = active use · rec = recognise when listening · adv = ★ Advanced (B1+/B2, section 7:05–9:56).
Entry: (en, pos, uk, meaning, example_IT, [collocations], family, tier)
Examples are IT contexts written for the course (not quotes from the video)."""
WORDS = [
 # ---- core (1:04–4:34) ----
 ("audit your experience", "v. phr.", "проаналізувати свій досвід", "look carefully at everything you have done to find useful skills", "Before the interview, audit your experience: projects, side jobs, even volunteering.", ["a skills audit", "audit your CV"], "audit (v / n) → auditor (n)", "core"),
 ("with fresh eyes", "phr.", "свіжим поглядом", "in a new way, as if you see it for the first time", "Look at your old pull request with fresh eyes – you’ll find three things to improve.", ["look at sth with fresh eyes"], "", "core"),
 ("AI-proof skills", "n. phr.", "навички, які не замінить ШІ", "skills that AI cannot easily do instead of people", "Communication and judgment are AI-proof skills.", ["AI-proof jobs / careers"], "-proof = waterproof, future-proof", "core"),
 ("bridge the gap", "v. phr.", "подолати розрив, «перекинути місток»", "connect two things that are far apart, or close a difference", "A short course can bridge the gap between QA and automation testing.", ["bridge the gap between A and B"], "bridge (n / v)", "core"),
 ("industry-specific terms", "n. phr.", "галузеві терміни", "words that people use in one particular field", "Translate your teaching experience into industry-specific terms: ‘onboarding’, not ‘first lesson’.", ["use / translate into industry-specific terms"], "specific (adj) → specify (v)", "core"),
 ("connect the dots", "v. phr.", "поєднати факти, показати зв’язок", "show how different facts or experiences are related", "In the interview, connect the dots between your support job and your new QA role.", ["help sb connect the dots"], "", "core"),
 ("skill gap", "n.", "прогалина в навичках", "the difference between the skills you have and the skills a job needs", "My skill gap is cloud infrastructure – I’m working on it.", ["close / fill a skill gap", "identify a skill gap"], "", "core"),
 ("think in verbs, not titles", "phr.", "мислити діями, а не посадами", "describe what you did (actions), not just your job name", "Think in verbs, not titles: ‘built’, ‘led’, ‘reduced’ – not just ‘Senior Developer’.", ["action verbs"], "", "core"),
 ("comfort with new tools", "n. phr.", "легкість в освоєнні нових інструментів", "being relaxed and quick when you learn new software", "Comfort with new tools is a must in a team that changes its stack every year.", ["show comfort with sth"], "comfortable (adj) → comfortably (adv)", "core"),
 ("side hustle", "n.", "підробіток, власний проєкт на стороні", "extra work or a project you do outside your main job", "My side hustle – a small Telegram bot – taught me product thinking.", ["start / run a side hustle"], "hustle (v / n) → hustler (n)", "core"),
 ("every experience counts", "phr.", "кожен досвід має значення", "all experience can be useful and worth mentioning", "Volunteering, freelancing, a student club – every experience counts.", ["sth counts (= is important)"], "count (v)", "core"),
 ("signal initiative", "v. phr.", "показати ініціативність", "show that you start things yourself without being told", "A free certificate can signal initiative to a recruiter.", ["take the initiative", "on your own initiative"], "initiate (v) → initiative (n)", "core"),
 ("a day in the life", "n. phr.", "один день із життя (формат відео)", "a typical working day of a person in a job", "Watch ‘a day in the life’ videos before you choose a new role.", ["a day-in-the-life video"], "", "core"),
 # ---- recognise (rec) ----
 ("go back to square one", "v. phr.", "почати все з нуля", "start again from the very beginning", "Changing careers doesn’t mean you go back to square one.", [], "", "rec"),
 ("industry-recognised credentials", "n. phr.", "визнані в галузі сертифікати", "certificates that employers in a field know and trust", "AWS certificates are industry-recognised credentials.", [], "credential (n)", "rec"),
 ("carry real weight", "v. phr.", "мати справжню вагу", "be respected and influential", "A strong GitHub profile can carry real weight with recruiters.", ["carry weight with sb"], "", "rec"),
 ("low cost to no cost", "phr.", "недорого або безкоштовно", "very cheap or free", "Many courses are low cost to no cost.", [], "", "rec"),
 ("more common than you think", "phr.", "частіше, ніж ви думаєте", "it happens more often than people believe", "Career changes into IT are more common than you think.", [], "", "rec"),
 ("tough job market", "n. phr.", "складний ринок праці", "a time when it is hard to find a job", "In a tough job market, referrals matter more.", ["a competitive job market"], "", "rec"),
 ("never too late", "phr.", "ніколи не пізно", "you can still start, whatever your age", "It’s never too late to learn to code.", [], "", "rec"),
 ("go after it", "phr. v.", "братися за це, йти до мети", "try hard to get something you want", "If you want that role, go after it.", ["go after a job / a goal"], "", "rec"),
 # ---- ★ advanced (7:05–9:56) ----
 ("through line", "n.", "наскрізна лінія", "one idea or theme that connects all parts of a story or career", "The through line of my career is making complex systems simple.", ["a common thread"], "", "adv"),
 ("narrate it with intention", "v. phr.", "розповідати свідомо, з метою", "tell your story in a planned way that leads the listener to your point", "Don’t just list jobs – narrate it with intention.", [], "narrate (v) → narrative (n)", "adv"),
 ("reframe longevity as loyalty", "v. phr.", "подати довгий стаж як лояльність", "present many years in one place as a strength, not a weakness", "Six years at one company? Reframe longevity as loyalty and depth.", ["reframe sth as sth"], "long (adj) → longevity (n)", "adv"),
 ("industry disruptions", "n. pl.", "потрясіння (злами) в галузі", "big changes that completely change how a field works", "I’ve led teams through two industry disruptions: cloud and AI.", ["disrupt (v)"], "disrupt (v) → disruption (n) → disruptive (adj)", "adv"),
 ("lead by example", "v. phr.", "показувати приклад", "influence others by doing things well yourself", "A good tech lead leads by example in code reviews.", [], "", "adv"),
 ("own it and articulate it", "phr.", "визнати це своїм і чітко сформулювати", "accept your story and explain it clearly and confidently", "Your career path isn’t a straight line – own it and articulate it.", ["articulate an idea"], "articulate (v / adj) → articulation (n)", "adv"),
 ("turn the conversation around", "v. phr.", "розвернути розмову (у свій бік)", "change a difficult conversation into a positive one", "When they asked about my gap year, I turned the conversation around to what I learned.", [], "", "adv"),
]
CORE = [w for w in WORDS if w[7] == "core"]
REC = [w for w in WORDS if w[7] == "rec"]
ADVW = [w for w in WORDS if w[7] == "adv"]
VIDEO_ID = "FRFb_JMB5g0"
VIDEO_TITLE = "How to Change Careers Using Transferable Skills You Already Have"
CHAPTERS = [(0, "Age as an asset"), (64, "Audit your transferable skills"), (170, "Gen Z & first-time job seekers"), (274, "Certificates without a degree"), (425, "A long career = loyalty and depth"), (596, "Never too late")]
