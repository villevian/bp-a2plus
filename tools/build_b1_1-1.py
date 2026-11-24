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

BOOK_ID = "Zu5M4iiEJao"
def vid(vid_id, title, open_=False):
    return ('<details class="ad"%s><summary>🎬 Video: %s</summary>'
            '<div style="position:relative;padding-top:56.25%%;margin:8px 0;max-width:720px"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0&cc_load_policy=1" '
            'style="position:absolute;inset:0;width:100%%;height:100%%;border:0;border-radius:8px" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></div>'
            '<p class="hint">Subtitles: press CC. Speed: ⚙ → Playback speed → 0.75. <a href="https://www.youtube.com/watch?v=%s" target="_blank">Open on YouTube</a></p></details>') % (" open" if open_ else "", title, vid_id, vid_id)
def bookvideo(open_=False): return vid(BOOK_ID, "<i>Transferable skills</i> (Business Partner B1, 1.1.1)", open_)
SHORT_ID, EP_ID = "yN0VrXS41Gc", "FRFb_JMB5g0"
def vidx(vid_id, title, extra="", open_=False, ratio="16/9", maxw=720):
    return ('<details class="ad"%s><summary>🎬 %s</summary>'
            '<div style="width:100%%;max-width:%dpx;aspect-ratio:%s;margin:8px 0"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0&cc_load_policy=1%s" '
            'style="width:100%%;height:100%%;border:0;border-radius:12px;display:block" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></div>'
            '<p class="hint">Subtitles: CC. Speed: ⚙ → 0.75. <a href="https://www.youtube.com/watch?v=%s" target="_blank">Open on YouTube</a></p></details>') % (" open" if open_ else "", title, maxw, ratio, vid_id, extra, vid_id)
def shortbox():
    return ('<div style="width:100%%;max-width:300px;aspect-ratio:9/16;flex:0 0 auto"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0&cc_load_policy=1" '
            'style="width:100%%;height:100%%;border:0;border-radius:14px;display:block" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe>'
            '<p class="hint" style="margin-top:4px">Indeed · 2026 · under 1 min · CC = subtitles</p></div>') % SHORT_ID
