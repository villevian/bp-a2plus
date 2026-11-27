"""Business Partner A2 · 1.1 Daily tasks (IT) — HOMEWORK, Supabase sync.
Usage: python3 build_a2_hw_1-1.py OUT.html [STUDENT_CODE]
"""
import sys, json
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK = "#3b7dd8", "#e3eefb", "#2a5fb0"
VIDS = [("RmQEETm8b1E", "Speaker 1"), ("TYds72a3klc", "Speaker 2"), ("NkVbRMJXHMU", "Speaker 3")]
TF = [("The Product Manager starts the day with the backlog.", "T", "Yes — the Product Manager checks the backlog (the list of tasks) first."),
      ("The Developer runs the daily stand-up meeting.", "F", "No — the Delivery Manager runs the stand-up."),
      ("The Delivery Manager reviews a user story.", "F", "No — the Developer reviews a user story."),
      ("The Product Manager meets stakeholders.", "T", "Yes — bosses, users and other departments."),
      ("The Developer talks about feedback from a usability test.", "T", "Yes — the Developer talks about feedback from users."),
      ("The Product Manager talks to external teams about a delay.", "F", "No — the Delivery Manager does this."),
      ("The Developer works with the Product Manager.", "T", "Yes — and the Delivery Manager works with the Product Manager too.")]
DEF = [("Developer", "writes code and builds apps"), ("UX/UI Designer", "draws app screens and makes apps easy to use"),
       ("Project Manager", "plans tasks, deadlines and people"), ("Product Manager", "decides what the team builds and why"),
       ("QA Engineer", "tests apps and finds bugs"), ("Data Analyst", "analyses numbers and makes charts"),
       ("DevOps Engineer", "looks after servers and releases"), ("Recruiter", "finds new people for the company")]
BANK = ["go to", "call", "process", "do", "make", "travel", "analyse", "write", "answer", "start"]
COLL = [("Every morning I", "answer", "messages in Slack."),
        ("Our designers", "do", "research before they draw new screens."),
        ("I often", "go to", "meetings with the product team."),
        ("The QA Engineer", "processes", "tickets in Jira every day."),
        ("We", "make", "video calls to clients in the USA."),
        ("My boss sometimes", "travels", "for work to our office in Kraków."),
        ("Data analysts", "analyse|analyze", "app data and make charts."),
        ("At the end of the month I", "write", "a report for my boss."),
        ("Our support manager", "calls", "customers when there is a problem."),
        ("We usually", "start", "work at 10 o’clock.")]
S3 = [("write", "writes"), ("go", "goes"), ("have", "has"), ("do", "does"), ("process", "processes"), ("finish", "finishes"),
      ("analyse", "analyses|analyzes"), ("test", "tests")]
T5 = [("Hi! I’m Dana. I", "be", "’m|am|'m|m", "a UX/UI Designer. My colleague Ivan"),
      (None, "be", "is|’s|'s|s", "a Developer. We"), (None, "work", "work", "in a small IT company in Kyiv. I usually"),
      (None, "start", "start", "work at 9 o’clock, but Ivan"), (None, "start", "starts", "at 11! He"),
      (None, "not like", "doesn’t like|does not like|doesnt like|doesn't like", "mornings. I"),
      (None, "not write", "don’t write|do not write|dont write|don't write", "code, I draw screens in Figma. Ivan"),
      (None, "have", "has", "a lot of meetings, so he often"), (None, "finish", "finishes", "work late.")]
ORD = [("I often start work at 10 o’clock.", ["I start often work at 10 o’clock.", "I often start work at 10 o’clock.", "Often I start always work at 10 o’clock."]),
       ("She is always busy on Mondays.", ["She always is busy on Mondays.", "She is always busy on Mondays.", "Always she busy on Mondays."]),
       ("We never have meetings on Fridays.", ["We never have meetings on Fridays.", "We have never meetings on Fridays.", "We have meetings never on Fridays."]),
       ("He doesn’t usually test the app.", ["He usually doesn’t tests the app.", "He doesn’t usually test the app.", "He doesn’t test usually the app."]),
       ("They sometimes work from home.", ["They work sometimes from home.", "They sometimes works from home.", "They sometimes work from home."]),
       ("Do you usually answer messages after work?", ["Do you usually answer messages after work?", "Do you answer usually messages after work?", "Usually do you answer messages after work?"])]
