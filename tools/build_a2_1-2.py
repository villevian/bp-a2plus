"""Business Partner A2 · 1.2 A work plan — LESSON (IT version; simple language, short UA hints for A1-level learners).
Mirrors the coursebook: Lead-in 1–2 (review of 1.1 tasks) · Vocabulary 3–4 · Reading and listening 5A–B, 6A–B (audio 1.01, updated) · Writing 7.
Updated = Slack messages + Google Calendar; Classic = emails (as in the book).
Usage: python3 build_a2_1-2.py LESSON_DIR [STUDENT_CODE]  -> LESSON_DIR/all/lesson.html and LESSON_DIR/all-classic/lesson.html
"""
import sys, os
from bp_page import page, fb, sel, inp, ta, ctl, SELF
from vocab_a2 import lesson
import vcard
from tts_dialog_text import A2_101
ROOT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3b7dd8", "#e3eefb", "#2a5fb0", "#4f9be8"
_, GROUPS = lesson("1.2")
VOC, VJS = vcard.build(GROUPS, ACC, ACC2, DARK, show_uk=True)
def ua(t): return '<span class="ua">🇺🇦 %s</span>' % t

def build(classic):
    K = {}
    # 1 Lead-in: review of 1.1
    T11 = ["go to meetings", "write emails", "answer messages in Slack", "make calls", "do research", "analyse data", "write reports", "travel for work"]
    FREQ = ["always", "usually", "often", "sometimes", "rarely", "never"]
    s1 = ('<div class="bsec">Lead-in</div><p class="ins"><b class="x">1</b>Look at the tasks from lesson 1.1. Which tasks do you do at work? How often? ' + ua("Згадай завдання з уроку 1.1. Як часто ти це робиш?") + '</p>' +
          "".join('<div class="row">%s → I %s %s</div>' % (t, sel("l1_%d" % i, FREQ, 120), t) for i, t in enumerate(T11)) +
          '<p class="ins" style="margin-top:14px">Now say it: <i>I usually go to meetings. I never travel for work.</i> Tell your teacher about your week.</p>' +
          ta("l1t", "I usually … I sometimes … I never …", 60) +
          '<p class="ins" style="margin-top:22px"><b class="x">2</b>Which meetings do you have at work? How often? ' + ua("Які наради в тебе бувають?") + '</p>'
          '<div class="chips"><span>budget meeting</span><span>client meeting</span><span>management meeting</span><span>planning meeting</span><span>project meeting</span></div>' +
          ta("l2", "I have a project meeting every … I never have …", 50))

    # 3–4 Vocabulary: calendar + to-do list
    CAL = [("Mon 25", [("10:00", "Budget meeting", "budget")]), ("Tue 26", [("9:30", "Client meeting (Zoom)", "")]),
           ("Wed 27", [("all day", "Management meeting", "")]), ("Thu 28", [("11:00", "Project meeting", "")]), ("Fri 29", [("9:00–11:00", "Demo for a client", "")])]
    TODO = ["<b>book a meeting room</b> for Friday", "<b>send out the agenda</b> for the planning meeting", "<b>create a brief</b> for the designer",
            "<b>prepare a presentation</b> for the client demo", "<b>get an update</b> from the QA team", "<b>calculate costs</b> for the new server"]
    calh = ('<div class="cal">%s</div>' % "".join('<div class="cd"><b>%s</b>%s</div>' % (d, "".join('<div class="ev">%s<br><i>%s</i></div>' % (t, e) for t, e, _ in evs)) for d, evs in CAL) +
            '<div class="todo"><b>✅ To do this week</b><ul>%s</ul></div>' % "".join("<li>☐ %s</li>" % t for t in TODO))
    DEF = [("book a meeting room", "reserve a room for a meeting"), ("budget meeting", "a meeting about money: how much we can spend"),
           ("send out the agenda", "send the list of topics for a meeting to everyone"), ("create a brief", "write a short document with the task and what the client wants"),
           ("prepare a presentation", "make slides for a talk"), ("get an update", "ask someone for new information about their work"),
           ("calculate costs", "find out how much something will cost")]
    PH = [p for p, _ in DEF]
    order = [2, 5, 0, 6, 3, 1, 4]
    for n, i in enumerate(order): K["v3_%d" % (n + 1)] = [DEF[i][0]]
    s2 = ('<div class="bsec">Vocabulary <span class="sub">Work tasks and activities</span></div>'
          '<p class="ins"><b class="x">3</b>Look at Dan’s Google Calendar and to-do list. Match the phrases in <b>bold</b> with the meanings. ' + ua("Знайди значення фраз.") + '</p>' + calh +
          "".join('<div class="row">%d. %s %s%s</div>' % (n + 1, DEF[i][1], sel("v3_%d" % (n + 1), sorted(PH), 200), fb("v3_%d" % (n + 1))) for n, i in enumerate(order)) + ctl("v3"))
    S4 = [("Can you ___ a meeting room for Friday?", "book"), ("In the ___ meeting we talk about money for the new app.", "budget"),
          ("Please send out the ___ before the meeting — the list of topics.", "agenda"), ("The designer needs a ___ with the client’s ideas.", "brief"),
          ("I need to prepare a ___ for the client demo.", "presentation"), ("Can I get an ___ from the QA team? Are the tests ready?", "update"),
          ("Let’s ___ the costs of the new server.", "calculate")]
    W4 = sorted(a for _, a in S4)
    for i, (_, a) in enumerate(S4): K["v4_%d" % (i + 1)] = [a]
    s3 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">4</b>Complete the sentences with words from Exercise 3. ' + ua("Встав слово.") + '</p>'
          '<div class="box">%s</div>' % " · ".join(W4) +
          "".join('<div class="row">%d. %s%s</div>' % (i + 1, q.replace("___", sel("v4_%d" % (i + 1), W4, 140)), fb("v4_%d" % (i + 1))) for i, (q, _) in enumerate(S4)) + ctl("v4"))

    # 5 Reading: messages / emails
    MSG = [("A", "Dan", "Hi Ira! Sorry, I’m not. I have a client meeting on Tuesday morning. How about Wednesday?"),
           ("B", "Ira", "Sorry, I’m busy on Wednesday — I’m at a management meeting all day. Are you available on Thursday 28th?"),
           ("C", "Ira", "Hi Dan! We need a planning meeting this week. Are you available on Tuesday 26th at 10 a.m.?"),
           ("D", "Ira", "Perfect! 2 p.m. on Thursday 28th in my office. I’ll send out the agenda. See you then!"),
           ("E", "Dan", "Thursday is fine. I’m available after lunch. How about 2 p.m.?")]
    ANS = {"A": "2", "B": "3", "C": "1", "D": "5", "E": "4"}
    if classic:
        cards = "".join('<div class="em"><div class="eh"><span class="lt">%s</span> From: %s · Subject: Planning meeting</div><p>%s</p><p>%s</p></div>' % (
            L, w, t.replace("Hi Ira!", "Hi Ira,").replace("Hi Dan!", "Hi Dan,"), "Best regards,<br>" + w) for L, w, t in MSG)
        what, ua5 = "emails", "Розстав листи по порядку. Лист C — перший."
    else:
        cards = "".join('<div class="sl"><span class="lt">%s</span><span class="av %s">%s</span><div><b>%s</b> <span class="tm2">#planning</span><p>%s</p></div></div>' % (
            L, "f" if w == "Ira" else "m", w[0], w, t) for L, w, t in MSG)
        what, ua5 = "Slack messages", "Розстав повідомлення по порядку. C — перше."
    for L, a in ANS.items(): K["r5_" + L] = [a]
    s4 = ('<div class="bsec">Reading and listening <span class="sub">Scheduling meetings</span></div>'
          '<p class="ins"><b class="x">5</b><b>A</b> Ira and Dan want to schedule a meeting. Put the %s in the correct order. %s is the first one. %s</p>' % (what, "C", ua(ua5)) + cards +
          "".join('<div class="row">%s → %s%s</div>' % (L, sel("r5_" + L, ["1", "2", "3", "4", "5"], 70), fb("r5_" + L)) for L in "ABCDE") + ctl("r5"))
    TIMES = ('<div class="gbox"><div class="gh">Saying the time and date</div><p>2 p.m. = <i>two o’clock in the afternoon</i> · 9.30 a.m. = <i>half past nine in the morning</i> · 12.00 = <i>twelve o’clock / noon</i><br>'
             'Thu 28 = <i>Thursday the twenty-eighth</i> · Fri 29 = <i>Friday the twenty-ninth</i></p></div>')
    K["r5b_day"] = ["Thursday 28th"]; K["r5b_time"] = ["2 p.m."]; K["r5b_place"] = ["in Ira’s office"]
    s5 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">5</b><b>B</b> Read again. When and where is the meeting? Then say the time and date aloud. ' + ua("Коли і де нарада?") + '</p>' + TIMES +
          '<details class="rd"><summary>💬 Open the messages</summary>%s</details>' % cards +
          '<div class="row">Day: %s%s</div>' % (sel("r5b_day", ["Tuesday 26th", "Wednesday 27th", "Thursday 28th", "Friday 29th"], 170), fb("r5b_day")) +
          '<div class="row">Time: %s%s</div>' % (sel("r5b_time", ["10 a.m.", "noon", "2 p.m.", "4 p.m."], 120), fb("r5b_time")) +
          '<div class="row">Place: %s%s</div>' % (sel("r5b_place", ["in Ira’s office", "on Zoom", "in Dan’s office"], 170), fb("r5b_place")) + ctl("r5b"))

    # 6 Listening
    player = ('<div class="aud"><span class="an">🔊 1.01</span><audio controls preload="none" src="../audio/1-01.mp3"></audio>'
              '<select class="g rate" onchange="document.querySelectorAll(\'audio\').forEach(a=>a.playbackRate=+this.value)"><option value="0.8">slower</option><option value="1" selected>normal</option></select>'
              '<button class="btn l" onclick="model(\'sc\')">Show script</button><div class="model" id="sc">%s</div></div>') % "".join(
              "<p><b>%s:</b> %s</p>" % ({"I": "Ira", "D": "Dan"}[s], t) for s, t in A2_101)
    L6 = [("Demo for a client", "until 11 a.m.|until 11|9–11|until eleven"), ("Call with the Berlin team", "12–1 p.m.|12–1|at 12|12.00–1.00|noon"),
          ("NEW: sprint planning meeting", "1 p.m.|1–2 p.m.|at 1|one o’clock|1.00")]
    O6 = {"0": ["until 11 a.m.", "until 2 p.m.", "from 2 p.m."], "1": ["9–10 a.m.", "12–1 p.m.", "3–4 p.m."], "2": ["11 a.m.", "1 p.m.", "2 p.m."]}
    for i, (_, a) in enumerate(L6): K["l6_%d" % (i + 1)] = [a.split("|")[0]]
    s6 = ('<div class="bsec">Listening</div><p class="ins"><b class="x">6</b><b>A</b> Ira calls Dan to change the date of the planning meeting. Listen and complete Dan’s calendar for <b>Friday 29th</b>. ' + ua("Послухай. Що в Дена в п’ятницю?") + '</p>' + player +
          "".join('<div class="row">📅 %s: %s%s</div>' % (t, sel("l6_%d" % (i + 1), O6[str(i)], 140), fb("l6_%d" % (i + 1))) for i, (t, _) in enumerate(L6)) + ctl("l6"))
    PHR = [("We need to change the ___ of the sprint planning meeting.", "date"), ("Are you ___ on Friday the 29th, in the morning?", "available"),
           ("How ___ Friday afternoon?", "about"), ("Sorry, I’m afraid I’m ___ then.", "busy"), ("___ we meet in the meeting room Kyiv?", "Shall"),
           ("I usually have lunch at one o’clock. How about ___?", "then"), ("Yes, that’s ___.", "fine"), ("___ you then.", "See")]
    WB = sorted(a for _, a in PHR)
    for i, (_, a) in enumerate(PHR): K["p6_%d" % (i + 1)] = [a]
    s7 = ('<div class="bsec">Listening</div><p class="ins"><b class="x">6</b><b>B</b> Complete the sentences from the phone call with the words in the box. Then listen again and check. ' + ua("Корисні фрази, щоб домовитись про зустріч.") + '</p>'
          '<div class="box">%s</div>' % " · ".join(WB) + player.replace('id="sc"', 'id="sc2"').replace("model('sc')", "model('sc2')") +
          "".join('<div class="row">%d. %s%s</div>' % (i + 1, q.replace("___", sel("p6_%d" % (i + 1), WB, 120)), fb("p6_%d" % (i + 1))) for i, (q, _) in enumerate(PHR)) + ctl("p6") +
          '<p class="hint">Practise: read the sentences aloud with your teacher — you are Ira, your teacher is Dan. Then swap.</p>')

    # 7 Writing
    MYCAL = '<div class="cal">%s</div>' % "".join('<div class="cd"><b>%s</b><div class="ev">%s</div></div>' % (d, e) for d, e in [
        ("Mon 25", "9–12 client meeting"), ("Tue 26", "free ✅"), ("Wed 27", "all day: workshop"), ("Thu 28", "10–11 project meeting<br>free after 11 ✅"), ("Fri 29", "free in the morning ✅")])
    if classic:
        fmt, start = "an email", "Hi …,<br>As you know, we need to have a planning meeting by Friday 29th. Are you available on …?<br>Best regards,<br>…"
    else:
        fmt, start = "a Slack message", "Hi …! 👋 We need a planning meeting by Friday 29th. Are you available on …?"
    s8 = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">7</b>You and your teacher need to have a <b>planning meeting</b> by Friday 29th. Look at your calendar. Write %s to your teacher and suggest a day and time. Your teacher answers — continue until you agree a time and a place. %s</p>' % (fmt, ua("Напиши повідомлення й домовся про час. Вчителька відповідає.")) + MYCAL +
          '<div class="card"><b>Useful phrases:</b> Are you available on …? · How about …? · Sorry, I’m busy then. · Shall we meet in / on …? · That’s fine. · See you then.</div>'
          '<p class="hint">Start like this: <i>%s</i></p>' % start +
          ta("w7a", "Your first message …", 80) + '<p class="ins">Your teacher’s answer → your reply:</p>' + ta("w7b", "Your reply …", 70) + ta("w7c", "Your last message (agree the time and place) …", 60) +
          '<div style="margin-top:20px">%s</div>' % (SELF % "I can schedule a meeting. How well can you do this now?"))

    XJS = VJS + r"""
document.head.insertAdjacentHTML("beforeend",`<style>.ua{display:block;font-size:14px;color:#6d6e70;font-weight:400;margin-top:2px}
.cal{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;margin:10px 0}.cd{border:1px solid #d6dbe4;border-radius:8px;padding:6px 8px;font-size:14px;background:#fff}.cd b{display:block;color:#2a5fb0}.ev{background:#e3eefb;border-left:3px solid #3b7dd8;border-radius:4px;padding:3px 6px;margin-top:4px}
@media(max-width:700px){.cal{grid-template-columns:1fr 1fr}}.todo{border:1px solid #d6dbe4;border-radius:8px;padding:8px 14px;margin:8px 0;background:#fffdf5}.todo ul{list-style:none;padding-left:4px;margin:4px 0}.todo b{color:#2a5fb0}
.sl{display:flex;gap:10px;padding:8px 0;border-bottom:1px solid #f0f0f2}.sl .av{width:34px;height:34px;border-radius:6px;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:600;flex:none}.sl .av.f{background:#d1508c}.sl .av.m{background:#3b7dd8}.sl p{margin:2px 0}.tm2{color:#888;font-size:13px}.lt{font-weight:700;color:#2a5fb0;font-size:20px;min-width:22px;align-self:center;margin-right:4px}
.em{border:1px solid #d6dbe4;border-radius:8px;padding:8px 14px;margin:8px 0;background:#fff}.em .eh{font-size:13px;color:#666;border-bottom:1px solid #eee;padding-bottom:4px}.em p{margin:6px 0}
.aud{display:flex;flex-wrap:wrap;gap:10px;align-items:center;background:#e3eefb;padding:8px 12px;border-radius:6px;margin:8px 0}.aud .an{font-weight:600;color:#2a5fb0}.aud audio{height:36px}.aud .model{flex-basis:100%}
details.rd summary{cursor:pointer;color:#2a5fb0;font-weight:500;margin:6px 0}.box{border:1.5px solid #c8c9cb;border-radius:6px;padding:6px 12px;display:inline-block;margin:6px 0 10px}</style>`);"""
    secs = [("1–2", s1), ("3", s2), ("4", s3), ("5A", s4), ("5B", s5), ("6A", s6), ("6B", s7), ("7", s8)]
    key = "BP A2 1.2 A work plan · " + ("Classic" if classic else "Lesson")
    return page("1.2", "A work plan", "LESSON", "Learners can schedule a meeting.", key, CODE, secs, K, VOC, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2,
                footer=("Classic version: emails (as in the book). " if classic else "Updated version: Slack + Google Calendar. ") + "Audio 1.01: updated dialogue, AI voices. ", extra_js=XJS)

for classic, d in [(False, "all"), (True, "all-classic")]:
    out = os.path.join(ROOT, d); os.makedirs(out, exist_ok=True)
    h = build(classic); open(os.path.join(out, "lesson.html"), "w").write(h); print("ok", d, len(h))
