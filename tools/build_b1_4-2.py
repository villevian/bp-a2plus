"""Business Partner B1 · 4.2 Back to the office? — LESSON + EXTRA (review: vocabulary, passive, causative have).
Usage: python3 build_b1_4-2.py OUTDIR [STUDENT_CODE]   -> OUTDIR/lesson.html, OUTDIR/extra.html
"""
import sys, os
from bp_page import page, fb, sel, inp, ta, ctl, radios, SELF
OUTDIR = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
os.makedirs(OUTDIR, exist_ok=True)
K = {}

# ---------------- LESSON ----------------
TOOLS = ["Zoom", "Notion", "Slack", "Jira"]
L1 = [("a", "Jira", "is a project tracking tool where tasks are created, assigned and moved across a board."),
      ("b", "Slack", "is a messaging app where teams talk in channels and threads."),
      ("c", "Notion", "started as a note-taking app; now it’s used by many teams as a shared wiki."),
      ("d", "Zoom", "is a video call platform for meetings, webinars and daily stand-ups.")]
HEAD = [("A", "Back-to-back calls"), ("B", "‘You’re at home, so you’re free’"), ("C", "Alone at the desk"), ("D", "The office that never closes"), ("E", "Out of sight, out of mind")]
R2B = ["C", "E", "D", "A", "B"]
INTRO = ("In 2020, millions of people were sent home with a laptop and a promise: ‘It’s only for a few weeks.’ Six years later, the debate continues. Office attendance is rising again: "
         "workers around the world now spend about 3.2 days a week in the office, up from 2.7 in 2024. Yet in a 2026 survey of over 4,000 US workers, only 4% said they wanted to work in the office full-time. "
         "So what is really wrong with working from home? I spoke to Marta Lis, a project manager who has led a distributed team from her kitchen table for five years.")
SECS = ["Loneliness is the problem that is mentioned most often in online remote-work communities. In one large survey, one in five remote workers named it as their biggest challenge. "
        "‘Some weeks I’m only spoken to on Slack,’ Marta says. ‘I didn’t realise how much I needed small talk by the coffee machine.’ Younger employees, who are still building their professional networks, are affected most.",
        "Remote workers often feel invisible – and they may be right. Research shows that people who work from home are promoted less often than their office colleagues, even when their results are just as good. "
        "Managers simply notice the people they see every day. ‘Last year a new team lead was chosen,’ Marta remembers. ‘He was in the office every day. I delivered more projects, but nobody saw it.’",
        "When your laptop lives on the kitchen table, work never really ends. Many remote workers say they work longer hours, not shorter ones. Messages are sent at 10 p.m., and people feel they have to answer. "
        "‘Nobody tells you to reply in the evening,’ Marta explains, ‘but if you don’t, you feel guilty.’ For many people, this is how burnout starts.",
        "Surprisingly, many extra meetings are created by managers who are worried about losing touch with their teams. A quick check-in is added here, a status call there, and soon the whole day is filled with video calls. "
        "‘On my worst day, I was invited to seven meetings,’ Marta says. ‘When was I supposed to do the actual work?’",
        "The last problem is more practical. Friends and family often think that people who work from home have the day off. ‘My neighbour asks me to wait for her deliveries,’ Marta laughs. "
        "Remote workers also pay more for electricity and heating, and these costs are rarely covered by employers."]
END = ("So, is the office the answer? Not completely. Most workers still don’t want to go back five days a week, and many say they are more productive at home. But the problems above are real, and they are not solved by a faster laptop or another app. "
       "Marta now goes to the office three days a week. ‘I didn’t want to give up working from home,’ she says. ‘I just wanted to be seen again.’ Perhaps that is the real lesson of 2026: the best place to work is not home or the office, but a smart mix of both.")

def article(with_sel):
    h = ['<div class="art"><h3>Who wants to go back to the office?</h3><p class="sub2">Six years after the big move home, the debate isn’t over</p><p>%s</p>' % INTRO]
    for i, s in enumerate(SECS):
        if with_sel:
            hd = sel("r2_%d" % (i + 1), ["%s – %s" % x for x in HEAD], 250)
        else:
            hd = "<i>%s</i>" % dict(HEAD)[R2B[i]]
        h.append('<div class="sh"><span class="num">%d</span>%s</div><p>%s</p>' % (i + 1, hd, s))
    h.append("<p>%s</p></div>" % END)
    return "".join(h)

