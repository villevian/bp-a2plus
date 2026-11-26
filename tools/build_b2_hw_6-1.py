"""Business Partner B2 · 6.1 Ethical choices — HOMEWORK (video + vocabulary), Supabase sync.
Usage: python3 build_b2_hw_6-1.py OUT.html [STUDENT_CODE]
"""
import sys, json
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK = "#5b5fc7", "#e8e9fa", "#4044a8"
VID = "aYLbCitY_0k"

TF = [("Guangzhou has about 50,000 clothes-related businesses.", "T", "Yes — ‘some 50,000 clothes-related businesses’ (0:58)."),
      ("Shein runs most of the factories in Guangzhou itself.", "F", "Not one of these factories is run by Shein. It uses independent workshops (1:17)."),
      ("Shein adds more than 6,000 new clothing items a day.", "T", "Yes — more than 6,000 new items a day (1:24)."),
      ("Small factories usually produce orders of 1,000 pieces or more.", "F", "They produce small orders of 50 to 100 pieces (2:13)."),
      ("Items that sell well are reordered immediately.", "T", "Yes — the on-demand model (2:05)."),
      ("When a product goes viral, competition between factories pushes prices up.", "F", "Competition drives prices down, and margins get thinner (2:33)."),
      ("Some workers are paid as little as 6 to 24 cents per item.", "T", "Yes — according to China Labor Watch (2:50)."),
      ("In busy periods, some workers earn more than €1,600 a month.", "T", "Yes — but only by working late into the night (2:59)."),
      ("Shein allows its suppliers’ workers to work up to 75 hours a week.", "F", "Shein’s limit is 60 hours with one day off; some workers do more than 75 (3:26)."),
      ("The expert from Redress says that only the factories are to blame.", "F", "She says responsibility is shared: consumers in the West drive the demand (5:01)."),
      ("Shein says its on-demand model helps to limit waste.", "T", "Yes — Shein’s statement (5:21).")]
DEF = [("garment", "a piece of clothing"), ("supplier", "a company that makes goods for a brand"), ("on-demand model", "producing only what customers are buying now"),
       ("profit margin", "the part of the price that is profit"), ("paid per piece", "getting money for each item you make, not for your hours"),
       ("labour law", "rules about working hours, pay and workers’ rights"), ("disposability", "the idea that things are so cheap you can just throw them away"),
       ("polluter", "a company that damages the environment")]
BANK = ["tough conditions", "low pay", "unethical conduct", "ethically sourced", "fair-trade cotton", "sweatshops", "supply chain", "clothing brands"]
COLL = [("Workers in the video sew for twelve hours a day in", "tough conditions", "."),
        ("Many garment workers get very", "low pay", ", so they work until midnight."),
        ("The company apologised for its", "unethical conduct", "and promised to change."),
        ("Our new T-shirts are made from 100%", "fair-trade cotton", "bought directly from farmers."),
        ("Factories with very long hours and bad conditions are often called", "sweatshops", "."),
        ("Shein doesn’t publish the names of the factories in its", "supply chain", "."),
        ("Big", "clothing brands", "like Zara and H&M now publish lists of their suppliers."),
        ("We only use materials that are", "ethically sourced", "— we know where they come from.")]
PREP = [("Several shopping apps have been accused ___ using fake discounts.", ["of", "for", "about"], "of"),
        ("Most users are not aware ___ the tricks that apps use.", ["about", "of", "on"], "of"),
        ("Who is responsible ___ the design decisions in your team?", ["of", "for", "to"], "for"),
        ("Consumer groups campaigned ___ dark patterns in 2025.", ["against", "for", "with"], "against"),
        ("Endless scroll has a big impact ___ how long we stay in an app.", ["to", "in", "on"], "on"),
        ("The platform must take responsibility ___ illegal products.", ["of", "for", "about"], "for"),
        ("If you look ___ the whole industry, the problem is the same everywhere.", ["across", "through", "over"], "across")]
