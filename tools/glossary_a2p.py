"""Business Partner A2+ — updated glossary (2026), by unit and lesson.
Entry: (en, pos, uk, meaning, example, [collocations], word_family, new)
  new = True → word added in the 2026 update (not in the coursebook glossary).
Source: coursebook glossary (Unit 1) + words of the updated lessons (bleisure / Barcelona story).
"""
UNITS = [
 ("1", "Travelling for work", [
  ("1.1", "Business travel", [
   ("abroad", "adv.", "за кордоном, за кордон", "in or to a country that is not your own", "I travel abroad for work three or four times a year.", ["travel abroad", "work abroad", "go abroad"], "", False),
   ("trip", "n.", "поїздка", "when you go to a place and come back again", "My last work trip was to Barcelona.", ["a business / work trip", "go on a trip", "a short trip"], "", False),
   ("transport", "n. [U]", "транспорт", "cars, buses, trains, etc. that people use to travel", "Public transport in Barcelona is cheap and fast.", ["public transport", "transport links", "by public transport"], "transport (v) — перевозити", False),
   ("public transport", "n. [U]", "громадський транспорт", "buses, trains, etc. that anyone can pay to use", "I always use public transport when I’m abroad.", ["take / use public transport"], "", False),
   ("vehicle", "n.", "транспортний засіб", "a thing such as a car or bus that carries people or things", "You can rent an electric vehicle at the airport.", ["an electric vehicle", "rent a vehicle"], "", False),
   ("ridesharing app", "n.", "застосунок для поїздок (Uber, Bolt)", "an app for getting a car and driver with your phone", "I booked a car with a ridesharing app.", ["book a ride", "use an app"], "", False),
   ("arrival", "n.", "прибуття", "when you get to a place", "Our arrival time is 10.45.", ["arrival time", "on arrival", "the arrivals hall"], "arrive (v) — прибувати", False),
   ("departure", "n.", "відправлення, виліт", "when you leave a place, especially at the start of a journey", "Check the departure board for your gate.", ["departure time", "the departure lounge", "departures board"], "depart (v) — відправлятися", False),
   ("gate", "n.", "вихід на посадку", "the place in an airport where you get on the plane", "The flight leaves from gate 23.", ["go to the gate", "the gate closes at …"], "", False),
   ("take-off", "n.", "зліт", "when a plane leaves the ground", "Switch off your laptop before take-off.", ["before / after take-off"], "take off (phr. v) — злітати", False),
   ("landing", "n.", "посадка (літака)", "when a plane comes down to the ground", "The landing was very smooth.", ["after landing", "a smooth landing"], "land (v) — приземлятися", False),
   ("lounge", "n.", "зала очікування, лаунж", "a room in an airport or hotel where people sit and relax", "I worked in the airport lounge for an hour.", ["the departure lounge", "a business lounge"], "", False),
   ("delayed", "adj.", "затриманий (рейс)", "late, usually because of a problem (opposite on time)", "My flight was delayed by two hours.", ["a delayed flight / train", "delayed by …"], "delay (n, v) — затримка, затримувати", False),
   ("on time", "adj.", "вчасно", "happening at the planned time", "Trains in Spain are usually on time.", ["arrive on time", "leave on time"], "", False),
   ("long-haul", "adj.", "далекомагістральний", "over a long distance (opposite short-haul)", "Long-haul flights are tiring.", ["a long-haul flight"], "", False),
   ("short-haul", "adj.", "ближньомагістральний", "over a short distance (opposite long-haul)", "Kyiv–Warsaw is a short-haul flight.", ["a short-haul flight"], "", False),
   ("book", "v.", "бронювати", "arrange to have a room, seat, table, etc. in the future", "I booked two extra nights in the hotel.", ["book a room / a flight / a table", "book online", "book in advance"], "booking (n) — бронювання", False),
   ("reservation", "n.", "бронювання, резерв", "an arrangement to have a room, seat, etc. in the future", "I have a reservation for three nights.", ["make a reservation", "cancel a reservation"], "reserve (v) — бронювати", False),
   ("accommodation", "n. [U]", "житло (готель, апартаменти)", "a place where you stay or live", "The company pays for your accommodation.", ["find / book accommodation", "cheap accommodation"], "accommodate (v) — вміщати, розміщувати", False),
   ("bed and breakfast (B&B)", "n.", "міні-готель зі сніданком", "a small hotel or house where you pay for a room and breakfast", "We stayed in a B&B in the old town.", ["stay in a B&B"], "", False),
   ("youth hostel", "n.", "хостел", "a cheap place to stay, often with shared rooms", "The beach hostel is the cheapest option.", ["stay in a hostel", "a shared room"], "", False),
   ("luxury", "adj.", "розкішний", "expensive and very comfortable", "The conference is in a luxury hotel.", ["a luxury hotel", "luxury travel"], "luxurious (adj) — розкішний", False),
   ("budget", "adj.", "бюджетний, дешевий", "very low in price", "I usually fly with budget airlines.", ["a budget hotel / airline"], "", False),
   ("comfort", "n. [U]", "комфорт", "a feeling of being relaxed with nothing hurting you", "For long flights, I pay more for comfort.", ["in comfort"], "comfortable (adj) — зручний", False),
   ("facilities", "n. [plural]", "зручності, обладнання", "rooms, equipment or services in a place", "The hotel has great facilities: a gym, a pool and meeting rooms.", ["sports / conference facilities"], "", False),
   ("local", "adj.", "місцевий", "near the place where you are", "Ask the hotel for a good local restaurant.", ["local food", "a local guide", "local time"], "", False),
   ("location", "n.", "розташування, місце", "the place where something is", "The hotel is in a great location.", ["a central location", "a great location"], "locate (v) — розташовувати", False),
   ("stay", "n.", "перебування", "a period of time you spend somewhere", "Enjoy your stay in Barcelona!", ["a short / long stay", "a two-night stay"], "stay (v) — зупинятися", False),
   ("tip", "n.", "порада", "a useful piece of advice", "Can you give me some tips for Barcelona?", ["a useful tip", "travel tips"], "", False),
   ("bleisure", "n. [U]", "поєднання роботи й відпочинку в поїздці", "business + leisure: adding free days to a work trip", "Bleisure is very popular: half the guests stay for the weekend.", ["a bleisure trip", "go on a bleisure trip"], "", True),
   ("extend a trip", "v. phr.", "продовжити поїздку", "make a trip longer", "I want to extend my trip by two days.", ["extend a stay", "book extra nights"], "extension (n) — продовження", True),
   ("eSIM", "n.", "електронна SIM-карта", "a digital SIM card you buy online for mobile internet abroad", "I bought an eSIM, so I have internet in Spain.", ["buy / install an eSIM", "mobile data"], "", True),
   ("boarding pass", "n.", "посадковий талон", "the ticket you show to get on a plane, often on your phone", "My boarding pass is in the airline app.", ["a mobile boarding pass", "show your boarding pass"], "", True),
   ("take the train", "v. phr.", "їхати потягом", "travel by train (often instead of flying, to save time or CO₂)", "From Madrid, I take the train — it’s faster than flying.", ["a high-speed train", "go by train"], "", True),
  ]),
  ("1.2", "Events management", [
   ("event", "n.", "захід, подія", "something that is organised, such as a party or a conference", "We organise about forty events a year.", ["plan / organise an event", "a corporate event", "attend an event"], "", False),
   ("events management", "n. [U]", "організація заходів (професія)", "the job of organising events such as conferences", "She works in events management.", ["an events manager", "an events company"], "", False),
   ("plan an event", "v. phr.", "планувати захід", "decide what, when and where an event happens", "Alicia plans events for tech companies.", ["plan a conference", "event planning"], "planner (n) — планувальник", True),
   ("conference", "n.", "конференція", "a large formal meeting where people discuss important things", "300 people attend the conference every year.", ["attend / go to a conference", "speak at a conference", "a two-day conference"], "", False),
   ("product launch", "n.", "запуск продукту", "an event to show a new product for the first time", "The product launch is on Thursday.", ["launch a new product", "a launch party"], "launch (v) — запускати", True),
   ("team offsite", "n.", "виїзна зустріч команди", "a meeting or event for a team outside the office", "Our team offsite is in a villa near Barcelona.", ["go on an offsite", "a two-day offsite"], "", True),
   ("hybrid event", "n.", "гібридний захід", "an event with people in the room and people online", "It’s a hybrid event — we stream the talks.", ["join online / in person", "stream the talks"], "", True),
   ("venue", "n.", "місце проведення", "the place where an event happens", "We choose the least expensive venue possible.", ["book / choose a venue", "an outdoor venue"], "", False),
   ("client", "n.", "клієнт", "a person or company that pays for a service", "Most of her clients are businesses.", ["a corporate client", "client satisfaction"], "", False),
   ("guest", "n.", "гість", "a person who is invited to an event", "We had about three hundred guests.", ["invite guests", "a guest list"], "", True),
   ("budget", "n.", "бюджет", "the money that is available, or a plan for how to spend it", "We talk about the budget at the first meeting.", ["a small / tight budget", "manage a budget", "over budget"], "", False),
   ("theme", "n.", "тема (заходу)", "the main idea of a party, event, etc.", "The party had a ‘no laptops’ theme.", ["a party theme", "a circus theme"], "", False),
   ("entertainment", "n. [U]", "розважальна програма", "music, shows or activities for guests", "The entertainment is a DJ and a jazz band.", ["live music", "organise entertainment"], "entertain (v) — розважати", True),
   ("informal", "adj.", "неформальний", "relaxed and friendly (opposite formal)", "An informal dinner is easier to plan than a formal one.", ["an informal meeting / event"], "formal (adj) — офіційний", False),
   ("organise", "v.", "організовувати", "plan and prepare something", "I organised a party on a rooftop.", ["organise an event / a trip"], "organisation (n), organised (adj), organiser (n)", True),
   ("pay attention to detail", "v. phr.", "звертати увагу на деталі", "be careful with small things", "In this job you need to pay attention to detail.", ["it’s all details", "check every detail"], "", True),
   ("get on with people", "phr. v.", "ладнати з людьми", "have good relationships with people", "You really need to get on with people.", ["people skills", "get on well with …"], "", True),
  ]),
  ("1.3", "Small talk", [
   ("make small talk", "v. phr.", "вести світську бесіду", "talk about easy, friendly topics with people you don’t know well", "At the conference, I made small talk with people from five countries.", ["small talk topics", "be good at small talk"], "", True),
   ("introduce yourself", "v. phr.", "представитися", "tell someone your name and who you are", "Let me introduce myself — I’m Anna from Kyiv.", ["introduce a colleague"], "introduction (n) — знайомство", True),
   ("Nice to meet you in person.", "phrase", "Приємно нарешті познайомитися наживо.", "what you say to someone you knew only online", "Hi Tom! Nice to meet you in person — after so many video calls!", ["meet in person", "face to face"], "", True),
   ("networking event", "n.", "захід для знайомств (нетворкінг)", "an event where people meet to make useful business contacts", "There’s a networking event after the talks.", ["go to a networking event"], "network (v) — заводити контакти", True),
   ("show interest", "v. phr.", "проявляти інтерес", "show that you want to hear more (ask questions, smile, nod)", "Show interest: ask a question back.", ["Really? / That’s interesting!"], "interested (adj), interesting (adj)", True),
  ]),
  ("1.4", "Dealing with problems", [
   ("induction", "n.", "вступний інструктаж (для новачків)", "information and training for a new employee", "The induction is on your first morning.", ["an induction briefing / day"], "", False),
   ("intranet", "n.", "внутрішня мережа компанії", "a company’s internal network, like the internet but private", "You can find the travel policy on the intranet.", ["log on to the intranet"], "", False),
   ("log on / log in", "phr. v.", "увійти (в систему)", "start using a computer or app with your name and password", "I can’t log in to my email from the hotel.", ["log in to an app", "log out"], "", False),
   ("log-in details", "n. [plural]", "дані для входу", "your username and password", "Check your log-in details and try again.", ["username", "password"], "", False),
   ("lock someone out", "phr. v.", "заблокувати доступ", "stop someone from using a computer or account", "After three wrong passwords, the system locked me out.", ["be locked out of your account"], "", False),
   ("network", "n.", "мережа (комп’ютерна)", "computers connected together", "The hotel Wi-Fi network is very slow.", ["connect to the network", "a Wi-Fi network"], "", False),
   ("set up", "phr. v.", "налаштувати", "make something ready to use", "Can you help me set up my email on my phone?", ["set up an account"], "set-up (n) — налаштування", False),
   ("extension", "n.", "внутрішній номер (телефону)", "a phone number inside an office system", "Call IT on extension 5182.", ["extension number"], "", False),
   ("reset a password", "v. phr.", "скинути пароль", "make a new password when you forget the old one", "I need to reset my password.", ["forget your password", "a new password"], "", True),
   ("connect", "v.", "підключити(ся)", "join a device to the internet, a projector, etc.", "My laptop doesn’t connect to the projector.", ["connect to the Wi-Fi", "connect a laptop"], "connection (n) — з’єднання", True),
   ("IT support / help desk", "n.", "служба IT-підтримки", "people who help with computer problems", "I sent a message to the help desk.", ["contact IT support", "open a ticket"], "", True),
  ]),
  ("1.5", "Asking for information", [
   ("enquire", "v.", "дізнаватися, робити запит", "ask for information (formal)", "I’m writing to enquire about the conference fee.", ["enquire about …"], "enquiry (n) — запит", False),
   ("confirm", "v.", "підтвердити", "say that an arrangement is definite", "Could you confirm my booking, please?", ["confirm a booking / the dates"], "confirmation (n) — підтвердження", False),
   ("look forward to", "phr. v.", "з нетерпінням чекати", "be happy about something in the future (end of an email)", "I look forward to hearing from you.", ["look forward to meeting you"], "", False),
   ("request", "n., v.", "запит; просити", "asking for something politely", "I have a request: can I stay two more days?", ["make a request", "a request for information"], "", True),
   ("travel policy", "n.", "правила компанії щодо відряджень", "company rules about work trips (who pays, which hotel, etc.)", "Our travel policy says the company pays for business days only.", ["check the travel policy"], "", True),
  ]),
  ("W1", "Business workshop: A business trip", [
   ("delegate", "n.", "делегат, учасник", "a person who goes to a conference for an organisation", "Over 300 delegates attend the conference.", ["conference delegates"], "", False),
   ("accommodate", "v.", "вміщати", "have space for a number of people or things", "The hall can accommodate 200 people.", ["accommodate guests"], "accommodation (n)", False),
   ("expire", "v.", "закінчуватися (про термін)", "stop being valid", "My passport expires next year.", ["expiry date"], "expiry (n) — закінчення терміну", False),
   ("cancelled flight", "n.", "скасований рейс", "a flight that does not happen", "Our flight was cancelled because of a strike.", ["cancel a flight / a booking"], "cancel (v), cancellation (n)", True),
   ("rebook", "v.", "перебронювати", "book again for a different time", "The airline rebooked me on the next flight.", ["rebook a flight / a hotel"], "", True),
   ("strike", "n.", "страйк", "when workers stop working to protest", "There’s a train strike on Monday.", ["a train / airport strike", "go on strike"], "", True),
   ("change your plans", "v. phr.", "змінити плани", "do something different from what you planned", "Sorry, I need to change my plans.", ["a change of plan", "last-minute changes"], "", True),
  ]),
 ]),
]

def trainer_vocab():
    """Lessons in the format build_vocab.py reads: [(num, title, [(group, [(en, uk, def, ex)])])]"""
    out = []
    for _, _, lessons in UNITS:
        for num, title, items in lessons:
            out.append((num, title, [("Words", [(e[0], e[2], e[3], e[4]) for e in items])]))
    return out
