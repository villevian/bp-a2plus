"""Business Partner B2 · 6.1 Ethical choices — bridge version: book video & exercises + ultra-fast fashion apps (Shein, Temu).
Structure mirrors the coursebook: Lead-in 1 · VIDEO 2–4 · Vocabulary 5–8 · PROJECT 9A–B, 10 · Self-assessment.
Usage: python3 build_b2_lesson_6-1.py OUT.html
"""
import sys, json
OUT = sys.argv[1]
ACC, ACC2, DARK = "#5b5fc7", "#e8e9fa", "#4044a8"

LEAD = ["How interested are you in fashion?", "Where do you usually buy your clothes and shoes — in shops, on websites or in apps?",
        "Where were your clothes and shoes made? (Hint: check the labels!)", "Are there any fast fashion brands that you never buy? Why?",
        "How ethical are the brands that you are wearing?"]
LEAD_UP = ["Have you ever bought anything from Shein or Temu? What made you buy?", "What does a shopping app do to make you buy more than you planned?",
           "Would you design or build a ‘spin the wheel’ discount game for an app? Why / Why not?", "Who is responsible for an unethical app: the company, the designer, the developer or the user?"]
SPK = ["the job seeker", "the clothing producer", "the garment worker", "the expert from Redress (NGO)", "Shein (statement)"]
V2 = [("Who explains how workers in Guangzhou choose a job?", 1, "0:41"), ("Who says the clothes are of good quality and very stretchy?", 2, "1:40"),
      ("Who works from 8 or 9 in the morning until midnight?", 3, "3:15"), ("Who says that consumers in the West are driving the demand?", 4, "4:48"),
      ("Who says the on-demand model helps to limit waste?", 5, "5:21")]
SUM = [("Guangzhou is one of China’s garment-making capitals, with some", "50,000|50000|50 000", "clothes-related businesses. Shein doesn’t run any of these factories. It relies on an informal network of"),
       ("", "independent workshops|independent suppliers|workshops", "that produce more than"),
       ("", "6,000 new items|6,000|6000|6,000 new clothing items|6000 new items", "a day. Its"),
       ("", "on-demand|on demand|on-demand business", "model tests small batches online, and items that sell well are immediately"),
       ("", "reordered|re-ordered", ". When a product goes viral, Shein orders it from"),
       ("", "multiple factories|several factories|many factories", ", which creates competition and drives"),
       ("", "prices down|prices|the price down", ". Many workers are"),
       ("", "paid per piece|paid by the piece|paid per item", ", sometimes only 6 to 24 cents per item. Shein says suppliers must limit work to"),
       ("", "60 hours a week|60 hours", ", but some employees work more than"),
       ("", "75 hours a week|75 hours", ". An expert from the NGO Redress says that the high"),
       ("", "volume|volume of sales|volumes", "and low quality create a growing sense of disposability in fashion.")]
CASE = [("May 2025", "The European Commission and national consumer authorities told <b>Shein</b> to stop <b>fake discounts</b> and <b>pressure selling</b>, for example false purchase deadlines."),
        ("June 2025", "European consumer groups complained about Shein’s <b>dark patterns</b>: countdown timers, ‘low stock’ messages that may not be true and <b>endless scroll</b>."),
        ("July 2025", "France fined Shein <b>€40 million</b> for misleading discounts and unproven environmental claims."),
        ("2026", "The EU fined <b>Temu</b> <b>€200 million</b> under the Digital Services Act: it did not properly assess the risk of <b>illegal products</b> on its marketplace."),
        ("2024", "A Swiss NGO, Public Eye, reported that workers at some Shein suppliers still worked around <b>75 hours a week</b>.")]
D4 = ["Why is it difficult for fast fashion to be ethical? Use examples from the video.", "Is it any different for other industries? Why / Why not?",
      "Look at the case file. Which problems come from the factories and which come from the app design?",
      "Who should change things: designers, developers, product managers, marketers or users?"]
