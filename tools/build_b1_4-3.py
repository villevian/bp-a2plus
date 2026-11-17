"""Business Partner B1 · 4.3 Communication skills: Managing conversations — LESSON (book version, videos from YouTube), Supabase sync.
Usage: python3 build_b1_4-3.py OUTDIR [STUDENT_CODE]  -> OUTDIR/lesson.html
"""
import sys, os
from bp_page import page, fb, sel, inp, ta, ctl, radios, SELF
OUTDIR = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
os.makedirs(OUTDIR, exist_ok=True)
VID = {"4.3.1": ("rNaJdDuQXSA", "Alex and Beata talk about the trip to Rio"), "4.3.2": ("8GaoWS-02Gg", "Option A – Beata tries to stay on track"),
       "4.3.3": ("U-ejfUrC5Rw", "Option B – Beata goes with the flow"), "4.3.4": ("vT7vrxUVTwE", "Conclusions")}
def video(n):
    y, t = VID[n]
    return ('<div class="vbox"><div class="vt"><span class="vn">▶ %s</span> %s <a href="https://www.youtube.com/watch?v=%s" target="_blank">open on YouTube</a></div>'
            '<div class="fr"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0&cc_load_policy=1" allowfullscreen loading="lazy"></iframe></div></div>') % (n, t, y, y)
def qa(k, q, a, h=56):
    return '<p class="ins"><span class="q">%s</span>%s</p>%s<button class="btn l" onclick="model(\'m_%s\')" style="margin-top:6px">Show answer</button><div class="model" id="m_%s">%s</div>' % (
        k.split("_")[-1], q, ta(k, "", h), k, k, a)
K = {}
s1 = ('<div class="bsec">Lead-in</div><p class="ins"><b class="x">1</b><b>A</b> Work in small groups. Give examples of your own experiences of meeting people who are different from you. Here are some possible differences to think about.</p>'
      '<div class="two">' + "".join('<div class="card">%d. %s</div>' % (i + 1, x) for i, x in enumerate(["their national culture", "their age", "their education", "the culture of their organisation", "their work/profession"])) + '</div>' +
      ta("l1a", "Example: I once worked with … They were different because …", 80) +
      '<p class="ins"><b>B</b> Discuss the questions.</p><div class="card">1. What is easy or difficult about such encounters?</div><div class="card">2. How is it different from meeting friends, colleagues and members of your family? Why?</div>' + ta("l1b", "Notes …", 70))
Q2 = [("Has Alex ever been to Rio de Janeiro?", "Yes, he has."), ("How well does he know Mateo?", "He has met him twice, on trips with Daniel."),
      ("What does Alex mean when he says, ‘It’s difficult to stay on track sometimes’?", "He means that Mateo likes to talk about other topics."),
      ("What preparation has Beata done for the trip?", "She has done some background reading."),
      ("What advice does Alex give Beata? Do you think it is useful advice? Why?", "Mateo likes the sound of his own voice and can be domineering at times. The trip will be like any other trip. Mateo likes to multitask. Alex suggests she ‘goes with the flow’.")]
s2 = ('<div class="bsec" style="color:#c2185b">VIDEO</div><p class="ins"><b class="x">2</b><b>A</b> Watch the video of Alex and Beata talking about Beata’s forthcoming trip to Rio de Janeiro. Answer the questions.</p>' + video("4.3.1") +
      '<p class="hint">💡 <b>like the sound of your own voice</b> = talk a lot and be very confident · <b>go with the flow</b> = be relaxed and do what is easiest</p>' +
      "".join(qa("v2_%d" % (i + 1), q, a) for i, (q, a) in enumerate(Q2)) +
      '<p class="ins"><b>B</b> Watch the video again. Why is Beata worried about the trip?</p>' + ta("v2b", "", 56) +
      '<button class="btn l" onclick="model(\'m_v2b\')" style="margin-top:6px">Show answer</button><div class="model" id="m_v2b">She feels it may be difficult and there won’t be enough time to learn about the market, get to know Mateo and build a good working relationship.</div>')
