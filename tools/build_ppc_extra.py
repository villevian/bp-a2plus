import json, re

# ---------- data ----------
# Ex 6: fill the gap. subj = subject shown before the gap, aux = have/has, ing = verb-ing
E1 = [
 ("I’m so tired! I", "have", "working", "(work)", "all weekend.", "I",
  "“all weekend” + “I’m so tired” → the action started in the past, went on for some time and you feel the result now.",
  "«all weekend» + «I’m so tired» → дія почалася в минулому, тривала якийсь час, і результат відчуваєш зараз (втома)."),
 ("Where are you? I", "have", "waiting", "(wait)", "for you at the gate for 40 minutes!", "I",
  "“for 40 minutes” and I’m still waiting now → Present Perfect Continuous.",
  "«for 40 minutes» і я досі чекаю → Present Perfect Continuous."),
 ("We", "have", "living", "(live)", "in Portugal for five years.", "We",
  "We started living there 5 years ago and we still live there → PPC + for.",
  "Почали жити там 5 років тому і досі живемо → PPC + for."),
 ("My boss", "has", "travelling", "(travel)", "a lot for work recently.", "He",
  "“recently” = in the last weeks, up to now. My boss = he → <b>has</b> been.",
  "«recently» = останнім часом, до сьогодні. My boss = he → <b>has</b> been."),
 ("She", "has", "staying", "(stay)", "at this hotel since Monday. She loves it.", "She",
  "“since Monday” + she is still there → PPC. She → <b>has</b> been.",
  "«since Monday» + вона досі там → PPC. She → <b>has</b> been."),
 ("They", "have", "looking", "(look)", "for accommodation on Booking all morning.", "They",
  "“all morning” — the action has continued for the whole morning, up to now.",
  "«all morning» — дія триває весь ранок, аж до зараз."),
 ("I", "have", "driving", "(drive)", "for 20 years, but I still hate traffic.", "I",
  "I started driving 20 years ago and I still drive → PPC + for.",
  "Почала водити 20 років тому і досі воджу → PPC + for."),
]
# question item handled separately
E1Q = ("You look stressed.", "you", "speaking", "(speak)", "to clients all day?",
       "In a question, <b>have</b> goes before the subject: <b>Have you been</b> speaking…?",
       "У питанні <b>have</b> стоїть перед підметом: <b>Have you been</b> speaking…?")

# Ex 7: How long…? (prompt, question regex, answer subj variants, verb-ing, duration variants, model Q, model A full, model A short)
E2 = [
 ("you / learn English / 3 months", r"^how long have you been learning( english)?", ["i have", "i've"], "learning", ["three months", "3 months"],
  "How long have you been learning English?", "I have been learning it for three months.", "I've been learning it for three months."),
 ("your husband / use this ride-sharing app / a year", r"^how long has your husband been using", ["he has", "he's"], "using", ["a year", "one year", "1 year"],
  "How long has your husband been using this ride-sharing app?", "He has been using it for a year.", "He's been using it for a year."),
 ("they / stay in this business hotel / a week", r"^how long have they been staying", ["they have", "they've"], "staying", ["a week", "one week", "1 week"],
  "How long have they been staying in this business hotel?", "They have been staying there for a week.", "They've been staying there for a week."),
 ("you / work in your company / 5 years", r"^how long have you been working", ["i have", "i've"], "working", ["five years", "5 years"],
  "How long have you been working in your company?", "I have been working there for five years.", "I've been working there for five years."),
 ("we / sit in this café / an hour", r"^how long have we been sitting", ["we have", "we've"], "sitting", ["an hour", "one hour", "1 hour"],
  "How long have we been sitting in this café?", "We have been sitting here for an hour.", "We've been sitting here for an hour."),
]

