"""Add Supabase sync to the 'Gerund vs Infinitive: Reddit Drama Edition' lesson (General English).
Saves karma, post results, comment results and drill stats via save_hw; restores them on load; adds a status bar + 'Send to teacher'.
Usage: python3 ge_sync.py SRC.html OUT.html "LESSON KEY" STUDENT_CODE
"""
import sys
SRC, OUT, KEY, CODE = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else ""
s = open(SRC, encoding="utf-8").read()
bar = '''<div id="syncbar" style="max-width:820px;margin:0 auto;padding:6px 16px 0;display:flex;gap:10px;align-items:center;flex-wrap:wrap;font-size:14px">
<a href="../index.html" style="color:var(--or);text-decoration:none;font-weight:700">← Мои уроки</a><span id="syst" style="color:var(--muted)">Загрузка…</span>
<button id="sysend" class="ghost" style="margin-left:auto;padding:6px 14px;font-size:14px">📨 Отправить учителю</button><span id="sydone" style="display:none;color:var(--ok);font-weight:700">✓ Отправлено</span></div>
<div id="tcom" style="display:none;max-width:820px;margin:8px auto 0;background:#fff6e0;border:1px solid #f5d79e;border-radius:10px;padding:10px 14px;font-size:14px;white-space:pre-wrap"><b>💬 Комментарий учителя:</b><div id="tcomt"></div></div>'''
s = s.replace("</header>", bar + "\n</header>", 1)
js = r'''<script>
(()=>{
const SB_URL="https://zuegojpfhgigsvyrnymt.supabase.co",SB_KEY="sb_publishable__Xn8xRhne9Hp2ckaXu6xCQ_MOe52bng";
const LESSON="__KEY__",CODE="__CODE__";const $=id=>document.getElementById(id);
const rpc=(f,b)=>fetch(SB_URL+"/rest/v1/rpc/"+f,{method:"POST",headers:{apikey:SB_KEY,"Content-Type":"application/json"},body:JSON.stringify(b)}).then(async r=>{const t=await r.text();if(!r.ok)throw new Error(t);return t?JSON.parse(t):null});
let ready=false,submitted=false,timer=null;const postRes={};let drillBest=null;
function st(t,c){$("syst").textContent=t;$("syst").style.color=c||"var(--muted)"}
function state(){return{karma:karma,postDone:postDone,postRes:postRes,commentsDone:ci,commentsOk:cOk,drill:drillBest}}
function scores(){const posts=Object.values(postRes);const ok=posts.reduce((a,p)=>a+p.ok,0),tot=posts.reduce((a,p)=>a+p.total,0);
 return{posts:posts.length+"/"+POSTS.length,posts_score:ok+"/"+tot,comments:Math.min(ci,COMMENTS.length)+"/"+COMMENTS.length,comments_ok:cOk,karma:karma,drill_errors:drillBest?drillBest.errors:null}}
function local(){try{localStorage.setItem("ge:"+LESSON+":"+(CODE||"preview"),JSON.stringify(state()))}catch(e){}}
async function save(){if(!ready)return;local();if(!CODE){st("Предпросмотр — результаты сохраняются только на этом устройстве.");return}
 try{await rpc("save_hw",{p_code:CODE,p_lesson:LESSON,p_answers:state(),p_score:scores(),p_submitted:submitted});st("Сохранено ✓ "+new Date().toLocaleTimeString().slice(0,5),"var(--ok)")}
 catch(e){st("Нет интернета — результаты сохранены на этом устройстве.","var(--bad)")}}
function later(){clearTimeout(timer);timer=setTimeout(save,900)}
/* hooks */
const _check=checkPost;checkPost=function(gaps){_check(gaps);const sels=[...document.querySelectorAll('#postBox select')];if(sels.some(x=>!x.disabled))return;
 const ok=sels.filter(x=>x.classList.contains('ok')||x.classList.contains('meh')).length;postRes[cur]={ok:ok,total:gaps.length,answers:sels.map(x=>x.value)};later()};
const _render=renderPost;renderPost=function(){_render();const r=postRes[cur];if(r){const e=$('res');if(e)e.textContent="Прошлый результат: "+r.ok+" / "+r.total}};
const _ans=answerDrill;answerDrill=function(a){_ans(a);if(!dq.length){drillBest={errors:dErr,missed:[...dMissed]};}later()};
document.addEventListener("click",e=>{if(e.target.closest("#cmBox"))later()},true);
$("sysend").onclick=async()=>{submitted=true;await save();$("sydone").style.display="inline";$("sysend").style.display="none"};
(async()=>{let a=null;if(CODE){try{const r=await rpc("get_my_hw",{p_code:CODE,p_lesson:LESSON});const d=r&&r[0];
  if(d){if(d.answers&&Object.keys(d.answers).length)a=d.answers;submitted=!!d.submitted;if(d.teacher_comment){$("tcomt").textContent=d.teacher_comment;$("tcom").style.display="block"}}}catch(e){}}
 if(!a){try{a=JSON.parse(localStorage.getItem("ge:"+LESSON+":"+(CODE||"preview"))||"null")}catch(e){}}
 if(a){addKarma((a.karma||0)-karma);Object.assign(postDone,a.postDone||{});Object.assign(postRes,a.postRes||{});drillBest=a.drill||null;
  if(a.commentsDone){ci=a.commentsDone;cOk=a.commentsOk||0;renderCm()}renderDots();renderPost()}
 if(submitted){$("sydone").style.display="inline";$("sysend").style.display="none"}
 ready=true;st(CODE?(a?"С возвращением! Твои результаты загружены.":"Результаты сохраняются автоматически."):"Предпросмотр — результаты сохраняются только на этом устройстве.",CODE?"var(--ok)":"")})();
})();
</script>'''.replace("__KEY__", KEY).replace("__CODE__", CODE)
i = s.rindex("</body>")
s = s[:i] + js + "\n" + s[i:]
open(OUT, "w", encoding="utf-8").write(s); print("ok")