for i, (l, t, _) in enumerate(L1): K["l1_%s" % l] = [t]
for i, a in enumerate(R2B): K["r2_%d" % (i + 1)] = ["%s – %s" % (a, dict(HEAD)[a])]

s1 = ('<div class="bsec">Lead-in</div><p class="ins"><b class="x">1</b>Work in pairs. Look at the names of these tools and discuss the questions.</p>'
      '<div class="chips">%s</div>' % "".join("<span>%s</span>" % t for t in TOOLS) +
      '<p class="ins"><span class="q">1</span>What type of tools are they? Match each tool with a description.</p>' +
      "".join('<div class="row"><b class="w">%s</b>%s %s%s</div>' % (l, sel("l1_%s" % l, TOOLS, 110), d, fb("l1_%s" % l)) for l, _, d in L1) + ctl("l1") +
      '<p class="ins"><span class="q">2</span>What problems do people have when they work remotely? Make a list.</p>' + ta("l1_2", "1 …\n2 …\n3 …", 120) +
      '<p class="ins"><span class="q">3</span>The article is called <i>Who wants to go back to the office?</i> Which five problems do you expect to read about? Why?</p>' + ta("l1_3", "I expect to read about … because …"))
s2 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">2</b><b>A</b> Read the article quickly. Which of your predictions are mentioned? Which problem surprised you?</p>' + ta("r2a", "My predictions … / What surprised me …", 70) +
      '<p class="ins"><b>B</b> Match headings A–E with sections 1–5 of the article.</p><div class="box">%s</div>' % " · ".join("<b>%s</b> %s" % x for x in HEAD) +
      article(True) + "".join(fb("r2_%d" % (i + 1)) for i in range(0)) + ctl("r2"))
Q3 = [("2", "What two statistics about the office are mentioned at the beginning?", "Workers spend about 3.2 days a week in the office (up from 2.7 in 2024); only 4% of US workers want to work in the office full-time."),
      ("3", "Which group of employees is affected by loneliness most? Why?", "Younger employees, because they are still building their professional networks."),
      ("4", "Why didn’t Marta get the team lead job?", "The new team lead was in the office every day; managers didn’t see her results."),
      ("5", "Why do many remote workers answer messages late in the evening?", "They feel guilty if they don’t answer."),
      ("6", "Who creates many of the extra meetings? Why?", "Managers, because they are worried about losing touch with their teams."),
      ("7", "What do friends and family often think about people who work from home?", "That they have the day off."),
      ("8", "Is the writer for or against working from the office? Why do you think so?", "Neither completely – the writer thinks a mix of home and office is best.")]
K["q3_1"] = ["b"]
s3 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">3</b>Read the article again and answer the questions.</p><details class="ad"><summary>📄 Show the article</summary>%s</details>' % article(False) +
      '<p class="ins"><span class="q">1</span>What does <i>out of sight, out of mind</i> mean in the article? Remote workers …</p>' +
      radios("q3_1", [("a", "<b>a</b> forget about their tasks when they work from home."), ("b", "<b>b</b> are not noticed by managers because they aren’t in the office."), ("c", "<b>c</b> don’t want to see their colleagues.")]) + fb("q3_1") + ctl("q3_1".rsplit("_", 1)[0], "chkRad") +
      "".join('<p class="ins"><span class="q">%s</span>%s</p>%s<button class="btn l" onclick="model(\'m3_%s\')" style="margin-top:6px">Show answer</button><div class="model" id="m3_%s">%s</div>' % (n, q, ta("q3_%s" % n, "", 60), n, n, a) for n, q, a in Q3))
s4 = ('<div class="bsec">Speaking</div><p class="ins"><b class="x">4</b>Work in pairs and discuss the questions.</p>' +
      "".join('<div class="card">%d. %s</div>' % (i + 1, q) for i, q in enumerate(["Which of the five problems is the biggest for you or your team? Why?", "As a project manager, what can you do to make remote team members more visible?", "How many meetings a day are too many? How are meetings organised in your team?"])) +
      '<p class="hint">Notes (optional)</p>' + ta("d4", "My ideas …"))
