"""General English B2/B2+ · Pet peeves: things that drive us up the wall — LESSON with Supabase sync.
Usage: python3 build_ge_peeves.py OUT.html [STUDENT_CODE]
"""
import sys, os, json
from bp_page import page, fb, sel, inp, ta, ctl, radios, SELF
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GRAD2 = "#c2416b", "#fbe7ee", "#9e2d55", "#ef7fa0"
VID = {"voa": ("b8SygfyQqM4", "VOA Learning English · English in a Minute: Pet Peeve", "1 min · reel", True),
       "cut": ("sAvIKc3dxug", "Cut · 100 People Tell Us Their Pet Peeves", "3:40", False),
       "spk": ("qH0uQK9mxg4", "Petty Misdemeanors · The Person Who Uses Speakerphone in Public (2026)", "6:53", False),
       "bbc": ("3R3uTv1xJT0", "BBC Learning English · How to complain politely", "1 min · reel", True),
       "rank": ("PgjKy6TNUjU", "scribblejuice & KelseyAnimated · Ranking ANNOYING Pet Peeves (2026)", "15:43", False)}
def video(k):
    y, t, d, short = VID[k]
    cls = "vbox short" if short else "vbox"
    return ('<div class="%s"><div class="vt"><span class="vn">▶</span> %s <span class="vd">%s</span> <a href="https://www.youtube.com/watch?v=%s" target="_blank">open on YouTube</a></div>'
            '<div class="fr"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0&cc_load_policy=1" allowfullscreen loading="lazy"></iframe></div></div>') % (cls, t, d, y, y)
def show(id_, label, body): return '<button class="btn l" onclick="model(\'%s\')" style="margin-top:6px">%s</button><div class="model" id="%s">%s</div>' % (id_, label, id_, body)
K = {}

# 1 Lead-in -------------------------------------------------------------
METER = ["Someone plays a TikTok out loud on the bus.", "A colleague says ‘Let’s circle back on this’ and never does.", "People who send five voice messages instead of one text.",
         "Someone stops dead at the top of the escalator.", "‘Reply all’ to a 200-person email.", "A friend is always ‘five minutes away’ (they haven’t left home).",
         "People who walk slowly, three in a row, on a narrow pavement.", "Someone eats crisps loudly in a quiet office.", "A ‘quick call’ that lasts an hour.",
         "Being left on ‘read’ for two days.", "People who reply ‘K.’", "Someone puts an empty milk carton back in the fridge."]
GUESS = [("Not cleaning up after your dog", "97"), ("Littering", "96"), ("Coughing or sneezing without covering your mouth", "88"),
         ("Playing music or videos out loud on a phone", "79"), ("Slow walking — 18–24-year-olds", "65"), ("Slow walking — over-65s", "17")]
s1 = ('<div class="bsec">Lead-in</div><p class="ins"><b class="x">1</b><b>A</b> Watch the reel. What is a <i>pet peeve</i>? Write your own definition.</p>' + video("voa") +
      ta("l1a", "A pet peeve is …", 50) + show("m1a", "Show answer", "A <b>pet peeve</b> (AmE) / <b>pet hate</b> (BrE) is a small, everyday thing that annoys you personally, much more than it probably should — and often more than it annoys other people.") +
      '<p class="ins" style="margin-top:24px"><b>B</b> The Annoy-o-meter 😤 How much do these situations annoy you? 0 = I don’t care, 5 = it makes my blood boil.</p>' +
      "".join('<div class="mrow"><span>%d. %s</span><input type="range" min="0" max="5" value="0" class="g meter" data-k="m1_%d"><b class="mv">0</b></div>' % (i + 1, s, i + 1) for i, s in enumerate(METER)) +
      '<p class="ins"><b>C</b> Tell your teacher about your top three. Why do they annoy you so much? Is anything missing from the list?</p>' + ta("l1c", "My top three: …\nMissing from the list: …", 70) +
      '<p class="ins" style="margin-top:24px"><b>D</b> In April 2025, YouGov asked Britons which public nuisances bother them. Guess the percentage of people who are bothered.</p>' +
      "".join('<div class="row"><span style="display:inline-block;min-width:430px">%s</span>%s %%</div>' % (t, inp("gu_%d" % (i + 1), 70, "?")) for i, (t, a) in enumerate(GUESS)) +
      show("m1d", "Show the real numbers", "".join('%s — <b>%s%%</b><br>' % (t, a) for t, a in GUESS) + '<span class="hint">Source: YouGov, 28 April 2025, ‘Littering, loudspeakers and Lime bikes: what public nuisances bother Britons most’.</span>'))


