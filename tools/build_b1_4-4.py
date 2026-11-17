"""Business Partner B1 · 4.4 Business skills: Building consensus — LESSON (book version; audio 4.01/4.02 read by browser voices from the audioscript).
Usage: python3 build_b1_4-4.py OUTDIR [STUDENT_CODE]
"""
import sys, os, json
from bp_page import page, fb, sel, inp, ta, ctl, radios, SELF
OUTDIR = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
os.makedirs(OUTDIR, exist_ok=True)
A401 = [("M", "OK, so what I want to do today is focus on ways of building consensus. Building consensus is all about finding what the group wants to do, not what each individual wants to do. It’s about group needs, not individual needs. Sometimes we need to meet halfway, to find the middle ground. And sometimes we will be persuaded that one way is best."),
        ("M", "We will do some practice activities later on, but first I want to remind everybody of two basic principles we all need to follow. First, if we want to build consensus, we must make sure that everybody is involved in the conversation. Everybody must have the chance to speak. And second, everybody’s opinion is of equal weight and is to be respected. No one in the group is more important than anyone else. OK? Got it? Good, so now here’s what we are going to do.")]
A402 = [("M", "So the first thing we are going to do is decide as a group how we want to proceed. We have three options. We can stay as one large group, we can break into smaller groups, or we can work in pairs. Any thoughts? Remember, everybody must be involved in the discussion, and everybody’s opinion is to be respected. Yes, Jose? What do you think?"),
        ("J", "So I think we should stay as one big group. There are not so many of us, and it will be easy for everyone to be heard."),
        ("T", "I’m afraid I disagree. It will be much better in smaller groups. That way everyone gets much more talking time."),
        ("S", "I agree with Tanya. Much better. With a big group one or two people always dominate."),
        ("D", "Yes, I agree, too. We can be much more efficient if we work in small groups."),
        ("J", "Well, I don’t think my idea is that bad. I agree that in a big group one or two people could dominate, but that is easy to fix. We use talking sticks."),
        ("S", "What are talking sticks?"),
        ("J", "Each person has two sticks. This gives them the right to talk twice. Each time they say something they must give up a stick. When they have no more sticks they cannot talk. That way everyone has the same chance."),
        ("S", "Actually, that’s not a bad idea. But we will need more than two sticks."),
        ("J", "That was just an example. Of course we need to decide how many sticks to use."),
        ("D", "So we need to find consensus about the number of sticks before we can even start a real discussion?"),
        ("M", "That’s a good point. Yes, we need to decide on the process before we can move to a discussion. So nobody is interested in working in pairs? Good, OK. So we’re already narrowing down the options and moving towards consensus. Not everybody has spoken, so I would like to hear what the rest of us have to say. Sandrine?")]
NAMES = {"M": "Manager", "J": "Jose", "T": "Tanya", "S": "Sam", "D": "Dorothy"}
def player(n, lines, suf=""):
    script = "".join("<p><b>%s:</b> %s</p>" % (NAMES[s], t) for s, t in lines)
    return ('<div class="aud"><span class="an">🔊 %s</span><button class="btn" onclick="play(\'%s\')">▶ Listen</button><button class="btn l" onclick="stopA()">■ Stop</button>'
            '<select class="g rate" onchange="RATE=+this.value"><option value="0.85">slower</option><option value="1" selected>normal</option></select>'
            '<button class="btn l" onclick="model(\'sc_%s\')">Show script</button><div class="model" id="sc_%s">%s</div></div>') % (n, n, n.replace(".", "") + suf, n.replace(".", "") + suf, script)
K = {}
s1 = ('<div class="bsec">Lead-in</div><p class="ins"><b class="x">1</b>Work in small groups and discuss the questions. Then share your ideas with the class.</p>' +
      "".join('<div class="card">%d. %s</div>' % (i + 1, q) for i, q in enumerate([
          "Building consensus (reaching agreement) in a group can be difficult. Why is this?",
          "How do we decide what <i>consensus</i> means? Does everyone have to agree, or is a majority enough?",
          "Can anyone say no to a decision, or is it a manager’s job to decide?",
          "Some people think that different cultures find consensus in different ways. Do you agree? Think of examples from your own experience."])) + ta("l1", "Notes …", 90))
