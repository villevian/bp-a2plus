"""B1 1.1 · Homework after class: Clean your English (Taras, 26.11). Usage: build_b1_1-1_clean.py OUTDIR CODE
Teacher's explanations from the lesson (EN + UA toggle), error clinic from his own speech, shadowing, 4/3/2 retelling."""
import sys, os
from bp_page import page, fb, sel, inp, ta, ctl, SELF

OUTDIR = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
os.makedirs(OUTDIR, exist_ok=True)
K = {}
EP = "FRFb_JMB5g0"

def X(n, l): return '<b class="x">%s</b><b>%s</b> ' % (n, l)
def rule(title, en, ua):
    return ('<div class="card" style="background:#f7f8ff;border-left:4px solid #5b5fc7;margin:8px 0 14px"><b style="font-size:17px">📘 %s</b>'
            '<div style="margin-top:6px;line-height:1.6">%s</div>'
            '<details style="margin-top:10px"><summary style="cursor:pointer;color:#2a5fb0;font-weight:600">🇺🇦 Пояснення українською</summary>'
            '<div style="margin-top:6px;line-height:1.6">%s</div></details></div>') % (title, en, ua)
import random as _r
_R = _r.Random(7)
def gaps(prefix, items, opts, w=110):
    h = ""
    for i, it in enumerate(items):
        txt, ans = it[0], it[1]
        k = "%s_%d" % (prefix, i + 1); K[k] = ans if isinstance(ans, list) else [ans]
        o = list(it[2]) if len(it) > 2 else list(opts)
        if len(it) > 2: _R.shuffle(o)
        h += '<div class="row">%s) %s%s</div>' % ("abcdefghijkl"[i], txt.replace("___", sel(k, o, w)), fb(k))
    return h + ctl(prefix)
def fix(prefix, items, w=560):
    h = ""
    for i, (bad, good) in enumerate(items):
        k = "%s_%d" % (prefix, i + 1); K[k] = good
        h += '<div class="row">%s) <span style="color:#a33">“%s”</span><br>%s%s</div>' % ("abcdefghijkl"[i], bad, inp(k, w, "Your correct sentence"), fb(k))
    return h + ctl(prefix)
def v(*a):  # variants with straight / curly apostrophes
    out = []
    for s in a:
        for x in (s, s.replace("’", "'"), s.replace("'", "’")):
            if x not in out: out.append(x)
    return out

# ---------- 1 Error clinic ----------
EC = [("I not understand it.", v("I didn't understand it.", "I don't understand it.", "I did not understand it.", "I do not understand it.")),
      ("In this week I am working more than previous.", v("This week I'm working more than last week.", "This week I am working more than last week.", "This week I'm working more than usual.", "This week I am working more than usual.", "This week I'm working more than before.", "This week I am working more than before.")),
      ("All these skills very important.", v("All these skills are very important.", "All the skills are very important.", "All skills are very important.")),
      ("It makes your work more comfortable, more easiest.", v("It makes your work more comfortable and easier.", "It makes your work more comfortable, easier.", "It makes your work easier and more comfortable.")),
      ("When you work in team, you should build relationships.", v("When you work in a team, you should build relationships.")),
      ("I understood what about it.", v("I understood what it is about.", "I understood what it was about.", "I understand what it is about.")),
      ("Yesterday I forget the meaning.", v("Yesterday I forgot the meaning.")),
      ("I should thinking about it.", v("I should think about it.", "I need to think about it.")),
      ("Good communication skill is the simplest way to build relationships.", v("Good communication skills are the simplest way to build relationships.")),
      ("This skill very helpful for your routine.", v("This skill is very helpful for your routine.", "This skill is very helpful for your daily routine.", "This skill is very helpful in your routine.")),
      ("If talk about me, my main skill is communication.", v("If we're talking about me, my main skill is communication.", "If we are talking about me, my main skill is communication.", "If we talk about me, my main skill is communication.", "Talking about me, my main skill is communication.")),
      ("I can to use it in another job.", v("I can use it in another job."))]
