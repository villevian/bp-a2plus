"""Business Partner B1 · 1.1 — HOMEWORK: Video words (Indeed · Job Search Stories).
Bloom ladder for vocabulary (meaning first → retrieval → controlled use → analysis → evaluation → creation), IT contexts.
Usage: python3 build_b1_1-1_words.py OUTDIR [STUDENT_CODE] -> OUTDIR/words.html
"""
import sys, os, json
from bp_page import page, fb, sel, inp, ta, ctl, SELF, tagged
from indeed_words import CORE, REC, ADVW, VIDEO_ID, VIDEO_TITLE, CHAPTERS
OUTDIR = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
os.makedirs(OUTDIR, exist_ok=True)
K, WHY = {}, {}
ADV = lambda title, body: '<div class="card" style="border-left:4px solid #e0a100;background:#fffaf0;margin-top:22px"><b style="color:#b26b00">★ Advanced option</b> · %s<div style="margin-top:6px">%s</div></div>' % (title, body)
STAGE = lambda n, name, ua: '<div style="display:inline-block;background:#eef0fb;color:#4044a8;border-radius:20px;padding:3px 12px;font-size:13px;font-weight:600;margin-bottom:6px">Step %d · %s <span style="font-weight:400;color:#6d6e70">· %s</span></div>' % (n, name, ua)
def mix(lst, order): return [lst[i] for i in order]
def tf_rows(prefix, items):
    h = ""
    for i, (q, a, w) in enumerate(items):
        k = "%s_%d" % (prefix, i + 1); K[k] = [a]
        if w: WHY[k] = w
        h += ('<div class="tf"><span class="q">%d. %s</span><label><input type="radio" name="%s" data-k="%s" value="A"> agree</label>'
              '<label><input type="radio" name="%s" data-k="%s" value="D"> disagree</label>%s</div>') % (i + 1, q, k, k, k, k, fb(k))
    return h
def radio_q(k, q, opts, ans):
    K[k] = [ans]
    return ('<div class="card" style="margin-top:10px">%s<div style="margin-top:6px">' % q +
            "".join('<label style="display:block;margin:4px 0;cursor:pointer"><input type="radio" name="%s" data-k="%s" value="%s"> %s</label>' % (k, k, o, o) for o in opts) +
            "</div>%s</div>" % fb(k))

