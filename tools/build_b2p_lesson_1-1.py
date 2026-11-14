"""B2+ 1.1 Research in tech — in-class lesson page (mint theme).
Reuses the CSS of the A2+ 1.1 lesson page, recoloured.
Usage: python3 build_b2p_lesson_1-1.py ../lessons/1-1/all/lesson.html OUT.html
"""
import json, sys, re

SRC, OUT = sys.argv[1], sys.argv[2]
src = open(SRC).read()
css = src[src.index("<style>") + 7:src.index("</style>")]
MINT, MINT2 = "#2f9a74", "#dcf0e6"
css = (css.replace("--coral:#3fa9ad", "--coral:" + MINT)
          .replace("#e6f4f4", MINT2)
          .replace("linear-gradient(120deg,var(--pur),var(--mag))", "linear-gradient(120deg,#1f7d5c,#4fb58c)")
          .replace("#2a7fa8", "#1f6f8b"))
css += ".outc{display:flex;align-items:center;gap:14px;background:%s;margin:0;padding:10px 22px;font-size:15px}nav button{min-width:46px;font-size:17px}.outc b{background:%s;color:#fff;padding:4px 10px;border-radius:4px;font-weight:600;font-size:13px}" % (MINT2, MINT)
css += ".mine.q input{max-width:none}.tip{font-size:14px;color:#4d4d4f;background:#f6f5f1;border:1px solid #e3e1da;border-radius:4px;padding:8px 12px;margin:6px 0 14px}"

css += """
.vbox{max-width:980px;margin:12px auto 0;padding:0 22px}
.vbox details{border:1.5px solid var(--coral);border-radius:6px;background:#fff}
.vbox summary{cursor:pointer;padding:9px 14px;font-weight:600;color:var(--coral);list-style:none}
.vbox summary::-webkit-details-marker{display:none}
.vbox .in{padding:0 14px 12px}
.vbox h4{margin:10px 0 6px;font-weight:600;font-size:14px;color:#4d4d4f}
.vbox .vocab{margin-bottom:6px}
.vbox .vocab.g span{background:#fdf7e6}
.box{display:inline-flex;flex-wrap:wrap;gap:10px;border:1.5px solid #a7a9ac;padding:8px 14px;margin:4px 0 14px;font-size:16px}
.gap{font:inherit;font-size:16px;width:130px;padding:3px 6px;border:none;border-bottom:2px solid #a7a9ac;background:#fafafa;margin:0 3px}
.gap.ok,.sel.ok{border-color:var(--green);background:var(--gbg)}.gap.no,.sel.no{border-color:#d6322f;background:var(--rbg)}
ol.ex{padding-left:22px;margin:4px 0 10px;font-size:16.5px;line-height:1.9}
ol.ex li{padding-left:4px}
.tfx button,.opt button,.cls button{font:inherit;font-size:14px;border:1.5px solid #a7a9ac;background:#fff;border-radius:16px;padding:3px 12px;margin:0 3px 0 0;cursor:pointer}
.tfx button.ok,.opt button.ok,.cls button.ok{background:var(--green);border-color:var(--green);color:#fff}
.tfx button.no,.opt button.no,.cls button.no{background:#d6322f;border-color:#d6322f;color:#fff}
.fb{display:block;font-size:14.5px;color:#1f6f8b;font-style:italic;line-height:1.4;margin:2px 0 4px}
.match{display:grid;grid-template-columns:200px 1fr;gap:8px 14px;align-items:center;font-size:16px;max-width:900px}
.match b{font-weight:500}
.sel{font:inherit;font-size:15px;padding:5px 6px;border:1.5px solid #a7a9ac;border-radius:4px;max-width:100%;background:#fff}
.defs{columns:2;column-gap:28px;font-size:15px;line-height:1.45;margin:0 0 14px;padding:10px 14px;background:var(--lg)}
.defs div{break-inside:avoid;margin-bottom:5px}
.cls{display:grid;grid-template-columns:200px 1fr;gap:6px 14px;align-items:center;font-size:16px;max-width:760px}
.pt{font-size:15px;color:var(--grey);margin-left:8px}
textarea.list{font:inherit;font-size:16px;width:100%;max-width:640px;height:110px;padding:8px 10px;border:1px solid #c9cacc;border-radius:4px}
.sa{background:var(--lg);padding:12px 16px;border-left:5px solid var(--coral);font-size:15.5px;line-height:1.5;display:none;margin-top:10px}
.sa.show{display:block}
@media(max-width:700px){.match,.cls{grid-template-columns:1fr}.defs{columns:1}}
"""

