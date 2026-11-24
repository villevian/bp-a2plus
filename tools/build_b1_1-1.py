"""Business Partner B1 · 1.1 Transferable skills — LESSON + HOMEWORK (IT adaptation, option A: Skills that survive AI).
Structure = coursebook p.8–9: Lead-in 1–2, Reading (replaces video 1.1.1) 3A–B, 4A–B, 5, Vocabulary 6–8, Project 9–10A–D, Self-assessment.
Usage: python3 build_b1_1-1.py OUTDIR [STUDENT_CODE]   -> OUTDIR/flip.html (before class), OUTDIR/lesson.html, OUTDIR/hw.html
"""
import sys, os, json
from bp_page import page, fb, sel, inp, ta, ctl, radios, SELF
OUTDIR = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
os.makedirs(OUTDIR, exist_ok=True)
K = {}
def mbtn(i, txt, label="Show ideas"):
    return '<button class="btn l" onclick="model(\'%s\')" style="margin-top:6px">%s</button><div class="model" id="%s">%s</div>' % (i, label, i, txt)

# ---------------- article (replaces video 1.1.1) ----------------
ART_T = "The skills that survive AI"
ART_S = "When AI writes the first draft of the code, what do employers actually look for?"
ART = [
 "In 2026, roughly half of all tech job ads mention AI skills, and many developers are asking themselves an uncomfortable question: if a machine can write the code, what am I being paid for? "
 "According to hiring managers, the answer is not to compete with AI, but to focus on what it can’t do. Increasingly, employers are looking for <b>transferable skills</b> – skills that can be applied to a range of tasks and roles, no matter which tools the team happens to use.",
 "‘A framework you master today may be old news by next year,’ says Lena Park, who leads an engineering team at a fintech start-up in Berlin. ‘So when I’m hiring, I’m less interested in a long list of technologies. "
 "I want people who can <b>think outside the box</b> and who can <b>set goals</b> that are ambitious but realistic. <b>Flexibility</b> matters too, because our tech stack changes almost every year.’",
 "Surprisingly, <b>critical thinking</b> has become more important since AI tools arrived, not less. AI assistants make mistakes that look extremely convincing, so a good engineer double-checks the output, asks ‘Why?’ and never accepts the first answer just because it works. "
 "<b>Problem-solving</b> works in a similar way: AI may suggest ten possible solutions, but someone still has to choose the right one and justify that choice to the rest of the team.",
 "Then there is teamwork. Most products today are built by distributed teams spread across several time zones, which means you need to be a good <b>team player</b> who works well with other people – including people you may never meet in person. "
 "Your <b>communication skills</b> are tested every day: in person, on video calls, in writing on Slack and in documentation, one-to-one with your manager, and in large groups when you demo your work to the whole company.",
 "Lena also values the ‘human’ qualities that are hard to automate: <b>honesty</b>, <b>integrity</b> and being <b>genuine</b>. ‘If you broke the build, admit it. If AI wrote half of your code, say so,’ she explains. "
 "She is looking for people who are <b>passionate</b> about the product, <b>motivated</b> and <b>hard-working</b>, with a <b>can-do attitude</b> – and enough <b>determination</b> to keep going when a release goes badly wrong.",
 "So what is her advice for people who want to stay employable? First, collect skills that you can take with you from one job, tool or team to the next. Second, be a team player, because nobody ships a successful product alone. "
 "And finally, remember that employers don’t just read your CV or scroll through your GitHub profile – they are looking at the person behind them.",
]
ART_PLAIN = " ".join(p.replace("<b>", "").replace("</b>", "") for p in ART)
def article():
    return ('<div class="art"><h3>%s</h3><p class="sub2">%s</p>%s</div>' % (ART_T, ART_S, "".join("<p>%s</p>" % p for p in ART)) +
            '<div class="ctl"><button class="btn l" onclick="readArt(this)">🔊 Listen to the article</button><span class="hint">The browser reads the text aloud.</span></div>')

VIDEO_ID = "wBEeVfhaDR4"
def video(open_=False):
    return ('<details class="ad"%s><summary>🎬 Video: <i>Use Transferable Skills For a Career In IT</i> (University of Phoenix, 2025, 3:16)</summary>'
            '<div style="position:relative;padding-top:56.25%%;margin:8px 0;max-width:720px"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0&cc_load_policy=1" '
            'style="position:absolute;inset:0;width:100%%;height:100%%;border:0;border-radius:8px" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></div>'
            '<p class="hint">Subtitles: press CC. <a href="https://www.youtube.com/watch?v=%s" target="_blank">Open on YouTube</a></p></details>') % (" open" if open_ else "", VIDEO_ID, VIDEO_ID)