player = ('<div style="position:relative;padding-top:56.25%%;max-width:720px;margin:8px 0"><iframe id="yt" src="https://www.youtube-nocookie.com/embed/%s?rel=0&cc_load_policy=1&start=64&enablejsapi=1" '
          'style="position:absolute;inset:0;width:100%%;height:100%%;border:0;border-radius:10px" allow="encrypted-media; picture-in-picture" allowfullscreen></iframe></div>'
          '<div class="chips" style="margin-bottom:6px">%s</div><p class="hint">Indeed · <i>%s</i> (2026). Subtitles: CC · Speed: ⚙ → 0.75.</p>') % (
          VIDEO_ID, "".join('<span style="cursor:pointer" onclick="jump(%d)">▶ %d:%02d %s</span>' % (t, t // 60, t % 60, n) for t, n in CHAPTERS), VIDEO_TITLE)

# ---------- Step 1 · REMEMBER: notice the chunks while listening (retrieval with first-letter hint) ----------
GAPS = [("audit your ___", "experience"), ("look at it with fresh ___", "eyes"), ("___-proof skills", "AI"), ("bridge the ___", "gap"), ("industry-specific ___", "terms"),
        ("connect the ___", "dots"), ("a skill ___", "gap"), ("think in ___, not titles", "verbs"), ("comfort with new ___", "tools"), ("a side ___", "hustle"),
        ("every experience ___", "counts"), ("signal ___", "initiative"), ("a day in the ___", "life")]
for i, (q, a) in enumerate(GAPS): K["w1_%d" % (i + 1)] = [a]
s1 = (STAGE(1, "Remember", "помітити й пригадати") + '<p class="ins"><b class="x">1</b>Watch the video again from <b>1:04 to 4:34</b>. Complete the phrases you hear. The first letter helps you.</p>' + player +
      '<div class="two"><div>%s</div><div>%s</div></div>' % tuple("".join('<div class="row">%d. %s%s</div>' % (i + 1, q.replace("___", inp("w1_%d" % (i + 1), 120, a[0] + "…")), fb("w1_%d" % (i + 1)))
                                                              for i, (q, a) in list(enumerate(GAPS))[sl]) for sl in (slice(0, 7), slice(7, 13))) + ctl("w1"))

# ---------- Step 2 · UNDERSTAND: meaning (match) + concept-check situations ----------
ORD = (6, 2, 10, 0, 8, 4, 12, 1, 9, 3, 11, 5, 7)
C2 = mix(CORE, ORD)
for i, w in enumerate(C2): K["w2_%d" % (i + 1)] = [w[3]]
SIT = [("Andrii worked in hotel management. Now he explains that ‘handling guest complaints’ = ‘customer support and conflict resolution’.", ["He bridges the gap with industry-specific terms.", "He goes back to square one.", "He has a side hustle."], "He bridges the gap with industry-specific terms."),
       ("Olha re-reads her CV after a two-week break and suddenly sees five weak lines.", ["She looks at it with fresh eyes.", "She signals initiative.", "She connects the dots."], "She looks at it with fresh eyes."),
       ("In the interview, Max explains how support, then QA, then automation all led him to this DevOps role.", ["He connects the dots.", "He has a skill gap.", "He watches a day in the life."], "He connects the dots."),
       ("Before applying, Ira lists all her projects, freelance tasks and volunteering, and writes the skills each one gave her.", ["She audits her experience.", "She leads by example.", "She goes after it."], "She audits her experience."),
       ("Taras doesn’t know Kubernetes yet, but the job needs it.", ["That’s his skill gap.", "That’s his side hustle.", "That’s an AI-proof skill."], "That’s his skill gap.")]
s2 = (STAGE(2, "Understand", "зрозуміти значення") + '<p class="ins"><b class="x">2</b><b>A</b> Match the phrases with their meanings.</p>' +
      "".join('<div class="row"><b style="display:inline-block;min-width:230px;font-weight:500">%s</b>%s%s</div>' % (w[0], sel("w2_%d" % (i + 1), sorted(x[3] for x in CORE), 520), fb("w2_%d" % (i + 1))) for i, w in enumerate(C2)) + ctl("w2") +
      '<p class="ins" style="margin-top:26px"><b>B</b> Read the situations. Choose the best description.</p>' +
      "".join(radio_q("w2b_%d" % (i + 1), "%d. %s" % (i + 1, q), o, a) for i, (q, o, a) in enumerate(SIT)) +
      '<div class="ctl"><button class="btn" onclick="chkRad(\'w2b\',WHY)">Check</button><span class="res" id="r_w2b"></span></div>')

# ---------- Step 3 · UNDERSTAND (receptive): phrases to recognise when listening ----------
R3 = mix(REC, (4, 0, 6, 2, 7, 1, 5, 3))
for i, w in enumerate(R3): K["w3_%d" % (i + 1)] = [w[3]]
s3 = (STAGE(3, "Understand", "впізнавати на слух") + '<p class="ins"><b class="x">3</b>You will <b>hear</b> these phrases in the video – you don’t need to use them yet. Match them with their meanings.</p>' +
      "".join('<div class="row"><b style="display:inline-block;min-width:260px;font-weight:500">%s</b>%s%s</div>' % (w[0], sel("w3_%d" % (i + 1), sorted(x[3] for x in REC), 440), fb("w3_%d" % (i + 1))) for i, w in enumerate(R3)) + ctl("w3"))

# ---------- Step 4 · APPLY: controlled use in IT messages ----------
MSG = [("Slack · #career-growth", "Mira", "Before my performance review, I want to ___ – all my projects from this year, not just the big ones.", ["audit my experience"]),
       ("Slack · DM", "Dan", "Honestly, my ___ is system design. I’m reading one chapter a week to close it.", ["skill gap"]),
       ("LinkedIn post", "Olena", "I built a small budgeting app as a ___ – and it got me my first junior role!", ["side hustle"]),
       ("Interview notes", "Recruiter", "Strong candidate: she can ___ between her customer-support years and the QA role.", ["connect the dots", "bridge the gap"]),
       ("Slack · #random", "Oleh", "AI writes boilerplate now, so I invest in ___ like communication and judgment.", ["AI-proof skills"]),
       ("CV tip", "Career coach", "Don’t write ‘Team Lead’ and stop. ___: led, built, reduced, launched.", ["think in verbs, not titles", "Think in verbs, not titles"]),
       ("Slack · #onboarding", "Tech lead", "Our stack changes fast, so ___ matters more than knowing one framework.", ["comfort with new tools"]),
       ("LinkedIn comment", "Mentor", "Free Google and AWS courses can ___ – recruiters notice that you started on your own.", ["signal initiative"])]
for i, (_, _, _, a) in enumerate(MSG): K["w4_%d" % (i + 1)] = a
BOX4 = sorted(set(a[0] for _, _, _, a in MSG))
s4 = (STAGE(4, "Apply", "використати в контексті") + '<p class="ins"><b class="x">4</b>Complete the messages with phrases from the box. One phrase in each gap.</p>'
      '<div class="box">%s</div>' % " · ".join(BOX4) +
      "".join('<div class="slack" style="margin:8px 0"><b>%s</b><span class="t">%s</span><br>%s%s</div>' % (who, ch, t.replace("___", inp("w4_%d" % (i + 1), 230)), fb("w4_%d" % (i + 1))) for i, (ch, who, t, a) in enumerate(MSG)) + ctl("w4"))

# ---------- Step 5 · ANALYSE: titles → verbs; which strategy is it? ----------
CV = [("Senior Developer, FinPay (2022–2025)", ["Senior Developer at FinPay for three years.", "Led a team of 4 and cut payment errors by 30%.", "Responsible for development tasks."], "Led a team of 4 and cut payment errors by 30%."),
      ("QA Engineer", ["Was a QA engineer in a big company.", "Worked on testing.", "Built 120 automated tests and reduced release time from 2 days to 4 hours."], "Built 120 automated tests and reduced release time from 2 days to 4 hours."),
      ("Volunteer, IT Army of students", ["Organised weekly coding workshops for 30 students.", "Volunteer.", "Was a member of a student club."], "Organised weekly coding workshops for 30 students.")]
for i, (t, o, a) in enumerate(CV): K["w5_%d" % (i + 1)] = [a]
STR = ["audit your experience", "bridge the gap", "signal initiative", "connect the dots"]
SORT = [("She takes a free cloud certificate before anyone asks her to.", "signal initiative"),
        ("He writes a list of every project and the skills each one gave him.", "audit your experience"),
        ("He explains how his support job led naturally to his QA role.", "connect the dots"),
        ("She takes a short course to move from manual testing to automation.", "bridge the gap"),
        ("He reads his old freelance contracts again to find forgotten skills.", "audit your experience"),
        ("She shows the recruiter how her teaching skills match ‘onboarding’ and ‘documentation’.", "bridge the gap")]
for i, (q, a) in enumerate(SORT): K["w5b_%d" % (i + 1)] = [a]
s5 = (STAGE(5, "Analyse", "аналізувати") + '<p class="ins"><b class="x">5</b><b>A</b> <i>Think in verbs, not titles.</i> Which CV line follows this advice best?</p>' +
      "".join(radio_q("w5_%d" % (i + 1), "<b>%s</b>" % t, o, a) for i, (t, o, a) in enumerate(CV)) +
      '<div class="ctl"><button class="btn" onclick="chkRad(\'w5\',WHY)">Check</button><span class="res" id="r_w5"></span></div>' +
      '<p class="ins" style="margin-top:26px"><b>B</b> Which strategy from the video is each person using?</p>' +
      "".join('<div class="row">%d. %s %s%s</div>' % (i + 1, q, sel("w5b_%d" % (i + 1), STR, 210), fb("w5b_%d" % (i + 1))) for i, (q, a) in enumerate(SORT)) + ctl("w5b"))

# ---------- Step 6 · EVALUATE: compare answers, take a position ----------
ANS_A = "“I don’t have an IT degree, sorry. I only worked as a teacher, so I know it’s not ideal, but I learn fast.”"
ANS_B = "“For six years I designed training programmes and built tracking tools for 200 students. That’s onboarding and data work – and I bridged the gap with a QA certificate last spring.”"
K["w6a"] = ["B"]
WHY["w6a"] = "B audits the experience, uses industry-specific terms, thinks in verbs and signals initiative. A apologises for a non-linear path."
s6 = (STAGE(6, "Evaluate", "оцінити й аргументувати") + '<p class="ins"><b class="x">6</b><b>A</b> The interviewer asks: <i>“Why should we hire you without an IT background?”</i> Which answer follows the advice from the video better?</p>'
      '<div class="card"><b>A</b> %s</div><div class="card"><b>B</b> %s</div>' % (ANS_A, ANS_B) +
      '<div class="tf"><span class="q">The better answer is:</span><label><input type="radio" name="w6a" data-k="w6a" value="A"> A</label><label><input type="radio" name="w6a" data-k="w6a" value="B"> B</label>%s</div>' % fb("w6a") +
      '<div class="ctl"><button class="btn" onclick="chkRad(\'w6a\',WHY)">Check</button><span class="res" id="r_w6a"></span></div>'
      '<p class="ins">Now explain <b>why</b> – use at least two phrases from this homework.</p>' + ta("w6a_why", "Answer B is better because …", 70) +
      '<p class="ins" style="margin-top:24px"><b>B</b> Do you agree? Choose and give a reason from <b>your</b> experience in IT. There are no wrong answers – we’ll discuss them in class.</p>' +
      "".join('<div class="card">%d. %s<div style="margin-top:4px"><label><input type="radio" name="w6b_%d" data-k="w6b_%d" value="agree"> agree</label> &nbsp; <label><input type="radio" name="w6b_%d" data-k="w6b_%d" value="partly"> partly</label> &nbsp; <label><input type="radio" name="w6b_%d" data-k="w6b_%d" value="disagree"> disagree</label></div>%s</div>'
              % (i + 1, q, i + 1, i + 1, i + 1, i + 1, i + 1, i + 1, ta("w6b_%d_why" % (i + 1), "because …", 46)) for i, q in enumerate(
                  ["Every experience counts – even a side hustle or volunteering.", "Certificates carry real weight in IT in 2026.", "There are no truly AI-proof skills.", "Career changes into IT are more common than you think."])))

# ---------- Step 7 · CREATE: my skills audit ----------
CHIPS = [w[0] for w in CORE]
s7 = (STAGE(7, "Create", "створити власне") + '<p class="ins"><b class="x">7</b><b>My skills audit.</b> Audit your experience and write 90–120 words for the start of a job interview (<i>“Tell me about yourself”</i>). Use at least <b>six</b> phrases – they light up when you use them.</p>'
      '<div class="chips" id="chips7">%s</div>' % "".join('<span data-p="%s">%s</span>' % (c.lower(), c) for c in CHIPS) +
      ta("w7", "I’ve worked as … When I audit my experience with fresh eyes, I see …", 190) + '<div class="res" id="cnt7"></div>' +
      '<p class="ins" style="margin-top:18px">Then <b>say it aloud</b> in one minute, without reading. Record it on your phone if you can – we’ll start the next lesson with it.</p>'
      '<label style="cursor:pointer"><input type="checkbox" class="yn" data-yn="w7_said"> I said it aloud in one minute</label><input class="g" data-k="w7_said" type="hidden" value="no">' +
      ADV("Your through line (video 7:05–9:56)", '<p>Watch <b>7:05–9:56</b> (<span style="cursor:pointer;color:#4044a8" onclick="jump(425)">▶ jump</span>). Match the phrases, then write 3 sentences about the <i>through line</i> of your career.</p>' +
          "".join('<div class="row"><b style="display:inline-block;min-width:240px;font-weight:500">%s</b>%s%s</div>' % (w[0], sel("w8_%d" % (i + 1), sorted(x[3] for x in ADVW), 460), fb("w8_%d" % (i + 1))) for i, w in enumerate(mix(ADVW, (3, 0, 5, 1, 6, 2, 4)))) + ctl("w8") +
          ta("w8_story", "The through line of my career is … I’ve … I own it: …", 90)) +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well do you know the phrases from the video?"))
for i, w in enumerate(mix(ADVW, (3, 0, 5, 1, 6, 2, 4))): K["w8_%d" % (i + 1)] = [w[3]]

XJS = r"""const WHY=__WHY__;
function jump(t){const f=document.getElementById("yt")||document.querySelector("iframe");if(!f)return;f.src=f.src.replace(/([?&])start=\d+/,"$1start="+t).replace(/&autoplay=1/,"")+"&autoplay=1";f.scrollIntoView({behavior:"smooth",block:"center"})}
document.querySelectorAll('.yn').forEach(c=>{const h=document.querySelector(`.g[data-k='${c.dataset.yn}']`);c.onchange=()=>{h.value=c.checked?'yes':'no';later()}});
const T7=document.querySelector('[data-k=w7]');
function u7(){const v=(T7.value||"").toLowerCase().replace(/[’']/g,"'");let n=0;document.querySelectorAll('#chips7 span').forEach(s=>{const p=s.dataset.p.replace(/[’']/g,"'"),key=p.split(/[ ,]+/).filter(w=>w.length>3).slice(0,2);const hit=v.includes(p)||key.length&&key.every(k=>v.includes(k.replace(/s$/,"")));s.style.background=hit?"#e7f6ec":"";s.style.color=hit?"#23824a":"";if(hit)n++});
 const w=(T7.value.match(/\S+/g)||[]).length;document.getElementById("cnt7").textContent=w+" words (90–120) · "+n+" phrases used (6+)"+(w>=90&&w<=120&&n>=6?" ✓":"")}
T7.addEventListener("input",u7);window.afterFill=()=>{document.querySelectorAll('.yn').forEach(c=>c.checked=document.querySelector(`.g[data-k='${c.dataset.yn}']`).value==='yes');u7()};"""
VOC = [("Use these (active)", [w[0] for w in CORE]), ("Recognise these (listening)", [w[0] for w in REC]), ("★ Advanced", [w[0] for w in ADVW])]
html = tagged({'w1': 'vocabulary', 'w2': 'vocabulary', 'w2b': 'vocabulary', 'w3': 'vocabulary', 'w4': 'vocabulary', 'w5': 'vocabulary', 'w5b': 'vocabulary', 'w6a': 'vocabulary', 'w8': 'vocabulary'})("1.1", "Transferable skills", "HOMEWORK · VIDEO WORDS", "After the lesson: learn and use the key phrases from the Indeed video.", "BP B1 1.1 Transferable skills · Video words", CODE,
            [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5), ("6", s6), ("7", s7)], K, VOC, extra_js=XJS.replace("__WHY__", json.dumps(WHY, ensure_ascii=False)))
open(os.path.join(OUTDIR, "words.html"), "w").write(html)
print("ok", OUTDIR)
