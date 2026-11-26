"""Shared shell for synced Business Partner pages (lesson / extra / hw) with one-task-per-screen navigation.
page(...) returns full HTML. Every answer field carries data-k; KEY maps data-k -> list of accepted answers.
Check helpers in the page: chkSet(prefix) for inputs/selects, chkRad(prefix) for radio groups, model(id) toggles a model answer.
"""
import json

def page(num, title, tag, outcome, lesson_key, code, sections, key, vocab=None, acc="#e8894a", acc2="#fbeadb", dark="#c4642a", grad2="#f2a66e", footer="", extra_js=""):
    nav = "".join('<button data-s="s%d"%s>%s</button>' % (i + 1, ' class="on"' if i == 0 else "", lab) for i, (lab, _) in enumerate(sections))
    body = "".join('<section id="s%d" class="sec%s">%s</section>' % (i + 1, " on" if i == 0 else "", html) for i, (_, html) in enumerate(sections))
    voc = ""
    if vocab:
        voc = '<details class="voc" open><summary>📖 Vocabulary of this lesson — click to hide / show</summary><div class="vgs">%s</div></details>' % "".join(
            '<div class="vg"><h4>%s</h4>%s</div>' % (t, "".join(('<span>%s <em class="tr">— %s</em></span>' % w) if isinstance(w, tuple) else "<span>%s</span>" % w for w in ws)) for t, ws in vocab)
    h = TPL
    for a, b in (("__NUM__", num), ("__TITLE__", title), ("__TAG__", tag), ("__OUT__", outcome), ("__VOC__", voc), ("__NAV__", nav), ("__BODY__", body),
                 ("__FOOT__", footer), ("__LESSON__", lesson_key), ("__CODE__", code), ("__KEY__", json.dumps(key, ensure_ascii=False)), ("__XJS__", extra_js)):
        h = h.replace(a, b)
    return h.replace("ACC2", acc2).replace("GRAD2", grad2).replace("ACC", acc).replace("DARK", dark)