# Full list of pet peeves in the Cut video (in order, with time codes; English only)
ALLPP = [("0:00", ["people who don’t wash their hands after using the toilet (⚠️ rude jokes 0:00–0:20)"]),
 ("0:22", ["snoring", "nose picking", "people touching my face", "uncleanliness", "singing a song when you don’t know the words", "chewing loudly with your mouth open"]),
 ("0:46", ["cutting in line at a coffee shop", "a soaking-wet bathroom floor after someone’s shower"]),
 ("0:55", ["the smell of lots of different foods cooking at the same time", "clothes hangers on the floor", "wasting time"]),
 ("1:02", ["sniffling", "whistling", "chewing gum / popping gum", "slurping", "people who complain about every little thing", "people who flake out on you (cancel plans)",
           "people who complain about things they do all the time", "dirty fingernails", "licking your fingers", "leaving only one thing in the packet", "snails on the pavement that you might step on"]),
 ("1:30", ["someone using the toilet stall right next to you when all the others are free", "not flushing the toilet", "leaving the cap off the toothpaste", "not washing your hands before you eat",
           "people who ask you a question and then interrupt", "people who brag", "flaky people", "not knocking before coming in", "lots of cat hair on your clothes", "farting in public", "loud people"]),
 ("2:00", ["very loud music in the car when I’m trying to talk", "loud noises", "people who stop in the middle of the pavement", "drivers who brake on the motorway when there’s no traffic",
           "cyclists who don’t signal", "drivers who don’t use their indicator", "squeaky brakes", "people who comment on everything during a film", "talking during films",
           "flossing your teeth in public", "people rolling their eyes at me", "friend requests from strangers on Facebook", "leaving DVDs out of their case", "customers asking ‘What size do you think I wear?’ (a shop assistant)"]),
 ("2:40", ["shaking your leg under the table", "people pointing out that I’m sweaty", "holding a drink while dancing", "being told to do something more than once", "ignorant people", "rude people",
           "lying", "talking too much", "not respecting personal space / walking too close to me", "children touching me"]),
 ("3:15", ["people who overreact", "people staring at me at the gym", "people who can’t do their job", "people who ask too many questions", "not keeping to the right on the escalator", "people who cut me off (in traffic)"])]
def _ts(t):
    m, s_ = t.split(":"); return int(m) * 60 + int(s_)
ALL_HTML = ('<details class="ad" style="margin-top:14px"><summary>📋 All the pet peeves in the video (%d) — open after you check</summary>' % sum(len(x) for _, x in ALLPP) +
            "".join('<p style="margin:10px 0 2px"><a href="https://www.youtube.com/watch?v=sAvIKc3dxug&t=%ds" target="_blank" style="font-weight:600;color:#9e2d55;text-decoration:none">▶ %s</a></p><ul style="margin:0 0 6px;padding-left:22px">%s</ul>'
                    % (_ts(t), t, "".join("<li>%s</li>" % x for x in xs)) for t, xs in ALLPP) +
            '<p class="hint">Auto-captions are unclear in a couple of places, so a few short phrases are not in the list.</p></details>')

# 2 Video 1 -------------------------------------------------------------
HEARD = [("people who cut in line at a coffee shop", True), ("leaving the cap off the toothpaste", True), ("people who flake out on you (cancel plans)", True),
         ("people who ask a question and then interrupt you", True), ("people who brag", True), ("not knocking before coming in", True),
         ("people talking during movies", True), ("drivers who don’t use their indicator (blinker)", True), ("leaving only one thing in the packet", True),
         ("someone using the toilet stall right next to you when all the others are free", True), ("shaking your leg under the table", True),
         ("people who complain about things they do themselves", True), ("people who overreact", True), ("chewing with your mouth open", True),
         ("people who reply ‘K.’", False), ("voice messages", False), ("people who are always late", False), ("loud typing", False), ("people on speakerphone", False), ("slow Wi-Fi", False)]
