# -*- coding: utf-8 -*-
"""Business Partner A2+ · 1.3 Communication skills: Small talk (video lesson — kept as in the coursebook, pp. 12–13).
Pages: flip.html (Before class: videos 1.3.1–1.3.4, Ex 2–5 at home), lesson.html (all coursebook exercises 1A–10D), hw.html (practice).
Videos: YouTube, channel "English with Daria" (Business Partner A2+ videos).
Usage: python3 build_a2p_1-3.py LESSON_DIR [STUDENT_CODE]   -> LESSON_DIR/all/{flip,lesson,hw}.html
"""
import sys, os, random
from bp_page import page, fb, sel, inp, ta, ctl, SELF
from vocab_a2p import lesson
import vcard
ROOT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3fa9ad", "#e6f4f4", "#2b8185", "#5cc1c4"
VOC, VJS = vcard.build(lesson("1.3")[1], ACC, ACC2, DARK)
random.seed(13)
def shuf(o): o = o[:]; random.shuffle(o); return o
def radio(k, opts): return "".join('<label class="opt" style="display:inline;margin:0 10px 0 0"><input type="radio" name="%s" data-k="%s" value="%s"> %s</label>' % (k, k, o, o) for o in opts)
def model(i, label, body): return '<button class="btn l" onclick="model(\'%s\')" style="margin-top:6px">%s</button><div class="model" id="%s">%s</div>' % (i, label, i, body)

VID = {"1.3.1": ("WVWn1IxQUH8", "Jasmine is on her way to the TGC welcome dinner"),
       "1.3.2": ("zb5bX2heX2k", "Video A — Orla, Azra and Shaun at the dinner"),
       "1.3.3": ("GoTobzm3l_E", "Video B — Jasmine, Thiago, Azra and Alex"),
       "1.3.4": ("yB7MGmtIJKA", "Conclusions — tips for small talk")}
def video(n):
    y, t = VID[n]
    return ('<div class="vbox"><div class="vt"><span class="vn">▶ %s</span> %s <a href="https://www.youtube.com/watch?v=%s" target="_blank">open on YouTube</a></div>'
            '<div class="fr"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0&cc_load_policy=1" allowfullscreen loading="lazy"></iframe></div></div>') % (n, t, y, y)

CSS = r"""document.head.insertAdjacentHTML("beforeend",`<style>
.vbox{margin:10px 0 14px;max-width:720px}.vt{font-weight:500;margin-bottom:4px}.vt .vn{color:#2b8185;font-weight:600;margin-right:6px}.vt a{font-size:13px;color:#2b8185;margin-left:8px}
.fr{position:relative;padding-top:56.25%}.fr iframe{position:absolute;inset:0;width:100%;height:100%;border:0;border-radius:8px}
table.tb{border-collapse:collapse;width:100%;margin:10px 0;font-size:15px}table.tb th,table.tb td{border:1px solid #c8c9cb;padding:6px 10px;vertical-align:top;text-align:left}table.tb th{background:#f3f4f6;font-weight:600}
.quote{font-family:Georgia,serif;font-style:italic;font-size:19px;color:#2b8185;border-left:4px solid #3fa9ad;padding:6px 14px;margin:8px 0}
.line{display:flex;justify-content:space-between;font-size:14px;color:#5b6478;border-top:2px solid #3fa9ad;padding-top:4px;margin:10px 0 4px}
.aaa{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin:8px 0}.aaa div{background:#e6f4f4;border-radius:8px;padding:10px 12px}.aaa b{display:block;color:#2b8185;font-size:20px}
@media(max-width:640px){.aaa{grid-template-columns:1fr}}
.qc{font-size:22px;font-weight:500;text-align:center;background:#e6f4f4;border-radius:12px;padding:22px 16px;margin:10px 0;min-height:90px;display:flex;align-items:center;justify-content:center}
.card{background:#fff7e0;border:1.5px dashed #f2b631;border-radius:8px;padding:10px 14px;margin:12px 0}
.home{background:#e6f4f4;border-radius:8px;padding:8px 14px;margin:8px 0;font-size:15px}
.react{display:flex;flex-wrap:wrap;gap:6px;margin:6px 0}.react button{border:1.5px solid #3fa9ad;background:#fff;color:#2b8185;border-radius:16px;padding:4px 12px;font:500 15px "Fira Sans",sans-serif;cursor:pointer}
</style>`);
document.addEventListener("change",e=>{const g=e.target.dataset&&e.target.dataset.grp;if(!g)return;const h=document.querySelector(`input.g[data-k="${g}"]`);h.value=[...document.querySelectorAll(`[data-grp="${g}"]:checked`)].map(x=>x.value).join("|");h.dispatchEvent(new Event("input",{bubbles:true}))});
function restoreChecks(){document.querySelectorAll('input[type=hidden].g').forEach(h=>{const v=(h.value||"").split("|");document.querySelectorAll(`[data-grp="${h.dataset.k}"]`).forEach(c=>c.checked=v.includes(c.value))})}
window.afterFill=restoreChecks;
function say(t){try{const u=new SpeechSynthesisUtterance(t);u.lang="en-GB";u.rate=.9;speechSynthesis.cancel();speechSynthesis.speak(u)}catch(e){}}
"""