ADV = lambda title, body: '<div class="card" style="border-left:4px solid #e0a100;background:#fffaf0;margin-top:22px"><b style="color:#b26b00">★ Advanced option</b> · %s<div style="margin-top:6px">%s</div></div>' % (title, body)
# ---------------- 1–2 Lead-in ----------------
BOX1 = ["calm", "good with computers", "good with numbers", "good with people", "good at problem-solving", "organised", "reliable", "resourceful", "good at explaining things", "curious"]
s1 = ('<div class="bsec">Lead-in</div><p class="ins"><b class="x">1</b>Tick (✓) the three words or phrases that best describe you.</p>'
      '<div class="chips" id="tick1">%s</div>' % "".join('<label style="border:1.5px solid #c8c9cb;border-radius:6px;padding:3px 12px;cursor:pointer"><input type="checkbox" class="t1" value="%s"> %s</label>' % (w, w) for w in BOX1) +
      '<input class="g" data-k="l1" type="hidden"><p class="hint" id="t1n">Choose three.</p>'
      '<p class="hint" style="margin-top:14px">Life skills are abilities that are useful in daily tasks at home, at work or in education.</p>')
s2 = ('<div class="bsec">Lead-in</div><p class="ins"><b class="x">2</b>Compare your answers with your teacher. Then discuss these questions.</p>'
      '<div class="card">1. Is there an expression in Exercise 1 that definitely <i>doesn’t</i> describe you?</div>' + ta("l2_1", "… doesn’t describe me because …", 60) +
      '<div class="card">2. Which is a) the most important b) the least important skill in the box for someone who works in tech? Why?</div>' + ta("l2_2", "a) … because …  b) … because …", 70))

# ---------------- 3–5 Reading ----------------
s3 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">3</b><b>A</b> Discuss the question.</p>'
      '<div class="card">According to the article you’re going to read, employers want <i>skills that can be applied to a range of tasks and roles</i> – even when AI does part of the work. What skills do you think this means? Give examples.</div>' +
      ta("r3a", "For example: … because AI can’t …", 80) +
      '<p class="ins"><b>B</b> Read (or listen to) the article. Were any of your ideas mentioned?</p><p class="hint">🏠 You read the article and watched the video before class – just compare your ideas now.</p>' + article() + video() + ta("r3b", "Yes, … was mentioned. / No, the article doesn’t mention …", 60))
A4 = ["the ability to work in teams / be a good team player, work well with other people, think outside the box, set goals you can achieve, flexibility, critical thinking, problem-solving, communication skills, honesty, integrity, being genuine, being passionate, motivated, hard-working, a can-do attitude, determination",
      "in person, on video calls, in writing (on Slack and in documentation), one-to-one, in large groups (a demo to the whole company)",
      "1 collect skills you can take from one job / tool / team to the next; 2 be a team player – nobody ships a successful product alone; 3 remember that employers look at the person behind the CV and the GitHub profile"]
Q4 = ["What skills and personal qualities does the article talk about? Add them to the list of skills you discussed in Exercise 3.",
      "What five ways of communicating are mentioned in the article?", "What are the three main pieces of advice the article gives?"]
s4 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">4</b><b>A</b> Read the article again. Answer the questions.</p><details class="ad"><summary>📄 Show the article</summary>%s</details>' % article() +
      "".join('<p class="ins"><span class="q">%d</span>%s</p>%s%s' % (i + 1, q, ta("r4_%d" % (i + 1), "In person, …" if i == 1 else "", 60), mbtn("m4_%d" % (i + 1), A4[i], "Show answer")) for i, q in enumerate(Q4)) +
      '<p class="ins"><b>B</b> Compare your answers with your teacher. Then think of two or three words to describe <i>unsuccessful</i> tech workers in 2026.</p>' + ta("r4b", "lazy, …", 50) +
      mbtn("m4b", "lazy, dishonest, negative, unmotivated, inflexible, not a team player, not able to set goals, copies AI code without checking it, never asks questions"))
s5 = ('<div class="bsec">Speaking</div><p class="ins"><b class="x">5</b>Discuss these questions.</p>'
      '<div class="card">1. Choose one of the transferable skills or personal qualities you listed in Exercise 4A. Think of at least two different situations where it might be useful.</div>' + ta("d5_1", "Critical thinking is useful when … and when …", 70) +
      '<div class="card">2. Which transferable skills are the most important in your current situation, as a professional in tech? Are there any that aren’t important?</div>' + ta("d5_2", "In my job, the most important … because …", 70) +
      ADV("One-minute talk", '<p>Prepare and give a one-minute talk: <i>“One skill AI will never replace – and why.”</i> Use this structure: <b>1</b> your claim → <b>2</b> two reasons → <b>3</b> a real example from your work → <b>4</b> a short conclusion.</p><p class="hint">Useful: <i>I’d argue that… · The main reason is… · On top of that… · For example, last month… · So, to sum up…</i></p>' + ta("d5_adv", "I’d argue that … The main reason is …", 110)))