WORDS = ["always", "usually", "often", "sometimes", "never", "go to meetings", "answer messages", "make calls", "write emails", "start work", "finish work", "don’t"]

h = []
h.append('<section><h2><span>1</span>Watch the videos again</h2><p class="ins">Watch “A day in the life” again: three people from one digital team. Turn on English subtitles if you need them.</p><div class="vids">%s</div>'
         '<p class="hint">Digital Public Services Wales (YouTube) · each video 1–2 min</p></section>' % "".join(
         '<div><b>%s</b> <a class="yt" href="https://www.youtube.com/watch?v=%s" target="_blank">▶ YouTube</a><div class="fr"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0&cc_load_policy=1" allowfullscreen loading="lazy"></iframe></div></div>' % (t, y, y) for y, t in VIDS))
h.append('<section><h2><span>2</span>True or false?</h2><p class="ins">Read the sentences about the people in the videos. Choose T (true) or F (false).</p>')
for i, (q, a, ex) in enumerate(TF):
    h.append('<div class="tf"><span class="n">%d</span><span class="q">%s</span><label><input type="radio" name="tf%d" data-k="tf_%d" value="T"> T</label><label><input type="radio" name="tf%d" data-k="tf_%d" value="F"> F</label>'
             '<div class="fb" id="fb_tf_%d"><span class="h"></span></div></div>' % (i + 1, q, i, i + 1, i, i + 1, i + 1))
h.append('<div class="ctl"><button class="btn" onclick="chkTF()">Check</button><span class="res" id="r_tf"></span></div></section>')
h.append('<section><h2><span>3</span>Jobs</h2><p class="ins">What does each person do? Match the jobs with the descriptions.</p>')
opts = sorted(d for _, d in DEF)
for i, (w, d) in enumerate(DEF):
    h.append('<div class="row"><b class="w">A(n) %s …</b><select data-k="def_%d" class="g"><option value="">— choose —</option>%s</select><div class="fb" id="fb_def_%d"><span class="h"></span></div></div>'
             % (w, i + 1, "".join('<option>%s</option>' % o for o in opts), i + 1))
h.append('<div class="ctl"><button class="btn" onclick="chkSet(\'def\')">Check</button><span class="res" id="r_def"></span></div></section>')
h.append('<section><h2><span>4</span>Tasks</h2><p class="ins">Complete the sentences with the verbs from the box. Remember: he / she + verb<b>-s</b>!</p><div class="box">%s</div>' % " · ".join(BANK))
for i, (pre, a, post) in enumerate(COLL):
    h.append('<div class="row">%d. %s <input class="g" data-k="col_%d" style="width:130px"> %s<div class="fb" id="fb_col_%d"><span class="h"></span></div></div>' % (i + 1, pre, i + 1, post, i + 1))
h.append('<div class="ctl"><button class="btn" onclick="chkSet(\'col\')">Check</button><span class="res" id="r_col"></span></div></section>')
h.append('<section><h2><span>5</span>He / she + -s</h2><p class="ins">Write the he / she form. Then say it aloud: /s/, /z/ or /ɪz/?</p><div class="grid2">')
for i, (b, a) in enumerate(S3):
    h.append('<div class="row">I %s → he / she <input class="g" data-k="s3_%d" style="width:120px"><div class="fb" id="fb_s3_%d"><span class="h"></span></div></div>' % (b, i + 1, i + 1))
h.append('</div><div class="ctl"><button class="btn" onclick="chkSet(\'s3\')">Check</button><span class="res" id="r_s3"></span></div></section>')
h.append('<section><h2><span>6</span>Dana and Ivan</h2><p class="ins">Complete the text with the correct form of the verb in brackets.</p><div class="txt">')
for k, (pre, v, a, post) in enumerate(T5):
    h.append('%s<sup>%d</sup><input class="g" data-k="gr_%d" placeholder="(%s)" style="width:140px"> %s ' % ((pre + " ") if pre else "", k + 1, k + 1, v, post))
h.append('</div>%s<div class="ctl"><button class="btn" onclick="chkSet(\'gr\')">Check</button><span class="res" id="r_gr"></span></div></section>'
         % "".join('<div class="fb" id="fb_gr_%d"><sup>%d</sup> <span class="h"></span></div>' % (k + 1, k + 1) for k in range(len(T5))))