D4_UP = ["Your client wants a countdown timer on every product page. What do you say?", "Is endless scroll always a dark pattern? Where is the line?",
         "Would you work for an ultra-fast fashion app if the salary were 30% higher? Why / Why not?", "Should app stores remove apps that use dark patterns?"]
DIALS = [("Example", [("human", "resources"), ("business", "partner"), ("stock", "market"), ("mobile", "phone")]),
         ("Dial 1", [("moral", "approach"), ("unethical", "conduct"), ("tough", "conditions"), ("low", "pay")]),
         ("Dial 2", [("ethically", "sourced"), ("clothing", "brands"), ("sweat", "shops"), ("fair-trade", "cotton")]),
         ("Dial 3 · from the video", [("on-demand", "model"), ("profit", "margins"), ("labour", "law"), ("supplier", "factories")])]
VERBS = ["be accused of", "be aware of", "be responsible for", "campaign against", "have an impact on", "look across", "take responsibility for"]
Q7 = [("If you", "look across|looked across", "the whole online shopping industry, is it more ethical today than it was five years ago?"),
      ("An increasing number of shopping apps", "have been accused of|were accused of", "manipulative design since people became more informed about dark patterns."),
      ("Who do you think", "is responsible for|was responsible for", "the working conditions in the factories that make clothes for ultra-fast fashion apps?"),
      ("Who should", "take responsibility for", "unsafe or illegal products sold on online marketplaces?"),
      ("Do you think the public in your country", "is aware of|are aware of", "the tricks that shopping apps use?"),
      ("If you were going to", "campaign against", "ultra-fast fashion in a way that would ___B___ young shoppers, what would you do?")]
T8 = [("We all love a bargain, but at what price? Looking", ["across", "for"], 0, "the ultra-fast fashion industry, we see apps that are designed to keep us buying: countdown timers, ‘only 2 left!’ messages and endless scroll. Many of the clothes are made in tough"),
      ("", ["conditions", "condition"], 0, "for low pay, and few retailers are transparent about their"),
      ("", ["supply chains", "supply chain’s"], 0, ".<br><br>Join our campaign"),
      ("", ["of", "against"], 1, "manipulative shopping apps! Make a difference by telling your family and friends to be"),
      ("", ["aware", "beware"], 0, "of the tricks that apps use, and support our campaign #ScrollLessChooseBetter.<br><br>Sign the petition in which we ask everyone in the e-commerce"),
      ("", ["industry", "show"], 0, ", not only those who are accused"),
      ("", ["for", "of"], 1, "dark patterns, to follow our five-point plan:<br>• Show real discounts and honest deadlines.<br>• Take responsibility"),
      ("", ["for", "of"], 0, "the products sold on your platform.<br>• Be transparent about supply chains and use"),
      ("", ["ethical", "ethically"], 1, "sourced materials.<br>• Design apps that respect users’ time, not"),
      ("", ["addicted", "addictive"], 1, "ones.<br>• Take care of the planet by taking"),
      ("", ["responsibly", "responsibility"], 1, "for returns and waste.<br><br>Install our free browser extension, built by volunteer developers. It flags fake discounts and has an impact"),
      ("", ["for", "on"], 1, "the way you shop. Show them we want to be smart shoppers, not addicted ones!")]
FIND = ["owns a garment made from organic or fair-trade cotton", "sometimes wears vintage or second-hand clothes", "often gives clothes away to charity",
        "has bought clothes made of recycled materials", "wears leather goods", "how often people buy fast fashion items (e.g. every two months / once a year)",
        "where your colleagues’ clothes were made", "has bought clothes in an app like Shein or Temu", "has bought something because of a countdown timer or a ‘low stock’ message",
        "has deleted a shopping app because it was too addictive", "has returned or thrown away an item after wearing it fewer than five times"]