# ---------------- 6–8 Vocabulary ----------------
P6 = [("can <b>think outside the box</b>", "d"), ("have <b>a can-do attitude</b>", "b"), ("can <b>set goals</b>", "a"), ("use <b>critical thinking</b>", "c"),
      ("have a lot of <b>determination</b>", "f"), ("are a <b>team player</b>", "g"), ("have <b>integrity</b>", "e"), ("have good <b>communication skills</b>", "h")]
S6 = {"a": "planned to pass a cloud certification in six months and studied every Saturday.",
      "b": "took the old project nobody wanted and finished it without complaining.",
      "c": "carefully checked AI-generated code line by line before merging it – and found a security bug.",
      "d": "suggested replacing a 40-page spec with a five-minute demo video – and the client loved it.",
      "e": "found a colleague’s password in a shared doc and told them to change it instead of using it.",
      "f": "failed a technical interview twice, but never gave up, kept practising and passed the third time.",
      "g": "helped a new junior set up their laptop and shared your tips in the team channel.",
      "h": "explained a difficult bug clearly to a non-technical client and really listened to their questions."}
for i, (_, a) in enumerate(P6): K["v6_%d" % (i + 1)] = [a]
def blk6(rng, letters):
    rows = "".join('<div class="row"><b class="w">%d</b>You … %s %s%s</div>' % (i + 1, P6[i][0], sel("v6_%d" % (i + 1), letters, 70), fb("v6_%d" % (i + 1))) for i in rng)
    sits = "".join('<p style="margin:3px 0"><b>%s</b> You … %s</p>' % (l, S6[l]) for l in letters)
    return '<div class="two"><div>%s</div><div class="box" style="display:block">%s</div></div>' % (rows, sits)
s6 = ('<div class="bsec">Vocabulary <span class="sub">Transferable skills</span></div><p class="ins"><b class="x">6</b>What do these words and phrases from the article mean? Match them with the best situation (a–h).</p>' +
      blk6(range(0, 4), "abcd") + '<div style="height:14px"></div>' + blk6(range(4, 8), "efgh") + ctl("v6"))
NEG = [("flexible", "inflexible"), ("motivated", "unmotivated"), ("honest", "dishonest"), ("dependable", "undependable"), ("confident", "unconfident"), ("organised", "disorganised"), ("reliable", "unreliable"), ("ambitious", "unambitious")]
NEG = [NEG[i] for i in (3, 0, 6, 2, 5, 1, 7, 4)]
for i, (a, n) in enumerate(NEG): K["v7x_%d" % (i + 1)] = [n]
T7 = [("", "adaptability", "adaptable", "a"), ("flexible", "", "flexibility", "n"), ("", "motivation", "motivated", "a"), ("confident", "", "confidence", "n"), ("", "dependability", "dependable", "a"), ("resourceful", "", "resourcefulness", "n"),
      ("", "independence", "independent", "a"), ("ambitious", "", "ambition", "n"), ("", "passion", "passionate", "a"), ("enthusiastic", "", "enthusiasm", "n"), ("", "honesty", "honest", "a"), ("authentic", "", "authenticity", "n")]
def tbl7(rows, start):
    h = '<table style="border-collapse:collapse;font-size:16px"><tr><th style="text-align:left;padding:4px 10px;background:#e6e7e8">Adjective</th><th style="text-align:left;padding:4px 10px;background:#e6e7e8">Noun</th></tr>'
    for j, (adj, noun, ans, gap) in enumerate(rows):
        n = start + j; K["v7_%d" % n] = [ans]
        cell = '<sup>%d</sup> %s%s' % (n, inp("v7_%d" % n, 150), fb("v7_%d" % n))
        h += '<tr><td style="padding:4px 10px;border-bottom:1px solid #eee">%s</td><td style="padding:4px 10px;border-bottom:1px solid #eee">%s</td></tr>' % (cell if gap == "a" else adj, cell if gap == "n" else noun)
    return h + "</table>"
s7 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">7</b>Complete the tables with the correct words.</p>'
      '<div class="two"><div>%s</div><div>%s</div></div>' % (tbl7(T7[:6], 1), tbl7(T7[6:], 7)) + ctl("v7") +
      '<p class="hint">💡 Word stress: <b>FLEX</b>ible – flexi<b>BIL</b>ity · <b>CON</b>fident – <b>CON</b>fidence · com<b>MU</b>nicate – communi<b>CA</b>tion</p>' +
      ADV("Negative prefixes", '<p>Make the adjectives negative with <b>in-</b>, <b>un-</b> or <b>dis-</b>. Then use two of them to describe the worst colleague you can imagine (no names!).</p>' + "".join('<div class="row">%d. %s → %s%s</div>' % (i + 1, a, inp("v7x_%d" % (i + 1), 170), fb("v7x_%d" % (i + 1))) for i, (a, n) in enumerate(NEG)) + ctl("v7x") + ta("v7x_use", "The worst colleague would be … and …", 50)))