s1 = ('<div class="bsec">Error clinic <span class="sub">Your own sentences from our lesson</span></div>' +
      '<div class="card" style="background:#fff8d6;border-left:4px solid #e0a100">🎯 <b>Why?</b> You told me: <i>“I already speak with mistakes – I need to re-learn.”</i> The best way is to <b>catch your own mistakes</b>. These are real sentences you said today (a little shortened).</div>' +
      '<p class="ins">' + X(1, "A") + 'Each sentence has <b>one</b> mistake. Write the correct sentence. Don’t look at the rules yet – try first. Then press <b>Check</b>.</p>' + fix("ec", EC) +
      '<p class="ins" style="margin-top:22px">' + X(1, "B") + 'Which mistake do you make <b>most often</b>? Write your own rule for it in 1–2 sentences – in English or Ukrainian.</p>' +
      ta("ec_rule", "My most common mistake is … My rule: …", 70))

# ---------- 2 Articles ----------
ART_EN = ("<b>Articles go in front of nouns.</b> They show that the word is a noun – some words can be a verb <i>and</i> a noun: <i>help</i>, <i>last</i> (<i>Last night we dined out.</i> / <i>The film lasts three hours.</i>).<br>"
          "<b>a / an</b> = one of many, any. <i>I need <b>a</b> pen</i> – any pen, not a special one. Only with nouns you can count, in the singular.<br>"
          "<b>the</b> = this exact one, the one we both know. <i>I need <b>the</b> cup you gave me yesterday.</i> <i>The love he gave me was not enough.</i> Even with names: <i>I saw <b>the</b> Peter</i> = that Peter we both know; <i>a Peter</i> = some Peter, I don’t know him.<br>"
          "<b>No article</b>: nouns you can’t count (<i>love, friendship, water, rice, sugar, juice, advice, feedback</i>) and plural nouns in general: <i>All skills are important.</i> But if it’s specific – <i>the</i>: <i>Give me <b>the</b> sugar on the top shelf.</i><br>"
          "<b>Jobs → a / an</b>: <i>I’m <b>a</b> teacher. I’m <b>an</b> IT specialist.</i> Specific: <i>I’m <b>the</b> English teacher of this university.</i><br>"
          "<b>Adjective + noun → the article goes before the adjective</b>: <i>in <b>a</b> friendly team</i>, <i>in <b>a</b> big IT team</i>.<br>"
          "<span class='hint'>Geography (countries, rivers…) has its own rules – later.</span>")
ART_UA = ("<b>Артикль стоїть перед іменником</b> і показує, що це іменник (help – допомагати / допомога; last – останній / тривати).<br>"
          "<b>a / an</b> – неозначений: «один із багатьох», будь-який. <i>I need a pen</i> – мені потрібна ручка, будь-яка. Тільки з тим, що можна порахувати, в однині.<br>"
          "<b>the</b> – означений: саме той, конкретний, про який ми обоє знаємо. <i>The cup you gave me yesterday</i> – саме та чашка. <i>The Peter</i> – той самий Пітер; <i>a Peter</i> – якийсь Пітер.<br>"
          "<b>Без артикля</b>: те, що не рахується (любов, дружба, вода, рис, цукор, сік, advice, feedback) і множина взагалі: <i>All skills are important</i> – усі навички загалом. Але конкретне – з the: <i>Дай мені той цукор з верхньої полиці – the sugar.</i><br>"
          "<b>Професія – завжди a / an</b>: <i>I’m a teacher, I’m an IT specialist.</i> Конкретний – the.<br>"
          "<b>Прикметник + іменник</b>: артикль іде перед прикметником – <i>in a friendly team</i>.")
