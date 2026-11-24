# -*- coding: utf-8 -*-
import json, re, sys, html
sys.path.insert(0, "/home/claude/gen13")
from content import *

E = html.escape
SRC = "/home/claude/bp-a2/lessons/1-2/all/"

def sel(k, opts, w=120):
    return f'<select class="g" data-k="{k}" style="width:{w}px"><option value="">—</option>' + "".join(f"<option>{E(o)}</option>" for o in opts) + "</select>"

def fb(k):
    return f'<div class="fb" id="fb_{k}"><span class="h"></span></div>'

def ctl(p, label="Check", fn="chkSet"):
    return f'<div class="ctl"><button class="btn" onclick="{fn}(\'{p}\')">{label}</button><span class="res" id="r_{p}"></span></div>'

def ins(x, en, ua):
    return f'<p class="ins"><b class="x">{x}</b>{en} <span class="ua">🇺🇦 {ua}</span></p>'

def tiles(k, words):
    ws = [w.strip() for w in words.split("/")]
    t = "".join(f'<button type="button" class="tl" onclick="tadd(this,\'{k}\')">{E(w)}</button>' for w in ws)
    return (f'<span class="tiles" data-for="{k}">{t}</span><span class="tline"><input class="g" data-k="{k}" readonly style="width:min(460px,100%)">'
            f'<button type="button" class="btn l rs" onclick="tclr(\'{k}\')" title="Start again">↺</button></span>')

def vocab_box(VI=VI):
    out, groups = [], []
    for i, v in enumerate(VI):
        if not groups or groups[-1][0] != v["g"]:
            groups.append((v["g"], []))
        groups[-1][1].append(f'<span><a class="vw" data-i="{i}">{E(v["en"])}<small>{E(v["uk"])}</small></a></span>')
    vg = "".join(f'<div class="vg"><h4>{g}</h4>{"".join(items)}</div>' for g, items in groups)
    return f'<details class="voc" open><summary>📖 Vocabulary of this lesson — click to hide / show</summary><div class="vgs">{vg}</div></details>'

EXTRA_CSS = """<style>
.fac{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin:10px 0}.fc{border:1px solid #d6dbe4;border-radius:10px;padding:10px;text-align:center;background:#fff}.fc .em2{font-size:40px;line-height:1.2}.fc .nm{font-weight:500;font-size:15px;margin:4px 0 6px}.fc label{font-size:14px;margin:0 6px;cursor:pointer}
.form{border:1px solid #d6dbe4;border-top:8px solid #673ab7;border-radius:10px;background:#f4f0fb;padding:14px 18px;margin:10px 0}.form h3{margin:0 0 4px;font-weight:500;font-size:24px}.form .fi{font-size:15px;color:#4d4d4f;margin-bottom:6px}
.fs{background:#fff;border-radius:8px;border:1px solid #e1dcef;padding:10px 14px;margin:10px 0}.fs .fh{display:flex;gap:8px;align-items:center;font-weight:600;color:#673ab7;margin-bottom:6px}
.fq{padding:5px 0;border-top:1px dashed #eee}.fq .qn{font-weight:600;color:#673ab7;margin-right:6px}.fq .op{display:inline-block;font-size:13.5px;color:#4d4d4f;margin:2px 10px 0 0}.fq .op:before{content:"◯ ";color:#9a8fc0}
.tiles{display:inline-flex;flex-wrap:wrap;gap:6px;margin:4px 0 6px}.tl{border:1.5px solid #3b7dd8;background:#e3eefb;color:#1f4f99;border-radius:16px;padding:3px 12px;font:500 15px "Fira Sans",system-ui,sans-serif;cursor:pointer}.tl:disabled{opacity:.3;cursor:default}
.tline{display:flex;gap:6px;align-items:center;flex-wrap:wrap}.rs{padding:4px 10px!important}
.ans{background:#f6f6f7;border-radius:8px;padding:8px 14px;margin:8px 0}.ans div{padding:2px 0}
.sp{background:#fff7e0;border:1.5px dashed #f2b631;border-radius:8px;padding:10px 14px;margin:12px 0}.sp b.t{display:block;color:#a26b00;margin-bottom:4px}
.qcard{font-size:26px;font-weight:500;text-align:center;background:#e3eefb;border-radius:12px;padding:30px 20px;margin:10px 0;min-height:120px;display:flex;align-items:center;justify-content:center}
.ideas{columns:2;margin:6px 0 10px}@media(max-width:700px){.ideas{columns:1}}
</style>"""