TENSES = ["Present Simple passive", "Past Simple passive", "Present Simple active", "Past Simple active"]
K["g5a_1"] = ["Present Simple passive"]; K["g5a_2"] = ["Past Simple passive"]; K["g5b_1"] = ["by"]
s5 = ('<div class="bsec">Grammar <span class="sub">Present Simple and Past Simple passive</span></div>'
      '<p class="ins"><b class="x">5</b><b>A</b> Look at these extracts from the article. What verb forms are the words in bold? What tense are they?</p>'
      '<div class="ext">1 Many extra meetings <b>are created</b> by managers who are worried about losing touch with their teams.<br>%s%s</div>' % (sel("g5a_1", TENSES, 240), fb("g5a_1")) +
      '<div class="ext">2 In 2020, millions of people <b>were sent</b> home with a laptop.<br>%s%s</div>' % (sel("g5a_2", TENSES, 240), fb("g5a_2")) + ctl("g5a") +
      '<p class="ins"><b>B</b> Look at sentence 1 again. Which preposition do we use to show who does the action? %s%s</p>' % (inp("g5b_1", 80), fb("g5b_1")) + ctl("g5b") +
      '<div class="gbox"><div class="gh">Present Simple and Past Simple passive</div><p><b>Present Simple passive:</b> am / is / are + past participle → <i>Tasks <b>are assigned</b> in Jira.</i></p>'
      '<p><b>Past Simple passive:</b> was / were + past participle → <i>The deadline <b>was moved</b> last week.</i></p><p><b>by + agent</b> (only when it’s important who did it) → <i>The report was approved <b>by the client</b>.</i></p></div>')
B6 = [("MEETINGS", "Daily stand-ups <sup>1</sup>__ (hold) at 10:00 on Zoom. They <sup>2</sup>__ (last) no longer than 15 minutes. Meetings without an agenda <sup>3</sup>__ (not accept)."),
      ("COMMUNICATION", "Urgent questions <sup>4</sup>__ (send) in the #urgent channel. Messages after 7 p.m. <sup>5</sup>__ (not expect) to get an answer until the next morning. Everyone <sup>6</sup>__ (update) their Slack status before a lunch break."),
      ("TASKS", "All tasks <sup>7</sup>__ (create) in Jira. Each ticket <sup>8</sup>__ (assign) to one owner, who <sup>9</sup>__ (move) it across the board until it’s done."),
      ("OFFICE DAYS", "Team office days <sup>10</sup>__ (plan) by the PM every month. On these days we <sup>11</sup>__ (meet) for retros and sprint planning. Lunch <sup>12</sup>__ (pay for) by the company.")]
A6 = ["are held", "last", "are not accepted|aren't accepted|aren’t accepted", "are sent", "are not expected|aren't expected|aren’t expected", "updates", "are created", "is assigned", "moves", "are planned", "meet", "is paid for"]
for i, a in enumerate(A6): K["g6_%d" % (i + 1)] = a.split("|")
def board():
    n = [0]; out = []
    for t, txt in B6:
        parts = txt.split("__"); h = parts[0]
        for p in parts[1:]:
            n[0] += 1; h += inp("g6_%d" % n[0], 110) + p
        out.append("<div><h4>%s</h4>%s</div>" % (t, h))
    return '<div class="board">%s</div>' % "".join(out)
s6 = ('<div class="bsec">Grammar</div><p class="ins"><b class="x">6</b>Complete your team’s hybrid working agreement on Notion with the active or present passive form of the verbs in brackets.</p>' + board() +
      ctl("g6", extra='<button class="btn l" onclick="model(\'m6\')">Show answers</button>') + '<div class="model" id="m6">%s</div>' % " · ".join("%d %s" % (i + 1, a.split("|")[0]) for i, a in enumerate(A6)))
S7 = [("Zoom", "found", "in 2011 by Eric Yuan, a former Cisco engineer.", "was founded", "T", ""),
      ("Slack", "first / develop", "as an internal tool for a video game company.", "was first developed", "T", ""),
      ("Slack", "buy", "by Google in 2021.", "was bought", "F", "It was bought by Salesforce."),
      ("Jira", "make", "by Atlassian, an American company.", "is made", "F", "Atlassian is an Australian company."),
      ("The name <i>Jira</i>", "take", "from <i>Gojira</i>, the Japanese name for Godzilla.", "was taken", "T", ""),
      ("Trello", "buy", "by Atlassian in 2017.", "was bought", "T", ""),
      ("Daily stand-ups", "usually / hold", "standing up, to keep them short.", "are usually held", "T", ""),
      ("The Agile Manifesto", "write", "by 17 software developers in 2001.", "was written", "T", "")]
