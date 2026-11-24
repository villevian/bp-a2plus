"""Business Partner B1 · 1.1 EXTRA — Portfolio career (freelance and contract work for international clients).
Optional material for students who want more. Usage: python3 build_b1_1-1_extra.py OUTDIR [STUDENT_CODE] -> OUTDIR/extra.html
"""
import sys, os, json
from bp_page import page, fb, sel, inp, ta, ctl, SELF
OUTDIR = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
os.makedirs(OUTDIR, exist_ok=True)
K = {}
ADV = lambda title, body: '<div class="card" style="border-left:4px solid #e0a100;background:#fffaf0;margin-top:22px"><b style="color:#b26b00">★ Advanced option</b> · %s<div style="margin-top:6px">%s</div></div>' % (title, body)
def mbtn(i, txt, label="Show answer"):
    return '<button class="btn l" onclick="model(\'%s\')" style="margin-top:6px">%s</button><div class="model" id="%s">%s</div>' % (i, label, i, txt)

T = "One developer, three clients"
SUB = "More and more engineers build a portfolio career instead of a single job. What does it take?"
ART = [
 "Mykola is a backend developer from Lviv. He doesn’t have one employer – he has three <b>clients</b>: a logistics start-up in the Netherlands, a US agency that builds e-commerce sites, and a Polish fintech company. "
 "He works with all of them as a <b>contractor</b>, and his <b>contracts</b> are renewed every six months. This kind of working life is called a <b>portfolio career</b>.",
 "‘The money is better than in my old full-time job, but that’s not the main reason,’ he says. ‘I learn something new on every project, and if one client stops working with me, I still have two others.’",
 "The difficult part, he explains, is not the code. ‘Every client has a different tech stack, different tools and a different culture. So the most important skill is <b>onboarding</b> fast: in the first week I read the docs, ask a lot of questions and deliver something small.’",
 "Communication is the next big skill. His clients are in three <b>time zones</b>, so he works mostly asynchronously: he writes a short update on Slack every evening and keeps his <b>availability</b> clear in his calendar. "
 "He has also learned to <b>manage expectations</b>. ‘If a client asks for a new feature, I agree the <b>scope</b> and the <b>deadline</b> first. Saying “not this week, but next week” is much better than missing a deadline.’",
 "Then there is the business side. Mykola sends an <b>invoice</b> to each client at the end of the month, keeps track of his hours and reviews his <b>rate</b> once a year. "
 "Between projects he works on a <b>side project</b>, which he adds to his <b>portfolio</b> on GitHub. ‘New clients rarely read my CV,’ he says. ‘They look at what I’ve built and they ask my old clients about me.’",
 "Is it for everyone? ‘No,’ he admits. ‘There’s no paid holiday, and some months are quiet. You need to be organised, disciplined and good with people. But if you like variety, it’s a great way to work.’",
]
PLAIN = " ".join(p.replace("<b>", "").replace("</b>", "") for p in ART)
art = ('<div class="art"><h3>%s</h3><p class="sub2">%s</p>%s</div>' % (T, SUB, "".join("<p>%s</p>" % p for p in ART)) +
       '<div class="ctl"><button class="btn l" onclick="readArt(this)">🔊 Listen to the article</button></div>')

TF = [("Mykola has one full-time employer and two side projects.", "F", "He has three clients and no employer."),
      ("For him, learning on every project is more important than the money.", "T", ""),
      ("He says the hardest part of the job is writing the code.", "F", "The hardest part is the different stacks, tools and cultures."),
      ("In the first week with a new client, he tries to deliver something small.", "T", ""),
      ("He prefers to promise a quick deadline, even if he can’t meet it.", "F", "He agrees scope and deadline first; ‘not this week, but next week’ is better."),
      ("New clients usually decide after looking at his work and talking to old clients.", "T", "")]
WHY = {}
for i, (q, a, w) in enumerate(TF):
    K["e1_%d" % (i + 1)] = [a]
    if w: WHY["e1_%d" % (i + 1)] = w
e1 = ('<div class="bsec">Extra <span class="sub">Reading</span></div><p class="ins"><b class="x">1</b>Read the article. Are the sentences true (T) or false (F)?</p>' + art +
      "".join('<div class="tf"><span class="q">%d. %s</span><label><input type="radio" name="e1_%d" data-k="e1_%d" value="T"> T</label><label><input type="radio" name="e1_%d" data-k="e1_%d" value="F"> F</label>%s</div>'
              % (i + 1, q, i + 1, i + 1, i + 1, i + 1, fb("e1_%d" % (i + 1))) for i, (q, a, w) in enumerate(TF)) +
      '<div class="ctl"><button class="btn" onclick="chkRad(\'e1\',WHY)">Check</button><span class="res" id="r_e1"></span></div>')

V = [("rate", "the money you charge per hour or per day"), ("scope", "exactly what work is included in a task or project"), ("invoice", "a document that asks a client to pay for your work"),
     ("contractor", "a person who works for a company under a contract, not as an employee"), ("onboarding", "the first days when you learn how a new team or project works"),
     ("manage expectations", "make sure people know what you can and can’t do, and when"), ("availability", "the times when you are free to work or talk"),
     ("side project", "something you build in your free time, not for a client"), ("portfolio", "a collection of your work that you show to clients or employers"), ("client", "a company or person who pays you for your work")]