s8 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">8</b>Work with your teacher.</p>'
      '<div class="card">1. Think of three or four more transferable skills that are important in tech in 2026. Use your dictionary if necessary.</div>' + ta("v8_1", "1 …\n2 …\n3 …", 90) +
      '<div class="card">2. For each skill, think of a way you could develop or demonstrate it at work.</div>' + ta("v8_2", "AI literacy – I could … / You can show it by …", 90) +
      mbtn("m8", "<b>AI literacy</b> – use AI tools every day, but always check the result; show it with a small project in your portfolio.\n"
                 "<b>async communication</b> – write clear updates in Slack so nobody needs a meeting.\n"
                 "<b>ownership</b> – take a task from start to finish and report problems early.\n"
                 "<b>giving and receiving feedback</b> – leave useful, polite comments in code reviews.\n"
                 "<b>time management</b> – estimate tasks realistically and meet deadlines."))

# ---------------- 9–10 Project ----------------
JOBS = ["backend developer", "QA engineer", "DevOps engineer", "product manager", "UX/UI designer", "tech recruiter", "customer success manager", "data analyst", "scrum master", "technical writer"]
s9 = ('<div class="bsec wr">PROJECT: Writing a job description</div><p class="ins"><b class="x">9</b>Look at the jobs below. Discuss how some of the transferable skills from Exercises 6 and 7 are necessary for each job.</p>'
      '<div class="chips">%s</div>' % "".join("<span>%s</span>" % j for j in JOBS) +
      "".join('<div class="row"><b>Job %d</b> %s needs … because …<br>%s</div>' % (i + 1, inp("p9_%dj" % (i + 1), 200, "job"), ta("p9_%d" % (i + 1), "", 50)) for i in range(3)) +
      mbtn("m9", "<b>QA engineer</b> – critical thinking (find what others miss), integrity (report every bug honestly), communication skills (explain a bug clearly to developers).\n"
                 "<b>tech recruiter</b> – good with people, confident, honest; needs determination because many candidates say no.\n"
                 "<b>DevOps engineer</b> – calm and dependable during incidents, good at problem-solving, flexible because tools change fast.", "Show model answer"))
s10 = ('<div class="bsec wr">PROJECT</div><p class="ins"><b class="x">10</b><b>A</b> Think of a job: one from Exercise 9, one you know about or one you would like to do.</p>'
       '<div class="row">• Job title: %s</div>' % inp("p10_job", 260, "e.g. Backend Engineer (remote, EU)") +
       '<div class="row">• List 3–5 things the person needs to do, e.g. <i>review pull requests, take part in daily stand-ups, talk to clients</i>.<br>%s</div>' % ta("p10_tasks", "1 …\n2 …\n3 …", 80) +
       '<div class="row">• Identify skills the person needs to take care of these responsibilities. Use skills from Exercises 6 and 7, or your own ideas.<br>%s</div>' % ta("p10_skills", "team player, …", 60) +
       '<p class="ins"><b>B</b> Write a job description for an international company based on your research (80–120 words).</p>' + ta("p10b", "We’re looking for …", 150) + '<div class="res" id="wc10"></div>' +
       mbtn("m10b", "<b>Wanted: Backend Engineer (remote, EU time zones)</b>\nWe’re a fast-growing fintech start-up and we’re looking for a motivated backend engineer to join our distributed team. "
                    "You will build and test new APIs, review pull requests and work closely with our product managers and designers. You should be a team player with good communication skills – most of our work happens in writing on Slack. "
                    "We’re looking for someone who uses critical thinking when working with AI tools, can set realistic goals and has a can-do attitude when things go wrong. Honesty and integrity are very important to us. "
                    "Flexible hours, a learning budget and a team that really listens.", "Show model answer") +
       '<p class="ins"><b>C</b> Read your teacher’s job description (or a real job ad she sends you). Does it:</p>'
       '<div class="row">• list 3–5 things the person needs to do? %s</div>' % radios("p10c_1", [("yes", "yes"), ("no", "no")]).replace('class="opt"', 'class="opt" style="display:inline;margin-left:12px"') +
       '<div class="row">• identify skills the person needs to take care of these responsibilities? %s</div>' % radios("p10c_2", [("yes", "yes"), ("no", "no")]).replace('class="opt"', 'class="opt" style="display:inline;margin-left:12px"') +
       '<p class="ins"><b>D</b> Circle any skills or personal qualities that you think have been used incorrectly. Would you like to apply for the job? Why / Why not?</p>' + ta("p10d", "I would / wouldn’t apply because …", 70) +
       '<div style="margin-top:20px">%s</div>' % (SELF % "How successfully have you achieved the lesson outcome?"))