ARTQ = [("I’m ___ .NET engineer with eight years of experience.", "a"), ("Thank you for ___ video you sent me yesterday – I watched it twice.", "the"),
        ("When you work in ___ team, communication is everything.", "a"), ("Can you give me some ___ advice about my CV?", "—"),
        ("I’m ___ IT specialist, and my wife is ___ designer.", None), ("___ skills you mentioned in your story are very strong.", "The"),
        ("I usually drink ___ water during long meetings.", "—"), ("We have ___ new client from Germany. ___ client wants a demo on Friday.", None)]
ARTQ2 = [("I’m ___ .NET engineer with eight years of experience.", "a"), ("Thank you for ___ video you sent me yesterday – I watched it twice.", "the"),
         ("When you work in ___ team, communication is everything.", "a"), ("Can you give me some ___ advice about my CV?", "– (no article)"),
         ("I’m ___ IT specialist.", "an"), ("___ skills you mentioned in your story are very strong.", "The"),
         ("I usually drink ___ water during long meetings.", "– (no article)"), ("We have a new client from Germany. ___ client wants a demo on Friday.", "The"),
         ("I work in ___ friendly international team.", "a"), ("___ feedback from my team lead was very useful.", "The")]
s2 = ('<div class="bsec">Grammar <span class="sub">Articles: a / an / the / no article</span></div>' +
      rule("What we said in class", ART_EN, ART_UA) +
      '<p class="ins">' + X(2, "A") + 'Choose <b>a</b>, <b>an</b>, <b>the</b> or <b>– (no article)</b>. Think: <i>one of many? this exact one? can I count it?</i></p>' +
      gaps("ar", [(t, [a.lower()]) for t, a in ARTQ2], ["a", "an", "the", "– (no article)"], 150) +
      '<p class="ins" style="margin-top:22px">' + X(2, "B") + 'Write 3 sentences about <b>your</b> work: one with <b>a/an</b>, one with <b>the</b>, one with <b>no article</b>.</p>' +
      ta("ar_own", "1 I’m a …\n2 The …\n3 I like … (no article)", 80))

# ---------- 3 to or -ing ----------
TI_EN = ("<b>Two verbs together.</b> The first verb is in the tense you need. The second verb is <b>to + verb</b> or <b>verb-ing</b>. "
         "In Ukrainian it’s always the infinitive (<i>я люблю грати</i>), in English you must <b>remember which verb takes which form</b>. There’s almost no system – so when you write down a new verb, write the form after it too.<br>"
         "<b>enjoy + -ing</b> – always: <i>I enjoy <b>working</b> with people.</i> Another form is a real mistake.<br>"
         "<b>like + -ing</b> (usually): <i>She likes <b>playing</b> the guitar.</i><br>"
         "<b>A verb at the start of a sentence → -ing</b>: <i><b>Smoking</b> is dangerous. <b>Thinking</b> outside the box is my strongest skill.</i><br>"
         "<b>try to</b> vs <b>try -ing</b> – the meaning changes:<br>"
         "• <b>try to do</b> = make an <b>effort</b>, it’s hard: <i>I tried <b>to fix</b> the bug all night.</i> Anchor: <b>effor<u>t</u> → <u>t</u>o</b>.<br>"
         "• <b>try doing</b> = test something new and see what happens: <i>Try <b>changing</b> the speed to 0.9.</i><br>"
         "<b>After can / should / must / will → just the verb</b>: <i>I should <b>think</b> about it</i> (not <s>should thinking</s>, not <s>can to use</s>).")