for i, (t, h) in enumerate(HEARD): K["h2_%d" % (i + 1)] = ["yes" if h else "no"]
s2 = ('<div class="bsec" style="color:#c2185b">VIDEO</div><p class="ins"><b class="x">2</b><b>A</b> Watch 100 people talk about their pet peeves. It’s fast! Which of these do you hear? Choose ✓ or ✗.</p>'
      '<p class="hint">⚠️ Real people, real language — a few rude words about the bathroom at the beginning.</p>' + video("cut") +
      '<div class="two">' + "".join('<div class="row">%d. %s %s%s</div>' % (i + 1, t, sel("h2_%d" % (i + 1), ["yes", "no"], 70), fb("h2_%d" % (i + 1))) for i, (t, h) in enumerate(HEARD)) + '</div>' + ctl("h2") +
      ALL_HTML +
      '<p class="ins" style="margin-top:24px"><b>B</b> Which pet peeves in the video are fair, and which are just <i>petty</i>? Which one do you secretly do yourself? 🙈</p>' + ta("v2b", "Fair: … / Petty: … / I’m guilty of …", 80))

# 3 Vocabulary ----------------------------------------------------------
LEVELS = ["😐 mild", "😠 strong", "🤬 explosive"]
SCALE = [("It bugs me.", 0), ("It gets on my nerves.", 0), ("It irritates me a bit.", 0), ("It winds me up. (BrE)", 1), ("I can’t stand it.", 1), ("It really grates on me.", 1),
         ("I find it infuriating.", 1), ("It drives me up the wall.", 2), ("It does my head in. (BrE)", 2), ("It makes my blood boil.", 2), ("I’ve had it up to here with …", 2), ("It drives me absolutely mad.", 2)]
for i, (p, l) in enumerate(SCALE): K["sc_%d" % (i + 1)] = [LEVELS[l]]
IDI = [("my pet peeve / my pet hate", "the small thing that annoys me most"), ("it grinds my gears", "it really annoys me (informal, jokey)"), ("it rubs me the wrong way", "it annoys me, often without a clear reason"),
       ("the last straw", "the final annoying thing that makes you lose patience"), ("a bugbear", "a problem that keeps annoying you"), ("petty", "too worried about small, unimportant things"),
       ("inconsiderate", "not thinking about other people’s feelings or needs"), ("oblivious", "not noticing what is happening around you"), ("passive-aggressive", "showing anger indirectly, e.g. with a ‘polite’ note"),
       ("the ick", "a sudden feeling of disgust about someone (Gen Z slang)")]
for i, (w, d) in enumerate(IDI): K["id_%d" % (i + 1)] = [d]
s3 = ('<div class="bsec">Vocabulary <span class="sub">From ‘it bugs me’ to ‘my blood boils’</span></div>'
      '<p class="ins"><b class="x">3</b><b>A</b> How strong is it? Put each expression on the Annoy-o-meter.</p>' +
      '<div class="two">' + "".join('<div class="row"><span style="display:inline-block;min-width:240px">%s</span>%s%s</div>' % (p, sel("sc_%d" % (i + 1), LEVELS, 140), fb("sc_%d" % (i + 1))) for i, (p, l) in enumerate(SCALE)) + '</div>' + ctl("sc") +
      '<div class="gbox"><div class="gh">Watch the grammar!</div><p><b>It</b> drives me mad <b>when</b> people … · <b>People who</b> … drive me up the wall. · I can’t stand / can’t bear <b>+ -ing</b>: <i>I can’t stand waiting.</i> · I’m fed up <b>with + -ing</b> · It gets <b>on</b> my nerves · I’ve had it up to here <b>with</b> …</p></div>' +
      '<p class="ins" style="margin-top:24px"><b>B</b> Match the words and idioms with their meanings.</p>' +
      "".join('<div class="row"><b style="display:inline-block;min-width:230px;font-weight:500">%s</b>%s%s</div>' % (w, sel("id_%d" % (i + 1), sorted(d for _, d in IDI), 420), fb("id_%d" % (i + 1))) for i, (w, d) in enumerate(IDI)) + ctl("id") +
      '<p class="ins" style="margin-top:24px"><b>C</b> Use four expressions from 3A and 3B to talk about your own pet peeves.</p>' + ta("v3c", "It really grates on me when … / My biggest bugbear is …", 90))

