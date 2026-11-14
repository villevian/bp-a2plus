LEVEL = "B2+"
ACC, ACC2 = "#2f9a74", "#dcf0e6"          # mint
GRAD = ("#1f7d5c", "#4fb58c")             # level badge gradient (mint)
VARIANTS = {"1.1": ["all"]}
PAGES = {"1.1": ["lesson"]}   # hw / extra not built yet
# (number, title, focus, tag kept|updated|new|both, status ready|soon[, classic focus])
U = [
 ("1", "User & market research", [
  ("1.1", "Research in tech", "Vocabulary: market research · Interviews, analytics, A/B tests, AI for analysing feedback · Project: how research changed a product", "updated", "ready"),
  ("1.2", "Talking to users", "Question tags · User interviews: why ‘Do you like it?’ is a bad question", "updated", "soon"),
  ("1.3", "Carrying out a needs analysis", "Leading and open questions · Agreeing details of a corporate event", "kept", "soon"),
  ("1.4", "Tough questions at a demo", "Handling stakeholder questions at a sprint review · ‘I’ll get back to you’", "updated", "soon"),
  ("1.5", "Writing: Research findings", "Slack / Notion post with research findings, AI draft + your edit · Reporting verb patterns", "both", "soon", "Summary findings from a report · Reporting verb patterns"),
  ("W1", "Business workshop: Rating crash", "An update tanks App Store ratings · Plan research to win users back", "updated", "soon")]),
 ("2", "Give and take", [
  ("2.1", "Manager or mentor?", "Vocabulary: giving back · 1:1s and ‘my manager never gives feedback’ · Project: an ideal mentor", "updated", "soon"),
  ("2.2", "Kindness or success?", "Cleft sentences · American directness and radical candor", "updated", "soon"),
  ("2.3", "Changing an agreement", "Renegotiating details of a client agreement", "kept", "soon"),
  ("2.4", "Async collaboration", "Brainstorming in Miro and Slack threads · ‘This meeting could have been a message’", "updated", "soon"),
  ("2.5", "Writing: A Jira ticket", "User story + acceptance criteria · Future Perfect Simple & Continuous", "both", "soon", "Email stating requirements · Future Perfect Simple & Continuous"),
  ("W2", "Business workshop: On-call burnout", "Survey findings · Write a team agreement in Notion", "updated", "soon")]),
 ("3", "Money matters", [
  ("3.1", "Fintech", "Vocabulary: personal banking · Getting paid by a US client: Wise, Payoneer", "updated", "soon"),
  ("3.2", "Millennials and money", "Phrasal verbs · Subscriptions, lifestyle creep, unaffordable housing", "updated", "soon"),
  ("3.3", "Presentation styles", "Fact-based and emotion-based presentations", "kept", "soon"),
  ("3.4", "Defending a decision", "Defending a product or technical decision at planning", "updated", "soon"),
  ("3.5", "Writing: An escalation", "Escalation in Slack or a complaint ticket to a vendor · Participle clauses", "both", "soon", "Formal letter of complaint · Participle clauses"),
  ("W3", "Business workshop: Contracting for the US", "Rates, invoices and taxes · Choose the best set-up", "updated", "soon")]),
 ("4", "Challenges", [
  ("4.1", "The real cost of AI", "Collocations: the environment · Energy use of AI and data centres · Project: sustainable solutions", "new", "soon"),
  ("4.2", "Cyber challenges", "Perfect aspect · Deepfake ‘CEO calls’ and phishing in Slack", "updated", "soon"),
  ("4.3", "Saying ‘no’ firmly and politely", "Managing challenging negotiations · Allocating tasks with a colleague", "kept", "soon"),
  ("4.4", "Asking for more", "Asking for a raise or promotion · Pushing back on scope creep", "updated", "soon"),
  ("4.5", "Writing: An RFC", "Recommendations in an RFC / design doc in Notion · Compound nouns and adjectives", "both", "soon", "Recommendations section of a proposal · Compound nouns and adjectives"),
  ("W4", "Business workshop: Failure talks", "Pitch a podcast or internal talk series about postmortems · Present with slides", "updated", "soon")]),
 ("5", "Global mobility", [
  ("5.1", "Remote for the US", "Vocabulary: relocation · Working from Europe across time zones or relocating", "updated", "soon"),
  ("5.2", "Retention", "Inversion · Return to office, quiet quitting, job-hopping", "updated", "soon"),
  ("5.3", "Giving feedback on performance", "Talking about performance · Conducting a performance review", "kept", "soon"),
  ("5.4", "Making the case", "Convincing management: remote or office", "updated", "soon"),
  ("5.5", "Writing: A LinkedIn post", "A post about relocating or going remote · Past Perfect Continuous", "both", "soon", "Blog post about a secondment · Past Perfect Continuous"),
  ("W5", "Business workshop: A remote contract", "Negotiate overlap hours and equipment · Sum up in Slack", "updated", "soon")]),
 ("6", "Alliances", [
  ("6.1", "Tech partnerships", "Vocabulary: alliances and acquisitions · Integrations, start-up acquisitions, AI partnerships · Project: choosing a partner", "updated", "soon"),
  ("6.2", "Outsourcing gone wrong", "Past modals · A vendor relationship that failed", "updated", "soon"),
  ("6.3", "Diffusing conflict", "Managing conflict between an organiser and a sponsor", "kept", "soon"),
  ("6.4", "Blameless postmortems", "Learning from a real major outage", "updated", "soon"),
  ("6.5", "Writing: A postmortem", "Postmortem doc with action items · Ways of expressing the future", "both", "soon", "Formal report extract · Ways of expressing the future"),
  ("W6", "Business workshop: Growing a SaaS", "SWOT · AI feature, new market or partnership?", "updated", "soon")]),
 ("7", "Risk", [
  ("7.1", "When systems fail", "Vocabulary: managing and minimising risk · Outages and disaster recovery · Project: emergency protocol", "updated", "soon"),
  ("7.2", "Risky bets", "Second, third and mixed conditionals · VC money, crypto, ‘if only I had bought…’", "updated", "soon"),
  ("7.3", "Dealing with risk", "Talking about risk · Managing risks for an upcoming event", "kept", "soon"),
  ("7.4", "The pre-mortem", "Risk register and pre-mortem in Jira / Notion", "updated", "soon"),
  ("7.5", "Writing: An incident report", "Jira incident report + status page update · Alternatives to if", "both", "soon", "Accident report · Alternatives to if"),
  ("W7", "Business workshop: AI risks", "Three start-ups · A risk plan: hallucinations, data leaks", "new", "soon")]),
 ("8", "Decisions", [
  ("8.1", "Head or heart?", "Vocabulary: decisions · Quit a stable job for a start-up?", "updated", "soon"),
  ("8.2", "Better decisions", "to + infinitive or -ing · Decision fatigue, disagree and commit, deciding with AI", "updated", "soon"),
  ("8.3", "Influencing a decision", "Fact-based and emotion-based approaches · Choosing suppliers", "kept", "soon"),
  ("8.4", "Managing up", "Saying no to a stakeholder and keeping the relationship", "updated", "soon"),
  ("8.5", "Writing: A decision log", "Decision record in Notion + Slack announcement · Avoiding repetition", "both", "soon", "Formal letter describing a decision · Ways to avoid repeating words"),
  ("W8", "Business workshop: Going to the US market", "Should a SaaS expand to the US? · Propose a strategy", "updated", "soon")]),
]
