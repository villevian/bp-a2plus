"""Business Partner A2 · 1.1 Daily tasks — IT version (designers, developers, project & product managers).
Structure mirrors the coursebook page: Lead-in 1A–B · Vocabulary 2A–B, 3 · Communicative grammar 4, 5 · VIDEO 6A–C · TASK 7A–B · Self-assessment.
Usage: python3 build_a2_lesson_1-1.py OUT.html
"""
import sys, json
OUT = sys.argv[1]
ACC, ACC2, DARK = "#3b7dd8", "#e3eefb", "#2a5fb0"

JOBS = ["Developer", "UX/UI Designer", "Project Manager", "Product Manager", "QA Engineer (tester)", "Data Analyst", "DevOps Engineer", "Recruiter (HR)"]
PHOTOS = [("A", "🎨🖥️", "A woman draws app screens in Figma on a big monitor.", 2),
          ("B", "💻⌨️", "A man writes code on his laptop. There are lines of code on the screen.", 1),
          ("C", "🗂️🟨", "A man stands at a board with sticky notes and tasks: To do · In progress · Done.", 3),
          ("D", "📊📈", "A woman looks at charts and numbers on a dashboard.", 6)]
LEAD_B = ["Which of the jobs in Exercise 1A do people do where you work?", "What is your job? Is it on the list?", "Which job do you think is the most interesting? Why?", "Which job is the most difficult? Why?"]
LEAD_B_UP = ["What is the difference between a Project Manager and a Product Manager?", "Who do you work with every day? What are their jobs?", "Which job do you want to try in the future? Why?", "Can AI do some of these jobs? Which ones?"]

T2A = ("I’m a(n) <span class='gap'>__SELA__</span>. I’m responsible for a team of five people: two developers, a designer, a tester and a data analyst. "
 "We often have meetings with users on Zoom. We sometimes work in the office and we <b>call customers</b> on video calls. "
 "At the end of the sprint, we <b>do research</b> to find new ideas for the app. I sometimes <b>go to meetings</b> with important clients, so I often <b>travel for work</b> to our office in Warsaw. "
 "I <b>analyse</b> app <b>data</b>, and I often <b>write reports</b>. I usually <b>make calls</b> to the other managers and to my boss, who works in the USA. "
 "My working hours are 10 a.m. to 7 p.m., but I’m so busy I never <b>finish work</b> before 7 p.m.")
T2B = ("Olena is a(n) <span class='gap'>__SELB__</span>. She usually <b>starts work</b> at 9 o’clock and she always has a lot of work to do. "
 "She <b>answers messages</b> in Slack and <b>makes calls</b> or <b>writes emails</b>. She works with the developers and often <b>processes tickets</b> in Jira for them. "
 "She sometimes <b>goes to meetings</b> and takes notes. She rarely <b>travels for work</b>.")
B2 = [("1", "", "meetings", "go to", "go to"), ("2", "", "customers", "call", ""), ("3", "process", "", "tickets", ""), ("4", "do", "", "research", ""),
      ("5", "", "calls", "make", ""), ("6", "", "for work", "travel", ""), ("7", "", "(app) data", "analyse|analyze", ""), ("8", "write", "/ emails", "reports|messages", ""),
      ("9", "answer", "", "messages|the phone|calls|emails", ""), ("10", "", "work", "start|finish|start / finish|finish / start|start/finish|finish/start", "")]
Q3 = ["do research?", "go to meetings?", "start work at 9 o’clock?", "finish work at 6 o’clock?", "write reports?", "write emails?", "analyse data?", "answer messages in Slack?", "make video calls?", "process tickets in Jira?"]
Q3_UP = ["work from home?", "have a stand-up meeting?", "travel for work?", "use AI (ChatGPT, Copilot) for your tasks?", "work at the weekend?", "check messages after work?", "have lunch at your desk?", "take notes in meetings?"]
S_END = [("writes", "s"), ("makes", "s"), ("starts", "s"), ("tests", "s"), ("calls", "z"), ("goes", "z"), ("answers", "z"), ("designs", "z"), ("processes", "iz"), ("finishes", "iz"), ("analyses", "iz"), ("uses", "iz")]
T4 = [("Marek, Alina, Roman and I", "work", "work", "in an IT company. Marek tests apps, but he"),
      (None, "not be", "isn’t|is not|isnt", "a developer, he"), (None, "be", "’s|is|'s|s", "a QA Engineer. Alina and Roman"),
      (None, "be", "are|’re|'re", "designers. They"), (None, "start", "start", "work at 10 o’clock. They"),
      (None, "not finish", "don’t finish|do not finish|dont finish", "work before 7 o’clock.<br><br>I"),
      (None, "analyse", "analyse|analyze", "data from the app, but I"), (None, "not be", "’m not|am not|'m not|m not", "a developer. I"),
      (None, "be", "’m|am|'m|m", "a Data Analyst.")]