# Ex 8: PPC or Past Simple. gaps: list of (accepted list, display correct, kind ppc|ps)
E3 = [
 ("Last month I {0} (go) to Poland. I {1} (stay) in a business hotel for one night.",
  [(["went"], "went", "ps"), (["stayed"], "stayed", "ps")],
  "“Last month” is a finished time in the past. The trip is over → Past Simple for both verbs.",
  "«Last month» — завершений час у минулому. Поїздка закінчилась → Past Simple для обох дієслів."),
 ("I {0} (stand) in this queue for 30 minutes and it isn’t moving!",
  [(["have been standing", "'ve been standing", "i have been standing", "i've been standing"], "have been standing / ’ve been standing", "ppc")],
  "“…and it isn’t moving” → I am still in the queue now. Started 30 minutes ago, still going → PPC.",
  "«…і вона не рухається» → я досі стою в черзі. Почалося 30 хвилин тому і триває → PPC."),
 ("Yesterday we {0} (meet) our client in person. It {1} (be) a great meeting.",
  [(["met"], "met", "ps"), (["was"], "was", "ps")],
  "“Yesterday” = finished time. The meeting is over → Past Simple (met, was).",
  "«Yesterday» = завершений час. Зустріч закінчилась → Past Simple (met, was)."),
 ("I’m still in Lisbon. I {0} (stay) here for a couple of days.",
  [(["have been staying", "'ve been staying", "i have been staying", "i've been staying"], "have been staying / ’ve been staying", "ppc")],
  "“I’m still in Lisbon” → the stay continues now → PPC + for.",
  "«Я досі в Лісабоні» → перебування триває зараз → PPC + for."),
 ("Last summer we {0} (go) on a cruise.",
  [(["went"], "went", "ps")],
  "“Last summer” = finished time → Past Simple.",
  "«Last summer» = завершений час → Past Simple."),
 ("She {0} (ask) everyone for help all morning, but nobody knows the answer.",
  [(["has been asking", "'s been asking", "she has been asking", "she's been asking"], "has been asking / ’s been asking", "ppc")],
  "“all morning” + “nobody knows” (present) → she is still asking → PPC. She → <b>has</b>.",
  "«all morning» + «nobody knows» (теперішній час) → вона досі питає → PPC. She → <b>has</b>."),
]

# Ex 9: find and fix. (wrong, accepted full forms, explanation en, ua)
E4 = [
 ("I have been waiting you for an hour.", ["i have been waiting for you for an hour"],
  "We say <b>wait for</b> someone. Without <i>for</i> the sentence is wrong.",
  "Кажемо <b>wait for</b> someone. Без <i>for</i> — помилка."),
 ("We have been live here for one year.", ["we have been living here for one year", "we have been living here for a year"],
  "After <b>been</b> the verb always takes <b>-ing</b>: been living.",
  "Після <b>been</b> дієслово завжди з <b>-ing</b>: been living."),
 ("He has been working here during ten years.", ["he has been working here for ten years", "he has been working here for 10 years"],
  "For a period of time we use <b>for</b>: for ten years. <i>During</i> answers “when?”, not “how long?”.",
  "Для тривалості — <b>for</b>: for ten years. <i>During</i> відповідає на «коли?», а не «як довго?»."),
 ("I have been staying in Poland last month.", ["i stayed in poland last month"],
  "“Last month” is finished time → Past Simple: I stayed. PPC can’t go with last month / yesterday / ago.",
  "«Last month» — завершений час → Past Simple: I stayed. PPC не вживаємо з last month / yesterday / ago."),
 ("How long you have been driving?", ["how long have you been driving"],
  "In questions <b>have</b> goes before the subject: How long <b>have you</b> been driving?",
  "У питанні <b>have</b> стоїть перед підметом: How long <b>have you</b> been driving?"),
 ("They has been planning this business trip for weeks.", ["they have been planning this business trip for weeks"],
  "They → <b>have</b>. <i>Has</i> is only for he / she / it.",
  "They → <b>have</b>. <i>Has</i> — тільки для he / she / it."),
]

E5 = [
 ("How long have you been living in Portugal?", "I have been living in Portugal for … years. / I’ve been living here since 20…"),
 ("How long have you been driving? Do you still enjoy it?", "I’ve been driving for … years. I still enjoy it, but I hate traffic."),
 ("What have you been doing at work recently?", "Recently I’ve been working on … / I have been meeting a lot of clients."),
 ("Have you been travelling a lot recently? Where?", "Yes, I’ve been travelling a lot — I went to … last month. / No, I haven’t been travelling much."),
 ("How long have you been working with AI tools at work?", "I’ve been using AI tools for about … months. I use them to …"),
 ("Some people say business trips are a waste of time. What have you been doing instead: video calls or meeting in person?", "Recently I’ve been having more video calls, because … But I think meeting in person is better for …"),
]