# ---------- shared video exercises (Ex 2–5) ----------
def ex_video(K, pre, home_note=""):
    note = '<div class="home">🏠 %s</div>' % home_note if home_note else ""
    # 2
    Q2 = [("What is Jasmine’s new job?", "She’s a trainee at TGC. She starts on Monday."),
          ("What does The Gallagher Consultancy (TGC) do?", "It’s an HR consultancy firm. It advises companies on recruitment, company strategy, that kind of thing."),
          ("Who are the people in the restaurant? Why are they meeting?", "New recruits (new employees) and people from TGC. It’s a welcome dinner for the new recruits."),
          ("Why is Jasmine late?", "She’s stuck in traffic.")]
    s2 = ('<div class="bsec">Video</div>' + note + '<p class="ins"><b class="x">2</b>Watch the video as Jasmine arrives at The Gallagher Consultancy dinner and answer the questions.</p>' + video("1.3.1") +
          "".join('<p class="ins"><span class="q">%d</span>%s</p>%s' % (i + 1, q, ta("%sv2_%d" % (pre, i + 1), "", 44)) for i, (q, _) in enumerate(Q2)) +
          model(pre + "m2", "Show answers", "<br>".join("%d %s" % (i + 1, a) for i, (_, a) in enumerate(Q2))))
    # 3A–B
    TOP = ["family", "health", "home town", "music", "personal finances", "the place you are in", "politics", "religion", "sports", "travel", "the weather"]
    s3 = ('<div class="bsec">Video A</div>' + note + '<p class="ins"><b class="x">3</b><b>A</b> Watch Video A.</p>' + video("1.3.2") +
          '<p class="ins"><span class="q">1</span>Which topics in Exercise 1C do Orla and Azra talk about? Tick them.</p><div class="chips">%s</div>' %
          "".join('<label class="opt" style="display:inline-flex;gap:4px;border:1.5px solid #c8c9cb;border-radius:6px;padding:3px 10px"><input type="checkbox" data-grp="%sv3t" value="%s"> %s</label>' % (pre, t, t) for i, t in enumerate(TOP)) + '<input type="hidden" class="g" data-k="%sv3t">' % pre +
          '<p class="ins"><span class="q">2</span>Where is Azra from originally? Where does she live now?</p>' + ta(pre + "v3_2", "", 40) +
          '<p class="ins"><span class="q">3</span>What do we learn about:<br><span style="font-weight:300">a&nbsp; Shaun’s typical journey home?<br>b&nbsp; Shaun’s trips to Los Angeles and Bangkok?</span></p>' + ta(pre + "v3_3", "a …\nb …", 60) +
          model(pre + "m3a", "Show answers", "1 home town (where Azra comes from), the place you are in (the restaurant / Dublin), travel (Shaun’s journeys)<br>"
                "2 She’s from Turkey, but she has lived in Dublin for years.<br>3a Friday traffic is terrible — it can take him hours to get home (he lives outside the city).<br>"
                "3b Los Angeles: the traffic was so bad that he arrived late and missed his presentation. Bangkok: the airline lost all his luggage.") +
          '<p class="ins" style="margin-top:20px"><b>B</b> In pairs, decide which sentence best describes how Shaun speaks.</p>' +
          '<div class="tf">%s%s</div>' % (radio(pre + "v3b_1", ["a", "b"]), fb(pre + "v3b_1")) +
          '<p>a&nbsp; He asks Jasmine a number of questions and listens carefully to her answers.<br>b&nbsp; He doesn’t really listen to Jasmine, but prefers to talk about himself.</p>' + ctl(pre + "v3b", "chkRad"))
    K[pre + "v3b_1"] = ["b"]
    # 4A–B
    PPL = ["Jasmine", "Thiago", "Azra", "Alex"]
    ROWS = ["Ask a question", "Answer the question", "Add new information", "Show interest (lean forward, use eye contact, smile)"]
    tbl = '<table class="tb"><tr><th></th>%s</tr>%s</table>' % ("".join("<th>%s</th>" % p for p in PPL), "".join(
        "<tr><td>%s</td>%s</tr>" % (r, "".join('<td style="text-align:center"><input type="checkbox" data-grp="%sv4b" value="%d-%d"></td>' % (pre, i, j) for j in range(4))) for i, r in enumerate(ROWS))) + '<input type="hidden" class="g" data-k="%sv4b">' % pre
    s4 = ('<div class="bsec">Video B</div>' + note + '<p class="ins"><b class="x">4</b><b>A</b> Watch Video B. What do you learn about:</p>' + video("1.3.3") +
          "".join('<p class="ins"><span class="q">%d</span>%s?</p>%s' % (i + 1, p, ta("%sv4_%d" % (pre, i + 1), "", 40)) for i, p in enumerate(PPL)) +
          model(pre + "m4a", "Show answers", "1 Jasmine: she’s American, from Boston, and went to university there. Her trip was about an hour. She met Orla at the interview. She doesn’t know much about TGC.<br>"
                "2 Thiago: he has a Brazilian name because his father is from Brazil, but he’s Italian. He has never been to Boston, but he’d like to go.<br>"
                "3 Azra: she was born in Istanbul, but her parents moved to London when she was five. They often go back to see family. She loves both London and Istanbul.<br>"
                "4 Alex: he knows Turkey a little — he went there on holiday about three years ago.") +
          '<p class="ins" style="margin-top:20px"><b>B</b> Watch Video B again and tick (✓) the things the speakers do as they make small talk.</p>' + tbl +
          model(pre + "m4b", "Show possible answers", "All four ask and answer questions. Jasmine, Azra and Alex add new information (Boston and university; Istanbul and London; a holiday three years ago). They all show interest: they smile, look at each other and lean in."))
    # 5
    s5 = ('<div class="bsec">Video</div>' + note + '<p class="ins"><b class="x">5</b>Watch the Conclusions section of the video. What is the AAA model?</p>' + video("1.3.4") +
          '<div class="aaa"><div><b>A</b>%s</div><div><b>A</b>%s</div><div><b>A</b>%s</div></div>' % (inp(pre + "v5_1", 200, "A…"), inp(pre + "v5_2", 200, "A…"), inp(pre + "v5_3", 200, "A…")) +
          model(pre + "m5", "Show answer", "<b>Answer</b> the speaker’s question, <b>add</b> new information, then <b>ask</b> him or her another question.<br>"
                "Other tips: choose your topic carefully, don’t be too negative, avoid personal finances, politics and religion, listen and show interest, change the subject if the other person looks bored, don’t dominate the conversation."))
    return [("2", s2), ("3", s3), ("4", s4), ("5", s5)]