O5 = [("at / work / I / 10 o’clock / start / often", "I often start work at 10 o’clock."),
      ("always / we / have a stand-up / on Mondays", "We always have a stand-up on Mondays."),
      ("sometimes / they / a video call / have", "They sometimes have a video call."),
      ("after lunch / you / never / emails / write", "You never write emails after lunch."),
      ("data / don’t / they / analyse", "They don’t analyse data."),
      ("the app / doesn’t / she / test / usually", "She doesn’t usually test the app.")]
VIDS = [("RmQEETm8b1E", 2), ("TYds72a3klc", 3), ("NkVbRMJXHMU", 1)]   # speaker -> index in TITLES6 (1-based)
TITLES6 = ["Developer", "Product Manager", "Delivery Manager"]
TICK = [("starts the day with the backlog (a list of tasks)?", [2]), ("runs the daily stand-up meeting?", [3]), ("reviews a user story?", [1]),
        ("meets stakeholders (bosses, users, other departments)?", [2]), ("talks about feedback from a usability test?", [1]),
        ("talks to external teams about a delay?", [3]), ("works with the Product Manager?", [1, 3])]
C6 = ["The Product Manager often goes to meetings. …", "The Delivery Manager doesn’t write code. …", "The Developer always … after the stand-up.", "Who analyses data? Who doesn’t?"]
VOC = [("Jobs", ["Developer", "UX/UI Designer", "Project Manager", "Product Manager", "QA Engineer (tester)", "Data Analyst", "DevOps Engineer", "Recruiter (HR)"]),
       ("Tasks", ["go to meetings", "call customers", "process tickets", "do research", "make calls", "travel for work", "analyse data", "write reports / emails", "answer messages", "start / finish work"]),
       ("How often?", ["never", "rarely", "sometimes", "often", "usually", "always"]),
       ("From the video", ["stand-up", "backlog", "user story", "stakeholders", "usability test", "feedback", "team", "work together"])]

def gapsel(i, ans):
    return '<select class="js" data-a="%d" id="g2%s"><option value="">— choose —</option>%s</select>' % (ans, i, "".join('<option value="%d">%s</option>' % (k + 1, j) for k, j in enumerate(JOBS)))

h = []
# ---------- 1 Lead-in ----------
h.append('<section id="s1" class="sec"><div class="bsec">Lead-in</div>')
h.append('<p class="ins"><b>1A</b>Match the photos (A–D) with the correct jobs (1–8).</p><div class="ph">')
for L, em, desc, a in PHOTOS:
    h.append('<div class="pc"><div class="pl">%s</div><div class="pe">%s</div><p>%s</p><select class="js" data-a="%d"><option value="">— job —</option>%s</select></div>'
             % (L, em, desc, a, "".join('<option value="%d">%d %s</option>' % (k + 1, k + 1, j) for k, j in enumerate(JOBS))))
h.append('</div><ol class="jl">%s</ol><div class="ctrl"><button onclick="chk(\'s1\')">Check</button><span class="res" id="r_s1"></span></div>' % "".join("<li>%s</li>" % j for j in JOBS))
h.append('<p class="ins" style="margin-top:28px"><b>B</b>Answer the questions.</p>__LVL_lb__</section>')
# ---------- 2 Vocabulary ----------
h.append('<section id="s2" class="sec"><div class="bsec">Vocabulary <span class="sub">Jobs and tasks</span></div>')
h.append('<p class="ins"><b>2A</b>Read about two jobs. Choose a job from Exercise 1A to complete the descriptions.</p>')
h.append('<div class="txt"><p><b class="tl">A</b> %s</p><p><b class="tl">B</b> %s</p></div>' % (T2A.replace("__SELA__", gapsel("a", 4)), T2B.replace("__SELB__", gapsel("b", 3))))
h.append('<div class="ctrl"><button onclick="chk(\'p2a\')">Check</button><span class="res" id="r_p2a"></span></div><div class="note">💡 <b>Product Manager</b> = <i>what</i> we build and why. <b>Project Manager</b> = <i>how and when</i> we build it: tasks, deadlines, people.</div>')
h.append('<div id="p2a" hidden></div>')
h.append('<p class="ins" style="margin-top:28px"><b>B</b>Complete the expressions with words from Exercise 2A.</p><div class="ex2b" id="p2b">')
for n, pre, post, a, given in B2:
    inp = '<input class="ji" data-a="%s" value="%s"%s>' % (a, given, " readonly" if given else "")
    h.append('<div><span class="nn">%s</span> %s %s %s</div>' % (n, pre, inp, post))
