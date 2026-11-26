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
        h += '<div class="row">%s) %s%s</div>' % ("abcdefghijklmnop"[i], txt.replace("___", sel(k, o, w)), fb(k))
    return h + ctl(prefix)
def fix(prefix, items, w=560):
    h = ""
    for i, (bad, good) in enumerate(items):
        k = "%s_%d" % (prefix, i + 1); K[k] = good
        h += '<div class="row">%s) <span style="color:#a33">“%s”</span><br>%s%s</div>' % ("abcdefghijklmnop"[i], bad, inp(k, w, "Your correct sentence"), fb(k))
    return h + ctl(prefix)
def v(*a):  # variants with straight / curly apostrophes
    out = []
    for s in a:
        for x in (s, s.replace("’", "'"), s.replace("'", "’")):
            if x not in out: out.append(x)
    return out

WO_EN = ("<b>Word order: who → does what.</b> In Ukrainian we can move words (<i>кішка з’їла мишку / мишку з’їла кішка</i>) because of endings. In English the order is fixed: <i>The cat ate the mouse.</i><br>"
         "So: <i>I understood <b>what it is about</b></i> (not <s>what about it</s>) – after <i>what</i> comes a normal sentence: <i>it + is</i>.<br>"
         "<b>Every sentence needs a verb.</b> Don’t forget <b>be</b>: <i>All these skills <b>are</b> very important.</i><br>"
         "<b>easier</b>, not <s>more easier</s> – short adjectives take <b>-er</b>, long ones take <b>more</b>: <i>easier, faster, but more comfortable</i>.")
WO_UA = ("<b>Порядок слів: хто → що робить.</b> В українській слова можна переставляти завдяки закінченням, в англійській порядок фіксований.<br>"
         "Тому <i>I understood what it is about</i> – після what іде звичайне речення: it + is.<br>"
         "<b>У реченні завжди потрібне дієслово</b> – не забувай <b>be</b>: All these skills <b>are</b> very important.<br>"
         "<b>easier</b>, а не more easier: короткі прикметники – <b>-er</b>, довгі – more.")