XJS = r"""const ART=__ART__;
function readArt(b){try{if(speechSynthesis.speaking){speechSynthesis.cancel();b.textContent="🔊 Listen to the article";return}const u=new SpeechSynthesisUtterance(ART);u.lang="en-GB";u.rate=.92;
 const v=speechSynthesis.getVoices().find(x=>/^en-GB/i.test(x.lang))||speechSynthesis.getVoices().find(x=>/^en/i.test(x.lang));if(v)u.voice=v;u.onend=()=>b.textContent="🔊 Listen to the article";speechSynthesis.speak(u);b.textContent="⏹ Stop"}catch(e){}}
const T1=[...document.querySelectorAll(".t1")],H1=document.querySelector('[data-k=l1]');
function t1(){const v=T1.filter(x=>x.checked).map(x=>x.value);H1.value=v.join(", ");document.getElementById("t1n").textContent=v.length===3?"✓ "+v.join(" · "):"Choose three ("+v.length+"/3).";}
T1.forEach(x=>x.onchange=()=>{if(T1.filter(y=>y.checked).length>3)x.checked=false;t1();later()});
function wc10(){const v=document.querySelector('[data-k=p10b]').value,n=(v.match(/\S+/g)||[]).length;document.getElementById("wc10").textContent=n+" words (80–120)"+(n>=80&&n<=120?" ✓":"")}
document.querySelector('[data-k=p10b]').addEventListener("input",wc10);
window.afterFill=()=>{const v=(H1.value||"").split(", ");T1.forEach(x=>x.checked=v.includes(x.value));t1();wc10()};"""

VOC_L = [("Transferable skills", ["transferable skills", "think outside the box", "a can-do attitude", "set goals", "critical thinking", "determination", "team player", "integrity", "communication skills", "problem-solving"]),
         ("Adjective → noun", ["adaptable – adaptability", "flexible – flexibility", "motivated – motivation", "confident – confidence", "dependable – dependability", "resourceful – resourcefulness",
                               "independent – independence", "ambitious – ambition", "passionate – passion", "enthusiastic – enthusiasm", "honest – honesty", "authentic – authenticity"]),
         ("From the article", ["be applied to a range of tasks and roles", "old news", "tech stack", "double-check the output", "justify a choice", "distributed team", "time zone", "demo your work", "break the build", "admit", "hard to automate", "ship a product", "genuine", "stay employable", "the person behind the CV"]),
         ("2026 skills", ["AI literacy", "async communication", "ownership", "job description"])]
NAV = [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5), ("6", s6), ("7", s7), ("8", s8), ("9", s9), ("10", s10)]
html = page("1.1", "Transferable skills", "LESSON", "Learners can use vocabulary related to skills and personal qualities.", "BP B1 1.1 Transferable skills · Lesson", CODE,
            NAV, K, VOC_L, extra_js=XJS.replace("__ART__", json.dumps(ART_PLAIN, ensure_ascii=False)))
open(os.path.join(OUTDIR, "lesson.html"), "w").write(html)


# ================= BEFORE CLASS (flipped classroom) =================
F = {}
VS = ["project management", "stakeholder management", "problem-solving", "communication", "teamwork and collaboration"]
VD = {"project management": "IT work is almost always organised as projects: building, rolling out or improving systems.",
      "stakeholder management": "find the groups of people involved, learn how each group communicates and meet their needs.",
      "problem-solving": "use technology to solve problems for customers or for teams inside the company.",
      "communication": "listen well and explain technical ideas in plain business language to other departments.",
      "teamwork and collaboration": "IT rarely works alone – projects involve several departments and customer groups."}
for i, v in enumerate(VS): F["f1_%d" % (i + 1)] = [v]
f1 = ('<div class="bsec">Before class <span class="sub">Video</span></div><p class="ins"><b class="x">1</b><b>A</b> Watch the video. A university IT leader explains which skills from other jobs help you in IT. '
      'In what order does she mention these five skills?</p>' + video(True) + '<div class="box">%s</div>' % " · ".join(sorted(VS)) +
      "".join('<div class="row"><b class="w">%d</b>%s%s</div>' % (i + 1, sel("f1_%d" % (i + 1), sorted(VS), 260), fb("f1_%d" % (i + 1))) for i in range(5)) + ctl("f1") +
      '<p class="ins"><b>B</b> Watch again. Match each skill with what the speaker says about it.</p>')
