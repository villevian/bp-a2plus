LEVEL = "B2+"
ACC, ACC2 = "#2f9a74", "#dcf0e6"          # mint
GRAD = ("#1f7d5c", "#4fb58c")             # level badge gradient (mint)
VARIANTS = {}
# (number, title, focus, tag kept|updated|new|both, status ready|soon[, classic focus])
U = [
 ("1", "Market research", [
  ("1.1", "Market research methods", "Vocabulary: market research · Surveys, analytics, A/B tests, AI tools · Project: how research affects brands", "updated", "soon"),
  ("1.2", "User interviews and focus groups", "Question tags · A focus group about a new app · Catching up with an old contact", "updated", "soon"),
  ("1.3", "Carrying out a needs analysis", "Leading and open questions · Agreeing details of a corporate event", "kept", "soon"),
  ("1.4", "Dealing with questions", "Responding to questions during a presentation · Proposing a change", "kept", "soon"),
  ("1.5", "Writing: Summary findings", "Survey findings in Notion / Slack with charts · Reporting verb patterns", "both", "soon", "Summary findings from a report · Reporting verb patterns"),
  ("W1", "Business workshop: Improving the image", "A social media crisis meeting · Plan research to improve the brand image", "updated", "soon")]),
 ("2", "Give and take", [
  ("2.1", "Manager or mentor?", "Vocabulary: giving back · Mentoring and 1:1s · Project: an ideal mentor", "updated", "soon"),
  ("2.2", "Kindness or success?", "Cleft sentences · Is it cruel to be kind? Feedback culture at work", "updated", "soon"),
  ("2.3", "Changing an agreement", "Renegotiating details of a client agreement", "kept", "soon"),
  ("2.4", "Collaboration", "Brainstorming meetings · Promoting collaboration", "kept", "soon"),
  ("2.5", "Writing: Stating requirements", "Requirements in a Jira ticket or Slack brief · Future Perfect Simple & Continuous", "both", "soon", "Bulleted and non-bulleted email stating requirements · Future Perfect Simple & Continuous"),
  ("W2", "Business workshop: Try to see it my way", "Support team vs managers · Guidelines based on survey findings", "updated", "soon")]),
 ("3", "Money matters", [
  ("3.1", "Mobile banking and fintech", "Vocabulary: personal banking · Neobanks and payment apps · Project: banking preferences survey", "updated", "soon"),
  ("3.2", "Managing money", "Phrasal verbs · Saving, BNPL and paying back money", "updated", "soon"),
  ("3.3", "Presentation styles", "Fact-based and emotion-based presentations", "kept", "soon"),
  ("3.4", "Defending your ideas", "Presenting and defending a proposal for a banking app", "kept", "soon"),
  ("3.5", "Writing: A complaint", "Complaint in a support chat, app review or public post · Participle clauses", "both", "soon", "Formal letter of complaint · Participle clauses"),
  ("W3", "Business workshop: Managing your money", "Millennials fall behind on living standards · Financial products for millennials", "kept", "soon")]),
 ("4", "Challenges", [
  ("4.1", "Environmental challenges", "Collocations: the environment · Climate and business · Project: sustainable solutions", "kept", "soon"),
  ("4.2", "Cyber challenges", "Perfect aspect · Cyberattacks, IoT and AI-powered scams · A short blog post", "updated", "soon"),
  ("4.3", "Saying ‘no’ firmly and politely", "Managing challenging negotiations · Allocating tasks with a colleague", "kept", "soon"),
  ("4.4", "Challenging conversations", "A difficult conversation about promotion · Reaching a positive outcome", "kept", "soon"),
  ("4.5", "Writing: Recommendations", "Recommendations in a Notion / Confluence proposal · Compound nouns and adjectives", "both", "soon", "Recommendations section of a proposal · Compound nouns and adjectives"),
  ("W4", "Business workshop: Business challenges", "Pitch a YouTube / podcast series about business challenges · Present with slides", "updated", "soon")]),
 ("5", "Global mobility", [
  ("5.1", "Relocation and remote work abroad", "Vocabulary: relocation · Secondments, digital nomads, work from anywhere · Project: relocating to a new country", "updated", "soon"),
  ("5.2", "Relocation and retention", "Inversion · Keeping talent: relocation packages and job-hopping", "updated", "soon"),
  ("5.3", "Giving feedback on performance", "Talking about performance · Conducting a performance review", "kept", "soon"),
  ("5.4", "Presentations", "Developing a convincing argument · Arguing for or against", "kept", "soon"),
  ("5.5", "Writing: A post about relocation", "LinkedIn / Medium post about relocation · Past Perfect Continuous", "both", "soon", "Blog post about a secondment · Past Perfect Continuous"),
  ("W5", "Business workshop: Ready for relocation?", "Pros and cons of relocation · Negotiate a secondment or remote contract", "updated", "soon")]),
 ("6", "Alliances", [
  ("6.1", "Strategic alliances", "Vocabulary: alliances and acquisitions · Project: choosing a partner", "kept", "soon"),
  ("6.2", "Business partnerships", "Past modals · When things didn’t go to plan", "kept", "soon"),
  ("6.3", "Diffusing conflict", "Managing conflict between an organiser and a sponsor", "kept", "soon"),
  ("6.4", "Learning from mistakes", "Lessons learnt in an IT project · A useful mistake", "kept", "soon"),
  ("6.5", "Writing: A report extract", "Retrospective / post-mortem in Confluence or Notion · Ways of expressing the future", "both", "soon", "Formal report extract · Ways of expressing the future"),
  ("W6", "Business workshop: Growing the business", "SWOT analysis · Choose an option and summarise your reasons", "kept", "soon")]),
 ("7", "Risk", [
  ("7.1", "A resilient building", "Vocabulary: managing and minimising risk · Project: emergency protocol", "kept", "soon"),
  ("7.2", "Risk in investment", "Second, third and mixed conditionals · Crypto, index funds and risky bets", "updated", "soon"),
  ("7.3", "Dealing with risk", "Talking about risk · Managing risks for an upcoming event", "kept", "soon"),
  ("7.4", "Analysing risk", "Project risks on a probability-impact matrix", "kept", "soon"),
  ("7.5", "Writing: An incident report", "Incident report in Jira / Slack · Alternatives to if", "both", "soon", "Accident report · Alternatives to if"),
  ("W7", "Business workshop: What could possibly go wrong?", "Three start-ups · A risk-management plan, including AI risks", "updated", "soon")]),
 ("8", "Decisions", [
  ("8.1", "The Idle Man", "Vocabulary: decisions · Project: the head or heart debate", "kept", "soon"),
  ("8.2", "Decisions with data and AI", "to + infinitive or -ing · AI-assisted decisions and decision fatigue", "new", "soon"),
  ("8.3", "Influencing a decision", "Fact-based and emotion-based approaches · Choosing suppliers", "kept", "soon"),
  ("8.4", "Maintaining relationships", "Relationship-oriented decision-making in difficult conversations", "kept", "soon"),
  ("8.5", "Writing: Describing a decision", "Decision log in Notion / announcement in Slack · Avoiding repetition", "both", "soon", "Formal letter describing a decision · Ways to avoid repeating words"),
  ("W8", "Business workshop: Decisions, decisions", "Growth of a restaurant chain · Propose a strategy to expand", "kept", "soon")]),
]