VS = [V[i] for i in (3, 7, 0, 5, 9, 2, 6, 1, 8, 4)]
for i, (w, d) in enumerate(VS): K["e2_%d" % (i + 1)] = [d]
e2 = ('<div class="bsec">Extra <span class="sub">Vocabulary</span></div><p class="ins"><b class="x">2</b>Match the words from the article with their meanings.</p>' +
      "".join('<div class="row"><b style="display:inline-block;min-width:200px;font-weight:500">%s</b>%s%s</div>' % (w, sel("e2_%d" % (i + 1), sorted(d for _, d in V), 520), fb("e2_%d" % (i + 1))) for i, (w, d) in enumerate(VS)) + ctl("e2"))
G = [("Before I start, let’s agree the ___ – what exactly is included?", "scope"), ("I’ll send you the ___ for November on Friday.", "invoice"),
     ("My ___ this week: Monday to Wednesday, 10:00–17:00 CET.", "availability"), ("I always try to ___ – I tell the client early if something will be late.", "manage expectations"),
     ("The first week was all about ___: reading docs and meeting the team.", "onboarding"), ("I built this tool as a ___ and now it’s the best thing in my ___.", None)]
G[5] = ("I built this tool as a ___ and now it’s the best thing in my portfolio.", "side project")
for i, (q, a) in enumerate(G): K["e3_%d" % (i + 1)] = [a]
e3 = ('<div class="bsec">Extra <span class="sub">Vocabulary in use</span></div><p class="ins"><b class="x">3</b>Complete the messages a contractor sends to clients.</p>'
      '<div class="box">%s</div>' % " · ".join(sorted(a for _, a in G)) +
      "".join('<div class="slack" style="margin:8px 0"><b>Mykola</b><span class="t">%s</span><br>%s%s</div>' % (["Mon 09:12", "Thu 17:40", "Mon 08:55", "Tue 14:03", "Fri 16:30", "Wed 11:20"][i], q.replace("___", inp("e3_%d" % (i + 1), 190)), fb("e3_%d" % (i + 1))) for i, (q, a) in enumerate(G)) + ctl("e3"))
e4 = ('<div class="bsec wr">Extra <span class="sub">Think and write</span></div><p class="ins"><b class="x">4</b><b>A</b> A portfolio career: what are the pros and cons for you?</p>'
      '<div class="two"><div><b>👍 Pros</b>%s</div><div><b>👎 Cons</b>%s</div></div>' % (ta("e4_pro", "variety, …", 90), ta("e4_con", "no paid holiday, …", 90)) +
      '<p class="ins"><b>B</b> Would you like to work like Mykola one day? Write 60–80 words. Use at least four words from Exercise 2.</p>' + ta("e4b", "I would / wouldn’t like … because …", 130) + '<div class="res" id="wce4"></div>' +
      mbtn("me4", "I think a portfolio career could be great for me in the future, but not right now. I like variety and I learn fast, so onboarding on new projects wouldn’t be a problem. "
                  "However, I’m not very good at managing expectations yet, and I don’t know how to set my rate or send an invoice. First, I want to build a strong portfolio with a few side projects. Then I’ll try one client as a contractor.", "Show model answer") +
      ADV("Pitch to a client", '<p>Write a three-sentence message to a potential client on LinkedIn: <b>1</b> who you are and what you build → <b>2</b> one result with a number → <b>3</b> a clear next step (a call, a link to your portfolio).</p>' +
          ta("e4_adv", "Hi …, I’m a … who helps … I recently … Would you be open to a 15-minute call next week?", 90)) +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you talk about freelance and contract work?"))
XJS = r"""const ART=__ART__,WHY=__WHY__;
function readArt(b){try{if(speechSynthesis.speaking){speechSynthesis.cancel();b.textContent="🔊 Listen to the article";return}const u=new SpeechSynthesisUtterance(ART);u.lang="en-GB";u.rate=.92;
 const v=speechSynthesis.getVoices().find(x=>/^en-GB/i.test(x.lang))||speechSynthesis.getVoices().find(x=>/^en/i.test(x.lang));if(v)u.voice=v;u.onend=()=>b.textContent="🔊 Listen to the article";speechSynthesis.speak(u);b.textContent="⏹ Stop"}catch(e){}}
function wce(){const v=document.querySelector('[data-k=e4b]').value,n=(v.match(/\S+/g)||[]).length;document.getElementById("wce4").textContent=n+" words (60–80)"+(n>=60&&n<=80?" ✓":"")}
document.querySelector('[data-k=e4b]').addEventListener("input",wce);window.afterFill=wce;"""
VOC = [("Portfolio career", ["portfolio career", "client", "contractor", "contract", "rate", "invoice", "scope", "deadline", "onboarding", "manage expectations", "availability", "time zone", "side project", "portfolio"])]
html = page("1.1", "Transferable skills", "EXTRA", "Extra: a portfolio career – freelance and contract work for international clients.", "BP B1 1.1 Transferable skills · Extra", CODE,
            [("1", e1), ("2", e2), ("3", e3), ("4", e4)], K, VOC, extra_js=XJS.replace("__ART__", json.dumps(PLAIN, ensure_ascii=False)).replace("__WHY__", json.dumps(WHY, ensure_ascii=False)))
open(os.path.join(OUTDIR, "extra.html"), "w").write(html)
print("ok", OUTDIR)
