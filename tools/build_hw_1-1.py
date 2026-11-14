import json
from expl import X6,X7A,X7B
css = open('/home/claude/pasha72/base.css').read().replace('--coral:#e8605a', '--coral:#3fa9ad') + """
.bar{position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid #e3e4e5;padding:10px 22px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.bar input{font:inherit;padding:7px 10px;border:1.5px solid var(--coral);border-radius:4px;min-width:200px}
.bar .st{font-size:14px;color:var(--grey)}
.bar .st.ok{color:#2e7d32}.bar .st.err{color:#c0392b}
.outcome{display:flex;margin:14px 0 0}
.outcome .l{background:var(--coral);color:#fff;font-weight:600;padding:10px 18px;font-size:15px}
.outcome .r{flex:1;background:var(--lg);padding:10px 16px;font-size:15px}
.ex{margin:26px 0 0;scroll-margin-top:70px}
.ex .q{display:flex;gap:10px;align-items:baseline;font-weight:500;font-size:17px;margin-bottom:10px;line-height:1.35}
.ex .q .n{color:var(--coral);font-weight:600;font-size:24px;min-width:30px}
.ex .q .n small{font-size:17px}
.lab{color:var(--grey);font-weight:500;font-size:20px;margin:30px 0 -6px;padding-top:10px;border-top:1px solid #e3e4e5}
.lab.v{color:var(--mag)}
.lnk{display:inline-flex;align-items:center;gap:5px;margin-left:8px;padding:2px 10px;border:1px solid var(--mag);border-radius:14px;color:var(--mag);font-size:13px;font-weight:500;text-decoration:none;white-space:nowrap}
.lnk.x{border-color:var(--grey);color:#4d4d4f}
.ticks{display:flex;flex-wrap:wrap;gap:8px;margin:4px 0 12px 40px}
.ticks label{border:1.5px solid #c9cacc;border-radius:18px;padding:6px 12px;cursor:pointer;font-size:15px;user-select:none}
.ticks input{display:none}
.ticks label.on{border-color:var(--coral);background:#e6f4f4;font-weight:500}
.ticks label.on:before{content:"✓ ";color:var(--coral);font-weight:600}
.sub{font-weight:600;margin:6px 0 4px 40px}
.wb{display:flex;flex-wrap:wrap;gap:6px 14px;border:1px solid #a7a9ac;padding:8px 12px;margin:0 0 12px 40px;font-size:15px}
ol.it{list-style:none;padding:0;margin:0 0 0 40px}
ol.it>li{display:flex;gap:10px;margin-bottom:9px;font-size:16px;line-height:1.5}
ol.it>li>.i{font-weight:600;min-width:16px}
ol.it>li>.t{flex:1}
.g{font:inherit;font-size:15px;border:0;border-bottom:1.5px solid var(--ink);padding:1px 4px;width:170px;background:#fff}
.g.right{border-color:#2e7d32;background:#eef7ea}.g.wrong{border-color:#c0392b;background:#fdecea}
select{font:inherit;font-size:15px;padding:3px 6px;border:1.5px solid #c9cacc;border-radius:4px;background:#fff}
select.right{border-color:#2e7d32;background:#eef7ea}select.wrong{border-color:#c0392b;background:#fdecea}
.mc{display:grid;grid-template-columns:1fr 1fr;gap:4px 24px;margin:0 0 0 40px}
.mc .qq{margin-bottom:10px;font-size:16px}
.mc .qq>div{font-weight:500;margin-bottom:3px}
.mc label{display:block;font-size:15px;padding:2px 0;cursor:pointer}
.mc label input{margin-right:6px;accent-color:var(--coral)}
textarea{font:inherit;font-size:15px;width:calc(100% - 40px);margin-left:40px;min-height:74px;padding:8px 10px;border:1px solid #c9cacc;border-radius:4px;resize:vertical}
textarea.sm{min-height:44px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:4px 28px}
.chk{margin:8px 0 0 40px;display:flex;gap:10px;align-items:center}
.chk button,.btn{font:inherit;font-weight:500;border:0;padding:8px 14px;border-radius:4px;cursor:pointer;background:var(--coral);color:#fff}
.chk span{font-size:14px;color:var(--grey)}
.oval{margin-left:40px;border:1.3px solid var(--coral);border-radius:50%;padding:12px 30px;text-align:center;line-height:1.9;max-width:640px;font-size:15px}
.oval span{margin:0 8px;white-space:nowrap}
.eg{color:#2a7fa8;font-style:italic;font-weight:400;margin:8px 0 8px 40px}
.proj{background:var(--lg);margin-top:30px;padding:0 0 16px}
.proj .ph{background:repeating-linear-gradient(135deg,#7d7e81 0 6px,#707174 6px 12px);color:#fff;font-weight:500;font-size:19px;padding:9px 18px}
.proj .ex{margin-top:16px;padding:0 16px}
.cats{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-left:40px}
.cats div b{display:block;font-weight:600;font-size:14.5px;margin-bottom:3px}
.cats textarea{margin-left:0;width:100%}
.selfa{display:flex;margin-top:30px}
.tcom{display:none;margin-top:16px;background:#fdf0d5;border-left:4px solid #f2b631;padding:10px 14px;border-radius:4px;font-size:15px;white-space:pre-wrap}
.tcom b{display:block;margin-bottom:4px;font-weight:600}
.selfa .l{background:var(--coral);color:#fff;font-weight:600;padding:14px 18px;display:flex;align-items:center}
.selfa .r{flex:1;background:var(--lg);padding:12px 16px}
.score{display:flex;gap:6px;margin-top:8px}
.score button{font:inherit;width:38px;height:38px;border-radius:50%;border:1.5px solid var(--coral);background:#fff;color:var(--coral);font-weight:600;cursor:pointer}
.score button.on{background:var(--coral);color:#fff}
.send{margin:24px 0 40px;display:flex;gap:12px;align-items:center}
.send .btn{padding:12px 22px;font-size:16px}
.done{background:#eef7ea;border:1px solid #9ccc65;padding:10px 14px;border-radius:4px;display:none}
.fb{display:none;margin:4px 0 2px;padding:7px 10px;border-radius:4px;font-size:14px;line-height:1.45;background:#f6f6f6}
.fb.show{display:block}.fb.ok{background:#eef7ea;border-left:3px solid #2e7d32}.fb.no{background:#fdecea;border-left:3px solid #c0392b}
.fb .h{font-weight:600;margin-bottom:3px}.fb .ua{color:#555;margin-top:3px}.fb .ua:before{content:"🇺🇦 "}.fb .en:before{content:"🇬🇧 "}
.fb s{color:#c0392b}
@media(max-width:760px){.mc,.two,.cats{grid-template-columns:1fr}.ticks,.wb,ol.it,.mc,.sub,.chk,.oval,.eg,.cats{margin-left:0}textarea{margin-left:0;width:100%}}
"""