QA_ = [("What topics do Beata and Mateo talk about?", "Family and Mateo’s previous trips to Poland (Warsaw)."),
       ("How does Beata try to turn the discussion towards the Diabsensor?", "She tries to change the subject at every chance she gets: ‘Can we move to the Diabsensor?’, ‘Is this a good moment to start talking about …?’, ‘I really think we should get to …’"),
       ("How does Mateo react to these attempts?", "He ignores them or tells her they will discuss the Diabsensor later."),
       ("Alex warned Beata that Mateo likes to multitask. What example of this do we see?", "He takes a phone call during the meeting."),
       ("Overall, how well does Beata manage the conversation?", "She does not manage to get Mateo to talk about the Diabsensor, and Mateo seems a little unhappy.")]
QB_ = [("What topics do Beata and Mateo talk about?", "Family and Mateo’s previous trips to Poland (Warsaw)."),
       ("How does Beata show an interest in what Mateo is saying?", "She answers his questions and asks her own (‘You sound like you know Warsaw well.’, ‘Of course.’)."),
       ("Does Beata try to turn the discussion towards the Diabsensor?", "No, she doesn’t. She goes with the flow and waits for Mateo to turn the discussion towards it."),
       ("Alex warned Beata that Mateo likes to multitask. What example of this do we see?", "He takes a phone call during the meeting."),
       ("Overall, how well does Beata manage the conversation?", "She goes with the flow. She doesn’t talk about the Diabsensor, but the relationship stays friendly.")]
s3 = ('<div class="bsec" style="color:#c2185b">VIDEO</div><p class="ins"><b class="x">3</b><b>A</b> Based on what you have seen so far, how should Beata behave in the meeting with Mateo? Decide which option to watch first.</p>' +
      radios("opt3", [("A", "<b>Option A –</b> Listen to Mateo, but politely try to stay on the topic of the Diabsensor and not be distracted. Stay focused on why she is in Rio."),
                      ("B", "<b>Option B –</b> Listen to Mateo, show interest in what he is saying and not worry about the Diabsensor. Go with the flow – he is the client, after all.")]) +
      ta("opt3why", "I chose this option because …", 50) +
      '<p class="ins"><b>B</b> Watch the videos and answer the questions for each video.</p>'
      '<div class="two"><div><h4 class="oh">Option A</h4>%s%s</div><div><h4 class="oh">Option B</h4>%s%s</div></div>' % (
          video("4.3.2"), "".join(qa("a3_%d" % (i + 1), q, a, 46) for i, (q, a) in enumerate(QA_)), video("4.3.3"), "".join(qa("b3_%d" % (i + 1), q, a, 46) for i, (q, a) in enumerate(QB_))))
s4 = ('<div class="bsec">Discussion</div><p class="ins"><b class="x">4</b>In pairs, discuss what you have learnt from Beata’s experience about adapting your communication style.</p>' +
      qa("d4_1", "What is the effect of going with the flow?", "Beata doesn’t get to discuss her agenda, but she might build a better relationship with Mateo.", 60) +
      qa("d4_2", "What is the effect of focusing on the task in hand?", "Beata’s attempts to bring the conversation back to the Diabsensor affect the relationship: Mateo is less friendly in Option A than in Option B.", 60))
s5 = ('<div class="bsec" style="color:#c2185b">VIDEO</div><p class="ins"><b class="x">5</b>Watch the Conclusions section of the video and note down the main learning point. How far do you agree with this? Why?</p>' + video("4.3.4") +
      ta("c5", "Main learning point: … / I agree / don’t agree because …", 90) +
      '<button class="btn l" onclick="model(\'m_c5\')" style="margin-top:6px">Show answer</button><div class="model" id="m_c5">Going with the flow might help build a better relationship with the business partner, but it takes more time. Focusing on the task might save time, but it may affect the relationship.</div>')
s6 = ('<div class="bsec">Reflection</div><p class="ins"><b class="x">6</b>Think about the following questions. Then discuss your answers with a partner.</p>'
      '<p class="ins"><span class="q">1</span>Compare yourself to Beata in a similar situation. How do you think you would manage?</p>' + ta("r6_1", "", 70) +
      '<p class="ins"><span class="q">2</span>Is ‘go with the flow’ a useful tip for you when you meet new people? Why / Why not?</p>' + ta("r6_2", "", 70))