DSORT = sorted(VD.values())
for i, v in enumerate(VS): F["f1b_%d" % (i + 1)] = [VD[v]]
f1 += "".join('<div class="row"><b style="display:inline-block;min-width:210px;font-weight:500">%s</b>%s%s</div>' % (v, sel("f1b_%d" % (i + 1), DSORT, 560), fb("f1b_%d" % (i + 1))) for i, v in enumerate(VS)) + ctl("f1b")
TF = [("She says you should connect your transferable skills to real IT examples in your application or interview.", "T", ""),
      ("She says you must learn to code before you apply for an IT job.", "F", "She doesn’t say that – she says build basic technical vocabulary."),
      ("She advises you to build basic technical vocabulary.", "T", ""),
      ("She says gaps in your knowledge are a big problem for employers.", "F", "Her advice: don’t worry too much about the gaps.")]
WHYF = {}
for i, (q, a, w) in enumerate(TF):
    F["f1c_%d" % (i + 1)] = [a]
    if w: WHYF["f1c_%d" % (i + 1)] = w
f1 += ('<p class="ins"><b>C</b> The end of the video (2:00–3:16): true (T) or false (F)?</p>' +
       "".join('<div class="tf"><span class="q">%d. %s</span><label><input type="radio" name="f1c_%d" data-k="f1c_%d" value="T"> T</label><label><input type="radio" name="f1c_%d" data-k="f1c_%d" value="F"> F</label>%s</div>'
               % (i + 1, q, i + 1, i + 1, i + 1, i + 1, fb("f1c_%d" % (i + 1))) for i, (q, a, w) in enumerate(TF)) +
       '<div class="ctl"><button class="btn" onclick="chkRad(\'f1c\',WHYF)">Check</button><span class="res" id="r_f1c"></span></div>')

# ---- 2 Vocabulary from the video ----
M2 = [("stakeholder", "a person or group who is affected by a project and cares about the result"),
      ("roll out (a system)", "introduce a new system to all the people who will use it"),
      ("internal team", "a team inside your own company"),
      ("department", "one part of a company, e.g. sales, HR or finance"),
      ("plain business language", "simple words that non-technical people understand"),
      ("gap (in your knowledge)", "something you don’t know yet"),
      ("cover letter", "a short letter you send together with your CV"),
      ("transition into IT", "move from another career into IT")]
M2 = [M2[i] for i in (5, 2, 7, 0, 4, 1, 6, 3)]
for i, (w, d) in enumerate(M2): F["v2a_%d" % (i + 1)] = [d]
C2 = [("___ a project", "manage"), ("___ a new system", "roll out"), ("___ the needs of customers", "meet"), ("___ technical ideas to other departments", "explain"),
      ("___ problems for internal teams", "solve"), ("___ your skills to real examples", "connect"), ("___ basic technical vocabulary", "build"), ("___ too much about the gaps", "worry")]
for i, (q, a) in enumerate(C2): F["v2b_%d" % (i + 1)] = [a]
W2 = [("manage", "management", "manager"), ("communicate", "communication", "communicator"), ("collaborate", "collaboration", "collaborator"),
      ("solve", "solution", "—"), ("apply", "application", "applicant"), ("lead", "leadership", "leader")]
GAPS2 = {0: [1], 1: [2], 2: [1, 2], 3: [1], 4: [1, 2], 5: [1]}
def tbl2():
    h = '<table style="border-collapse:collapse;font-size:16px"><tr>' + "".join('<th style="text-align:left;padding:4px 10px;background:#e6e7e8">%s</th>' % t for t in ["Verb", "Noun (thing / activity)", "Noun (person)"]) + "</tr>"
    for r, row in enumerate(W2):
        h += "<tr>"
        for c, w in enumerate(row):
            if c in GAPS2[r] and w != "—":
                k = "v2c_%dx%d" % (r + 1, c); F[k] = [w]
                h += '<td style="padding:4px 10px;border-bottom:1px solid #eee">%s%s</td>' % (inp(k, 160), fb(k))
            else:
                h += '<td style="padding:4px 10px;border-bottom:1px solid #eee">%s</td>' % w
        h += "</tr>"
    return h + "</table>"
F2D = [("I think my strongest skill is ___ because …", "problem-solving / communication …"), ("In my job, I often explain technical things to ___ like …", "other departments / stakeholders"),
       ("One gap in my knowledge is …, but I’m working on it by …", ""), ("If I had to write a cover letter tomorrow, I would connect … to …", "")]