WF = [("ethics", "Is it ___ to use a countdown timer that is not true?", "unethical", "unethical"),
      ("ethics", "All our cotton is ___ sourced.", "ethically", "ethically"),
      ("responsible", "Users want brands to take ___ for their supply chains.", "responsibility", "responsibility"),
      ("responsible", "Selling unsafe toys is completely ___.", "irresponsible", "irresponsible"),
      ("addict", "The app is designed to be ___: people open it 20 times a day.", "addictive", "addictive"),
      ("transparent", "Shoppers ask for more ___ about where clothes are made.", "transparency", "transparency"),
      ("sustain", "Is ultra-fast fashion ever ___?", "sustainable", "sustainable")]
WORDS = ["dark patterns", "tough conditions", "low pay", "paid per piece", "supply chain", "be responsible for", "take responsibility for", "be aware of",
         "ethically sourced", "unethical conduct", "disposability", "on-demand model"]

def esc(s): return s.replace("<", "&lt;")
h = []
h.append('<section><h2><span>1</span>Watch the video again</h2><p class="ins">Watch the FRANCE 24 report once more. Turn on English subtitles if you need them.</p>'
         '<div class="fr"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0&cc_load_policy=1" allowfullscreen loading="lazy"></iframe></div>'
         '<p class="hint"><a href="https://www.youtube.com/watch?v=%s" target="_blank">▶ open on YouTube</a> · Inside the Chinese factories of fast-fashion giant Shein · FRANCE 24 English · 6:10</p></section>' % (VID, VID))
h.append('<section><h2><span>2</span>True or false?</h2><p class="ins">Choose T or F. If a sentence is false, write the correct information.</p>')
for i, (q, a, ex) in enumerate(TF):
    h.append('<div class="tf"><span class="n">%d</span><span class="q">%s</span><label><input type="radio" name="tf%d" data-k="tf_%d" value="T"> T</label><label><input type="radio" name="tf%d" data-k="tf_%d" value="F"> F</label>'
             '<input class="g fix" data-k="tfx_%d" placeholder="If F: correct it…"><div class="fb" id="fb_tf_%d"><span class="h"></span></div></div>' % (i + 1, q, i, i + 1, i, i + 1, i + 1, i + 1))
h.append('<div class="ctl"><button class="btn" onclick="chkTF()">Check</button><span class="res" id="r_tf"></span></div></section>')
h.append('<section><h2><span>3</span>Words from the video</h2><p class="ins">Match the words with the meanings.</p>')
opts = sorted(d for _, d in DEF)
for i, (w, d) in enumerate(DEF):
    h.append('<div class="row"><b class="w">%s</b><select data-k="def_%d" class="g"><option value="">— meaning —</option>%s</select><div class="fb" id="fb_def_%d"><span class="h"></span></div></div>'
             % (w, i + 1, "".join('<option>%s</option>' % o for o in opts), i + 1))
h.append('<div class="ctl"><button class="btn" onclick="chkSet(\'def\')">Check</button><span class="res" id="r_def"></span></div></section>')
h.append('<section><h2><span>4</span>Collocations</h2><p class="ins">Complete the sentences with the collocations from the box.</p><div class="box">%s</div>' % " · ".join(BANK))
for i, (pre, a, post) in enumerate(COLL):
    h.append('<div class="row">%d. %s <input class="g" data-k="col_%d" style="width:190px"> %s<div class="fb" id="fb_col_%d"><span class="h"></span></div></div>' % (i + 1, pre, i + 1, post, i + 1))
h.append('<div class="ctl"><button class="btn" onclick="chkSet(\'col\')">Check</button><span class="res" id="r_col"></span></div></section>')
h.append('<section><h2><span>5</span>Verbs with prepositions</h2><p class="ins">Choose the correct preposition.</p>')
for i, (q, ch, a) in enumerate(PREP):
    sel = '<select class="g" data-k="pr_%d"><option value="">—</option>%s</select>' % (i + 1, "".join("<option>%s</option>" % c for c in ch))
    h.append('<div class="row">%d. %s<div class="fb" id="fb_pr_%d"><span class="h"></span></div></div>' % (i + 1, q.replace("___", sel), i + 1))