P7 = [("There will be plenty of time for that later.", "S"), ("I really think we should get to the …", "C"), ("Is this a good moment to start talking about the … ?", "C"), ("We’ll come to that later.", "S"),
      ("That reminds me.", "C"), ("We’ll get to the … in a moment.", "S"), ("Can we move to … ?", "C"), ("Before I forget, …", "C")]
for i, (p, a) in enumerate(P7): K["f7_%d" % (i + 1)] = [a]
s7 = ('<div class="bsec">Functional language <span class="sub">Changing the subject and staying on track</span></div>'
      '<p class="ins"><b class="x">7</b>Look at these phrases from the video. Decide which are for changing the subject (C) and which are for staying on track (S).</p>' +
      "".join('<div class="row">%d. %s %s%s</div>' % (i + 1, sel("f7_%d" % (i + 1), ["C", "S"], 70), p, fb("f7_%d" % (i + 1))) for i, (p, a) in enumerate(P7)) + ctl("f7"))
A8 = ["can we move to|could we move to", "this a good moment to start talking about the", "get to the|come to the", "in a moment", "reminds me", "will be plenty of time for that later|’ll be plenty of time for that later|'ll be plenty of time for that later"]
for i, a in enumerate(A8): K["f8_%d" % (i + 1)] = a.split("|")
def g(n, w=260): return '<sup>%d</sup>%s' % (n, inp("f8_%d" % n, w))
s8 = ('<div class="bsec">Functional language</div><p class="ins"><b class="x">8</b>Use words from the phrases in Exercise 7 to complete the dialogue. Then practise reading the dialogue.</p><div class="dlg">'
      '<p><b>A:</b> So, %s item 3 on the agenda, the new minibus?</p>' % g(1, 160) +
      '<p><b>B:</b> Yes, of course. It will be delivered next Monday morning. So we can use it for the trip to the factory on Tuesday.</p>'
      '<p><b>A:</b> Is %s factory visit? What’s the plan?</p>' % g(2, 330) +
      '<p><b>B:</b> We’ll %s details of the factory visit %s.</p>' % (g(3, 110), g(4, 120)) +
      '<p><b>A:</b> Actually, that %s, I need to check if my children are being picked up from school today. The bus company is on strike.</p>' % g(5, 120) +
      '<p><b>B:</b> I’m sure there %s. Could we first finish discussing the minibus? Then we’ll have a break and you can sort out your children’s bus.</p></div>' % g(6, 290) +
      "".join(fb("f8_%d" % (i + 1)).replace('<span class="h">', '<sup>%d</sup> <span class="h">' % (i + 1)) for i in range(6)) + ctl("f8"))
PR = [("bus → buses", "extra"), ("agenda → agendas", "no"), ("choice → choices", "extra"), ("client → clients", "no"), ("decide → decides", "no"), ("manage → manages", "extra"), ("office → offices", "extra"), ("talk → talks", "no")]
for i, (w, a) in enumerate(PR): K["pr_%d" % (i + 1)] = [a]
s9 = ('<div class="bsec">Speaking</div><p class="ins"><b class="x">9</b><b>A</b> Work in pairs and discuss one of these topics using phrases from Exercise 7. One person tries to talk about the topic, the other tries to change the subject. After a few minutes, change partners and choose a new topic.</p>'
      '<div class="two">' + "".join('<div class="card">%s</div>' % t for t in ["Plans for next week", "A new smartphone on the market", "Organising a surprise birthday party for a friend", "A trip abroad"]) + '</div>' +
      '<p class="ins"><b>B</b> Write short dialogues based on your discussions.</p>' + ta("w9", "A: …\nB: …", 140) +
      '<div class="gbox"><div class="gh">Pronunciation bank: -(e)s endings</div><p>We add an extra syllable /ɪz/ after the sounds /s/, /z/, /ʃ/, /tʃ/, /dʒ/: <i>go – goes</i> (1 syllable) but <i>age – ag·es</i> (2 syllables).</p>'
      '<p>Does the word get an extra syllable?</p>' + "".join('<div class="row">%d. %s %s%s</div>' % (i + 1, w, sel("pr_%d" % (i + 1), ["extra", "no"], 90), fb("pr_%d" % (i + 1))) for i, (w, a) in enumerate(PR)) + ctl("pr") + '</div>')