VOC_BOOK = ["online surveys", "focus group", "customer satisfaction", "in-depth interviews", "desk research",
            "launch a product", "target audience", "sample size", "primary research", "secondary research"]
VOC_7 = ["quantitative", "qualitative", "product tester", "impact", "respondent", "gauge", "researcher",
         "gather", "viable", "data analysis"]
VOC_UP = ["A/B test", "churn rate", "user interview", "usability test", "insight", "synthesis", "NPS", "MVP"]

D = {
 "w": [
  "Why do you think companies need market research?",
  "Have you ever completed a market research survey — after a flight, a hotel stay, an app update? What was it about?",
  "What kind of information do companies try to get about their products and the people who use them?"],
 "wp": [
  "“If I had asked people what they wanted, they would have said faster horses.” Is user research overrated?",
  "Some teams now let AI summarise hundreds of user interviews in minutes. What could go wrong?",
  "A survey says 80% of users ‘love’ a new feature, but almost nobody uses it. How is that possible?",
  "Who should talk to users in a tech company: researchers, PMs, designers or engineers? Why?",
  "Data or gut feeling: what usually decides things in your team?"],
 "p": [
  ["Why do users cancel their subscription after the first month?", "In-depth user interviews — qualitative, primary. You need the ‘why’."],
  ["Which sign-up button gets more clicks: ‘Start free’ or ‘Get started’?", "A/B test — quantitative, primary."],
  ["How big is the market for project-management tools in Germany?", "Desk research: industry reports, statistics — secondary, quantitative."],
  ["Can new users set up their first project without help?", "Usability test: watch 5 users try — qualitative."],
  ["How satisfied are our 20,000 customers with support?", "Online survey with rating questions / NPS — quantitative."],
  ["What do competitors offer in their premium plans?", "Desk research: competitors’ websites, reviews — secondary."],
  ["Users leave 1-star reviews after the update. What exactly annoys them?", "Analyse the reviews (AI can group them by theme), then a few follow-up interviews."]],
 "bp": [
  ["showing two versions of a screen to different users to see which works better", "A/B test", "We ran an A/B test on the pricing page."],
  ["the percentage of users who stop using a product", "churn rate", "Our churn rate doubled after the price change."],
  ["a one-to-one conversation to understand a user’s problems", "user interview", "I did five user interviews this week."],
  ["watching users try to complete tasks with your product", "usability test", "The usability test showed nobody could find ‘Export’."],
  ["a deep understanding of why users behave in a certain way", "insight", "The key insight: people don’t trust auto-save."],
  ["combining findings from many interviews into key themes", "synthesis", "AI can speed up synthesis, but check the quotes."],
  ["a score showing how likely users are to recommend a product", "NPS (Net Promoter Score)", "Our NPS went from 20 to 35."],
  ["a simple first version built to test an idea", "MVP (minimum viable product)", "We tested the idea with an MVP in two weeks."]],
 "op": [
  ["___ research", "carry out / conduct / commission / outsource"],
  ["___ data", "gather / collect / analyse / interpret"],
  ["___ a survey", "design / run / send out / fill in / complete"],
  ["___ feedback", "get / collect / act on / ignore"],
  ["___ a product", "launch / test / roll out / pull"],
  ["___ the impact", "gauge / measure / assess"]],
 "pp": [
  ["You have one week and no budget. Find out why trial users don’t upgrade.", "Make a plan: method, sample, what you’ll ask, how you’ll report it."],
  ["Your CEO wants to launch in the US next quarter. What do you research first — and how?", ""],
  ["Analytics says users love feature X, but the sales team says clients hate it. How do you find out the truth?", ""],
  ["Your manager says: “Just ask ChatGPT what our users want.” Respond.", "Agree with part of it, then explain the limits."],
  ["A focus group of 8 people hated the new design. Should you cancel the launch?", "Think about sample size and who was in the group."]],
}