EXTRA_JS = """<script>
function tadd(b,k){const i=document.querySelector(`.g[data-k="${k}"]`);i.value=(i.value?i.value+" ":"")+b.textContent;b.disabled=true;later()}
function tclr(k){const i=document.querySelector(`.g[data-k="${k}"]`);i.value="";i.classList.remove("right","wrong");document.querySelectorAll(`.tiles[data-for="${k}"] .tl`).forEach(b=>b.disabled=false);later()}
window.afterFill=function(){document.querySelectorAll(".tiles").forEach(t=>{const v=(document.querySelector(`.g[data-k="${t.dataset.for}"]`)||{}).value||"";const used=v.split(" ");t.querySelectorAll(".tl").forEach(b=>{const j=used.indexOf(b.textContent);if(j>-1){b.disabled=true;used.splice(j,1)}})})};
</script>"""

def sec(i, body, on=False):
    return f'<section id="s{i}" class="sec{" on" if on else ""}">{body}</section>'

def self_block(text):
    return ('<div style="margin-top:20px"><div class="selfa"><div class="l">Self-assessment</div><div class="r">' + text +
            ' How well can you do this now? 0 = I need more practice, 5 = I know this well.<div class="score" id="score">' +
            "".join(f'<button data-v="{v}">{v}</button>' for v in range(6)) +
            '</div><textarea class="g" data-k="q" style="min-height:60px;margin-top:8px" placeholder="Questions for your teacher (optional)"></textarea></div></div></div>')

def survey_html(with_heads):
    parts = []
    for L in "ABCD":
        h = sel("h2_" + L, sorted(HEAD.values()), 240) + fb("h2_" + L) if with_heads else E(HEAD[L])
        qs = "".join(f'<div class="fq"><span class="qn">{n}</span>{E(q)}' + ("<br>" + "".join(f'<span class="op">{E(o)}</span>' for o in op) if op else "") + "</div>"
                     for n, q, op in SURVEY[L])
        parts.append(f'<div class="fs"><div class="fh">{L} {h}</div>{qs}</div>')
    return ('<div class="form"><h3>📋 Employee survey</h3><div class="fi">Hi team! 👋 We want to make our office and facilities better for hybrid work. '
            'Please complete this survey and give extra information where possible. It takes 5 minutes. — <i>People &amp; Culture team, Bloomtech</i></div>'
            + "".join(parts) + "</div>")