s2 = ('<div class="bsec">Listening</div><p class="ins"><b class="x">2</b>Listen to the beginning of a meeting.</p>' + player("4.01", A401) +
      "".join('<p class="ins"><span class="q">%d</span>%s</p>%s<button class="btn l" onclick="model(\'m2_%d\')" style="margin-top:6px">Show answer</button><div class="model" id="m2_%d">%s</div>' % (i + 1, q, ta("q2_%d" % (i + 1), "", 50), i + 1, i + 1, a)
              for i, (q, a) in enumerate([("What does the speaker want to do?", "Focus on ways of building consensus."), ("According to the speaker, what is building consensus about?", "Finding what the group wants to do, not what each individual wants to do.")])))
G3 = [("involved", "chance"), ("respected", "important")]
for i, a in enumerate(["involved", "chance", "respected", "important"]): K["g3_%d" % (i + 1)] = [a]
s3 = ('<div class="bsec">Listening</div><p class="ins"><b class="x">3</b>Complete the sentences using the words in the box. Then listen again to check.</p><div class="box">chance · important · involved · respected</div>'
      '<div class="row">1. If we want to build consensus, we must make sure that everybody is %s in the conversation. Everybody must have the %s to speak.</div>' % (inp("g3_1", 120), inp("g3_2", 120)) +
      '<div class="row">2. And second, everybody’s opinion is of equal weight and is to be %s. No one in the group is more %s than anyone else.</div>' % (inp("g3_3", 120), inp("g3_4", 120)) +
      "".join(fb("g3_%d" % (i + 1)) for i in range(4)) + ctl("g3") + player("4.01", A401, "b"))
s4 = ('<div class="bsec">Listening</div><p class="ins"><b class="x">4</b>Listen to the next part of the meeting. Has this group reached a consensus? Explain your answer.</p>' + player("4.02", A402) +
      ta("q4", "Yes / No, because …", 60) + '<button class="btn l" onclick="model(\'m4\')" style="margin-top:6px">Show answer</button><div class="model" id="m4">No, they haven’t. The manager says: ‘So we’re already narrowing down the options and moving towards consensus. Not everybody has spoken, so I would like to hear what the rest of us have to say.’</div>')
Q5 = [("What are the three options the manager mentions?", "Staying as one large group, breaking into small groups, working in pairs."), ("What are ‘talking sticks’?", "A way of controlling who speaks: each person has sticks and gives one up each time they speak."),
      ("What does the manager mean by ‘process’?", "‘How’ they will reach consensus — the way they will work."), ("What does the manager mean by ‘narrowing down’?", "Getting closer to consensus by removing one of the options.")]
s5 = ('<div class="bsec">Listening</div><p class="ins"><b class="x">5</b>Listen again and answer the questions.</p>' +
      "".join('<p class="ins"><span class="q">%d</span>%s</p>%s<button class="btn l" onclick="model(\'m5_%d\')" style="margin-top:6px">Show answer</button><div class="model" id="m5_%d">%s</div>' % (i + 1, q, ta("q5_%d" % (i + 1), "", 46), i + 1, i + 1, a) for i, (q, a) in enumerate(Q5)))
L6 = [("Manager", "Yes, Jose? What do you think?", 1, True), ("Tanya", "<b>I’m afraid I disagree</b>. It will be much better in smaller groups. That way everyone gets much more talking time.", 3, False),
      ("Dorothy", "<b>Yes, I agree, too.</b> We can be much more efficient if we work in small groups.", 5, False),
      ("Dorothy", "<b>So we need to</b> find consensus about the number of sticks before we can even start a real discussion?", 11, False),
      ("Jose", "Well, <b>I don’t think</b> my idea is that bad. <b>I agree that</b> in a big group one or two people could dominate, but that is easy to fix. We use talking sticks.", 6, False),
      ("Jose", "So <b>I think we should</b> stay as one big group. There are not so many of us, and it will be easy for everyone to be heard.", 2, True),
      ("Jose", "Each person has two sticks. This gives them the right to talk twice. Each time they say something they must give up a stick. When they have no more sticks they cannot talk. That way everyone has the same chance.", 8, False),
      ("Jose", "That was just an example. Of course we need to decide how many sticks to use.", 10, False),
      ("Sam", "<b>I agree with</b> Tanya. Much better. With a big group one or two people always dominate.", 4, False), ("Sam", "What are talking sticks?", 7, False),
      ("Sam", "Actually <b>that’s not a bad idea</b>. But we will need more than two sticks.", 9, False)]