h.append('</div><div class="ctrl"><button onclick="chk(\'p2b\')">Check</button><button class="l" onclick="showAns(\'p2b\')">Show answers</button><span class="res" id="r_p2b"></span></div></section>')
# ---------- 3 ----------
h.append('<section id="s3" class="sec"><div class="bsec">Vocabulary</div>')
h.append('<p class="ins"><b>3</b>Ask and answer the questions. Use the words in the box.</p>')
h.append('<div class="scale"><div class="sl"><span>0%</span><span>100%</span></div><div class="sw">' + "".join("<span>%s</span>" % w for w in ["never", "rarely", "sometimes", "often", "usually", "always"]) + '</div></div>')
h.append('<p class="hw">How often do you …</p>__LVL_q3__')
h.append('<div class="pron"><p class="ins"><span class="star">♪</span>Pronunciation: the <b>-s</b> ending. Listen to your teacher, then click the sound: /s/, /z/ or /ɪz/.</p><div class="sends">')
for w, s in S_END:
    h.append('<div class="se" data-a="%s"><b>%s</b><span><button onclick="snd(this,\'s\')">/s/</button><button onclick="snd(this,\'z\')">/z/</button><button onclick="snd(this,\'iz\')">/ɪz/</button></span></div>' % (s, w))
h.append('</div><p class="hint2">/ɪz/ after s, z, sh, ch, x, ge: <i>processes, finishes, uses</i>.</p></div></section>')
# ---------- 4 grammar ----------
h.append('<section id="s4" class="sec"><div class="bsec">Communicative grammar</div>')
h.append('''<div class="gbox"><div class="gh">FACTS AND ROUTINES</div><table>
<tr><td class="pm">+</td><td>I <b>am/’m</b> a Product Manager.<br>You/We/They <b>are/’re</b> Developers.</td><td>He/She <b>is/’s</b> a UX Designer.</td></tr>
<tr><td class="pm">+</td><td>I/You/We/They <b>always start</b> work at 10 o’clock.<br>I/You/We/They <b>usually come</b> to the office on Mondays.</td><td>He/She <b>often has</b> video calls.<br>It (the meeting) <b>usually finishes</b> at 11.</td></tr>
<tr><td class="pm">−</td><td>I <b>am not/’m not</b> a Data Analyst.<br>I/You/We/They <b>do not/don’t write</b> code.</td><td>He/She <b>is not/isn’t</b> a Developer.<br>He/She <b>does not/doesn’t call</b> customers.</td></tr></table>
<p class="gn">he/she/it + verb<b>-s</b>: work<b>s</b>, test<b>s</b>, analyse<b>s</b> · have → <b>has</b> · go → go<b>es</b> · do → do<b>es</b> · Adverb <i>before</i> the verb: <i>I <b>often</b> start…</i> but <i>after</i> be: <i>I’m <b>always</b> busy.</i></p></div>''')
h.append('<p class="ins"><b>4</b>Complete the text with the correct form of the verb in brackets.</p><div class="txt" id="p4"><p>')
for k, (pre, v, a, post) in enumerate(T4):
    h.append('%s<sup>%d</sup><input class="ji w" data-a="%s" placeholder="(%s)"> %s ' % ((pre + " ") if pre else "", k + 1, a, v, post))
h.append('</p></div><div class="ctrl"><button onclick="chk(\'p4\')">Check</button><button class="l" onclick="showAns(\'p4\')">Show answers</button><span class="res" id="r_p4"></span></div></section>')
# ---------- 5 ----------
h.append('<section id="s5" class="sec"><div class="bsec">Communicative grammar</div><p class="ins"><b>5</b>Put the words in order to make sentences. Click the words.</p><div id="p5">')
for k, (w, a) in enumerate(O5):
    h.append('<div class="ord" data-a="%s" data-w="%s"><span class="nn">%d</span><div class="src"></div><div class="dst"></div><button class="l sm" onclick="ordReset(this)">↺</button></div>' % (a, w, k + 1))
