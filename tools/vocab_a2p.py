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
 ("1.3", "Small talk", [
  ("Small talk", [
   ("make small talk", "вести світську бесіду", "have a short friendly chat about easy topics with people you don’t know well", "We made small talk at the coffee machine.", ["small talk topics", "be good at small talk"]),
   ("a safe topic", "безпечна тема", "a topic that won’t upset anyone: the weather, travel, food", "The weather is always a safe topic.", ["avoid a topic", "change the subject"]),
   ("change the subject", "змінити тему", "start talking about something different", "If they look bored, change the subject.", ["Anyway, …", "By the way, …"]),
   ("show interest", "проявляти інтерес", "show that you want to hear more: ask, smile, use eye contact", "Lean forward and smile to show interest.", ["Really?", "That’s interesting!", "Oh, nice!"]),
   ("dominate the conversation", "домінувати в розмові", "talk all the time and don’t let others speak", "Shaun dominates the conversation.", ["talk about yourself", "listen carefully"]),
  ]),
  ("Questions for small talk", [
   ("Where do you come from?", "Звідки ти родом?", "ask about someone’s home country or town", "— Where do you come from? — I’m from Turkey.", ["Whereabouts?", "Where do you live?"]),
   ("What do you think about …?", "Що ти думаєш про …?", "ask for an opinion", "What do you think about this restaurant?", ["What do you think of …?"]),
   ("How long was your trip?", "Скільки тривала дорога?", "ask about a journey", "— How long was your trip? — About an hour.", ["How was your flight?"]),
   ("What do you know about …?", "Що ти знаєш про …?", "ask about someone’s information", "What do you know about working at TGC?", ["Not much.", "A little."]),
   ("Do you know …?", "Ти знаєш / бував(ла) в …?", "ask about a person or a place", "Do you know Turkey? Do you know Orla?", ["I’ve never been, but I’d like to."]),
   ("Which do you prefer, … or …?", "Що тобі більше подобається, … чи …?", "ask someone to choose", "Which do you prefer, London or Istanbul?", ["I love them both."]),
   ("What are you doing in …?", "Що ти робиш у …?", "ask why someone is in a place", "What are you doing in Dublin?", ["I’m starting a new job.", "I’m here for a conference."]),
  ]),
  ("The AAA model", [
   ("answer", "відповісти", "first, answer the question", "Answer: Italy.", ["a short answer"]),
   ("add new information", "додати нову інформацію", "then say one more thing about it", "Add: I live in Trieste.", ["Actually, …", "I went to university there."]),
   ("ask a question back", "поставити зустрічне питання", "finally, ask the other person something", "Ask: Do you know it?", ["And you?", "What about you?"]),
  ]),
 ]),
]

def lesson(num):
    for n, t, groups in VOCAB:
        if n == num:
            return t, groups
    raise KeyError(num)

# Trainer: all lessons from the updated glossary (1.2 keeps its own groups above)
from glossary_a2p import trainer_vocab as _tv
VOCAB = [x for x in _tv() if x[0] not in ("1.2", "1.3")] + VOCAB
VOCAB.sort(key=lambda x: (x[0].startswith("W"), x[0]))