VOC = [("Business ethics", ["ethical / unethical", "ethically sourced", "fair-trade cotton", "sweatshop", "tough (working) conditions", "low pay", "moral approach", "unethical conduct", "clothing brand", "supply chain", "transparent"]),
       ("Verbs + prepositions", VERBS),
       ("Apps and design", ["ultra-fast fashion", "dark patterns", "fake discount", "pressure selling", "countdown timer", "‘low stock’ message", "endless scroll", "push notification", "illegal products"]),
       ("From the video", ["garment", "supplier", "on-demand model", "profit margin", "paid per piece", "labour law", "polluter", "disposability"]),
       ("Reporting a survey", ["the majority of respondents", "just over a quarter", "none of the participants", "over half of those surveyed", "the findings suggest that"])]

def opts(xs): return "".join('<option value="%d">%s</option>' % (i + 1, x) for i, x in enumerate(xs))
h = []
h.append('<section id="s1" class="sec"><div class="bsec">Lead-in</div><p class="ins"><b>1</b>Discuss these questions.</p>__LV_lead__</section>')
h.append('<section id="s2" class="sec"><div class="bsec vid">VIDEO</div><div class="vh">▶ <b>Inside the Chinese factories of fast-fashion giant Shein</b> · FRANCE 24 English · 3 February 2026 · 6:10 · <a href="https://www.youtube.com/watch?v=aYLbCitY_0k" target="_blank">open on YouTube</a></div>'
         '<div class="fr1"><iframe src="https://www.youtube-nocookie.com/embed/aYLbCitY_0k?rel=0&cc_load_policy=1" allowfullscreen loading="lazy"></iframe></div>'
         '<p class="ins"><b>2</b>Watch the video about the factories that make clothes for Shein and answer the questions using the people in the box.</p><div class="tbox">%s</div><div class="qs" id="p2">' % " · ".join(SPK))
for i, (q, a, t) in enumerate(V2):
    h.append('<div class="qr"><span class="nn">%d</span> %s <select class="js" data-a="%d"><option value="">— who? —</option>%s</select> <span class="ts">%s</span></div>' % (i + 1, q, a, opts(SPK), t))
h.append('</div><div class="ctrl"><button onclick="chkSel(\'p2\')">Check</button><span class="res" id="r_p2"></span></div></section>')
h.append('<section id="s3" class="sec"><div class="bsec vid">VIDEO</div><p class="ins"><b>3</b>Watch the video again and complete the summary. Use one to four words or a number in each gap.</p><div class="txt" id="p3"><p>')
for i, (pre, a, post) in enumerate(SUM):
    h.append('%s <sup>%d</sup><input class="ji" data-a="%s" style="width:150px"> %s ' % (pre, i + 1, a, post))
h.append('</p></div><div class="ctrl"><button onclick="chk(\'p3\')">Check</button><button class="l" onclick="showAns(\'p3\')">Show answers</button><span class="res" id="r_p3"></span></div>'
         '<div class="fr1 sm"><iframe src="https://www.youtube-nocookie.com/embed/aYLbCitY_0k?rel=0&cc_load_policy=1" allowfullscreen loading="lazy"></iframe></div></section>')
h.append('<section id="s4" class="sec"><div class="bsec vid">VIDEO</div><p class="ins"><b>4</b>Work in pairs. Read the case file first. Then discuss the questions.</p>'
         '<div class="case"><h4>📁 Case file: ultra-fast fashion apps</h4><table>%s</table></div>__LV_d4__</section>' % "".join("<tr><td class='cd'>%s</td><td>%s</td></tr>" % c for c in CASE))
h.append('<section id="s5" class="sec"><div class="bsec">Vocabulary <span class="sub">Business ethics</span></div><p class="ins"><b>5</b>Which word that is repeated in the video collocates with all these words?</p>'
         '<div class="tbox big3">… designer &nbsp; … industry &nbsp; … retailer &nbsp; … show</div><div class="ctrl"><input class="ji" id="w5" data-a="fashion" placeholder="your word"><button onclick="chkOne(\'w5\')">Check</button><span class="res" id="r_w5"></span></div>'
         '<p class="ins" style="margin-top:24px"><span class="star">★</span>Level up: which word goes with all of these? <i>… fashion · … delivery · … food · … growth</i></p>'
         '<div class="ctrl"><input class="ji" id="w5b" data-a="fast" placeholder="your word"><button onclick="chkOne(\'w5b\')">Check</button><span class="res" id="r_w5b"></span></div></section>')