h.append('</div><div class="ctrl"><button onclick="ordChk()">Check</button><button class="l" onclick="ordShow()">Show answers</button><span class="res" id="r_p5"></span></div></section>')
# ---------- 6 VIDEO ----------
h.append('<section id="s6" class="sec"><div class="bsec vid">VIDEO</div><div class="vh"><b>A day in the life</b> · three people from one digital product team (UK) · each video 1–2 min</div>')
h.append('<p class="ins"><b>6A</b>Watch the videos. Match the job titles with the speakers 1–3.</p><div class="tbox">%s</div><div class="vids" id="p6a">' % " · ".join(TITLES6))
for k, (yid, a) in enumerate(VIDS):
    h.append('<div class="vc"><div class="vt">Speaker %d <a href="https://www.youtube.com/watch?v=%s" target="_blank">▶ open on YouTube</a></div><div class="fr"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0" allowfullscreen loading="lazy"></iframe></div><select class="js" data-a="%d"><option value="">— job title —</option>%s</select></div>'
             % (k + 1, yid, yid, a, "".join('<option value="%d">%s</option>' % (i + 1, t) for i, t in enumerate(TITLES6))))
h.append('</div><div class="ctrl"><button onclick="chk(\'p6a\')">Check</button><span class="res" id="r_p6a"></span></div>')
h.append('<p class="ins" style="margin-top:28px"><b>B</b>Watch the videos again. Tick (✓) the things that each person does.</p><table class="tk" id="p6b"><tr><th>Who …</th>%s</tr>' % "".join("<th>%s</th>" % t for t in TITLES6))
for q, who in TICK:
    h.append("<tr><td>%s</td>%s</tr>" % (q, "".join('<td><input type="checkbox" data-a="%d"></td>' % (1 if (i + 1) in who else 0) for i in range(3))))
h.append('</table><div class="ctrl"><button onclick="tick()">Check</button><span class="res" id="r_p6b"></span></div>')
h.append('<p class="ins" style="margin-top:28px"><b>C</b>Talk about what each person does and doesn’t do. Use the words in Exercise 3.</p><p class="ex"><i>The Delivery Manager always starts the day with a stand-up. The Developer doesn’t meet stakeholders…</i></p>__CARD_c6__</section>')
# ---------- 7 TASK ----------
h.append('''<section id="s7" class="sec"><div class="bsec task">TASK</div>
<p class="ins"><b>7A</b>Introduce yourself. Talk about these things: your name · your job · some tasks you do · your routine.</p>
<p class="ex"><i>My name’s Nick. I’m a front-end developer. I build websites. I always start work at ten o’clock.</i></p>
<div class="form" id="f7">
<label>My name’s <input id="t_name" placeholder="Maryna"></label>
<label>I’m a(n) <input id="t_job" placeholder="Project Manager"></label>
<label>I <input id="t_t1" placeholder="go to meetings"> and I <input id="t_t2" placeholder="write reports">.</label>
<label>I <select id="t_f1"><option>always</option><option selected>usually</option><option>often</option><option>sometimes</option><option>rarely</option><option>never</option></select> <input id="t_r1" placeholder="start work at 9 o’clock">.</label>
<label>I <select id="t_f2"><option>always</option><option>usually</option><option>often</option><option selected>sometimes</option><option>rarely</option><option>never</option></select> <input id="t_r2" placeholder="travel for work">.</label>
<label>I don’t <input id="t_neg" placeholder="write code">.</label>
<label class="gd">I’m <select id="t_g"><option value="she">she</option><option value="he">he</option></select> (for 7B)</label>
<div class="ctrl"><button onclick="intro()">Build my introduction</button></div>
</div>
<div class="out" id="o7a"></div>
<p class="ins" style="margin-top:28px"><b>B</b>Now talk about your partner — or about a colleague from your team. Use <b>he / she</b> + verb<b>-s</b>.</p>
<p class="ex"><i>This is Nick. He’s a front-end developer. He builds websites. He always starts work at ten o’clock.</i></p>
<div class="out" id="o7b"></div>
<p class="hint2">Check the <b>-s</b>: has, goes, does, analyses, processes, doesn’t + verb (no -s!).</p></section>''')
# ---------- self-assessment ----------
h.append('''<section id="s8" class="sec"><div class="bsec sa">Self-assessment</div>
<p class="big2">I can describe work activities and tasks.</p>
<div class="smile" id="score"><button onclick="sc(this)">🙂</button><button onclick="sc(this)">😐</button><button onclick="sc(this)">🙁</button></div>
<p class="ins" style="margin-top:22px">Tick the words you used today.</p><div class="chk">__WORDS__</div><p class="res" id="wc"></p>
<p class="ins" style="margin-top:22px">My 5 new phrases</p><div id="mine">%s</div></section>''' % "".join('<input placeholder="%d.">' % i for i in range(1, 6)))

