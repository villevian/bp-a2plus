LEVEL = "A2"
ACC, ACC2 = "#3b7dd8", "#e3eefb"          # blue
GRAD = ("#2a5fb0", "#4f9be8")
COLS = 5                                   # A2 book: 5 lessons per unit, x.5 = business workshop
VARIANTS = {"1.1": ["all"], "1.2": ["all"], "7.2": ["all"], "7.3": ["all"], "7.4": ["all"]}
PAGES = {"1.1": ["lesson", "hw"], "1.2": ["lesson", "hw"], "7.2": ["lesson", "hw", "extra", "games"], "7.3": ["lesson", "hw", "extra", "games"], "7.4": ["present"]}   # extra not built yet
# (number, title, focus, tag kept|updated|new|both, status ready|soon[, classic focus])
U = [
 ("1", "Working day", [
  ("1.1", "Daily tasks", "Vocabulary: jobs and tasks · Present Simple: facts and routines · Introducing yourself on a video call", "updated", "ready"),
  ("1.2", "A work plan", "Vocabulary: work tasks and meetings · Review of 1.1 · Scheduling a meeting in Slack / Google Calendar", "both", "ready", "Email to schedule a meeting"),
  ("1.3", "A survey", "Questions · An employee survey (Google Forms) about the office and remote work", "updated", "soon"),
  ("1.4", "Work skills: Talking about people and roles", "Video: What do you do? · Talking about people and roles in a team", "kept", "soon"),
  ("1.5", "Business workshop: We want to meet you…", "A company webpage · Arranging to meet on a video call · Talking about your job", "updated", "soon")]),
 ("2", "Doing business", [
  ("2.1", "Orders and deliveries", "Vocabulary: orders and deliveries · Things you can and can’t count · Online orders and delivery tracking", "updated", "soon"),
  ("2.2", "Placing an order", "can / can’t · Placing an order on a video call or in a chat (instead of the phone)", "updated", "soon"),
  ("2.3", "Enquiries", "there is / there are · FAQ page · Answering a customer enquiry in a chat", "both", "soon", "Response to an email enquiry"),
  ("2.4", "Work skills: Making agreements", "Video: Agreeing contract details · Making agreements", "kept", "soon"),
  ("2.5", "Business workshop: Planning a team event", "Catering offers · Comparing information · Replying to an order in a chat", "updated", "soon")]),
 ("3", "Changes", [
  ("3.1", "A company’s story", "Past Simple (1) · A startup story · Completing a timeline", "updated", "soon"),
  ("3.2", "New office or remote?", "Giving instructions · Rules for a hybrid office · Slack message with instructions", "both", "soon", "Email giving instructions"),
  ("3.3", "Company performance", "Past Simple (2) · Successes and challenges · Short update in Slack", "both", "soon", "Email describing successes and challenges"),
  ("3.4", "Work skills: How did it go?", "Video: How did the project go? · Talking about projects", "kept", "soon"),
  ("3.5", "Business workshop: Our first year", "A timeline of a new company · Preparing for a move · Discussing a project", "kept", "soon")]),
 ("4", "Travelling for work", [
  ("4.1", "I’m flying to Tokyo tomorrow", "Present Continuous for arrangements · Booking with travel apps", "updated", "soon"),
  ("4.2", "The 12.05 is delayed", "will / won’t · Dealing with delays: airport and train apps · Message about a change", "updated", "soon"),
  ("4.3", "An update", "Present Continuous: things happening now · Project update in Slack or a Jira comment", "both", "soon", "An update email"),
  ("4.4", "Work skills: Setting up a video call", "Video: Technical problems · Making suggestions · Problems on video calls", "kept", "soon"),
  ("4.5", "Business workshop: A business trip", "A change in plans · Arranging a meeting · Messages giving updates", "kept", "soon")]),
 ("5", "Organising", [
  ("5.1", "Trade shows and online events", "Vocabulary: organising an event · Talking about intentions (going to)", "updated", "soon"),
  ("5.2", "Organising a conference", "Voice notes and calls about a conference (instead of phone messages)", "updated", "soon"),
  ("5.3", "Invitations", "Invitations with would and want · Calendar invites and Slack invitations", "both", "soon", "Informal messages of invitation"),
  ("5.4", "Work skills: Socialising with clients", "Video: What do you think of the trade fair? · Socialising with clients", "kept", "soon"),
  ("5.5", "Business workshop: The conference", "Comparing conference details on a call · Small talk at a conference dinner · A message about a conference", "updated", "soon")]),
 ("6", "Products", [
  ("6.1", "Future products: AI everywhere", "Speculating about the future · AI in everyday products and at work", "new", "soon"),
  ("6.2", "A problem with an order", "Helping with a problem · Customer support chat and video call", "updated", "soon"),
  ("6.3", "The production process", "Describing production · Ethical and sustainable products · Product description for a website", "kept", "soon"),
  ("6.4", "Work skills: Placing an order", "Video: How many do you want to order? · Placing an order", "kept", "soon"),
  ("6.5", "Business workshop: Buy natural", "Ethical products · Placing an order · A complaint in a support chat", "updated", "soon")]),
 ("7", "Competition", [
  ("7.1", "Should I upgrade?", "Comparatives · Upgrading a phone, laptop or software plan", "updated", "soon"),
  ("7.2", "Services and subscriptions", "Vocabulary: fees and hidden fees · Reading: Adobe, Microsoft, Amazon · Listening: recruitment agencies · An honest pricing page", "both", "ready", "Advertisement for a courier agency"),
  ("7.3", "The best providers", "Superlatives · Mobile operators for company eSIMs · A recommendation in Slack", "both", "ready", "Email comparing services (Travel Care)"),
  ("7.4", "Work skills: Presentations", "Video: Our products and services · Presenting online: share your screen · Presentation kit", "updated", "ready"),
  ("7.5", "Business workshop: The big contract", "A trade show · Giving a presentation · A recommendation message", "updated", "soon")]),
 ("8", "Jobs", [
  ("8.1", "Work experience", "Talking about experience (Present Perfect) · Skills and personal qualities", "kept", "soon"),
  ("8.2", "The best person for the job", "Job requirements · Choosing candidates · Job ads on LinkedIn", "updated", "soon"),
  ("8.3", "Professional profiles", "Present Perfect vs Past Simple · A LinkedIn profile", "both", "soon", "An employee profile"),
  ("8.4", "Work skills: A job interview", "Video: The job interview · Job interviews online", "kept", "soon"),
  ("8.5", "Business workshop: The interviewer and the candidate", "Online interview questions · AI in hiring · Choosing the best candidate", "new", "soon")]),
]