# 4 Grammar -------------------------------------------------------------
G4 = [("My flatmate / always / leave / wet towels on the floor.", "My flatmate is always leaving wet towels on the floor.|My flatmate's always leaving wet towels on the floor.", "always + Present Continuous"),
      ("My colleague / keep / interrupt / me in meetings.", "My colleague keeps interrupting me in meetings.", "keep + -ing"),
      ("I wish / people / stop / playing videos out loud on the bus.", "I wish people would stop playing videos out loud on the bus.", "I wish + would"),
      ("What / really / annoy / me / is / people / reply ‘K.’", "What really annoys me is when people reply 'K.'|What really annoys me is people who reply 'K.'|What really annoys me is when people reply K.|What really annoys me is people replying 'K.'", "cleft: What … is"),
      ("He / constantly / check / his phone when we’re talking.", "He's constantly checking his phone when we're talking.|He is constantly checking his phone when we're talking.", "constantly + Present Continuous"),
      ("The thing that / drive / me mad / is / people who are always ‘five minutes away’.", "The thing that drives me mad is people who are always 'five minutes away'.|The thing that drives me mad is people who are always five minutes away.", "cleft: The thing that … is"),
      ("I wish / my neighbour / not / play / drums at midnight.", "I wish my neighbour wouldn't play drums at midnight.|I wish my neighbour would not play drums at midnight.|I wish my neighbour would stop playing drums at midnight.", "I wish + wouldn't"),
      ("She / will / leave / her dishes in the sink for days! (typical habit)", "She will leave her dishes in the sink for days!|She'll leave her dishes in the sink for days!", "will = annoying typical habit")]
for i, (q, a, n) in enumerate(G4): K["g4_%d" % (i + 1)] = a.split("|")
s4 = ('<div class="bsec">Grammar <span class="sub">Complaining about annoying habits</span></div>'
      '<div class="gbox"><div class="gh">Five ways to sound really annoyed</div><table class="gt">'
      '<tr><td><b>always / constantly / forever + Present Continuous</b></td><td>He’s <b>always leaving</b> his socks on the sofa. (= again and again, and it annoys me)</td></tr>'
      '<tr><td><b>keep (on) + -ing</b></td><td>She <b>keeps sending</b> me voice messages.</td></tr>'
      '<tr><td><b>will / would</b> (stressed) for typical habits</td><td>He <b>WILL</b> talk during films! · My ex <b>would</b> always be late.</td></tr>'
      '<tr><td><b>I wish + would / wouldn’t</b></td><td>I <b>wish</b> people <b>would</b> let others off the train first. · I wish he <b>wouldn’t</b> chew so loudly.</td></tr>'
      '<tr><td><b>Cleft sentences</b> (to emphasise)</td><td><b>What</b> really gets me <b>is</b> when people … · <b>The thing that</b> drives me mad <b>is</b> … · <b>It’s not</b> the noise <b>that</b> bothers me, <b>it’s</b> …</td></tr></table>'
      '<p style="color:#6d6e70">⚠️ <i>I wish he would …</i> = I want another person to change. Not about yourself: <s>I wish I would</s> → <i>I wish I could / I wish I didn’t …</i></p></div>'
      '<p class="ins"><b class="x">4</b><b>A</b> Make full sentences. Use the structure in brackets.</p>' +
      "".join('<div class="row">%d. %s <span class="hint">(%s)</span><br>→ %s%s</div>' % (i + 1, q, n, inp("g4_%d" % (i + 1), 560), fb("g4_%d" % (i + 1))) for i, (q, a, n) in enumerate(G4)) + ctl("g4") +
      '<p class="ins" style="margin-top:24px"><b>B</b> Your turn! Write three sentences about people you know (no names 😉) — use three different structures.</p>' + ta("g4b", "My … is always …\nI wish …\nWhat really gets me is …", 90))

# 5 Video 2 -------------------------------------------------------------
Q5 = [("When, according to the narrator, does speakerphone make perfect sense?", "At home / in private, when your hands are busy (cooking, folding laundry)."),
      ("Why is it ‘no longer eavesdropping’ when someone uses speakerphone in public?", "Eavesdropping takes effort; here the information ‘finds you’ — you hear both people without trying."),
      ("What is the ‘acoustic arms race’?", "The caller speaks louder because the room is noisy, the phone gets louder, and then other people in the room start speaking louder too."),
      ("Why can’t you simply ask the person to turn it down?", "You would become part of a conversation you’re trying hard not to join (and you can’t always move away or use headphones)."),
      ("Why is the person on the other end of the call ‘the most complicated participant’?", "They often don’t know they’re on speaker, so they share private things that are broadcast to strangers."),
      ("What exceptions does the narrator accept?", "Busy hands, accessibility features, urgent calls, a broken earpiece, someone else needs to hear, a 10-second call in an empty space."),
      ("What is the ‘strangest rule’ of all?", "The audience must listen but is not allowed to take part (you can’t turn around and give your opinion)."),
      ("What simple ‘policy’ does the narrator suggest?", "In shared indoor spaces, for longer calls: hold the phone normally, use headphones, step outside or find a quiet corner.")]