body = "".join(h)
def card(key, title=""):
    return ('<div class="card"><span class="cnt" id="%sn"></span><div class="big" id="%sw"></div></div><div class="ctrl"><button class="l" onclick="step(\'%s\',-1)">← Back</button>'
            '<button onclick="step(\'%s\',1)">Next →</button><button class="l" onclick="shuf(\'%s\')">Shuffle</button></div>' % ((key,) * 5))
def lvl(sec, base, up):
    return ('<div class="lvl"><button class="on" onclick="lv(this,0)">Base</button><button class="p" onclick="lv(this,1)">★ Level up</button></div><div class="base">%s</div><div class="plus">%s</div>' % (card(base), card(up)))
body = body.replace("__LVL_lb__", '<div class="lvw">' + lvl("s1", "lb", "lbp") + "</div>").replace("__LVL_q3__", '<div class="lvw">' + lvl("s3", "q", "qp") + "</div>").replace("__CARD_c6__", card("c6"))
words = [w for _, ws in VOC for w in ws]
body = body.replace("__WORDS__", "".join('<label><input type="checkbox" onchange="wcnt()"> %s</label>' % w for w in words))
D = {"lb": LEAD_B, "lbp": LEAD_B_UP, "q": ["How often do you " + q for q in Q3], "qp": ["How often do you " + q for q in Q3_UP], "c6": C6}
vocab = "".join('<div class="vg"><h4>%s</h4>%s</div>' % (t, "".join("<span>%s</span>" % w for w in ws)) for t, ws in VOC)
nav = [("s1", "1"), ("s2", "2"), ("s3", "3"), ("s4", "4"), ("s5", "5"), ("s6", "6"), ("s7", "7"), ("s8", "✓")]

