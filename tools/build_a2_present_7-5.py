"""Business Partner A2 · 7.5 Business workshop: The big contract — PRESENTATION DECK (online pitch, screen share).
BrightCode (Pavlo's IT studio) vs AppNova and WebGiant for the GreenBox contract. Each slide has a TASK under it (not a script):
what to say, what to COMPARE, the Unit 7 words and book phrases to use, and a hidden example. Teacher ticks Unit 7 words as the student uses them.
Usage: python3 build_a2_present_7-5.py OUT.html
"""
import sys, os, json
OUT = sys.argv[1]
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "build_a2_present_7-4.py")).read()
CSS = src[src.index("<style>"):src.index("</style>") + 8]
C = "#e07a2f"
def S(kind, title, body, task, cmp, use, ex):
    return {"k": kind, "t": title, "b": body, "task": task, "cmp": cmp, "use": use, "ex": ex}
SL = [
 S("title", "BrightCode × GreenBox", "<div class='sub'>Our offer: a mobile app, an online shop and a payment system</div><div class='by'>Pavlo · Project Manager · BrightCode</div>",
   "Greet the client, say who you are and thank them for attending.", "",
   ["Good morning, everyone.", "My name is … and I’m …", "Thank you for attending."],
   "Good morning, everyone. My name is Pavlo, and I’m a project manager at BrightCode. Thank you for attending this presentation."),
 S("list", "Today’s agenda", "<ol><li>About BrightCode</li><li>Our services</li><li>Price: what you get for your money</li><li>Speed and quality</li><li>Why BrightCode</li><li>Questions</li></ol>",
   "Say the aim of the presentation and give the plan. Use First / Then / Finally.", "",
   ["The aim of today’s presentation is to …", "First, … Then, … Finally, …", "a question and answer session"],
   "The aim of today’s presentation is to show you our offer for GreenBox. First, I’ll tell you about our company. Then I’ll explain our services and our price. Finally, we’ll have a question and answer session."),
 S("stats", "About BrightCode", "<div class='kp'><div><b>Kyiv</b>based in</div><div><b>2017</b>started</div><div><b>45</b>people</div><div><b>140</b>projects</div></div><p style='text-align:center;margin-top:3cqi;font-size:2.6cqi;color:#6d6e70'>WebGiant: 2,000 projects · AppNova: 40 projects</p>",
   "Start the main part. Talk about the company: where, when, how big.",
   "Compare BrightCode with WebGiant and AppNova. Are we the biggest? Do we have more experience than AppNova?",
   ["So, let’s start with …", "We’re based in …", "We started in …", "bigger than / smaller than", "more experience than", "the biggest provider"],
   "So, let’s start with our company. We’re based in Kyiv and we started in 2017. We aren’t the biggest provider — WebGiant is bigger. But we have more experience than AppNova: 140 projects, not 40."),
 S("icons", "Our services", "<div class='ic' style='grid-template-columns:repeat(3,1fr)'><div>📱<b>Mobile app</b></div><div>🛒<b>Online shop</b></div><div>💳<b>Payment system</b></div><div>🗄️<b>Secure database</b></div><div>🤖<b>AI chat assistant</b></div><div>🛟<b>Support 24/7</b></div></div>",
   "Move on to your services. Say what you provide and what you can do for GreenBox.", "",
   ["Let’s move on to …", "We provide a range of …", "We can …", "e-commerce", "a payment system", "a database"],
   "Let’s move on to our services. We provide a range of e-commerce services: a mobile app, an online shop and a payment system. We can also add an AI chat assistant, and we keep all customer data in a secure database."),
 S("chart", "Price: the fee for the project", "<div class='bars'><div style='--h:62%;background:#e07a2f'><span>BrightCode</span><em>€38,000</em></div><div style='--h:47%;background:#9aa5b1'><span>AppNova</span><em>€29,000*</em></div><div style='--h:90%;background:#9aa5b1'><span>WebGiant</span><em>€55,000</em></div></div><p class='cap'>* + additional fees (see the next slide)</p>",
   "Talk about the price. Be honest: we are not the cheapest on this slide!",
   "Compare the three fees. Who is the cheapest? Who is the most expensive? Is AppNova really the cheapest? (Look at the *.)",
   ["As you can see on this slide, …", "cheaper than / more expensive than", "the cheapest / the most expensive", "a fixed fee"],
   "As you can see on this slide, AppNova looks the cheapest, and WebGiant is the most expensive. Our fee is €38,000. It’s more expensive than AppNova, but it’s a fixed fee — the price doesn’t change."),
 S("table", "What does the fee include?", "<table><tr><th></th><th>BrightCode</th><th>AppNova</th><th>WebGiant</th></tr><tr><td>Design + app + online shop</td><td>✅</td><td>✅</td><td>✅</td></tr><tr><td>Payment system</td><td>✅</td><td>+ €6,000</td><td>✅</td></tr><tr><td>Support</td><td>✅ 6 months</td><td>€900 / month</td><td>✅ 12 months</td></tr><tr><td>Cancellation</td><td>free (14 days)</td><td>early termination fee €5,000</td><td>annual contract</td></tr><tr><td><b>Real price (first year)</b></td><td><b>€38,000</b></td><td><b>€45,800</b></td><td><b>€55,000</b></td></tr></table>",
   "Explain what each fee includes. Show the hidden fees in AppNova’s offer.",
   "Compare what you get for your money. Which offer has hidden fees? Which offer is the best value for money in the first year?",
   ["The fee includes …", "There’s an additional fee for …", "a hidden fee", "a monthly fee", "an early termination fee", "the small print", "value for money"],
   "Our fee includes the payment system and six months of support. AppNova charges an additional fee of €6,000 for the payment system and a monthly fee of €900 for support. And look at the small print: there’s an early termination fee. So in the first year, AppNova is more expensive than BrightCode. We offer the best value for money."),
 S("chart", "Speed and quality", "<div class='bars'><div style='--h:40%;background:#e07a2f'><span>BrightCode</span><em>8 weeks ⭐4.8</em></div><div style='--h:50%;background:#9aa5b1'><span>AppNova</span><em>10 weeks ⭐4.1</em></div><div style='--h:80%;background:#9aa5b1'><span>WebGiant</span><em>16 weeks ⭐4.5</em></div></div><p class='cap'>Weeks to the first version · customer rating</p>",
   "Talk about speed and quality. GreenBox needs the app before the spring sale (in 10 weeks).",
   "Compare: who is the fastest? Who is the slowest? Who has the most satisfied customers? Can WebGiant finish before the spring sale?",
   ["faster than / slower than", "the fastest / the slowest", "the most reliable", "satisfied customers", "service reliability"],
   "We are the fastest: the first version will be ready in eight weeks. AppNova is slower — ten weeks — and WebGiant needs sixteen weeks, so they can’t finish before your spring sale. We also have the most satisfied customers: our rating is 4.8."),
 S("list", "Why BrightCode?", "<ul><li>💶 The best value for money — a fixed fee, no hidden fees</li><li>⚡ The fastest: ready before your spring sale</li><li>⭐ The most satisfied customers: 4.8</li><li>🛟 Support 24/7 in a chat, in Ukrainian and English</li></ul>",
   "Give your recommendation: why should GreenBox choose BrightCode? Choose your three strongest arguments.",
   "Compare one last time: what can BrightCode do better than AppNova and WebGiant?",
   ["We offer the best …", "We can …", "better than", "no hidden fees", "a guarantee"],
   "So why BrightCode? We offer the best value for money: a fixed fee with no hidden fees. We are the fastest, so your app will be ready before the spring sale. And our customers are the most satisfied — and we give a guarantee: if we are late, the support is free for one more year."),
 S("end", "Thank you!", "<div class='sub'>Any questions?</div><div class='by'>pavlo@brightcode.example</div>",
   "Finish the presentation and invite questions. Then answer the client’s questions.", "",
   ["So, that’s the end of my presentation.", "Thank you for listening.", "Does anyone have any questions?"],
   "So, that’s the end of my presentation. Thank you for listening. Does anyone have any questions?")]