# ---------- 1 Error clinic ----------
# (wrong sentence, [correct variants], why it is right, what the mistake is)
EC = [
 ("Sorry, I not understand your question yesterday.", ["Sorry, I didn't understand your question yesterday.", "Sorry, I did not understand your question yesterday."],
  "Past + negative → <b>didn’t + verb</b>: I didn’t understand.", "It’s the past (yesterday) and negative. We need <b>didn’t</b> + verb, not just <i>not</i>."),
 ("Last month I’m reading a great book about leadership.", ["Last month I read a great book about leadership."],
  "Finished action in the past → <b>Past Simple</b>: I read.", "<i>Last month</i> is finished past. <i>I’m reading</i> = now. Use the past form."),
 ("In this week I’m working from home.", ["This week I'm working from home.", "This week I am working from home."],
  "<b>this / that / next / last week</b> – no <i>in</i>.", "Look at the word before <i>this week</i>. With this / that / next / last we don’t use a preposition."),
 ("Right now we discuss the new release – can I call you back?", ["Right now we're discussing the new release – can I call you back?", "Right now we are discussing the new release – can I call you back?", "Right now we're discussing the new release - can I call you back?", "Right now we are discussing the new release - can I call you back?", "Right now we're discussing the new release, can I call you back?", "Right now we are discussing the new release, can I call you back?"],
  "Happening at this moment → <b>be + -ing</b>: we’re discussing.", "<i>Right now</i> = at this moment. Present Simple is for habits. Use <b>be + -ing</b>."),
 ("Our team lead have a stand-up every day at 10.", ["Our team lead has a stand-up every day at 10."],
  "A habit → Present Simple; <b>he / she / it → +s</b>: has.", "Who? The team lead = <b>he / she</b>. In Present Simple he/she/it changes the verb: have → ?"),
 ("These skill is very useful for developers.", ["This skill is very useful for developers."],
  "One skill → <b>this</b> (short /ɪ/). Many skills → these.", "Count: one skill or many? <i>is</i> and <i>skill</i> are singular."),
 ("All these tools very helpful for remote work.", ["All these tools are very helpful for remote work."],
  "Every sentence needs a verb → <b>are</b> very helpful.", "Where is the verb? Don’t forget <b>be</b>."),
 ("Working with AI makes my job more easier.", ["Working with AI makes my job easier."],
  "Short adjective → <b>-er</b>: easier (no <i>more</i>).", "<i>easy</i> is short: we add <b>-er</b>. <i>more</i> is only for long adjectives."),
 ("She works in big IT company in Lviv.", ["She works in a big IT company in Lviv.", "She works for a big IT company in Lviv."],
  "One of many companies → <b>a</b>, and it goes before the adjective: <b>a</b> big IT company.", "<i>company</i> is a countable noun. Which article? Where does it go if there is an adjective?"),
 ("My brother is engineer at a bank.", ["My brother is an engineer at a bank."],
  "Jobs → <b>a / an</b>: an engineer (vowel sound → an).", "Before a job we always use an article. <i>engineer</i> starts with a vowel sound."),
 ("Can you send me video from yesterday’s meeting?", ["Can you send me the video from yesterday's meeting?"],
  "This exact video, we both know which → <b>the</b>.", "It’s one specific video – from yesterday’s meeting. Which article?"),
 ("I enjoy to work with international clients.", ["I enjoy working with international clients."],
  "<b>enjoy + -ing</b> – always.", "After <i>enjoy</i> the second verb has one form only – not <i>to</i>."),
 ("Set clear goals is important for every team.", ["Setting clear goals is important for every team."],
  "A verb at the start of a sentence → <b>-ing</b>: Setting goals…", "The sentence starts with a verb as a subject. Which form do we use?"),
 ("I tried fixing this bug all night, but it was too hard.", ["I tried to fix this bug all night, but it was too hard."],
  "A big effort → <b>try to</b> (effor<b>t</b> → <b>t</b>o).", "Was it an effort or a quick test? Remember: effor<b>t</b> → <b>t</b>o."),
 ("I don’t know what about this task.", ["I don't know what this task is about.", "I do not know what this task is about."],
  "After <i>what</i> → normal order: <b>this task + is</b> about.", "Who → does what. After <i>what</i> we need a normal sentence: subject + verb."),
 ("Yesterday I forget my laptop at the office.", ["Yesterday I forgot my laptop at the office.", "Yesterday I left my laptop at the office."],
  "Past → <b>forgot</b>.", "<i>Yesterday</i> = past. <i>forget</i> has an irregular past form."),
 ("I can’t open my colleague laptop.", ["I can't open my colleague's laptop."],
  "Whose laptop? → <b>colleague’s</b> (’s = belongs to).", "The laptop belongs to the colleague. How do we show this?"),
 ("He has good communication skill.", ["He has good communication skills."],
  "A fixed phrase: <b>communication skills</b> (plural).", "This phrase is usually plural."),
]
import random as _rr
_rr.Random(26).shuffle(EC)
ECW = {}
ECUA = {'Sorry, I not understand your question yesterday.': 'Вибач, я вчора не зрозумів твого питання.', 'Last month I’m reading a great book about leadership.': 'Минулого місяця я прочитав чудову книжку про лідерство.', 'In this week I’m working from home.': 'Цього тижня я працюю з дому (а зазвичай – ні).', 'Right now we discuss the new release – can I call you back?': 'Ми саме зараз обговорюємо новий реліз – можна я тобі передзвоню?', 'Our team lead have a stand-up every day at 10.': 'Наш тімлід щодня проводить стендап о 10-й.', 'These skill is very useful for developers.': 'Ця навичка дуже корисна для розробників.', 'All these tools very helpful for remote work.': 'Усі ці інструменти дуже корисні для віддаленої роботи.', 'Working with AI makes my job more easier.': 'Робота з ШІ робить мою роботу легшою.', 'She works in big IT company in Lviv.': 'Вона працює у великій IT-компанії у Львові.', 'My brother is engineer at a bank.': 'Мій брат – інженер у банку.', 'Can you send me video from yesterday’s meeting?': 'Можеш надіслати мені відео з учорашньої зустрічі?', 'I enjoy to work with international clients.': 'Мені подобається працювати з іноземними клієнтами.', 'Set clear goals is important for every team.': 'Ставити чіткі цілі важливо для кожної команди.', 'I tried fixing this bug all night, but it was too hard.': 'Я цілу ніч намагався виправити цей баг, але це було надто складно.', 'I don’t know what about this task.': 'Я не знаю, про що це завдання.', 'Yesterday I forget my laptop at the office.': 'Учора я забув ноутбук в офісі.', 'I can’t open my colleague laptop.': 'Я не можу відкрити ноутбук колеги.', 'He has good communication skill.': 'У нього хороші комунікативні навички.'}
def ecfix(prefix, items, w=560):
    h = ""
    for i, (bad, good, okx, errx) in enumerate(items):
        k = "%s_%d" % (prefix, i + 1); K[k] = v(*good); ECW[k] = [okx, errx]
        h += '<div class="row">%d. <span style="color:#a33">“%s”</span><br><span class="hint">🇺🇦 %s</span><br>%s%s</div>' % (i + 1, bad, ECUA[bad], inp(k, w, "Write the correct sentence"), fb(k))
    return h + '<div class="ctl"><button class="btn" onclick="chkEC(\'%s\')">Check</button><span class="res" id="r_%s"></span></div>' % (prefix, prefix)
