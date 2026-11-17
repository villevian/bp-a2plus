"""Business Partner A2 · 1.1 Daily tasks (IT) — EASY HOMEWORK (A1-friendly), Supabase sync.
Short sentences, choose-the-answer tasks, instructions in English + Ukrainian.
Usage: python3 build_a2_hw_1-1_easy.py OUT.html [STUDENT_CODE]
"""
import sys, json
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK = "#3b7dd8", "#e3eefb", "#2a5fb0"
WORDS_UA = [("go to meetings", "ходити на зустрічі"), ("answer messages", "відповідати на повідомлення"), ("write emails", "писати листи (імейли)"),
            ("make calls", "дзвонити"), ("start work", "починати роботу"), ("finish work", "закінчувати роботу"),
            ("analyse data", "аналізувати дані"), ("always", "завжди"), ("usually", "зазвичай"), ("sometimes", "іноді"), ("never", "ніколи")]
JOBS = [("💻 Developer", "writes code"), ("🎨 UX/UI Designer", "draws app screens"), ("🐞 QA Engineer", "tests apps"),
        ("📊 Data Analyst", "makes charts"), ("🗂️ Project Manager", "plans tasks"), ("🤝 Recruiter", "finds new people")]
VERB = [("I ___ meetings every day.", ["go to", "do"], "go to"),
        ("I ___ messages in Slack.", ["answer", "travel"], "answer"),
        ("We ___ calls to clients.", ["make", "go"], "make"),
        ("I ___ emails to my boss.", ["write", "start"], "write"),
        ("I ___ work at 9 o’clock.", ["start", "answer"], "start"),
        ("I ___ work at 6 o’clock.", ["finish", "make"], "finish"),
        ("Designers ___ research.", ["do", "go"], "do"),
        ("Data analysts ___ data.", ["analyse", "write"], "analyse")]
S3 = [("I work. → She ___.", ["work", "works"], "works"), ("I write code. → He ___ code.", ["write", "writes"], "writes"),
      ("I start at 9. → She ___ at 9.", ["start", "starts"], "starts"), ("I go to meetings. → He ___ to meetings.", ["gos", "goes"], "goes"),
      ("I have a meeting. → She ___ a meeting.", ["haves", "has"], "has"), ("I do research. → He ___ research.", ["does", "dos"], "does"),
      ("They test apps. → Ivan ___ apps.", ["test", "tests"], "tests"), ("We answer messages. → Olena ___ messages.", ["answer", "answers"], "answers")]
BE = [("I ___ a Project Manager.", ["am", "is", "are"], "am"), ("Olena ___ a designer.", ["am", "is", "are"], "is"),
      ("We ___ developers.", ["am", "is", "are"], "are"), ("My boss ___ in the USA.", ["am", "is", "are"], "is"),
      ("They ___ in the office.", ["am", "is", "are"], "are"), ("You ___ my colleague.", ["am", "is", "are"], "are")]
NEG = [("I ___ write code.", ["don’t", "doesn’t"], "don’t"), ("She ___ travel for work.", ["don’t", "doesn’t"], "doesn’t"),
       ("We ___ work at the weekend.", ["don’t", "doesn’t"], "don’t"), ("Ivan ___ like mornings.", ["don’t", "doesn’t"], "doesn’t"),
       ("They ___ make calls.", ["don’t", "doesn’t"], "don’t"), ("My boss ___ answer emails after 6.", ["don’t", "doesn’t"], "doesn’t")]
SEN = [("I always start work at 9.", ["I always start work at 9.", "I start always work at 9."]),
       ("She never works at the weekend.", ["She works never at the weekend.", "She never works at the weekend."]),
       ("We usually have a meeting on Monday.", ["We usually have a meeting on Monday.", "Usually we have always a meeting on Monday."]),
       ("I am always busy.", ["I always am busy.", "I am always busy."]),
       ("He sometimes makes calls.", ["He sometimes makes calls.", "He makes sometimes calls."])]
MY = [("My name is", "Maryna", ".", "Моє ім’я"), ("I am a(n)", "Project Manager", ".", "Я — (професія)"),
      ("I usually start work at", "9 o’clock", ".", "Зазвичай починаю роботу о…"), ("I always", "answer messages", ".", "Я завжди…"),
      ("I often", "go to meetings", ".", "Я часто…"), ("I sometimes", "make calls", ".", "Я іноді…"),
      ("I never", "work at the weekend", ".", "Я ніколи не…"), ("I don’t", "write code", ".", "Я не…")]