def shortvideo(open_=False): return vidx(SHORT_ID, "Video: <i>Transferable Skills Employers Want (Even in a Tough Market)</i> · Indeed, 2026 · under 1 min", "", open_, "9/16", 300)
from indeed_words import CHAPTERS as EP_CH
def epvideo(open_=False):
    return (vidx(EP_ID, "Video 2: <i>How to Change Careers Using Transferable Skills You Already Have</i> · Indeed · Job Search Stories, 2026", "&start=64&enablejsapi=1", open_).replace("<iframe ", '<iframe id="yt" ', 1) +
            '<div class="chips" style="margin:-4px 0 8px">%s</div>' % "".join('<span style="cursor:pointer" onclick="jump(%d)">▶ %d:%02d %s</span>' % (t, t // 60, t % 60, n) for t, n in EP_CH))
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
      '<p class="ins"><b>B</b> Read (or listen to) the article. Were any of your ideas mentioned?</p><p class="hint">🏠 You read the article and watched the video before class – just compare your ideas now.</p>' + article() + shortvideo() + ta("r3b", "Yes, … was mentioned. / No, the article doesn’t mention …", 60))
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
s8 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">9</b>Work with your teacher.</p>'
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
def GUIDE(en, ua): return '<div class="card" style="background:#f4f6ff;border-left:4px solid #5b5fc7;margin:6px 0 14px"><b>🧭 What to do:</b> %s<br><span class="hint">%s</span></div>' % (en, ua)
F = {}
QS = [("conflict resolution", True), ("communication", True), ("coding", False), ("speed", False), ("perfect English", False), ("a university degree", False)]
for i, (w, a) in enumerate(QS): F["f1a_%d" % (i + 1)] = ["yes" if a else "no"]
OPT1B = ["It is not important if you change careers.", "It is still valuable, even in a difficult job market.", "AI can do it better now.", "Only your last job matters."]
def yn(k, w): return '<span style="display:inline-flex;align-items:center;gap:2px;margin:4px 8px 4px 0"><label style="display:inline-flex;gap:6px;align-items:center;border:1.5px solid #c8c9cb;border-radius:8px;padding:4px 10px;cursor:pointer"><input type="checkbox" class="yn" data-yn="%s"> %s</label><input class="g" data-k="%s" type="hidden" value="no">%s</span>' % (k, w, k, fb(k).replace("<div", "<span").replace("</div>", "</span>"))
WHYF = {}
BL = {"R": ("🔍 Remember", "#e8f1fb", "#2a5d9f"), "U": ("💭 Understand", "#eef7ee", "#2e7d4f"), "AP": ("✍️ Apply", "#fff4e6", "#b25e00"),
      "AN": ("🔎 Analyse", "#f3eefb", "#6a3fb0"), "E": ("⚖️ Evaluate", "#fdeef2", "#a8325e"), "C": ("🛠 Create", "#fff8d6", "#8a6d00")}
def bt(x):
    t, bg, c = BL[x]
    return '<span style="display:inline-block;background:%s;color:%s;border-radius:20px;padding:1px 10px;font-size:13px;font-weight:600;margin-right:6px;vertical-align:2px">%s</span>' % (bg, c, t)
def BQ(q):
    return ('<div style="background:#fff7ef;border:1.5px dashed #e8894a;border-radius:12px;padding:8px 14px;margin:4px 0 10px;font-size:15px">🧳 <b>Our big question:</b> '
            '<i>What is in your suitcase – and how will you show it to an international company?</i><br><span style="color:#c4642a">Today’s step:</span> %s</div>') % q
def think(k, q, ph="", model="", h=70):
    return ('<div class="card" style="margin-top:12px">%s</div>' % q) + ta(k, ph, h) + (mbtn("m_" + k, model, "Compare with a model answer") if model else "")
def recall(prefix, items):
    """items: [(phrase, meaning)] -> type the phrase from memory (auto-check)."""
    h = '<div class="hint" style="margin:4px 0 6px">Cover the cards above. Write the phrase from memory.</div>'
    for n, (ph, mean) in enumerate(items):
        k = "%s_%d" % (prefix, n + 1); F[k] = [ph, ph.replace(",", ""), ph.replace("’", "'")]
        h += '<div class="row">%d. <i>%s</i> → %s%s</div>' % (n + 1, mean, inp(k, 300, ph.split()[0][0] + "…"), fb(k))
    return h + ctl(prefix)
def useit(k, task, ph, need, h=80):
    return ('<div class="card" style="margin-top:12px">%s</div>' % task + ta(k, ph, h).replace("<textarea ", '<textarea data-need="%s" ' % "|".join(need)) +
            '<div class="need" data-for="%s"></div>' % k)

# ---- Step 1 · What are transferable skills? (concept first, then words, then video) ----
def guess_custom(prefix, items):
    h = ""
    for n, (en, mean, uk, ex, hint, d1, d2) in enumerate(items):
        k = "%s_%d" % (prefix, n + 1); F[k] = [mean]
        opts = [[mean, d1, d2], [d1, mean, d2], [d2, d1, mean]][n % 3]
        h += ('<div class="card" style="margin-top:10px"><b>“%s”</b> – what do you think it means? <span class="hint">Guess first!</span><div style="margin-top:6px">%s</div>'
              '<button class="btn l" style="margin-top:6px;font-size:13px;padding:3px 10px" onclick="this.nextElementSibling.style.display=\'block\';this.remove()">💡 Hint</button>'
              '<div class="hint" style="display:none;margin-top:4px">💡 %s</div>%s<div class="hint ans" style="display:none;margin-top:4px">🇺🇦 %s · e.g. <i>%s</i></div></div>') % (
              en, "".join('<label style="display:block;margin:3px 0;cursor:pointer"><input type="radio" name="%s" data-k="%s" value="%s"> %s</label>' % (k, k, o, o) for o in opts), hint, fb(k), uk, ex)
    return h + '<div class="ctl"><button class="btn" onclick="chkRad(\'%s\',WHYF);document.querySelectorAll(\'.ans\').forEach(a=>{if(a.closest(\'.card\').querySelector(\'input[data-k^=%s_]\'))a.style.display=\'block\'})">Check</button><span class="res" id="r_%s"></span></div>' % (prefix, prefix, prefix)
TS = [("communication", True), ("using your company’s own billing system", False), ("problem-solving", True), ("teamwork", True), ("the server passwords of your old company", False),
      ("time management", True), ("knowing where the coffee machine is in your office", False), ("conflict resolution", True)]
for i, (w, a) in enumerate(TS): F["f0a_%d" % (i + 1)] = ["yes" if a else "no"]
PRE = [("previous experience", "the jobs, projects and other things you did before", "попередній досвід", "Your previous experience is still valuable.", "previous = попередній", "a skill you learn at university", "the job you want next"),
       ("conflict resolution", "helping people agree when there is a problem between them", "вирішення конфліктів", "In a big team, conflict resolution is part of the job.", "conflict = конфлікт; resolve = вирішити", "a very fast internet connection", "a meeting about salaries"),
       ("a tough job market", "a time when it is hard to find a job", "складний ринок праці", "In a tough job market, your network matters.", "tough = важкий, жорсткий", "a market where you buy computers", "a job with a lot of physical work"),
       ("the AI boom", "the time when AI is growing very fast", "бум штучного інтелекту", "Many companies are hiring AI engineers during the AI boom.", "boom = різке зростання (як вибух)", "a loud noise from a computer", "an AI tool that stopped working")]
f0 = ('<div class="bsec">Before class <span class="sub">Step 1 · What are transferable skills?</span></div>' +
      GUIDE("Start here. First understand the key idea of the lesson, then learn 4 words you will hear in the video. Read, think, guess – then check. Write your answers in full sentences: your teacher reads them before the lesson.", "Почни тут: спочатку головна ідея, потім 4 слова з відео. Пиши відповіді реченнями – викладачка їх прочитає до уроку.") +
      BQ("What are transferable skills? Which ones do <b>you</b> have?") +
      '<div style="display:flex;gap:18px;flex-wrap:wrap;align-items:center;background:#fff7ef;border:1.5px solid #f5d2b5;border-radius:14px;padding:16px 18px;margin:6px 0 16px">'
      '<div style="font-size:54px;line-height:1">🧳</div><div style="flex:1;min-width:240px"><b style="font-size:19px">Transferable skills</b> are skills you can <b>take with you</b> from one job to another – like things in a suitcase.<br>'
      'You change your job, your company or even your profession – but these skills come with you.<br><span class="hint">🇺🇦 навички, які «переїжджають» з тобою з роботи на роботу</span></div></div>' +
      '<p class="ins"><b class="x">1</b><b>A</b> %sCan you take it to another job? Tick (✓) the <b>transferable</b> skills.</p>' % bt("U") +
      '<div>%s</div>' % "".join(yn("f0a_%d" % (i + 1), w) for i, (w, a) in enumerate(TS)) + ctl("f0a") +
      think("f0a_why", bt("AN") + "Why is <i>“using your company’s own billing system”</i> <b>not</b> transferable – but <i>“problem-solving”</i> is? Write 1–2 sentences.",
            "It isn’t transferable because …", "You can only use that billing system in one company. Problem-solving works in any job, team or tool – you take it with you.") +
      '<p class="ins" style="margin-top:24px"><b>B</b> %sYou will hear these words in the video. Guess what they mean.</p>' % bt("U") + guess_custom("f0b", PRE) +
      '<p class="ins" style="margin-top:24px"><b>C</b> %sNow without the cards: write the words.</p>' % bt("R") +
      recall("f0r", [(e, m) for e, m, *_ in [PRE[i] for i in (2, 0, 3, 1)]]) +
      '<p class="ins" style="margin-top:24px"><b>D</b> %sThink about you. Name two transferable skills you have – and where you got them. Use <b>previous experience</b> or <b>conflict resolution</b> if you can.</p>' % bt("AP") +
      useit("f0c", "", "1 communication – I got it in my previous experience as …\n2 …", ["previous experience", "conflict resolution"]) +
      '<p class="hint">Now you’re ready for the video → Step 2.</p>')
f1 = ('<div class="bsec">Before class <span class="sub">Step 2 · A short clip</span></div>' + GUIDE("Watch a very short clip (under 1 minute). First tick, then explain in your own words. It’s a warm-up – don’t worry if you don’t understand every word.", "Короткий ролик: спочатку познач, потім поясни своїми словами.") +
      BQ("What do employers want – even in a tough job market?") +
      '<p class="ins"><b class="x">2</b><b>A</b> ' + bt("R") + 'Watch the clip. Which <b>two</b> qualities do employers want in every field – especially during the AI boom? Tick (✓) them.</p>' +
      '<div style="display:flex;gap:24px;flex-wrap:wrap;align-items:flex-start">' + shortbox() + '<div style="flex:1;min-width:260px">' +
      '<div>%s</div>' % "".join(yn("f1a_%d" % (i + 1), w) for i, (w, a) in enumerate(QS)) + ctl("f1a") +
      '<p class="ins" style="margin-top:22px"><b>B</b> %sWhat does the speaker say about your <b>previous experience</b>? Write it in your own words.</p>' % bt("U") +
      ta("f1b", "She says that …", 60) + mbtn("m_f1b", "Your previous experience is still valuable – even in a tough job market. You don’t start from zero.", "Compare with a model answer") + '</div></div>' +
      '<p class="ins" style="margin-top:24px"><b>C</b> %sThe full episode is called <i>“How to Change Careers Using Transferable Skills You Already Have”</i>. What do you expect to hear? Write <b>two</b> predictions.</p>' % bt("AN") +
      ta("f1c", "1 I think they will say that …\n2 Maybe they will give advice about …", 60) +
      '<p class="hint">Keep your predictions – in Step 3 you’ll check them.</p>')
VS = ["project management", "stakeholder management", "problem-solving", "communication", "teamwork and collaboration"]
VD = {"project management": "IT work is almost always organised as projects: building, rolling out or improving systems.",
      "stakeholder management": "find the groups of people involved, learn how each group communicates and meet their needs.",
      "problem-solving": "use technology to solve problems for customers or for teams inside the company.",
      "communication": "listen well and explain technical ideas in plain business language to other departments.",
      "teamwork and collaboration": "IT rarely works alone – projects involve several departments and customer groups."}
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
fv = ('<div class="bsec">Before class <span class="sub">Vocabulary: IT work</span></div>'
      '<p class="ins"><b class="x">2</b><b>A</b> Match the words and phrases about skills in IT with their meanings.</p>' +
      "".join('<div class="row"><b style="display:inline-block;min-width:220px;font-weight:500">%s</b>%s%s</div>' % (w, sel("v2a_%d" % (i + 1), sorted(d for _, d in M2), 470), fb("v2a_%d" % (i + 1))) for i, (w, d) in enumerate(M2)) + ctl("v2a") +
      '<p class="ins" style="margin-top:26px"><b>B</b> Complete the collocations about IT work with the verbs in the box.</p>'
      '<div class="box">%s</div>' % " · ".join(sorted(a for _, a in C2)) +
      "".join('<div class="row">%d. %s%s</div>' % (i + 1, q.replace("___", inp("v2b_%d" % (i + 1), 120)), fb("v2b_%d" % (i + 1))) for i, (q, a) in enumerate(C2)) + ctl("v2b") +
      '<p class="ins" style="margin-top:26px"><b>C</b> Complete the word families.</p>' + tbl2() + ctl("v2c") +
      '<p class="ins" style="margin-top:26px"><b>D</b> Make it personal. Complete the sentences about you. Use words from A–C.</p>' +
      "".join('<div class="row">%d. %s<br>%s</div>' % (i + 1, q, ta("v2d_%d" % (i + 1), ph, 46)) for i, (q, ph) in enumerate(F2D)))
f2 = ('<div class="bsec">Before class <span class="sub">Step 8 · Reading</span></div>' + GUIDE("Read the article for our lesson (or listen with 🔊). Answer the questions – use <b>Show answer</b> to check yourself.", "Прочитай статтю до уроку й відповідай на питання.") + BQ("Which skills survive AI – and do you have them?") + '<p class="ins"><b class="x">8</b>Read (or listen to) the article. Then answer the questions. Words in <b>bold</b> are the key vocabulary of the lesson.</p>' + article() +
      "".join('<p class="ins"><span class="q">%d</span>%s</p>%s%s' % (i + 1, q, ta("f2_%d" % (i + 1), "", 60), mbtn("mf2_%d" % (i + 1), A4[i], "Show answer")) for i, q in enumerate(Q4)) +
      '<p class="ins"><span class="q">4</span>Which skills are mentioned in <b>both</b> the video and the article?</p>' + ta("f2_4", "", 50) +
      mbtn("mf2_4", "problem-solving, communication (skills), teamwork / being a team player") +
      think("f2_5", bt("E") + "5. The video and the article both give advice. Which piece of advice is the most useful for <b>you</b> right now – and which one would you ignore? Why?", "The most useful advice for me is … I would ignore … because …"))
ALLPH = ["transferable skills", "previous experience", "audit your experience", "with fresh eyes", "AI-proof", "bridge the gap", "industry-specific terms", "connect the dots",
         "think in verbs, not titles", "side hustle", "skill gap", "every experience counts", "signal initiative", "industry-recognised credentials", "through line", "critical thinking", "team player", "can-do attitude"]
f3 = ('<div class="bsec">Before class <span class="sub">Step 9 · My suitcase: get ready to speak</span></div>' +
      GUIDE("Last step: put everything together. Look at your own answers from Steps 1–7, then write your story. In class you will <b>tell</b> it – not read it. Then press <b>Send to my teacher</b>.", "Останній крок: збери все разом. Подивись на свої відповіді, напиши свою історію – на уроці ти її розкажеш. Потім «Send to my teacher».") +
      BQ("Your answer to the big question.") +
      '<p class="ins"><b class="x">9</b><b>A</b> %sYour notes so far – everything you wrote in Steps 1–7:</p>' % bt("R") +
      '<div id="suitcase" class="card" style="font-size:15.5px;background:#fffaf4;white-space:pre-wrap">…</div>' +
      '<p class="ins" style="margin-top:24px"><b>B</b> %sWrite your <b>60-second story</b> for an interview at an international company (80–120 words): who you are, 3 transferable skills with real examples, your skill gap and how you’re bridging it. Use at least <b>6</b> phrases from the lesson.</p>' % bt("C") +
      useit("f3_1", "", "I’m a … with … years of previous experience in … When I audit my experience with fresh eyes, …", ALLPH, 170) + '<div class="res" id="wc9"></div>' +
      think("f3_2", bt("E") + "<b>C</b> Read your story again. What is the strongest sentence? Which sentence is still weak – and why?", "My strongest sentence is … The weak one is …") +
      think("f3_3", "<b>D</b> Two questions you want to ask your teacher in class (about the words, the video or your story).", "1 …\n2 …") +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you talk about your transferable skills now?"))
VOC_F = [("Step 1 + clip + Part A", ["transferable skills", "previous experience", "conflict resolution", "a tough job market", "the AI boom", "audit your experience", "with fresh eyes", "AI-proof skills", "bridge the gap", "industry-specific terms", "connect the dots"]),
         ("Parts B + C", ["side hustle", "think in verbs, not titles", "comfort with new tools", "skill gap", "every experience counts", "go back to square one", "industry-recognised credentials", "low cost to no cost", "signal initiative", "a day in the life"]),
         ("★ Part D", ["through line", "reframe longevity as loyalty", "industry disruptions", "lead by example", "own it and articulate it"]),
         ("From the article", ["think outside the box", "set goals", "flexibility", "critical thinking", "team player", "integrity", "a can-do attitude", "determination", "old news", "tech stack"])]

# ================= GUIDED LISTENING (flipped classroom) =================
from indeed_words import WORDS as IW
IWD = {w[0]: w for w in IW}
def GUIDE(en, ua): return '<div class="card" style="background:#f4f6ff;border-left:4px solid #5b5fc7;margin:6px 0 14px"><b>🧭 What to do:</b> %s<br><span class="hint">%s</span></div>' % (en, ua)
def clip(a, b, label):
    return ('<div style="width:100%%;max-width:640px;aspect-ratio:16/9;margin:8px 0"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0&cc_load_policy=1&start=%d&end=%d" '
            'style="width:100%%;height:100%%;border:0;border-radius:12px;display:block" allow="encrypted-media; picture-in-picture" allowfullscreen loading="lazy"></iframe></div>'
            '<p class="hint">▶ %s · plays %d:%02d–%d:%02d and stops · CC = subtitles · ⚙ = speed 0.75</p>') % (EP_ID, a, b, label, a // 60, a % 60, b // 60, b % 60)
HINT = {"audit your experience": "audit = перевірка (як аудит у бухгалтерії). Що ти перевіряєш?", "with fresh eyes": "fresh = свіжий. Як ти бачиш річ, коли дивишся «свіжими очима»?",
 "AI-proof skills": "waterproof = не пропускає воду. Тоді AI-proof = …?", "bridge the gap": "bridge = міст, gap = проміжок. Що робить міст?", "industry-specific terms": "specific = особливий для чогось; terms = слова, терміни.",
 "connect the dots": "Дитяча гра: з’єднай крапки – і з’явиться малюнок.", "narrate it with intention": "narrate = розповідати; intention = намір, мета.",
 "side hustle": "side = збоку, поруч з основною роботою.", "think in verbs, not titles": "verbs = дієслова (built, led); titles = назви посад.", "comfort with new tools": "comfortable = зручно, спокійно.",
 "skill gap": "gap = прогалина. Чого бракує?", "every experience counts": "count = рахуватися, мати значення.", "go back to square one": "square one = перша клітинка в настільній грі.",
 "industry-recognised credentials": "credentials = документи, що підтверджують кваліфікацію.", "low cost to no cost": "no cost = 0 грн.", "carry real weight": "weight = вага. Що «важить» для рекрутера?",
 "signal initiative": "signal = подавати сигнал; initiative = ініціатива.", "more common than you think": "common = поширений.", "a day in the life": "Формат відео на YouTube: «мій робочий день».",
 "through line": "through = крізь; line = лінія. Що проходить крізь усю кар’єру?", "reframe longevity as loyalty": "longevity = довгий час; loyalty = вірність.", "industry disruptions": "disrupt = зламати, перервати.",
 "lead by example": "example = приклад. Як лідер веде команду?", "own it and articulate it": "own = володіти, визнати своїм; articulate = чітко сказати.", "never too late": "late = пізно.", "go after it": "go after = іти за чимось, переслідувати.", "tough job market": "tough = важкий, жорсткий."}
def guess_cards(prefix, phrases):
    h = ""
    for n, ph in enumerate(phrases):
        w = IWD[ph]; k = "%s_%d" % (prefix, n + 1); F[k] = [w[3]]
        others = [x[3] for x in IW if x[0] != ph]
        opts = [w[3], others[(n * 7 + 3) % len(others)], others[(n * 11 + 5) % len(others)]]
        opts = [opts[(n + j) % 3] for j in range(3)]
        h += ('<div class="card" style="margin-top:10px"><b>“%s”</b> – what do you think it means? <span class="hint">Guess first!</span><div style="margin-top:6px">%s</div>'
              '<button class="btn l" style="margin-top:6px;font-size:13px;padding:3px 10px" onclick="this.nextElementSibling.style.display=\'block\';this.remove()">💡 Hint</button>'
              '<div class="hint" style="display:none;margin-top:4px">💡 %s</div>%s'
              '<div class="hint ans" style="display:none;margin-top:4px">🇺🇦 %s · e.g. <i>%s</i></div></div>') % (
              ph, "".join('<label style="display:block;margin:3px 0;cursor:pointer"><input type="radio" name="%s" data-k="%s" value="%s"> %s</label>' % (k, k, o, o) for o in opts), HINT.get(ph, ""), fb(k), w[2], w[4])
    return h + '<div class="ctl"><button class="btn" onclick="chkRad(\'%s\',WHYF);document.querySelectorAll(\'.ans\').forEach(a=>{if(a.closest(\'.card\').querySelector(\'input[data-k^=%s]\'))a.style.display=\'block\'})">Check</button><span class="res" id="r_%s"></span></div>' % (prefix, prefix, prefix)
def mcq(k, q, opts, ans, why=""):
    F[k] = [ans]
    if why: WHYF[k] = why
    return ('<div class="card" style="margin-top:10px">%s<div style="margin-top:6px">%s</div>%s</div>' % (q, "".join('<label style="display:block;margin:3px 0;cursor:pointer"><input type="radio" name="%s" data-k="%s" value="%s"> %s</label>' % (k, k, o, o) for o in opts), fb(k)))
def chk(prefix): return '<div class="ctl"><button class="btn" onclick="chkRad(\'%s\',WHYF)">Check</button><span class="res" id="r_%s"></span></div>' % (prefix, prefix)

g2 = ('<div class="bsec">Before class <span class="sub">Step 3 · The whole episode</span></div>' +
      GUIDE("Now watch the <b>whole episode once</b> (about 11 minutes), from the start. Don’t stop and don’t look up words – just follow the main ideas. Then answer three questions.", "Подивись усе відео один раз, без зупинок і словника – лише головні ідеї. Потім 3 питання.") +
      BQ("What is the main message of the episode?") +
      epvideo(True).replace("&start=64", "&start=0") +
      mcq("g2_1", bt("R") + "1. Who is the advice for?", ["Only university students", "Only managers with 20 years of experience", "Job seekers of any age – from Gen Z to people with long careers"], "Job seekers of any age – from Gen Z to people with long careers") +
      mcq("g2_2", "2. Which topic is in the episode?", ["Getting certificates without a degree", "Negotiating your salary", "Working remotely from another country"], "Getting certificates without a degree") + chk("g2") +
      think("g2_pred", bt("AN") + "3. Look at your predictions from Step 2. Which one was right? What surprised you?", "My prediction about … was right. I was surprised that …") +
      think("g2_slack", bt("U") + "4. A colleague asks in Slack: <i>“Is this video worth watching? What’s it about?”</i> Answer in 2–3 sentences.",
            "Yes! It’s about …", "Yes, it’s worth it! It’s about how to change careers with the skills you already have. They explain how to audit your experience, describe it in industry terms and get certificates without a degree.") +
      '<p class="hint">Next: we’ll listen to the episode in small parts and work with the key phrases.</p>')
def M(ph): return IWD[ph][3]
def part(lbl, title, bq, guide_en, guide_ua, a, b_, opens, phrases, uses, evalq, adv=False):
    pre = lbl.lower()
    h = '<div class="bsec">Before class <span class="sub">%s</span></div>' % title
    if adv: h += '<div class="card" style="border-left:4px solid #e0a100;background:#fffaf0"><b style="color:#b26b00">★ Advanced option</b> – do this part if you have time and energy. It’s harder, but very useful for interviews.</div>'
    h += GUIDE(guide_en, guide_ua) + BQ(bq) + clip(a, b_, "Part " + lbl)
    h += '<p class="ins" style="margin-top:18px"><b>1</b> %sListen and answer in your own words. Then compare with the model answer.</p>' % bt("U")
    for i, (q, ph_, model) in enumerate(opens): h += think("g%so_%d" % (lbl, i + 1), q, ph_, model, 55)
    h += '<p class="ins" style="margin-top:24px"><b>2</b> %sThe key phrases from Part %s. Guess the meaning first – 💡 Hint only if you need it.</p>' % (bt("U"), lbl) + guess_cards("g" + lbl, phrases)
    h += '<p class="ins" style="margin-top:24px"><b>3</b> %sNow from memory.</p>' % bt("R") + recall("g%sr" % lbl, [(ph, M(ph)) for ph in phrases[::-1][:4]])
    h += '<p class="ins" style="margin-top:24px"><b>4</b> %sUse the phrases about <b>you</b>. The phrases turn green when you use them.</p>' % bt("AP")
    for i, (task, ph_, need) in enumerate(uses): h += useit("g%su_%d" % (lbl, i + 1), task, ph_, need)
    if evalq:
        q, ph_, model = evalq
        h += '<p class="ins" style="margin-top:24px"><b>5</b> %sWhat do you think?</p>' % bt("E") + think("g%st" % lbl, q, ph_, model, 70)
    return h

gA = part("A", "Step 4 · Part A: audit your skills", "How can you see your experience <b>with fresh eyes</b>?",
  "Listen to <b>Part A only</b> (1:04–2:50) – the player starts and stops there. Then go step by step: <b>1</b> answer → <b>2</b> guess the phrases → <b>3</b> write them from memory → <b>4</b> use them about you → <b>5</b> your opinion.",
  "Слухай лише частину A. Далі по кроках: відповідь → вгадай фрази → напиши з пам’яті → використай про себе → твоя думка.", 64, 170,
  [("a) The guest used to be a school teacher. How does she describe her old job in <b>new words</b>?", "She says that she …", "She says she designed programmes, developed tracking tools and educated people – she translates her experience into industry-specific terms."),
   ("b) Which skill do they mention that employers want and AI can’t replace?", "", "Communication – it’s an AI-proof skill.")],
  ["audit your experience", "with fresh eyes", "AI-proof skills", "bridge the gap", "industry-specific terms", "connect the dots"],
  [("a) Audit your experience <b>with fresh eyes</b>. Take one thing from your past (a job, studies, a hobby) and describe it in <b>industry-specific terms</b> for an IT company.", "When I audit my experience with fresh eyes, I see that …", ["audit your experience", "with fresh eyes", "industry-specific terms"]),
   ("b) What is the <b>gap</b> between your experience now and a job in an international company? How will you <b>bridge the gap</b>?", "The biggest gap is … I’m going to bridge the gap by …", ["bridge the gap"])],
  ("They say communication is an <b>AI-proof skill</b>. Do you agree? Name one more skill you think is AI-proof – and one that is <b>not</b>. Explain why.", "I agree / don’t agree, because … Another AI-proof skill is … because …",
   "e.g. I agree – AI can write a message, but it can’t build trust in a team. Another AI-proof skill is conflict resolution. Writing simple boilerplate code is not AI-proof any more."))
gB = part("B", "Step 5 · Part B: first-time job seekers", "What counts as experience – if it wasn’t a paid job?",
  "Listen to <b>Part B</b> (2:50–4:34). It’s about young people with little work experience – but the advice works for everyone. Then the same 5 steps.",
  "Частина B: поради для тих, хто шукає першу роботу. Ті самі 5 кроків.", 170, 274,
  [("a) Which experiences, besides paid jobs, can build useful skills? Name at least three.", "", "Caregiving, volunteering, freelance work, side hustles, student organisations."),
   ("b) How should you describe these experiences – with job titles or with verbs? Give one example.", "", "With action verbs: organise, coach, communicate, build. e.g. “I organised a team of 10 volunteers.”")],
  ["side hustle", "think in verbs, not titles", "comfort with new tools", "skill gap", "every experience counts"],
  [("a) <b>Think in verbs, not titles.</b> Write your job title – then turn it into three action verbs about what you really do.", "My title: … → I build …, I explain …, I …", ["think in verbs, not titles"]),
   ("b) Do you have a <b>side hustle</b>, volunteering or a hobby project? What skill did it give you? (No? Which side hustle could help you in IT?)", "My side hustle is … It gave me …", ["side hustle", "every experience counts"])],
  ("“<b>Every experience counts.</b>” Is this always true when you apply to an international IT company? When is it <b>not</b> true?", "I think it’s true when … but not when …",
   "e.g. It’s true if you can show a skill and a result. It’s not true if the experience has nothing to do with the role and you can’t connect the dots for the recruiter."))
gC = part("C", "Step 6 · Part C: certificates", "How can you <b>prove</b> your skills without a new degree?",
  "Listen to <b>Part C</b> (4:34–7:05) about getting certified without a degree. Then the same 5 steps.", "Частина C: сертифікати без диплома. Ті самі 5 кроків.", 274, 425,
  [("a) What do they say about many online certificates – the price and what they show employers?", "", "Many are free or low-cost, and they signal initiative – that you learn on your own."),
   ("b) What should you do <b>before</b> you choose a new role?", "", "Research the role, e.g. watch “a day in the life” videos.")],
  ["go back to square one", "industry-recognised credentials", "low cost to no cost", "signal initiative", "a day in the life"],
  [("a) Which <b>industry-recognised credential</b> could <b>signal initiative</b> for the job you want? (e.g. AWS, Scrum, Google PM, ISTQB…) Why this one?", "For my next role, … would signal initiative because …", ["industry-recognised credentials", "signal initiative"]),
   ("b) Find a <b>“day in the life”</b> video of the role you want in an international company. Paste the link and write two things you learned.", "Link: …\n1 …\n2 …", ["a day in the life"])],
  ("A certificate or a real project on GitHub – what carries more real weight for a recruiter? Why?", "I think … carries more weight, because …", ""))
gD = part("D", "Step 7 · ★ Part D: tell your story", "How do you turn your whole career into <b>one strong story</b>?",
  "Listen to <b>Part D</b> (7:05–9:56): how to present a long career. Then the steps.", "Частина D (за бажанням): як подати довгу кар’єру.", 425, 596,
  [("a) Which sentence is stronger, and why? <i>“I’ve been in this field for 20 years.”</i> or <i>“I’ve built and led teams through two industry disruptions.”</i>", "", "The second – it shows actions and results, not just years.")],
  ["through line", "reframe longevity as loyalty", "industry disruptions", "lead by example", "own it and articulate it"],
  [("What is the <b>through line</b> of your career? One sentence that connects all your jobs.", "The through line of my career is …", ["through line"]),
   ("Rewrite a weak sentence about you into a strong one (actions + results), like in the video.", "Weak: I have worked in IT for … years.\nStrong: I’ve …", ["industry disruptions", "lead by example"])], None, adv=True)
for _k in [k for k in F if k.startswith("v2")]: del F[_k]
NEEDJS = r"""function needUpd(t){const box=document.querySelector('.need[data-for="'+t.dataset.k+'"]');if(!box)return;const P=x=>x.toLowerCase().replace(/[’']/g,"'").replace(/,/g,'').replace(/\b(your|my|his|her|our|their)\b/g,'·').replace(/\s+/g,' ');const v=P(t.value||'');const ws=t.dataset.need.split('|');let n=0;
box.innerHTML=ws.map(w=>{const core=P(w).replace(/^(a|the) /,'');const ok=v.includes(core);if(ok)n++;return '<span style="display:inline-block;margin:3px 6px 0 0;padding:1px 9px;border-radius:12px;font-size:13px;border:1.5px solid '+(ok?'#3a9d5d;background:#eaf7ee;color:#1e6b3d':'#d0d1d3;color:#77787b')+'">'+(ok?'✓ ':'')+w+'</span>'}).join('')+(ws.length>3?' <b style="font-size:13px;color:#1e6b3d">'+n+' used</b>':'')}
function suit(){const el=document.getElementById('suitcase');if(!el)return;const L=[['f0c','Step 1 · My transferable skills'],['f0a_why','Step 1 · Why transferable'],['gAu_1','Part A · My experience with fresh eyes'],['gAu_2','Part A · My gap'],['gAt','Part A · AI-proof skills'],['gBu_1','Part B · Verbs, not titles'],['gBu_2','Part B · Side hustle'],['gBt','Part B · Every experience counts?'],['gCu_1','Part C · A credential for me'],['gCu_2','Part C · A day in the life'],['gDu_1','★ My through line'],['gDu_2','★ My strong sentence'],['f2_5','Step 8 · Most useful advice']];
let o='';L.forEach(([k,t])=>{const x=document.querySelector('[data-k="'+k+'"]');if(x&&x.value.trim())o+='<b>'+t+':</b> '+x.value.trim().replace(/</g,'&lt;')+'\n\n'});el.innerHTML=o||'<span class="hint">Your answers from Steps 1–7 will appear here. Go back and write them first 🙂</span>'}
function wc9(){const t=document.querySelector('[data-k="f3_1"]');if(!t)return;const n=(t.value.match(/\S+/g)||[]).length;document.getElementById('wc9').textContent=n+' words (80–120)'+(n>=80&&n<=120?' ✓':'')}
document.querySelectorAll('textarea[data-need]').forEach(t=>{t.addEventListener('input',()=>{needUpd(t);if(t.dataset.k==='f3_1')wc9()});needUpd(t)});
document.querySelectorAll('nav button').forEach(b=>b.addEventListener('click',()=>setTimeout(suit,30)));
const _af2=window.afterFill;window.afterFill=()=>{_af2&&_af2();document.querySelectorAll('textarea[data-need]').forEach(needUpd);suit();wc9()};
"""
html = page("1.1", "Transferable skills", "BEFORE CLASS", "Watch, read and prepare at home – class time is for speaking.", "BP B1 1.1 Transferable skills · Before class", CODE,
            [("1", f0), ("2", f1), ("3", g2), ("4", gA), ("5", gB), ("6", gC), ("7", gD), ("8", f2), ("9", f3)], F, VOC_F, extra_js=("const WHYF=%s;\n" % json.dumps(WHYF, ensure_ascii=False)) + "document.querySelectorAll('.yn').forEach(c=>{const h=document.querySelector(`.g[data-k='${c.dataset.yn}']`);c.onchange=()=>{h.value=c.checked?'yes':'no';later()}});const _af=window.afterFill;window.afterFill=()=>{document.querySelectorAll('.yn').forEach(c=>{c.checked=document.querySelector(`.g[data-k='${c.dataset.yn}']`).value==='yes'});_af&&_af()};\n" + NEEDJS + 'function jump(t){const f=document.getElementById("yt");if(!f)return;const d=f.closest("details");if(d)d.open=true;f.src=f.src.replace(/([?&])start=\\d+/,"$1start="+t)+"&autoplay=1";f.scrollIntoView({behavior:"smooth",block:"center"})}\n' + XJS.split("const T1=")[0].replace("__ART__", json.dumps(ART_PLAIN, ensure_ascii=False)))
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