def ex_7_to_10(K):
    Q7 = ["Where do you come from?", "What do you think about this restaurant?", "How long was your trip?", "What do you know about working at TGC?",
          "Do you know Turkey?", "Which do you prefer, London or Istanbul?", "Do you know Orla?", "What are you doing in Dublin?"]
    A7 = {"a": "It’s very nice.", "b": "Not much.", "c": "Yes, I met her at the interview.", "d": "About an hour.", "e": "I’m starting a new job on Monday.",
          "f": "A little. I went there on holiday about three years ago.", "g": "I’m from Turkey.", "h": "I love them both."}
    KEY7 = ["g", "a", "d", "b", "f", "h", "c", "e"]
    for i, a in enumerate(KEY7): K["f7_%d" % (i + 1)] = [a]
    BOLD = ["Where do you", "What do you think about", "How long was your", "What do you know about", "Do you know", "Which do you prefer", "Do you know", "What are you doing"]
    s7 = ('<div class="bsec">Functional language <span class="sub">Making small talk</span></div><p class="ins"><b class="x">7</b><b>A</b> Match the questions (1–8) with the answers (a–h).</p>' +
          '<div class="card" style="background:#f6f8fb;border:0">%s</div>' % "<br>".join("<b>%s</b>&nbsp; %s" % (k, v) for k, v in A7.items()) +
          "".join('<div class="row">%d. <b>%s</b>%s %s%s</div>' % (i + 1, BOLD[i], q[len(BOLD[i]):], sel("f7_%d" % (i + 1), list("abcdefgh"), 70), fb("f7_%d" % (i + 1))) for i, q in enumerate(Q7)) + ctl("f7") +
          '<div class="react">🔊 Listen and repeat: %s</div>' % "".join('<button onclick="say(this.dataset.t)" data-t="%s">%d</button>' % (q, i + 1) for i, q in enumerate(Q7)))
    BOX = ["Angelina’s Pizzeria", "the company", "David", "fashion", "flight", "the food", "in Boston", "Prague or Barcelona", "the project", "the town"]
    s7b = ('<div class="bsec">Functional language</div><p class="ins"><b>B</b> Match words from the box with the expressions in bold in Exercise 7A to make more small talk questions. There may be more than one possible answer.</p>'
           '<div class="box">%s · <s>live</s></div><p><i>1 Where do you live?</i></p>' % " · ".join(BOX) + ta("f7b", "What do you think about the food?\n…", 150) +
           model("m7b", "Show possible answers", "Where do you live? · What do you think about Angelina’s Pizzeria / the food / the town / the project? · How long was your flight? · "
                 "What do you know about the company / the project / fashion? · Do you know David / the town / Angelina’s Pizzeria? · Which do you prefer, Prague or Barcelona? · What are you doing in Boston?") +
           '<p class="ins" style="margin-top:20px"><b>C</b> Write eight more small talk questions using the phrases in bold from Exercise 7A. Think about a conference, a business trip or your city.</p>' +
           ta("f7c", "1 What do you think about the hotel?\n2 How long was your …\n3 …", 170))
    # 8
    BOX8 = ["I’d like to", "that’s right", "to university", "you from", "you know it"]
    KEY8 = ["you from", "that’s right", "to university", "you know it", "I’d like to"]
    for i, a in enumerate(KEY8): K["f8_%d" % (i + 1)] = [a]
    s = lambda i: sel("f8_%d" % i, BOX8, 150) + fb("f8_%d" % i)
    s8 = ('<div class="bsec">Functional language</div><p class="ins"><b class="x">8</b><b>A</b> Complete the extract from the video using the phrases in the box.</p><div class="box">%s</div>' % " · ".join(BOX8) +
          '<div class="row"><b>Thiago:</b> Shaun says you’re American. Where are %s?</div><div class="row"><b>Jasmine:</b> %s. I’m from Boston. I went %s there. Do %s?</div><div class="row"><b>Thiago:</b> No, I’ve never been, but %s.</div>' % (s(1), s(2), s(3), s(4), s(5)) +
          ctl("f8") + '<button class="btn l" onclick="say(\'Shaun says you are American. Where are you from? That is right. I am from Boston. I went to university there. Do you know it? No, I have never been, but I would like to.\')">🔊 Listen</button>' +
          '<p class="ins" style="margin-top:20px"><b>B</b> Look at Jasmine’s response in Exercise 8A.</p><p class="ins"><span class="q">1</span>Does she use the AAA (answer, add, ask) model? Explain your answer.</p>' + ta("f8b1", "", 44) +
          '<p class="ins"><span class="q">2</span>Could Thiago also use the AAA model and continue the conversation? What could he say?</p>' + ta("f8b2", "No, I’ve never been, but I’d like to. I’ve been to … What’s Boston like?", 50) +
          model("m8b", "Show answers", "1 Yes. Answer: <i>That’s right. I’m from Boston.</i> Add: <i>I went to university there.</i> Ask: <i>Do you know it?</i><br>"
                "2 Yes, for example: <i>No, I’ve never been, but I’d like to. I’ve only been to New York. What’s Boston like in the summer?</i>") +
          '<p class="ins" style="margin-top:20px"><b>C</b> Watch Video B again and find two more examples of the AAA model.</p>' + video("1.3.3") + ta("f8c", "1 …\n2 …", 60) +
          model("m8c", "Show answers", "Azra: <i>Well, I was born in Istanbul</i> (answer), <i>but my parents moved to London when I was five. We go back quite often to see family</i> (add). <i>Do you know Turkey?</i> (ask)<br>"
                "Alex: <i>A little</i> (answer). <i>I went there on holiday about three years ago</i> (add). <i>Which do you prefer, London or Istanbul?</i> (ask)"))
    # 9
    s9 = ('<div class="bsec">Functional language</div><p class="ins"><b class="x">9</b>Work in pairs. Use the AAA model and the question forms in Exercise 7A to practise making small talk.</p>'
          '<div class="card" style="background:#f6f8fb;border:0"><i>Where do you come from?</i><br><u>Answer:</u> Italy. &nbsp; <u>Add:</u> I live in Trieste. &nbsp; <u>Ask:</u> Do you know it?</div>'
          '<div class="qc" id="q9">Click “New question” ▶</div><div class="ctl"><button class="btn" onclick="q9()">New question ▶</button></div>'
          '<div class="aaa"><div><b>Answer</b>%s</div><div><b>Add</b>%s</div><div><b>Ask</b>%s</div></div>' % (inp("p9_1", 220), inp("p9_2", 220), inp("p9_3", 220)) +
          '<p class="hint">Answer the question on the card out loud with AAA. Write your best one. Then ask your teacher the same question.</p>'
          '<div class="gbox"><div class="gh">Pronunciation bank: Showing interest in small talk</div><p>We show interest with our voice: start high and go down. Click, listen and repeat with the same intonation.</p><div class="react">%s</div></div>'
          % "".join('<button onclick="say(this.textContent)">%s</button>' % r for r in ["Really?", "Oh, that’s interesting!", "That sounds great!", "Oh, nice!", "Lucky you!", "Oh no! What happened?", "How was it?", "Me too!"]))
    # 10 Task
    SIT = ["at the coffee machine", "on an aeroplane", "during a conference", "in the staff canteen", "at a train station", "before a video call starts (2026)", "at the hotel breakfast in Barcelona (2026)"]
    TOP = ["food", "holidays", "home town", "music", "sports", "the weather"]
    s10 = ('<div class="bsec wr">Task</div><p class="ins"><b class="x">10</b><b>A</b> Work in pairs. Choose one of the situations below to practise making small talk.</p>'
           '<div class="chips">%s</div>' % "".join("<span>%s</span>" % x for x in SIT) +
           '<p class="ins"><b>B</b> Practise making small talk using the AAA model and the expressions in Exercise 7A to discuss two or more of these topics. Remember to show interest as you speak.</p>'
           '<div class="chips">%s</div>' % "".join("<span>%s</span>" % x for x in TOP) +
           '<div class="card"><b>🎲 Situation + topics</b><div class="qc" id="sit" style="font-size:19px">Click “Roll” ▶</div><div class="ctl"><button class="btn" onclick="roll()">Roll ▶</button><span class="res" id="tm"></span><button class="btn l" onclick="timer3()">⏱ 3 minutes</button></div></div>'
           '<p class="ins"><b>C</b> Work with a different partner. Choose a different situation and topic(s) from the lists in Exercises 10A and 10B.</p>'
           '<p class="hint">In our lesson your teacher is your partner. Roll again for a new situation.</p>'
           '<p class="ins"><b>D</b> Tell the class what you learnt about your partners.</p>' + ta("t10d", "My partner is from … She likes … She went to … last year.", 70) +
           '<div style="margin-top:20px">%s</div>' % (SELF % "I can make small talk using a simple model. How well can you do this now?"))
    return [("7A", s7), ("7B–C", s7b), ("8", s8), ("9", s9), ("10", s10)], Q7, SIT, TOP

