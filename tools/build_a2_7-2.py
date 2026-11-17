"""Business Partner A2 · 7.2 Services — LESSON, IT/subscriptions version ("hidden fees").
Structure mirrors the coursebook pages 70–71: Lead-in 1 · Vocabulary 2A–C, 3A–C (+ Pronunciation bank) · Listening 4A–D (audio 7.02, AI voices) · Writing 5 · Self-assessment.
Writing: Updated = an honest pricing page (no hidden fees); Classic = book task (AP Couriers advert).
Vocabulary chips on top open a card (UA translation, meaning, collocations, example).
Usage: python3 build_a2_7-2.py ROOT_LESSON_DIR [STUDENT_CODE]   e.g. ../../bp-a2/lessons/7-2
"""
import sys, os, json, re
from bp_page import page, fb, sel, inp, ta, ctl, radios, SELF
from vocab_a2 import lesson
ROOT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3b7dd8", "#e3eefb", "#2a5fb0", "#4f9be8"
TITLE, GROUPS = lesson("7.2")
K = {}

# ---------- vocabulary chips + card ----------
VITEMS = []
VOC = []
for g, ws in GROUPS:
    chips = []
    for en, uk, df, ex, co in ws:
        VITEMS.append({"en": en, "uk": uk, "df": df, "ex": ex, "co": co})
        chips.append('<a class="vw" data-i="%d">%s</a>' % (len(VITEMS) - 1, en))
    VOC.append((g, chips))

# ---------- 1 Lead-in ----------
BOX1 = ["cloud storage", "design software", "AI assistant", "video calls", "music / video streaming", "online shopping & delivery", "office software", "project management", "online courses", "recruitment"]
s1 = ('<div class="bsec">Lead-in</div><p class="ins"><b class="x">1</b>Work in pairs. Which of these services or subscriptions do you or your company pay for?</p>'
      '<div class="chips">%s</div>' % "".join("<span>%s</span>" % b for b in BOX1) +
      '<div class="card">Example: <i>My company pays for Slack and Jira. I pay for cloud storage and music streaming.</i></div>' + ta("l1", "We pay for … I pay for …", 80) +
      '<p class="hint">Extra question: How many subscriptions do you have? Do you use all of them?</p>')

# ---------- 2 Reading: three stories ----------
STORIES = [
 ("A", "Adobe", "#f2d6d6", "“A low monthly price … for a year”",
  "I wanted to use Photoshop for a small design project. On the website, the plan looked cheap — a low <b>monthly fee</b>. I clicked ‘Buy’. "
  "Three months later, my project was finished and I wanted to <b>cancel</b>. Surprise! It was not a monthly plan. It was an <b>annual plan, paid monthly</b>. "
  "To cancel, I had to <b>pay</b> an <b>early termination fee</b> — 50% of all the payments until the end of the year. This information was in <b>the small print</b>.",
  "In 2024, the US Federal Trade Commission (FTC) took the company to court. It says the company <b>hid</b> the fee and made cancelling difficult."),
 ("B", "Microsoft", "#dbe7f7", "“Pay more or cancel?”",
  "I use Word, Excel and 1 TB of <b>cloud storage</b> for my work. In 2024, the company added an <b>AI assistant</b>, Copilot, to my plan. "
  "Then the <b>annual fee</b> went up from A$109 to A$159 — a <b>price increase</b> of 45%. The email said: ‘Pay more or cancel.’ "
  "But there was a third option: a ‘Classic’ plan with no AI at the old price. You only saw it when you started to cancel!",
  "People found the <b>hidden</b> plan and wrote about it on Reddit. In 2025, the Australian regulator (&#65;CCC) took the company to court."),
 ("C", "Amazon", "#fbe9cf", "“I only wanted a phone case”",
  "I wanted to buy a phone case. On the last page there was a big button: ‘Get FREE delivery’. I clicked it — and I <b>signed up for</b> Prime, a subscription with a monthly fee. "
  "I didn’t want it! Then I tried to <b>cancel my subscription</b>. It was like a game: many pages, ‘Are you sure?’, special offers … In the end, I gave up.",
  "In 2025, the company agreed to pay $2.5 billion. Some customers <b>get a refund</b> of up to $51. Now there must be a clear ‘No, thanks’ button and an easy way to cancel."),
]
COMMENTS = [
 ("u/ticket_pain", "Concert tickets: €60. Then, on the last page, the website <b>charges</b> a €12 <b>booking fee</b>. Why not show it at the start?"),
 ("u/bank_watch", "My bank app charges a €3 <b>administration fee</b> every month. I only saw it on my statement."),
 ("u/gym_hostage", "My gym has a €50 <b>cancellation fee</b>. I’m still a member because of it 😅"),
 ("u/freelance_dev", "This is why I like a <b>fixed fee</b>: one price, and the fee <b>includes</b> everything. No <b>additional fees</b>."),
]
story_html = "".join(
    '<div class="stc" style="border-color:%s"><div class="sth" style="background:%s"><b>%s</b> %s <span class="stt">%s</span></div>'
    '<p>%s</p><p class="nx"><b>What happened next?</b> %s</p></div>' % (bg, bg, l, inp("n2b_%s" % l, 130, "company?"), t, txt, nx)
    for l, nm, bg, t, txt, nx in STORIES)