CSS = """*{box-sizing:border-box}body{margin:0;font-family:"Fira Sans",system-ui,sans-serif;font-weight:300;color:#231f20;background:#fff;font-size:17px;line-height:1.45}
header{display:flex;border-bottom:3px solid ACC}header .n{background:linear-gradient(120deg,DARK,#4f9be8);color:#fff;font-weight:500;font-size:34px;padding:10px 24px}
header h1{margin:0;align-self:center;padding-left:18px;font-weight:500;font-size:30px;color:#4d4d4f}header .tag{margin-left:auto;align-self:center;margin-right:16px;background:ACC;color:#fff;font-weight:600;font-size:12px;padding:6px 10px;border-radius:4px}
.out1{display:flex;align-items:center;gap:14px;background:ACC2;padding:8px 22px;font-size:15px}.out1 b{background:ACC;color:#fff;font-weight:600;padding:3px 10px;border-radius:3px;font-size:13px}
details.voc{max-width:1000px;margin:12px auto 0;border:1.5px solid ACC;border-radius:6px}details.voc summary{cursor:pointer;padding:8px 16px;color:DARK;font-weight:500}
.vgs{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;padding:6px 16px 14px}.vg h4{margin:4px 0 6px;color:DARK;font-weight:600;font-size:14px;text-transform:uppercase}.vg span{display:inline-block;background:ACC2;border-radius:12px;padding:2px 10px;margin:2px;font-size:14px}
.top{max-width:1000px;margin:0 auto;padding:10px 0 0}.top a{color:ACC;text-decoration:none;font-weight:500;font-size:15px}
nav{max-width:1000px;margin:8px auto 0;display:flex;flex-wrap:wrap;gap:8px}nav button{width:46px;height:40px;border:1.5px solid ACC;background:#fff;color:DARK;border-radius:20px;font:500 16px "Fira Sans",system-ui,sans-serif;cursor:pointer}nav button.on{background:ACC;color:#fff}
main{max-width:1000px;margin:0 auto;padding:6px 0 40px}.sec{display:none}.sec.on{display:block}
.bsec{font-weight:600;color:#8a8b8d;font-size:24px;margin:18px 0 10px}.bsec .sub{color:#231f20;font-weight:500;font-size:20px;margin-left:10px}.bsec.vid{color:#c2185b}.bsec.task{color:#fff;background:#d9534f;display:inline-block;padding:2px 14px;border-radius:4px}.bsec.sa{color:#fff;background:#d9746f;display:inline-block;padding:2px 14px;border-radius:4px}
.ins{font-weight:500;margin:14px 0 8px}.ins b{color:#d9534f;font-size:21px;margin-right:6px}.star{color:#c99a00;margin-right:6px}
.ph{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.pc{border:1px solid #d5d6d7;border-radius:6px;padding:10px;position:relative;background:#fafbfc}.pl{position:absolute;top:6px;left:6px;background:#d9534f;color:#fff;font-weight:600;padding:0 7px;border-radius:3px;font-size:14px}.pe{font-size:44px;text-align:center}.pc p{font-size:14px;margin:4px 0 8px;min-height:60px}
select,input{font:inherit;font-size:16px;border:1.5px solid #c8c9cb;border-radius:4px;padding:4px 6px;background:#fff}select{max-width:100%}.pc select{width:100%}
.jl{columns:2;font-size:16px;margin:12px 0 0;padding-left:24px}
.ctrl{display:flex;gap:8px;align-items:center;margin-top:10px;flex-wrap:wrap}.ctrl button,.form button{background:#4d4d4f;color:#fff;border:0;border-radius:4px;padding:8px 16px;font:500 15px "Fira Sans",system-ui,sans-serif;cursor:pointer}.ctrl button.l{background:#fff;color:#4d4d4f;border:1.5px solid #c8c9cb}button.sm{padding:3px 9px!important}
.res{font-weight:500;color:DARK}.ok{border-color:#3a9d5d!important;background:#eaf7ee!important}.no{border-color:#d9534f!important;background:#fdecec!important}
.txt{background:#fafbfc;border-left:4px solid ACC;padding:6px 16px;border-radius:4px}.txt b{font-weight:500}.tl{color:#d9534f;margin-right:6px}.note{margin-top:10px;background:#fff8e6;border-left:4px solid #f2b631;padding:8px 14px;font-size:15px}
.ex2b{display:grid;grid-template-columns:1fr 1fr;gap:8px 30px}.ex2b input{width:150px}.nn{font-weight:600;color:#d9534f;margin-right:6px}input[readonly]{color:#2a5fb0;font-style:italic;border-style:dashed}
.scale{border:1.5px solid #c8c9cb;border-radius:6px;max-width:620px;overflow:hidden}.sl{display:flex;justify-content:space-between;background:#fbe9e7;padding:4px 10px;font-weight:600;font-size:14px}.sw{display:flex;justify-content:space-between;padding:6px 10px}
.hw{font-weight:600;margin:16px 0 6px}.lvl{display:inline-flex;border:1.5px solid ACC;border-radius:18px;overflow:hidden;margin:4px 0 10px}.lvl button{border:0;background:#fff;padding:5px 16px;font:500 15px "Fira Sans",system-ui,sans-serif;color:DARK;cursor:pointer}.lvl button.p{color:#a07800}.lvl button.on{background:ACC;color:#fff}.lvw .plus{display:none}.lvw.up .plus{display:block}.lvw.up .base{display:none}
.card{background:#eef0f2;border-left:5px solid ACC;padding:22px 26px;min-height:110px;position:relative;border-radius:2px}.card .big{font-size:24px;font-weight:400}.cnt{position:absolute;right:12px;top:8px;font-size:13px;color:#8a8b8d}
.pron{margin-top:30px;border-top:1px dashed #c8c9cb;padding-top:4px}.sends{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.se{border:1px solid #d5d6d7;border-radius:6px;padding:6px 8px;display:flex;justify-content:space-between;align-items:center}.se b{font-weight:500}.se button{border:1px solid #c8c9cb;background:#fff;border-radius:3px;margin-left:3px;cursor:pointer;font-size:13px;padding:2px 5px}.hint2{font-size:14px;color:#6d6e70}
.gbox{border:2px solid #f0a59f;border-radius:4px;padding:0 0 8px;margin-bottom:14px}.gh{color:#d9534f;font-weight:600;padding:6px 12px;border-bottom:1px solid #f0a59f}.gbox table{width:100%;border-collapse:collapse;font-size:16px}.gbox td{padding:7px 10px;border-bottom:1px dotted #f0a59f;vertical-align:top}.gbox b{font-weight:600}.pm{color:#d9534f;font-weight:600;width:20px}.gn{font-size:15px;margin:8px 12px 0;color:#4d4d4f}
#p4 input.w{width:130px}#p4 p{line-height:2.3}
.ord{display:flex;align-items:flex-start;gap:8px;border-bottom:1px solid #eee;padding:8px 0}.src,.dst{display:flex;flex-wrap:wrap;gap:5px;min-height:32px}.src{flex:1}.dst{flex:1.3;border-bottom:2px solid #c8c9cb;padding-bottom:4px}.src span,.dst span{background:ACC2;border-radius:4px;padding:3px 8px;cursor:pointer;font-size:15px}.dst span{background:#fff;border:1px solid ACC}.ord.ok .dst{border-color:#3a9d5d}.ord.no .dst{border-color:#d9534f}.ord .ans{flex-basis:100%;color:DARK;font-style:italic;font-size:15px}
.vh{background:#fcf1f5;border-left:4px solid #c2185b;padding:6px 14px;font-size:15px}.tbox{border:1.5px solid #c8c9cb;display:inline-block;padding:6px 14px;margin-bottom:10px}.vids{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.vt{font-weight:500;margin-bottom:4px}.vt a{font-size:13px;color:#c2185b;margin-left:6px}.fr{position:relative;padding-top:56.25%}.fr iframe{position:absolute;inset:0;width:100%;height:100%;border:0}.vc select{width:100%;margin-top:6px}
.tk{border-collapse:collapse;font-size:16px}.tk th,.tk td{border:1px solid #c8c9cb;padding:6px 10px}.tk th{background:ACC2;font-weight:500}.tk td input{width:20px;height:20px}.tk td:not(:first-child){text-align:center}.tk td.ok{background:#eaf7ee}.tk td.no{background:#fdecec}
.ex{color:#2a5fb0;margin:4px 0 10px}.form{display:flex;flex-direction:column;gap:8px;background:#fafbfc;border:1px solid #e1e2e3;padding:14px;border-radius:6px}.form input{width:230px}.gd{font-size:14px;color:#6d6e70}
.out{white-space:pre-wrap;background:#fdf3f2;border-left:4px solid #d9534f;padding:10px 14px;margin-top:10px;font-size:18px;display:none}
.big2{font-size:22px}.smile button{font-size:34px;background:#fff;border:2px solid #e1e2e3;border-radius:50%;width:62px;height:62px;cursor:pointer;margin-right:8px}.smile button.on{border-color:ACC;background:ACC2}
.chk{display:flex;flex-wrap:wrap;gap:6px}.chk label{background:#f3f4f5;border-radius:14px;padding:3px 10px;font-size:15px;cursor:pointer}#mine input{display:block;width:420px;margin:5px 0}
footer{max-width:1000px;margin:0 auto;padding:10px 0 30px;font-size:12px;color:#77787b}
@media(max-width:800px){main,nav,.top,details.voc{padding-left:12px;padding-right:12px}.ph,.vids,.sends,.vgs{grid-template-columns:1fr 1fr}.ex2b{grid-template-columns:1fr}}"""
CSS = CSS.replace("ACC2", ACC2).replace("ACC", ACC).replace("DARK", DARK)