B = "https://english-dashboard.pearson.com/CDN/ProdStore/BUSINESS_PARTNER/A2P/packets/BPA2P_01_BusinessTravel_"
Q = "/index.html?a5_lms_api=Console"
icon = '<svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.07 0l3-3a5 5 0 0 0-7.07-7.07l-1.5 1.5"/><path d="M14 11a5 5 0 0 0-7.07 0l-3 3a5 5 0 0 0 7.07 7.07l1.5-1.5"/></svg>'
L = lambda p, t="Do it online", c="": f'<a class="lnk {c}" target="_blank" rel="noopener" href="{B}{p}{Q}">{icon}{t}</a>'


def ticks(name, items):
    return f'<div class="ticks" data-k="{name}">' + "".join(f'<label><input type="checkbox" value="{x}">{x}</label>' for x in items) + '</div>'


def ta(k, ph="", cls=""):
    return f'<textarea class="{cls}" data-k="{k}" placeholder="{ph}"></textarea>'


def mc(qs):
    out = '<div class="mc">'
    for i, (t, opts) in enumerate(qs, 1):
        out += f'<div class="qq"><div>{i} {t}</div>' + "".join(
            f'<label><input type="radio" name="e4_{i}" data-k="e4_{i}" value="{l}"><b>{l}</b> {o}</label>' for l, o in zip("abc", opts)) + '</div>'
    return out + '</div>'


def gap(k):
    return f'<input class="g" data-k="{k}" autocomplete="off">'