# ---------- HTML ----------
CSS = """
.rule{margin:6px 0 0 40px;background:#e6f4f4;border-radius:6px;padding:12px 16px;font-size:15px;line-height:1.55;max-width:760px}
.rule b{font-weight:600}.rule .ua{color:#555}
.rule table{border-collapse:collapse;margin:6px 0;font-size:14.5px}
.rule td{padding:3px 12px 3px 0}
.fb .h2{margin-top:4px}
.fb .alt{margin-top:5px;font-size:13.5px;color:#2e7d32}
.qa{margin-left:40px}
.qa .p{font-weight:500;margin:10px 0 4px}
.qa input{display:block;margin:4px 0}
"""

def norm_py(s): return s


def gap_input(k, w=190):
    return f'<input class="g" style="width:{w}px" data-k="{k}" autocomplete="off">'


blk = []
blk.append('<div class="sec-h">Grammar: Present Perfect Continuous</div>')
blk.append('''<div class="ex"><div class="q"><span class="n">★</span><span>How it works</span></div>
<div class="rule">
<b>Form:</b> have / has + been + verb-ing
<table><tr><td>I / you / we / they</td><td><b>have been working</b></td><td>= <b>’ve been working</b></td></tr>
<tr><td>he / she / it</td><td><b>has been working</b></td><td>= <b>’s been working</b></td></tr>
<tr><td>Question</td><td colspan="2"><b>How long have you been</b> working here?</td></tr></table>
<b>Use:</b> an action started in the past and is <b>still going on now</b> (or just stopped and you see the result).<br>
<b>for</b> + a period (for two hours, for five years) · <b>since</b> + a start point (since Monday, since 2020)<br>
<span class="ua">🇺🇦 Дія почалася в минулому і <b>триває досі</b>. Якщо дія вже закінчилась (yesterday, last month, ago) — це Past Simple.</span><br>
<span class="ua">🇺🇦 Можна писати і повністю (<b>I have been</b>), і скорочено (<b>I’ve been</b>) — обидва варіанти правильні.</span>
</div></div>''')

# Ex 6
html_e1 = ""
FBH = lambda k: f'<div class="fb" id="fb_{k}"><div class="h"></div><div class="d"></div></div>'
lis = []
for i, (pre, aux, ing, base, post, pron, en, ua) in enumerate(E1, 1):
    lis.append(f'<li><span class="i">{i}</span><span class="t">{pre} {gap_input(f"p1_{i}")} {base} {post}{FBH(f"p1_{i}")}</span></li>')
pre, pron, ing, base, post, en, ua = E1Q
lis.append(f'<li><span class="i">8</span><span class="t">{pre} {gap_input("p1_8a", 80)} {pron} {gap_input("p1_8b", 150)} {base} {post}{FBH("p1_8")}</span></li>')
blk.append(f'''<div class="ex"><div class="q"><span class="n">6</span><span>Complete with have / has been + -ing.<small>You can write the full form (have been working) or the short form (’ve been working).</small></span></div>
<ol class="it">{"".join(lis)}</ol><div class="chk"><button onclick="chkP1()">Check</button><span id="r_p1"></span></div></div>''')

# Ex 7
lis = []
for i, (pr, *_rest) in enumerate(E2, 1):
    lis.append(f'''<li><span class="i">{i}</span><span class="t"><b style="font-weight:500">{pr}</b>
<input class="g wide" data-k="p2q_{i}" placeholder="Question: How long …?" autocomplete="off">
<input class="g wide" data-k="p2a_{i}" placeholder="Answer: I’ve been … for …" autocomplete="off">{FBH(f"p2_{i}")}</span></li>''')
blk.append(f'''<div class="ex"><div class="q"><span class="n">7</span><span>How long…? Write the question and the answer with <i>for</i>.<small>Example: you / wait for the coach / 2 hours → How long have you been waiting for the coach? — I’ve been waiting for it for two hours.</small></span></div>
<ol class="it">{"".join(lis)}</ol><div class="chk"><button onclick="chkP2()">Check</button><span id="r_p2"></span></div></div>''')