# Ex 4: true/false (statement, answer, correction)
TF = [
 ("Companies use market research for new products and services, and for existing ones too.", True, "Research helps launch new products and also improve existing ones: performance, communication, customer satisfaction."),
 ("The company that needs the research usually does it itself.", False, "Some companies have in-house research teams, others outsource projects to specialist companies."),
 ("Surveys, focus groups and in-depth interviews are ways of collecting new data from people.", True, "These are methods of primary research."),
 ("Companies use focus groups when they want information from a large number of people.", False, "Surveys reach large numbers of people. Focus groups bring together a small number of carefully selected people."),
 ("Some small businesses make their sample size bigger to make research cheaper.", False, "To make research more affordable, they reduce the sample size."),
 ("Both primary and secondary research help companies plan and build future strategy.", True, "The key is to plan carefully and keep research relevant, so the insights can shape strategy."),
]
# Ex 6A
GAPS = [
 ("These days most companies collect feedback through", "surveys.", "online"),
 ("", "groups are small, but they can help predict how target users will react.", "focus"),
 ("A rating pop-up in an app can tell you about the level of", "satisfaction.", "customer"),
 ("One method of primary research is to hold", "interviews with potential users.", "in-depth"),
 ("Secondary research is also called", "research because it uses data that already exists.", "desk"),
 ("Checking what competitors are doing is useful before you", "a product.", "launch"),
 ("Research helps you define your", "audience and decide how to communicate with them.", "target"),
 ("To make research cheaper, a start-up can reduce the", "size.", "sample"),
]
# Ex 6B
CLS = [("online surveys", "adjective + noun"), ("focus groups", "noun + noun"), ("customer satisfaction", "noun + noun"),
       ("in-depth interviews", "adjective + noun"), ("desk research", "noun + noun"), ("launch a product", "verb + noun"),
       ("target audience", "noun + noun"), ("sample size", "noun + noun")]
# Ex 7
DEFS = [
 ("a", "to measure how people feel about something, or the effect something is likely to have on them"),
 ("b", "realistic, and therefore likely to succeed"),
 ("c", "a person who tries something new to find out how well it works"),
 ("d", "a person whose job is to study a subject and find out new things about it"),
 ("e", "connected with how good something is, not how much or how many"),
 ("f", "the effect that an event or situation has on someone or something"),
 ("g", "connected with research whose results can be shown as numbers or percentages"),
 ("h", "a person who answers a set of questions, especially in a survey"),
 ("i", "examining information carefully in order to understand it better"),
 ("j", "to collect something over a period of time"),
]
MATCH = [("quantitative", "g"), ("product tester", "c"), ("impact", "f"), ("respondent", "h"), ("gauge", "a"),
         ("researcher", "d"), ("qualitative", "e"), ("gather", "j"), ("viable", "b"), ("data analysis", "i")]
# Ex 8
OPT = [
 ("<u>Qualitative research</u> gives you", ["lots of numbers about a product", "information about why people like or dislike a product"], 1, "."),
 ("<u>Primary research</u> means", ["collecting new data", "using data that already exists"], 0, "."),
 ("A company can measure <u>customer satisfaction</u> by", ["using research tools such as surveys and ratings", "building the product"], 0, "."),
 ("A <u>viable</u> product", ["has", "doesn’t have"], 0, " a good chance of success."),
 ("The <u>sample size</u> is the number of", ["questions", "people"], 1, " you need to get reliable information."),
 ("To <u>gauge</u> how users may react to a new feature, you can", ["watch their reactions to a prototype", "ask them if they have already bought it"], 0, "."),
]

def card(k, plus=False, reveal=False, label="Show answer", shuffle=True):
    pc = " pluscard" if plus else ""
    sh = '<button class="l" onclick="shuf(\'%s\')">Shuffle</button>' % k if shuffle else ""
    rv = '<button class="c" onclick="rev(\'%s\')">%s</button>' % (k, label) if reveal else ""
    return ('<div class="card%s"><span class="cnt" id="%sn"></span><div class="big" id="%sw" style="font-size:24px"></div>'
            '<div class="hint" id="%sh"></div><div class="ans" id="%sa"></div></div>'
            '<div class="ctrl"><button class="l" onclick="step(\'%s\',-1)">← Back</button>%s<button onclick="step(\'%s\',1)">Next →</button>%s</div>'
            % (pc, k, k, k, k, k, rv, k, sh))