E6 = [("They made a ", " for two rooms, but when they arrived, only one was available."),
      ("I took a thirteen-hour ", " from Madrid to Buenos Aires."),
      ("We need to hire a ", " to take ten people from the airport to the conference centre."),
      ("He usually uses a ", " to get a car from one meeting to the next."),
      ("I arrived at the ", " five minutes after the plane had left."),
      ("We had a comfortable ", " in Vietnam because the resort was very modern."),
      ("They waited in the departure ", " until it was time to get on the plane."),
      ("The ", " of the apartment is perfect – near the office and the station."),
      ("I like to take ", " so I can see what life in the city is like.")]
K6 = ["reservation", "flight", "vehicle", "ridesharing app", "gate", "stay", "lounge", "location", "public transportation"]
S7 = ["I go <b>abroad</b> for work trips quite often.", "I take several <b>short-haul</b> flights each year.", "The flight was <b>delayed</b> by two hours.",
      "The captain said that we were ready for <b>landing</b>.", "The <b>departure</b> was a few minutes late."]
DEF7 = {"a": "a flight or plane that travels a short distance", "b": "the action of bringing a plane down to the ground after being in the air",
        "c": "to or in another country", "d": "the action of leaving a place, especially at the start of a journey", "e": "late, usually because of a problem"}
K7A = ["c", "a", "e", "b", "d"]
O7 = ["long-haul", "take-off", "arrival", "on-time", "local"]
K7B = [["short-haul"], ["landing"], ["departure"], ["delayed", "late"], ["abroad", "international", "foreign"]]

FB = lambda k,en,ua: f'<div class="fb" id="fb_{k}"><div class="h"></div><div class="en">{en}</div><div class="ua">{ua}</div></div>'
e6 = "".join(f'<li><span class="i">{i}</span><span class="t">{a}{gap(f"e6_{i}")}{b}{FB(f"e6_{i}",*X6[i-1])}</span></li>' for i, (a, b) in enumerate(E6, 1))
sel = lambda k: f'<select data-k="{k}"><option value="">–</option>' + "".join(f'<option value="{l}">{l}</option>' for l in "abcde") + '</select>'
e7a_l = "".join(f'<li><span class="i">{i}</span><span class="t">{s} &nbsp;{sel(f"e7a_{i}")}{FB(f"e7a_{i}",*X7A[i-1])}</span></li>' for i, s in enumerate(S7, 1))
e7a_r = "".join(f'<li><span class="i">{l}</span><span class="t">{d}</span></li>' for l, d in DEF7.items())
e7b = "".join(f'<li><span class="i">{i}</span><span class="t">{w} &nbsp;{gap(f"e7b_{i}")}{FB(f"e7b_{i}",*X7B[i-1])}</span></li>' for i, w in enumerate(O7, 1))

html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>1.1 Business travel — Homework</title>
<link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>{css}</style></head><body>
<header><div class="n">1.1</div><h1>Business travel</h1><div class="t">HOMEWORK</div></header>
<div class="bar"><span class="st" id="st">Loading…</span></div>
<a href="../../../index.html" style="display:inline-block;margin:12px 22px 0;color:#3fa9ad;font-weight:500;text-decoration:none;font-size:15px">← Contents</a>
<main>
<div class="outcome"><div class="l">Lesson outcome</div><div class="r">Learners can use vocabulary related to business travel.</div></div>

<div class="tcom" id="tcom"><b>💬 Teacher’s comment</b><div id="tcomt"></div></div>
<div class="lab">Lead-in</div>
<div class="ex"><div class="q"><span class="n">1</span><span>Tick (✓) the types of transport and accommodation you use when you travel to another country.{L("01")}</span></div>
 <div class="sub">Transport</div>{ticks("e1_t", ["boat","bus","car","coach","motorcycle","plane","taxi","train"])}
 <div class="sub">Accommodation</div>{ticks("e1_a", ["bed and breakfast (B&B)","budget hotel","business hotel","holiday resort","home of friend or family","luxury hotel","rented apartment","youth hostel"])}