s1 = ('<div class="bsec">Error clinic <span class="sub">Find and fix the mistake · analyse</span></div>' +
      '<div class="card" style="background:#fff8d6;border-left:4px solid #e0a100">🎯 <b>Why?</b> You said in our lesson: <i>“I already speak with mistakes – I need to re-learn.”</i> You have practised the rules in Steps 1–3. Now learn to <b>catch mistakes</b> – first in other people’s English, then in your own.</div>' +
      '<p class="ins">Before you start – two more rules from our lesson:</p>' + rule("Word order, “be”, easier", WO_EN, WO_UA) +
      '<p class="ins">' + X(4, "A") + 'Colleagues wrote these sentences in Slack. Each one has <b>one</b> mistake – the topics we talked about in class. Under each sentence you can see in Ukrainian what the person wants to say. Write the correct sentence and press <b>Check</b>. If it’s wrong, read the hint and try again.</p>' + ecfix("ec", EC) +
      '<p class="ins" style="margin-top:22px">' + X(4, "B") + 'Which of these mistakes do <b>you</b> make too? Write your own rule for it in 1–2 sentences – in English or Ukrainian.</p>' +
      ta("ec_rule", "I also make the mistake with … My rule: …", 70))

# ---------- 2 Articles ----------
ART_EN = ("<b>Articles go in front of nouns.</b> They show that the word is a noun – some words can be a verb <i>and</i> a noun: <i>help</i>, <i>last</i> (<i>Last night we dined out.</i> / <i>The film lasts three hours.</i>).<br>"
          "<b>a / an</b> = one of many, any. <i>I need <b>a</b> pen</i> – any pen, not a special one. Only with nouns you can count, in the singular.<br>"
          "<b>the</b> = this exact one, the one we both know. <i>I need <b>the</b> cup you gave me yesterday.</i> <i>The love he gave me was not enough.</i> Even with names: <i>I saw <b>the</b> Peter</i> = that Peter we both know; <i>a Peter</i> = some Peter, I don’t know him.<br>"
          "<b>No article</b>: nouns you can’t count (<i>love, friendship, water, rice, sugar, juice</i>) and plural nouns in general: <i>All skills are important.</i> But if it’s specific – <i>the</i>: <i>Give me <b>the</b> sugar on the top shelf.</i><br>"
          "<b>Jobs → a / an</b>: <i>I’m <b>a</b> teacher. I’m <b>an</b> IT specialist.</i> Specific: <i>I’m <b>the</b> English teacher of this university.</i><br>"
          "<b>Adjective + noun → the article goes before the adjective</b>: <i>in <b>a</b> friendly team</i>, <i>in <b>a</b> big IT team</i>.<br>"
          "<span class='hint'>Geography (countries, rivers…) has its own rules – later.</span>")
ART_UA = ("<b>Артикль стоїть перед іменником</b> і показує, що це іменник (help – допомагати / допомога; last – останній / тривати).<br>"
          "<b>a / an</b> – неозначений: «один із багатьох», будь-який. <i>I need a pen</i> – мені потрібна ручка, будь-яка. Тільки з тим, що можна порахувати, в однині.<br>"
          "<b>the</b> – означений: саме той, конкретний, про який ми обоє знаємо. <i>The cup you gave me yesterday</i> – саме та чашка. <i>The Peter</i> – той самий Пітер; <i>a Peter</i> – якийсь Пітер.<br>"
          "<b>Без артикля</b>: те, що не рахується (любов, дружба, вода, рис, цукор, сік) і множина взагалі: <i>All skills are important</i> – усі навички загалом. Але конкретне – з the: <i>Дай мені той цукор з верхньої полиці – the sugar.</i><br>"
          "<b>Професія – завжди a / an</b>: <i>I’m a teacher, I’m an IT specialist.</i> Конкретний – the.<br>"
          "<b>Прикметник + іменник</b>: артикль іде перед прикметником – <i>in a friendly team</i>.")