fv = ('<div class="bsec">Before class <span class="sub">Vocabulary from the video</span></div>'
      '<p class="ins"><b class="x">2</b><b>A</b> Match the words and phrases about skills in IT with their meanings.</p>' +
      "".join('<div class="row"><b style="display:inline-block;min-width:220px;font-weight:500">%s</b>%s%s</div>' % (w, sel("v2a_%d" % (i + 1), sorted(d for _, d in M2), 470), fb("v2a_%d" % (i + 1))) for i, (w, d) in enumerate(M2)) + ctl("v2a") +
      '<p class="ins" style="margin-top:26px"><b>B</b> Complete the collocations with the verbs in the box. Then watch the video again and check which ideas you hear.</p>'
      '<div class="box">%s</div>' % " · ".join(sorted(a for _, a in C2)) +
      "".join('<div class="row">%d. %s%s</div>' % (i + 1, q.replace("___", inp("v2b_%d" % (i + 1), 120)), fb("v2b_%d" % (i + 1))) for i, (q, a) in enumerate(C2)) + ctl("v2b") +
      '<p class="ins" style="margin-top:26px"><b>C</b> Complete the word families.</p>' + tbl2() + ctl("v2c") +
      '<p class="ins" style="margin-top:26px"><b>D</b> Make it personal. Complete the sentences about you. Use words from A–C.</p>' +
      "".join('<div class="row">%d. %s<br>%s</div>' % (i + 1, q, ta("v2d_%d" % (i + 1), ph, 46)) for i, (q, ph) in enumerate(F2D)))
f2 = ('<div class="bsec">Before class <span class="sub">Reading</span></div><p class="ins"><b class="x">3</b>Read (or listen to) the article. Then answer the questions. Words in <b>bold</b> are the key vocabulary of the lesson.</p>' + article() +
      "".join('<p class="ins"><span class="q">%d</span>%s</p>%s%s' % (i + 1, q, ta("f2_%d" % (i + 1), "", 60), mbtn("mf2_%d" % (i + 1), A4[i], "Show answer")) for i, q in enumerate(Q4)) +
      '<p class="ins"><span class="q">4</span>Which skills are mentioned in <b>both</b> the video and the article?</p>' + ta("f2_4", "", 50) +
      mbtn("mf2_4", "problem-solving, communication (skills), teamwork / being a team player"))
f3 = ('<div class="bsec">Before class <span class="sub">Get ready to speak</span></div><p class="ins"><b class="x">4</b>Prepare for the lesson. Make short notes – we will talk about them in class.</p>'
      '<div class="card">1. Which three skills from the video and the article do you already have? Think of one real example from your work for each.</div>' + ta("f3_1", "1 problem-solving – last month I …\n2 …\n3 …", 110) +
      '<div class="card">2. Which skill do you want to develop this year? Why?</div>' + ta("f3_2", "", 60) +
      '<div class="card">3. Write down 3–5 new words or phrases from the video or the article. <span class="hint">Tip: select a word on this page and press ＋ to save it to My vocabulary.</span></div>' + ta("f3_3", "", 60) +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well did you understand the video and the article?"))
VOC_F = [("From the video", ["transferable skills", "project management", "stakeholder management", "problem-solving", "communication skills", "teamwork and collaboration", "plain business language", "technical vocabulary"]),
         ("Words about IT work", ["stakeholder", "roll out (a system)", "internal team", "department", "gap (in your knowledge)", "cover letter", "transition into IT", "manage a project", "meet the needs of customers", "explain technical ideas", "connect your skills to real examples"]),
         ("From the article", ["think outside the box", "set goals", "flexibility", "critical thinking", "team player", "integrity", "a can-do attitude", "determination", "old news", "tech stack"])]
html = page("1.1", "Transferable skills", "BEFORE CLASS", "Watch, read and prepare at home – class time is for speaking.", "BP B1 1.1 Transferable skills · Before class", CODE,
            [("1", f1), ("2", fv), ("3", f2), ("4", f3)], F, VOC_F, extra_js=("const WHYF=%s;\n" % json.dumps(WHYF, ensure_ascii=False)) + XJS.split("const T1=")[0].replace("__ART__", json.dumps(ART_PLAIN, ensure_ascii=False)))
open(os.path.join(OUTDIR, "flip.html"), "w").write(html)

# ================= HOMEWORK =================
H = {}
REC = [("can-do", "can-do attitude"), ("team", "team player"), ("critical", "critical thinking"), ("set", "set goals"), ("integrity", "integrity"), ("outside", "think outside the box"),
       ("determination", "determination"), ("communication", "communication skills")]
REC_T = ("I worked with Andrii for two years on our payments team, and I can honestly recommend him. He always has a <sup>1</sup>__ attitude: when we got the old billing system that nobody wanted, he just said ‘OK, let’s do it.’ "
         "He’s a real <sup>2</sup>__ player – he helped every new junior in the team. He uses <sup>3</sup>__ thinking with AI tools and never merges code he hasn’t checked. "
         "He knows how to <sup>4</sup>__ realistic goals for each sprint. People trust him because he has <sup>5</sup>__: when he made a mistake, he told us immediately. "
         "He also likes to think <sup>6</sup>__ the box – his idea of a five-minute demo video saved us a week of documentation. His <sup>7</sup>__ helped us finish the migration on time, "
         "and his <sup>8</sup>__ skills made our calls with the client in London much easier.")
for i, (a, _) in enumerate(REC): H["h1_%d" % (i + 1)] = [a]
def rec():
    parts = REC_T.split("__"); h = parts[0]
    for i, p in enumerate(parts[1:]): h += inp("h1_%d" % (i + 1), 130) + p
    return '<div class="slack" style="line-height:2.1"><b>LinkedIn recommendation</b><span class="t">Olha K., Engineering Manager</span><br>%s</div>' % h
h1 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">1</b>Complete the LinkedIn recommendation with the words in the box.</p>'
      '<div class="box">%s</div>' % " · ".join(sorted(a for a, _ in REC)) + rec() + ctl("h1"))