def lvl(sid):
    return ('<div class="lvl"><button class="on" onclick="lv(\'%s\',0,this)">Base</button>'
            '<button class="p" onclick="lv(\'%s\',1,this)">★ Level up</button></div>' % (sid, sid))

chips = lambda xs, g="": '<div class="vocab%s">%s</div>' % (g, "".join("<span>%s</span>" % x for x in xs))

tf_html = '<ol class="ex">' + "".join(
    '<li>%s <span class="tfx" data-a="%s"><button onclick="tf(this,1)">T</button><button onclick="tf(this,0)">F</button></span><span class="fb"></span></li>'
    % (st, "1" if a else "0") for st, a, c in TF) + '</ol>'
gaps_html = '<ol class="ex">' + "".join(
    '<li>%s <input class="gap" data-a="%s" autocomplete="off"> <b>%s</b></li>' % (a, ans, b) for a, b, ans in GAPS) + '</ol>'
cls_html = '<div class="cls">' + "".join(
    '<b>%s</b><span class="opt" data-a="%s">%s</span>' % (w, t, "".join('<button onclick="pick(this)">%s</button>' % o for o in ["adjective + noun", "noun + noun", "verb + noun"]))
    for w, t in CLS) + '</div>'
defs_html = '<div class="defs">' + "".join('<div><b>%s</b> %s</div>' % (l, d) for l, d in DEFS) + '</div>'
opts = '<option value="">—</option>' + "".join('<option value="%s">%s</option>' % (l, l) for l, _ in DEFS)
match_html = '<div class="match">' + "".join(
    '<b>%d &nbsp;%s</b><select class="sel" data-a="%s">%s</select>' % (i + 1, w, a, opts) for i, (w, a) in enumerate(MATCH)) + '</div>'
opt_html = '<ol class="ex">' + "".join(
    '<li>%s <span class="opt" data-a="%s">%s</span>%s</li>' % (a, o[c], " ".join('<button onclick="pick(this)">%s</button>' % x for x in o), end)
    for a, o, c, end in OPT) + '</ol>'