def ua(s): return '<span class="ua">🇺🇦 %s</span>' % s
def sel(k, opts):
    return '<select class="g" data-k="%s"><option value="">—</option>%s</select>' % (k, "".join("<option>%s</option>" % o for o in opts))
def fb(k, n=None): return '<div class="fb" id="fb_%s">%s<span class="h"></span></div>' % (k, ("<sup>%d</sup> " % n) if n else "")
def ctl(p): return '<div class="ctl"><button class="btn" onclick="chkSet(\'%s\')">Check</button><span class="res" id="r_%s"></span></div></section>' % (p, p)

h = []
h.append('<div class="tipbox">👋 Hi! This homework is short and easy. Choose the answers, then click <b>Check</b>. Green = correct ✓<br>%s</div>'
         % ua("Привіт! Обирай відповіді та натискай <b>Check</b>. Зелене — правильно. Можна робити частинами: все зберігається автоматично."))
h.append('<section><h2><span>1</span>Words</h2><p class="ins">Match the English words with the Ukrainian words.</p>%s' % ua("З’єднай англійські слова з українськими."))
opts = sorted(u for _, u in WORDS_UA)
for i, (e, u) in enumerate(WORDS_UA):
    h.append('<div class="row"><b class="w">%s</b>%s%s</div>' % (e, sel("w_%d" % (i + 1), opts), fb("w_%d" % (i + 1))))
h.append(ctl("w"))
h.append('<section><h2><span>2</span>Jobs</h2><p class="ins">What does he or she do? Choose.</p>%s' % ua("Що робить ця людина? Обери."))
jopts = sorted(d for _, d in JOBS)
for i, (j, d) in enumerate(JOBS):
    h.append('<div class="row"><b class="w">%s</b> … %s%s</div>' % (j, sel("job_%d" % (i + 1), jopts), fb("job_%d" % (i + 1))))
h.append(ctl("job"))
def block(n, title, ins, insua, items, p):
    h.append('<section><h2><span>%d</span>%s</h2><p class="ins">%s</p>%s' % (n, title, ins, ua(insua)))
    for i, (q, ch, a) in enumerate(items):
        k = "%s_%d" % (p, i + 1)
        h.append('<div class="row big">%d. %s%s</div>' % (i + 1, q.replace("___", sel(k, ch)), fb(k)))
    h.append(ctl(p))
block(3, "Tasks", "Choose the correct verb.", "Обери правильне дієслово.", VERB, "v")
block(4, "He / she + -s", "Choose the correct word.", "Він / вона → додаємо <b>-s</b>: I work → she work<b>s</b>. Обери правильне слово.", S3, "s")
block(5, "am / is / are", "Choose am, is or are.", "I → <b>am</b> · he / she / it → <b>is</b> · we / you / they → <b>are</b>", BE, "be")
block(6, "don’t / doesn’t", "Choose don’t or doesn’t.", "I / we / you / they → <b>don’t</b> · he / she → <b>doesn’t</b> (не)", NEG, "neg")
ADV = [("always", "завжди", "100%"), ("usually", "зазвичай", "90%"), ("often", "часто", "70%"), ("sometimes", "іноді", "50%"), ("rarely", "рідко", "10%"), ("never", "ніколи", "0%")]
def blk(w, c): return '<span class="wb %s">%s</span>' % (c, w)
PICT = ('<div class="pic"><div class="pt">How often? · Як часто?</div><div class="scale2">%s</div>'
        '<div class="pt" style="margin-top:14px">Word order · Порядок слів</div>'
        '<div class="ordr"><div class="lab">1. Звичайне дієслово → adverb <b>ПЕРЕД</b> дієсловом</div>%s</div>'
        '<div class="ordr"><div class="lab">2. am / is / are → adverb <b>ПІСЛЯ</b></div>%s</div>'
        '<div class="ordr"><div class="lab">3. don’t / doesn’t → adverb <b>МІЖ</b> ними</div>%s</div>'
        '<div class="legend">%s хто · %s як часто · %s дія · %s решта</div></div>') % (
    "".join('<div class="ad" style="--w:%s"><div class="bar"><i></i></div><b>%s</b><span>%s</span><em>%s</em></div>' % (p, e, u, p) for e, u, p in ADV),
    blk("I", "s") + blk("always", "a") + blk("start", "v") + blk("work at 9.", "r") + '<br>' + blk("She", "s") + blk("often", "a") + blk("goes", "v") + blk("to meetings.", "r"),
    blk("I", "s") + blk("am", "v") + blk("always", "a") + blk("busy.", "r") + '<br>' + blk("He", "s") + blk("is", "v") + blk("never", "a") + blk("late.", "r"),
    blk("She", "s") + blk("doesn’t", "v") + blk("usually", "a") + blk("work", "v") + blk("at the weekend.", "r"),
    blk("I / she", "s"), blk("always", "a"), blk("start", "v"), blk("…", "r"))