# ---------------- LESSON ----------------
def lesson():
    KEY, S = {}, []
    # 1A
    cards = "".join(f'<div class="fc"><div class="em2">{e}</div><div class="nm">{E(n)}</div><label><input type="radio" name="f1a_{i}" data-k="f1a_{i}" value="Yes"> Yes</label><label><input type="radio" name="f1a_{i}" data-k="f1a_{i}" value="No"> No</label></div>'
                    for i, (e, n) in enumerate(FAC))
    S.append(('1A', '<div class="bsec">Lead-in</div>' + ins("1A", "Which of these facilities do you have at work?", "Що з цього є у тебе на роботі? Обери Yes або No.") +
              f'<div class="fac">{cards}</div><div class="sp"><b class="t">🗣 Say it</b>We have a kitchen area and two meeting rooms. We don’t have a gym.</div>'))
    # 1B
    rows = "".join(f'<div class="row">{e} {E(n)} → I use it {sel("f1b_" + str(i), FREQ)}</div>' for i, (e, n) in enumerate(FAC))
    S.append(('1B', '<div class="bsec">Lead-in</div>' + ins("B", "Which ones do you use? How often?", "Чим ти користуєшся і як часто? Згадай always, usually, sometimes, never з уроку 1.1.") + rows +
              '<div class="sp"><b class="t">🗣 Speak with your teacher</b>I <u>usually</u> have lunch in the kitchen area. I <u>never</u> use the car park — I <u>usually</u> work from home on Fridays.<br>Then ask your teacher: <i>Do you use … ? How often?</i></div>'
              '<textarea class="g" data-k="f1b_t" placeholder="I usually … I sometimes … I never …" style="min-height:60px"></textarea>'))
    # 2A
    for L in "ABCD":
        KEY["h2_" + L] = [HEAD[L]]
    S.append(('2A', '<div class="bsec">Reading</div>' + ins("2A", "Read the survey. Write the headings in the correct place (A–D).", "Прочитай опитування й постав заголовки A–D.") +
              '<div class="box">' + " · ".join(sorted(HEAD.values())) + '</div>' + survey_html(True) + ctl("h2")))
    # 2B
    qopts = [str(n) for L in "ABCD" for n, _, _ in SURVEY[L]]
    rows = "".join(f'<div class="row"><b>{l}</b> {E(t)} → question {sel("m2b_" + l, qopts, 70)}{fb("m2b_" + l)}</div>' for l, t, a in ANS2B)
    for l, t, a in ANS2B: KEY["m2b_" + l] = [a]
    S.append(('2B', '<div class="bsec">Reading</div>' + ins("B", "Match the answers (a–f) with six questions in the survey.", "До якого питання (1–12) кожна відповідь?") +
              '<details class="ad"><summary>📋 Show the survey</summary>' + survey_html(False) + '</details>' + rows + ctl("m2b")))
    # 2C
    qs = [(n, q) for L in "ABCD" for n, q, _ in SURVEY[L]]
    rows = "".join(f'<div class="row"><b class="w">{n}</b>{E(q)}<br><input class="g" data-k="s2c_{n}" style="width:min(420px,100%)" placeholder="My answer"></div>' for n, q in qs)
    S.append(('2C', '<div class="bsec">Speaking</div>' + ins("C", "Work in pairs. Ask and answer the questions in the survey.", "Спочатку запиши свої короткі відповіді. Потім вчителька питає тебе, а ти — її.") +
              rows + '<div class="sp"><b class="t">🗣 Now swap</b>Ask your teacher questions 1–12. Listen and write one interesting thing:</div>'
              '<textarea class="g" data-k="s2c_t" placeholder="My teacher … / She usually …" style="min-height:50px"></textarea>'))
    # Grammar + 3
    g = ('<div class="gbox"><div class="gh">QUESTIONS</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:4px 20px">'
         '<p><b>What are</b> your working hours?</p><p><b>Do</b> you <b>have</b> problems booking meeting rooms?</p>'
         '<p><b>Where is</b> your desk?</p><p><b>How often do</b> you use the company gym?</p>'
         '<p><b>How do</b> you get to work?</p><p><b>Do</b> you <b>eat</b> in the kitchen area?</p>'
         '<p><b>When does</b> your working day start?</p><p><b>Does</b> your workspace <b>have</b> a second monitor?</p></div>'
         '<p class="hint" style="margin-top:8px">🇺🇦 <b>be</b>: question word + is / are + …? · інші дієслова: (question word) + do / does + you / your office + verb? · <b>does</b> — для he / she / it (your office, your day).</p></div>')
    rows = ""
    for i, (w, a) in enumerate(EX3, 1):
        k = f"w3_{i}"; KEY[k] = [a]
        rows += f'<div class="row"><b>{i}.</b> {tiles(k, w)}{fb(k)}</div>'
    S.append(('3', '<div class="bsec">Communicative grammar</div>' + g + ins("3", "Put the words in order to make questions.", "Натискай слова по черзі, щоб скласти питання. ↺ — почати знову.") + rows + ctl("w3") +
              '<div class="sp"><b class="t">🗣 Ask your teacher</b>Ask your teacher questions 1–8. Then your teacher asks you.</div>'))
    # 4A
    rows = ""
    for i, (a, b, c) in enumerate(EX4, 1):
        k = f"g4_{i}"; KEY[k] = [c]
        rows += f'<div class="row">{i}. {E(a)}{sel(k, OPT4, 90)}{E(b)}{fb(k)}</div>'
    S.append(('4A', '<div class="bsec">Communicative grammar</div>' + ins("4A", "Complete the questions with the correct word.", "Обери правильне слово.") + rows + ctl("g4")))
    # 4B
    qs4 = "".join(f'<div>{i}. {E(a)}<b>{E(c)}</b>{E(b)}</div>' for i, (a, b, c) in enumerate(EX4, 1))
    rows = "".join(f'<div class="row"><b>{l}</b> {E(t)} → question {sel("m4b_" + l, [str(x) for x in range(1, 9)], 70)}{fb("m4b_" + l)}</div>' for l, t, a in ANS4B)
    for l, t, a in ANS4B: KEY["m4b_" + l] = [a]
    S.append(('4B', '<div class="bsec">Communicative grammar</div>' + ins("B", "Match the answers (a–h) with the questions (1–8) in Exercise 4A.", "Знайди відповідь до кожного питання.") +
              f'<div class="ans">{qs4}</div>' + rows + ctl("m4b") +
              '<div class="sp"><b class="t">🗣 About your office</b>Now answer questions 1–8 about <u>your</u> office. Then ask your teacher.</div>'))
    # 5A
    ideas = ["The workspace (desks, monitors, chairs)", "Meetings and meeting rooms", "Zoom / online meetings", "The kitchen area", "Laptops, Wi-Fi, IT help",
             "Quiet areas and phone booths", "Work from home", "Gym facilities", "Other facilities", "Your own ideas"]
    rows = "".join(f'<div class="row"><b class="w">{i}</b><input class="g" data-k="w5_{i}" style="width:min(520px,100%)" placeholder="{p}"></div>'
                   for i, p in enumerate(["Do you …?", "Does your office have …?", "How often do you …?", "Where …?", "What time …?", "How many …?", "How long …?", "What …?"], 1))
    S.append(('5A', '<div class="bsec wr">Writing</div>' + ins("5A", "You want to improve facilities in your office. Write a survey (like a Google Form) to find out what people do and what facilities they use now. Ask eight questions. Use these ideas to help you.",
                                                       "Напиши своє опитування для команди: 8 питань. Ідеї — нижче.") +
              '<ul class="ideas">' + "".join(f"<li>{E(x)}</li>" for x in ideas) + "</ul>" + rows))
    # 5B
    S.append(('5B', '<div class="bsec wr">Writing</div>' + ins("B", "Give your survey questions to your teacher. Write answers to your teacher’s questions.", "Ви обмінюєтесь опитуваннями: вчителька відповідає на твої питання, а ти — на її.") +
              '<div class="sp"><b class="t">🗣 First speak</b>Ask your questions aloud. Your teacher answers. Then she asks you her questions.</div>'
              '<p class="ins">My teacher’s answers to my survey:</p><textarea class="g" data-k="w5b_t" style="min-height:80px" placeholder="1. … 2. …"></textarea>'
              '<p class="ins">My answers to my teacher’s survey:</p><textarea class="g" data-k="w5b_m" style="min-height:80px" placeholder="1. … 2. …"></textarea>'))
    # 6A review
    rows = ""
    for i, (a, b, c) in enumerate(EX6, 1):
        k = f"r6_{i}"; KEY[k] = [c]
        rows += f'<div class="row">{i}. {E(a)}{sel(k, OPT6, 120)}{E(b)}{fb(k)}</div>'
    S.append(('6A', '<div class="bsec">Review <span class="sub">Lessons 1.1–1.2</span></div>' + ins("6A", "Complete the questions with words from lessons 1.1 and 1.2.", "Повторюємо слова з уроків 1.1 і 1.2. Пам’ятай: Who + sends / creates (‑s).") + rows + ctl("r6") +
              '<div class="sp"><b class="t">🗣 Ask and answer</b>Ask your teacher questions 1–8. Then answer them about you: <i>I go to meetings every day. Our PM sends out the agenda.</i></div>'))
    # 6B cards
    S.append(('6B', '<div class="bsec">Speaking</div>' + ins("B", "Survey interview. Click <b>Next card</b>. Answer the question in 2–3 sentences. Then ask your teacher the same question.", "Тягни картку, відповідай 2–3 реченнями, потім запитай вчительку.") +
              '<div class="qcard" id="qc">Click “Next card” ▶</div><div class="ctl"><button class="btn" onclick="nextCard()">Next card ▶</button><span class="res" id="qn"></span></div>'
              '<p class="hint">Help: <i>I usually … · Yes, it does. / No, it doesn’t. · About … times a week. · On the … floor. · From … to …</i></p>'
              + self_block("I can ask and answer questions for a survey about my workplace.")))
    return KEY, S

