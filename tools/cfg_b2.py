LEVEL = "B2"
ACC, ACC2 = "#5b5fc7", "#e8e9fa"          # indigo
GRAD = ("#4044a8", "#7b7fe0")
VARIANTS = {"6.1": ["all"]}
PAGES = {"6.1": ["lesson"]}   # hw / extra not built yet
LEGEND = ("modern IT context: remote teams, Slack, Jira, Notion, Figma", "new topic: AI, new ways of working")
# (number, title, focus, tag kept|updated|new|both, status ready|soon[, classic focus])
U = [
 ("1", "Corporate culture", [
  ("1.1", "Workplace culture", "Video: A culture of equal pay · Vocabulary: corporate culture · Remote-first, async and flat teams · Project: a team working agreement", "updated", "soon"),
  ("1.2", "Employee retention", "Future Continuous & Future Perfect · Why people leave tech jobs: burnout, career paths, 4-day week · Where do you see yourself in five years?", "updated", "soon"),
  ("1.3", "Communication skills: Building relationships", "Video: Building relationships · Building trust · Choosing a candidate", "kept", "soon"),
  ("1.4", "Business skills: Presenting yourself", "Presenting yourself to a new project team · Intro at a kick-off call, on LinkedIn and in Slack", "updated", "soon"),
  ("1.5", "Writing: A company news update", "Team update in Slack / Notion · Phrases with be", "both", "soon", "A company news blog · Phrases with be"),
  ("W1", "Business workshop: Keeping the workforce happy", "Analysing a pulse / eNPS survey · Ideas to improve retention · A proposal in Notion", "updated", "soon")]),
 ("2", "Training and development", [
  ("2.1", "Learning on the job", "Video: Types of training · Onboarding, mentoring and learning with AI · Project: an onboarding plan for a new developer", "updated", "soon"),
  ("2.2", "Human resource strategies", "Modals in the passive · Upskilling teams for AI · Agreeing action points in Notion / Jira", "updated", "soon"),
  ("2.3", "Communication skills: Team communication", "Video: Team communication · Exchanging ideas · Organising a team-building event", "kept", "soon"),
  ("2.4", "Business skills: Facilitating a meeting", "Facilitating a discussion on Zoom and Miro · Retros and workshops · Coming to an agreement", "updated", "soon"),
  ("2.5", "Writing: A training request", "Slack request for a course or conference budget · Linking words for reason and purpose", "both", "soon", "Email requesting a course · Linking words for reason and purpose"),
  ("W2", "Business workshop: Quality service for all", "Regional teams’ training issues · Create and present an online course with AI tools", "updated", "soon")]),
 ("3", "Finance", [
  ("3.1", "Booms, bubbles and crashes", "Video: Past crashes and crises · Dot-com, tech layoffs and the AI bubble · Project: the ups and downs of a tech company", "updated", "soon"),
  ("3.2", "Catching up with rivals", "Certainty and probability · Position of adverbs · Startups vs Big Tech · Discussing future changes", "updated", "soon"),
  ("3.3", "Communication skills: Managing bad news", "Video: Managing bad news · Balancing positives with negatives", "kept", "soon"),
  ("3.4", "Business skills: Calling to clarify", "Clarifying on a video call · Asking for clarification and paraphrasing · Checking a budget or invoice", "updated", "soon"),
  ("3.5", "Writing: A quarterly update", "Investor / stakeholder update in Notion · Articles", "both", "soon", "Annual report summary for shareholders · Articles"),
  ("W3", "Business workshop: Investment opportunities", "VC pitch and startup metrics · Describing graphs · Choosing a startup to invest in", "updated", "soon")]),
 ("4", "Digital business", [
  ("4.1", "Digital disruptors", "Video: A disruptive marketing start-up · AI-native startups · Stress in word building · Project: disruptive technology", "updated", "soon"),
  ("4.2", "Talking technology", "Zero, first and second conditionals · A product demo at a tech conference · Release notes for an app", "updated", "soon"),
  ("4.3", "Communication skills: Handling difficult communicators", "Video: Handling difficult communicators · Keeping a meeting on track", "kept", "soon"),
  ("4.4", "Business skills: Negotiating strategies", "Positional and principled negotiation · Negotiating scope, deadlines and salary", "updated", "soon"),
  ("4.5", "Writing: A short proposal", "One-pager in Notion · Noun phrases instead of verb phrases", "both", "soon", "Short business proposal · Noun phrases"),
  ("W4", "Business workshop: Rise of the AI agents", "AI agents and robots at work · Analyse feedback statistics · Recommend future improvements", "new", "soon")]),
 ("5", "Performance", [
  ("5.1", "Performance and rewards", "Video: The cyber manager · OKRs, KPIs and performance reviews · Project: career ladders in tech", "updated", "soon"),
  ("5.2", "A culture of rewards", "Linking words and concessive clauses · Recognition, bonuses and equity · Concessions and compromises", "updated", "soon"),
  ("5.3", "Communication skills: Managing challenging feedback", "Video: Managing challenging feedback · Responding to feedback", "kept", "soon"),
  ("5.4", "Business skills: Reviewing projects", "Sprint retrospectives and post-mortems · Leading and taking part in review meetings", "updated", "soon"),
  ("5.5", "Writing: A performance review", "Self-review and peer feedback in a review tool · Phrasal verbs", "both", "soon", "Performance review summary · Phrasal verbs"),
  ("W5", "Business workshop: Changing expectations", "What Gen Z and millennials expect at work · Negotiating changes in benefits", "updated", "soon")]),
 ("6", "Ethics", [
  ("6.1", "Ethical choices", "Video: Inside Shein’s factories (FRANCE 24, 2026) · Ultra-fast fashion apps (Shein, Temu): dark patterns · Vocabulary: business ethics · Project: survey — how ethical are your clothes and apps?", "updated", "ready"),
  ("6.2", "The triple bottom line", "Third conditional · Sustainability and green tech · Discussing a company’s ethical performance", "kept", "soon"),
  ("6.3", "Communication skills: Transparency in business", "Video: Transparency in business · Voicing and responding to concerns", "kept", "soon"),
  ("6.4", "Business skills: Sales and selling", "Selling a SaaS product at a meetup or demo · Promoting a product or service", "updated", "soon"),
  ("6.5", "Writing: A company newsletter", "Internal newsletter / changelog · Linking words for causes and results", "both", "soon", "Company newsletter · Linking words for causes and results"),
  ("W6", "Business workshop: Keeping an ethical reputation", "An AI bias or data-leak case · An action plan to rebuild trust", "updated", "soon")]),
 ("7", "Time management", [
  ("7.1", "Managing time", "Video: Time management · Deep work, focus apps and AI assistants · Project: the working-from-home debate", "updated", "soon"),
  ("7.2", "Smart work", "Adverbials and time expressions · Cutting overtime: 4-day week and the right to disconnect", "updated", "soon"),
  ("7.3", "Communication skills: Dealing with urgency", "Video: Dealing with matters of urgency · Discussing priorities", "kept", "soon"),
  ("7.4", "Business skills: Difficult negotiations", "Dealing with difficulties: deadlines, scope creep, difficult stakeholders", "updated", "soon"),
  ("7.5", "Writing: Giving reasons", "Slack message explaining a delay · Prepositions of time", "both", "soon", "Email giving reasons · Prepositions of time"),
  ("W7", "Business workshop: Planning a product launch", "Planning a tech conference stand or online launch · A summary after the event", "updated", "soon")]),
 ("8", "Change", [
  ("8.1", "Change at Brompton Bikes", "Video: Brompton Bikes · Change management · Project: an adaptability quiz", "kept", "soon"),
  ("8.2", "Managing change", "Reported speech and reporting verbs · Reorganisations, AI transformation, new tools", "updated", "soon"),
  ("8.3", "Communication skills: Coaching and mentoring", "Video: Discussing future options · The GROW model", "kept", "soon"),
  ("8.4", "Business skills: Brainstorming", "Leading a brainstorm in Miro / FigJam · Brainstorming with AI", "updated", "soon"),
  ("8.5", "Writing: A launch announcement", "Product launch post (blog, LinkedIn) · Passive with reporting verbs", "both", "soon", "Press release · Passive with reporting verbs"),
  ("W8", "Business workshop: Stopping the rumours", "A rumour crisis on social media · Putting a stop to rumours", "updated", "soon")]),
]
