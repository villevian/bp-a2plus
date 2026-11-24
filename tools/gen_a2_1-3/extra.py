# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/home/claude/gen13")
from build import assemble, sel, fb, ctl, ins, self_block, E

VX = [
 dict(g="Present Simple — usually", en="I work from the office.", uk="Я (зазвичай) працюю з офісу.", df="a habit, a routine, a fact", ex="She writes code every day.", co=["every day", "usually", "on Mondays", "never"]),
 dict(g="Present Simple — usually", en="Do you … ? / Does she … ?", uk="питання в Present Simple", df="do / does + verb", ex="Does he work from home?", co=["I don’t …", "She doesn’t …"]),
 dict(g="Present Continuous — now", en="I’m working from home.", uk="Я (зараз / цього тижня) працюю з дому.", df="now, at the moment, this week", ex="She is writing code right now.", co=["now", "at the moment", "today", "this week"]),
 dict(g="Present Continuous — now", en="Are you … ing? / Is she … ing?", uk="питання в Present Continuous", df="am / is / are + verb‑ing", ex="Is he working now?", co=["I’m not …", "She isn’t …"]),
 dict(g="Words for Simple", en="every day / always / usually", uk="щодня / завжди / зазвичай", df="markers of Present Simple", ex="I usually start work at 9.", co=["often", "sometimes", "never", "on Fridays"]),
 dict(g="Words for Continuous", en="now / at the moment / today", uk="зараз / в цей момент / сьогодні", df="markers of Present Continuous", ex="I’m in a meeting at the moment.", co=["right now", "this week", "Look!", "Listen!"]),
]

A = [("Olha writes code.", "usually"), ("Olha is writing code.", "now"), ("Max is having lunch.", "now"), ("Max has lunch at one.", "usually"),
     ("I answer messages in Slack.", "usually"), ("I’m answering a message in Slack.", "now"), ("They’re testing the app.", "now"), ("They test the app on Fridays.", "usually")]
B = [("every day", "Simple"), ("now", "Continuous"), ("usually", "Simple"), ("at the moment", "Continuous"), ("on Mondays", "Simple"),
     ("right now", "Continuous"), ("never", "Simple"), ("this week", "Continuous"), ("Look!", "Continuous"), ("always", "Simple")]
C = [("Ira usually ", " at 9 a.m.", ["starts", "is starting"], "starts"), ("Right now she ", " a meeting with the client.", ["has", "is having"], "is having"),
     ("Dan ", " in Jira every morning.", ["checks", "is checking"], "checks"), ("At the moment he ", " a bug.", ["fixes", "is fixing"], "is fixing"),
     ("Olha and Max ", " at home today.", ["work", "are working"], "are working"), ("They usually ", " in the office.", ["work", "are working"], "work"),
     ("Listen! The PM ", " about the new release.", ["talks", "is talking"], "is talking"), ("We ", " a planning meeting on Mondays.", ["have", "are having"], "have")]
D_TEXT = ("<p><b>Hi team! 👋</b> Some news about me this week.</p>"
          "<p>I’m a QA engineer. I usually <b>work</b> in the office from Monday to Thursday, and on Friday I <b>work</b> from home. "
          "I usually <b>go</b> to the office by bike. I <b>test</b> our mobile app and I <b>write</b> bug reports in Jira.</p>"
          "<p>But this week is different! My office <b>is closing</b> for repairs, so this week I’<b>m working</b> from home every day. "
          "I’<b>m testing</b> the new version of the app, and right now I’<b>m writing</b> this message from my kitchen. ☕</p>"
          "<p>See you on Zoom! — <i>Max</i></p>")
D = [("Max usually works from home.", "F"), ("This week Max is working from home.", "T"), ("Max usually goes to the office by bike.", "T"),
     ("Max is going to the office by bike this week.", "F"), ("Right now Max is in the office.", "F"), ("This week Max is testing a new version of the app.", "T")]
E5 = [(("She is knowing the answer.", "She knows the answer."), 1), (("I am agree with you.", "I agree with you."), 1), (("He is working now.", "He working now."), 0),
      (("Do you work on Fridays?", "Are you work on Fridays?"), 0), (("Look! It’s raining.", "Look! It rains."), 0), (("She don’t like meetings.", "She doesn’t like meetings."), 1)]

CSS = """<style>.sl{display:flex;gap:10px;padding:8px 0;border-bottom:1px solid #f0f0f2}.sl .av{width:34px;height:34px;border-radius:6px;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:600;flex:none}.sl .av.f{background:#d1508c}.sl .av.m{background:#3b7dd8}.sl p{margin:2px 0}.tm2{color:#888;font-size:13px}.slack p{margin:6px 0}</style>"""