comm_html = ('<div class="rdt"><div class="rdh">💬 r/personalfinance · “What hidden fees make you angry?”</div>%s</div>'
             % "".join('<div class="rc"><span class="u">%s</span><p>%s</p></div>' % (u, t) for u, t in COMMENTS))
for l, nm, *_ in STORIES: K["n2b_%s" % l] = [nm]
SERV = {"A": "design software", "B": "office software / cloud storage / AI assistant", "C": "online shopping & delivery"}
s2 = ('<div class="bsec">Vocabulary <span class="sub">Fees</span></div>'
      '<p class="ins"><b class="x">2</b><b>A</b> Read the stories about three companies. Which services from Exercise 1 do they sell?</p>' +
      "".join('<div class="row"><span class="w">%s</span>%s <button class="btn l" style="padding:2px 10px" onclick="model(\'m2a_%s\')">Answer</button><div class="model" id="m2a_%s">%s</div></div>'
              % (l, inp("s2a_%s" % l, 300, "service(s)"), l, l, SERV[l]) for l in "ABC") +
      '<p class="ins"><b>B</b> Choose a company for each story (A–C). Write it in the gap next to the letter.</p><div class="chips"><span>Adobe</span><span>Amazon</span><span>Microsoft</span></div>' +
      story_html + "".join(fb("n2b_%s" % l) for l in "ABC") + ctl("n2b") + comm_html)

Q2C = [("charged people 50% of the remaining payments when they cancelled?", "A"), ("put the price up after it added AI?", "B"), ("signed people up for a subscription they didn’t want?", "C"),
       ("has to give money back to some customers?", "C"), ("shows a monthly price, but the plan is for one year?", "A"), ("had a problem that people found on Reddit?", "B")]
for i, (q, a) in enumerate(Q2C): K["r2c_%d" % (i + 1)] = [a]
s3 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">2</b><b>C</b> Read the stories again. Answer the questions. <span class="hint">(Open the stories in Exercise 2B if you need them.)</span></p><p>Which company …</p>' +
      "".join('<div class="tf"><span class="q">%d. %s</span>%s%s</div>' % (i + 1, q, "".join('<label class="opt" style="display:inline;margin:0 10px 0 0"><input type="radio" name="r2c_%d" data-k="r2c_%d" value="%s"> %s</label>' % (i + 1, i + 1, x, x) for x in "ABC"), fb("r2c_%d" % (i + 1)))
              for i, (q, a) in enumerate(Q2C)) + ctl("r2c", "chkRad") +
      '<details class="ad"><summary>Open the stories</summary>' + re.sub(r'<input class="g" data-k="n2b_[^>]*>', '<b>______</b>', story_html) + comm_html + '</details>')