# Ex 8
lis = []
for i, (s, gaps, en, ua) in enumerate(E3, 1):
    t = s
    for j in range(len(gaps)):
        t = t.replace("{" + str(j) + "}", gap_input(f"p3_{i}_{j}", 170))
    lis.append(f'<li><span class="i">{i}</span><span class="t">{t}{FBH(f"p3_{i}")}</span></li>')
blk.append(f'''<div class="ex"><div class="q"><span class="n">8</span><span>Present Perfect Continuous or Past Simple?<small>Still going on now → PPC. Finished (yesterday, last month, ago) → Past Simple.</small></span></div>
<ol class="it">{"".join(lis)}</ol><div class="chk"><button onclick="chkP3()">Check</button><span id="r_p3"></span></div></div>''')

# Ex 9
lis = []
for i, (w, *_r) in enumerate(E4, 1):
    lis.append(f'<li><span class="i">{i}</span><span class="t"><s style="color:#c0392b">{w}</s><br><input class="g wide" data-k="p4_{i}" placeholder="Write the correct sentence" autocomplete="off">{FBH(f"p4_{i}")}</span></li>')
blk.append(f'''<div class="ex"><div class="q"><span class="n">9</span><span>Find and fix the mistake. Write the whole correct sentence.</span></div>
<ol class="it">{"".join(lis)}</ol><div class="chk"><button onclick="chkP4()">Check</button><span id="r_p4"></span></div></div>''')

# Ex 10
sp = "".join(f'<div class="msg"><div class="bubble"><b>Question {i}</b>{q}</div><textarea placeholder="Answer in 2–3 sentences, or say it aloud…"></textarea><div class="chk" style="margin-left:0"><button class="l" onclick="this.parentNode.nextElementSibling.classList.toggle(\'show\')">Show an example</button></div><div class="model"><b>Example:</b> {m}</div></div><br>' for i, (q, m) in enumerate(E5, 1))
blk.append(f'<div class="ex"><div class="q"><span class="n">10</span><span>Speaking: talk about yourself. Say your answer aloud or write it. We’ll discuss it in class.</span></div>{sp}</div>')