</div>
<div class="ex"><div class="q"><span class="n">2</span><span>When you travel, how do you choose which transport to use? Price? Speed? Comfort? How easy it is to use? What about accommodation? Price? Comfort? Location? Something else?{L("02")}</span></div>
 {ta("e2","Write 2–3 sentences. We’ll talk about it in class.")}</div>

<div class="lab v">VIDEO</div>
<div class="ex"><div class="q"><span class="n">3</span><span>Watch the video about business travel. Which topics do the speakers talk about?{L("03","Watch / do it online")}</span></div>
 {ticks("e3", ["a Why they travel","b Where they travel","c Who they travel with","d Types of transportation","e Accommodation","f The cost of travel","g Advice for travel","h How to pack a suitcase"])}</div>
<div class="ex"><div class="q"><span class="n">4</span><span>Watch the video again and choose the correct option.{L("04")}{L("Extra_AB","Extra activity","x")}</span></div>
 {mc([("Which type of travel do they talk about?",["travel to cities in their own country","travel to other countries","going to and from work"]),
      ("What does Alex talk about?",["using his laptop for video chats","problems with travelling a lot","travelling by plane"]),
      ("For a hotel, what’s important to Alessio?",["It needs to be near his job.","It should have free breakfast.","He likes to be able to book it online."]),
      ("How does Amira feel about talking with local people?",["She worries about it a lot.","She never tries it.","She likes it because they help her."]),
      ("What problem did Amira have at the airport?",["She didn’t arrive at the airport on time.","She made a mistake about the time.","The time of her plane was changed."]),
      ("What does Alessio’s advice include?",["an idea for having more free time","an idea for saving money","tips for good communication"])])}</div>
<div class="ex"><div class="q"><span class="n">5</span><span>Do you think each speaker enjoys travelling for work? Why? / Why not?{L("05")}</span></div>
 {ta("e5","Alex … / Alessio … / Amira …")}</div>

<div class="lab">Vocabulary · Transport, accommodation and travel</div>
<div class="ex"><div class="q"><span class="n">6</span><span>Complete the sentences with these words from the video.{L("06")}</span></div>
 <div class="wb"><span>flight</span><span>gate</span><span>location</span><span>lounge</span><span>public transportation</span><span>reservation</span><span>ridesharing app</span><span>stay</span><span>vehicle</span></div>
 <ol class="it">{e6}</ol>
 <div class="chk"><button onclick="check6()">Check</button><span id="r6"></span></div></div>
<div class="ex"><div class="q"><span class="n">7<small>A</small></span><span>Match the words in bold with the definitions.{L("07")}</span></div>
 <div class="two"><ol class="it">{e7a_l}</ol><ol class="it">{e7a_r}</ol></div>
 <div class="chk"><button onclick="check7a()">Check</button><span id="r7a"></span></div></div>
<div class="ex"><div class="q"><span class="n"><small>B</small></span><span>Write the words in bold in Exercise 7A with their opposites.{L("Extra_C","Extra activity","x")}</span></div>
 <ol class="it">{e7b}</ol>
 <div class="chk"><button onclick="check7b()">Check</button><span id="r7b"></span></div></div>
<div class="ex"><div class="q"><span class="n">8</span><span>Use adjectives to make sentences about business travel. Write three sentences.{L("08")}</span></div>
 <div class="oval"><span>Making a hotel reservation</span> <span>Waiting in a lounge</span> <span>Travelling abroad</span> <span>Using a ridesharing app</span> <span>A delayed train or flight</span> <span>Driving when you’re abroad</span> <span>A long-haul flight</span></div>
 <div class="eg">… is … because … — Travelling abroad <b>is</b> interesting <b>because</b> you see new places.</div>
 {ta("e8_1","1. ","sm")}{ta("e8_2","2. ","sm")}{ta("e8_3","3. ","sm")}</div>