body = '''
<header><div class="n">1.1</div><h1>Research in tech</h1><div class="t">LESSON</div></header>
<div class="outc"><b>Lesson outcome</b>You can use a range of vocabulary related to market and user research.</div>
<div class="vbox"><details open><summary>📖 Vocabulary of this lesson — click to hide / show</summary><div class="in">
 <h4>Collocations (Exercise 6)</h4>__V1__
 <h4>Words and phrases (Exercise 7)</h4>__V2__
 <h4>★ Level up: research words people use in tech</h4>__V3__
</div></details></div>
<a href="../../../index.html" style="display:inline-block;margin:12px 22px 0;color:var(--coral);font-weight:500;text-decoration:none;font-size:15px">← Contents</a>
<nav>__NAV__</nav>
<main>

<section id="s1" class="sec">
 __LVL1__
 <div class="base"><p class="ins"><b>1</b>Discuss these questions.</p>__C_w__</div>
 <div class="plus"><p class="ins"><b>1</b><span class="star">★</span>Discuss. Give reasons and examples from your work.</p>__CP_wp__</div>
</section>

<section id="s2" class="sec">
 <p class="ins"><b>2</b>You are going to watch a video about market research. How many ways can you think of for a company to collect information before it launches a new product? Make a list.</p>
 <textarea class="list" placeholder="online surveys&#10;…"></textarea>
 <div class="ctrl"><button class="c" onclick="sa('a2')">Show possible answers</button></div>
 <div class="sa" id="a2">Street or online surveys, focus groups, personal interviews, observation, field trials. In tech also: A/B tests, analytics, usability tests, social listening (reviews, Reddit), AI analysis of feedback.</div>
</section>

<section id="s3" class="sec">
 <p class="ins"><b>3</b>Watch the video 1.1.1. Were any of your ideas from Exercise 2 mentioned? Did you hear about any other ways for companies to collect information?</p>
 <div class="ctrl"><button class="c" onclick="sa('a3')">Show the main points</button></div>
 <div class="sa" id="a3"><b>Primary research</b> — gathering new data from customers: (online) surveys, focus groups, in-depth interviews.<br><b>Secondary research</b> (desk research) — data that already exists and is publicly available: government reports, company websites, academic publications.<br>Small businesses can save money with online surveys and a smaller sample size.</div>
</section>

<section id="s4" class="sec">
 <p class="ins"><b>4</b>Watch the video again and decide if these sentences are true (T) or false (F). Correct the false sentences.</p>
 __TF__
</section>

<section id="s5" class="sec">
 __LVL5__
 <div class="base"><p class="ins"><b>5</b>Discuss. Research is expensive — so why do companies still put money into it? What is better: primary research you design yourself, or secondary research you buy? Why?</p>
  <div class="phr"><span>I think companies invest in research because …</span><span>Primary research is more … but …</span><span>Secondary research is cheaper, although …</span><span>It depends on …</span></div></div>
 <div class="plus"><p class="ins"><b>5</b><span class="star">★</span>Which method would you choose for each research question? Is it primary or secondary, qualitative or quantitative? Explain, then check.</p>__CR_p__
  <div class="phr g" style="margin-top:12px"><span>I’d go for … because …</span><span>This is a qualitative / quantitative question.</span><span>We could carry out … with a sample of …</span><span>Desk research would be cheaper, but …</span></div></div>
</section>

<section id="s6" class="sec">
 <p class="ins"><b>6A</b>Complete the sentences with the words in the box to make collocations from the video.</p>
 <div class="box"><span>customer</span><span>desk</span><span>focus</span><span>in-depth</span><span>launch</span><span>online</span><span>sample</span><span>target</span></div>
 __GAPS__
 <div class="ctrl"><button class="c" onclick="chk('#s6 .gap')">Check</button><button class="l" onclick="showAns('#s6 .gap')">Show answers</button><span class="pt" id="s6pt"></span></div>
 <p class="ins" style="margin-top:26px"><b>B</b>Are the collocations in Exercise 6A adjective + noun, noun + noun or verb + noun?</p>
 __CLS__
</section>

<section id="s7" class="sec">
 __LVL7__
 <div class="base"><p class="ins"><b>7</b>Match the words and phrases (1–10) with the definitions (a–j).</p>
  __DEFS__ __MATCH__
  <div class="ctrl"><button class="c" onclick="chk('#s7 .sel')">Check</button><button class="l" onclick="showAns('#s7 .sel')">Show answers</button><span class="pt" id="s7pt"></span></div></div>
 <div class="plus"><p class="ins"><b>7</b><span class="star">★</span>Research words people use in tech. Read the explanation and say the word. Then tell a short story from your work where you use it.</p>__CPR_bp__</div>
</section>

<section id="s8" class="sec">
 __LVL8__
 <div class="base"><p class="ins"><b>8</b>Choose the best option to complete the explanations of the underlined words and phrases.</p>__OPT__</div>
 <div class="plus"><p class="ins"><b>8</b><span class="star">★</span>Which verbs go with it? Say as many as you can, then make a sentence about your work.</p>__CPR_op__</div>
</section>

<section id="s9" class="sec">
 __LVL9__
 <div class="base"><p class="ins"><b>9</b>Discuss. Is it important to do market research before launching a new product? What kind of information would a company need? Use vocabulary from Exercises 6A and 7.</p>
  __V12__</div>
 <div class="plus"><p class="ins"><b>9</b><span class="star">★</span>A real-life problem. Make a research plan in two minutes, then defend it. Your teacher plays a sceptical stakeholder.</p>__CP_pp__
  <div class="phr g" style="margin-top:12px"><span>Given the budget, I’d …</span><span>The risk is that …</span><span>That would give us a rough idea, but …</span><span>The sample is too small to …</span></div></div>
</section>

<section id="s10" class="sec">
 __LVL10__
 <div class="base">
  <p class="ins"><b>10A</b>PROJECT: How market research affects brands. Think of an everyday product or app you use. Choose two well-known brands for it and create a profile of each one.</p>
  <div class="chips"><span>Notion vs Obsidian</span><span>Duolingo vs Babbel</span><span>Spotify vs Apple Music</span><span>Revolut vs Monobank</span><span>Slack vs Microsoft Teams</span><span>Figma vs Canva</span></div>
  <div class="cats">
   <div><b>Attract</b>How does the brand attract customers? What does it offer them?</div>
   <div><b>Promise</b>What does the brand promise to do?</div>
   <div><b>Visibility</b>What makes it visible or memorable?</div>
   <div><b>Ideal customer</b>Who is the ideal customer for the brand?</div>
  </div>
  <p class="ins"><b>B</b>Come up with a new product or feature related to the original one. Write questions for a survey to find out what customers feel about it and what they would like.</p>
  <div class="tip">Mix question types: open, closed (yes/no), rating (1–10) and multiple-choice. Start general, then get more specific.</div>
  <div class="mine q"><input placeholder="1. …"><input placeholder="2. …"><input placeholder="3. …"><input placeholder="4. …"><input placeholder="5. …"><input placeholder="6. …"></div>
  <p class="ins" style="margin-top:18px"><b>C</b>Take turns playing the respondent and the researcher. Ask your teacher your questions and take notes; then answer your teacher’s questions.</p>
  <p class="ins"><b>D</b>Use the answers to create a brand profile for your new product. Present it to the respondent and get feedback: how well did you include their wishes and needs?</p>
  <div class="phr"><span>According to the survey, …</span><span>The respondent said / suggested that …</span><span>Based on the answers, we’ll …</span><span>We decided not to … because …</span></div>
 </div>
 <div class="plus">
  <p class="ins"><b>10</b><span class="star">★</span>Do 10A as in Base. Then, instead of a survey (10B–C), run a five-minute user interview with your teacher. Follow these rules.</p>
  <div class="cats g">
   <div><b>Their life, not your idea</b>Don’t pitch the feature. Ask how they do things now.</div>
   <div><b>The past, not the future</b>“Tell me about the last time you …” — not “Would you use …?”</div>
   <div><b>Listen more</b>Talk 20%, listen 80%. Ask “Why?” and “What happened next?”</div>
   <div><b>Compliments are not data</b>“Great idea!” tells you nothing. Ask what they actually did.</div>
  </div>
  <div class="phr g"><span>✗ Would you use an app that …?</span><span>✓ How do you … at the moment?</span><span>✗ Do you like our idea?</span><span>✓ What’s the hardest part about …?</span><span>✓ Is there anything else I should have asked?</span></div>
  <p class="ins">Then present your insights (10D) to a US stakeholder — your teacher. They will challenge you: “Five people? That’s not data.” Defend your findings.</p>
 </div>
</section>

<section id="s11" class="sec">
 <p class="ins"><b>Self-assessment</b> How well have you achieved the lesson outcome? 0 = I need more practice, 5 = I know this well.</p>
 <div class="score" id="score"><button onclick="sc(this)">0</button><button onclick="sc(this)">1</button><button onclick="sc(this)">2</button><button onclick="sc(this)">3</button><button onclick="sc(this)">4</button><button onclick="sc(this)">5</button></div>
 <p class="ins" style="margin-top:24px">My phrases: write 5 phrases from today you want to remember — the whole phrase, not one word: <i>gauge interest in a feature</i>, not <i>gauge</i>.</p>
 <div class="mine" id="mine"><input placeholder="1. …"><input placeholder="2. …"><input placeholder="3. …"><input placeholder="4. …"><input placeholder="5. …"></div>
 <div class="ctrl"><button class="c" onclick="copyMine()">Copy my phrases</button><span class="msg" id="cmsg"></span></div>
</section>
</main>
<footer style="max-width:980px;margin:0 auto;padding:0 22px 30px;font-size:12px;color:var(--grey)">Valentyna Hordiienko · Middle Learning Architect</footer>
'''