JS = r"""
<script>
const PPC={E1:__E1__,E1Q:__E1Q__,E2:__E2__,E3:__E3__,E4:__E4__};
const nz=s=>s.toLowerCase().replace(/[’‘`]/g,"'").replace(/[.!?,]/g," ").replace(/\s+/g," ").trim().replace(/traveling/g,"travelling").replace(/ride sharing|ridesharing/g,"ride-sharing").replace(/cafe/g,"café");
const SHORT={"i have":"i've","you have":"you've","we have":"we've","they have":"they've","he has":"he's","she has":"she's"};
function variants(full){const v=[full];for(const k in SHORT){if(full.includes(k))v.push(full.replace(k,SHORT[k]))}return v}
function setFB(k,ok,head,parts){const f=document.getElementById("fb_"+k);f.className="fb show "+(ok?"ok":"no");f.querySelector(".h").innerHTML=head;f.querySelector(".d").innerHTML=parts.join("")}
const EN=t=>`<div class="en">${t}</div>`,UA=t=>`<div class="ua">${t}</div>`,ALT=t=>`<div class="alt">✓ ${t}</div>`;
function mark(el,ok){el.classList.remove("right","wrong");el.classList.add(ok?"right":"wrong")}
/* diagnose a PPC verb form: returns [en,ua] or null */
function diag(v,aux,ing,subjHas){
 v=nz(v);if(!v)return["You didn’t write anything.","Ви нічого не написали."];
 if(!/been/.test(v))return["The word <b>been</b> is missing. Form: have/has + <b>been</b> + -ing.","Пропущено <b>been</b>. Формула: have/has + <b>been</b> + -ing."];
 if(!new RegExp(ing).test(v)){if(/been \w+(ed)?$/.test(v)||/been \w+$/.test(v))return[`After <b>been</b> use the <b>-ing</b> form: been <b>${ing}</b>.`,`Після <b>been</b> потрібна форма з <b>-ing</b>: been <b>${ing}</b>.`];}
 if(aux==="has"&&/\bhave\b|'ve/.test(v))return["He / she / it → <b>has</b> been, not <i>have</i>.","He / she / it → <b>has</b> been, а не <i>have</i>."];
 if(aux==="have"&&/\bhas\b|'s been/.test(v))return["I / you / we / they → <b>have</b> been, not <i>has</i>.","I / you / we / they → <b>have</b> been, а не <i>has</i>."];
 if(!/\bhave\b|\bhas\b|'ve|'s/.test(v))return["<b>have</b> or <b>has</b> is missing before been.","Перед been пропущено <b>have</b> або <b>has</b>."];
 return null;
}
function chkP1(){let n=0;
 PPC.E1.forEach(([pre,aux,ing,base,post,pron,en,ua],i)=>{const k="p1_"+(i+1),el=document.querySelector(`[data-k="${k}"]`);const v=nz(el.value);
  const sh=aux==="have"?"'ve":"'s";const full=`${aux} been ${ing}`,short=`${sh} been ${ing}`;
  const p=pron.toLowerCase(),acc=[full,short,`${p} ${full}`,`${p}${sh} been ${ing}`];if(pre.endsWith("My boss"))acc.push(`my boss ${full}`,`my boss's been ${ing}`);
  const ok=acc.includes(v);if(ok)n++;mark(el,ok);
  const d=ok?null:diag(el.value,aux,ing);
  setFB(k,ok,ok?"✓ Correct! / Правильно!":"✗ Not quite. / Не зовсім.",[...(d?[EN(d[0]),UA(d[1])]:[]),EN(en),UA(ua),ALT(`Correct: <b>${full}</b> or <b>${sh.replace("'","’")} been ${ing}</b>`)])});
 const [pre,pron,ing,base,post,en,ua]=PPC.E1Q;const a=document.querySelector('[data-k="p1_8a"]'),b=document.querySelector('[data-k="p1_8b"]');
 const ok8=nz(a.value)==="have"&&nz(b.value)===`been ${ing}`;if(ok8)n++;mark(a,nz(a.value)==="have");mark(b,nz(b.value)===`been ${ing}`);
 let d8=[];if(nz(a.value)!=="have")d8=[EN("The question starts with <b>Have</b> (you = have)."),UA("Питання починається з <b>Have</b> (you = have).")];
 else if(nz(b.value)!==`been ${ing}`)d8=[EN(`After the subject: <b>been ${ing}</b>.`),UA(`Після підмета: <b>been ${ing}</b>.`)];
 setFB("p1_8",ok8,ok8?"✓ Correct! / Правильно!":"✗ Not quite. / Не зовсім.",[...d8,EN(en),UA(ua),ALT("Correct: <b>Have</b> you <b>been speaking</b> to clients all day?")]);
 document.getElementById("r_p1").textContent=n+" / 8 correct"}
function chkP2(){let n=0;
 PPC.E2.forEach(([pr,qre,subs,ing,durs,mq,ma,mas],i)=>{const qi=document.querySelector(`[data-k="p2q_${i+1}"]`),ai=document.querySelector(`[data-k="p2a_${i+1}"]`);
  const q=nz(qi.value),a=nz(ai.value);const qok=new RegExp(qre).test(q);
  const aok=subs.some(s=>a.includes(`${s} been ${ing}`))&&durs.some(d=>a.includes("for "+d));
  mark(qi,qok);mark(ai,aok);const ok=qok&&aok;if(ok)n++;const parts=[];
  if(!qok){if(/^how long (you|your|they|we)/.test(q))parts.push(EN("Word order: <b>How long + have/has + subject + been + -ing?</b>"),UA("Порядок слів: <b>How long + have/has + підмет + been + -ing?</b>"));
   else if(q&&!/been/.test(q))parts.push(EN("The question needs <b>been</b>: How long have you <b>been</b> …ing?"),UA("У питанні потрібне <b>been</b>: How long have you <b>been</b> …ing?"));
   else if(/^how long have (your husband|he|she)/.test(q))parts.push(EN("Your husband = he → <b>has</b>: How long <b>has</b> your husband been…?"),UA("Your husband = він → <b>has</b>: How long <b>has</b> your husband been…?"));
   else parts.push(EN("Check the question: How long + have/has + subject + been + verb-ing?"),UA("Перевірте питання: How long + have/has + підмет + been + дієслово-ing?"))}
  if(!aok){if(a&&/\bsince\b/.test(a))parts.push(EN("<b>since</b> is for a start point (since May). For a period → <b>for</b>."),UA("<b>since</b> — для точки початку (since May). Для тривалості → <b>for</b>."));
   else if(a&&!/\bfor\b/.test(a))parts.push(EN("For a period of time use <b>for</b>: for three months, for a year."),UA("Для тривалості вживаємо <b>for</b>: for three months, for a year."));
   else parts.push(EN("The answer: subject + have/has been + -ing + for + period."),UA("Відповідь: підмет + have/has been + -ing + for + період."))}
  setFB("p2_"+(i+1),ok,ok?"✓ Correct! / Правильно!":"✗ Not quite. / Не зовсім.",[...parts,ALT(`${mq}<br>${ma} / ${mas}`)])});
 document.getElementById("r_p2").textContent=n+" / 5 correct"}
function chkP3(){let n=0;
 PPC.E3.forEach(([s,gaps,en,ua],i)=>{let all=true;const parts=[];
  gaps.forEach(([acc,disp,kind],j)=>{const el=document.querySelector(`[data-k="p3_${i+1}_${j}"]`);const v=nz(el.value);const ok=acc.includes(v);mark(el,ok);if(!ok){all=false;
   if(kind==="ps"&&/been/.test(v))parts.push(EN("This action is finished (time in the past) → <b>Past Simple</b>, not have been …ing."),UA("Дія закінчилась (час у минулому) → <b>Past Simple</b>, а не have been …ing."));
   else if(kind==="ppc"&&v&&!/been/.test(v))parts.push(EN("This action is still going on now → <b>have/has been + -ing</b>, not Past Simple."),UA("Дія досі триває → <b>have/has been + -ing</b>, а не Past Simple."));
   else if(kind==="ps"&&v)parts.push(EN(`Check the Past Simple form: <b>${disp}</b> (irregular verbs: go → went, meet → met, be → was).`),UA(`Перевірте форму Past Simple: <b>${disp}</b> (неправильні дієслова: go → went, meet → met, be → was).`))}});
  if(all)n++;setFB("p3_"+(i+1),all,all?"✓ Correct! / Правильно!":"✗ Not quite. / Не зовсім.",[...parts,EN(en),UA(ua),ALT("Correct: "+gaps.map(g=>"<b>"+g[1]+"</b>").join(", "))])});
 document.getElementById("r_p3").textContent=n+" / 6 correct"}
function chkP4(){let n=0;
 PPC.E4.forEach(([w,accs,en,ua],i)=>{const el=document.querySelector(`[data-k="p4_${i+1}"]`);const v=nz(el.value);const all=accs.flatMap(variants);const ok=all.includes(v);if(ok)n++;mark(el,ok);
  const fix=accs[0].charAt(0).toUpperCase()+accs[0].slice(1);const sv=variants(accs[0]);const shortv=sv.length>1?sv[1].charAt(0).toUpperCase()+sv[1].slice(1):null;
  setFB("p4_"+(i+1),ok,ok?"✓ Correct! / Правильно!":"✗ Not quite. / Не зовсім.",[EN(en),UA(ua),ALT(`Correct: <b>${fix}.</b>${shortv?` or <b>${shortv.replace(/'/g,"’")}.</b>`:""}`)])});
 document.getElementById("r_p4").textContent=n+" / 6 correct"}
</script>"""
JS = (JS.replace("__E1__", json.dumps(E1, ensure_ascii=False)).replace("__E1Q__", json.dumps(E1Q, ensure_ascii=False))
      .replace("__E2__", json.dumps(E2, ensure_ascii=False)).replace("__E3__", json.dumps(E3, ensure_ascii=False))
      .replace("__E4__", json.dumps(E4, ensure_ascii=False)))

path = '/home/claude/bp-larysa/lessons/1-1/all/extra.html'
s = open(path).read()
assert 'Grammar: Present Perfect Continuous' not in s
s = s.replace('</style>', CSS + '</style>', 1)
s = s.replace('</main>', "\n".join(blk) + '\n</main>', 1)
s = s.replace('</body>', JS + '\n</body>', 1)
open(path, 'w').write(s)
print("ok")