TI_UA = ("<b>Два дієслова підряд.</b> Перше – у потрібному часі, друге – або <b>to + дієслово</b>, або <b>дієслово з -ing</b>. В українській друге завжди в інфінітиві (люблю грати), в англійській треба <b>запам’ятати, яка форма йде після якого дієслова</b>. Системи майже немає, тому коли виписуєш слово – пиши й форму після нього.<br>"
         "<b>enjoy + -ing</b> – завжди. Інша форма – це помилка.<br><b>like + -ing</b> – найчастіше.<br>"
         "<b>Дієслово на початку речення → -ing</b>: <i>Smoking is dangerous</i> – курити шкідливо. <i>Thinking outside the box…</i><br>"
         "<b>try to</b> = намагатися, докладати зусиль. Якір: <b>effort</b> закінчується на <b>t → to</b>.<br><b>try -ing</b> = спробувати щось нове і подивитися, що буде.<br>"
         "<b>Після can / should / must / will</b> – просто дієслово: <i>I should think, I can use</i>.")
TIQ = [("I really enjoy ___ (work) with international teams.", "working", "to work"), ("___ (think) outside the box helps me in every area of my life.", "Thinking", "Think"),
       ("I tried ___ (change) the speed: 0.9 was perfect.", "changing", "to change"), ("I tried ___ (fix) the bug all night, but I couldn’t.", "to fix", "fixing"),
       ("I should ___ (think) about this puzzle.", "think", "thinking"), ("She likes ___ (play) the guitar.", "playing", "play"),
       ("You can ___ (use) this skill in any job.", "use", "to use"), ("___ (learn) a language is easier when you speak every day.", "Learning", "Learn")]
s3 = ('<div class="bsec">Grammar <span class="sub">Two verbs together: to or -ing?</span></div>' +
      rule("What we said in class", TI_EN, TI_UA) +
      '<p class="ins">' + X(3, "A") + 'Choose the correct form.</p>' +
      gaps("ti", [(t, [a], [a, b]) for t, a, b in TIQ], [], 140) +
      '<p class="ins" style="margin-top:22px">' + X(3, "B") + 'Two sentences about you: one with <b>try to</b> (an effort) and one with <b>try -ing</b> (a test).</p>' +
      ta("ti_own", "1 Last month I tried to …\n2 I tried … and it worked.", 70))

# ---------- 4 Simple vs Continuous ----------
SC_EN = ("<b>Present Simple</b> = what usually happens: habits, facts, schedules. Formula: <b>who + verb</b>. The verb doesn’t change – only with <b>he / she / it</b> we add <b>-s</b>: <i>it exists, my TV hangs, she works</i>. No -ing.<br>"
         "Markers: <i>every day / week, always, usually, often, sometimes, rarely, not often, never</i>. <i>I always work here. I usually have dinner at 7.</i><br>"
         "<b>Present Continuous</b> = <b>be + -ing</b>. If you forget <b>be</b>, it’s a mistake. Use it for:<br>"
         "• right now: <i>Sorry, I’m <b>having</b> a lesson – I’ll call you back.</i><br>"
         "• something different from usual, temporary: <i>Usually I work 8 hours, but this week <b>I’m working</b> more.</i><br>"
         "• a period of life: <i>I’m <b>learning</b> English.</i><br>"
         "• global trends: <i>The climate <b>is changing</b>.</i><br>"
         "Markers: <i>now, at the moment, right now, today, this week</i>.<br>"
         "<b>this / that / next / last week → no “in”</b>: <i><s>in this week</s> → this week</i>.<br>"
         "Bonus: Past and Future Continuous use the same formula – <i>was/were + -ing</i>, <i>will be + -ing</i>.")
SC_UA = ("<b>Present Simple</b> – те, що зазвичай: звички, факти, розклади. Формула: хто + що робить. Дієслово не змінюється, тільки з <b>he / she / it</b> додаємо <b>-s</b>. Ніякого -ing.<br>"
         "Маркери: every day, always, usually, often, sometimes, rarely / not often, never.<br>"
         "<b>Present Continuous</b> – <b>be + -ing</b> (без be – помилка). Коли: прямо зараз; щось не так, як завжди, тимчасово (зазвичай курю багато, а зараз менше); період життя (зараз вчу англійську); глобальні процеси (клімат змінюється).<br>"
         "Маркери: now, at the moment, right now, today, this week.<br>"
         "<b>this / that / next / last week</b> – без <b>in</b>. Українською «на цьому тижні», англійською просто this week.<br>"
         "Бонус: Past і Future Continuous – та сама формула: was/were + -ing, will be + -ing.")