# ---------- 3 Spidergram / matching / gaps ----------
SP_TYPES = ["annual", "hidden", "cancellation", "early termination", "booking", "administration", "fixed"]
K["sp_1"] = ["includes", "include"]
K["sp_2"] = ["pay", "charge"]; K["sp_3"] = ["charge", "pay"]
spider = ('<div class="spd"><div class="sb"><b>1</b> (the) fee %s</div><div class="sb"><b>2</b> %s / %s a/the fee</div><div class="sc">FEE</div>'
          '<div class="sb wide"><b>3</b> <u>additional</u> fee, monthly or %s fee, %s fee, %s fee, %s fee, %s fee, %s fee, %s fee</div></div>'
          % (inp("sp_1", 110), inp("sp_2", 90), inp("sp_3", 90), *[inp("spt_%d" % (i + 1), 120) for i in range(7)]))
s4 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">3</b><b>A</b> Complete the spidergram with the words in bold from the stories and the comments.</p>' + spider +
      '<div class="fb" id="fb_sp"><span class="h"></span></div><div class="ctl"><button class="btn" onclick="chkSpider()">Check</button><span class="res" id="r_sp"></span></div>'
      '<p class="hint">Group 3: any order.</p><details class="ad"><summary>Open the stories</summary>' + re.sub(r'<input class="g" data-k="n2b_[^>]*>', '<b>______</b>', story_html) + comm_html + '</details>')

M3B = [("ask someone to pay some money for a service", "charge", "a fee)"), ("an amount of money that does not change", "fixed", "fee)"), ("when you pay every month", "monthly", "fee)"),
       ("some extra money", "additional", "fee)"), ("money you pay when you stop a plan or a booking", "cancellation", "fee)"), ("you pay a fee and you get these things", "includes", ")"),
       ("a fee that the company does not show clearly", "hidden", "fee)"), ("money you pay to book a ticket or a hotel online", "booking", "fee)"),
       ("money you pay if you end a contract before the end", "early termination", "fee)"), ("a fee for paperwork or for managing your account", "administration", "fee)")]
OPTS3B = sorted(set(a for _, a, _ in M3B))
for i, (_, a, _) in enumerate(M3B): K["m3b_%d" % (i + 1)] = [a]
s5 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">3</b><b>B</b> Match the words from the spidergram with the explanations below.</p>' +
      "".join('<div class="row">%d. %s <span style="white-space:nowrap">(%s%s %s</span>%s</div>' % (i + 1, d, "the fee " if a == "includes" else "", sel("m3b_%d" % (i + 1), OPTS3B, 170), e, fb("m3b_%d" % (i + 1)))
              for i, (d, a, e) in enumerate(M3B)) + ctl("m3b") +
      '<div class="gbox"><div class="gh">Pronunciation bank: /əʊ/ and /aʊ/</div><p>Listen and repeat. Which sound is it? Click 🔊.</p><div class="two">' +
      "".join('<div class="row">%s <i style="color:#6d6e70">%s</i> <button class="btn l" style="padding:2px 10px" onclick="say1(\'%s\')">🔊</button></div>' % (w, s, w)
              for w, s in [("go", "/əʊ/"), ("now", "/aʊ/"), ("load", "/əʊ/"), ("discount", "/aʊ/"), ("video", "/əʊ/"), ("without", "/aʊ/"), ("no hidden fees", "/əʊ/"), ("account", "/aʊ/"), ("show the price", "/əʊ/"), ("how much?", "/aʊ/")]) +
      '</div></div>')

G3C = [("The design agency ", "a fee of €40 an hour.", "charges", ["charges"]),
       ("The plan is €20 a month. There is a(n) ", "fee of €5 for extra cloud storage.", "additional", ["additional"]),
       ("The AI tool has a 7-day free trial. After that, there is a ", "fee of €18.", "monthly", ["monthly"]),
       ("The fee for the online course ", "all videos and a certificate.", "includes", ["includes"]),
       ("You can pay a(n) ", "fee of €180 once a year and save 15%.", "annual", ["annual"]),
       ("There is no ", "fee if you cancel in the first 14 days.", "cancellation", ["cancellation"]),
       ("All concert tickets include a ", "fee of €3.50.", "booking", ["booking"]),
       ("Our web studio charges a ", "fee of €1,500 for a landing page — no extra costs.", "fixed", ["fixed"])]