ARTQ = [("I’m ___ .NET engineer with eight years of experience.", "a"), ("Thank you for ___ video you sent me yesterday – I watched it twice.", "the"),
        ("When you work in ___ team, communication is everything.", "a"), ("Can you give me some ___ advice about my CV?", "—"),
        ("I’m ___ IT specialist, and my wife is ___ designer.", None), ("___ skills you mentioned in your story are very strong.", "The"),
        ("I usually drink ___ water during long meetings.", "—"), ("We have ___ new client from Germany. ___ client wants a demo on Friday.", None)]
ARTQ2 = [("I’m ___ .NET engineer with eight years of experience.", "a"), ("Thank you for ___ video you sent me yesterday – I watched it twice.", "the"),
         ("When you work in ___ team, communication is everything.", "a"), ("Friendship is important, but ___ love is more important.", "– (no article)"),
         ("I’m ___ IT specialist.", "an"), ("___ skills you mentioned in your story are very strong.", "The"),
         ("I usually drink ___ water during long meetings.", "– (no article)"), ("We have a new client from Germany. ___ client wants a demo on Friday.", "The"),
         ("I work in ___ friendly international team.", "a"), ("___ juice in the office fridge is mine – please don’t drink it!", "The")]

STAR_EN = ("Some nouns in English are <b>uncountable</b>, but in Ukrainian we can count them. They have <b>no a/an</b> and <b>no plural</b>:<br>"
           "<i>advice, information, feedback, news, software, equipment, research, knowledge</i>.<br>"
           "❌ <s>an advice</s>, <s>informations</s> → ✅ <b>some</b> advice, <b>a piece of</b> advice, <b>much</b> information, <b>the</b> feedback (this exact feedback).<br>"
           "<i>news</i> looks plural but it’s singular: <i>The news <b>is</b> good.</i>")
STAR_UA = ("Деякі іменники в англійській <b>незлічувані</b>, хоча в українській ми їх рахуємо (порада – поради, інформація). З ними <b>немає a/an</b> і <b>немає множини</b>: advice, information, feedback, news, software, equipment, research, knowledge.<br>"
           "Не можна: an advice, informations. Можна: some advice, a piece of advice (одна порада), much information, the feedback (саме цей).<br>"
           "<i>news</i> виглядає як множина, але це однина: The news is good.")
STQ = [("Can you give me ___ advice about my CV?", "some", "an"), ("Thanks for ___ feedback you gave me yesterday – it really helped.", "the", "a"),
       ("I need more ___ about the project.", "information", "informations"), ("Let me give you ___ piece of advice: show, don’t tell.", "a", "an"),
       ("The news about the release ___ good.", "is", "are"), ("We don’t have ___ equipment for video calls in this room.", "much", "many")]
s2star = ('<div class="card" style="margin-top:26px;border-left:4px solid #e0a100;background:#fffaf0"><b style="color:#b26b00">★ If you want to know more</b> – optional. Words like <i>advice</i> and <i>information</i>.</div>' +
          rule("Uncountable nouns at work", STAR_EN, STAR_UA) +
          '<p class="ins">' + X(1, "C") + '★ Choose the correct word.</p>' +
          gaps("st", [(t, [a], [a, b]) for t, a, b in STQ], [], 150))
s2 = ('<div class="bsec">Grammar <span class="sub">Articles: a / an / the / no article · understand → apply</span></div>' +
      rule("What we said in class", ART_EN, ART_UA) +
      '<p class="ins">' + X(1, "A") + 'Choose <b>a</b>, <b>an</b>, <b>the</b> or <b>– (no article)</b>. Think: <i>one of many? this exact one? can I count it?</i></p>' +
      gaps("ar", [(t, [a.lower()]) for t, a in ARTQ2], ["a", "an", "the", "– (no article)"], 150) +
      '<p class="ins" style="margin-top:22px">' + X(1, "B") + 'Write 3 sentences about <b>your</b> work: one with <b>a/an</b>, one with <b>the</b>, one with <b>no article</b>.</p>' +
      ta("ar_own", "1 I’m a …\n2 The …\n3 I like … (no article)", 80) + s2star)