<div class="proj"><div class="ph">PROJECT: Helping a business traveller</div>
 <div class="ex"><div class="q"><span class="n">9<small>A</small></span><span>Imagine you need to give advice about your town to a visitor from abroad. For each category, write what advice you would give and why.</span></div>
  <div class="cats">
   <div><b>Travel</b> — how to arrive: by plane, bus, train, etc.{ta("e9_travel","")}</div>
   <div><b>Accommodation</b> — where to stay{ta("e9_acc","")}</div>
   <div><b>Travelling around town</b> — transportation{ta("e9_around","")}</div>
   <div><b>Other useful information</b> — sights, food to try, etc.{ta("e9_other","")}</div>
  </div>
  <div class="eg">The City Hotel is quiet and is in a good location. It’s a great place to stay.</div></div>
 <div class="ex"><div class="q"><span class="n"><small>B</small></span><span>Prepare for a conference call with a colleague: write 3–4 questions the visitor might ask you. We’ll roleplay it in class.</span></div>
  <div class="eg">A: How do I get to your city? &nbsp; B: Take a flight. Then take a train from the airport to the Central Rail Station.</div>
  {ta("e9b","How do I get … ? Where can I … ?")}</div>
</div>

<div class="selfa"><div class="l">Self-assessment</div><div class="r">How successfully have you achieved the lesson outcome? 0 = I need more practice, 5 = I know this well.
 <div class="score" id="score">{"".join(f'<button data-v="{i}">{i}</button>' for i in range(6))}</div>
 {ta("q","Questions for your teacher (optional)","sm").replace('margin-left:40px','')}</div></div>

<div class="send"><button class="btn" id="submit">Send to my teacher</button><span class="st" id="st2"></span></div>
<div class="done" id="done">✓ Your homework has been sent. You can still change your answers — they save automatically.</div>
</main>
<script>
const SB_URL = "https://zuegojpfhgigsvyrnymt.supabase.co";
const SB_KEY = "sb_publishable__Xn8xRhne9Hp2ckaXu6xCQ_MOe52bng";
const LESSON = "BP A2+ 1.1 Business travel";
const STUDENT_CODE = "__CODE__";   // personal code of the student whose page this is ("" = template preview)
const rpc=(f,body)=>fetch(SB_URL+"/rest/v1/rpc/"+f,{{method:"POST",headers:{{apikey:SB_KEY,"Content-Type":"application/json"}},body:JSON.stringify(body)}}).then(async r=>{{const t=await r.text();if(!r.ok)throw new Error(t);return t?JSON.parse(t):null}});
const K6={json.dumps(K6)}, K7A={json.dumps(K7A)}, K7B={json.dumps(K7B)};
const $=id=>document.getElementById(id);
let student="", timer=null, submitted=false, ready=false;
const norm=s=>s.trim().toLowerCase().replace(/\\s+/g," ").replace(/^(a|an|the) /,"");