TPL = r"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>__NUM__ __TITLE__ — __TAG__</title><link href="https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&display=swap" rel="stylesheet">
<style>*{box-sizing:border-box}body{margin:0;font-family:"Fira Sans",system-ui,sans-serif;font-weight:300;color:#231f20;background:#fff;font-size:17px;line-height:1.5}
header{display:flex;border-bottom:3px solid ACC}header .n{background:linear-gradient(120deg,DARK,GRAD2);color:#fff;font-weight:500;font-size:34px;padding:10px 24px}
header h1{margin:0;align-self:center;padding-left:18px;font-weight:500;font-size:30px;color:#4d4d4f}header .tag{margin-left:auto;align-self:center;margin-right:16px;background:ACC;color:#fff;font-weight:600;font-size:12px;padding:6px 10px;border-radius:4px}
.out1{display:flex;align-items:center;gap:14px;background:#e6e7e8;padding:8px 22px;font-size:15px}.out1 b{background:ACC;color:#fff;font-weight:600;padding:3px 10px;border-radius:3px;font-size:13px}
.wrap{max-width:1000px;margin:0 auto;padding:0 20px}
details.voc{margin:12px 0 0;border:1.5px solid ACC;border-radius:6px}details.voc summary{cursor:pointer;padding:8px 16px;color:DARK;font-weight:500}
.vgs{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;padding:6px 16px 14px}.vg h4{margin:4px 0 6px;color:DARK;font-weight:600;font-size:14px;text-transform:uppercase}.vg em.tr{font-style:normal;color:#77787b;font-size:13px}.vg span{display:inline-block;background:ACC2;border-radius:12px;padding:2px 10px;margin:2px;font-size:14px}
.top{display:flex;justify-content:space-between;align-items:center;margin-top:10px;flex-wrap:wrap;gap:8px}.top a{color:DARK;text-decoration:none;font-weight:500;font-size:15px}
.bar{background:ACC2;padding:6px 14px;border-radius:6px;font-size:14.5px}.st.ok{color:#2e7d4f}.st.err{color:#c0392b}
.tcom{display:none;margin-top:10px;background:#fdf0d5;border-left:4px solid #f2b631;padding:10px 14px;border-radius:4px;font-size:15px;white-space:pre-wrap}.tcom b{display:block;font-weight:600}
nav{margin:12px 0 0;display:flex;flex-wrap:wrap;gap:8px}nav button{min-width:46px;height:40px;border:1.5px solid ACC;background:#fff;color:DARK;border-radius:20px;font:500 16px "Fira Sans",system-ui,sans-serif;cursor:pointer;padding:0 12px}nav button.on{background:ACC;color:#fff}
main{padding:4px 0 30px}.sec{display:none}.sec.on{display:block}body.tv nav,body.tv #submit,body.tv .ctl .btn,body.tv #vkFab{display:none!important}body.tv .sec{display:block!important;border-top:3px solid ACC;margin-top:26px;padding-top:6px}body.tv .sec:before{content:attr(data-tv);display:block;font:600 19px "Fira Sans",sans-serif;color:DARK;margin:6px 0 4px}body.tv .model{display:block!important}body.tv input.g,body.tv select.g,body.tv textarea.g{background:#fbfbfd;color:#111;opacity:1}#tvbar{display:none}body.tv #tvbar{display:block;position:sticky;top:0;z-index:50;background:#fff7ef;border-bottom:2px solid #e8894a;padding:8px 14px;font-size:15px}
.bsec{font-weight:600;color:#8a8b8d;font-size:24px;margin:18px 0 8px}.bsec .sub{color:#231f20;font-weight:500;font-size:20px;margin-left:10px}.bsec.wr{color:#fff;background:ACC;display:inline-block;padding:2px 14px;border-radius:4px}
.ins{font-weight:500;margin:16px 0 8px}.ins b.x{color:ACC;font-size:21px;margin-right:6px}.ins .q{color:DARK;margin-right:6px}
.chips{display:flex;gap:8px;flex-wrap:wrap;margin:6px 0}.chips span{border:1.5px solid #c8c9cb;border-radius:6px;padding:3px 14px;font-weight:500}
.row{padding:7px 0;border-bottom:1px solid #f0f0f2}.row .w{display:inline-block;min-width:44px;font-weight:600;color:DARK}
input.g,select.g{max-width:100%;font:inherit;font-size:16px;border:1.5px solid #c8c9cb;border-radius:4px;padding:4px 6px;background:#fff}textarea.g{width:100%;min-height:90px;font:inherit;font-size:16px;border:1.5px solid #c8c9cb;border-radius:6px;padding:8px 10px}
.right{border-color:#3a9d5d!important;background:#eaf7ee!important}.wrong{border-color:#d9534f!important;background:#fdecec!important}
.fb{display:none;font-size:14.5px;margin-top:3px}.fb.show{display:block}.fb.ok{color:#2e7d4f}.fb.no{color:#b03a2e}
.ctl{display:flex;gap:10px;align-items:center;margin-top:12px;flex-wrap:wrap}.btn{background:#4d4d4f;color:#fff;border:0;border-radius:4px;padding:8px 18px;font:500 15px "Fira Sans",system-ui,sans-serif;cursor:pointer}.btn.l{background:#fff;color:#4d4d4f;border:1.5px solid #c8c9cb}.res{font-weight:500;color:DARK}
.model{display:none;background:#f6f6f7;border-left:4px solid #8a8b8d;padding:8px 14px;margin-top:8px;font-size:15.5px;white-space:pre-wrap}.model.show{display:block}
.art{background:#f9e3d3;padding:16px 22px;border-radius:4px;columns:2;column-gap:30px;font-size:16px}.art h3{column-span:all;font-family:Georgia,serif;font-size:28px;margin:0}.art .sub2{column-span:all;font-weight:600;font-size:14px;margin:0 0 10px}.art p{margin:0 0 10px}.art .sh{font-weight:600;margin:12px 0 4px;break-after:avoid}.art .sh .num{margin-right:6px}
details.ad{margin:8px 0}details.ad summary{cursor:pointer;color:DARK;font-weight:500}
.opt{display:block;margin:3px 0 3px 26px;cursor:pointer}.box{border:1.5px solid #c8c9cb;padding:6px 12px;border-radius:4px;display:inline-block;margin-bottom:6px}
.gbox{border:2px solid ACC;border-radius:4px;padding:10px 16px;margin:14px 0;background:#fffaf6}.gbox p{margin:4px 0}.gbox .gh{color:DARK;font-weight:600;margin-bottom:6px}
.ext{background:#f9e3d3;padding:10px 16px;margin:6px 0;border-left:6px solid DARK}
.board{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;background:#e8ebee;border-top:5px solid #3a7cb0;padding:14px}.board>div{background:#fff;padding:10px 12px;font-size:15.5px;line-height:2.1}.board h4{margin:0 0 6px;background:#f9e3d3;color:DARK;padding:6px 10px;font-weight:600;font-size:14px}
.board input{width:110px}.tf{display:flex;gap:10px;align-items:center;padding:7px 0;border-bottom:1px solid #f0f0f2;flex-wrap:wrap}.tf .q{flex:1;min-width:280px}
.card{background:#eef0f2;border-left:5px solid ACC;padding:14px 20px;margin:8px 0;font-size:18px}
.selfa{display:flex;margin-top:14px;border-radius:6px;overflow:hidden}.selfa .l{background:ACC;color:#fff;font-weight:600;padding:12px 16px}.selfa .r{flex:1;background:#f0f0f1;padding:10px 16px;font-size:15px}
.score button{width:42px;height:42px;border-radius:50%;border:2px solid #e1e2e3;background:#fff;font-size:16px;margin:6px 6px 0 0;cursor:pointer}.score button.on{border-color:ACC;background:ACC2}
.done{display:none;margin-top:10px;background:#eaf7ee;color:#1e6b3d;padding:10px 14px;border-radius:6px}
.slack{border:1px solid #ddd;border-radius:8px;padding:10px 14px;background:#fff;font-size:15.5px}.slack b{font-weight:600}.slack .t{color:#8a8b8d;font-size:13px;margin-left:6px}
.hint{font-size:14px;color:#6d6e70}.two{display:grid;grid-template-columns:1fr 1fr;gap:6px 30px}
footer{max-width:1000px;margin:0 auto;padding:0 20px 30px;font-size:12px;color:#77787b}
@media(max-width:800px){.art{columns:1}.board,.two{grid-template-columns:1fr}}</style></head><body>
<header><div class="n">__NUM__</div><h1>__TITLE__</h1><div class="tag">__TAG__</div></header>
<div class="out1"><b>Lesson outcome</b><span>__OUT__</span></div>
<div class="wrap">__VOC__
<div class="top"><a href="../../../index.html">← Contents</a><div class="bar"><span class="st" id="st">Loading…</span></div></div>
<div class="tcom" id="tcom"><b>💬 Teacher’s comment</b><div id="tcomt"></div></div>
<nav>__NAV__</nav><main>__BODY__
<div class="ctl" style="margin-top:26px"><button class="btn" id="submit">Send to my teacher</button><span class="st" id="st2"></span></div>
<div class="done" id="done">✓ Sent to your teacher. You can still change your answers — they save automatically.</div></main></div>
<footer>__FOOT__Valentyna Hordiienko · Middle Learning Architect</footer>
<script>
const SB_URL="https://zuegojpfhgigsvyrnymt.supabase.co",SB_KEY="sb_publishable__Xn8xRhne9Hp2ckaXu6xCQ_MOe52bng";
const LESSON="__LESSON__";const STUDENT_CODE="__CODE__";const KEY=__KEY__;
const rpc=(f,b)=>fetch(SB_URL+"/rest/v1/rpc/"+f,{method:"POST",headers:{apikey:SB_KEY,"Content-Type":"application/json"},body:JSON.stringify(b)}).then(async r=>{const t=await r.text();if(!r.ok)throw new Error(t);return t?JSON.parse(t):null});
const $=id=>document.getElementById(id);let student="",timer=null,submitted=false,ready=false;
const norm=s=>(s||"").toLowerCase().replace(/[’`]/g,"'").replace(/\s+/g," ").replace(/[.!?]+$/,"").trim();
const okv=(k,v)=>KEY[k].some(x=>norm(x)===norm(v));
let CTX=null;const VIEW=new URLSearchParams(location.search).has("view");
function _tx(el){const c=el.cloneNode(true);c.querySelectorAll("b.x").forEach(b=>b.append(" "));c.querySelectorAll("b").forEach(b=>{if(/^[A-H]$/.test(b.textContent.trim()))b.append(" ")});return (c.textContent||"").replace(/\s+/g," ").trim()}
function _prompt(el){
 const nl=el.closest(".notes");if(nl){const lb=el.previousElementSibling;if(lb&&lb.tagName==="LABEL")return _tx(lb)}
 const row=el.closest(".row,.tf,.gbr,.fh,.pc,.msg");
 if(row){const c=row.cloneNode(true);c.querySelectorAll("input,select,textarea").forEach(x=>{if(x.type==="radio"){x.remove();return}x.replaceWith(document.createTextNode(" ___ "))});
  c.querySelectorAll(".fb,button,.opt,label").forEach(x=>{if(!x.querySelector||!x.querySelector("input"))x.remove()});const t=_tx(c);if(t)return t.slice(0,260)}
 let p=el.previousElementSibling;for(let i=0;p&&i<4;i++,p=p.previousElementSibling){if(p.matches&&p.matches("p.ins,p,h4,.card")){const t=_tx(p);if(t)return t.slice(0,260)}}
 return el.placeholder||""}
function buildCtx(){const c={};let i=0;document.querySelectorAll("section.sec").forEach(sec=>{const nb=document.querySelector('nav button[data-s="'+sec.id+'"]');
 const ins=sec.querySelector(".ins");const st=((nb?nb.textContent.trim()+" · ":"")+(ins?_tx(ins):"")).slice(0,220);
 sec.querySelectorAll("[data-k]").forEach(el=>{const k=el.dataset.k;if(!k||c[k])return;c[k]={s:st,q:_prompt(el),i:i++}})});
 c.self={s:"Self-assessment",q:"0–5",i:i++};c.q={s:"Questions for the teacher",q:"",i:i++};return c}
function collect(){const a={};document.querySelectorAll("input.g[data-k],select.g[data-k],textarea.g[data-k]").forEach(x=>a[x.dataset.k]=x.value);
 document.querySelectorAll("input[type=radio][data-k]:checked").forEach(x=>a[x.dataset.k]=x.value);const s=document.querySelector("#score .on");a.self=s?+s.dataset.v:null;if(!CTX)CTX=buildCtx();a._ctx=CTX;a._page=location.href.split("?")[0];a._sent=sentBy;return a}
function fill(a){document.querySelectorAll("input.g[data-k],select.g[data-k],textarea.g[data-k]").forEach(x=>{if(a[x.dataset.k]!=null)x.value=a[x.dataset.k]});
 document.querySelectorAll("input[type=radio][data-k]").forEach(x=>x.checked=a[x.dataset.k]===x.value);document.querySelectorAll("#score button").forEach(b=>b.classList.toggle("on",a.self!=null&&+b.dataset.v===a.self));if(window.afterFill)afterFill()}
function scores(){const a=collect(),r={};for(const k in KEY){const p=k.replace(/_[^_]+$/,"");r[p]=r[p]||[0,0];r[p][1]++;if(a[k]!=null&&okv(k,a[k]))r[p][0]++}const o={};for(const p in r)o[p]=r[p][0]+"/"+r[p][1];return o}
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
 if(!a){try{a=JSON.parse(localStorage.getItem("hw:"+LESSON+":"+(STUDENT_CODE||"preview"))||localStorage.getItem("hw:"+LESSON+":preview")||"null")}catch(e){}}if(a)fill(a);ready=true;if(STUDENT_CODE&&a&&!a._ctx)save();
 if(!STUDENT_CODE)status("Template preview — answers are not sent anywhere.");else status(student?(a?"Welcome back, "+student+"! Your answers are loaded.":"Hi, "+student+"! Your answers save automatically."):"Your answers save automatically.","ok")}
function fbk(k,ok,txt){const f=$("fb_"+k);if(!f)return;f.className="fb show "+(ok?"ok":"no");f.querySelector(".h").innerHTML=txt}
function chkSet(p){let n=0,t=0;for(const k in KEY){if(k.replace(/_[^_]+$/,"")!==p)continue;const el=document.querySelector(`.g[data-k="${k}"]`);if(!el)continue;t++;const ok=okv(k,el.value);if(ok)n++;
 el.classList.remove("right","wrong");el.classList.add(ok?"right":"wrong");fbk(k,ok,ok?"✓":"✗ <b>"+KEY[k][0]+"</b>")}$("r_"+p).textContent=n+" / "+t+(n===t?" ✓ Well done!":"");save()}
function chkRad(p,why){let n=0,t=0;for(const k in KEY){if(k.replace(/_[^_]+$/,"")!==p)continue;t++;const s=document.querySelector(`input[data-k="${k}"]:checked`);const ok=!!s&&okv(k,s.value);if(ok)n++;
 const w=(why&&why[k])?" "+why[k]:"";fbk(k,ok,(ok?"✓":"✗ <b>"+KEY[k][0]+"</b>")+w)}$("r_"+p).textContent=n+" / "+t+(n===t?" ✓ Well done!":"");save()}
function model(id){$(id).classList.toggle("show")}
document.querySelectorAll("#score button").forEach(b=>b.onclick=()=>{document.querySelectorAll("#score button").forEach(x=>x.classList.remove("on"));b.classList.add("on");later()});
document.addEventListener("input",e=>{if(e.target.closest("main"))later()});document.addEventListener("change",e=>{if(e.target.closest("main"))later()});
document.querySelectorAll("nav button").forEach(b=>b.onclick=()=>{document.querySelectorAll("nav button,.sec").forEach(x=>x.classList.remove("on"));b.classList.add("on");$(b.dataset.s).classList.add("on");scrollTo(0,0)});
$("submit").onclick=async()=>{submitted=true;sentBy="button";await save();$("done").style.display="block"};
__XJS__
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
</script><script src="https://villevian.github.io/bp-admin/vocab-kit.js" defer></script></body></html>"""

def fb(k): return '<div class="fb" id="fb_%s"><span class="h"></span></div>' % k
def sel(k, opts, w=None): return '<select class="g" data-k="%s"%s><option value="">—</option>%s</select>' % (k, ' style="width:%dpx"' % w if w else "", "".join("<option>%s</option>" % o for o in opts))
def inp(k, w=150, ph=""): return '<input class="g" data-k="%s" style="width:%dpx" placeholder="%s">' % (k, w, ph)
def ta(k, ph="", h=None): return '<textarea class="g" data-k="%s" placeholder="%s"%s></textarea>' % (k, ph, ' style="min-height:%dpx"' % h if h else "")
def ctl(p, fn="chkSet", extra=""): return '<div class="ctl"><button class="btn" onclick="%s(\'%s\')">Check</button>%s<span class="res" id="r_%s"></span></div>' % (fn, p, extra, p)
def radios(k, opts): return "".join('<label class="opt"><input type="radio" name="%s" data-k="%s" value="%s"> %s</label>' % (k, k, v, lab) for v, lab in opts)
SELF = ('<div class="selfa"><div class="l">Self-assessment</div><div class="r">%s 0 = I need more practice, 5 = I know this well.'
        '<div class="score" id="score">' + "".join('<button data-v="%d">%d</button>' % (i, i) for i in range(6)) + '</div>'
        '<textarea class="g" data-k="q" style="min-height:60px;margin-top:8px" placeholder="Questions for your teacher (optional)"></textarea></div></div>')