h.append('<section id="s6" class="sec"><div class="bsec">Vocabulary</div><p class="ins"><b>6</b>Turn the outer words of each dial to make collocations for talking about business ethics. Dial 3 is from the video. Look at the example first.</p><div class="dials">')
for k, (name, pairs) in enumerate(DIALS):
    h.append('<div class="dial" id="d%d" data-ok=\'%s\'><h4>%s</h4><div class="rows"></div><div class="ctrl"><button class="l" onclick="turn(%d,-1)">↺ anticlockwise</button><button class="l" onclick="turn(%d,1)">↻ clockwise</button></div><div class="res" id="r_d%d"></div></div>'
             % (k, json.dumps([p[1] for p in pairs]), name, k, k, k))
h.append('</div></section>')
h.append('<section id="s7" class="sec"><div class="bsec">Vocabulary</div><p class="ins"><b>7</b>Complete the questions using the correct form of the verbs with prepositions in the box. Then ask and answer them.</p><div class="tbox">%s</div><div id="p7">' % " · ".join(VERBS))
for i, (pre, a, post) in enumerate(Q7):
    extra = ""
    if "___B___" in post:
        post = post.replace("___B___", '<input class="ji" data-a="have an impact on" style="width:170px">')
    h.append('<div class="qr"><span class="nn">%d</span> %s <input class="ji" data-a="%s" style="width:200px"> %s</div>' % (i + 1, pre, a, post))
h.append('</div><div class="ctrl"><button onclick="chk(\'p7\')">Check</button><button class="l" onclick="showAns(\'p7\')">Show answers</button><span class="res" id="r_p7"></span></div></section>')
h.append('<section id="s8" class="sec"><div class="bsec">Vocabulary</div><p class="ins"><b>8</b>Choose the correct options to complete the campaign text.</p><div class="camp"><div class="ch">SCROLL LESS<br>CHOOSE BETTER</div><div class="txt" id="p8"><h3>Scroll less, choose better</h3><p>')
for i, (pre, ch, a, post) in enumerate(T8):
    h.append('%s <span class="pick" data-a="%d"><sup>%d</sup>%s</span> %s ' % (pre, a, i + 1, "".join('<button onclick="pk(this)">%s</button>' % c for c in ch), post))
h.append('</p></div></div><div class="ctrl"><button onclick="chk8()">Check</button><span class="res" id="r_p8"></span></div><p class="note">This text is written for this course. The facts behind it are in the case file (Exercise 4).</p></section>')
h.append('<section id="s9" class="sec"><div class="bsec proj">PROJECT: Survey — How ethical are your clothes and apps?</div>'
         '<p class="ins"><b>9A</b>You are going to survey your classmates or colleagues. Prepare questions before you start. You want to find out:</p><div id="p9">')
for i, f in enumerate(FIND):
    tag = ' <span class="newt">apps</span>' if i >= 7 else ""
    h.append('<div class="qr sv"><span class="nn">%d</span><span class="ft">who %s%s</span><input class="fi q9" placeholder="Your question…"></div>' % (i + 1, f, tag) if not f.startswith(("how", "where")) else
             '<div class="qr sv"><span class="nn">%d</span><span class="ft">%s%s</span><input class="fi q9" placeholder="Your question…"></div>' % (i + 1, f, tag))
h.append('</div><p class="hint2">💡 Use different question types: yes/no (<i>Have you ever…?</i>), multiple choice (<i>How often…? a) b) c)</i>), open (<i>Why…?</i>). Start general, then ask more personal questions.</p>'
         '<p class="ins" style="margin-top:24px"><b>B</b>Carry out your survey. Make careful notes of people’s answers and the total number of people interviewed.</p>'
         '<div class="ctrl"><label>People interviewed: <input type="number" id="tot" min="1" value="10" style="width:70px" oninput="pct()"></label></div><table class="tk" id="tally"><tr><th>#</th><th>Question</th><th>Yes / chosen</th><th>%</th></tr></table></section>')