WHY7 = {}
for i, (s, v, r, a, tf, why) in enumerate(S7):
    K["g7_%d" % (i + 1)] = [a]; K["g7b_%d" % (i + 1)] = [tf]
    if why: WHY7["g7b_%d" % (i + 1)] = why
s7 = ('<div class="bsec">Grammar</div><p class="ins"><b class="x">7</b><b>A</b> Complete the sentences with the past or present passive form of the verbs in brackets.</p>' +
      "".join('<div class="row">%d. %s %s (%s) %s%s</div>' % (i + 1, s, inp("g7_%d" % (i + 1), 170), v, r, fb("g7_%d" % (i + 1))) for i, (s, v, r, a, tf, why) in enumerate(S7)) + ctl("g7") +
      '<p class="ins"><b>B</b> Decide if the sentences in Exercise 7A are true (T) or false (F).</p>' +
      "".join('<div class="tf"><span class="q">%d. %s … %s</span><label><input type="radio" name="g7b_%d" data-k="g7b_%d" value="T"> T</label><label><input type="radio" name="g7b_%d" data-k="g7b_%d" value="F"> F</label>%s</div>'
              % (i + 1, s, r, i + 1, i + 1, i + 1, i + 1, fb("g7b_%d" % (i + 1))) for i, (s, v, r, a, tf, why) in enumerate(S7)) +
      '<div class="ctl"><button class="btn" onclick="chkRad(\'g7b\',WHY7)">Check</button><span class="res" id="r_g7b"></span></div>')
MODEL8 = ("Hi team! Quick update on our new hybrid schedule. From 1 December, Tuesday, Wednesday and Thursday are planned as office days. Sprint planning and retros are held in person, "
          "and lunch is paid for by the company. Mondays and Fridays stay remote, and no meetings are scheduled after 4 p.m. The full calendar was shared in Notion yesterday – please check it before Friday. Questions? Drop them in this thread.")
s8 = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">8</b>Your company has a new hybrid policy: the team will work in the office three days a week. Write a Slack message to your team (60–80 words). '
      'Explain the new office days, what is done in the office and what is expected from everyone. Use at least three passive forms.</p>' + ta("w8", "Hi team! …", 150) + '<div class="res" id="wc8"></div>' +
      '<p class="ins" style="color:#6d6e70"><b style="color:#e8894a">Alternative:</b> A remote colleague writes to you: <i>‘I feel like nobody sees my work anymore.’</i> Reply in a Slack thread (60–80 words) and suggest how to make their work more visible.</p>' + ta("w8alt", "Reply in the thread …", 110) +
      '<button class="btn l" onclick="model(\'m8\')" style="margin-top:8px">Show model answer</button><div class="model" id="m8"><div class="slack"><b>Marta Lis</b><span class="t">9:14 AM · #team-general</span><br>%s</div></div>' % MODEL8 +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How successfully have you achieved the lesson outcome?"))
XJS_L = r"""const WHY7=__WHY7__;
const PASS=/\b(am|is|are|was|were)( not| usually| always| often| never| first)? (\w+ed|\w+en|paid|held|sent|made|built|bought|found|told|kept|set|put|met|shut|run|read|left|brought|thought|taught|sold|spent|lost|won|cut|hit)\b/gi;
function wc8(){const v=document.querySelector('[data-k=w8]').value;const n=(v.match(/\S+/g)||[]).length,p=(v.match(PASS)||[]).length;$("wc8").textContent=n+" words (60–80) · "+p+" passive forms (at least 3)"+(n>=60&&n<=80&&p>=3?" ✓":"")}
document.querySelector('[data-k=w8]').addEventListener("input",wc8);window.afterFill=wc8;wc8();"""
import json
VOC_L = [("Tools", ["project tracking tool", "messaging app", "channel / thread", "shared wiki", "video call platform", "daily stand-up"]),
         ("Remote work", ["work remotely", "distributed team", "office attendance", "hybrid", "back-to-back calls", "check-in / status call", "burnout", "feel guilty"]),
         ("From the article", ["out of sight, out of mind", "be promoted", "deliver projects", "lose touch with", "professional network", "small talk", "have the day off", "cover costs", "give up"]),
         ("Grammar", ["am / is / are + past participle", "was / were + past participle", "by + agent"])]