rows = []
for i, (who, t, n, given) in enumerate(L6):
    k = "o6_%d" % (i + 1)
    if given: c = '<b class="giv">%d</b>' % n
    else:
        K[k] = [str(n)]; c = sel(k, [str(x) for x in range(3, 12)], 62)
    rows.append('<div class="o6"><span class="w6">%s:</span><span class="t6">%s</span>%s</div>%s' % (who, t, c, "" if given else fb(k)))
s6 = ('<div class="bsec">Functional language <span class="sub">Reaching agreement</span></div><p class="ins"><b class="x">6</b>Put this conversation in the right order so that it makes sense. The first two are done for you. Then listen to check.</p>' +
      "".join(rows) + ctl("o6") + player("4.02", A402, "b"))
CAT = ["Expressing agreement", "Expressing disagreement", "Making a suggestion", "Reacting to a suggestion"]
P7A = [("Yes, I agree, too.", 0), ("I’m afraid I disagree.", 1), ("So we need to …", 3), ("I don’t think …", 3), ("I agree that …", 0), ("I think we should …", 2), ("I agree with …", 0), ("that’s not a bad idea", 3)]
P7B = [("<b>Yes, I think you’re right.</b>", 0), ("<b>Sorry, I don’t agree with you</b>.", 1), ("<b>Why don’t we</b> work as one big group?", 2), ("<b>Good idea!</b> Let’s think about that.", 3),
       ("<b>I’m not sure I agree with you</b> on that.", 1), ("<b>How about if</b> we break into small groups after ten minutes?", 2)]
for i, (p, c) in enumerate(P7A): K["c7a_%d" % (i + 1)] = [CAT[c]]
for i, (p, c) in enumerate(P7B): K["c7b_%d" % (i + 1)] = [CAT[c]]
LINK = ["meet‿again next week", "just‿an‿example", "not‿a bad‿idea", "I’m‿afraid‿I disagree", "I want to remind‿everybody", "decide‿as‿a group", "listed‿on the board", "narrow it down‿if possible"]
s7 = ('<div class="bsec">Functional language</div><p class="ins"><b class="x">7</b><b>A</b> Put the phrases in bold from Exercise 6 into the correct category.</p>' +
      "".join('<div class="row"><span style="display:inline-block;min-width:230px">%s</span>%s%s</div>' % (p, sel("c7a_%d" % (i + 1), CAT, 240), fb("c7a_%d" % (i + 1))) for i, (p, c) in enumerate(P7A)) + ctl("c7a") +
      '<p class="ins" style="margin-top:26px"><b>B</b> Match the phrases in bold (1–6) with the categories in Exercise 7A.</p>' +
      "".join('<div class="row">%d. %s %s%s</div>' % (i + 1, p, sel("c7b_%d" % (i + 1), CAT, 240), fb("c7b_%d" % (i + 1))) for i, (p, c) in enumerate(P7B)) + ctl("c7b") +
      '<div class="gbox"><div class="gh">Pronunciation bank: consonant–vowel linking</div><p>When a word ends in a consonant and the next word starts with a vowel, we join them: <i>his‿office</i>, <i>not‿a</i>. Click 🔊 and repeat.</p>' +
      "".join('<div class="row">%d. %s <button class="btn l" style="padding:2px 10px" onclick="say1(\'%s\')">🔊</button></div>' % (i + 1, l, l.replace("‿", " ").replace("’", "\\'")) for i, l in enumerate(LINK)) + '</div>')