WF = [("Our team lead is very ___ – she always does what she promises.", "depend", "dependable"),
      ("For this role, ___ is more important than knowing one framework.", "flexible", "flexibility"),
      ("He speaks with a lot of ___ in meetings now.", "confident", "confidence"),
      ("We’re looking for an ___ engineer who can work without a manager.", "independence", "independent"),
      ("Her ___ for clean code is visible in every pull request.", "passionate", "passion"),
      ("Be ___ in your profile – don’t write that you know Kubernetes if you don’t.", "honesty", "honest"),
      ("The new junior shows a lot of ___ – he asks questions all the time.", "enthusiastic", "enthusiasm"),
      ("You need to be ___ – our priorities change every sprint.", "adaptability", "adaptable")]
for i, (_, _, a) in enumerate(WF): H["h2_%d" % (i + 1)] = [a]
h2 = ('<div class="bsec">Vocabulary <span class="sub">Word building</span></div><p class="ins"><b class="x">2</b>Complete the sentences with the correct form of the word in brackets.</p>' +
      "".join('<div class="row">%d. %s (%s)%s</div>' % (i + 1, q.replace("___", inp("h2_%d" % (i + 1), 160)), w, fb("h2_%d" % (i + 1))) for i, (q, w, a) in enumerate(WF)) + ctl("h2"))
CH = [("You should always ___ realistic goals for a sprint.", ["make", "set", "put"], "set"),
      ("A good engineer uses ___ thinking when AI suggests a solution.", ["critical", "serious", "careful"], "critical"),
      ("She’s a great team ___ – everybody wants to work with her.", ["partner", "member", "player"], "player"),
      ("We need someone who can think ___ the box.", ["inside", "outside", "out"], "outside"),
      ("He showed a lot of ___ when he passed the interview on his third try.", ["determination", "decision", "dependability"], "determination"),
      ("Good ___ skills are tested every day in a distributed team.", ["communication", "communicating", "communicative"], "communication")]
for i, (_, _, a) in enumerate(CH): H["h3_%d" % (i + 1)] = [a]
h3 = ('<div class="bsec">Vocabulary <span class="sub">Collocations</span></div><p class="ins"><b class="x">3</b>Choose the correct option.</p>' +
      "".join('<div class="row">%d. %s%s</div>' % (i + 1, q.replace("___", sel("h3_%d" % (i + 1), o, 150)), fb("h3_%d" % (i + 1))) for i, (q, o, a) in enumerate(CH)) + ctl("h3"))
h4 = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">4</b>Write the <i>About</i> section of your LinkedIn profile (60–90 words). Choose <b>three</b> transferable skills and, for each one, give a real example from your work that <b>shows</b> it – don’t just name it.</p>'
      '<p class="hint">Not: <i>I am a hard-working team player.</i> → But: <i>Last year I helped two new developers onboard in our distributed team, and I wrote our team’s Slack guide.</i></p>' +
      ta("h4", "I’m a … who …", 160) + '<div class="res" id="wc4"></div>' +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you talk about your transferable skills?"))
XJS_H = r"""function wc4(){const v=document.querySelector('[data-k=h4]').value,n=(v.match(/\S+/g)||[]).length;document.getElementById("wc4").textContent=n+" words (60–90)"+(n>=60&&n<=90?" ✓":"")}
document.querySelector('[data-k=h4]').addEventListener("input",wc4);window.afterFill=wc4;"""
VOC_H = [("Transferable skills", ["a can-do attitude", "team player", "critical thinking", "set goals", "integrity", "think outside the box", "determination", "communication skills"]),
         ("Word building", ["dependable", "flexibility", "confidence", "independent", "passion", "honest", "enthusiasm", "adaptable"])]
html = page("1.1", "Transferable skills", "HOMEWORK", "Learners can use vocabulary related to skills and personal qualities.", "BP B1 1.1 Transferable skills · Homework", CODE,
            [("1", h1), ("2", h2), ("3", h3), ("4", h4)], H, VOC_H, extra_js=XJS_H)
open(os.path.join(OUTDIR, "hw.html"), "w").write(html)
print("ok", OUTDIR)