NAV_L = [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5), ("6", s6), ("7", s7), ("8", s8)]
html = page("4.2", "Back to the office?", "LESSON", "Learners can use past and present passive forms when speaking and writing.", "BP B1 4.2 Back to the office? · Lesson", CODE,
            NAV_L, {k: v for k, v in K.items()}, VOC_L, extra_js=XJS_L.replace("__WHY7__", json.dumps(WHY7, ensure_ascii=False)))
# board feedback: show numbered notes under the board
html = html.replace('<span class="h"></span></div>', '<span class="h"></span></div>')
open(os.path.join(OUTDIR, "lesson.html"), "w").write(html)

# ---------------- EXTRA (today: review) ----------------
X = {}
M1 = [("distributed team", "a team whose members work in different places"), ("office attendance", "how often people come to the office"),
      ("be promoted", "get a higher position at work"), ("lose touch with", "stop having contact with someone"),
      ("back-to-back calls", "meetings one after another with no break"), ("burnout", "feeling exhausted because you work too much"),
      ("have the day off", "not work on a normal working day"), ("small talk", "a short friendly chat about simple things"),
      ("cover costs", "pay for something"), ("feel guilty", "feel bad because you think you did something wrong")]
for i, (w, d) in enumerate(M1): X["v1_%d" % (i + 1)] = [d]
G2 = [("Our team has people in Kyiv, Warsaw and Lisbon — it’s a", "distributed team", "."),
      ("I had six", "back-to-back calls", "yesterday and no time for lunch."),
      ("If you answer messages every evening, you can get", "burnout", "."),
      ("Research shows that remote workers are", "promoted", "less often than office workers."),
      ("Managers add extra check-ins because they don’t want to lose", "touch", "with the team."),
      ("My neighbour thinks I", "have the day off", "because I work from home."),
      ("I miss", "small talk", "by the coffee machine."),
      ("Our company doesn’t", "cover", "the costs of electricity and heating.")]
for i, g in enumerate(G2): X["v2_%d" % (i + 1)] = [g[1]]
P1 = [("Our code ___ (review) by two developers before every release.", "is reviewed"),
      ("The new design ___ (approve) by the client yesterday.", "was approved"),
      ("Bugs ___ (usually / report) in Jira.", "are usually reported"),
      ("The meeting ___ (cancel) because the PM was ill.", "was cancelled|was canceled"),
      ("Notifications ___ (not send) after 7 p.m.", "are not sent|aren't sent|aren’t sent"),
      ("Our Kyiv office ___ (open) in 2022.", "was opened"),
      ("Two new developers ___ (hire) last month.", "were hired"),
      ("The roadmap ___ (update) every quarter.", "is updated")]
for i, (q, a) in enumerate(P1): X["p1_%d" % (i + 1)] = a.split("|")
P2 = [("The client approved the budget.", "The budget was approved by the client.|The budget was approved."),
      ("Managers create many extra meetings.", "Many extra meetings are created by managers.|Many extra meetings are created."),
      ("Someone moved the deadline last week.", "The deadline was moved last week."),
      ("We update the team calendar every Monday.", "The team calendar is updated every Monday.|The team calendar is updated every Monday by us."),
      ("The PM assigns each ticket to one person.", "Each ticket is assigned to one person by the PM.|Each ticket is assigned to one person."),
      ("Somebody sent the invitation at 10 p.m.", "The invitation was sent at 10 p.m.")]
for i, (q, a) in enumerate(P2): X["p2_%d" % (i + 1)] = a.split("|")
C1 = [("I had my laptop repaired last week.", "else"), ("I repaired my laptop last week.", "self"), ("We’re having our website redesigned.", "else"),
      ("She checked the contract herself.", "self"), ("Kate had her CV checked by a recruiter.", "else"), ("We clean the office every Friday.", "self")]