h.append('''<section id="s10" class="sec"><div class="bsec proj">PROJECT</div><p class="ins"><b>10</b>Write up your key findings as a report. You do not need to include all the data from your survey. Write 160–180 words.</p>
<div class="two"><div><div class="fmt"><button class="on" onclick="fmt(this,0)">📄 Report (book)</button><button onclick="fmt(this,1)">💬 Slack / Notion summary</button></div>
<p class="hint2" id="fhint">Introduction (aim, who you asked) → Findings (3–4 key results with numbers) → Conclusion and recommendation.</p>
<textarea id="rep" oninput="wc()" placeholder="Report: How ethical are our clothes and apps?&#10;&#10;Introduction&#10;The aim of this survey was to…"></textarea><div class="res" id="wcount">0 words</div></div>
<div class="bank"><h4>Phrase bank</h4><p><b>Numbers</b><br>The majority of respondents… · Over half of those surveyed… · Just over a quarter… · Only two people… · None of the participants…</p>
<p><b>Findings</b><br>The findings suggest / indicate that… · It is clear that… · Surprisingly, …</p><p><b>Reporting verbs</b><br>Several people admitted that… · Most respondents felt that… · A few raised concerns about…</p>
<p><b>Unit vocabulary</b><br>ethically sourced · fair-trade · unethical conduct · dark patterns · take responsibility for · be aware of</p></div></div>
<div class="ctrl"><button class="l" onclick="copyRep()">Copy my text</button><span class="res" id="cmsg"></span></div></section>''')
h.append('<section id="s11" class="sec"><div class="bsec sa">Self-assessment</div><p class="big2">How successfully have you achieved the lesson outcome? Give yourself a score from 0 (I need more practice) to 5 (I know this well).</p>'
         '<div class="score" id="score">%s</div><p class="ins" style="margin-top:22px">Tick the words you used today.</p><div class="chk">__WORDS__</div><p class="res" id="wcn"></p>'
         '<p class="ins" style="margin-top:22px">My 5 new phrases</p><div id="mine">%s</div></section>' % ("".join('<button onclick="sc(this)">%d</button>' % i for i in range(6)), "".join('<input placeholder="%d.">' % i for i in range(1, 6))))
body = "".join(h)

def card(k): return ('<div class="card"><span class="cnt" id="%sn"></span><div class="big" id="%sw"></div></div><div class="ctrl"><button class="l" onclick="step(\'%s\',-1)">← Back</button>'
                     '<button onclick="step(\'%s\',1)">Next →</button><button class="l" onclick="shuf(\'%s\')">Shuffle</button></div>' % ((k,) * 5))
def lvl(b, u): return ('<div class="lvw"><div class="lvl"><button class="on" onclick="lv(this,0)">Base</button><button class="p" onclick="lv(this,1)">★ Level up: apps</button></div><div class="base">%s</div><div class="plus">%s</div></div>' % (card(b), card(u)))
body = body.replace("__LV_lead__", lvl("la", "lu")).replace("__LV_d4__", lvl("da", "du"))
words = [w for _, ws in VOC for w in ws]
body = body.replace("__WORDS__", "".join('<label><input type="checkbox" onchange="wcn()"> %s</label>' % w for w in words))
D = {"la": LEAD, "lu": LEAD_UP, "da": D4, "du": D4_UP}
vocab = "".join('<div class="vg"><h4>%s</h4>%s</div>' % (t, "".join("<span>%s</span>" % w for w in ws)) for t, ws in VOC)
nav = [("s1", "1"), ("s2", "2"), ("s3", "3"), ("s4", "4"), ("s5", "5"), ("s6", "6"), ("s7", "7"), ("s8", "8"), ("s9", "9"), ("s10", "10"), ("s11", "✓")]