# ---------- 3 to or -ing ----------
TI_EN = ("<b>Two verbs together.</b> The first verb is in the tense you need. The second verb is <b>to + verb</b> or <b>verb-ing</b>. "
         "In Ukrainian it’s always the infinitive (<i>я люблю грати</i>), in English you must <b>remember which verb takes which form</b>. There’s almost no system – so when you write down a new verb, write the form after it too.<br>"
         "<b>enjoy + -ing</b> – always: <i>I enjoy <b>working</b> with people.</i> Another form is a real mistake.<br>"
         "<b>like + -ing</b> (usually): <i>She likes <b>playing</b> the guitar.</i><br>"
         "<b>A verb at the start of a sentence → -ing</b>: <i><b>Smoking</b> is dangerous. <b>Thinking</b> outside the box is my strongest skill.</i><br>"
         "<b>try to</b> vs <b>try -ing</b> – the meaning changes:<br>"
         "• <b>try to do</b> = make an <b>effort</b>, it’s hard: <i>I tried <b>to fix</b> the bug all night.</i> Anchor: <b>effor<u>t</u> → <u>t</u>o</b>.<br>"
         "• <b>try doing</b> = test something new and see what happens: <i>Try <b>changing</b> the speed to 0.9.</i><br>"
         "<b>More verbs from Unit 1:</b> <i>want / decide / plan / hope <b>to</b> do</i> · <i>avoid / consider / keep <b>doing</b></i> · <i>how about / what about <b>doing</b>?</i> · <i>should / could / why don’t you + <b>do</b></i>.")
TI_UA = ("<b>Два дієслова підряд.</b> Перше – у потрібному часі, друге – або <b>to + дієслово</b>, або <b>дієслово з -ing</b>. В українській друге завжди в інфінітиві (люблю грати), в англійській треба <b>запам’ятати, яка форма йде після якого дієслова</b>. Системи майже немає, тому коли виписуєш слово – пиши й форму після нього.<br>"
         "<b>enjoy + -ing</b> – завжди. Інша форма – це помилка.<br><b>like + -ing</b> – найчастіше.<br>"
         "<b>Дієслово на початку речення → -ing</b>: <i>Smoking is dangerous</i> – курити шкідливо. <i>Thinking outside the box…</i><br>"
         "<b>try to</b> = намагатися, докладати зусиль. Якір: <b>effort</b> закінчується на <b>t → to</b>.<br><b>try -ing</b> = спробувати щось нове і подивитися, що буде.<br>"
         "<b>Ще дієслова з Unit 1:</b> want / decide / plan / hope + <b>to</b>; avoid / consider / keep + <b>-ing</b>; how about / what about + <b>-ing</b>; should / could / why don’t you + просто дієслово.")
TIQ = [("I really enjoy ___ (work) in a team.", "working", "to work"), ("___ (set) clear goals helps me finish projects on time.", "Setting", "Set"),
       ("I want ___ (change) careers and work for an international company.", "to change", "changing"), ("Many people decide ___ (apply) for jobs abroad.", "to apply", "applying"),
       ("I tried ___ (fix) the bug all night, but I couldn’t.", "to fix", "fixing"), ("Try ___ (ask) your online connections for advice – maybe it will work.", "asking", "to ask"),
       ("You should ___ (show) your transferable skills, not just list them.", "show", "to show"), ("How about ___ (add) your side project to your CV?", "adding", "to add"),
       ("Why don’t you ___ (write) about your experience with AI?", "write", "writing"), ("Avoid ___ (use) words like “hard-working” – show it instead.", "using", "to use"),
       ("Have you considered ___ (do) a cloud certification?", "doing", "to do"), ("Keep ___ (learn) new tools – the market changes fast.", "learning", "to learn")]