for i, (s, a) in enumerate(C1): X["c1_%d" % (i + 1)] = [a]
C2 = [("The office is a mess after the week. We ___ (it / clean) every Friday.", "have it cleaned|get it cleaned"),
      ("My laptop broke, so I ___ (it / repair) last week.", "had it repaired|got it repaired"),
      ("Before the interview, Kate ___ (her CV / check) by a recruiter.", "had her CV checked|got her CV checked"),
      ("Our company ___ (the new logo / design) by an agency in 2025.", "had the new logo designed|got the new logo designed"),
      ("Every year we ___ (our servers / test) by security experts.", "have our servers tested|get our servers tested"),
      ("Our presentation was in English, so we ___ (it / translate) into Polish.", "had it translated|got it translated"),
      ("The PM is very busy, so she ___ (the meeting notes / write) by an AI tool.", "has the meeting notes written|gets the meeting notes written"),
      ("Where do you ___ (your hair / cut)?", "have your hair cut|get your hair cut")]
for i, (q, a) in enumerate(C2): X["c2_%d" % (i + 1)] = a.split("|")
C3 = [("I didn’t design the logo myself. (have)", "I had the logo designed.|I had the logo designed by someone.|I had my logo designed."),
      ("A technician is going to install the new software for us. (have)", "We are going to have the new software installed.|We're going to have the new software installed.|We’re going to have the new software installed."),
      ("An agency writes our job ads. (have)", "We have our job ads written by an agency.|We have our job ads written."),
      ("A courier delivered lunch to the office. (have)", "We had lunch delivered to the office.")]
for i, (q, a) in enumerate(C3): X["c3_%d" % (i + 1)] = a.split("|")

e1 = ('<div class="bsec">Vocabulary <span class="sub">Review</span></div><p class="ins"><b class="x">1</b><b>A</b> Match the words from the lesson with their meanings.</p>' +
      "".join('<div class="row"><b style="display:inline-block;min-width:190px;font-weight:500">%s</b>%s%s</div>' % (w, sel("v1_%d" % (i + 1), sorted(d for _, d in M1), 380), fb("v1_%d" % (i + 1))) for i, (w, d) in enumerate(M1)) + ctl("v1") +
      '<p class="ins" style="margin-top:28px"><b>B</b> Complete the sentences with words from the lesson.</p><div class="box">%s</div>' % " · ".join(sorted(["distributed team", "back-to-back calls", "burnout", "promoted", "touch", "have the day off", "small talk", "cover"])) +
      "".join('<div class="row">%d. %s %s %s%s</div>' % (i + 1, a, inp("v2_%d" % (i + 1), 170), c, fb("v2_%d" % (i + 1))) for i, (a, b, c) in enumerate(G2)) + ctl("v2"))
e2 = ('<div class="bsec">Grammar <span class="sub">Passive: review</span></div>'
      '<div class="gbox"><div class="gh">Remember</div><p><b>Present Simple passive:</b> am / is / are + V3 → <i>Bugs <b>are reported</b> in Jira.</i></p><p><b>Past Simple passive:</b> was / were + V3 → <i>The meeting <b>was cancelled</b>.</i></p>'
      '<p><b>Negative:</b> <i>Messages <b>aren’t sent</b> after 7. · The report <b>wasn’t approved</b>.</i> · <b>Question:</b> <i><b>Is</b> lunch <b>paid for</b>? · When <b>was</b> Zoom <b>founded</b>?</i></p><p>Use <b>by</b> only when it’s important who did it.</p></div>'
      '<p class="ins"><b class="x">2</b><b>A</b> Complete with the Present or Past Simple passive.</p>' +
      "".join('<div class="row">%d. %s%s</div>' % (i + 1, q.replace("___", inp("p1_%d" % (i + 1), 190)), fb("p1_%d" % (i + 1))) for i, (q, a) in enumerate(P1)) + ctl("p1") +
      '<p class="ins" style="margin-top:28px"><b>B</b> Rewrite the sentences in the passive. Use <i>by</i> only if it’s important.</p>' +
      "".join('<div class="row">%d. %s<br>→ %s%s</div>' % (i + 1, q, inp("p2_%d" % (i + 1), 520), fb("p2_%d" % (i + 1))) for i, (q, a) in enumerate(P2)) + ctl("p2"))