CSS = open(__file__.replace("build_b2_lesson_6-1.py", "build_a2_lesson_1-1.py")).read().split('CSS = """')[1].split('"""')[0]
CSS += """
.fr1{position:relative;padding-top:56.25%;max-width:720px;margin:10px 0}.fr1.sm{max-width:480px;padding-top:0;height:270px}.fr1 iframe{position:absolute;inset:0;width:100%;height:100%;border:0}.ts{color:#8a8b8d;font-size:13px}.vh a{color:#c2185b}
.qs .qr,#p7 .qr{padding:6px 0;border-bottom:1px solid #eee}.qr select{margin-left:6px}.note{color:#6d6e70;font-size:14px}.sum{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.sum input{width:150px}
.case{border:1.5px solid ACC;border-radius:6px;padding:4px 14px 10px;background:#fafaff;margin-bottom:12px}.case h4{color:DARK;margin:8px 0}.case table{border-collapse:collapse;font-size:15px}.case td{padding:5px 8px;vertical-align:top;border-bottom:1px dotted #d5d6d7}.case td.cd{font-weight:500;color:DARK;white-space:nowrap}.case b{font-weight:500}
.big3{font-size:19px}.dials{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.dial{border:1px solid #d5d6d7;border-radius:10px;padding:8px 12px}.dial h4{margin:4px 0 8px;color:DARK}
.rows div{display:flex;gap:6px;margin:5px 0}.rows .in{background:ACC2;padding:4px 10px;border-radius:14px;font-weight:500;min-width:90px;text-align:right}.rows .ot{border:1.5px dashed ACC;padding:3px 10px;border-radius:14px}.dial.ok .ot{border-style:solid;border-color:#3a9d5d;background:#eaf7ee}
.camp{display:grid;grid-template-columns:150px 1fr;gap:14px}.ch{background:#c2185b;color:#fff;font-weight:600;font-size:20px;text-align:center;padding:26px 8px;border-radius:6px;height:fit-content}.camp .txt{border:2px solid #c2185b;border-left-width:2px}.camp h3{margin:6px 0;font-weight:500;font-size:24px}
.pick{white-space:nowrap}.pick button{border:1px solid #c8c9cb;background:#fff;font:italic 300 16px "Fira Sans",system-ui,sans-serif;padding:1px 6px;cursor:pointer}.pick button:first-of-type{border-radius:4px 0 0 4px}.pick button:last-of-type{border-radius:0 4px 4px 0}.pick button.on{background:ACC2;border-color:ACC}.pick.ok button.on{background:#eaf7ee;border-color:#3a9d5d}.pick.no button.on{background:#fdecec;border-color:#d9534f}
.bsec.proj{color:#fff;background:#6b6fb5;padding:6px 14px;border-radius:4px;font-size:20px}.sv .ft{flex:1;min-width:300px}.sv{display:flex;gap:8px;align-items:center}.q9{flex:1.2}.newt{background:#fff2cc;color:#8a6100;font-size:12px;padding:1px 6px;border-radius:8px;margin-left:4px}
.two{display:grid;grid-template-columns:1.5fr 1fr;gap:16px}textarea{width:100%;min-height:300px;font:inherit;font-size:16px;border:1.5px solid #c8c9cb;border-radius:6px;padding:10px}.bank{background:#fafaff;border:1px solid #e1e2ee;border-radius:6px;padding:4px 14px;font-size:14px}.bank h4{color:DARK;margin:8px 0}.bank b{font-weight:500;color:DARK}
.fmt button{border:1.5px solid ACC;background:#fff;color:DARK;padding:5px 12px;border-radius:16px;margin-right:6px;cursor:pointer;font:500 14px "Fira Sans",system-ui,sans-serif}.fmt button.on{background:ACC;color:#fff}
.score button{width:48px;height:48px;border-radius:50%;border:2px solid #e1e2e3;background:#fff;font-size:18px;margin-right:6px;cursor:pointer}.score button.on{border-color:ACC;background:ACC2}
#tally td:nth-child(2){text-align:left}#tally td:nth-child(3),#tally td:nth-child(4){text-align:center}
@media(max-width:800px){.dials,.two,.camp{grid-template-columns:1fr}.sum{grid-template-columns:1fr 1fr}}"""
CSS = CSS.replace("#3b7dd8", ACC).replace("#e3eefb", ACC2).replace("#2a5fb0", DARK).replace("#4f9be8", "#7b7fe0").replace("ACC2", ACC2).replace("ACC", ACC).replace("DARK", DARK)
CSS = CSS.replace("nav button{width:46px", "nav button{min-width:46px;padding:0 8px")

