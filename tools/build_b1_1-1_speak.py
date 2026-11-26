"""B1 1.1 Transferable skills · In class: speaking (soft skills 2026). Usage: build_b1_1-1_speak.py OUTDIR CODE"""
import sys, os
from bp_page import page, fb, sel, inp, ta, ctl, SELF

OUTDIR = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
os.makedirs(OUTDIR, exist_ok=True)
K = {}

def card(h, bg="#fff", bd="#e8894a"):
    return '<div class="card" style="margin-top:12px;background:%s;border-left:4px solid %s">%s</div>' % (bg, bd, h)
def qlist(items):
    return "".join(card('<b>%s)</b> %s' % ("abcdefghij"[i], q), "#fbfbfd", "#c9cbe8") for i, q in enumerate(items))
def X(n, l): return '<b class="x">%s</b><b>%s</b> ' % (n, l)
BIG = ('<div style="background:#fff7ef;border:1.5px dashed #e8894a;border-radius:12px;padding:8px 14px;margin:4px 0 12px;font-size:15px">🧳 <b>Our big question:</b> '
       '<i>What is in your suitcase – and how will you show it to an international company?</i></div>')

s1 = ('<div class="bsec">Warm-up</div>' + BIG +
      '<p class="ins">' + X(1, "A") + 'In your homework you wrote: <i>“I am best.”</i> Prove it in <b>30 seconds</b> – but you can’t use the words <b>best</b>, <b>good</b> or <b>experienced</b>.</p>' +
      card('💡 Try: <i>I’ve …</i> · <i>Last year I …</i> · <i>The result was …</i> · <i>My team / users …</i>', "#f4f6ff", "#5b5fc7") +
      '<p class="ins" style="margin-top:22px">' + X(1, "B") + 'Write the strongest sentence you said.</p>' + ta("k1b", "I’ve …", 50))

s2 = ('<div class="bsec">Your story – live</div>' +
      '<p class="ins">' + X(2, "A") + 'Tell your <b>60-second story</b> (Step 9B of Before class) <b>from memory</b>. Don’t read it. Your teacher is a recruiter – she can interrupt you.</p>' +
      card('🎧 The recruiter may ask: <i>“Sorry – what exactly did <b>you</b> do there?”</i> · <i>“What was the result?”</i> · <i>“Can you give me an example?”</i>', "#f4f6ff", "#5b5fc7") +
      '<p class="ins" style="margin-top:22px">' + X(2, "B") + 'Be honest. Which sentences in your story are 100% <b>yours</b>? Did AI help you write it? What was easy and what was hard to say without the text?</p>' +
      ta("k2b", "The sentences that are really mine: … It was hard to say … because …", 80) +
      card('💬 <b>2026 truth:</b> using AI is normal. But in an interview there is no AI. <b>If you can’t say it live, it’s not your story yet.</b>', "#fff8d6", "#e0a100"))

BIGQ = ["If AI writes half your code, what exactly are you paid for?",
        "Tell me about a time AI was confidently wrong – and you caught it. What would have happened if you hadn’t?",
        "You were a team lead. What was the worst conflict in your team – and what did <b>you</b> do wrong?",
        "Is <b>flexibility</b> a real skill – or a nice word for “I can’t say no”?",
        "Senior: is it about <b>years</b> or about <b>decisions</b>?",
        "In an international team, what’s harder – English, or silence on Zoom and slow replies in Slack?",
        "Which soft skill do you <b>not</b> have? What would your old team say about you?",
        "Your side project <b>aliasgame.fun</b>: what did real users teach you that your job never did?"]
s3 = ('<div class="bsec">Speaking <span class="sub">Soft skills in 2026</span></div>' +
      '<p class="ins">' + X(3, "A") + 'Discuss the questions with your teacher. Give <b>real examples</b>, not adjectives. Use words from the lesson: <i>audit your experience, bridge the gap, AI-proof, signal initiative, lead by example, through line</i>.</p>' +
      qlist(BIGQ) +
      '<p class="ins" style="margin-top:22px">' + X(3, "B") + 'Which question made you think the most? What is your answer now – in 2–3 sentences?</p>' + ta("k3b", "The question that made me think was … because …", 80))

PH = ["What I actually did was …", "The result was …", "To be honest, …", "I learnt that …", "Looking back, I would …", "That’s a good question. Let me think …"]
IQ = ["Tell me about yourself.",
      "Why should we hire you – and not a junior developer with AI tools?",
      "Give an example of a time you influenced a decision without having authority.",
      "Tell me about a time you disagreed with your PM. What happened?",
      "What’s your biggest weakness – and what are you doing about it?"]
