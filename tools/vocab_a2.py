"""Vocabulary data for Business Partner A2 (per lesson).
Each item: (en, uk, definition, example, collocations). Used by lesson pages (click a word -> card) and the vocab trainer.
"""
VOCAB = [
 ("1.2", "A work plan", [
  ("Meetings", [
   ("budget meeting", "нарада про бюджет", "a meeting about money: how much we can spend", "In the budget meeting we talk about money for the new app.", ["the budget for…", "a small budget"]),
   ("client meeting", "зустріч із клієнтом", "a meeting with a customer", "I have a client meeting on Tuesday morning.", ["meet clients", "a client demo"]),
   ("planning meeting", "нарада з планування", "a meeting to plan the work", "The sprint planning meeting is on Friday.", ["sprint planning", "plan the week"]),
   ("project meeting", "нарада по проєкту", "a meeting about a project", "We have a project meeting every Thursday.", ["a project update"]),
   ("management meeting", "нарада керівництва", "a meeting of managers", "My boss is at a management meeting all day.", ["managers", "the management team"]),
  ]),
  ("Work tasks", [
   ("book a meeting room", "забронювати переговорну", "reserve a room for a meeting", "Can you book a meeting room for Friday?", ["book a room", "book a call"]),
   ("send out the agenda", "розіслати порядок денний", "send the list of topics for a meeting to everyone", "I send out the agenda before the meeting.", ["the agenda for the meeting"]),
   ("create a brief", "створити бриф (опис завдання)", "write a short document: the task and what the client wants", "The designer needs a brief from the client.", ["write a brief", "a design brief"]),
   ("prepare a presentation", "підготувати презентацію", "make slides for a talk", "I prepare a presentation for the client demo.", ["make slides", "give a presentation"]),
   ("get an update", "отримати оновлення (новини)", "ask somebody for new information about their work", "Can I get an update from the QA team?", ["give an update", "a quick update"]),
   ("calculate costs", "розрахувати витрати", "find out how much something will cost", "We calculate costs for the new server.", ["costs", "the price"]),
  ]),
  ("Scheduling", [
   ("Are you available on…?", "Ти вільний / вільна у…?", "a question: do you have time then?", "Are you available on Friday morning?", ["I’m available after lunch."]),
   ("I’m busy then.", "Я тоді зайнятий / зайнята.", "I don’t have time at that time", "Sorry, I’m afraid I’m busy then.", ["I’m not available."]),
   ("How about…?", "Як щодо…?", "a way to suggest a time or a day", "How about Thursday at 2 p.m.?", ["What about…?"]),
   ("Shall we…?", "Давай…? / Може…?", "a polite way to suggest something", "Shall we meet in the meeting room?", ["Let’s…"]),
   ("That’s fine.", "Це підходить.", "yes, it’s OK for me", "Thursday at 2 p.m.? Yes, that’s fine.", ["Sounds good.", "Perfect!"]),
   ("See you then.", "Тоді до зустрічі.", "a way to finish when you agree a time", "OK, Friday at one. See you then.", ["See you on Friday."]),
  ]),
 ]),
 ("7.2", "Services and subscriptions", [
  ("Fees", [
   ("fee", "плата, збір", "money you pay for a service", "What is the fee for this course?", ["pay a fee", "charge a fee", "a small / high fee", "the fee includes …"]),
   ("charge a fee", "стягувати плату", "ask someone to pay money for a service", "The agency charges a fee of €40 an hour.", ["charge (someone) €10", "charge for delivery", "free of charge"]),
   ("pay a fee", "платити (збір, внесок)", "give money for a service", "You can pay the fee after the project.", ["pay monthly / yearly", "pay by card", "pay in advance"]),
   ("the fee includes …", "у вартість входить …", "you pay a fee and you get these things", "The fee includes all videos and a certificate.", ["include everything", "VAT included", "not included"]),
   ("fixed fee", "фіксована плата", "an amount of money that does not change", "Our studio charges a fixed fee of €1,500 for a landing page.", ["for a fixed fee", "a fixed price", "a fixed monthly fee"]),
   ("monthly fee", "щомісячна плата", "money you pay every month", "The AI tool has a monthly fee of €18.", ["pay a monthly fee", "a low monthly fee", "per user per month"]),
   ("annual fee", "річна плата", "money you pay once a year", "The annual fee went up from A$109 to A$159.", ["pay an annual fee", "an annual plan", "billed annually"]),
   ("additional fee", "додаткова плата", "some extra money you pay for something more", "There is an additional fee for extra storage.", ["for an additional fee", "extra cost", "at no additional cost"]),
   ("administration fee", "адміністративний збір", "money for paperwork or for managing your account", "My bank app charges a €3 administration fee every month.", ["an admin fee", "a one-time administration fee"]),
   ("booking fee", "збір за бронювання", "money you pay to the company that books something for you (tickets, hotels)", "The website charges a €12 booking fee for every ticket.", ["a booking fee per ticket", "no booking fee", "book online"]),
   ("cancellation fee", "плата за скасування", "money you pay when you cancel a plan or a booking", "My gym has a €50 cancellation fee.", ["no cancellation fee", "cancel for free", "cancel within 14 days"]),
  ]),
  ("Hidden fees", [
   ("hidden fee", "прихована плата", "a fee that the company does not show clearly", "I hate hidden fees — show me the real price!", ["hide a fee", "hidden costs", "no hidden fees"]),
   ("early termination fee", "плата за дострокове розірвання", "money you pay if you end a contract or plan before the end", "To cancel early, I had to pay an early termination fee.", ["end a contract early", "terminate a plan", "an ETF"]),
   ("the small print", "дрібний шрифт (умови)", "important information in small letters that people often don't read", "The fee was in the small print.", ["read the small print", "check the terms and conditions"]),
   ("sign up for", "підписатися на, зареєструватися", "start a plan, a subscription or a service", "I signed up for Prime by mistake.", ["sign up for a plan", "sign up for a free trial", "sign up online"]),
   ("cancel a subscription", "скасувати підписку", "stop a subscription so you don't pay any more", "I tried to cancel my subscription, but it was very difficult.", ["cancel online", "cancel any time", "cancel in two clicks"]),
   ("annual plan, paid monthly", "річний план із щомісячною оплатою", "you pay every month, but you promise to stay for a year", "It looked like a monthly plan, but it was an annual plan, paid monthly.", ["a monthly plan", "an annual plan", "billed monthly"]),
   ("price increase", "підвищення ціни", "when the price goes up", "After the price increase, the plan cost 45% more.", ["a big / small price increase", "the price goes up", "raise the price"]),
   ("get a refund", "отримати повернення коштів", "get your money back", "Some customers get a refund of up to $51.", ["ask for a refund", "a full refund", "give a refund"]),
   ("free trial", "безкоштовний пробний період", "you can use a product for free for a short time", "The app has a 7-day free trial.", ["start a free trial", "a 14-day free trial", "after the free trial"]),
  ]),
  ("Services", [
   ("cloud storage", "хмарне сховище", "space on the internet for your files", "My plan includes 1 TB of cloud storage.", ["store files in the cloud", "extra storage"]),
   ("design software", "програма для дизайну", "a program for making pictures, layouts and app screens", "Photoshop is design software.", ["use design software", "a design tool"]),
   ("AI assistant", "ШІ-асистент", "a program that answers questions and helps you with tasks", "Copilot is an AI assistant in Word and Excel.", ["use an AI assistant", "ask the AI assistant"]),
   ("recruitment agency", "кадрове агентство", "a company that finds new workers for other companies", "We use a recruitment agency to find developers.", ["work with an agency", "hire through an agency"]),
   ("background check", "перевірка кандидата", "a check of a person's job history and other information", "The agency does background checks on candidates.", ["do a background check", "run a check"]),
   ("guarantee", "гарантія", "a promise from a company that something will be OK", "They offer a six-month guarantee on candidates.", ["a money-back guarantee", "a three-month guarantee"]),
  ]),
 ]),
]

def lesson(num):
    for n, t, groups in VOCAB:
        if n == num:
            return t, groups
    raise KeyError(num)