e3 = ('<div class="bsec">Grammar <span class="sub">Causative: have something done</span></div>'
      '<div class="gbox"><div class="gh">have + something + past participle (V3)</div>'
      '<p>We use it when <b>someone else does the job for us</b> (usually a professional, often we pay for it).</p>'
      '<p>I <b>fixed</b> my laptop. → <i>I did it myself.</i> &nbsp;|&nbsp; I <b>had my laptop fixed</b>. → <i>A technician did it for me.</i></p>'
      '<table style="border-collapse:collapse;font-size:15.5px;margin:6px 0">'
      '<tr><td style="padding:3px 12px 3px 0"><b>Present</b></td><td>We <b>have</b> our office <b>cleaned</b> every Friday.</td></tr>'
      '<tr><td style="padding:3px 12px 3px 0"><b>Past</b></td><td>I <b>had</b> my CV <b>checked</b> by a recruiter.</td></tr>'
      '<tr><td style="padding:3px 12px 3px 0"><b>Continuous</b></td><td>We’<b>re having</b> our website <b>redesigned</b>.</td></tr>'
      '<tr><td style="padding:3px 12px 3px 0"><b>Future / plan</b></td><td>I’m <b>going to have</b> my logo <b>redesigned</b>.</td></tr>'
      '<tr><td style="padding:3px 12px 3px 0"><b>Negative / ?</b></td><td>We <b>didn’t have</b> the slides <b>translated</b>. · Where do you <b>have</b> your laptop <b>repaired</b>?</td></tr></table>'
      '<p><b>get</b> something done = the same, more informal: <i>I need to <b>get</b> my phone <b>fixed</b>.</i></p>'
      '<p style="color:#6d6e70">Compare with the passive: <i>My laptop <b>was repaired</b>.</i> (we only say what happened) — <i>I <b>had</b> my laptop <b>repaired</b>.</i> (I organised it)</p></div>'
      '<p class="ins"><b class="x">3</b><b>A</b> Who did the job: the person in the sentence or someone else?</p>' +
      "".join('<div class="row">%d. %s %s%s</div>' % (i + 1, s, radios("c1_%d" % (i + 1), [("self", "the person did it"), ("else", "someone else did it")]).replace('class="opt"', 'class="opt" style="display:inline;margin-left:14px"'), fb("c1_%d" % (i + 1))) for i, (s, a) in enumerate(C1)) +
      '<div class="ctl"><button class="btn" onclick="chkRad(\'c1\')">Check</button><span class="res" id="r_c1"></span></div>' +
      '<p class="ins" style="margin-top:28px"><b>B</b> Complete the sentences with <i>have</i> + object + past participle. Use the correct form of <i>have</i>.</p>' +
      "".join('<div class="row">%d. %s%s</div>' % (i + 1, q.replace("___", inp("c2_%d" % (i + 1), 240)), fb("c2_%d" % (i + 1))) for i, (q, a) in enumerate(C2)) + ctl("c2") +
      '<p class="ins" style="margin-top:28px"><b>C</b> Rewrite the sentences with <i>have something done</i>.</p>' +
      "".join('<div class="row">%d. %s<br>→ %s%s</div>' % (i + 1, q, inp("c3_%d" % (i + 1), 520), fb("c3_%d" % (i + 1))) for i, (q, a) in enumerate(C3)) + ctl("c3"))
SPK = ["What things do you have done instead of doing them yourself? (at home, at work)", "Have you ever had your CV or LinkedIn profile checked by someone? Was it useful?",
       "What jobs in your team are done by other people or companies (outsourcing)?", "What would you like to have done by AI at work? Why?",
       "Do you have your lunch delivered when you work from home or in the office?", "Is it better to work from home or from the office? Use at least two passive forms."]
e4 = ('<div class="bsec">Speaking</div><p class="ins"><b class="x">4</b>Answer the questions. Use the passive and <i>have something done</i>.</p>' +
      "".join('<div class="card">%d. %s</div>' % (i + 1, q) for i, q in enumerate(SPK)) + '<p class="hint">Notes (optional)</p>' + ta("s4", "I usually have … done. / … is done by …") +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you use the passive and <i>have something done</i>?"))
VOC_X = [("Vocabulary", [w for w, _ in M1]), ("Passive", ["am / is / are + V3", "was / were + V3", "by + agent"]),
         ("Causative", ["have + something + V3", "get + something + V3", "have my laptop repaired", "have our website redesigned", "have my CV checked"])]
html = page("4.2", "Back to the office?", "EXTRA · REVIEW", "Review: lesson vocabulary, Present and Past Simple passive, <i>have something done</i>.", "BP B1 4.2 Back to the office? · Extra", CODE,
            [("1", e1), ("2", e2), ("3", e3), ("4", e4)], X, VOC_X)
open(os.path.join(OUTDIR, "extra.html"), "w").write(html)
print("ok", OUTDIR)