JS = r"""
const D=__D__;const st={},ord={};const $=id=>document.getElementById(id);
const norm=s=>(s||"").toLowerCase().replace(/[’`]/g,"'").replace(/\s+/g," ").replace(/[.!?]+$/,"").trim();
function render(k){const a=ord[k];$(k+"w").textContent=D[k][a[st[k]]];$(k+"n").textContent=(st[k]+1)+" / "+a.length}
function step(k,d){st[k]=(st[k]+d+ord[k].length)%ord[k].length;render(k)}
function shuf(k){const a=ord[k];for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}st[k]=0;render(k)}
function lv(b,u){const w=b.closest(".lvw");w.classList.toggle("up",!!u);b.parentNode.querySelectorAll("button").forEach(x=>x.classList.remove("on"));b.classList.add("on")}
function chk(id){const box=$(id==="p2a"?"s2":id);let ok=0,n=0;
 const els=id==="p2a"?box.querySelectorAll(".txt select"):box.querySelectorAll("select.js,input.ji");
 els.forEach(e=>{if(e.readOnly)return;n++;const good=e.tagName==="SELECT"?e.value===e.dataset.a:e.dataset.a.split("|").some(a=>norm(a)===norm(e.value));e.classList.toggle("ok",good);e.classList.toggle("no",!good);if(good)ok++});
 $("r_"+id).textContent=ok+" / "+n+(ok===n?" ✓ Well done!":"")}
function showAns(id){$(id).querySelectorAll("input.ji").forEach(e=>{if(!e.readOnly){e.value=e.dataset.a.split("|")[0];e.classList.remove("no")}})}
function snd(b,s){const d=b.closest(".se");const good=d.dataset.a===s;d.classList.toggle("ok",good);d.classList.toggle("no",!good)}
function ordInit(){document.querySelectorAll(".ord").forEach(o=>{const src=o.querySelector(".src"),dst=o.querySelector(".dst");src.innerHTML="";dst.innerHTML="";o.classList.remove("ok","no");const x=o.querySelector(".ans");if(x)x.remove();
 o.dataset.w.split(" / ").forEach(w=>{const s=document.createElement("span");s.textContent=w;s.onclick=()=>{(s.parentNode===src?dst:src).appendChild(s)};src.appendChild(s)})})}
function ordReset(b){const o=b.closest(".ord"),src=o.querySelector(".src");o.querySelectorAll(".dst span").forEach(s=>src.appendChild(s));o.classList.remove("ok","no")}
function ordText(o){let t=[...o.querySelectorAll(".dst span")].map(s=>s.textContent).join(" ");return t.charAt(0).toUpperCase()+t.slice(1)}
function ordChk(){let ok=0;document.querySelectorAll(".ord").forEach(o=>{const good=norm(ordText(o))===norm(o.dataset.a);o.classList.toggle("ok",good);o.classList.toggle("no",!good);if(good)ok++});$("r_p5").textContent=ok+" / 6"+(ok===6?" ✓ Well done!":"")}
function ordShow(){document.querySelectorAll(".ord").forEach(o=>{if(!o.querySelector(".ans")){const p=document.createElement("div");p.className="ans";p.textContent="→ "+o.dataset.a;o.appendChild(p)}})}
function tick(){let ok=0,n=0;document.querySelectorAll("#p6b input").forEach(c=>{n++;const good=(c.checked?1:0)===+c.dataset.a;c.parentNode.className=good?"ok":"no";if(good)ok++});$("r_p6b").textContent=ok+" / "+n+(ok===n?" ✓ Well done!":"")}
function s3(v){v=v.trim();const sp=v.split(" ");let w=sp[0].toLowerCase(),r=sp.slice(1).join(" ");const irr={have:"has",go:"goes",do:"does",be:"is"};
 if(irr[w])w=irr[w];else if(/(s|sh|ch|x|z|o)$/.test(w))w+="es";else if(/[^aeiou]y$/.test(w))w=w.slice(0,-1)+"ies";else w+="s";return (w+" "+r).trim()}
function intro(){const g=x=>$(x).value.trim();const nm=g("t_name")||"…",job=g("t_job")||"…",t1=g("t_t1")||"…",t2=g("t_t2")||"…",r1=g("t_r1")||"…",r2=g("t_r2")||"…",ng=g("t_neg")||"…",f1=$("t_f1").value,f2=$("t_f2").value;
 const he=$("t_g").value,He=he==="he"?"He":"She";
 $("o7a").textContent=`My name’s ${nm}. I’m a(n) ${job}. I ${t1} and I ${t2}. I ${f1} ${r1}. I ${f2} ${r2}. I don’t ${ng}.`;
 $("o7b").textContent=`This is ${nm}. ${He}’s a(n) ${job}. ${He} ${s3(t1)} and ${he} ${s3(t2)}. ${He} ${f1} ${s3(r1)}. ${He} ${f2} ${s3(r2)}. ${He} doesn’t ${ng}.`;
 $("o7a").style.display=$("o7b").style.display="block"}
function sc(b){document.querySelectorAll("#score button").forEach(x=>x.classList.remove("on"));b.classList.add("on")}
function wcnt(){const n=document.querySelectorAll(".chk input:checked").length;$("wc").textContent=n+" words used"+(n>=10?" — great!":"")}
document.querySelectorAll("nav button").forEach(b=>b.onclick=()=>{document.querySelectorAll("nav button,.sec").forEach(x=>x.classList.remove("on"));b.classList.add("on");$(b.dataset.s).classList.add("on");scrollTo(0,0)});
for(const k in D){ord[k]=D[k].map((_,i)=>i);st[k]=0;render(k)}ordInit();$("s1").classList.add("on");
"""
html = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>1.1 Daily tasks — Lesson</title><link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300;400;500;600&display=swap" rel="stylesheet"><style>%s</style></head><body>
<header><div class="n">1.1</div><h1>Daily tasks</h1><div class="tag">LESSON</div></header>
<div class="out1"><b>Lesson outcome</b>You can describe work activities and tasks.</div>
<details class="voc" open><summary>📖 Vocabulary of this lesson — click to hide / show</summary><div class="vgs">%s</div></details>
<div class="top"><a href="../../../index.html">← Contents</a></div>
<nav>%s</nav><main>%s</main><footer>Video: “A day in the life”, Digital Public Services Wales (YouTube). Valentyna Hordiienko · Middle Learning Architect</footer>
<script>%s</script></body></html>""" % (CSS, vocab, "".join('<button data-s="%s"%s>%s</button>' % (s, ' class="on"' if s == "s1" else "", l) for s, l in nav), body, JS.replace("__D__", json.dumps(D, ensure_ascii=False)))
open(OUT, "w").write(html); print("ok", len(html))