SCQ = [("I usually ___ (start) work at 9.", "start", "’m starting"), ("This week I ___ (work) from home because of the repairs.", "’m working", "work"),
       ("He ___ (write) the backend, and she designs the UI.", "writes", "is writing"), ("Sorry, I can’t talk – I ___ (have) a lesson right now.", "’m having", "have"),
       ("I ___ (learn) English with a private teacher this year.", "’m learning", "learn"), ("Our team ___ (have) a stand-up every morning.", "has", "is having"),
       ("The IT job market ___ (change) very fast these days.", "is changing", "changes"), ("How often ___ (you / read) books in English?", "do you read", "are you reading")]
SCOPT = ["start", "’m starting", "’m working", "work", "writes", "is writing", "’m having", "have", "’m learning", "learn", "has", "is having", "is changing", "changes", "do … read", "are … reading"]
s4 = ('<div class="bsec">Grammar <span class="sub">Present Simple or Present Continuous?</span></div>' +
      rule("What we said in class", SC_EN, SC_UA) +
      '<p class="ins">' + X(4, "A") + 'Usually or now / this week? Choose the correct form.</p>' +
      gaps("sc", [(t, v(a), [a, b]) for t, a, b in SCQ], [], 150) +
      '<p class="ins" style="margin-top:22px">' + X(4, "B") + 'Your week. Write 3 pairs: <b>Usually I …, but this week I’m …</b></p>' +
      ta("sc_own", "1 Usually I …, but this week I’m …\n2 …\n3 …", 90))

# ---------- 5 Word order, be, sounds ----------
WO_EN = ("<b>Word order: who → does what.</b> In Ukrainian we can move words (<i>кішка з’їла мишку / мишку з’їла кішка</i>) because of endings. In English the order is fixed: <i>The cat ate the mouse.</i><br>"
         "So: <i>I understood <b>what it is about</b></i> (not <s>what about it</s>) – after <i>what</i> comes a normal sentence: <i>it + is</i>.<br>"
         "<b>Every sentence needs a verb.</b> Don’t forget <b>be</b>: <i>All these skills <b>are</b> very important. This skill <b>is</b> very helpful.</i><br>"
         "<b>easier</b>, not <s>more easier</s> – short adjectives take <b>-er</b>, long ones take <b>more</b>: <i>easier, faster, but more comfortable</i>.<br>"
         "<b>this</b> = one, short sound /ɪ/: <i>this skill</i>. <b>these</b> = many, long sound /iː/ – you “sing” it: <i>these skills</i>.")
WO_UA = ("<b>Порядок слів: хто → що робить.</b> В українській слова можна переставляти завдяки закінченням, в англійській порядок фіксований.<br>"
         "Тому <i>I understood what it is about</i> – після what іде звичайне речення: it + is.<br>"
         "<b>У реченні завжди потрібне дієслово</b> – не забувай <b>be</b>: All these skills <b>are</b> very important.<br>"
         "<b>easier</b>, а не more easier: короткі прикметники – <b>-er</b>, довгі – more.<br>"
         "<b>this</b> – один, короткий звук /ɪ/. <b>these</b> – багато, довгий звук /iː/, ніби проспівуєш.")
SND = [("ship", "sheep"), ("this", "these"), ("live", "leave"), ("it", "eat"), ("fill", "feel"), ("bit", "beat"), ("sit", "seat"), ("still", "steal")]
import random
rnd = random.Random(11)
snd = ""
for i, (a, b) in enumerate(SND):
    w = [a, b][rnd.randint(0, 1)]; k = "sn_%d" % (i + 1); K[k] = [w]
    snd += ('<div class="row">%s) <button class="btn l" type="button" style="min-height:40px;padding:4px 14px" onclick="say(\'%s\')">🔊 Listen</button> %s%s</div>'
            % ("abcdefgh"[i], w, sel(k, [a, b], 120), fb(k)))