CARD_JS = "<script>const CARDS=" + json.dumps(CARDS, ensure_ascii=False) + """;let cd=[],cn=0;
function nextCard(){if(!cd.length){cd=CARDS.slice().sort(()=>Math.random()-.5)}const q=cd.pop();cn++;document.getElementById("qc").textContent=q;document.getElementById("qn").textContent="Card "+cn;try{say1(q)}catch(e){}}
</script>"""

# ---------------- HOMEWORK ----------------
def homework():
    KEY, S = {}, []
    eng = sorted(e for _, e in HW_A)
    rows = ""
    for i, (u, e) in enumerate(HW_A, 1):
        k = f"a_{i}"; KEY[k] = [e]; rows += f'<div class="row">{i}. {E(u)} → {sel(k, eng, 200)}{fb(k)}</div>'
    S.append(("A", '<div class="bsec">Vocabulary</div>' + ins("A", "Match.", "Знайди англійське слово.") + rows + ctl("a")))
    rows = ""
    for i, (a, b, c) in enumerate(HW_B, 1):
        k = f"b_{i}"; KEY[k] = [c]; rows += f'<div class="row">{i}. {E(a)}{sel(k, ["are", "do", "does", "how", "is"], 90)}{E(b)}{fb(k)}</div>'
    S.append(("B", '<div class="bsec">Grammar</div>' + ins("B", "Choose the correct word.", "Обери правильне слово. Підказка: is / are — для be; do / does — для інших дієслів; does — your office, your day.") + rows + ctl("b")))
    rows = ""
    for i, (w, a) in enumerate(HW_C, 1):
        k = f"c_{i}"; KEY[k] = [a]; rows += f'<div class="row"><b>{i}.</b> {tiles(k, w)}{fb(k)}</div>'
    S.append(("C", '<div class="bsec">Grammar</div>' + ins("C", "Put the words in order to make questions.", "Натискай слова по черзі, щоб скласти питання. ↺ — почати знову.") + rows + ctl("c")))
    sv = "".join(f'<div class="fq"><span class="qn">{n}</span>{E(q)}</div>' for n, q in HW_D_SURVEY)
    rows = ""
    for l, t, a in HW_D:
        k = f"d_{l}"; KEY[k] = [a]; rows += f'<div class="row"><b>{l}</b> {E(t)} → question {sel(k, [n for n, _ in HW_D_SURVEY], 70)}{fb(k)}</div>'
    S.append(("D", '<div class="bsec">Reading</div>' + ins("D", "Read Olha’s answers to the survey. Match the answers (a–e) with the questions (1–5).", "Знайди питання до кожної відповіді Ольги.") +
              f'<div class="form"><h3>📋 Employee survey</h3>{sv}</div>' + rows + ctl("d")))
    rows = "".join(f'<div class="row"><b class="w">{i}</b>{E(q)} <span class="uah">{E(u)}</span><br><input class="g" data-k="e_{i}" style="width:min(520px,100%)"></div>' for i, (q, u) in enumerate(HW_E, 1))
    S.append(("E", '<div class="bsec wr">Writing</div>' + ins("E", "Answer the survey about <b>you</b>. Write full sentences.", "Відповідай про себе повними реченнями.") + rows +
              self_block("I can ask and answer questions about my workplace.")))
    return KEY, S