s4 = ('<div class="bsec">Role-play <span class="sub">An interview at an international company</span></div>' +
      '<p class="ins">' + X(4, "A") + 'Your teacher is a recruiter. Answer her questions. Use the phrases in the box.</p>' +
      card("📦 " + " · ".join("<i>%s</i>" % p for p in PH), "#f4f6ff", "#5b5fc7") + qlist(IQ) +
      '<p class="ins" style="margin-top:22px">' + X(4, "B") + 'Feedback from your teacher: one thing that worked and one thing to make stronger.</p>' +
      ta("k4b", "Worked: …\nMake stronger: …", 70))

SK = ["writing code", "estimating tasks", "explaining trade-offs to business people", "giving feedback to a colleague", "conflict resolution",
      "writing clear async messages in Slack", "taking ownership of a release", "working with people from other cultures", "judging if AI output is correct"]
OPT = ["—", "AI does it", "AI helps", "Only human"]
s5 = ('<div class="bsec">Thinking <span class="sub">What is valuable in 2026?</span></div>' +
      '<p class="ins">' + X(5, "A") + 'Sort the skills. There’s no single right answer – be ready to explain your choice.</p>' +
      "".join('<div class="row">%s) %s → %s</div>' % ("abcdefghi"[i], s, sel("k5a_%d" % (i + 1), OPT, 150)) for i, s in enumerate(SK)) +
      '<p class="ins" style="margin-top:22px">' + X(5, "B") + 'Choose <b>two</b> soft skills you want to develop on this course. How will you know you’ve got better?</p>' +
      ta("k5b", "1 … – I’ll know I’ve got better when …\n2 …", 80))

ERR = [("She say that your experience is valuable.", ["She says that your experience is valuable."]),
       ("My estimation skill very good.", ["My estimation skill is very good.", "My estimation skills are very good."]),
       ("All of these terms is industry-specific terms.", ["All of these terms are industry-specific terms.", "All of these terms are industry-specific."]),
       ("I’m going to bridge the gap by studding English.", ["I’m going to bridge the gap by studying English.", "I'm going to bridge the gap by studying English."]),
       ("It’s about a situation when you founding a new job.", ["It’s about a situation when you are finding a new job.", "It’s about a situation when you find a new job.", "It's about a situation when you find a new job.", "It's about a situation when you are finding a new job.", "It’s about a situation when you are looking for a new job.", "It's about a situation when you are looking for a new job."]),
       ("You should finding something which you love.", ["You should find something which you love.", "You should find something that you love.", "You should find something you love."]),
       ("One part of my job it’s oftener conflict resolution.", ["One part of my job is often conflict resolution.", "Part of my job is often conflict resolution.", "One part of my job is conflict resolution.", "A big part of my job is conflict resolution."])]
rows = ""
for i, (bad, good) in enumerate(ERR):
    k = "k6_%d" % (i + 1); K[k] = good
    rows += '<div class="row">%s) <s style="color:#a33">%s</s><br>%s%s</div>' % ("abcdefg"[i], bad, inp(k, 520, "Correct sentence"), fb(k))
s6 = ('<div class="bsec">Language <span class="sub">From your homework</span></div>' +
      '<p class="ins">' + X(6, "A") + 'These sentences are from your homework. Each one has a mistake. Write the correct sentence.</p>' + rows + ctl("k6"))

s7 = ('<div class="bsec">Wrap-up</div>' + BIG +
      '<p class="ins">' + X(7, "A") + 'Finish the sentence. Say it, then write it.</p>' +
      ta("k7a", "My strongest soft skill is … – and the proof is …", 60) +
      '<p class="ins" style="margin-top:22px">' + X(7, "B") + 'Homework for Monday: <b>Homework 1.1</b> and <b>Video words</b> (in your course). Next lesson: <b>1.2 Careers advice</b>.</p>' +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How confident do you feel talking about your soft skills now?"))

VOC = [("Video words", ["audit your experience", "with fresh eyes", "AI-proof skills", "bridge the gap", "industry-specific terms", "connect the dots", "skill gap", "side hustle", "signal initiative", "through line", "lead by example", "industry disruptions"]),
       ("Article", ["critical thinking", "team player", "flexibility", "a can-do attitude", "integrity", "think outside the box"])]
html = page("1.1", "Transferable skills", "IN CLASS · SPEAKING", "Talk about your soft skills with real examples and tell your career story live.",
            "BP B1 1.1 Transferable skills · Speaking", CODE,
            [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5), ("6", s6), ("7", s7)], K, VOC)
open(os.path.join(OUTDIR, "speak.html"), "w").write(html)
print("ok", OUTDIR)