SUP = ("<b>Student S – Supplier</b><br>Your company has just produced a new app for managing a database of business contacts. Your aim is to present it and agree on a trial.<ul>"
       "<li>Key points: easy to install (10 minutes), simple to use, works on phone and laptop, syncs with Outlook and Google Contacts.</li><li>Price: €4 per user per month; 30-day free trial.</li>"
       "<li>You don’t have much time: you have another meeting in 40 minutes. Try to stay on track politely.</li></ul>")
CLI = ("<b>Student C – Client</b><br>You are interested in learning about the app, but that will be later. First you want to talk about other things:<ul>"
       "<li>the supplier’s journey and the new office you have just moved to;</li><li>a conference you both went to last year;</li><li>a problem with your current system (your sales team lost 200 contacts last month).</li>"
       "<li>When you finally talk about the app, ask about price, data security and training for your team.</li></ul>")
s10 = ('<div class="bsec wr">TASK</div><p class="ins"><b class="x">10</b><b>A</b> Work in pairs. Read the situation and decide who will be the supplier (S) and who will be the client (C). Read your instructions.</p>'
       '<div class="ext">A supplier is visiting a client to talk about a new app which his/her company has just produced. This app will be very useful for managing a database of business contacts, and is easy to install, simple to use and inexpensive.</div>'
       '<div class="two"><div><button class="btn l" onclick="model(\'rS\')">Role card S</button><div class="model" id="rS">%s</div></div><div><button class="btn l" onclick="model(\'rC\')">Role card C</button><div class="model" id="rC">%s</div></div></div>' % (SUP, CLI) +
       '<p class="ins"><b>B</b> Hold your meeting. Try to change the subject and stay on track as necessary, using phrases from Exercise 7.</p>'
       '<p class="ins"><b>C</b> When you have finished, discuss how the meeting went. Was it successful? What was easy and what was difficult? What could you do better?</p>' + ta("t10c", "It was easy / difficult to … Next time I will …", 80) +
       '<p class="ins"><b>D</b> Find a new partner, change roles and repeat the conversation.</p>' +
       '<div style="margin-top:20px">%s</div>' % (SELF % "How successfully have you achieved the lesson outcome?"))
VOC = [("Changing the subject", ["Can we move to …?", "Is this a good moment to start talking about …?", "I really think we should get to …", "That reminds me.", "Before I forget, …"]),
       ("Staying on track", ["We’ll come to that later.", "We’ll get to … in a moment.", "There will be plenty of time for that later."]),
       ("From the video", ["stay on track", "change the subject", "go with the flow", "like the sound of your own voice", "domineering", "multitask", "push your agenda", "business relationship"])]
EXTRA_CSS = ('const st=document.createElement("style");st.textContent=".vbox{margin:10px 0 14px;max-width:720px}.vt{font-weight:500;margin-bottom:4px}.vt .vn{color:#c2185b;font-weight:600;margin-right:6px}.vt a{font-size:13px;color:#c2185b;margin-left:8px}'
             '.fr{position:relative;padding-top:56.25%}.fr iframe{position:absolute;inset:0;width:100%;height:100%;border:0}.oh{color:#c4642a;margin:6px 0}.dlg p{margin:6px 0;line-height:2.2}";document.head.appendChild(st);')
html = page("4.3", "Managing conversations", "LESSON", "Learners are aware of different approaches to managing a conversation and can use a range of expressions to signal and respond to a change of topic.",
            "BP B1 4.3 Managing conversations · Lesson", CODE, [(str(i + 1), s) for i, s in enumerate([s1, s2, s3, s4, s5, s6, s7, s8, s9, s10])], K, VOC,
            footer="Videos: Business Partner B1 (Pearson), YouTube. ", extra_js=EXTRA_CSS)
open(os.path.join(OUTDIR, "lesson.html"), "w").write(html)
print("ok")