for i, (_, _, _, a) in enumerate(G3C): K["g3c_%d" % (i + 1)] = a
s6 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">3</b><b>C</b> Complete the sentences with the correct form of the words in Exercise 3A.</p>' +
      "".join('<div class="row">%d. %s%s %s%s</div>' % (i + 1, a, inp("g3c_%d" % (i + 1), 130), b, fb("g3c_%d" % (i + 1))) for i, (a, b, _, _) in enumerate(G3C)) + ctl("g3c") +
      '<p class="ins" style="margin-top:22px">Your turn: Which hidden fees did you see in your life? Write 1–2 sentences.</p>' + ta("y3c", "Once I paid a … fee for …", 60))

# ---------- 4 Listening (audio 7.02) ----------
def player(id_):
    return ('<div class="aud"><span class="an">🔊 7.02</span><audio id="%s" controls preload="none" src="../audio/7-02.mp3"></audio>'
            '<select class="g rate" onchange="document.querySelectorAll(\'audio\').forEach(a=>a.playbackRate=+this.value)"><option value="0.85">slower</option><option value="1" selected>normal</option></select>'
            '<button class="btn l" onclick="model(\'sc_%s\')">Show script</button><div class="model" id="sc_%s">%s</div></div>') % (id_, id_, id_, SCRIPT)
from tts_dialog_text import A702
SCRIPT = "".join("<p><b>%s:</b> %s</p>" % ({"E": "Ellie", "T": "Tom"}[s], t) for s, t in A702)
s7 = ('<div class="bsec">Listening <span class="sub">Comparing recruitment agencies</span></div>'
      '<p class="ins"><b class="x">4</b><b>A</b> Work in pairs. Your company needs three new people. Which services are important for a recruitment agency to offer? Why?</p>' + ta("l4a", "It’s important that the agency … because …", 70) +
      '<p class="ins"><b>B</b> Tom and Ellie are discussing two recruitment agencies. Which agency do they choose? Why?</p>' + player("a4b") + ta("l4b", "They choose … because …", 50) +
      '<button class="btn l" onclick="model(\'m4b\')" style="margin-top:6px">Show answer</button><div class="model" id="m4b">They decide to use Jones if Jones is cheaper overall (they want to know Jones’ fee for background checks first).</div>')
G4C = [("1", ["London"]), ("2", ["six", "6"]), ("3", ["three", "3"]), ("4", ["professional"]), ("5", ["interviews"]), ("6", ["10–15%", "10-15%", "10–15", "10-15", "10 to 15%", "10 to 15"]), ("7", ["399"]), ("8", ["additional"])]
for n, a in G4C: K["w4c_%s" % n] = a
def gi(n, w=110): return '<sup>%s</sup>%s' % (n, inp("w4c_%s" % n, w))
web = ('<div class="webs"><div class="web" style="--c:#2f63b5"><div class="wh">▼ All Recruit</div>'
       '<div class="wr"><b>Speciality areas</b><span>advertising, marketing, sales</span></div><div class="wr"><b>offices</b><span>%s, Manchester</span></div>'
       '<div class="wr"><b>services</b><span>• online advertising<br>• recruitment for permanent and temporary roles<br>• %s-month guarantee on candidates<br>• background checks on candidates<br>• search of %s networking sites<br>• candidate %s with expert consultants</span></div>'
       '<div class="wr"><b>fees</b><span>• fee between %s of candidate’s first annual salary</span></div></div>'
       '<div class="web" style="--c:#b39a5a"><div class="wh">▼ Jones Recruitment</div>'
       '<div class="wr"><b>Speciality areas</b><span>advertising, marketing, media, sales, television</span></div><div class="wr"><b>offices</b><span>Brighton, Bristol, Belfast, Glasgow, Reading, Manchester</span></div>'
       '<div class="wr"><b>services</b><span>• online advertising<br>• recruitment for permanent and temporary roles<br>• %s-month guarantee on candidates<br>• background checks on candidates</span></div>'
       '<div class="wr"><b>fees</b><span>• fixed fee of £%s for <b>standard service</b> (the fee includes advertising and selection of CVs)<br>• %s fee for background checks</span></div></div></div>'
       % (gi("1"), gi("2", 70), gi("4"), gi("5"), gi("6", 90), gi("3", 70), gi("7", 70), gi("8")))