def lesson_page():
    K = {}
    s1 = ('<div class="bsec">Lead-in</div><p class="ins"><b class="x">1</b><b>A</b> Work in pairs. Read the comment about small talk and discuss whether you agree or disagree.</p>'
          '<div class="quote">‘Small talk’ is an unimportant conversation about unimportant things, usually with people you don’t know very well.</div>' +
          '<div class="tf">%s</div>' % radio("l1a", ["I agree", "I partly agree", "I disagree"]) + ta("l1a_t", "I (don’t) agree because …", 50) +
          '<p class="ins" style="margin-top:18px"><b>B</b> Discuss the questions.</p>' +
          '<p class="ins"><span class="q">1</span>In which situations and places can small talk take place? Make a list.</p>' + ta("l1b_1", "at a conference, in a lift, …", 44) +
          '<p class="ins"><span class="q">2</span>Why do people make small talk?</p>' + ta("l1b_2", "", 40) +
          '<p class="ins"><span class="q">3</span>What do you usually talk about when you meet someone for the first time?</p>' + ta("l1b_3", "", 40))
    TOP = ["family", "health", "home town", "music", "personal finances", "the place you are in", "politics", "religion", "sports", "travel", "the weather"]
    s1c = ('<div class="bsec">Lead-in</div><p class="ins"><b>C</b> Where on the line would you put these small talk topics? Explain your choice.</p>'
           '<div class="line"><span>⟵ I definitely would talk about this.</span><span>I definitely wouldn’t talk about this. ⟶</span></div>' +
           "".join('<div class="row"><b class="w" style="min-width:170px">%s</b> %s</div>' % (t, sel("l1c_%d" % i, ["1 · definitely would", "2 · probably would", "3 · it depends", "4 · probably wouldn’t", "5 · definitely wouldn’t"], 220)) for i, t in enumerate(TOP)) +
           '<div class="card">🗣 Explain: <i>I’d definitely talk about the weather — it’s a safe topic. I wouldn’t talk about politics with a new client because …</i></div>' +
           model("m1c", "What the video says", "In the Conclusions video: choose your topic carefully and don’t be too negative. Don’t talk about personal finances, politics, religion or other very personal topics."))
    secs = [("1A–B", s1), ("1C", s1c)] + ex_video(K, "", "Did you watch this at home (Before class)? Quickly tell your teacher your answers. If not, watch it now.")
    secs.append(("6", '<div class="bsec">Reflection</div><p class="ins"><b class="x">6</b>Think about how good you are at making small talk. In pairs, discuss how you could improve your skills.</p>' +
                 '<div class="tf">%s</div>' % "".join('<label class="opt" style="display:inline;margin-right:10px"><input type="radio" name="r6s" data-k="r6s" value="%d"> %s</label>' % (i, l) for i, l in enumerate(["😬 not good", "🙂 OK", "😎 very good"])) +
                 ta("r6t", "I’m good at … I find it difficult to … To improve, I can …", 60) +
                 '<div class="card">Ideas: prepare 3 safe questions before an event · use AAA · react: <i>Really? That’s interesting!</i> · don’t only answer “Yes / No” · remember people’s names</div>'))
    more, *_ = ex_7_to_10(K)
    secs += more
    js = VJS + CSS + r"""
const Q9=""" + str([q for q in ["Where do you come from?", "What do you think about this hotel?", "How long was your trip?", "What do you know about our company?", "Do you know Barcelona?",
                                  "Which do you prefer, tea or coffee?", "Do you know Anna from Marketing?", "What are you doing in Kyiv this week?", "What do you think about the conference?", "How long was your flight?",
                                  "Which do you prefer, summer or winter holidays?", "What are you doing at the weekend?"]]) + r""";let q9i=-1;
function q9(){q9i=(q9i+1+Math.floor(Math.random()*(Q9.length-1)))%Q9.length;$("q9").textContent=Q9[q9i];say(Q9[q9i])}
const SIT=["at the coffee machine","on an aeroplane","during a conference","in the staff canteen","at a train station","before a video call starts","at the hotel breakfast in Barcelona"],TOP=["food","holidays","home town","music","sports","the weather"];
function roll(){const s=SIT[Math.floor(Math.random()*SIT.length)];const t=TOP.slice().sort(()=>Math.random()-.5).slice(0,2);$("sit").innerHTML="📍 "+s+"<br>💬 "+t.join(" + ")}
let tmr=null;function timer3(){clearInterval(tmr);let s=180;const e=$("tm");const f=()=>{e.textContent="⏱ "+Math.floor(s/60)+":"+String(s%60).padStart(2,"0");if(s--<=0){clearInterval(tmr);e.textContent="⏱ Time!"}};f();tmr=setInterval(f,1000)}
"""
    return page("1.3", "Small talk", "LESSON", "Learners can make small talk using a simple model.", "BP A2+ 1.3 Small talk · Lesson", CODE, secs, K, VOC,
                acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, footer="Videos 1.3.1–1.3.4 from the coursebook (YouTube). ", extra_js=js)