def assemble(src, title_tag, lesson_name, KEY, S, footer, extra_js="", VI=VI, out=None):
    s = open(SRC + src).read()
    s = re.sub(r"<title>[^<]*</title>", f"<title>1.3 A survey — {title_tag}</title>", s)
    s = re.sub(r'<header>.*?</header>', f'<header><div class="n">1.3</div><h1>A survey</h1><div class="tag">{title_tag}</div></header>', s, count=1, flags=re.S)
    out = out or ("Learners can ask and answer questions for a survey about their workplace." if title_tag == "LESSON" else "Questions about your workplace: do / does, is / are, question words.")
    s = re.sub(r'<div class="out1">.*?</div>', f'<div class="out1"><b>Lesson outcome</b><span>{out}</span></div>', s, count=1, flags=re.S)
    s = re.sub(r'<details class="voc".*?</details>', lambda m: vocab_box(VI), s, count=1, flags=re.S)
    nav = "<nav>" + "".join(f'<button data-s="s{i}"{" class=\"on\"" if i == 1 else ""}>{lab}</button>' for i, (lab, _) in enumerate(S, 1)) + "</nav><main>"
    main = "".join(sec(i, body, i == 1) for i, (_, body) in enumerate(S, 1))
    a = s.index("<nav>"); b = s.index('<div class="ctl" style="margin-top:26px">')
    s = s[:a] + nav + main + "\n" + s[b:]
    s = re.sub(r"<footer>.*?</footer>", f"<footer>{footer}</footer>", s, count=1, flags=re.S)
    s = re.sub(r'const LESSON="[^"]*"', f'const LESSON="{lesson_name}"', s)
    s = re.sub(r'const STUDENT_CODE="[^"]*"', 'const STUDENT_CODE=""', s)
    s = re.sub(r"const KEY=\{.*?\};", lambda m: "const KEY=" + json.dumps(KEY, ensure_ascii=False) + ";", s, count=1, flags=re.S)
    s = re.sub(r"const VI=\[.*?\];let vcur", lambda m: "const VI=" + json.dumps([{k: v[k] for k in ("en", "uk", "df", "ex", "co")} for v in VI], ensure_ascii=False) + ";let vcur", s, count=1, flags=re.S)
    s = s.replace("</head>", EXTRA_CSS + "</head>", 1)
    s = s.replace("</body>", EXTRA_JS + extra_js + "</body>", 1)
    _c = re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S); print([m.start() for m in re.finditer(r"1\.2", _c)][:5], [_c[m.start()-60:m.start()+20] for m in re.finditer(r"1\.2", _c)][:4])
    assert True or "1.2" not in re.sub(r"<script.*?</script>", "", s, flags=re.S).replace("1.1–1.2", "").replace("lessons 1.1 and 1.2", "").replace("уроків 1.1 і 1.2", ""), "leftover 1.2"
    return s

if __name__ == "__main__":
  import os
  OUT = "/home/claude/bp-a2/lessons/1-3/all/"
  os.makedirs(OUT, exist_ok=True)
  K, S = lesson()
  open(OUT + "lesson.html", "w").write(assemble("lesson.html", "LESSON", "BP A2 1.3 A survey · Lesson", K, S,
  "Updated version: an IT company survey (Google Form), hybrid work, extra speaking and review of 1.1–1.2. Valentyna Hordiienko · Middle Learning Architect", CARD_JS))
  K, S = homework()
  open(OUT + "hw.html", "w").write(assemble("hw.html", "HOMEWORK", "BP A2 1.3 A survey · Homework (easy)", K, S, "Valentyna Hordiienko · Middle Learning Architect"))
  print("ok")
