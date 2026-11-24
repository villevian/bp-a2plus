# -*- coding: utf-8 -*-
# Content for Business Partner A2 1.3 "A survey" (IT / hybrid office version)

VI = [
 # Facilities
 dict(g="Facilities", en="a meeting room", uk="переговорна кімната", df="a room for meetings", ex="Our office has six meeting rooms.", co=["book a meeting room", "a small / big meeting room"]),
 dict(g="Facilities", en="a car park", uk="парковка", df="a place where you leave your car", ex="Does your company have a car park?", co=["a free car park", "park in the car park"]),
 dict(g="Facilities", en="an area for relaxing", uk="зона відпочинку", df="a place with sofas where you can rest", ex="We have an area for relaxing with bean bags.", co=["relax in the …", "a relax area"]),
 dict(g="Facilities", en="a kitchen area", uk="кухня (на роботі)", df="a place where you make coffee and eat", ex="I have lunch in the kitchen area.", co=["eat in the kitchen area", "a canteen = їдальня"]),
 dict(g="Facilities", en="a workspace", uk="робоче місце", df="the place where you work: desk, chair, laptop", ex="My workspace has two monitors.", co=["a quiet workspace", "a shared workspace"]),
 dict(g="Facilities", en="a quiet room", uk="тиха кімната", df="a room with no noise, for focus work or calls", ex="I take calls in the quiet room.", co=["work in a quiet room", "a phone booth = кабінка для дзвінків"]),
 dict(g="Facilities", en="the company gym", uk="спортзал компанії", df="a gym in the office or paid by the company", ex="I use the company gym twice a week.", co=["use the gym", "go to the gym"]),
 # Survey
 dict(g="Survey", en="an employee survey", uk="опитування працівників", df="a list of questions for people in a company", ex="Please complete the employee survey by Friday.", co=["complete a survey", "send out a survey"]),
 dict(g="Survey", en="facilities", uk="зручності, приміщення та обладнання", df="rooms and things a company gives you: kitchen, gym, meeting rooms", ex="We want to make our facilities better.", co=["office facilities", "use the facilities"]),
 dict(g="Survey", en="working hours", uk="робочі години", df="the time when you start and finish work", ex="My working hours are from 10 to 6.", co=["flexible working hours", "What are your working hours?"]),
 dict(g="Survey", en="work from home", uk="працювати з дому", df="do your job at home, not in the office", ex="I work from home on Fridays.", co=["work from home two days a week", "remote work"]),
 dict(g="Survey", en="spend time at your desk", uk="проводити час за столом", df="how many hours you sit and work at your desk", ex="I spend about six hours at my desk.", co=["spend time in meetings", "spend two hours on calls"]),
 dict(g="Survey", en="take a break", uk="робити перерву", df="stop working for a short time", ex="I take a break at 11 a.m.", co=["a lunch break", "a coffee break"]),
 # Questions
 dict(g="Questions", en="How do you get to work?", uk="Як ти добираєшся на роботу?", df="ask about transport", ex="— How do you get to work? — By metro.", co=["by car / by bus / on foot"]),
 dict(g="Questions", en="How often do you …?", uk="Як часто ти …?", df="ask about frequency", ex="— How often do you use the gym? — Twice a week.", co=["How often do you work from home?"]),
 dict(g="Questions", en="How long is …?", uk="Скільки триває …?", df="ask about time", ex="— How long is your lunch break? — About an hour.", co=["How long is the meeting?"]),
 dict(g="Questions", en="Does your office have …?", uk="Чи є у твоєму офісі …?", df="ask about facilities", ex="— Does your office have a gym? — Yes, it does.", co=["Yes, it does. / No, it doesn’t."]),
 dict(g="Questions", en="Where is …?", uk="Де …?", df="ask about place", ex="— Where is the kitchen? — On the second floor.", co=["on the second floor", "next to the meeting room"]),
]

FAC = [("🪑", "a meeting room"), ("🚗", "a car park"), ("🛋️", "an area for relaxing"), ("☕", "a kitchen area"), ("💻", "a workspace"), ("🎧", "a quiet room / phone booth"), ("🏋️", "a gym")]
FREQ = ["always", "usually", "often", "sometimes", "rarely", "never"]

SURVEY = {
 "A": [(1, "How do you get to work?", ["Bike", "Car", "Scooter", "Public transport", "Walk", "I work from home"]),
       (2, "What are your working hours?", None),
       (3, "How much time do you spend at your desk?", None)],
 "B": [(4, "Which team do you work in?", None),
       (5, "Do you have a problem with noise in the open space?", ["Yes", "Sometimes", "No"]),
       (6, "Does your workspace have a second monitor?", ["Yes", "No"])],
 "C": [(7, "How many hours a week do you spend in meetings (Zoom too)?", ["0–2", "2–5", "More than 5"]),
       (8, "Does your office have enough meeting rooms?", ["Yes", "No"]),
       (9, "How often do you have problems booking meeting rooms?", ["Never", "Sometimes", "Often", "Always", "I don’t book them"])],
 "D": [(10, "How often do you use the company gym?", None),
       (11, "How many times a week do you eat in the kitchen area?", None),
       (12, "Where do you take a break?", None)],
}
HEAD = {"A": "The work day", "B": "The workplace", "C": "Meetings and meeting rooms", "D": "Other facilities"}