h.append('<div class="ctl"><button class="btn" onclick="chkSet(\'pr\')">Check</button><span class="res" id="r_pr"></span></div></section>')
h.append('<section><h2><span>6</span>Word building</h2><p class="ins">Complete the sentences with the correct form of the word in brackets.</p>')
for i, (base, q, a, _) in enumerate(WF):
    h.append('<div class="row">%d. %s <span class="br">(%s)</span><div class="fb" id="fb_wf_%d"><span class="h"></span></div></div>' % (i + 1, q.replace("___", '<input class="g" data-k="wf_%d" style="width:150px">' % (i + 1)), base, i + 1))
h.append('<div class="ctl"><button class="btn" onclick="chkSet(\'wf\')">Check</button><span class="res" id="r_wf"></span></div></section>')
h.append('<section><h2><span>7</span>Your opinion</h2><p class="ins">Would you work as a designer, developer or product manager for an ultra-fast fashion app? Why / Why not? Write 80–100 words. Use at least five words from the list — they turn green when you use them.</p>'
         '<div class="chips" id="chips">%s</div><textarea class="g" data-k="opinion" id="op" placeholder="I would / wouldn’t work for… because…"></textarea><div class="res" id="wc">0 words</div></section>' % "".join('<span data-w="%s">%s</span>' % (w, w) for w in WORDS))
body = "".join(h)

KEY = {}
for i, (q, a, ex) in enumerate(TF): KEY["tf_%d" % (i + 1)] = [a, ex]
for i, (w, d) in enumerate(DEF): KEY["def_%d" % (i + 1)] = [d]
for i, (pre, a, post) in enumerate(COLL): KEY["col_%d" % (i + 1)] = [a]
for i, (q, ch, a) in enumerate(PREP): KEY["pr_%d" % (i + 1)] = [a]
for i, (b, q, a, alt) in enumerate(WF): KEY["wf_%d" % (i + 1)] = [a]

html = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>6.1 Ethical choices — Homework</title><link href="https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&display=swap" rel="stylesheet">
<style>*{box-sizing:border-box}body{margin:0;font-family:"Fira Sans",system-ui,sans-serif;font-weight:300;color:#231f20;background:#fff;font-size:17px;line-height:1.5}
header{display:flex;border-bottom:3px solid ACC}header .n{background:linear-gradient(120deg,DARK,#7b7fe0);color:#fff;font-weight:500;font-size:34px;padding:10px 24px}
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
footer{max-width:960px;margin:0 auto;padding:0 20px 30px;font-size:12px;color:#77787b}body.tv nav,body.tv #submit,body.tv .ctl .btn,body.tv #vkFab{display:none!important}body.tv .sec{display:block!important;border-top:3px solid #999;margin-top:26px;padding-top:6px}body.tv .sec:before{content:attr(data-tv);display:block;font:600 19px "Fira Sans",sans-serif;color:#333;margin:6px 0 4px}body.tv .model{display:block!important}body.tv input.g,body.tv select.g,body.tv textarea.g{background:#fbfbfd;color:#111;opacity:1}#tvbar{display:none}body.tv #tvbar{display:block;position:sticky;top:0;z-index:50;background:#fff7ef;border-bottom:2px solid #e8894a;padding:8px 14px;font-size:15px}</style></head><body>
<header><div class="n">6.1</div><h1>Ethical choices</h1><div class="tag">HOMEWORK</div></header>
<main><div class="top"><a href="../../../index.html">← Contents</a></div>
<div class="bar"><span class="st" id="st">Loading…</span></div><div class="tcom" id="tcom"><b>💬 Teacher’s comment</b><div id="tcomt"></div></div>
__BODY__
<div class="selfa"><div class="l">Self-assessment</div><div class="r">How well can you use language related to ethics in business? 0 = I need more practice, 5 = I know this well.
<div class="score" id="score">__SCORE__</div><textarea class="g" data-k="q" style="min-height:60px" placeholder="Questions for your teacher (optional)"></textarea></div></div>
<div class="send"><button class="btn" id="submit">Send to my teacher</button><span class="st" id="st2"></span></div>
<div class="done" id="done">✓ Your homework has been sent. You can still change your answers — they save automatically.</div></main>
<footer>Video: FRANCE 24 English (YouTube, 03.02.2026). Valentyna Hordiienko · Middle Learning Architect</footer>
<script>
const SB_URL="https://zuegojpfhgigsvyrnymt.supabase.co",SB_KEY="sb_publishable__Xn8xRhne9Hp2ckaXu6xCQ_MOe52bng";
const LESSON="BP B2 6.1 Ethical choices";const VIEW=new URLSearchParams(location.search).has("view");const STUDENT_CODE="__CODE__";const KEY=__KEY__;const WORDS=__WORDS__;
const rpc=(f,b)=>fetch(SB_URL+"/rest/v1/rpc/"+f,{method:"POST",headers:{apikey:SB_KEY,"Content-Type":"application/json"},body:JSON.stringify(b)}).then(async r=>{const t=await r.text();if(!r.ok)throw new Error(t);return t?JSON.parse(t):null});
const $=id=>document.getElementById(id);let student="",timer=null,submitted=false,ready=false;
const norm=s=>(s||"").toLowerCase().replace(/[’`]/g,"'").replace(/\\s+/g," ").trim();
function collect(){const a={};document.querySelectorAll("input.g[data-k],select.g[data-k],textarea.g[data-k]").forEach(x=>a[x.dataset.k]=x.value);
 document.querySelectorAll("input[type=radio][data-k]:checked").forEach(x=>a[x.dataset.k]=x.value);const s=document.querySelector("#score .on");a.self=s?+s.dataset.v:null;a._sent=sentBy;return a}
function fill(a){document.querySelectorAll("input.g[data-k],select.g[data-k],textarea.g[data-k]").forEach(x=>{if(a[x.dataset.k]!=null)x.value=a[x.dataset.k]});
 document.querySelectorAll("input[type=radio][data-k]").forEach(x=>x.checked=a[x.dataset.k]===x.value);document.querySelectorAll("#score button").forEach(b=>b.classList.toggle("on",a.self!=null&&+b.dataset.v===a.self));wc()}
function scoreSet(p,a){let n=0,t=0;for(const k in KEY)if(k.startsWith(p+"_")){t++;if(norm(a[k])===norm(KEY[k][0]))n++}return n+"/"+t}
function scores(){const a=collect();return{tf:scoreSet("tf",a),def:scoreSet("def",a),col:scoreSet("col",a),pr:scoreSet("pr",a),wf:scoreSet("wf",a),words:(a.opinion.match(/\\S+/g)||[]).length}}
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
function chkSet(p){let n=0,t=0;for(const k in KEY){if(!k.startsWith(p+"_"))continue;t++;const el=document.querySelector(`[data-k="${k}"]`);const ok=norm(el.value)===norm(KEY[k][0]);if(ok)n++;
 mark(el,ok,ok?"✓ Correct!":"✗ Correct answer: <b>"+KEY[k][0]+"</b>")}$("r_"+p).textContent=n+" / "+t+(n===t?" ✓ Well done!":"");save()}
function chkTF(){let n=0,t=0;for(const k in KEY){if(!k.startsWith("tf_"))continue;t++;const sel=document.querySelector(`input[data-k="${k}"]:checked`);const v=sel?sel.value:"";const ok=v===KEY[k][0];if(ok)n++;
 const f=$("fb_"+k);f.className="fb show "+(ok?"ok":"no");f.querySelector(".h").innerHTML=(ok?"✓ ":"✗ Answer: <b>"+KEY[k][0]+"</b>. ")+KEY[k][1]}$("r_tf").textContent=n+" / "+t+(n===t?" ✓ Well done!":"");save()}
function wc(){const v=$("op").value,n=(v.match(/\\S+/g)||[]).length;let used=0;document.querySelectorAll("#chips span").forEach(s=>{const on=norm(v).includes(norm(s.dataset.w).replace(/^be /,""));s.classList.toggle("on",on);if(on)used++});
 $("wc").textContent=n+" words (80–100) · "+used+" words from the list"+(n>=80&&n<=100&&used>=5?" ✓":"")}
$("op").addEventListener("input",wc);
document.querySelectorAll("#score button").forEach(b=>b.onclick=()=>{document.querySelectorAll("#score button").forEach(x=>x.classList.remove("on"));b.classList.add("on");later()});
document.addEventListener("input",e=>{if(e.target.closest("main"))later()});document.addEventListener("change",e=>{if(e.target.closest("main"))later()});
$("submit").onclick=async()=>{submitted=true;sentBy="button";await save();$("done").style.display="block"};
let sentBy="";
document.addEventListener("click",e=>{if(typeof VIEW!=="undefined"&&VIEW)return;const b=e.target.closest("button");if(b&&b.id!=="submit"&&b.closest("main")&&/^check/i.test(b.textContent.trim())){submitted=true;if(!sentBy)sentBy="check";later()}},true);
function updSubmit(){const s=$("submit");if(!s)return;const w=s.closest(".ctl")||s.parentElement;const secs=[...document.querySelectorAll("section.sec")];const show=secs.length<2||secs[secs.length-1].classList.contains("on");w.style.display=show?"":"none";const d=$("done");if(d)d.style.display=(show&&sentBy==="button")?"block":"none"}
document.addEventListener("click",e=>{if(e.target.closest("nav button"))setTimeout(updSubmit,0)});updSubmit();
function goStep(b){if(!b)return;b.click();setTimeout(()=>{const s=document.querySelector("section.sec.on");if(s){const y=s.getBoundingClientRect().top+scrollY-10;scrollTo({top:Math.max(0,y),behavior:"smooth"})}},30)}
(function(){const nb=[...document.querySelectorAll("nav button[data-s]")];if(nb.length<2)return;
 const byLabel=l=>nb.find(b=>b.textContent.replace(/[^0-9A-Za-z★–-]/g,"").toLowerCase()===String(l).toLowerCase());
 nb.forEach((b,i)=>{const sec=document.getElementById(b.dataset.s);if(!sec)return;
  sec.querySelectorAll("p,div,span,em,i").forEach(el=>{if(el.children.length>3)return;const m=(el.textContent||"").match(/(?:→|->)\s*Step\s*([0-9]+)/i);if(!m||el.dataset.nx)return;const t=byLabel(m[1]);if(!t)return;el.dataset.nx=1;el.style.cursor="pointer";el.style.color="var(--nxc,#2a5fb0)";el.style.textDecoration="underline";el.onclick=()=>goStep(t)});
  if(i<nb.length-1&&!sec.querySelector(".nextbar")){const n=nb[i+1];const d=document.createElement("div");d.className="nextbar";d.style.cssText="margin:28px 0 6px;text-align:right";
   const x=document.createElement("button");x.className="btn";x.type="button";x.style.cssText="font-size:17px;padding:10px 22px;min-height:44px";x.textContent="Next step → "+n.textContent.trim();x.onclick=()=>goStep(n);d.appendChild(x);sec.appendChild(d)}});
 nb.forEach(b=>b.addEventListener("click",e=>{if(e.isTrusted)setTimeout(()=>{const s=document.querySelector("section.sec.on");if(s)scrollTo({top:Math.max(0,s.getBoundingClientRect().top+scrollY-10)})},0)}));
 const st=document.createElement("style");st.textContent="body.tv .nextbar{display:none}";document.head.appendChild(st)})();
start();
</script></body></html>"""
html = (html.replace("__BODY__", body).replace("__SCORE__", "".join('<button data-v="%d">%d</button>' % (i, i) for i in range(6)))
        .replace("__KEY__", json.dumps(KEY, ensure_ascii=False)).replace("__WORDS__", json.dumps(WORDS)).replace("__CODE__", CODE)
        .replace("ACC2", ACC2).replace("ACC", ACC).replace("DARK", DARK))
open(OUT, "w").write(html); print("ok", len(html))