function collect(){{
 const a={{}};
 document.querySelectorAll(".ticks").forEach(t=>a[t.dataset.k]=[...t.querySelectorAll("input:checked")].map(x=>x.value));
 document.querySelectorAll("textarea[data-k], input.g[data-k], select[data-k]").forEach(x=>a[x.dataset.k]=x.value);
 document.querySelectorAll("input[type=radio][data-k]:checked").forEach(x=>a[x.dataset.k]=x.value);
 const s=document.querySelector("#score .on"); a.self=s?+s.dataset.v:null;
 return a;
}}
function fill(a){{
 document.querySelectorAll(".ticks").forEach(t=>{{const v=a[t.dataset.k]||[];t.querySelectorAll("input").forEach(i=>{{i.checked=v.includes(i.value);i.parentNode.classList.toggle("on",i.checked)}})}});
 document.querySelectorAll("textarea[data-k], input.g[data-k], select[data-k]").forEach(x=>{{if(a[x.dataset.k]!=null)x.value=a[x.dataset.k]}});
 document.querySelectorAll("input[type=radio][data-k]").forEach(x=>x.checked=a[x.dataset.k]===x.value);
 document.querySelectorAll("#score button").forEach(b=>b.classList.toggle("on",a.self!=null&&+b.dataset.v===a.self));
}}
function scores(){{
 const a=collect();let s6=0,s7a=0,s7b=0;
 K6.forEach((k,i)=>{{if(norm(a["e6_"+(i+1)]||"")===k)s6++}});
 K7A.forEach((k,i)=>{{if(a["e7a_"+(i+1)]===k)s7a++}});
 K7B.forEach((k,i)=>{{if(k.includes(norm(a["e7b_"+(i+1)]||"")))s7b++}});
 return {{e6:s6+"/9",e7a:s7a+"/5",e7b:s7b+"/5"}};
}}
function status(t,c=""){{$("st").textContent=t;$("st").className="st "+c}}
function local(){{try{{localStorage.setItem("hw:"+LESSON+":"+(STUDENT_CODE||"preview"),JSON.stringify(collect()))}}catch(e){{}}}}
async function save(){{
 if(!ready)return;local();
 if(!STUDENT_CODE){{status("Template preview — answers are not sent anywhere.");return}}
 status("Saving…");
 try{{await rpc("save_hw",{{p_code:STUDENT_CODE,p_lesson:LESSON,p_answers:collect(),p_score:scores(),p_submitted:submitted}});status("Saved ✓ "+new Date().toLocaleTimeString().slice(0,5),"ok")}}
 catch(e){{status("Not saved online — check your internet. Your answers are kept on this device.","err")}}
}}
function later(){{clearTimeout(timer);timer=setTimeout(save,1200)}}
async function start(){{
 let a=null;
 if(STUDENT_CODE){{try{{const r=await rpc("get_my_hw",{{p_code:STUDENT_CODE,p_lesson:LESSON}});const d=r&&r[0];
  if(d){{student=d.name;if(d.answers){{a=d.answers;submitted=!!d.submitted;if(submitted)$("done").style.display="block"}}
   if(d.teacher_comment){{$("tcomt").textContent=d.teacher_comment;$("tcom").style.display="block"}}}}}}catch(e){{}}}}
 if(!a){{try{{a=JSON.parse(localStorage.getItem("hw:"+LESSON+":"+(STUDENT_CODE||"preview"))||"null")}}catch(e){{}}}}
 if(a)fill(a);ready=true;
 if(!STUDENT_CODE)status("Template preview — answers are not sent anywhere.");
 else status(student?(a?"Welcome back, "+student+"! Your answers are loaded.":"Hi, "+student+"! Your answers save automatically."):"Your answers save automatically.","ok");
}}
function mark(el,ok,correct){{el.classList.remove("right","wrong");el.classList.add(ok?"right":"wrong");
 const f=$("fb_"+el.dataset.k);if(!f)return;f.className="fb show "+(ok?"ok":"no");
 f.querySelector(".h").innerHTML=ok?"✓ Correct! / Правильно!":(el.value?"✗ Not quite. / Не зовсім. ":"✗ No answer. / Немає відповіді. ")+"Correct answer / Правильна відповідь: <b>"+correct+"</b>"}}
function check6(){{let n=0;K6.forEach((k,i)=>{{const el=document.querySelector(`[data-k=e6_${{i+1}}]`);const ok=norm(el.value)===k;if(ok)n++;mark(el,ok,k)}});$("r6").textContent=n+" / 9 correct";save()}}
function check7a(){{let n=0;K7A.forEach((k,i)=>{{const el=document.querySelector(`[data-k=e7a_${{i+1}}]`);const ok=el.value===k;if(ok)n++;mark(el,ok,k)}});$("r7a").textContent=n+" / 5 correct";save()}}
function check7b(){{let n=0;K7B.forEach((k,i)=>{{const el=document.querySelector(`[data-k=e7b_${{i+1}}]`);const ok=k.includes(norm(el.value));if(ok)n++;mark(el,ok,k[0])}});$("r7b").textContent=n+" / 5 correct";save()}}
document.querySelectorAll(".ticks label").forEach(l=>l.addEventListener("click",e=>{{e.preventDefault();const i=l.querySelector("input");i.checked=!i.checked;l.classList.toggle("on",i.checked);later()}}));
document.querySelectorAll("#score button").forEach(b=>b.onclick=()=>{{document.querySelectorAll("#score button").forEach(x=>x.classList.remove("on"));b.classList.add("on");later()}});
document.addEventListener("input",e=>{{if(e.target.closest("main"))later()}});
document.addEventListener("change",e=>{{if(e.target.closest("main"))later()}});
$("submit").onclick=async()=>{{submitted=true;await save();$("done").style.display="block";$("st2").textContent=""}};
start();
</script></body></html>'''
import sys
open(sys.argv[1], 'w').write(html.replace('__CODE__', sys.argv[2] if len(sys.argv)>2 else ''))