NAV = "".join('<button data-s="s%d"%s>%d</button>' % (i, ' class="on"' if i == 1 else "", i) for i in range(1, 11)) + '<button data-s="s11">✓</button>'
LABELS = {"op": "Show verbs", "p": "Show a suggestion"}
rep = {"__V1__": chips(VOC_BOOK), "__V2__": chips(VOC_7), "__V3__": chips(VOC_UP, " g"), "__V12__": chips(VOC_BOOK + VOC_7),
       "__NAV__": NAV, "__TF__": tf_html, "__GAPS__": gaps_html, "__CLS__": cls_html, "__DEFS__": defs_html,
       "__MATCH__": match_html, "__OPT__": opt_html}
for n in (1, 5, 7, 8, 9, 10):
    rep["__LVL%d__" % n] = lvl("s%d" % n)
for k, v in rep.items():
    body = body.replace(k, v)
def sub(m):
    f, k = m.group(1), m.group(2)
    return card(k, plus="P" in f, reveal="R" in f, label=LABELS.get(k, "Show answer"))
body = re.sub(r"__C(P?R?)_(\w+)__", sub, body)
assert "__" not in body.replace("___", ""), re.findall(r"__\w+__", body)

TFC = [c for _, _, c in TF]
js = r'''
const D=__D__, TFC=__TFC__;
const st={},ord={};for(const k in D){st[k]=0;ord[k]=D[k].map((_,i)=>i)}
const $=id=>document.getElementById(id);
const big=t=>'<span style="color:var(--ink);font-size:18px;font-weight:400">'+t+'</span>';
function render(k){const d=D[k][ord[k][st[k]]];$(k+"n").textContent=(st[k]+1)+" / "+D[k].length;const a=$(k+"a");a.classList.remove("show");const w=$(k+"w"),h=$(k+"h");
 if(k=="w"||k=="wp"){w.textContent=d;h.textContent=""}
 else if(k=="bp"){w.textContent=d[0];h.textContent="What’s the word?";a.innerHTML="<b>"+d[1]+"</b> — "+d[2]}
 else if(k=="op"){w.textContent=d[0];h.textContent="Which verbs can you use?";a.textContent=d[1]}
 else if(k=="p"){w.textContent=d[0];h.textContent="Which method would you choose?";a.textContent=d[1]}
 else if(k=="pp"){w.textContent=d[0];h.innerHTML=d[1]?big(d[1]):""}
}
function step(k,n){const L=D[k].length;st[k]=(st[k]+n+L)%L;render(k)}
function rev(k){$(k+"a").classList.toggle("show")}
function shuf(k){const a=ord[k];for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}st[k]=0;render(k)}
function lv(s,u,b){$(s).classList.toggle("up",!!u);b.parentNode.querySelectorAll("button").forEach(x=>x.classList.remove("on"));b.classList.add("on")}
function sa(id){$(id).classList.toggle("show")}
const norm=s=>s.trim().toLowerCase().replace(/[’']/g,"'").replace(/\s+/g," ");
function chk(q){let ok=0,all=0;document.querySelectorAll(q).forEach(e=>{all++;const r=norm(e.value)==norm(e.dataset.a);e.classList.toggle("ok",r);e.classList.toggle("no",!r&&e.value!=="");if(r)ok++});
 const sec=document.querySelector(q).closest("section");const pt=$(sec.id+"pt");if(pt)pt.textContent=ok+" / "+all}
function showAns(q){document.querySelectorAll(q).forEach(e=>{e.value=e.dataset.a;e.classList.add("ok");e.classList.remove("no")})}
function tf(b,v){const s=b.parentNode,li=s.parentNode,i=[...li.parentNode.children].indexOf(li),r=String(v)==s.dataset.a;
 s.querySelectorAll("button").forEach(x=>x.className="");b.className=r?"ok":"no";li.querySelector(".fb").textContent=r?(s.dataset.a=="0"?"✓ False. "+TFC[i]:"✓ True. "+TFC[i]):"Not quite — listen again."}
function pick(b){const s=b.parentNode,r=b.textContent==s.dataset.a;s.querySelectorAll("button").forEach(x=>x.className="");b.className=r?"ok":"no"}
function copyMine(){const t=[...document.querySelectorAll("#mine input")].map(x=>x.value.trim()).filter(Boolean).join("\n");if(!t){cmsg.textContent="Write your phrases first.";return}
 try{navigator.clipboard.writeText(t).then(()=>cmsg.textContent="Copied!",()=>cmsg.textContent="Select the text and copy it manually.")}catch(e){cmsg.textContent="Select the text and copy it manually."}}
function sc(b){document.querySelectorAll("#score button").forEach(x=>x.classList.remove("on"));b.classList.add("on")}
document.querySelectorAll("nav button").forEach(b=>b.onclick=()=>{document.querySelectorAll("nav button,.sec").forEach(x=>x.classList.remove("on"));b.classList.add("on");$(b.dataset.s).classList.add("on")});
$("s1").classList.add("on");for(const k in D)render(k);
'''.replace("__D__", json.dumps(D, ensure_ascii=False)).replace("__TFC__", json.dumps(TFC, ensure_ascii=False))

html = ('<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<title>1.1 Research in tech — Lesson</title>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">\n'
        '<style>' + css + '</style></head><body>' + body + '<script>' + js + '</script></body></html>')
open(OUT, "w").write(html)
print("ok", len(html))