W5 = [("eavesdrop", "listen secretly to other people’s conversation"), ("overhear", "hear something by accident"), ("etiquette", "the rules of polite behaviour"),
      ("a misdemeanour", "a small crime / a minor bad act (here: as a joke)"), ("a shared space", "a place used by many people at the same time"), ("broadcast", "send out to a large audience, like radio"),
      ("an arms race", "a competition where each side keeps making things bigger or louder"), ("a reasonable exception", "a fair situation when the rule doesn’t apply")]
for i, (w, d) in enumerate(W5): K["w5_%d" % (i + 1)] = [d]
s5 = ('<div class="bsec" style="color:#c2185b">VIDEO</div><p class="ins"><b class="x">5</b><b>A</b> Watch a funny ‘investigation’ into one modern pet peeve: speakerphone in public. Answer the questions.</p>' + video("spk") +
      "".join('<p class="ins"><span class="q">%d</span>%s</p>%s%s' % (i + 1, q, ta("q5_%d" % (i + 1), "", 44), show("m5_%d" % (i + 1), "Show answer", a)) for i, (q, a) in enumerate(Q5)) +
      '<p class="ins" style="margin-top:24px"><b>B</b> Match the words from the video with their meanings.</p>' +
      "".join('<div class="row"><b style="display:inline-block;min-width:200px;font-weight:500">%s</b>%s%s</div>' % (w, sel("w5_%d" % (i + 1), sorted(d for _, d in W5), 420), fb("w5_%d" % (i + 1))) for i, (w, d) in enumerate(W5)) + ctl("w5") +
      '<p class="ins" style="margin-top:24px"><b>C</b> Do you agree with the narrator’s ‘policy’? Has this ever happened to you? What did you do?</p>' + ta("v5c", "", 70))

# 6 Saying it nicely ----------------------------------------------------
STY = ["🙂 diplomatic", "😬 passive-aggressive", "😡 too direct"]
P6 = [("I don’t know if you’ve noticed, but your music is quite loud.", 0), ("Per my last email…", 1), ("Turn that off. Now.", 2), ("This might sound a bit petty, but could you not eat at your desk during calls?", 0),
      ("Just a gentle reminder that the dishwasher doesn’t empty itself 🙂", 1), ("Would you mind using headphones? I’m trying to concentrate.", 0), ("Can you, like, stop?", 2),
      ("It’s probably just me, but I find it hard to focus when the door is open.", 0), ("As previously mentioned…", 1), ("Wow. Nice of you to finally reply.", 1), ("You’re so annoying.", 2), ("I was wondering if we could talk about the noise in the evenings.", 0)]
for i, (p, s) in enumerate(P6): K["st_%d" % (i + 1)] = [STY[s]]
R6 = [("Stop leaving your dishes in the sink!", "I don’t know if you’ve noticed, but the dishes have been in the sink since Monday. Could we take turns washing up?"),
      ("You’re always late. It’s so rude.", "This might sound a bit petty, but could you message me if you’re running late? I end up waiting for ages."),
      ("Your speakerphone is driving everyone mad.", "Sorry to bother you — would you mind taking the call off speaker? It’s a bit loud in here."),
      ("Why do you keep sending me voice messages?!", "It’s probably just me, but I find texts easier to read at work. Could you write instead of sending voice notes?")]