WORDS = [("7.2 Fees", ["fee", "the fee includes", "fixed fee", "monthly fee", "annual fee", "additional fee", "hidden fee", "cancellation fee", "early termination fee", "the small print", "free trial", "guarantee"]),
         ("7.3 Providers & superlatives", ["provider", "value for money", "service reliability", "satisfied customers", "the best", "the cheapest", "the fastest", "the most reliable", "the most expensive", "the biggest"]),
         ("7.1 Comparing", ["cheaper than", "more expensive than", "faster than", "bigger than", "better than"]),
         ("7.4 Presenting", ["Thank you for attending", "The aim of …", "First / Then / Finally", "Let’s start with", "Let’s move on to", "We’re based in", "We provide a range of", "As you can see", "Any questions?"])]
QA = ["Why should we pay more than AppNova’s price?", "WebGiant is the biggest provider in Europe. Why are you better?", "What does your fee include exactly?", "Are there any hidden fees?",
      "What happens if you are late?", "Can we cancel the contract?", "Can you give us a free trial or a discount?", "Who will be our contact person?"]
HTML = r"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>7.5 The big contract — presentation</title><link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@400;500;600&display=swap" rel="stylesheet">
""" + CSS + r"""<style>
.task{background:#fff;border:1.5px solid #e07a2f;border-radius:8px;padding:12px 14px;font-size:15.5px;line-height:1.5}.task h4{margin:0 0 4px;font-size:13px;text-transform:uppercase;color:#b8571a;letter-spacing:.4px}
.cmp{background:#fff4ea;border-radius:8px;padding:10px 14px;margin-top:10px;font-size:15.5px}.cmp h4{margin:0 0 4px;font-size:13px;text-transform:uppercase;color:#b8571a}
.use{margin-top:10px}.use h4{margin:0 0 4px;font-size:13px;text-transform:uppercase;color:#2a5fb0}.use span{display:inline-block;background:#e3eefb;color:#2a5fb0;border-radius:14px;padding:3px 10px;margin:3px;font-size:14px;cursor:pointer}
.exb{margin-top:10px}.exb .m{display:none;background:#fffdf3;border:1.5px solid #f0d68a;border-radius:8px;padding:10px 12px;margin-top:6px;font-size:15px}.exb .m.on{display:block}
.chk{margin-top:18px;background:#fff;border:1px solid #d5d6d7;border-radius:10px;padding:12px 16px}.chk h3{margin:0 0 4px;font-size:16px}.chk h5{margin:10px 0 2px;color:#6d6e70;font-size:13px;text-transform:uppercase}
.chk label{display:inline-flex;align-items:center;gap:5px;border:1px solid #d5d6d7;border-radius:14px;padding:3px 10px;margin:3px;font-size:14px;cursor:pointer;background:#fff}.chk label.on{background:#e9f8ee;border-color:#16a34a;color:#15803d}
.chk label input{display:none}.cnt{font-weight:600;color:#15803d}
.qa{margin-top:18px;background:#fff;border:1px solid #d5d6d7;border-radius:10px;padding:12px 16px}.qa li{margin:4px 0}
</style></head><body>
<header><div class="n">7.5</div><h1>The big contract: your presentation</h1><div class="tag">ONLINE PITCH</div></header>
<div class="wrap"><div class="top"><a href="lesson.html">← Lesson 7.5</a> · <a href="../../../index.html">Contents</a></div>
<div class="who">🎯 You are <b>Pavlo, a project manager at BrightCode</b>. GreenBox (online grocery delivery) wants a mobile app, an online shop and a payment system. Three companies want the contract. Today you present BrightCode’s offer online (5 minutes). Your teacher is <b>Olena, Head of Digital at GreenBox</b>.</div>
<p class="hint">There is no script — read the <b>task</b> under each slide and speak. Use the words in blue (click to listen). Stuck? Click <b>💡 Example</b>. Keyboard: → / ← · F full screen.</p>
<div class="stage"><div><div class="slide" id="slide"></div>
<div class="ctl"><button class="btn l" onclick="go(-1)">← Back</button><button class="btn" onclick="go(1)">Next →</button><button class="btn l" onclick="fs()">⛶ Full screen</button>
<button class="btn l" onclick="timer()">⏱ 5:00</button><span class="tm" id="tm"></span></div></div>
<div><div class="task"><h4>Your task</h4><div id="task"></div></div><div class="cmp" id="cmpB"><h4>⚖️ Compare</h4><div id="cmp"></div></div>
<div class="use"><h4>Use</h4><div id="use"></div></div><div class="exb"><button class="btn l" onclick="$('ex').classList.toggle('on')">💡 Example</button><div class="m" id="ex"></div></div></div></div>
<div class="chk"><h3>✅ Unit 7 words — teacher’s checklist <span class="cnt" id="cnt"></span></h3><p class="hint" style="margin:0">Click a word when Pavlo uses it. After the presentation: which words are still grey? Use them in your answers to the questions.</p><div id="chk"></div><button class="btn l" style="margin-top:8px" onclick="reset()">Reset</button></div>
<div class="qa"><h3 style="margin:0">❓ Question and answer session (Olena asks)</h3><ol>__QA__</ol></div></div>
<footer>Business Partner A2 · Unit 7 · BrightCode, GreenBox, AppNova and WebGiant are invented companies. Valentyna Hordiienko · Middle Learning Architect</footer>
<script>
const SL=__SL__,W=__W__;let I=0,T=null;
const $=id=>document.getElementById(id);
function speak(t){if(!("speechSynthesis" in window))return;speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(t.replace(/…/g,""));u.lang="en-GB";u.rate=.9;speechSynthesis.speak(u)}
function show(){const s=SL[I],el=$("slide");el.className="slide "+(s.k==="table"?"list":s.k);el.style.setProperty("--c","#e07a2f");
 el.innerHTML='<div class="bar"></div><h2>'+s.t+'</h2><div class="body">'+s.b+'</div><div class="pg">'+(I+1)+' / '+SL.length+'</div>';
 $("task").textContent=s.task;$("cmpB").style.display=s.cmp?"block":"none";$("cmp").textContent=s.cmp;
 $("use").innerHTML=s.use.map(u=>'<span>'+u+'</span>').join("");$("use").querySelectorAll("span").forEach(x=>x.onclick=()=>speak(x.textContent));
 $("ex").textContent=s.ex;$("ex").classList.remove("on")}
function go(k){I=Math.max(0,Math.min(SL.length-1,I+k));show()}
function fs(){const el=$("slide");if(document.fullscreenElement)document.exitFullscreen();else if(el.requestFullscreen)el.requestFullscreen()}
function timer(){clearInterval(T);let t=300;const f=()=>{$("tm").textContent=Math.floor(t/60)+":"+String(t%60).padStart(2,"0")+(t<=0?" ⏰ Time!":"");if(t--<=0)clearInterval(T)};f();T=setInterval(f,1000)}
const KEY="bp-a2-7-5-chk";let ON={};try{ON=JSON.parse(localStorage.getItem(KEY)||"{}")}catch(e){}
function drawChk(){let n=0,tot=0;$("chk").innerHTML=W.map(([h,ws])=>'<h5>'+h+'</h5>'+ws.map(w=>{tot++;if(ON[w])n++;return '<label class="'+(ON[w]?"on":"")+'" data-w="'+w+'">'+(ON[w]?"✔ ":"")+w+'</label>'}).join("")).join("");
 $("cnt").textContent=n+" / "+tot;$("chk").querySelectorAll("label").forEach(l=>l.onclick=()=>{const w=l.dataset.w;ON[w]=!ON[w];try{localStorage.setItem(KEY,JSON.stringify(ON))}catch(e){}drawChk()})}
function reset(){ON={};try{localStorage.removeItem(KEY)}catch(e){}drawChk()}
document.addEventListener("keydown",e=>{if(e.key==="ArrowRight"||e.key===" ")go(1);if(e.key==="ArrowLeft")go(-1);if(e.key==="f"||e.key==="F")fs()});
$("slide").addEventListener("click",()=>{if(document.fullscreenElement)go(1)});
show();drawChk();
</script></body></html>"""
h = HTML.replace("__SL__", json.dumps(SL, ensure_ascii=False)).replace("__W__", json.dumps(WORDS, ensure_ascii=False)).replace("__QA__", "".join("<li>%s</li>" % q for q in QA))
h = h.replace("#3b7dd8", "#e07a2f") if False else h
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True); open(OUT, "w").write(h); print("ok", OUT, len(h))
