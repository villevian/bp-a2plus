"""'My vocabulary' trainer (Quizlet-style): pick words per lesson with checkboxes, train them (Flashcards, Learn, Write, Match).
Selection + progress sync to Supabase via save_hw (lesson key "BP <LEVEL> Vocabulary").
Usage: python3 build_vocab.py OUT.html vocab_b2 B2 [STUDENT_CODE] [ACC ACC2 DARK]
"""
import sys, json, importlib
OUT, MOD, LEVEL = sys.argv[1], sys.argv[2], sys.argv[3]
CODE = sys.argv[4] if len(sys.argv) > 4 else ""
ACC, ACC2, DARK = (sys.argv[5:8] if len(sys.argv) > 7 else ("#5b5fc7", "#e8e9fa", "#4044a8"))
V = importlib.import_module(MOD).VOCAB
items, lessons = [], []
for num, title, groups in V:
    lessons.append({"n": num, "t": title, "g": [g for g, _ in groups]})
    for g, ws in groups:
        for i, w in enumerate(ws):
            en, uk, df, ex = w[:4]
            items.append({"id": "%s|%s" % (num, en), "l": num, "g": g, "en": en, "uk": uk, "df": df, "ex": ex})

html = r"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>My vocabulary — Business Partner __LEVEL__</title><link href="https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&display=swap" rel="stylesheet">
<style>*{box-sizing:border-box}body{margin:0;font-family:"Fira Sans",system-ui,sans-serif;font-weight:300;color:#231f20;background:#fff;font-size:17px;line-height:1.45}
header{display:flex;border-bottom:3px solid ACC}header .n{background:linear-gradient(120deg,DARK,#7b7fe0);color:#fff;font-weight:500;font-size:30px;padding:10px 22px}
header h1{margin:0;align-self:center;padding-left:18px;font-weight:500;font-size:28px;color:#4d4d4f}
main{max-width:980px;margin:0 auto;padding:10px 20px 50px}.top{display:flex;gap:14px;align-items:center;flex-wrap:wrap}.top a{color:ACC;text-decoration:none;font-weight:500;font-size:15px}.st{font-size:14px;color:#6d6e70;margin-left:auto}.st.ok{color:#2e7d4f}
.tabs{display:flex;gap:8px;margin:14px 0}.tabs button{border:1.5px solid ACC;background:#fff;color:DARK;border-radius:20px;padding:7px 18px;font:500 16px "Fira Sans",system-ui,sans-serif;cursor:pointer}.tabs button.on{background:ACC;color:#fff}
.bar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;background:ACC2;padding:8px 12px;border-radius:8px;margin-bottom:10px;font-size:15px}
.bar select,.bar input{font:inherit;font-size:15px;border:1.5px solid #c8c9cb;border-radius:4px;padding:3px 6px}.bar .cnt{font-weight:600;color:DARK;margin-left:auto}
.btn{background:#4d4d4f;color:#fff;border:0;border-radius:4px;padding:7px 14px;font:500 15px "Fira Sans",system-ui,sans-serif;cursor:pointer}.btn.l{background:#fff;color:#4d4d4f;border:1.5px solid #c8c9cb}.btn.a{background:ACC}
.grp{margin:16px 0 4px;display:flex;align-items:center;gap:10px}.grp h3{margin:0;font-size:16px;font-weight:600;color:DARK;text-transform:uppercase}.grp button{font-size:13px;padding:3px 10px}
.lh{font-size:20px;font-weight:500;margin:18px 0 0;border-bottom:2px solid ACC2;padding-bottom:4px}
.w{display:grid;grid-template-columns:30px 1.1fr 1fr 70px 28px;gap:8px;align-items:center;padding:7px 4px;border-bottom:1px solid #f0f0f2;cursor:pointer}.w:hover{background:#fafaff}
.w input{width:20px;height:20px;accent-color:ACC}.w .en{font-weight:500}.w .uk{color:#4d4d4f}.w .more{grid-column:2/6;font-size:14.5px;color:#6d6e70;display:none}.w.open .more{display:block}
.lv{display:flex;gap:3px}.lv i{width:12px;height:12px;border-radius:50%;background:#e1e2e3}.lv i.f{background:#3a9d5d}.spk{border:0;background:none;cursor:pointer;font-size:17px}
.modes{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:10px 0}.mode{border:1.5px solid #d5d6d7;border-radius:10px;padding:14px;cursor:pointer;background:#fff;text-align:left;font:inherit}.mode b{display:block;font-weight:600;color:DARK;font-size:17px}.mode span{font-size:14px;color:#6d6e70}.mode.on{border-color:ACC;background:ACC2}
.stage{margin-top:14px}.card{perspective:1000px;height:260px;cursor:pointer;max-width:640px;margin:0 auto}.ci{position:relative;width:100%;height:100%;transition:transform .45s;transform-style:preserve-3d}.card.fl .ci{transform:rotateY(180deg)}
.face{position:absolute;inset:0;backface-visibility:hidden;border-radius:14px;border:1.5px solid #d5d6d7;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:20px;text-align:center;box-shadow:0 3px 10px rgba(0,0,0,.06)}
.face.b{transform:rotateY(180deg);background:#fafaff}.face .big{font-size:30px;font-weight:500}.face .sm{font-size:15px;color:#6d6e70;margin-top:10px}.face .ex{font-style:italic;font-size:15px;margin-top:8px}
.prog{text-align:center;color:#6d6e70;font-size:14px;margin:8px 0}.row2{display:flex;gap:10px;justify-content:center;margin-top:12px;flex-wrap:wrap}
.q{font-size:26px;font-weight:500;text-align:center;margin:14px 0 6px}.qs{text-align:center;color:#6d6e70;font-size:15px}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:10px;max-width:680px;margin:14px auto}.opts button{border:1.5px solid #d5d6d7;background:#fff;border-radius:8px;padding:12px;font:inherit;font-size:17px;cursor:pointer;text-align:left}
.opts button.ok{border-color:#3a9d5d;background:#eaf7ee}.opts button.no{border-color:#d9534f;background:#fdecec}
.wr{display:flex;gap:8px;justify-content:center;margin-top:12px}.wr input{font:inherit;font-size:20px;border:1.5px solid #c8c9cb;border-radius:6px;padding:8px 12px;width:360px}.fbk{text-align:center;margin-top:10px;font-size:16px;min-height:24px}.fbk.ok{color:#2e7d4f}.fbk.no{color:#b03a2e}
.match{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;max-width:860px;margin:10px auto}.tile{border:1.5px solid #d5d6d7;border-radius:8px;padding:12px;min-height:74px;display:flex;align-items:center;justify-content:center;text-align:center;cursor:pointer;background:#fff;font-size:15.5px}
.tile.sel{border-color:ACC;background:ACC2}.tile.gone{visibility:hidden}.tile.no{border-color:#d9534f;background:#fdecec}
.done{text-align:center;padding:30px;font-size:20px}.dir{display:inline-flex;border:1.5px solid ACC;border-radius:18px;overflow:hidden}.dir button{border:0;background:#fff;color:DARK;padding:4px 12px;font:500 14px "Fira Sans",system-ui,sans-serif;cursor:pointer}.dir button.on{background:ACC;color:#fff}
.empty{text-align:center;color:#6d6e70;padding:30px}footer{max-width:980px;margin:0 auto;padding:0 20px 30px;font-size:12px;color:#77787b}
@media(max-width:700px){.w{grid-template-columns:28px 1fr 60px 26px}.w .uk{grid-column:2/3;grid-row:2}.modes,.match{grid-template-columns:1fr 1fr}.opts{grid-template-columns:1fr}}</style></head><body>
<header><div class="n">__LEVEL__</div><h1>My vocabulary</h1></header>
<main><div class="top"><a href="index.html">← Contents</a><span class="st" id="st"></span></div>
<div class="tabs"><button class="on" data-t="list">📖 Words</button><button data-t="train">🎯 Train <b id="tc"></b></button></div>
<div id="list"><div class="bar"><label>Lesson <select id="fl"><option value="">All lessons</option></select></label><label><input type="checkbox" id="fn"> only words I don’t know yet</label>
<input id="fs" placeholder="🔍 search"><button class="btn l" onclick="selAll(1)">Select all</button><button class="btn l" onclick="selAll(0)">Clear</button><span class="cnt" id="cnt"></span></div>
<p style="font-size:14px;color:#6d6e70;margin:4px 0">Tick the words you want to train. Click a word to see its meaning and an example. ● ● ● = how well you know it.</p><div id="words"></div></div>
<div id="train" hidden><div class="bar"><span>Training <b id="tn">0</b> words</span><span class="dir"><button class="on" data-d="en">EN → УКР</button><button data-d="uk">УКР → EN</button></span><label><input type="checkbox" id="tw"> only words I don’t know yet</label></div>
<div class="modes"><button class="mode on" data-m="cards"><b>🃏 Flashcards</b><span>Flip the card: do you know it?</span></button><button class="mode" data-m="learn"><b>✅ Learn</b><span>Choose the right answer</span></button>
<button class="mode" data-m="write"><b>⌨️ Write</b><span>Type the English word</span></button><button class="mode" data-m="match"><b>🧩 Match</b><span>Match words and meanings</span></button></div><div class="stage" id="stage"></div></div></main>
<footer>Valentyna Hordiienko · Middle Learning Architect</footer>
<script>
const SB_URL="https://zuegojpfhgigsvyrnymt.supabase.co",SB_KEY="sb_publishable__Xn8xRhne9Hp2ckaXu6xCQ_MOe52bng";
const KEYL="BP __LEVEL__ Vocabulary",CODE="__CODE__";let ITEMS=__ITEMS__;const LESSONS=[{n:"★",t:"My words",g:["My words"]}].concat(__LESSONS__);
const $=id=>document.getElementById(id);const byId={};ITEMS.forEach(x=>byId[x.id]=x);
let S={sel:[],lv:{},own:[],del:[]},timer=null,ready=false,dir="en",mode="cards";
const rpc=(f,b)=>fetch(SB_URL+"/rest/v1/rpc/"+f,{method:"POST",headers:{apikey:SB_KEY,"Content-Type":"application/json"},body:JSON.stringify(b)}).then(async r=>{const t=await r.text();if(!r.ok)throw new Error(t);return t?JSON.parse(t):null});
const norm=s=>(s||"").toLowerCase().replace(/[’`]/g,"'").replace(/[.!?,]/g,"").replace(/\s+/g," ").trim();
const lv=id=>S.lv[id]||0;
function status(t,c=""){$("st").textContent=t;$("st").className="st "+c}
function local(){try{localStorage.setItem("voc:"+KEYL+":"+(CODE||"preview"),JSON.stringify(S))}catch(e){}}
async function save(){if(!ready)return;local();if(!CODE){status("Preview — your words are saved on this device only.");return}
 try{try{const r=await rpc("get_my_hw",{p_code:CODE,p_lesson:KEYL});const R=(r&&r[0]&&r[0].answers)||{};const del=new Set([...(R.del||[]),...(S.del||[])]),o={};[...(R.own||[]),...(S.own||[])].forEach(w=>{if(!del.has(w.id))o[w.id]=w});S.own=Object.values(o);S.del=[...del];(R.sel||[]).forEach(id=>{if(/^own\|/.test(id)&&o[id]&&!S.sel.includes(id))S.sel.push(id)});ownSync()}catch(e){}
 const known=Object.values(S.lv).filter(v=>v>=3).length;await rpc("save_hw",{p_code:CODE,p_lesson:KEYL,p_answers:S,p_score:{selected:S.sel.length,mastered:known},p_submitted:false});status("Saved ✓","ok")}catch(e){status("Saved on this device (no internet).")}}
function later(){clearTimeout(timer);timer=setTimeout(save,1000)}
function speak(t){try{const u=new SpeechSynthesisUtterance(t);u.lang="en-GB";u.rate=.9;speechSynthesis.cancel();speechSynthesis.speak(u)}catch(e){}}
function dots(id){const n=lv(id);return '<span class="lv">'+[0,1,2].map(i=>'<i class="'+(i<n?"f":"")+'"></i>').join("")+"</span>"}

function ownSync(){(S.own||[]).forEach(w=>{const x={id:w.id,l:"★",g:"My words",en:w.en,uk:w.uk||"",df:w.src?"from "+w.src:"my word",ex:w.ex||""};byId[w.id]=x;if(!ITEMS.some(i=>i.id===w.id))ITEMS.push(x)});ITEMS=ITEMS.filter(i=>i.l!=="★"||S.own.some(o=>o.id===i.id))}
function ownForm(){return `<div class="bar" style="margin-top:8px"><input id="oEn" placeholder="English word or phrase" style="flex:1;min-width:180px"><input id="oUk" placeholder="translation" style="flex:1;min-width:140px"><input id="oEx" placeholder="example (optional)" style="flex:2;min-width:200px"><button class="btn a" id="ownAdd">＋ Add</button></div><p style="font-size:14px;color:#6d6e70;margin:2px 0 6px">Add your own words here – or select any text in a lesson and press <b>＋</b>.</p>`}
function addOwn(){const en=$("oEn").value.trim();if(!en)return;const w={id:"own|"+Date.now(),en,uk:$("oUk").value.trim(),ex:$("oEx").value.trim(),src:"",at:new Date().toISOString()};S.own.push(w);ownSync();S.sel.push(w.id);renderList();later()}
function delOwn(id){S.own=S.own.filter(w=>w.id!==id);S.del=[...(S.del||[]),id];S.sel=S.sel.filter(x=>x!==id);delete S.lv[id];ownSync();renderList();later()}
document.addEventListener("visibilitychange",()=>{if(document.visibilityState==="visible"&&CODE&&ready){rpc("get_my_hw",{p_code:CODE,p_lesson:KEYL}).then(r=>{const a=r&&r[0]&&r[0].answers;if(!a)return;const del=new Set([...(a.del||[]),...(S.del||[])]),o={};[...(S.own||[]),...(a.own||[])].forEach(w=>{if(!del.has(w.id))o[w.id]=w});S.own=Object.values(o);S.del=[...del];(a.sel||[]).forEach(id=>{if(!S.sel.includes(id))S.sel.push(id)});ownSync();S.sel=S.sel.filter(id=>byId[id]);renderList()}).catch(()=>{})}});
function renderList(){const L=$("fl").value,onlyNew=$("fn").checked,q=norm($("fs").value);let h="";
 LESSONS.forEach(les=>{if(L&&les.n!==L)return;let lh="";if(les.n==="★"&&!onlyNew&&!q)lh+=ownForm();les.g.forEach(g=>{const ws=ITEMS.filter(x=>x.l===les.n&&x.g===g&&(!onlyNew||lv(x.id)<3)&&(!q||norm(x.en+" "+x.uk).includes(q)));if(!ws.length)return;
  lh+=`<div class="grp"><h3>${g}</h3><button class="btn l" onclick="selGrp('${les.n}','${g.replace(/'/g,"\\'")}')">select group</button></div>`;
  ws.forEach(x=>{lh+=`<div class="w" data-id="${x.id}"><input type="checkbox" ${S.sel.includes(x.id)?"checked":""}><span class="en">${x.en}</span><span class="uk">${x.uk}</span>${dots(x.id)}<button class="spk" title="listen">🔊</button><div class="more">${x.df}${x.l==="★"?' <button class="btn l dl" style="font-size:12px;padding:2px 8px;margin-left:8px">delete</button>':""}<br><i>${x.ex}</i></div></div>`})});
  if(lh)h+=`<div class="lh">${les.n==="★"?"⭐":les.n} ${les.t}</div>`+lh});
 $("words").innerHTML=h||'<div class="empty">No words here.</div>';
 document.querySelectorAll(".w").forEach(r=>{const id=r.dataset.id;r.querySelector("input").onclick=e=>{e.stopPropagation();tog(id,e.target.checked)};r.querySelector(".spk").onclick=e=>{e.stopPropagation();speak(byId[id].en)};r.onclick=()=>r.classList.toggle("open");const d=r.querySelector(".dl");if(d)d.onclick=e=>{e.stopPropagation();delOwn(id)}});const ob=$("ownAdd");if(ob)ob.onclick=addOwn;cnt()}
function tog(id,on){S.sel=S.sel.filter(x=>x!==id);if(on)S.sel.push(id);cnt();later()}
function cnt(){$("cnt").textContent="Selected: "+S.sel.length;$("tc").textContent=S.sel.length?"("+S.sel.length+")":""}
function selAll(on){document.querySelectorAll(".w").forEach(r=>{r.querySelector("input").checked=!!on;tog(r.dataset.id,!!on)})}
function selGrp(l,g){ITEMS.filter(x=>x.l===l&&x.g===g).forEach(x=>{if(!S.sel.includes(x.id))S.sel.push(x.id)});renderList();later()}
function pool(){let p=S.sel.map(id=>byId[id]).filter(Boolean);if($("tw").checked)p=p.filter(x=>lv(x.id)<3);return p}
const shuffle=a=>{a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
function bump(id,d){S.lv[id]=Math.max(0,Math.min(3,lv(id)+d));later()}
const Q=x=>dir==="en"?x.en:x.uk, A=x=>dir==="en"?x.uk:x.en;
let deck=[],pos=0,score=0;
function startMode(){const p=pool();$("tn").textContent=p.length;const st=$("stage");
 if(!p.length){st.innerHTML='<div class="empty">Tick some words in 📖 Words first.</div>';return}
 deck=shuffle(p);pos=0;score=0;({cards:cards,learn:learn,write:write,match:match})[mode]()}
function endScreen(txt){$("stage").innerHTML=`<div class="done">🎉 ${txt}<div class="row2"><button class="btn a" onclick="startMode()">Again</button><button class="btn l" onclick="$('tw').checked=true;startMode()">Only words I don’t know yet</button></div></div>`}
function cards(){if(pos>=deck.length)return endScreen(`Done! You knew ${score} of ${deck.length}.`);const x=deck[pos];
 $("stage").innerHTML=`<div class="prog">${pos+1} / ${deck.length} · click the card to flip</div><div class="card" id="cd"><div class="ci"><div class="face"><div class="big">${Q(x)}</div><div class="sm">${dir==="en"?"🔊 click to flip":"click to flip"}</div></div>
 <div class="face b"><div class="big">${A(x)}</div><div class="sm">${x.df}</div><div class="ex">${x.ex}</div></div></div></div>
 <div class="row2"><button class="btn l" onclick="ans(0)">✗ Still learning</button><button class="btn a" onclick="ans(1)">✓ I know it</button><button class="btn l" onclick="speak('${x.en.replace(/'/g,"\\'")}')">🔊</button></div>`;
 $("cd").onclick=()=>$("cd").classList.toggle("fl")}
function ans(k){const x=deck[pos];bump(x.id,k?1:-1);if(k)score++;pos++;cards()}
function learn(){if(pos>=deck.length)return endScreen(`Score: ${score} / ${deck.length}`);const x=deck[pos];
 const others=shuffle(ITEMS.filter(y=>y.id!==x.id)).slice(0,3);const op=shuffle([x,...others]);
 $("stage").innerHTML=`<div class="prog">${pos+1} / ${deck.length}</div><div class="q">${Q(x)}</div><div class="qs">${dir==="en"?x.df:""}</div><div class="opts">${op.map(o=>`<button data-id="${o.id}">${A(o)}</button>`).join("")}</div><div class="fbk" id="fb"></div>`;
 document.querySelectorAll(".opts button").forEach(b=>b.onclick=()=>{const ok=b.dataset.id===x.id;b.classList.add(ok?"ok":"no");if(!ok)document.querySelector(`.opts button[data-id="${x.id}"]`).classList.add("ok");
  document.querySelectorAll(".opts button").forEach(z=>z.disabled=true);bump(x.id,ok?1:-1);if(ok)score++;$("fb").innerHTML=`<i>${x.ex}</i>`;speak(x.en);setTimeout(()=>{pos++;learn()},ok?1100:2200)})}
function write(){if(pos>=deck.length)return endScreen(`Score: ${score} / ${deck.length}`);const x=deck[pos];
 $("stage").innerHTML=`<div class="prog">${pos+1} / ${deck.length}</div><div class="q">${x.uk}</div><div class="qs">${x.df}</div><div class="wr"><input id="wi" placeholder="type in English" autocomplete="off"><button class="btn a" id="wb">Check</button></div><div class="fbk" id="fb"></div><div class="row2"><button class="btn l" id="hint">Hint</button></div>`;
 const i=$("wi");i.focus();let done=false;$("hint").onclick=()=>{i.value=x.en.slice(0,Math.ceil(x.en.length/3));i.focus()};
 const go=()=>{if(done){pos++;return write()}const ok=norm(i.value)===norm(x.en);done=true;bump(x.id,ok?1:-1);if(ok)score++;
  $("fb").className="fbk "+(ok?"ok":"no");$("fb").innerHTML=(ok?"✓ Correct! ":"✗ Correct answer: <b>"+x.en+"</b> · ")+`<i>${x.ex}</i><br><small>Press Enter to continue</small>`;speak(x.en)};
 $("wb").onclick=go;i.onkeydown=e=>{if(e.key==="Enter")go()}}
function match(){const set=deck.slice(0,6);if(set.length<2)return endScreen("Choose at least 2 words for Match.");const t0=Date.now();let first=null,left=set.length;
 const tiles=shuffle(set.flatMap(x=>[{id:x.id,t:x.en},{id:x.id,t:dir==="en"?x.uk:x.df}]));
 $("stage").innerHTML=`<div class="prog">Match each English word with its meaning · <b id="tm">0.0</b> s</div><div class="match">${tiles.map((t,k)=>`<div class="tile" data-id="${t.id}" data-k="${k}">${t.t}</div>`).join("")}</div>`;
 const iv=setInterval(()=>{const e=$("tm");if(!e)return clearInterval(iv);e.textContent=((Date.now()-t0)/1000).toFixed(1)},100);
 document.querySelectorAll(".tile").forEach(el=>el.onclick=()=>{if(el===first)return;if(!first){first=el;el.classList.add("sel");return}
  if(first.dataset.id===el.dataset.id){first.classList.add("gone");el.classList.add("gone");bump(el.dataset.id,1);first=null;if(--left===0){clearInterval(iv);setTimeout(()=>endScreen("Matched in "+((Date.now()-t0)/1000).toFixed(1)+" s"),300)}}
  else{const a=first;a.classList.add("no");el.classList.add("no");setTimeout(()=>{a.classList.remove("no","sel");el.classList.remove("no")},450);first=null}})}
document.querySelectorAll(".tabs button").forEach(b=>b.onclick=()=>{document.querySelectorAll(".tabs button").forEach(x=>x.classList.remove("on"));b.classList.add("on");$("list").hidden=b.dataset.t!=="list";$("train").hidden=b.dataset.t!=="train";if(b.dataset.t==="train")startMode();else renderList()});
document.querySelectorAll(".mode").forEach(b=>b.onclick=()=>{document.querySelectorAll(".mode").forEach(x=>x.classList.remove("on"));b.classList.add("on");mode=b.dataset.m;startMode()});
document.querySelectorAll(".dir button").forEach(b=>b.onclick=()=>{document.querySelectorAll(".dir button").forEach(x=>x.classList.remove("on"));b.classList.add("on");dir=b.dataset.d;startMode()});
$("tw").onchange=startMode;["fl","fn"].forEach(i=>$(i).onchange=renderList);$("fs").oninput=renderList;
LESSONS.forEach(l=>$("fl").insertAdjacentHTML("beforeend",`<option value="${l.n}">${l.n} ${l.t}</option>`));
(async()=>{let a=null;if(CODE){try{const r=await rpc("get_my_hw",{p_code:CODE,p_lesson:KEYL});const d=r&&r[0];if(d&&d.answers)a=d.answers}catch(e){}}
 if(!a){try{a=JSON.parse(localStorage.getItem("voc:"+KEYL+":"+(CODE||"preview"))||"null")}catch(e){}}
 if(a&&a.sel){S={sel:a.sel,lv:a.lv||{},own:a.own||[],del:a.del||[]};ownSync();S.sel=S.sel.filter(id=>byId[id])}ready=true;renderList();status(CODE?"Your words save automatically.":"Preview — your words are saved on this device only.",CODE?"ok":"")})();
</script></body></html>"""
html = (html.replace("__ITEMS__", json.dumps(items, ensure_ascii=False)).replace("__LESSONS__", json.dumps(lessons, ensure_ascii=False))
        .replace("__LEVEL__", LEVEL).replace("__CODE__", CODE).replace("ACC2", ACC2).replace("ACC", ACC).replace("DARK", DARK))
open(OUT, "w").write(html)
import os as _o
json.dump({"level": LEVEL, "items": items}, open(_o.path.join(_o.path.dirname(_o.path.abspath(OUT)), "vocab.json"), "w"), ensure_ascii=False)
print("ok", len(items), "words")