s6 = ('<div class="bsec">Functional language <span class="sub">Saying it nicely (or not)</span></div>'
      '<p class="ins"><b class="x">6</b><b>A</b> Watch the reel. Which phrases can you use to complain politely?</p>' + video("bbc") + ta("b6a", "", 50) +
      show("m6a", "Show answer", "I’d like to complain. · I’m (really) unhappy about + noun · It’s unacceptable that + clause · Don’t lose your temper!") +
      '<p class="ins" style="margin-top:24px"><b>B</b> Diplomatic, passive-aggressive or too direct? Choose.</p>' +
      "".join('<div class="row"><span style="display:inline-block;min-width:520px">%d. %s</span>%s%s</div>' % (i + 1, p, sel("st_%d" % (i + 1), STY, 200), fb("st_%d" % (i + 1))) for i, (p, s) in enumerate(P6)) + ctl("st") +
      '<div class="gbox"><div class="gh">Softeners for a difficult conversation</div><p>I don’t know if you’ve noticed, but … · This might sound a bit petty, but … · It’s probably just me, but … · No big deal, but … · Would you mind (not) + -ing …? · I was wondering if you could … · Could we maybe …? · I’d really appreciate it if you could …</p></div>'
      '<p class="ins"><b>C</b> Rewrite these complaints so that they sound diplomatic.</p>' +
      "".join('<div class="row">%d. <i>%s</i><br>%s%s</div>' % (i + 1, r, inp("r6_%d" % (i + 1), 620, "→ …"), show("m6r_%d" % (i + 1), "Possible answer", m)) for i, (r, m) in enumerate(R6)))

# 7 Speaking ------------------------------------------------------------
TIERS = ["S — unbearable", "A — very annoying", "B — mildly annoying", "C — I don’t care"]
TL = ["Loud chewing", "Speakerphone in public", "Voice messages", "‘Reply all’", "People who are always late", "Slow walkers", "Being left on read", "Kicking the back of your seat on a plane",
      "Someone saying ‘Let’s take this offline’", "People who say ‘no offence, but…’", "Spoilers", "Small talk in the lift"]
ROLES = [("🏠 Flatmate", "Your flatmate keeps using your oat milk and putting the empty carton back in the fridge. Talk to them — stay friendly, but get a result."),
         ("💻 Colleague", "A colleague in the open-plan office takes long calls on speaker and eats crisps during your meetings. Raise it politely."),
         ("☕ Stranger", "In a café, the person at the next table has been on speakerphone for 15 minutes. You need to work. What do you say?"),
         ("💬 Friend", "Your best friend is always ‘five minutes away’ and is usually 30 minutes late. Tell them how you feel without starting a fight.")]
s7 = ('<div class="bsec">Speaking</div><p class="ins"><b class="x">7</b><b>A</b> Pet Peeve Tier List! Put each thing into a tier. Then explain your choices using the language from Exercises 3 and 4.</p>' +
      '<div class="two">' + "".join('<div class="row"><span style="display:inline-block;min-width:250px">%s</span>%s</div>' % (t, sel("t7_%d" % (i + 1), TIERS, 180)) for i, t in enumerate(TL)) + '</div>' +
      '<div id="tierview" class="tierv"></div>' +
      '<p class="hint">💡 Want more? Watch two animators argue about their tier list (start at the beginning, 5–10 minutes is enough):</p>' + video("rank") +
      '<p class="ins" style="margin-top:24px"><b>B</b> Role-play. Choose a situation. Your teacher is the annoying person. Use softeners from Exercise 6 — and don’t lose your temper!</p>' +
      '<div class="two">' + "".join('<div class="card"><b>%s</b><br>%s</div>' % r for r in ROLES) + '</div>' + ta("r7", "Phrases I used / want to use next time …", 70))

# 8 Writing -------------------------------------------------------------
MODEL8 = ("r/PetPeeves · Posted by u/quietcarriage\n\nPeople who take speakerphone calls in shared spaces 📢\n\n"
          "Can we talk about this? What really gets me is people who put their phone on speaker in a café and then act as if the conversation is private. "
          "Yesterday a guy next to me was constantly discussing his cousin’s divorce, at full volume, for twenty minutes. I wasn’t eavesdropping — I literally had no choice. "
          "I can cope with loud music, but this drives me up the wall, because you can’t even politely ignore it. I wish people would just use headphones or step outside. "
          "Is it just me, or is this the most inconsiderate habit of the 2020s?\n\nEdit: Yes, I know it’s petty. I still stand by it. 😅")