s3 = ('<div class="bsec">Grammar <span class="sub">Two verbs together: to or -ing? · understand → apply</span></div>' +
      rule("What we said in class", TI_EN, TI_UA) +
      '<p class="ins">' + X(2, "A") + 'Choose the correct form. All the verbs are from <b>Unit 1</b> – you will need them for careers advice on Monday.</p>' +
      gaps("ti", [(t, [a], [a, b]) for t, a, b in TIQ], [], 140) +
      '<p class="ins" style="margin-top:22px">' + X(2, "B") + 'Two sentences about you: one with <b>try to</b> (an effort) and one with <b>try -ing</b> (a test).</p>' +
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
s4 = ('<div class="bsec">Grammar <span class="sub">Present Simple or Present Continuous? · understand → apply</span></div>' +
      rule("What we said in class", SC_EN, SC_UA) +
      '<p class="ins">' + X(3, "A") + 'Usually or now / this week? Choose the correct form.</p>' +
      gaps("sc", [(t, v(a), [a, b]) for t, a, b in SCQ], [], 150) +
      '<p class="ins" style="margin-top:22px">' + X(3, "B") + 'Your week. Write 3 pairs: <b>Usually I …, but this week I’m …</b></p>' +
      ta("sc_own", "1 Usually I …, but this week I’m …\n2 …\n3 …", 90))

# ---------- 5 Word order, be, sounds ----------
SN_EN = ("In Ukrainian we have one sound <b>і</b>. English has <b>two different sounds</b> – and they change the meaning: <i>live</i> (жити) – <i>leave</i> (їхати, йти); <i>ship</i> – <i>sheep</i>; <i>this</i> – <i>these</i>.<br>"
         "<b>/ɪ/ – short and relaxed.</b> Your mouth is relaxed, the sound is short, a bit like Ukrainian <b>и</b>: <i>th<b>i</b>s, sk<b>i</b>ll, l<b>i</b>ve, sh<b>i</b>p, f<b>i</b>t, b<b>u</b>sy</i>.<br>"
         "<b>/iː/ – long and tense.</b> Smile, your lips are stretched, the sound is long – like a long Ukrainian <b>і-і</b>: <i>th<b>e</b>se, t<b>ea</b>m, l<b>ea</b>ve, sh<b>ee</b>p, n<b>ee</b>d, f<b>ie</b>ld</i>.<br>"
         "<b>How to know from the spelling:</b><br>"
         "• <b>ee, ea, ie, e + consonant + e</b> → long /iː/: <i>meeting, feedback, team, lead, field, these, complete</i>. Also <i>he, she, we, me</i>.<br>"
         "• <b>i</b> + consonant at the end of a syllable → short /ɪ/: <i>this, skill, fix, build, ship, live, quick, think</i>.<br>"
         "• Exceptions to remember: <i>police, machine</i> (i = /iː/); <i>been</i> is often short.<br>"
         "<b>Tip:</b> for /iː/ – smile and make it long; for /ɪ/ – relax and make it short. Put your hand under your chin: with /iː/ your mouth is wider and more tense.")
SN_UA = ("В українській є один звук <b>і</b>, а в англійській – <b>два різні</b>, і вони змінюють значення: live (жити) – leave (йти, їхати); ship (корабель) – sheep (вівця); this (це) – these (ці).<br>"
         "<b>/ɪ/ – короткий і розслаблений</b>, трохи схожий на українське <b>и</b>: this, skill, live, ship.<br>"
         "<b>/iː/ – довгий і напружений</b>: усміхнись, губи розтягнуті, звук довгий, як «і-і»: these, team, leave, sheep.<br>"
         "<b>Як зрозуміти з написання:</b> ee, ea, ie, e + приголосна + e → довгий /iː/ (meeting, team, field, these). <b>i</b> + приголосна в кінці складу → короткий /ɪ/ (this, skill, fix, build). Винятки: police, machine.<br>"
         "<b>Порада:</b> для /iː/ – усміхнись і тягни; для /ɪ/ – розслабся і коротко.")
SND = [("ship", "sheep"), ("this", "these"), ("live", "leave"), ("fill", "feel"), ("fit", "feet"), ("sit", "seat"), ("still", "steal"), ("hit", "heat")]
import random
rnd = random.Random(11)
def pair_row(i, a, b):
    return ('<div class="row">%s) <button class="btn l" type="button" style="min-height:40px;padding:4px 12px" onclick="say(\'%s\')">🔊 %s</button> '
            '<button class="btn l" type="button" style="min-height:40px;padding:4px 12px" onclick="say(\'%s\')">🔊 %s</button></div>') % ("abcdefgh"[i], a, a, b, b)
snd = ""
for i, (a, b) in enumerate(SND):
    w = [a, b][rnd.randint(0, 1)]; k = "sn_%d" % (i + 1); K[k] = [w]
    snd += ('<div class="row">%s) <button class="btn l" type="button" style="min-height:40px;padding:4px 14px" onclick="say(\'%s\')">🔊 Listen</button> %s%s</div>'
            % ("abcdefgh"[i], w, sel(k, [a, b], 120), fb(k)))
SORTW = ["skill", "team", "these", "this", "meeting", "fix", "feedback", "build", "need", "think", "lead", "field", "quick", "leave", "live", "keep"]
rnd.shuffle(SORTW)
LONG = {"team", "these", "meeting", "feedback", "need", "lead", "field", "leave", "keep"}
sortr = ""
for i, w in enumerate(SORTW):
    k = "so_%d" % (i + 1); K[k] = ["long /iː/" if w in LONG else "short /ɪ/"]
    sortr += '<span style="display:inline-block;margin:4px 14px 4px 0"><b>%s</b> %s%s</span>' % (w, sel(k, ["short /ɪ/", "long /iː/"], 120), fb(k))
def yt(i):
    return ('<div style="width:100%%;max-width:600px;aspect-ratio:16/9;margin:8px 0"><iframe src="https://www.youtube-nocookie.com/embed/%s?rel=0&cc_load_policy=1" '
            'style="width:100%%;height:100%%;border:0;border-radius:12px" allow="encrypted-media; picture-in-picture" allowfullscreen loading="lazy"></iframe></div>') % i
s5 = ('<div class="bsec">Sounds <span class="sub">Short /ɪ/ or long /iː/?</span></div>' +
      rule("Two English sounds for one Ukrainian «і»", SN_EN, SN_UA) +
      '<p class="ins">' + X(5, "A") + '<b>Watch and repeat.</b> Pause the video and repeat every word and sentence after the speaker.</p>' +
      '<div class="card" style="background:#fbfbfd;margin-top:14px"><b>American English</b> – practice with Hadar, a pronunciation coach (English is not her first language either): <i>sheep – ship, leave – live</i>. You listen and repeat the pairs and then sentences with her.</div>' + yt("Xh-KHPHPVXg") +
      '<p class="hint">🇺🇦 Зупиняй відео й повторюй кожне слово та речення вголос.</p>' +
      '<p class="ins" style="margin-top:22px">' + X(5, "B") + '<b>Listen and compare.</b> Press each button. Watch your mouth in a mirror or your camera: relaxed and short – or smile and long?</p>' +
      "".join(pair_row(i, a, b) for i, (a, b) in enumerate(SND[:6])) +
      '<p class="ins" style="margin-top:22px">' + X(5, "C") + '<b>Hear the difference.</b> Listen and choose the word you hear.</p>' + snd + ctl("sn") +
      '<p class="ins" style="margin-top:22px">' + X(5, "D") + '<b>Use the spelling rule.</b> Words from our lesson – short or long? Use the spelling rule – no listening here.</p>' + sortr + ctl("so") +
      '<p class="ins" style="margin-top:22px">' + X(5, "E") + '<b>Say it.</b> Read these sentences aloud 3 times, slowly, then faster:</p>' +
      '<div class="card" style="background:#fbfbfd;line-height:1.9">1 <i>Th<b>i</b>s sk<b>i</b>ll is important. Th<b>e</b>se sk<b>i</b>lls are important.</i><br>2 <i>I l<b>i</b>ve in Kyiv. I l<b>ea</b>ve work at six.</i><br>'
      '3 <i>Our t<b>ea</b>m n<b>ee</b>ds a qu<b>i</b>ck f<b>i</b>x.</i><br>4 <i>I th<b>i</b>nk the f<b>ee</b>dback from the m<b>ee</b>ting is useful.</i></div>' +
      '<div class="card" style="margin-top:12px;background:#eef7ff;border-left:4px solid #2a9df4">📲 <b>Record sentences 1–4 as a voice message and send it to your teacher in Telegram.</b></div>' +
      '')

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
      '<div class="card" style="margin-top:12px;background:#eef7ff;border-left:4px solid #2a9df4">📲 <b>Record one clip (round ④) as a voice message and send it to your teacher in Telegram.</b></div>' +
      '<p class="ins" style="margin-top:22px">' + X(6, "D") + 'Write down 3 phrases you can now say <b>exactly like the speaker</b>.</p>' + ta("sh_ph", "1 …\n2 …\n3 …", 70))