h.append('<section><h2><span>7</span>How often?</h2><p class="ins">Choose the correct sentence.</p>')
for i, (a, ch) in enumerate(ORD):
    h.append('<div class="row"><b>%d.</b>%s<div class="fb" id="fb_or_%d"><span class="h"></span></div></div>' % (i + 1, "".join('<label class="opt"><input type="radio" name="or%d" data-k="or_%d" value="%s"> %s</label>' % (i, i + 1, c, c) for c in ch), i + 1))
h.append('<div class="ctl"><button class="btn" onclick="chkRad(\'or\')">Check</button><span class="res" id="r_or"></span></div></section>')
h.append('<section><h2><span>8</span>My working day</h2><p class="ins">Write about your working day: your job, your tasks and how often you do them. Write 50–70 words. Use at least five words from the list — they turn green when you use them.</p>'
         '<p class="exm"><i>I’m a Project Manager in an IT company. I usually start work at 9 o’clock. I always answer messages in Slack first…</i></p>'
         '<div class="chips" id="chips">%s</div><textarea class="g" data-k="opinion" id="op" placeholder="I’m a(n)… I usually…"></textarea><div class="res" id="wc">0 words</div></section>' % "".join('<span data-w="%s">%s</span>' % (w, w) for w in WORDS))
body = "".join(h)

KEY = {}
for i, (q, a, ex) in enumerate(TF): KEY["tf_%d" % (i + 1)] = [a, ex]
for i, (w, d) in enumerate(DEF): KEY["def_%d" % (i + 1)] = [d]
for i, c in enumerate(COLL): KEY["col_%d" % (i + 1)] = c[1].split("|")
for i, (b, a) in enumerate(S3): KEY["s3_%d" % (i + 1)] = a.split("|")
for i, t in enumerate(T5): KEY["gr_%d" % (i + 1)] = t[2].split("|")
for i, (a, ch) in enumerate(ORD): KEY["or_%d" % (i + 1)] = [a]

html = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>1.1 Daily tasks — Homework</title><link href="https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&display=swap" rel="stylesheet">
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
.vids{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.vids .fr{margin-top:4px}a.yt{color:#c2185b;font-size:13px;text-decoration:none}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:0 30px}.txt{background:#fafbfc;border-left:4px solid ACC;padding:6px 16px;border-radius:4px;line-height:2.4}
label.opt{display:block;margin:3px 0 3px 22px;cursor:pointer}.exm{color:DARK;margin:4px 0 10px}.row .w{min-width:210px}
@media(max-width:800px){.vids,.grid2{grid-template-columns:1fr}}
footer{max-width:960px;margin:0 auto;padding:0 20px 30px;font-size:12px;color:#77787b}body.tv nav,body.tv #submit,body.tv .ctl .btn,body.tv #vkFab{display:none!important}body.tv .sec{display:block!important;border-top:3px solid #999;margin-top:26px;padding-top:6px}body.tv .sec:before{content:attr(data-tv);display:block;font:600 19px "Fira Sans",sans-serif;color:#333;margin:6px 0 4px}body.tv .model{display:block!important}body.tv input.g,body.tv select.g,body.tv textarea.g{background:#fbfbfd;color:#111;opacity:1}#tvbar{display:none}body.tv #tvbar{display:block;position:sticky;top:0;z-index:50;background:#fff7ef;border-bottom:2px solid #e8894a;padding:8px 14px;font-size:15px}</style></head><body>
<header><div class="n">1.1</div><h1>Daily tasks</h1><div class="tag">HOMEWORK</div></header>
<main><div class="top"><a href="../../../index.html">← Contents</a></div>
<div class="bar"><span class="st" id="st">Loading…</span></div><div class="tcom" id="tcom"><b>💬 Teacher’s comment</b><div id="tcomt"></div></div>
__BODY__
<div class="selfa"><div class="l">Self-assessment</div><div class="r">How well can you describe work activities and tasks? 0 = I need more practice, 5 = I know this well.
<div class="score" id="score">__SCORE__</div><textarea class="g" data-k="q" style="min-height:60px" placeholder="Questions for your teacher (optional)"></textarea></div></div>
<div class="send"><button class="btn" id="submit">Send to my teacher</button><span class="st" id="st2"></span></div>
<div class="done" id="done">✓ Your homework has been sent. You can still change your answers — they save automatically.</div></main>
<footer>Video: “A day in the life”, Digital Public Services Wales (YouTube). Valentyna Hordiienko · Middle Learning Architect</footer>
<script>
const SB_URL="https://zuegojpfhgigsvyrnymt.supabase.co",SB_KEY="sb_publishable__Xn8xRhne9Hp2ckaXu6xCQ_MOe52bng";
const LESSON="BP A2 1.1 Daily tasks";const VIEW=new URLSearchParams(location.search).has("view");const STUDENT_CODE="__CODE__";const KEY=__KEY__;const WORDS=__WORDS__;
const rpc=(f,b)=>fetch(SB_URL+"/rest/v1/rpc/"+f,{method:"POST",headers:{apikey:SB_KEY,"Content-Type":"application/json"},body:JSON.stringify(b)}).then(async r=>{const t=await r.text();if(!r.ok)throw new Error(t);return t?JSON.parse(t):null});
const $=id=>document.getElementById(id);let student="",timer=null,submitted=false,ready=false;
const norm=s=>(s||"").toLowerCase().replace(/[’`]/g,"'").replace(/\\s+/g," ").trim();
function collect(){const a={};document.querySelectorAll("input.g[data-k],select.g[data-k],textarea.g[data-k]").forEach(x=>a[x.dataset.k]=x.value);
 document.querySelectorAll("input[type=radio][data-k]:checked").forEach(x=>a[x.dataset.k]=x.value);const s=document.querySelector("#score .on");a.self=s?+s.dataset.v:null;a._sent=sentBy;return a}
function fill(a){document.querySelectorAll("input.g[data-k],select.g[data-k],textarea.g[data-k]").forEach(x=>{if(a[x.dataset.k]!=null)x.value=a[x.dataset.k]});
 document.querySelectorAll("input[type=radio][data-k]").forEach(x=>x.checked=a[x.dataset.k]===x.value);document.querySelectorAll("#score button").forEach(b=>b.classList.toggle("on",a.self!=null&&+b.dataset.v===a.self));wc()}
function scoreSet(p,a){let n=0,t=0;for(const k in KEY)if(k.startsWith(p+"_")){t++;if(KEY[k].some(x=>norm(x)===norm(a[k])))n++}return n+"/"+t}
function scores(){const a=collect();return{tf:scoreSet("tf",a),def:scoreSet("def",a),col:scoreSet("col",a),s3:scoreSet("s3",a),gr:scoreSet("gr",a),or:scoreSet("or",a),words:(a.opinion.match(/\\S+/g)||[]).length}}
function status(t,c=""){$("st").textContent=t;$("st").className="st "+c}
function local(){try{localStorage.setItem("hw:"+LESSON+":"+(STUDENT_CODE||"preview"),JSON.stringify(collect()))}catch(e){}}
async function save(){if(!ready||VIEW)return;local();if(!STUDENT_CODE){status("Template preview — answers are not sent anywhere.");return}status("Saving…");
 try{await rpc("save_hw",{p_code:STUDENT_CODE,p_lesson:LESSON,p_answers:collect(),p_score:scores(),p_submitted:submitted});status("Saved ✓ "+new Date().toLocaleTimeString().slice(0,5),"ok")}
 catch(e){status("Not saved online — check your internet. Your answers are kept on this device.","err")}}
function later(){if(VIEW)return;clearTimeout(timer);timer=setTimeout(save,1200)}
function teacherView(d){const a=d.answers||{};fill(a);document.body.classList.add("tv");
 const bar=document.createElement("div");bar.id="tvbar";bar.innerHTML="👩‍🏫 <b>Teacher view</b> · "+(d.name||"")+" · "+(d.submitted?"✓ Sent to teacher":"⏳ Not sent yet")+" · read-only, nothing is saved";document.body.prepend(bar);
 document.querySelectorAll("section.sec").forEach(sec=>{const nb=document.querySelector('nav button[data-s="'+sec.id+'"]');sec.dataset.tv="Step "+(nb?nb.textContent.trim():sec.id)});
 document.querySelectorAll(".ctl .btn[onclick]").forEach(b=>{try{(new Function(b.getAttribute("onclick")))()}catch(e){}});
 document.querySelectorAll("input.g,textarea.g").forEach(x=>x.readOnly=true);document.querySelectorAll("select.g,input[type=radio]").forEach(x=>x.disabled=true);
 if(window.afterFill)afterFill();const post=()=>parent.postMessage({tvHeight:document.documentElement.scrollHeight},"*");post();setTimeout(post,800);setTimeout(post,2500)}
async function start(){let a=null;if(VIEW){status("Teacher view");addEventListener("message",e=>{if(e.data&&e.data.tv)teacherView(e.data.tv)});parent.postMessage({tvReady:1},"*");return}if(STUDENT_CODE){try{const r=await rpc("get_my_hw",{p_code:STUDENT_CODE,p_lesson:LESSON});const d=r&&r[0];
 if(d){student=d.name;if(d.answers){a=d.answers;submitted=!!d.submitted;sentBy=a._sent||(submitted?"button":"");if(sentBy==="button")$("done").style.display="block";updSubmit()}if(d.teacher_comment){$("tcomt").textContent=d.teacher_comment;$("tcom").style.display="block"}}}catch(e){}}
 if(!a){try{a=JSON.parse(localStorage.getItem("hw:"+LESSON+":"+(STUDENT_CODE||"preview"))||"null")}catch(e){}}if(a)fill(a);ready=true;
 if(!STUDENT_CODE)status("Template preview — answers are not sent anywhere.");else status(student?(a?"Welcome back, "+student+"! Your answers are loaded.":"Hi, "+student+"! Your answers save automatically."):"Your answers save automatically.","ok")}
function mark(el,ok,txt){el.classList.remove("right","wrong");el.classList.add(ok?"right":"wrong");const f=$("fb_"+el.dataset.k);if(!f)return;f.className="fb show "+(ok?"ok":"no");f.querySelector(".h").innerHTML=txt}
function chkSet(p){let n=0,t=0;for(const k in KEY){if(!k.startsWith(p+"_"))continue;t++;const el=document.querySelector(`[data-k="${k}"]`);const ok=KEY[k].some(x=>norm(x)===norm(el.value));if(ok)n++;
 mark(el,ok,ok?"✓ Correct!":"✗ Correct answer: <b>"+KEY[k][0]+"</b>")}$("r_"+p).textContent=n+" / "+t+(n===t?" ✓ Well done!":"");save()}
function chkTF(){let n=0,t=0;for(const k in KEY){if(!k.startsWith("tf_"))continue;t++;const sel=document.querySelector(`input[data-k="${k}"]:checked`);const v=sel?sel.value:"";const ok=v===KEY[k][0];if(ok)n++;
 const f=$("fb_"+k);f.className="fb show "+(ok?"ok":"no");f.querySelector(".h").innerHTML=(ok?"✓ ":"✗ Answer: <b>"+KEY[k][0]+"</b>. ")+KEY[k][1]}$("r_tf").textContent=n+" / "+t+(n===t?" ✓ Well done!":"");save()}
function chkRad(p){let n=0,t=0;for(const k in KEY){if(!k.startsWith(p+"_"))continue;t++;const sel=document.querySelector(`input[data-k="${k}"]:checked`);const ok=!!sel&&sel.value===KEY[k][0];if(ok)n++;
 const f=$("fb_"+k);f.className="fb show "+(ok?"ok":"no");f.querySelector(".h").innerHTML=ok?"✓ Correct!":"✗ Correct: <b>"+KEY[k][0]+"</b>"}$("r_"+p).textContent=n+" / "+t+(n===t?" ✓ Well done!":"");save()}
function wc(){const v=$("op").value,n=(v.match(/\\S+/g)||[]).length;let used=0;document.querySelectorAll("#chips span").forEach(s=>{const on=norm(v).includes(norm(s.dataset.w).replace(/^be /,""));s.classList.toggle("on",on);if(on)used++});
 $("wc").textContent=n+" words (50–70) · "+used+" words from the list"+(n>=50&&n<=70&&used>=5?" ✓":"")}
$("op").addEventListener("input",wc);
document.querySelectorAll("#score button").forEach(b=>b.onclick=()=>{document.querySelectorAll("#score button").forEach(x=>x.classList.remove("on"));b.classList.add("on");later()});
document.addEventListener("input",e=>{if(e.target.closest("main"))later()});document.addEventListener("change",e=>{if(e.target.closest("main"))later()});
$("submit").onclick=async()=>{submitted=true;sentBy="button";await save();$("done").style.display="block"};
let sentBy="";
document.addEventListener("click",e=>{if(typeof VIEW!=="undefined"&&VIEW)return;const b=e.target.closest("button");if(b&&b.id!=="submit"&&b.closest("main")&&/^check/i.test(b.textContent.trim())){submitted=true;if(!sentBy)sentBy="check";later()}},true);
function updSubmit(){const s=$("submit");if(!s)return;const w=s.closest(".ctl")||s.parentElement;const secs=[...document.querySelectorAll("section.sec")];const show=secs.length<2||secs[secs.length-1].classList.contains("on");w.style.display=show?"":"none";const d=$("done");if(d)d.style.display=(show&&sentBy==="button")?"block":"none"}
document.addEventListener("click",e=>{if(e.target.closest("nav button"))setTimeout(updSubmit,0)});updSubmit();
function navH(){const n=document.querySelector("nav.stk");return (n?n.offsetHeight:0)+10}
(function(){const nb=[...document.querySelectorAll("nav button[data-s]")];if(nb.length<2)return;const nav=nb[0].closest("nav");nav.classList.add("stk");
 const st=document.createElement("style");st.textContent='nav.stk{position:sticky;top:0;z-index:40;background:rgba(255,255,255,.96);padding:8px 0;margin-top:4px;border-bottom:1px solid #eee}nav button.dn{background:#e8f6ec;border-color:#3a9d5d;color:#1e6b3d}nav button.dn:after{content:" ✓";font-size:13px}nav button.on.dn{background:#3a9d5d;color:#fff}nav button.opt{border-style:dashed}nav button.opt:before{content:"★";font-size:12px;margin-right:2px}@media(max-width:640px){nav.stk{flex-wrap:nowrap;overflow-x:auto;gap:6px;padding:6px 0;-webkit-overflow-scrolling:touch}nav.stk button{flex:0 0 auto;min-width:40px;height:40px;padding:0 8px;font-size:15px}}';document.head.appendChild(st);
 nb.forEach(b=>{const s=document.getElementById(b.dataset.s);if(!s)return;const h=s.querySelector(".bsec .sub,.bsec,h2,h3,.ins");let t=h?h.textContent.replace(/\s+/g," ").trim():"";t=t.replace(/^Before class\s*/,"");if(t.length>70)t=t.slice(0,68)+"…";b.title=t;if(/★|optional|Advanced option/i.test((s.querySelector(".bsec")||{}).textContent||"")||/★/.test(b.textContent))b.classList.add("opt")});
 window.navUpd=function(){nb.forEach(b=>{const s=document.getElementById(b.dataset.s);if(!s)return;const f=[...s.querySelectorAll("input.g,select.g,textarea.g")];const rg={};s.querySelectorAll("input[type=radio][data-k]").forEach(r=>{rg[r.dataset.k]=rg[r.dataset.k]||r.checked});
  const tot=f.length+Object.keys(rg).length;const fill=f.filter(x=>String(x.value||"").trim()).length+Object.values(rg).filter(Boolean).length;b.classList.toggle("dn",tot>0&&fill>=tot)})};
 document.addEventListener("input",()=>navUpd());document.addEventListener("change",()=>navUpd());[600,1500,3500].forEach(t=>setTimeout(navUpd,t))})();
function goStep(b){if(!b)return;b.click();setTimeout(()=>{const s=document.querySelector("section.sec.on");if(s){const y=s.getBoundingClientRect().top+scrollY-navH();scrollTo({top:Math.max(0,y),behavior:"smooth"})}},30)}
(function(){const nb=[...document.querySelectorAll("nav button[data-s]")];if(nb.length<2)return;
 const byLabel=l=>nb.find(b=>b.textContent.replace(/[^0-9A-Za-z★–-]/g,"").toLowerCase()===String(l).toLowerCase());
 nb.forEach((b,i)=>{const sec=document.getElementById(b.dataset.s);if(!sec)return;
  sec.querySelectorAll("p,div,span,em,i").forEach(el=>{if(el.children.length>3)return;const m=(el.textContent||"").match(/(?:→|->)\s*Step\s*([0-9]+)/i);if(!m||el.dataset.nx)return;const t=byLabel(m[1]);if(!t)return;el.dataset.nx=1;el.style.cursor="pointer";el.style.color="var(--nxc,#2a5fb0)";el.style.textDecoration="underline";el.onclick=()=>goStep(t)});
  if(i<nb.length-1&&!sec.querySelector(".nextbar")){const n=nb[i+1];const d=document.createElement("div");d.className="nextbar";d.style.cssText="margin:28px 0 6px;text-align:right";
   const x=document.createElement("button");x.className="btn";x.type="button";x.style.cssText="font-size:17px;padding:10px 22px;min-height:44px";x.textContent="Next step → "+n.textContent.trim();x.onclick=()=>goStep(n);d.appendChild(x);sec.appendChild(d)}});
 nb.forEach(b=>b.addEventListener("click",e=>{if(e.isTrusted)setTimeout(()=>{const s=document.querySelector("section.sec.on");if(s)scrollTo({top:Math.max(0,s.getBoundingClientRect().top+scrollY-navH())})},0)}));
 const st=document.createElement("style");st.textContent="body.tv .nextbar{display:none}";document.head.appendChild(st)})();
(function(){if(typeof VIEW!=="undefined"&&VIEW)return;
 const pref=k=>k.replace(/_[^_]+$/,"");
 const hist=()=>{let h=document.querySelector('textarea[data-k="_hist"]');if(!h){h=document.createElement("textarea");h.className="g";h.dataset.k="_hist";h.style.display="none";document.body.appendChild(h)}return h};
 document.querySelectorAll(".ctl").forEach(ctl=>{const b=[...ctl.querySelectorAll("button[onclick]")].find(x=>/chk[A-Za-z]*\(\s*'[^']+'/.test(x.getAttribute("onclick")));if(!b||ctl.querySelector(".redo"))return;
  const p=b.getAttribute("onclick").match(/chk[A-Za-z]*\(\s*'([^']+)'/)[1];
  const r=document.createElement("button");r.type="button";r.className="btn l redo";r.style.cssText="margin-left:8px;min-height:40px";r.textContent="↺ Try again";r.title="Clear your answers in this exercise and do it again";
  let armed=0,tm=null;r.onclick=()=>{if(!armed){armed=1;r.textContent="Clear answers? Tap again";clearTimeout(tm);tm=setTimeout(()=>{armed=0;r.textContent="↺ Try again"},3500);return}
   armed=0;r.textContent="↺ Try again";const els=[...document.querySelectorAll("[data-k]")].filter(e=>e.dataset.k!=="_hist"&&pref(e.dataset.k)===p);const old={};
   els.forEach(e=>{if(e.type==="radio"){if(e.checked)old[e.dataset.k]=e.value;e.checked=false}else{if(e.value)old[e.dataset.k]=e.value;if(e.tagName==="SELECT")e.selectedIndex=0;else e.value=""}e.classList.remove("right","wrong");const f=document.getElementById("fb_"+e.dataset.k);if(f){f.innerHTML="";f.className=f.className.replace(/\\b(show|ok|no)\\b/g,"").trim()}});
   if(Object.keys(old).length){const h=hist();let a=[];try{a=JSON.parse(h.value||"[]")}catch(e){}a.push({ex:p,at:new Date().toISOString(),answers:old});h.value=JSON.stringify(a)}
   const res=document.getElementById("r_"+p);if(res)res.textContent="";if(typeof ECT!=="undefined")Object.keys(ECT).forEach(k=>{if(pref(k)===p)delete ECT[k]});
   if(typeof navUpd==="function")navUpd();const first=els.find(e=>e.type!=="radio");if(first)first.focus();if(typeof later==="function")later()};
  b.after(r)})})();
start();
</script></body></html>"""
html = (html.replace("__BODY__", body).replace("__SCORE__", "".join('<button data-v="%d">%d</button>' % (i, i) for i in range(6)))
        .replace("__KEY__", json.dumps(KEY, ensure_ascii=False)).replace("__WORDS__", json.dumps(WORDS)).replace("__CODE__", CODE)
        .replace("ACC2", ACC2).replace("ACC", ACC).replace("DARK", DARK))
open(OUT, "w").write(html); print("ok", len(html))