s8 = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">8</b>Write a post for the subreddit r/PetPeeves about one of your pet peeves (120–150 words). '
      'Describe the situation, explain why it annoys you and say what you wish people would do instead. Use at least <b>five expressions</b> from Exercise 3 and <b>two structures</b> from Exercise 4.</p>' +
      '<div class="rd"><div class="rdh">r/PetPeeves · Create post</div>' + inp("w8t", 640, "Title: People who …") + ta("w8", "Can we talk about this? What really gets me is …", 220) + '</div>' +
      '<div class="res" id="wc8"></div><div class="chk2" id="chk8"></div>' + show("m8", "Show model post", MODEL8) +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you talk about things that annoy you and complain politely?"))

VOC = [("How annoyed are you?", [("it bugs me", "мене це дратує"), ("it gets on my nerves", "це діє мені на нерви"), ("it winds me up", "мене це заводить"), ("I can’t stand", "терпіти не можу"),
         ("it grates on me", "мене це коробить"), ("infuriating", "шалено дратівливий"), ("it drives me up the wall", "це доводить до сказу"), ("it does my head in", "мене це вибішує"),
         ("it makes my blood boil", "аж кров закипає"), ("I’ve had it up to here with", "з мене досить"), ("I’m fed up with", "мені набридло")]),
       ("Idioms & adjectives", [("my pet peeve / pet hate", "те, що мене особливо дратує"), ("it grinds my gears", "мене це бісить"), ("it rubs me the wrong way", "мені це якось не подобається"),
         ("the last straw", "остання крапля"), ("a bugbear", "постійне подразнення"), ("petty", "дріб’язковий"), ("inconsiderate", "неуважний до інших"), ("oblivious", "що нічого не помічає"),
         ("passive-aggressive", "пасивно-агресивний"), ("the ick", "відраза, «фу»")]),
       ("Grammar", [("He’s always + -ing", "він вічно …"), ("keep + -ing", "постійно щось робити"), ("He WILL …", "він обов’язково (знову) …"), ("I wish people would …", "хотілося б, щоб люди …"),
         ("What really gets me is …", "що мене найбільше бісить, так це …"), ("The thing that drives me mad is …", "найбільше мене дратує …")]),
       ("Saying it nicely", [("I don’t know if you’ve noticed, but …", "не знаю, чи ти помітив, але …"), ("This might sound a bit petty, but …", "може, це дріб’язково, але …"),
         ("It’s probably just me, but …", "може, це тільки мені так, але …"), ("Would you mind (not) + -ing?", "ти не проти (не) …?"), ("eavesdrop", "підслуховувати"), ("overhear", "випадково почути"), ("etiquette", "етикет")])]
PH = json.dumps([["bugs me", "bug me"], ["nerves"], ["winds me up", "wind me up"], ["can't stand", "can't bear"], ["grates", "grate on"], ["infuriating", "maddening", "exasperating"], ["up the wall"], ["head in"], ["blood boil"], ["up to here"],
                 ["pet peeve", "pet hate"], ["grinds my gears", "grind my gears"], ["wrong way"], ["last straw"], ["bugbear"], ["petty"], ["inconsiderate"], ["oblivious"], ["passive-aggressive", "passive aggressive"], ["the ick"], ["fed up"], ["drives me mad", "drive me mad", "drives me crazy"]])
ST = json.dumps([["always / constantly + -ing", ["always [a-z]+ing", "constantly [a-z]+ing", "forever [a-z]+ing"]], ["keep + -ing", ["keeps? [a-z]+ing", "kept [a-z]+ing"]], ["I wish … would", ["wish [a-z ]{0,30}would"]],
                 ["What … is / The thing that … is", ["what (really |honestly |actually )?[a-z]+s? me is", "the thing that [a-z ]{0,30} is"]]])
