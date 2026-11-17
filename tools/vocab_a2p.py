"""Vocabulary data for Business Partner A2+ (per lesson). Item: (en, uk, definition, example, collocations).
Used by lesson pages (click a word -> card) and the vocab trainer (build_vocab.py reads the first 4 fields)."""
VOCAB = [
 ("1.2", "Events management", [
  ("Events", [
   ("plan an event", "планувати захід", "decide what, when and where an event happens", "Alicia plans events for tech companies.", ["plan a conference", "plan a party", "event planning"]),
   ("attend a conference", "відвідувати конференцію", "go to a conference as a guest", "300 people attend the conference every year.", ["go to a conference", "speak at a conference", "a two-day conference"]),
   ("product launch", "запуск продукту", "an event to show a new product for the first time", "The product launch is on Thursday.", ["launch a new product", "a launch party"]),
   ("team offsite", "виїзна зустріч команди", "a meeting or event for a team outside the office", "Our team offsite is in a villa near Barcelona.", ["go on an offsite", "a two-day offsite"]),
   ("hybrid event", "гібридний захід", "an event with people in the room and people online", "It’s a hybrid event — we stream the talks.", ["stream the talks", "join online", "in person"]),
   ("stay for the weekend", "залишитися на вихідні", "not go home after work on Friday, stay until Sunday", "Half of the guests stay for the weekend.", ["extend a trip", "bleisure (business + leisure)", "take a day off"]),
  ]),
  ("People and places", [
   ("client", "клієнт", "a person or company that pays for a service", "Most of her clients are businesses.", ["a corporate client", "meet a client", "client satisfaction"]),
   ("guest", "гість", "a person who is invited to an event", "We had about three hundred guests.", ["invite guests", "a guest list", "welcome the guests"]),
   ("venue", "місце проведення", "the place where an event happens", "We choose the least expensive venue possible.", ["book a venue", "choose a venue", "an outdoor venue"]),
   ("staff", "персонал", "the people who work for a company or at an event", "The boat restaurant has 18 staff.", ["hire staff", "friendly staff", "staff costs"]),
   ("entertainment", "розважальна програма", "music, shows or activities for guests", "The entertainment is a DJ and a jazz band.", ["live music", "a DJ", "organise entertainment"]),
  ]),
  ("Verbs and skills", [
   ("arrange", "домовлятися, організовувати", "make plans so that something happens", "We arrange the food, tables and chairs.", ["arrange transport", "arrange a meeting"]),
   ("organise", "організовувати", "plan and prepare something", "I organised a party on a rooftop.", ["well organised", "be organised", "organise a trip"]),
   ("manage a budget", "керувати бюджетом", "control how much money you spend", "If you can’t manage a budget — forget it!", ["a small / tight budget", "be good with budgets", "over budget"]),
   ("pay attention to detail", "звертати увагу на деталі", "be careful with small things", "In this job you need to pay attention to detail.", ["it’s all details", "check every detail"]),
   ("get on with people", "ладнати з людьми", "have good relationships with people", "You really need to get on with people.", ["people skills", "get on well with"]),
  ]),
 ]),
]

def lesson(num):
    for n, t, groups in VOCAB:
        if n == num:
            return t, groups
    raise KeyError(num)