s8 = ('<div class="bsec">Listening</div><p class="ins"><b>C</b> Listen again and complete the gaps in the webpages.</p>' + player("a4c") + web +
      "".join(fb("w4c_%s" % n) for n, _ in G4C) + ctl("w4c"))
TF4 = [("Jones Recruitment have a wider range of speciality areas.", "T"), ("All Recruit has more offices than Jones Recruitment.", "F"), ("Jones Recruitment advertise temporary jobs.", "F"),
       ("The standard service at Jones Recruitment includes interviews with candidates.", "F"), ("All Recruit use people with special knowledge to interview candidates.", "T")]
# book key: 1 T 2 F 3 F 4 F 5 T
for i, (_, a) in enumerate(TF4): K["t4d_%d" % (i + 1)] = [a]
s9 = ('<div class="bsec">Listening</div><p class="ins"><b>D</b> Look at the webpages in Exercise 4C. Are the sentences <i>true</i> (T) or <i>false</i> (F)?</p>' +
      "".join('<div class="tf"><span class="q">%d. %s</span>%s%s</div>' % (i + 1, q, "".join('<label class="opt" style="display:inline;margin:0 10px 0 0"><input type="radio" name="t4d_%d" data-k="t4d_%d" value="%s"> %s</label>' % (i + 1, i + 1, x, x) for x in "TF"), fb("t4d_%d" % (i + 1)))
              for i, (q, a) in enumerate(TF4)) + ctl("t4d", "chkRad"))

# ---------- 5 Writing ----------
TAB_UP = ('<table class="tb"><tr><th colspan="3">TaskFlow — a simple task manager for small teams</th></tr>'
          '<tr><th>Plan</th><th>Price</th><th>The price includes</th></tr>'
          '<tr><td><b>Free</b></td><td>€0 (up to 3 users)</td><td rowspan="3">unlimited projects<br>Slack and Jira integration<br>support in a chat</td></tr>'
          '<tr><td><b>Pro</b></td><td>€8 per user per month<br>or €80 per user per year</td></tr>'
          '<tr><td><b>Business</b></td><td>fixed fee: €300 a month (up to 50 users)</td></tr>'
          '<tr><th colspan="3">Additional fees</th></tr>'
          '<tr><td colspan="3">extra storage over 100 GB: €5 a month · onboarding training (optional): €150 · <b>no cancellation fee</b> — cancel any time in two clicks</td></tr></table>')
QUP = [("What do you offer?", "We offer …"), ("Do you charge a fixed fee? What does the fee include?", "We charge … Our fixed fee includes …"), ("How much is the Pro plan? Is there an annual plan?", "We charge … You can also pay …"),
       ("What do you charge additional fees for?", "There is an additional fee for …"), ("Is there a cancellation fee? Are there any hidden fees?", "There is no … You can cancel …")]
MODEL_UP = ("TaskFlow is a simple task manager for small teams. We offer three plans: Free, Pro and Business.\n"
            "The Free plan is for up to three users. The Pro plan costs €8 per user per month. You can also pay €80 per user per year and save money.\n"
            "For bigger teams, we charge a fixed fee of €300 a month for up to 50 users. All plans include unlimited projects, Slack and Jira integration and support in a chat.\n"
            "There is an additional fee of €5 a month for extra storage over 100 GB. We also offer onboarding training for €150 — it is optional.\n"
            "There is no cancellation fee. You can cancel any time in two clicks. No hidden fees, no small print!")