s8 = ('<div class="bsec wr">TASK</div><p class="ins"><b class="x">8</b><b>A</b> Choose one of the following topics to discuss, or suggest a different topic. Individually, take a few minutes to note down your ideas.</p>' +
      radios("t8", [("1", "The maximum and minimum number of working hours in a week."), ("2", "The ideal number of public holidays in a year."), ("3", "What makes a good language learner."), ("4", "My own topic (e.g. the best hybrid schedule, the ideal number of meetings a day)")]) +
      ta("t8a", "My ideas …", 90) +
      '<p class="ins"><b>B</b> Follow the four steps to discuss your ideas and try to reach agreement.</p><div class="ext"><ol style="margin:0;padding-left:20px"><li>Take turns to explain your ideas. When you are not speaking, listen and make notes.</li><li>Read your notes and decide which idea(s) you prefer.</li><li>Take turns to state your preferences and list them on the board.</li><li>As a group, discuss the preferences list using phrases from Exercises 6 and 7. Try to reach agreement on the best idea.</li></ol></div>' +
      ta("t8b", "Notes / our preferences list …", 80) +
      '<p class="ins"><b>C</b> When you have finished, discuss how well the group participated in the meeting.</p>' +
      "".join('<p class="ins"><span class="q">%d</span>%s</p>%s' % (i + 1, q, ta("t8c_%d" % (i + 1), "", 44)) for i, q in enumerate(["Did you find it useful to write down your ideas?", "Did the discussion follow the structure in Exercise 8B?", "Did the group succeed in reaching agreement?", "Which phrases in Exercises 6 and 7 did you use?"])) +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How successfully have you achieved the lesson outcome?"))
VOC = [("Building consensus", ["build consensus", "reach agreement", "majority", "meet halfway", "find the middle ground", "be involved", "of equal weight", "talking sticks", "process", "narrow down the options", "dominate"]),
       ("Agreeing / disagreeing", ["Yes, I agree, too.", "I agree with …", "I agree that …", "Yes, I think you’re right.", "I’m afraid I disagree.", "Sorry, I don’t agree with you.", "I’m not sure I agree with you on that."]),
       ("Suggesting / reacting", ["I think we should …", "Why don’t we …?", "How about if we …?", "Good idea!", "That’s not a bad idea.", "So we need to …", "I don’t think …"])]
VOICES = {"M": [1.0, 0], "J": [1.08, 1], "T": [1.15, 2], "S": [0.95, 3], "D": [1.2, 4]}
XJS = r"""const AUD=__AUD__,VO=__VO__;let RATE=1,qi=0,cur=null;
function vlist(){const v=speechSynthesis.getVoices().filter(x=>/^en/i.test(x.lang));return v.length?v:speechSynthesis.getVoices()}
function stopA(){speechSynthesis.cancel();qi=1e9}
function play(n){stopA();const L=AUD[n],vs=vlist();qi=0;const next=()=>{if(qi>=L.length)return;const [s,t]=L[qi++];const u=new SpeechSynthesisUtterance(t);const o=VO[s]||[1,0];u.pitch=o[0];u.rate=RATE;if(vs.length)u.voice=vs[o[1]%vs.length];u.lang="en-GB";u.onend=next;speechSynthesis.speak(u)};next()}
function say1(t){speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(t);u.lang="en-GB";u.rate=.9;speechSynthesis.speak(u)}
if(window.speechSynthesis)speechSynthesis.getVoices();
const st=document.createElement("style");st.textContent=".aud{background:#fff6ee;border:1px solid #f3c9a6;border-radius:6px;padding:8px 12px;margin:10px 0;display:flex;flex-wrap:wrap;gap:8px;align-items:center}.aud .an{font-weight:600;color:#c4642a}.aud .model{flex-basis:100%}.o6{display:grid;grid-template-columns:80px 1fr 70px;gap:8px;align-items:center;padding:6px 0;border-bottom:1px solid #f0f0f2}.w6{font-weight:600}.giv{display:inline-block;width:40px;text-align:center;border:1.5px solid #c4642a;border-radius:4px;color:#c4642a}";document.head.appendChild(st);"""
XJS = XJS.replace("__AUD__", json.dumps({"4.01": A401, "4.02": A402}, ensure_ascii=False)).replace("__VO__", json.dumps(VOICES))
html = page("4.4", "Building consensus", "LESSON", "Learners can use a range of expressions to build consensus in a discussion on a familiar topic.", "BP B1 4.4 Building consensus · Lesson", CODE,
            [(str(i + 1), s) for i, s in enumerate([s1, s2, s3, s4, s5, s6, s7, s8])], K, VOC, footer="Audio: read aloud by your browser from the coursebook audioscript (4.01, 4.02). ", extra_js=XJS)
open(os.path.join(OUTDIR, "lesson.html"), "w").write(html)
print("ok")