s5 = ('<div class="bsec">Grammar & sounds <span class="sub">Word order, “be”, this / these</span></div>' +
      rule("What we said in class", WO_EN, WO_UA) +
      '<p class="ins">' + X(5, "A") + 'Short /ɪ/ or long /iː/? Listen and choose the word you hear.</p>' + snd + ctl("sn") +
      '<p class="ins" style="margin-top:22px">' + X(5, "B") + 'Say these pairs aloud 3 times, slowly: <i>this skill – these skills · ship – sheep · live – leave · sit – seat</i>. Record yourself below and listen: can you hear the difference?</p>' +
      '<div class="rec" data-r="pair"></div>')

# ---------- 6 Shadowing ----------
def clip(a, b):
    return ('<div style="width:100%%;max-width:600px;aspect-ratio:16/9;margin:8px 0"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0&cc_load_policy=1&start=%d&end=%d" '
            'style="width:100%%;height:100%%;border:0;border-radius:12px" allow="encrypted-media; picture-in-picture" allowfullscreen loading="lazy"></iframe></div>') % (EP, a, b)
s6 = ('<div class="bsec">Shadowing <span class="sub">Speak like the speakers</span></div>' +
      '<div class="card" style="background:#f4f6ff;border-left:4px solid #5b5fc7">🧭 <b>Shadowing</b> = you repeat what the speaker says <b>at the same time</b>, like a shadow. It trains pronunciation, rhythm and ready-made phrases. You already know this video – that makes it easier.<br>'
      '<b>4 rounds for each clip:</b> ① listen with subtitles (CC) · ② speed <b>0.9</b>: whisper together with the speaker · ③ speed 0.9: speak aloud together · ④ normal speed: speak aloud together.<br>'
      '<span class="hint">🇺🇦 Повторюй за спікером одночасно, як тінь. 4 кола: слухаєш із субтитрами → шепочеш на 0.9 → говориш уголос на 0.9 → на звичайній швидкості.</span></div>' +
      '<p class="ins">' + X(6, "A") + 'Clip 1 (about 30 seconds).</p>' + clip(64, 94) +
      '<p class="ins" style="margin-top:18px">' + X(6, "B") + 'Clip 2.</p>' + clip(94, 130) +
      '<p class="ins" style="margin-top:18px">' + X(6, "C") + 'Clip 3.</p>' + clip(130, 170) +
      '<p class="ins" style="margin-top:22px">' + X(6, "D") + 'Record yourself shadowing one clip (round ④) and listen.</p><div class="rec" data-r="shadow"></div>' +
      '<p class="ins" style="margin-top:22px">' + X(6, "E") + 'Write down 3 phrases you can now say <b>exactly like the speaker</b>.</p>' + ta("sh_ph", "1 …\n2 …\n3 …", 70))