# ---------- 7 4/3/2 ----------
s7 = ('<div class="bsec">Speaking <span class="sub">Say it again – cleaner (2 / 1.5 / 1) · create → evaluate</span></div>' +
      '<div class="card" style="background:#fff8d6;border-left:4px solid #e0a100">🧭 You tell the <b>same story three times</b>, each time faster: <b>2 minutes → 1.5 minutes → 1 minute</b>. Each time you make fewer mistakes and fewer pauses.<br>'
      '<span class="hint">🇺🇦 Одну й ту саму історію розповідаєш тричі, щоразу коротше: 2 хв → 1,5 хв → 1 хв. Щоразу чистіше.</span></div>' +
      '<p class="ins">' + X(7, "A") + 'Your topic: <b>“Thinking outside the box is my strongest skill.”</b> Why? Give a real example from work or life. Bonus: tell how you tried to solve the <b>nine dots puzzle</b> (<i>First I tried…, then I realised…</i>).</p>' +
      '<div class="card" style="background:#fbfbfd">✅ <b>My checklist before I speak:</b> <i>be</i> in every sentence? · <i>-s</i> with he/she/it? · <i>a / the</i> before nouns? · who → does what? · past = <i>didn’t / forgot / tried</i>?</div>' +
      '<div class="card" style="margin-top:12px;background:#fbfbfd">⏱ Use a timer: <button class="btn l" type="button" onclick="tmr(this,120)">2:00</button> <button class="btn l" type="button" onclick="tmr(this,90)">1:30</button> <button class="btn l" type="button" onclick="tmr(this,60)">1:00</button> <b class="tmv" style="font:600 20px monospace;margin-left:10px"></b></div>' +
      '<div class="card" style="margin-top:12px;background:#eef7ff;border-left:4px solid #2a9df4">📲 <b>Record round 1 and round 3 as voice messages and send them to your teacher in Telegram.</b></div>' +
      '<p class="ins" style="margin-top:22px">' + X(7, "B") + 'Listen to your round 1 and round 3. Which mistakes did you fix? Which mistakes are still there?</p>' +
      ta("r_ref", "In round 3 I fixed … I still say …", 80) +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you notice and fix your own mistakes now?"))

XJS = r"""const ECW=__ECW__;const ECT={};
function chkEC(p){let n=0,t=0;for(const k in KEY){if(k.replace(/_[^_]+$/,"")!==p)continue;const el=document.querySelector(`.g[data-k="${k}"]`);if(!el)continue;t++;const val=el.value.trim();const ok=!!val&&okv(k,val);if(ok)n++;else if(val)ECT[k]=(ECT[k]||0)+1;
 el.classList.remove("right","wrong");el.classList.add(ok?"right":"wrong");const w=ECW[k]||["",""];fbk(k,ok,ok?"✓ <b>Well done!</b> "+w[0]:(!val?"✗ Write your sentence first.":"✗ <b>Not yet.</b> "+w[1]+(ECT[k]>=2?"<br>👉 Correct: <b>"+KEY[k][0]+"</b>":"")))}$("r_"+p).textContent=n+" / "+t+(n===t?" ✓ Well done!":"");save()}
const _AU={};function say(w){let a=_AU[w];if(!a){a=_AU[w]=new Audio("audio/"+w+".mp3");a.preload="auto"}try{a.pause();a.currentTime=0}catch(e){}a.play().catch(()=>{try{const u=new SpeechSynthesisUtterance(w);u.lang="en-US";u.rate=.8;speechSynthesis.speak(u)}catch(e){}})}
let _tv=null;function tmr(b,t){clearInterval(_tv);const o=b.parentElement.querySelector(".tmv");let l=t;const sh=()=>o.textContent=Math.floor(l/60)+":"+String(l%60).padStart(2,"0");sh();_tv=setInterval(()=>{l--;sh();if(l<=0){clearInterval(_tv);o.textContent="⏰ Stop!"}},1000)}
"""
VOC = [("Clean English", ["I didn’t understand it.", "this week", "in a team", "what it is about", "I forgot", "I should think about it", "communication skills", "easier", "try to", "try -ing"]),
       ("Lesson words", ["a can-do attitude", "set goals", "determination", "integrity", "think outside the box", "critical thinking", "team player"])]
import json as _j
XJS = XJS.replace("__ECW__", _j.dumps(ECW, ensure_ascii=False))
html = page("1.1", "Transferable skills", "HOMEWORK · CLEAN YOUR ENGLISH", "Notice and fix your own mistakes; use articles, to/-ing and Simple vs Continuous correctly.",
            "BP B1 1.1 Transferable skills · Clean English", CODE,
            [("1", s2), ("2", s3), ("3", s4), ("4", s1), ("5", s5), ("6", s6), ("7", s7)], K, VOC, extra_js=XJS)
open(os.path.join(OUTDIR, "clean.html"), "w").write(html)
print("ok", OUTDIR)