def flip_page():
    K = {}
    intro = ('<div class="bsec">Before class</div><p class="ins">Watch four short videos at home (about 6 minutes in total) and answer the questions. In class, we will use them to practise small talk.</p>'
             '<div class="card"><b>The story:</b> Jasmine is American. She is starting a new job at TGC, a consultancy in Dublin. Tonight TGC has a welcome dinner for the new employees, but Jasmine is late …</div>'
             '<p class="ins">Before you watch: what do you usually talk about with people you don’t know well?</p>' + ta("b0", "the weather, …", 44))
    secs = [("Start", intro)] + ex_video(K, "h", "")
    secs.append(("Done", '<div class="bsec">Before class</div><p class="ins">One question for your teacher: which tip from the Conclusions video do you find most useful? Why?</p>' + ta("b9", "", 50) +
                 '<div style="margin-top:20px">%s</div>' % (SELF % "I understood the videos.")))
    return page("1.3", "Small talk", "BEFORE CLASS", "Watch the videos at home. In class, we practise small talk.", "BP A2+ 1.3 Small talk · Before class", CODE, secs, K, VOC,
                acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, footer="Videos 1.3.1–1.3.4 from the coursebook (YouTube). ", extra_js=VJS + CSS)

def hw_page():
    K = {}
    # 1 Questions + answers (conference in Barcelona)
    QA = [("Where do you come from?", "I’m from Lviv, in the west of Ukraine."), ("What do you think about the hotel?", "It’s very nice, and the breakfast is great."),
          ("How long was your flight?", "About three hours."), ("What do you know about the speaker?", "Not much. I think she works for Google."),
          ("Do you know Barcelona?", "A little. I was here for a conference two years ago."), ("Which do you prefer, the beach or the mountains?", "The mountains. I love hiking."),
          ("Do you know Marta from Sales?", "Yes, we met at the welcome dinner."), ("What are you doing after the conference?", "I’m staying for the weekend. I want to see the Sagrada Família.")]
    ans = shuf([a for _, a in QA])
    for i, (_, a) in enumerate(QA): K["h1_%d" % (i + 1)] = [a]
    s1 = ('<div class="bsec">Functional language</div><p class="ins"><b class="x">1</b>You are at a conference coffee break in Barcelona. Match the questions with the answers.</p>' +
          "".join('<div class="row">%d. %s<br>%s%s</div>' % (i + 1, q, sel("h1_%d" % (i + 1), ans, 460), fb("h1_%d" % (i + 1))) for i, (q, _) in enumerate(QA)) + ctl("h1"))
    # 2 Make questions
    MQ = [("you / come / do / where / from", "where do you come from"), ("was / how / your / long / trip", "how long was your trip"),
          ("think / about / do / you / what / the food", "what do you think about the food"), ("know / do / you / Madrid", "do you know madrid"),
          ("prefer / which / you / do / , trains or planes", "which do you prefer, trains or planes"), ("doing / are / you / what / in Barcelona", "what are you doing in barcelona")]
    for i, (_, a) in enumerate(MQ): K["h2_%d" % (i + 1)] = [a, a.replace(",", "")]
    s2 = ('<div class="bsec">Functional language</div><p class="ins"><b class="x">2</b>Put the words in order to make small talk questions.</p>' +
          "".join('<div class="row">%d. <i>%s</i><br>%s ?%s</div>' % (i + 1, w, inp("h2_%d" % (i + 1), 420), fb("h2_%d" % (i + 1))) for i, (w, _) in enumerate(MQ)) + ctl("h2"))
    # 3 AAA: choose the best add / ask
    AA = [("Where do you come from?", "I’m from Ukraine.", ["I live in Kyiv, but I was born in Odesa.", "Yes.", "I don’t like travelling."], ["Do you know it?", "Goodbye.", "Why?"]),
          ("How long was your trip?", "About two hours.", ["The flight was on time, and the view was amazing.", "I hate planes.", "Two."], ["How was yours?", "Are you tired?", "Where is the toilet?"]),
          ("What do you think about the conference?", "It’s really interesting.", ["The first talk about AI was great.", "I don’t know.", "It’s a conference."], ["Which talk did you like?", "Is it free?", "Who are you?"])]
    s3 = '<div class="bsec">AAA</div><p class="ins"><b class="x">3</b>Complete the conversations with the AAA model. Choose the best <b>Add</b> and the best <b>Ask</b>.</p>'
    for i, (q, a, add, ask) in enumerate(AA):
        K["h3a_%d" % (i + 1)] = [add[0]]; K["h3b_%d" % (i + 1)] = [ask[0]]
        s3 += ('<div class="row"><b>— %s</b><br>Answer: <i>%s</i><br>Add: %s%s<br>Ask: %s%s</div>' %
               (q, a, sel("h3a_%d" % (i + 1), shuf(add), 380), fb("h3a_%d" % (i + 1)), sel("h3b_%d" % (i + 1), shuf(ask), 260), fb("h3b_%d" % (i + 1))))
    s3 += ctl("h3a") + ctl("h3b")
    # 4 Topics
    TOP = [("the weather", "OK"), ("your salary", "avoid"), ("your trip to the conference", "OK"), ("politics", "avoid"), ("the food at the event", "OK"), ("religion", "avoid"), ("your home town", "OK"), ("how much your flat cost", "avoid")]
    for i, (_, a) in enumerate(TOP): K["h4_%d" % (i + 1)] = [a]
    s4 = ('<div class="bsec">Small talk tips</div><p class="ins"><b class="x">4</b>Is it OK to talk about it with a person you don’t know well, or better to avoid it?</p>' +
          "".join('<div class="row">%s %s%s</div>' % (t, sel("h4_%d" % (i + 1), ["OK", "avoid"], 110), fb("h4_%d" % (i + 1))) for i, (t, _) in enumerate(TOP)) + ctl("h4"))
    # 5 Writing
    s5 = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">5</b>You meet a new colleague at the welcome dinner of a conference in Barcelona. Write a short small talk conversation (8–10 lines). Use the AAA model at least twice and two questions from the lesson.</p>' +
          ta("h5", "A: Hi, I’m … Nice to meet you.\nB: …", 220) + '<p class="hint" id="h5c"></p>' +
          '<div style="margin-top:20px">%s</div>' % (SELF % "I can make small talk using a simple model. How well can you do this now?"))
    js = VJS + CSS + r"""function wc(){const t=document.querySelector('.g[data-k="h5"]');if(!t)return;const n=(t.value.trim().match(/\S+/g)||[]).length;$("h5c").textContent=n+" words"}
document.addEventListener("input",e=>{if(e.target.dataset&&e.target.dataset.k==="h5")wc()});window.afterFill=wc;"""
    return page("1.3", "Small talk", "HOMEWORK", "Small talk questions, the AAA model and safe topics.", "BP A2+ 1.3 Small talk · Homework", CODE,
                [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5)], K, VOC, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, extra_js=js)

d = os.path.join(ROOT, "all"); os.makedirs(d, exist_ok=True)
for name, fn in (("flip.html", flip_page), ("lesson.html", lesson_page), ("hw.html", hw_page)):
    h = fn(); open(os.path.join(d, name), "w").write(h); print("ok", name, len(h))