# ---------- 7 4/3/2 ----------
s7 = ('<div class="bsec">Speaking <span class="sub">Say it again – cleaner (2 / 1.5 / 1)</span></div>' +
      '<div class="card" style="background:#fff8d6;border-left:4px solid #e0a100">🧭 You tell the <b>same story three times</b>, each time faster: <b>2 minutes → 1.5 minutes → 1 minute</b>. Each time you make fewer mistakes and fewer pauses.<br>'
      '<span class="hint">🇺🇦 Одну й ту саму історію розповідаєш тричі, щоразу коротше: 2 хв → 1,5 хв → 1 хв. Щоразу чистіше.</span></div>' +
      '<p class="ins">' + X(7, "A") + 'Your topic: <b>“Thinking outside the box is my strongest skill.”</b> Why? Give a real example from work or life. Bonus: tell how you tried to solve the <b>nine dots puzzle</b> (<i>First I tried…, then I realised…</i>).</p>' +
      '<div class="card" style="background:#fbfbfd">✅ <b>My checklist before I speak:</b> <i>be</i> in every sentence? · <i>-s</i> with he/she/it? · <i>a / the</i> before nouns? · who → does what? · past = <i>didn’t / forgot / tried</i>?</div>' +
      '<div class="rec" data-r="r1" data-t="120"></div><div class="rec" data-r="r2" data-t="90"></div><div class="rec" data-r="r3" data-t="60"></div>' +
      '<p class="ins" style="margin-top:22px">' + X(7, "B") + 'Listen to round 1 and round 3. Which mistakes did you fix? Which mistakes are still there?</p>' +
      ta("r_ref", "In round 3 I fixed … I still say …", 80) +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you notice and fix your own mistakes now?"))

XJS = r"""function say(w){try{const u=new SpeechSynthesisUtterance(w);u.lang="en-GB";u.rate=.8;speechSynthesis.cancel();speechSynthesis.speak(u)}catch(e){}}
document.querySelectorAll(".rec").forEach(box=>{const t=+box.dataset.t||0;const lab={r1:"Round 1 · 2:00",r2:"Round 2 · 1:30",r3:"Round 3 · 1:00",pair:"Sound pairs",shadow:"Shadowing"}[box.dataset.r]||"Record";
 box.className="card rec";box.style.cssText="margin:10px 0;background:#fff";box.innerHTML='<b>🎙 '+lab+'</b> <button class="btn" type="button" style="min-height:40px">● Record</button> <span class="tm" style="font:600 18px monospace;margin-left:8px"></span> <audio controls style="display:none;vertical-align:middle;margin-left:8px;max-width:100%"></audio><div class="hint">The recording stays on your device – only you can hear it.</div>';
 const b=box.querySelector("button"),tm=box.querySelector(".tm"),au=box.querySelector("audio");let mr=null,ch=[],iv=null,left=0;
 function stop(){if(mr&&mr.state!=="inactive")mr.stop();clearInterval(iv);b.textContent="● Record again"}
 b.onclick=async()=>{if(mr&&mr.state==="recording"){stop();return}
  try{const s=await navigator.mediaDevices.getUserMedia({audio:true});mr=new MediaRecorder(s);ch=[];mr.ondataavailable=e=>ch.push(e.data);mr.onstop=()=>{au.src=URL.createObjectURL(new Blob(ch));au.style.display="inline-block";s.getTracks().forEach(x=>x.stop())};mr.start();b.textContent="■ Stop";
   left=t;const show=()=>{tm.textContent=t?(Math.floor(left/60)+":"+String(left%60).padStart(2,"0")):"";};show();if(t)iv=setInterval(()=>{left--;show();if(left<=0){stop();tm.textContent="⏰ time!"}},1000)}
  catch(e){tm.textContent="Microphone is not available – just speak and use a timer.";}}});
"""
VOC = [("Clean English", ["I didn’t understand it.", "this week", "in a team", "what it is about", "I forgot", "I should think about it", "communication skills", "easier", "try to", "try -ing"]),
       ("Lesson words", ["a can-do attitude", "set goals", "determination", "integrity", "think outside the box", "critical thinking", "team player"])]
html = page("1.1", "Transferable skills", "HOMEWORK · CLEAN YOUR ENGLISH", "Notice and fix your own mistakes; use articles, to/-ing and Simple vs Continuous correctly.",
            "BP B1 1.1 Transferable skills · Clean English", CODE,
            [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5), ("6", s6), ("7", s7)], K, VOC, extra_js=XJS)
open(os.path.join(OUTDIR, "clean.html"), "w").write(html)
print("ok", OUTDIR)