JS = r"""
const D=__D__;const st={},ord={};const $=id=>document.getElementById(id);
const norm=s=>(s||"").toLowerCase().replace(/[’`]/g,"'").replace(/\s+/g," ").replace(/[.!?]+$/,"").trim();
function render(k){const a=ord[k];$(k+"w").textContent=D[k][a[st[k]]];$(k+"n").textContent=(st[k]+1)+" / "+a.length}
function step(k,d){st[k]=(st[k]+d+ord[k].length)%ord[k].length;render(k)}
function shuf(k){const a=ord[k];for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}st[k]=0;render(k)}
function lv(b,u){const w=b.closest(".lvw");w.classList.toggle("up",!!u);b.parentNode.querySelectorAll("button").forEach(x=>x.classList.remove("on"));b.classList.add("on")}
const good=e=>e.dataset.a.split("|").some(a=>norm(a)===norm(e.value));
function chkOne(id){const e=$(id),g=good(e);e.classList.toggle("ok",g);e.classList.toggle("no",!g);$("r_"+id).textContent=g?"✓ Correct!":"Try again"}
function chk(id){let ok=0,n=0;$(id).querySelectorAll("input.ji").forEach(e=>{n++;const g=good(e);e.classList.toggle("ok",g);e.classList.toggle("no",!g);if(g)ok++});$("r_"+id).textContent=ok+" / "+n+(ok===n?" ✓ Well done!":"")}
function showAns(id){$(id).querySelectorAll("input.ji").forEach(e=>{e.value=e.dataset.a.split("|")[0];e.classList.remove("no")})}
const rot=[0,0,0,0];const IN=__IN__;
function drawDial(k){const d=$("d"+k),ok=JSON.parse(d.dataset.ok),n=ok.length,r=rot[k];const outs=ok.map((_,i)=>ok[((i+r)%n+n)%n]);
 d.querySelector(".rows").innerHTML=IN[k].map((w,i)=>`<div><span class="in">${w}</span><span class="ot">${outs[i]}</span></div>`).join("");
 const win=r%n===0;d.classList.toggle("ok",win);$("r_d"+k).textContent=win?"✓ All four collocations are correct!":""}
function turn(k,dir){rot[k]+=dir;drawDial(k)}
function chkSel(id){let ok=0,n=0;$(id).querySelectorAll("select.js").forEach(e=>{n++;const g=e.value===e.dataset.a;e.classList.toggle("ok",g);e.classList.toggle("no",!g);if(g)ok++});$("r_"+id).textContent=ok+" / "+n+(ok===n?" ✓ Well done!":"")}
function pk(b){b.parentNode.querySelectorAll("button").forEach(x=>x.classList.remove("on"));b.classList.add("on");b.parentNode.classList.remove("ok","no")}
function chk8(){let ok=0,n=0;document.querySelectorAll("#p8 .pick").forEach(p=>{n++;const on=[...p.querySelectorAll("button")].findIndex(x=>x.classList.contains("on"));const g=on===+p.dataset.a;p.classList.toggle("ok",g);p.classList.toggle("no",!g&&on>=0);if(g)ok++});$("r_p8").textContent=ok+" / "+n+(ok===n?" ✓ Well done!":"")}
function buildTally(){const t=$("tally");t.querySelectorAll("tr.r").forEach(r=>r.remove());document.querySelectorAll("#p9 .sv").forEach((r,i)=>{const q=r.querySelector(".q9").value.trim()||r.querySelector(".ft").firstChild.textContent;
 const tr=document.createElement("tr");tr.className="r";tr.innerHTML=`<td>${i+1}</td><td>${q.replace(/</g,"&lt;")}</td><td><input type="number" min="0" value="0" style="width:70px" oninput="pct()"></td><td class="pc">0%</td>`;t.appendChild(tr)});pct()}
function pct(){const tot=+$("tot").value||1;document.querySelectorAll("#tally tr.r").forEach(r=>{const v=+r.querySelector("input").value||0;r.querySelector(".pc").textContent=Math.round(v/tot*100)+"%"})}
let target=[160,180];function fmt(b,i){document.querySelectorAll(".fmt button").forEach(x=>x.classList.remove("on"));b.classList.add("on");target=i?[80,100]:[160,180];
 $("fhint").textContent=i?"TL;DR in one line → 3–4 bullet points with numbers → next steps. 80–100 words.":"Introduction (aim, who you asked) → Findings (3–4 key results with numbers) → Conclusion and recommendation.";wc()}
function wc(){const n=($("rep").value.match(/\S+/g)||[]).length;$("wcount").textContent=n+" words (target "+target[0]+"–"+target[1]+")"+(n>=target[0]&&n<=target[1]?" ✓":"")}
function copyRep(){try{navigator.clipboard.writeText($("rep").value).then(()=>$("cmsg").textContent="Copied!",()=>$("cmsg").textContent="Select and copy manually.")}catch(e){$("cmsg").textContent="Select and copy manually."}}
function sc(b){document.querySelectorAll("#score button").forEach(x=>x.classList.remove("on"));b.classList.add("on")}
function wcn(){const n=document.querySelectorAll(".chk input:checked").length;$("wcn").textContent=n+" words used"+(n>=10?" — great!":"")}
document.querySelectorAll("nav button").forEach(b=>b.onclick=()=>{document.querySelectorAll("nav button,.sec").forEach(x=>x.classList.remove("on"));b.classList.add("on");$(b.dataset.s).classList.add("on");if(b.dataset.s==="s9")buildTally();scrollTo(0,0)});
document.querySelectorAll(".q9").forEach(e=>e.addEventListener("change",buildTally));
for(const k in D){ord[k]=D[k].map((_,i)=>i);st[k]=0;render(k)}rot[0]=0;rot[1]=2;rot[2]=3;rot[3]=1;[0,1,2,3].forEach(drawDial);buildTally();$("s1").classList.add("on");
"""
JS = JS.replace("__D__", json.dumps(D, ensure_ascii=False)).replace("__IN__", json.dumps([[p[0] for p in d[1]] for d in DIALS], ensure_ascii=False))
html = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>6.1 Ethical choices — Lesson</title><link href="https://fonts.googleapis.com/css2?family=Fira+Sans:ital,wght@0,300;0,400;0,500;0,600;1,300&display=swap" rel="stylesheet"><style>%s</style></head><body>
<header><div class="n">6.1</div><h1>Ethical choices</h1><div class="tag">LESSON</div></header>
<div class="out1"><b>Lesson outcome</b>You can use language related to ethics in business.</div>
<details class="voc" open><summary>📖 Vocabulary of this lesson — click to hide / show</summary><div class="vgs">%s</div></details>
<div class="top"><a href="../../../index.html">← Contents</a></div>
<nav>%s</nav><main>%s</main><footer>Video: FRANCE 24 English, “Inside the Chinese factories of fast-fashion giant Shein” (YouTube, 03.02.2026). Case file sources: European Commission / CPC Network (05.2025), BEUC (06.2025), DGCCRF France (07.2025), European Commission DSA decision on Temu (2026), Public Eye (2024). Valentyna Hordiienko · Middle Learning Architect</footer>
<script>%s</script></body></html>""" % (CSS, vocab, "".join('<button data-s="%s"%s>%s</button>' % (s, ' class="on"' if s == "s1" else "", l) for s, l in nav), body, JS)
open(OUT, "w").write(html); print("ok", len(html))