s10 = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">5</b>Your team makes a small online tool. Write a short <b>pricing page</b> with <b>no hidden fees</b>. '
       'Use the information in the table to answer the questions. Write full sentences.</p>' + TAB_UP +
       "".join('<p class="ins"><span class="q">%d</span>%s <i style="color:%s">%s</i></p>' % (i + 1, q, DARK, h) for i, (q, h) in enumerate(QUP)) +
       ta("w5", "TaskFlow is … We offer …", 200) + '<p class="hint" id="w5c"></p>'
       '<button class="btn l" onclick="model(\'m5\')">Show a model answer</button><div class="model" id="m5">%s</div>' % MODEL_UP +
       '<div style="margin-top:20px">%s</div>' % (SELF % "I can explain the cost of a service. How well can you do this now?"))

TAB_CL = ('<table class="tb"><tr><th colspan="4">AP Couriers</th></tr><tr><th>Where they deliver</th><th>Services</th><th>Delivery / Fees (1 kg – 5 kg parcels) (includes collection and recorded delivery)</th><th>Additional fees</th></tr>'
          '<tr><td>Local / National</td><td>Parcels &amp; large / heavy items</td><td>Same day — all items £22<br>Next day — £10–20<br>2 days — from £3, 3–7 days — from £2<br>Daily courier service contracts (pay monthly or yearly)</td>'
          '<td>Contract agreements for daily courier service (administration)<br>Items over 5 kg<br>Cancellation of orders</td></tr></table>')
QCL = [("What types of delivery do you offer?", "We offer … We charge …"), ("Do you charge a fixed fee? What for? What does the fixed fee include?", "We charge … Our fixed fee …"),
       ("What fee do you charge for next-day delivery of items between 1 kg and 5 kg?", "We charge …"), ("Do you offer contracts? What for?", "We also offer …"), ("What do you charge additional fees for?", "There is …")]
MODEL_CL = ("We provide local and national delivery of parcels and large and/or heavy items.\nWe offer same-day or next-day delivery. We charge a £22 fixed fee for same-day delivery.\n"
            "We charge £10–20 for next-day delivery for items between 1 kg and 5 kg. Two-day delivery costs from £3 and 3–7-day delivery costs from £2.\n"
            "Our fixed fees include collection and recorded delivery. We also offer contracts for a daily courier service.\n"
            "We charge an administration fee for contract agreements. There is a cancellation fee for cancellation of orders. There is an additional fee for items over 5 kg.")
s10c = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">5</b>Write an advertisement for the services of a courier agency. Use the information in the table below to answer the questions. Write full sentences.</p>' + TAB_CL +
        "".join('<p class="ins"><span class="q">%d</span>%s <i style="color:%s">%s</i></p>' % (i + 1, q, DARK, h) for i, (q, h) in enumerate(QCL)) +
        ta("w5", "We provide …", 200) + '<p class="hint" id="w5c"></p>'
        '<button class="btn l" onclick="model(\'m5\')">Show a model answer</button><div class="model" id="m5">%s</div>' % MODEL_CL +
        '<div style="margin-top:20px">%s</div>' % (SELF % "I can explain the cost of a service. How well can you do this now?"))