XJS = r"""
document.querySelectorAll(".meter").forEach(r=>{const o=()=>r.nextElementSibling.textContent=r.value+(["",""," 😠"," 😠"," 😡"," 🤬"][r.value]||"");r.addEventListener("input",o);r._o=o});
function tiers(){const T=["S — unbearable","A — very annoying","B — mildly annoying","C — I don’t care"],C=["#ff7f7f","#ffbf7f","#ffdf7f","#bfff7f"];const L=[...document.querySelectorAll("[data-k^=t7_]")];
 document.getElementById("tierview").innerHTML=T.map((t,i)=>'<div class="tr"><span class="tl" style="background:'+C[i]+'">'+t.split(" — ")[0]+'</span><span class="ti">'+L.filter(s=>s.value===t).map(s=>'<i>'+s.closest(".row").querySelector("span").textContent+'</i>').join("")+'</span></div>').join("")}
document.querySelectorAll("[data-k^=t7_]").forEach(s=>s.addEventListener("change",tiers));
const PH=__PH__,ST=__ST__;const ch=document.getElementById("chk8");ch.innerHTML=ST.map(s=>'<span>'+s[0]+'</span>').join("");
function w8(){const v=(document.querySelector("[data-k=w8]").value||"").toLowerCase().replace(/[’]/g,"'");const n=(v.match(/\S+/g)||[]).length;const e=PH.filter(p=>p.some(x=>v.includes(x))).length;let s=0;
 [...ch.children].forEach((x,i)=>{const on=ST[i][1].some(r=>new RegExp(r).test(v));x.classList.toggle("on",on);if(on)s++});
 document.getElementById("wc8").textContent=n+" words (120–150) · "+e+" expressions from Ex. 3 (5+) · "+s+" structures from Ex. 4 (2+)"+(n>=120&&n<=150&&e>=5&&s>=2?" ✓ Great!":"")}
document.querySelector("[data-k=w8]").addEventListener("input",w8);
window.afterFill=()=>{document.querySelectorAll(".meter").forEach(r=>r._o());tiers();w8()};tiers();w8();
const st=document.createElement("style");st.textContent=`.vbox{margin:10px 0 14px;max-width:720px}.vbox.short{max-width:340px}.vbox.short .fr{padding-top:177%}.vt{font-weight:500;margin-bottom:4px}.vt .vn{color:#c2185b;font-weight:600;margin-right:4px}.vt .vd{color:#8a8b8d;font-size:13px}.vt a{font-size:13px;color:#c2185b;margin-left:8px}
.fr{position:relative;padding-top:56.25%}.fr iframe{position:absolute;inset:0;width:100%;height:100%;border:0;border-radius:6px}
.mrow{display:grid;grid-template-columns:1fr 200px 40px;gap:12px;align-items:center;padding:5px 0;border-bottom:1px solid #f3f3f3}.mrow input{accent-color:#c2416b}.mv{font-weight:600;color:#9e2d55}
.gt{border-collapse:collapse;font-size:15.5px}.gt td{padding:5px 12px 5px 0;vertical-align:top;border-bottom:1px solid #f2d3dd}.gt td:first-child{width:300px}
.tierv{margin:12px 0;border:1px solid #ddd;border-radius:6px;overflow:hidden}.tr{display:flex;min-height:44px;border-bottom:1px solid #eee}.tl{width:60px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:20px}.ti{flex:1;padding:6px;display:flex;flex-wrap:wrap;gap:6px;align-items:center;background:#fafafa}.ti i{font-style:normal;background:#fff;border:1px solid #ddd;border-radius:4px;padding:3px 8px;font-size:14px}
.rd{border:1px solid #ccc;border-radius:8px;padding:10px 14px;background:#fff;max-width:760px}.rdh{font-weight:600;color:#ff4500;margin-bottom:8px}.rd input{margin-bottom:8px;font-weight:500}
.chk2 span{display:inline-block;background:#f3f4f5;border-radius:14px;padding:3px 10px;margin:3px;font-size:14.5px}.chk2 span.on{background:#d9f2e2;color:#1e6b3d}
@media(max-width:800px){.mrow{grid-template-columns:1fr 120px 30px}}`;document.head.appendChild(st);
""".replace("__PH__", PH).replace("__ST__", ST)
html = page("😤", "Pet peeves", "B2+ · GENERAL ENGLISH", "Learners can talk about things that annoy them using strong expressions and habit structures, and complain diplomatically.",
            "GE B2+ Pet peeves: things that drive us up the wall", CODE, [(str(i + 1), s) for i, s in enumerate([s1, s2, s3, s4, s5, s6, s7, s8])], K, VOC,
            acc=ACC, acc2=ACC2, dark=DARK, grad2=GRAD2, footer="Videos: VOA Learning English, Cut, Petty Misdemeanors, BBC Learning English, scribblejuice (YouTube). Data: YouGov, April 2025. ", extra_js=XJS)
html = html.replace('<a href="../../../index.html">← Contents</a>', '<a href="../index.html">← My lessons</a>')
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
open(OUT, "w").write(html)
print("ok")