ANS2B = [("a", "Development.", "4"), ("b", "From 10.00 a.m. to 6.30 p.m.", "2"), ("c", "About three times a week – I like to exercise after work.", "10"),
         ("d", "Five – I have lunch there every day.", "11"), ("e", "About six hours a day.", "3"), ("f", "In the area for relaxing – we have sofas there.", "12")]

EX3 = [("are / working / your / what / hours", "what are your working hours"),
       ("office / your / meeting rooms / does / enough / have", "does your office have enough meeting rooms"),
       ("have / a quiet room / does / your office", "does your office have a quiet room"),
       ("gym / the / you / use / do", "do you use the gym"),
       ("is / where / the kitchen", "where is the kitchen"),
       ("work / you / what / do / time / start", "what time do you start work"),
       ("does / your / when / finish / day", "when does your day finish"),
       ("your / does / have / company / a car park", "does your company have a car park")]

EX4 = [("Where ", " the gym?", "is"), ("", " the office have a kitchen area?", "does"), ("What time ", " you usually take a break?", "do"),
       ("What ", " the gym’s opening hours?", "are"), ("How long ", " your lunch break?", "is"), ("", " you usually work from home on Friday?", "do"),
       ("", " the office have a space for relaxing?", "does"), ("", " often do you book a meeting room?", "how")]
OPT4 = ["are", "do", "does", "how", "is"]
ANS4B = [("a", "About 11.00 a.m.", "3"), ("b", "Yes, I do.", "6"), ("c", "On the second floor.", "1"), ("d", "10.00 a.m. to 6.00 p.m. every day.", "4"),
         ("e", "Yes, it does.", "2"), ("f", "About forty-five minutes.", "5"), ("g", "About two or three times a week.", "8"), ("h", "Yes, it has a quiet room with sofas.", "7")]

# 6A review of 1.1–1.2 vocabulary inside questions
EX6 = [("How often do you ", " to meetings?", "go"), ("Who ", " out the agenda in your team?", "sends"), ("Do you ", " a meeting room for client meetings?", "book"),
       ("Does your manager ", " an update from you every day?", "get"), ("Who ", " a brief for the designer?", "creates"), ("Do you ", " data in Excel or Google Sheets?", "analyse"),
       ("Who ", " costs for a new project?", "calculates"), ("Are you ", " on Friday afternoon?", "available")]
OPT6 = ["analyse", "available", "book", "calculates", "creates", "get", "go", "sends"]

CARDS = ["How do you get to work?", "What time do you start work?", "How often do you work from home?", "How many meetings do you have a week?",
         "Does your office have a quiet room?", "Where do you take a break?", "How often do you send out an agenda?", "Do you write reports? How often?",
         "Who books meeting rooms in your team?", "Are you available on Monday morning?", "How long is your lunch break?", "What do you usually do after a planning meeting?",
         "Do you answer messages in Slack at the weekend?", "Does your company have a gym? Do you use it?", "What is your favourite place in the office?", "What facility do you want in your office?"]

# Homework (easy, A1-friendly)
HW_A = [("переговорна кімната", "a meeting room"), ("парковка", "a car park"), ("кухня (на роботі)", "a kitchen area"), ("робоче місце", "a workspace"),
        ("робити перерву", "take a break"), ("робочі години", "working hours"), ("працювати з дому", "work from home")]
HW_B = [("", " you work from home on Monday?", "do"), ("Where ", " the meeting room?", "is"), ("", " your office have a gym?", "does"),
        ("What ", " your working hours?", "are"), ("", " often do you take a break?", "how"), ("What time ", " your day finish?", "does")]
HW_C = [("you / do / the gym / use", "do you use the gym"), ("is / where / the kitchen", "where is the kitchen"),
        ("time / what / you / start work / do", "what time do you start work"), ("have / does / a car park / your office", "does your office have a car park"),
        ("often / how / you / work from home / do", "how often do you work from home")]
HW_D_SURVEY = [("1", "What are your working hours?"), ("2", "How do you get to work?"), ("3", "Does your office have a quiet room?"), ("4", "How often do you work from home?"), ("5", "Where do you take a break?")]
HW_D = [("a", "Yes, it does. I take calls there.", "3"), ("b", "In the kitchen area.", "5"), ("c", "From 9 a.m. to 6 p.m.", "1"), ("d", "Two days a week – on Monday and Friday.", "4"), ("e", "By metro.", "2")]
HW_E = [("How do you get to work?", "Як ти добираєшся на роботу?"), ("What are your working hours?", "Які в тебе робочі години?"),
        ("How often do you work from home?", "Як часто ти працюєш з дому?"), ("Does your office have a kitchen area?", "Чи є в офісі кухня?"),
        ("Where do you take a break?", "Де ти робиш перерву?"), ("What facility do you want in your office? Why?", "Що б ти хотіла мати в офісі? Чому?")]