def build():
    KEY, S = {}, []
    G = ('<div class="gbox"><div class="gh">Two ideas — дві різні думки</div>'
         '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:10px 22px">'
         '<p>🔁 <b>Present Simple = usually</b> (звичка, факт, розклад)<br><i>I <b>work</b> from the office.</i><br><i>She <b class="a">doesn’t</b> work on Fridays.</i></p>'
         '<p>▶️ <b>Present Continuous = now</b> (зараз, цього тижня)<br><i>I<b>’m working</b> from home today.</i><br><i>She <b>isn’t working</b> now.</i></p></div>'
         '<p class="hint">🇺🇦 Питай себе: це <b>завжди / зазвичай</b>, чи <b>саме зараз</b>? Continuous = <b>am / is / are + ‑ing</b>.</p></div>')
    rows = ""
    for i, (t, a) in enumerate(A, 1):
        k = f"a_{i}"; KEY[k] = [a]
        rows += (f'<div class="tf"><span class="q">{i}. {E(t)}</span>'
                 f'<label class="opt" style="display:inline;margin:0 10px 0 0"><input type="radio" name="{k}" data-k="{k}" value="usually"> 🔁 usually</label>'
                 f'<label class="opt" style="display:inline;margin:0 10px 0 0"><input type="radio" name="{k}" data-k="{k}" value="now"> ▶️ now</label>{fb(k)}</div>')
    S.append(("A", '<div class="bsec">Meaning</div>' + G + ins("A", "Usually or now? Read and choose.", "Це звичка (usually) чи відбувається зараз (now)?") + rows + ctl("a", fn="chkRad")))
    rows = "".join(f'<div class="row"><b class="w">{E(w)}</b> → {sel("b_" + str(i), ["Simple", "Continuous"], 140)}{fb("b_" + str(i))}</div>' for i, (w, _) in enumerate(B, 1))
    for i, (_, a) in enumerate(B, 1): KEY[f"b_{i}"] = [a]
    S.append(("B", '<div class="bsec">Signal words</div>' + ins("B", "Which tense goes with these words?", "Які слова «дружать» із Simple, а які — з Continuous?") + rows + ctl("b")))
    st = ('<div class="slack"><b>#team-mobile</b> · Slack statuses<div class="sl"><div class="av f">I</div><div><b>Ira</b> <span class="tm2">PM</span><p>🗓 In a meeting with the client</p></div></div>'
          '<div class="sl"><div class="av m">D</div><div><b>Dan</b> <span class="tm2">Developer</span><p>🐞 Fixing a bug — don’t disturb</p></div></div>'
          '<div class="sl"><div class="av f">O</div><div><b>Olha</b> & <b>Max</b> <span class="tm2">QA</span><p>🏠 Working from home today</p></div></div></div>')
    rows = ""
    for i, (a, b, o, r) in enumerate(C, 1):
        k = f"c_{i}"; KEY[k] = [r]; rows += f'<div class="row">{i}. {E(a)}{sel(k, o, 130)}{E(b)}{fb(k)}</div>'
    S.append(("C", '<div class="bsec">Practice</div>' + ins("C", "Look at the Slack statuses. Choose the correct form.", "Подивись на статуси: що люди роблять ЗАРАЗ, а що — ЗАЗВИЧАЙ?") + st + rows + ctl("c")))
    rows = ""
    for i, (t, a) in enumerate(D, 1):
        k = f"d_{i}"; KEY[k] = [a]
        rows += (f'<div class="tf"><span class="q">{i}. {E(t)}</span>' + "".join(f'<label class="opt" style="display:inline;margin:0 10px 0 0"><input type="radio" name="{k}" data-k="{k}" value="{v}"> {v}</label>' for v in "TF") + fb(k) + "</div>")
    S.append(("D", '<div class="bsec">Reading</div>' + ins("D", "Read Max’s message. True (T) or false (F)?", "Прочитай повідомлення Макса. Що він робить зазвичай, а що — цього тижня?") +
              f'<div class="slack">{D_TEXT}</div>' + rows + ctl("d", fn="chkRad")))
    rows = ""
    for i, ((x, y), good) in enumerate(E5, 1):
        k = f"e_{i}"; KEY[k] = [(x, y)[good]]
        rows += f'<div class="row"><b>{i}.</b>' + "".join(f'<label class="opt"><input type="radio" name="{k}" data-k="{k}" value="{E(v)}"> {E(v)}</label>' for v in (x, y)) + fb(k) + "</div>"
    S.append(("E", '<div class="bsec">Grammar</div>' + ins("E", "Which sentence is correct?", "Обери правильне речення. Пам’ятай: know, like, agree — без ‑ing.") + rows + ctl("e", fn="chkRad")))
    rows = ("<p class='ins'>🔁 My usual working day:</p>" + "".join(f'<div class="row">I usually <input class="g" data-k="f_u{i}" style="width:min(420px,100%)"></div>' for i in range(1, 4)) +
            "<p class='ins'>▶️ Today / this week:</p>" + "".join(f'<div class="row">Today I’m <input class="g" data-k="f_n{i}" style="width:min(420px,100%)"></div>' for i in range(1, 4)))
    S.append(("F", '<div class="bsec wr">Speaking</div>' + ins("F", "Your usual day and your day today. Write 3 + 3 sentences, then tell your teacher.", "Напиши 3 речення про звичайний день і 3 — про сьогодні. Потім розкажи вчительці й запитай її: <i>What are you doing today?</i>") +
              rows + '<div class="sp"><b class="t">🗣 Ask your teacher</b>What do you usually do on Mondays? · What are you doing right now? · Are you working from home this week?</div>' +
              self_block("I understand the difference between Present Simple and Present Continuous.")))
    return KEY, S

if __name__ == "__main__":
    import os
    OUT = "/home/claude/bp-a2/lessons/1-3/all/"
    K, S = build()
    open(OUT + "extra.html", "w").write(assemble("hw.html", "EXTRA", "BP A2 1.3 A survey · Extra: Present Simple vs Continuous", K, S,
        "Valentyna Hordiienko · Middle Learning Architect", VI=VX, out="Present Simple (usually) vs Present Continuous (now): understand the difference.").replace("</head>", CSS + "</head>", 1))
    print("ok")
