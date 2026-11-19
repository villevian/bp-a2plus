"""Shared content for Business Partner B2 · 1.2 Employee retention (updated 2026: AI layoffs and rehiring)."""

TITLE = "Fired by AI, hired back: why the cheapest employee is the one you keep"

# Article (≈430 words). Underlined = Future Continuous / Future Perfect forms for Exercise 5.
ARTICLE = [
 "In 2023, IBM’s chief executive said the company would pause hiring for back-office jobs and that AI could replace around 7,800 roles within five years. "
 "Three years later, IBM is doing the opposite: it is tripling its entry-level hiring in the US, including software developers. “Today’s entry-level employees are also "
 "tomorrow’s managers,” says its HR chief, Nickle LaMoreaux. If companies stop hiring juniors now, she warns, in a few years they <u>will be poaching</u> mid-level staff "
 "from rivals at a premium of around 30%.",
 "IBM is not alone. In 2024, the Swedish fintech Klarna boasted that its AI assistant was doing the work of 700 customer service agents. A year later, its CEO admitted that "
 "cost had been too important in the decision, that quality had suffered — and Klarna started hiring people again. Australia’s biggest bank, Commonwealth Bank, let 45 "
 "call-centre staff go after launching a voice bot. When calls went up by 2,000 a week and team leaders had to answer the phones, the bank reversed its decision and admitted an “error”.",
 "AI has become the number one reason that US companies give for layoffs: it was cited in more than 121,000 job cuts in 2026 by October, more than double the figure for the "
 "whole of 2025. But a survey by Orgvue found that 55% of leaders who made people redundant because of AI now say it was a mistake, and about a third of companies have already "
 "rehired staff. Gartner predicts that by 2027, half of the companies that cut customer service headcount because of AI <u>will have rehired</u> for similar roles. Critics call "
 "much of this ‘AI washing’: a cost-cutting exercise dressed up as innovation.",
 "Why do the cuts cost so much? According to Gallup, replacing an employee costs between half and twice their annual salary — for a software engineer earning $120,000, that "
 "can mean $150,000. And when experienced people leave, institutional knowledge leaves with them: who the most loyal clients are, and why the old code still works. Orgvue "
 "estimates that companies spend about $1.27 for every $1 they save through cuts.",
 "So what keeps people? Not free pizza. Young employees put learning first: for Gen Z, learning and development is one of the top three reasons for choosing an employer. They "
 "want diverse work instead of menial tasks — which AI really can take over — clear promotion paths, a healthy work-life balance and, at some firms, a paid sabbatical. "
 "Hopefully, by the end of the decade, managers <u>will have learnt</u> that AI should augment people, not replace them. The best way to keep good staff is to convince them "
 "that their employer <u>will still be investing</u> in them in five years’ time — and that they <u>will be working</u> alongside AI, not competing with it.",
]
SOURCES = "Based on: Fortune and Bloomberg (IBM, Feb 2026); Bloomberg (Klarna, May 2025); Bloomberg and Finextra (Commonwealth Bank, Aug 2025); Challenger, Gray &amp; Christmas (Nov 2026); Orgvue; Gartner; Gallup; Deloitte Gen Z Survey 2025."

# Exercise 1 (coursebook words and definitions, kept)
EX1 = [("menial tasks", "work which needs little skill"), ("sabbatical", "a fixed period of time when someone takes an agreed break from their job"),
       ("promotion", "the fact of getting a better-paid, more responsible job"),
       ("work-life balance", "a situation in which you are able to give the right amount of time and effort to your work and to your personal life outside work"),
       ("diverse work", "jobs that are very different from each other")]

# Exercise 4
TF = [("IBM still plans to replace 7,800 jobs with AI.", "F", "IBM is now tripling its entry-level hiring."),
      ("Klarna’s CEO admitted that cost was too important in the decision.", "T", ""),
      ("Commonwealth Bank’s voice bot reduced the number of calls.", "F", "Calls went up by 2,000 a week."),
      ("Most leaders who cut jobs because of AI are happy with their decision.", "F", "55% say it was a mistake."),
      ("Replacing a software engineer can cost more than his or her annual salary.", "T", ""),
      ("Employees need to believe that the company will invest in them in the future.", "T", "")]

UNDERLINED = [("will be poaching", "FC"), ("will have rehired", "FP"), ("will have learnt", "FP"), ("will still be investing", "FC"), ("will be working", "FC")]
TIME = [("will be poaching", "in a few years"), ("will have rehired", "by 2027"), ("will have learnt", "by the end of the decade"), ("will still be investing", "in five years’ time")]

# Exercise 6 (verbs from the book: change, do, improve, promote, rest, take)
EX6 = [("In April she", "will be taking", "a month-long paid sabbatical — she’s going to travel and do an AI course."),
       ("My company has just announced that by the summer it", "will have changed", "the support team to an ‘AI-first’ set-up. I’m worried about our clients."),
       ("I’m glad the release is over. By next Monday I", "will have rested", "and should have the energy for a very busy sprint."),
       ("By the middle of the next decade, tech companies", "will have improved", "the training of their junior staff a great deal and should see better retention."),
       ("There is a lot of discussion about what companies", "will be doing", "in the future to keep their developers motivated."),
       ("Our CTO said that by the end of the year they", "will have promoted", "a number of junior developers to middle positions.")]

# Exercise 7A
EX7 = [("What kind of job", "will you be looking for", "(you / look for) in the future? Do you think AI is going to change it?"),
       ("By the end of the year, what", "will you have finished", "(you / finish)?"),
       ("Is there anything that", "you won’t have finished|you will not have finished|won't you have finished", "(you / not finish)?"),
       ("What", "will you be doing", "(you / do) ten years from now?"),
       ("By the time you have worked for five (more) years, what position", "will you have reached", "(you / reach)? And in ten years?")]

# Homework: six comments (1–4 retold from real Reddit comments; 5–6 written in the same style)
REVIEWS = [
 ("The AI didn’t know our best customer", "A friend of mine was an assistant at a big firm. Her manager decided AI could do her job, so she was let go — not even a goodbye party. "
  "Guess who they had to call a few weeks later? Her. The AI didn’t know the phone number of the firm’s most loyal customer.", "reddit", "friend"),
 ("My knowledge is expensive now", "My friend was laid off for the same reason. When his old boss called and asked for help, he said: “Sure, but my knowledge is going to be "
  "expensive.” They took him back as a consultant — for $300 an hour.", "reddit", "friend"),
 ("My manager loved AI more than design", "I’m a graphic designer and I lost my job ‘indirectly’ because of AI. My manager wasn’t a designer and didn’t understand how "
  "anything worked, but she was amazed by what AI could do. Every single day she asked me why I hadn’t done my task with AI.", "reddit", "employee"),
 ("I trained my own replacement", "I worked as a game developer at a huge company. I had no idea they were using my own work to train the AI that would replace me. "
  "I was laid off three days before Christmas.", "reddit", "employee"),
 ("Nobody understands the old code", "As a team lead, I was told to cut two junior developers because “AI writes the code now”. Six months later, nobody on the team "
  "understands our legacy system, and we’re paying a contractor twice their salary to fix it. Great savings.", "style", "manager"),
 ("I just kept shouting “human”", "I spent forty minutes with my bank’s voice bot. It kept sending me back to the same menu. In the end I just kept shouting “Human! Agent!” "
  "until someone finally picked up. If a company replaces people with this, I’m moving my money.", "style", "customer"),
]