h.append('<section><h2><span>7</span>Which sentence is correct?</h2><p class="ins">Choose the correct sentence.</p>%s' % (PICT + ua("Обери правильне речення. Слова <i>always, never, usually, sometimes</i> стоять перед дієсловом, але після <i>am / is / are</i>.")))
for i, (a, ch) in enumerate(SEN):
    k = "sen_%d" % (i + 1)
    h.append('<div class="row"><b>%d.</b>%s%s</div>' % (i + 1, "".join('<label class="opt"><input type="radio" name="sen%d" data-k="%s" value="%s"> %s</label>' % (i, k, c, c) for c in ch), fb(k)))
h.append('<div class="ctl"><button class="btn" onclick="chkRad(\'sen\')">Check</button><span class="res" id="r_sen"></span></div></section>')
h.append('<section><h2><span>8</span>About me</h2><p class="ins">Complete the sentences about you.</p>%s<div class="my">' % ua("Допиши речення про себе."))
for i, (pre, ex, post, u) in enumerate(MY):
    h.append('<div class="row">%s <input class="g" data-k="my_%d" style="width:220px">%s <span class="uah">%s</span></div>' % (pre, i + 1, post, u))
h.append('</div></section>')
body = "".join(h)

KEY = {}
for i, (e, u) in enumerate(WORDS_UA): KEY["w_%d" % (i + 1)] = [u]
for i, (j, d) in enumerate(JOBS): KEY["job_%d" % (i + 1)] = [d]
for p, items in (("v", VERB), ("s", S3), ("be", BE), ("neg", NEG)):
    for i, (q, ch, a) in enumerate(items): KEY["%s_%d" % (p, i + 1)] = [a]
for i, (a, ch) in enumerate(SEN): KEY["sen_%d" % (i + 1)] = [a]
WORDS = []

html = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>1.1 Daily tasks — Homework (easy)</title><link href="https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&display=swap" rel="stylesheet">
<style>*{box-sizing:border-box}body{margin:0;font-family:"Fira Sans",system-ui,sans-serif;font-weight:300;color:#231f20;background:#fff;font-size:17px;line-height:1.5}
header{display:flex;border-bottom:3px solid ACC}header .n{background:linear-gradient(120deg,DARK,#4f9be8);color:#fff;font-weight:500;font-size:34px;padding:10px 24px}
header h1{margin:0;align-self:center;padding-left:18px;font-weight:500;font-size:30px;color:#4d4d4f}header .tag{margin-left:auto;align-self:center;margin-right:16px;background:#f2b631;color:#3b2c00;font-weight:600;font-size:12px;padding:6px 10px;border-radius:4px}
main{max-width:960px;margin:0 auto;padding:10px 20px 40px}.top a{color:ACC;text-decoration:none;font-weight:500;font-size:15px}
.bar{background:ACC2;padding:8px 14px;border-radius:6px;margin:10px 0;font-size:15px}.st.ok{color:#2e7d4f}.st.err{color:#c0392b}
.tcom{display:none;margin-top:12px;background:#fdf0d5;border-left:4px solid #f2b631;padding:10px 14px;border-radius:4px;font-size:15px;white-space:pre-wrap}.tcom b{display:block;font-weight:600}
section{border-top:1px solid #e1e2e3;padding:6px 0 18px}h2{font-weight:500;font-size:21px;color:DARK;margin:16px 0 4px}h2 span{display:inline-block;background:ACC;color:#fff;border-radius:50%;width:30px;height:30px;text-align:center;line-height:30px;margin-right:10px;font-size:16px}
.ins{font-weight:500;margin:6px 0 10px}.hint{font-size:14px;color:#6d6e70}.hint a{color:#c2185b}
.fr{position:relative;padding-top:56.25%;max-width:720px}.fr iframe{position:absolute;inset:0;width:100%;height:100%;border:0}
.tf{display:grid;grid-template-columns:28px 1fr 52px 52px;gap:4px 8px;align-items:center;padding:7px 0;border-bottom:1px solid #f0f0f2}.tf .n{font-weight:600;color:DARK}.tf .fix{grid-column:2/5}.tf .fb{grid-column:2/5}
.row{padding:7px 0;border-bottom:1px solid #f0f0f2}.row .w{display:inline-block;min-width:150px}.br{color:#8a8b8d;font-size:15px}
input.g,select.g{font:inherit;font-size:16px;border:1.5px solid #c8c9cb;border-radius:4px;padding:4px 6px}input.fix{width:100%;font-size:15px}
.right{border-color:#3a9d5d!important;background:#eaf7ee!important}.wrong{border-color:#d9534f!important;background:#fdecec!important}
.fb{display:none;font-size:14.5px;margin-top:4px}.fb.show{display:block}.fb.ok{color:#2e7d4f}.fb.no{color:#b03a2e}
.box{border:1.5px solid #c8c9cb;padding:6px 12px;border-radius:4px;display:inline-block;margin-bottom:6px;font-size:16px}
.ctl{display:flex;gap:10px;align-items:center;margin-top:10px}.btn{background:#4d4d4f;color:#fff;border:0;border-radius:4px;padding:8px 18px;font:500 15px "Fira Sans",system-ui,sans-serif;cursor:pointer}.res{font-weight:500;color:DARK}
textarea{width:100%;min-height:170px;font:inherit;font-size:16px;border:1.5px solid #c8c9cb;border-radius:6px;padding:10px;margin-top:8px}
.chips{display:flex;flex-wrap:wrap;gap:6px}.chips span{background:#f3f4f5;border-radius:14px;padding:3px 10px;font-size:14.5px}.chips span.on{background:#d9f2e2;color:#1e6b3d}
.selfa{display:flex;margin-top:14px;border-radius:6px;overflow:hidden}.selfa .l{background:#d9746f;color:#fff;font-weight:600;padding:12px 16px}.selfa .r{flex:1;background:#f6f6f7;padding:10px 16px;font-size:15px}
.score button{width:42px;height:42px;border-radius:50%;border:2px solid #e1e2e3;background:#fff;font-size:16px;margin:6px 6px 0 0;cursor:pointer}.score button.on{border-color:ACC;background:ACC2}
.send{margin-top:18px}.done{display:none;margin-top:10px;background:#eaf7ee;color:#1e6b3d;padding:10px 14px;border-radius:6px}
.pic{border:2px solid #cfe0f6;border-radius:10px;padding:14px 18px;margin:8px 0 16px;background:#fbfdff}.pt{font-weight:600;color:DARK;margin-bottom:8px}
.scale2{display:grid;grid-template-columns:repeat(6,1fr);gap:8px}.ad{text-align:center}.ad .bar{height:70px;background:#eef3fa;border-radius:6px;position:relative;overflow:hidden}.ad .bar i{position:absolute;left:0;right:0;bottom:0;height:var(--w);background:linear-gradient(#7fb0ec,ACC)}
.ad b{display:block;font-weight:600;margin-top:4px}.ad span{display:block;font-size:13.5px;color:#6d6e70}.ad em{font-size:12.5px;color:#9a9b9d;font-style:normal}
.ordr{margin:8px 0}.ordr .lab{font-size:14.5px;color:#4d4d4f;margin-bottom:4px}.wb{display:inline-block;padding:4px 10px;margin:3px 4px 3px 0;border-radius:5px;font-size:17px}
.wb.s{background:#e8eaed}.wb.a{background:#ffe08a;font-weight:600}.wb.v{background:#cfe3fb;font-weight:500}.wb.r{background:#f3f4f5}.legend{font-size:13px;color:#6d6e70;margin-top:6px}.legend .wb{font-size:12.5px;padding:1px 6px}
@media(max-width:700px){.scale2{grid-template-columns:repeat(3,1fr)}}
.ua{display:block;color:#6d6e70;font-size:14.5px;margin:-4px 0 8px}.uah{color:#9a9b9d;font-size:13.5px;margin-left:6px}
.tipbox{background:#fff8e6;border-left:4px solid #f2b631;padding:10px 14px;border-radius:4px;margin:10px 0}.tipbox .ua{margin:4px 0 0}
.row.big{font-size:18px}.row .w{min-width:190px}label.opt{display:block;margin:4px 0 4px 22px;cursor:pointer;font-size:17.5px}.my .row{font-size:18px}
footer{max-width:960px;margin:0 auto;padding:0 20px 30px;font-size:12px;color:#77787b}</style></head><body>
<header><div class="n">1.1</div><h1>Daily tasks</h1><div class="tag">HOMEWORK</div></header>
<main><div class="top"><a href="../../../index.html">← Contents</a></div>
<div class="bar"><span class="st" id="st">Loading…</span></div><div class="tcom" id="tcom"><b>💬 Teacher’s comment</b><div id="tcomt"></div></div>
__BODY__
<div class="selfa"><div class="l">Self-assessment</div><div class="r">Can you talk about your work and your tasks? 0 = I need more practice, 5 = I know this well.<br><span class="ua">🇺🇦 Чи можеш розповісти про свою роботу? 0 — треба ще практики, 5 — знаю добре.</span>
<div class="score" id="score">__SCORE__</div><textarea class="g" data-k="q" style="min-height:60px" placeholder="Questions for your teacher (optional) / Питання до вчителя"></textarea></div></div>
<div class="send"><button class="btn" id="submit">Send to my teacher / Надіслати вчителю</button><span class="st" id="st2"></span></div>
<div class="done" id="done">✓ Your homework has been sent. You can still change your answers — they save automatically.</div></main>
<footer>Valentyna Hordiienko · Middle Learning Architect</footer>
<script>
const SB_URL="https://zuegojpfhgigsvyrnymt.supabase.co",SB_KEY="sb_publishable__Xn8xRhne9Hp2ckaXu6xCQ_MOe52bng";
const LESSON="BP A2 1.1 Daily tasks (easy)";const STUDENT_CODE="__CODE__";const KEY=__KEY__;const WORDS=__WORDS__;
const rpc=(f,b)=>fetch(SB_URL+"/rest/v1/rpc/"+f,{method:"POST",headers:{apikey:SB_KEY,"Content-Type":"application/json"},body:JSON.stringify(b)}).then(async r=>{const t=await r.text();if(!r.ok)throw new Error(t);return t?JSON.parse(t):null});
const $=id=>document.getElementById(id);let student="",timer=null,submitted=false,ready=false;
const norm=s=>(s||"").toLowerCase().replace(/[’`]/g,"'").replace(/\\s+/g," ").trim();
function collect(){const a={};document.querySelectorAll("input.g[data-k],select.g[data-k],textarea.g[data-k]").forEach(x=>a[x.dataset.k]=x.value);
 document.querySelectorAll("input[type=radio][data-k]:checked").forEach(x=>a[x.dataset.k]=x.value);const s=document.querySelector("#score .on");a.self=s?+s.dataset.v:null;return a}
function fill(a){document.querySelectorAll("input.g[data-k],select.g[data-k],textarea.g[data-k]").forEach(x=>{if(a[x.dataset.k]!=null)x.value=a[x.dataset.k]});
 document.querySelectorAll("input[type=radio][data-k]").forEach(x=>x.checked=a[x.dataset.k]===x.value);document.querySelectorAll("#score button").forEach(b=>b.classList.toggle("on",a.self!=null&&+b.dataset.v===a.self));wc()}
function scoreSet(p,a){let n=0,t=0;for(const k in KEY)if(k.startsWith(p+"_")){t++;if(KEY[k].some(x=>norm(x)===norm(a[k])))n++}return n+"/"+t}
function scores(){const a=collect();return{w:scoreSet("w",a),job:scoreSet("job",a),v:scoreSet("v",a),s:scoreSet("s",a),be:scoreSet("be",a),neg:scoreSet("neg",a),sen:scoreSet("sen",a)}}
function status(t,c=""){$("st").textContent=t;$("st").className="st "+c}
function local(){try{localStorage.setItem("hw:"+LESSON+":"+(STUDENT_CODE||"preview"),JSON.stringify(collect()))}catch(e){}}
async function save(){if(!ready)return;local();if(!STUDENT_CODE){status("Template preview — answers are not sent anywhere.");return}status("Saving…");
 try{await rpc("save_hw",{p_code:STUDENT_CODE,p_lesson:LESSON,p_answers:collect(),p_score:scores(),p_submitted:submitted});status("Saved ✓ "+new Date().toLocaleTimeString().slice(0,5),"ok")}
 catch(e){status("Not saved online — check your internet. Your answers are kept on this device.","err")}}
function later(){clearTimeout(timer);timer=setTimeout(save,1200)}
async function start(){let a=null;if(STUDENT_CODE){try{const r=await rpc("get_my_hw",{p_code:STUDENT_CODE,p_lesson:LESSON});const d=r&&r[0];
 if(d){student=d.name;if(d.answers){a=d.answers;submitted=!!d.submitted;if(submitted)$("done").style.display="block"}if(d.teacher_comment){$("tcomt").textContent=d.teacher_comment;$("tcom").style.display="block"}}}catch(e){}}
 if(!a){try{a=JSON.parse(localStorage.getItem("hw:"+LESSON+":"+(STUDENT_CODE||"preview"))||"null")}catch(e){}}if(a)fill(a);ready=true;
 if(!STUDENT_CODE)status("Template preview — answers are not sent anywhere.");else status(student?(a?"Welcome back, "+student+"! Your answers are loaded.":"Hi, "+student+"! Your answers save automatically."):"Your answers save automatically.","ok")}
function mark(el,ok,txt){el.classList.remove("right","wrong");el.classList.add(ok?"right":"wrong");const f=$("fb_"+el.dataset.k);if(!f)return;f.className="fb show "+(ok?"ok":"no");f.querySelector(".h").innerHTML=txt}
function chkSet(p){let n=0,t=0;for(const k in KEY){if(!k.startsWith(p+"_"))continue;t++;const el=document.querySelector(`[data-k="${k}"]`);const ok=KEY[k].some(x=>norm(x)===norm(el.value));if(ok)n++;
 mark(el,ok,ok?"✓ Correct!":"✗ Correct answer: <b>"+KEY[k][0]+"</b>")}$("r_"+p).textContent=n+" / "+t+(n===t?" ✓ Well done!":"");save()}
function chkTF(){let n=0,t=0;for(const k in KEY){if(!k.startsWith("tf_"))continue;t++;const sel=document.querySelector(`input[data-k="${k}"]:checked`);const v=sel?sel.value:"";const ok=v===KEY[k][0];if(ok)n++;
 const f=$("fb_"+k);f.className="fb show "+(ok?"ok":"no");f.querySelector(".h").innerHTML=(ok?"✓ ":"✗ Answer: <b>"+KEY[k][0]+"</b>. ")+KEY[k][1]}$("r_tf").textContent=n+" / "+t+(n===t?" ✓ Well done!":"");save()}
function chkRad(p){let n=0,t=0;for(const k in KEY){if(!k.startsWith(p+"_"))continue;t++;const sel=document.querySelector(`input[data-k="${k}"]:checked`);const ok=!!sel&&sel.value===KEY[k][0];if(ok)n++;
 const f=$("fb_"+k);f.className="fb show "+(ok?"ok":"no");f.querySelector(".h").innerHTML=ok?"✓ Correct!":"✗ Correct: <b>"+KEY[k][0]+"</b>"}$("r_"+p).textContent=n+" / "+t+(n===t?" ✓ Well done!":"");save()}
function wc(){}

document.querySelectorAll("#score button").forEach(b=>b.onclick=()=>{document.querySelectorAll("#score button").forEach(x=>x.classList.remove("on"));b.classList.add("on");later()});
document.addEventListener("input",e=>{if(e.target.closest("main"))later()});document.addEventListener("change",e=>{if(e.target.closest("main"))later()});
$("submit").onclick=async()=>{submitted=true;await save();$("done").style.display="block"};start();
</script></body></html>"""
html = (html.replace("__BODY__", body).replace("__SCORE__", "".join('<button data-v="%d">%d</button>' % (i, i) for i in range(6)))
        .replace("__KEY__", json.dumps(KEY, ensure_ascii=False)).replace("__WORDS__", json.dumps(WORDS)).replace("__CODE__", CODE)
        .replace("ACC2", ACC2).replace("ACC", ACC).replace("DARK", DARK))
open(OUT, "w").write(html); print("ok", len(html))