CSS = r"""
document.head.insertAdjacentHTML("beforeend",`<style>
.vg a.vw{display:inline-block;background:ACC2;border-radius:12px;padding:2px 10px;margin:2px;font-size:14px;cursor:pointer;color:#231f20;text-decoration:none;border:1px solid transparent}
.vg a.vw:hover{border-color:ACC}.vg span:has(a){background:none;padding:0;margin:0}
.vcard{position:fixed;inset:0;background:rgba(30,40,60,.25);display:none;align-items:center;justify-content:center;z-index:50}.vcard.on{display:flex}
.vbox{background:#fff;border-radius:12px;max-width:460px;width:92%;padding:20px 24px;box-shadow:0 8px 30px rgba(0,0,0,.15);border-top:5px solid ACC}
.vbox .en{font-size:26px;font-weight:500}.vbox .uk{font-size:18px;color:DARK;margin:2px 0 10px}.vbox .lb{font-size:12px;font-weight:600;color:#8a8b8d;text-transform:uppercase;margin-top:10px}
.vbox ul{margin:4px 0;padding-left:18px}.vbox .ex{font-style:italic}.vbox .x{float:right;border:0;background:none;font-size:22px;cursor:pointer;color:#8a8b8d}
.vnav{display:flex;justify-content:space-between;margin-top:14px}
.stc{border:2px solid;border-radius:6px;margin:12px 0;background:#fff}.sth{padding:6px 12px;display:flex;gap:10px;align-items:center;flex-wrap:wrap}.sth .stt{font-family:Georgia,serif;font-style:italic}
.stc p{margin:8px 14px}.stc .nx{background:#f6f6f7;padding:6px 10px;border-radius:4px;font-size:15.5px}
.rdt{border:1px solid #d5d6d7;border-radius:8px;margin:14px 0;background:#fafafa}.rdh{background:#ff4500;color:#fff;padding:6px 12px;border-radius:8px 8px 0 0;font-weight:500;font-size:15px}
.rc{padding:6px 14px;border-bottom:1px solid #eee;font-size:15.5px}.rc .u{font-size:13px;color:#6d6e70}.rc p{margin:2px 0}
.spd{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0;align-items:center}.spd .sb{border:2px solid #c8c9cb;border-radius:8px;padding:10px 14px;line-height:2.2}.spd .sb.wide{grid-column:1/3}
.spd .sc{grid-column:1/3;justify-self:center;background:ACC2;color:DARK;font-weight:600;padding:6px 26px;border-radius:6px}
.aud{display:flex;flex-wrap:wrap;gap:10px;align-items:center;background:ACC2;padding:8px 12px;border-radius:6px;margin:8px 0}.aud .an{font-weight:600;color:DARK}.aud audio{height:36px}.aud .model{flex-basis:100%}
.webs{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:10px 0}.web{border:1px solid #d5d6d7;font-size:14.5px;line-height:1.9}.web .wh{background:var(--c);color:#fff;font-weight:600;padding:5px 10px}
.web .wr{display:grid;grid-template-columns:110px 1fr;border-top:1px solid #eee}.web .wr b{background:#f3f4f6;color:var(--c);padding:4px 8px;font-weight:600}.web .wr span{padding:4px 8px}.web input{width:100px}
table.tb{border-collapse:collapse;width:100%;margin:10px 0;font-size:15px}table.tb th,table.tb td{border:1px solid #c8c9cb;padding:6px 10px;vertical-align:top;text-align:left}table.tb th{background:#f3f4f6;font-weight:600}
@media(max-width:800px){.webs,.spd{grid-template-columns:1fr}.spd .sb.wide,.spd .sc{grid-column:1}}
</style>`);
"""
JS = r"""
const VI=__VI__;let vcur=0;
document.body.insertAdjacentHTML("beforeend",'<div class="vcard" id="vcard" onclick="if(event.target===this)vclose()"><div class="vbox" id="vbox"></div></div>');
function vshow(i){vcur=(i+VI.length)%VI.length;const v=VI[vcur];$("vbox").innerHTML=`<button class="x" onclick="vclose()">×</button><div class="en">${v.en} <button class="btn l" style="padding:2px 10px" onclick="say1(VI[${vcur}].en)">🔊</button></div><div class="uk">${v.uk}</div>`+
 `<div class="lb">Meaning</div><div>${v.df}</div><div class="lb">Collocations</div><ul>${v.co.map(c=>"<li>"+c+"</li>").join("")}</ul><div class="lb">Example</div><div class="ex">${v.ex} <button class="btn l" style="padding:1px 8px" onclick="say1(VI[${vcur}].ex)">🔊</button></div>`+
 `<div class="vnav"><button class="btn l" onclick="vshow(${vcur-1})">← prev</button><button class="btn l" onclick="vshow(${vcur+1})">next →</button></div>`;$("vcard").classList.add("on")}
function vclose(){$("vcard").classList.remove("on")}
document.addEventListener("keydown",e=>{if(!$("vcard").classList.contains("on"))return;if(e.key==="Escape")vclose();if(e.key==="ArrowRight")vshow(vcur+1);if(e.key==="ArrowLeft")vshow(vcur-1)});
document.querySelectorAll("a.vw").forEach(a=>a.onclick=e=>{e.preventDefault();vshow(+a.dataset.i)});
function say1(t){try{speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(t);u.lang="en-GB";u.rate=.9;const v=speechSynthesis.getVoices().find(x=>/^en/i.test(x.lang));if(v)u.voice=v;speechSynthesis.speak(u)}catch(e){}}
const SPT=["annual","hidden","cancellation","early termination","booking","administration","fixed"];
function chkSpider(){let n=0,t=0;const one=(k,ok)=>{const el=document.querySelector(`.g[data-k="${k}"]`);el.classList.remove("right","wrong");el.classList.add(ok?"right":"wrong");t++;if(ok)n++};
 one("sp_1",okv("sp_1",document.querySelector('.g[data-k="sp_1"]').value));
 const a=norm(document.querySelector('.g[data-k="sp_2"]').value),b=norm(document.querySelector('.g[data-k="sp_3"]').value);
 one("sp_2",(a==="pay"||a==="charge")&&a!==b);one("sp_3",(b==="pay"||b==="charge")&&a!==b);
 const seen=new Set();for(let i=1;i<=7;i++){const v=norm(document.querySelector(`.g[data-k="spt_${i}"]`).value);const ok=SPT.includes(v)&&!seen.has(v);if(ok)seen.add(v);one("spt_"+i,ok)}
 $("r_sp").textContent=n+" / "+t+(n===t?" ✓ Well done!":"");const f=$("fb_sp");f.className="fb show "+(n===t?"ok":"no");f.querySelector(".h").innerHTML=n===t?"✓":"Answers: 1 includes · 2 pay / charge · 3 annual, hidden, cancellation, early termination, booking, administration, fixed (any order)";save()}
function wc(){const t=document.querySelector('.g[data-k="w5"]');if(!t)return;const n=(t.value.trim().match(/\S+/g)||[]).length;$("w5c").textContent=n+" words (aim: 60–100)"}
document.addEventListener("input",e=>{if(e.target.dataset&&e.target.dataset.k==="w5")wc()});window.afterFill=wc;
"""
XJS = (CSS + JS.replace("__VI__", json.dumps(VITEMS, ensure_ascii=False))).replace("ACC2", ACC2).replace("ACC", ACC).replace("DARK", DARK)
OUT = "Learners can explain the cost of a service."
FOOT = "Stories based on: FTC v. Adobe (2024), &#65;CCC v. Microsoft (2025), FTC–Amazon settlement (2025). Audio 7.02: coursebook audioscript, AI voices. "
# keys of spidergram types for scoring (any order; checked in JS)
for i in range(7): K["spt_%d" % (i + 1)] = SP_TYPES

def build(sub, s_last, tag, key_suffix):
    secs = [("1", s1), ("2A–B", s2), ("2C", s3), ("3A", s4), ("3B", s5), ("3C", s6), ("4A–B", s7), ("4C", s8), ("4D", s9), ("5", s_last)]
    h = page("7.2", "Services and subscriptions", tag, OUT, "BP A2 7.2 Services · " + key_suffix, CODE, secs, K, VOC,
             acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, footer=FOOT, extra_js=XJS)
    d = os.path.join(ROOT, sub); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "lesson.html"), "w").write(h); print("ok", sub, len(h))

build("all", s10, "LESSON · UPDATED", "Lesson")
build("all-classic", s10c, "LESSON · CLASSIC", "Classic")
