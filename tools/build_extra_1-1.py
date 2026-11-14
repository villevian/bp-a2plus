import json
css = open('/home/claude/pasha72/base.css').read().replace('--coral:#e8605a', '--coral:#3fa9ad') + """
:root{--gold:#f2b631}
.back{display:inline-block;margin:12px 22px 0;color:var(--coral);font-weight:500;text-decoration:none;font-size:15px}
.ex{margin:26px 0 0}
.ex .q{display:flex;gap:10px;align-items:baseline;font-weight:500;font-size:17px;margin-bottom:10px;line-height:1.35}
.ex .q .n{color:var(--coral);font-weight:600;font-size:24px;min-width:30px}
.ex .q small{display:block;font-weight:400;color:var(--grey);font-size:14px;margin-top:2px}
.flash{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px;margin-left:40px}
.fc{height:118px;perspective:800px;cursor:pointer}
.fc .in{position:relative;width:100%;height:100%;transition:transform .45s;transform-style:preserve-3d}
.fc.flip .in{transform:rotateY(180deg)}
.fc .f,.fc .b{position:absolute;inset:0;backface-visibility:hidden;border-radius:6px;padding:12px;display:flex;flex-direction:column;justify-content:center;text-align:center}
.fc .f{background:var(--lg);border-left:4px solid var(--coral);font-size:14.5px;line-height:1.35}
.fc .f small{color:var(--grey);font-size:11px;margin-top:6px}
.fc .b{background:#e6f4f4;transform:rotateY(180deg);font-weight:600;font-size:17px}
.fc .b i{font-weight:400;font-size:13px;color:#2a7fa8;margin-top:6px}
.fc.adv .f{border-left-color:var(--gold);background:#fdf7e6}
.fc.adv .b{background:#fdf0d5}
.row{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 0 40px;align-items:center}
ol.it{list-style:none;padding:0;margin:0 0 0 40px}
ol.it>li{display:flex;gap:10px;margin-bottom:10px;font-size:16px;line-height:1.5}
ol.it>li>.i{font-weight:600;min-width:18px}
ol.it>li>.t{flex:1}
select,.g{font:inherit;font-size:15px}
select{padding:3px 6px;border:1.5px solid #c9cacc;border-radius:4px;background:#fff}
.g{border:0;border-bottom:1.5px solid var(--ink);padding:1px 4px;width:150px;background:#fff}
.g.wide{width:min(560px,100%)}
.right{border-color:#2e7d32!important;background:#eef7ea!important}.wrong{border-color:#c0392b!important;background:#fdecea!important}
.chk{margin:8px 0 0 40px;display:flex;gap:10px;align-items:center}
.chk button{font:inherit;font-weight:500;border:0;padding:8px 14px;border-radius:4px;cursor:pointer;background:var(--coral);color:#fff}
.chk button.l{background:#fff;color:#4d4d4f;border:1px solid #a7a9ac}
.chk span{font-size:14px;color:var(--grey)}
.fb{display:none;margin:4px 0 2px;padding:7px 10px;border-radius:4px;font-size:14px;line-height:1.45}
.fb.show{display:block}.fb.ok{background:#eef7ea;border-left:3px solid #2e7d32}.fb.no{background:#fdecea;border-left:3px solid #c0392b}
.fb .h{font-weight:600;margin-bottom:3px}.fb .ua{color:#555;margin-top:3px}.fb .ua:before{content:"🇺🇦 "}.fb .en:before{content:"🇬🇧 "}
.msg{margin-left:40px;max-width:620px}
.bubble{background:#f4f4f5;border-radius:10px;padding:10px 12px;font-size:15px;margin-bottom:8px}
.bubble b{font-weight:600;display:block;font-size:13px;color:#4a154b;margin-bottom:2px}
textarea{font:inherit;font-size:15px;width:100%;min-height:80px;padding:8px 10px;border:1px solid #c9cacc;border-radius:4px}
.model{display:none;margin-top:6px;background:#e6f4f4;padding:8px 12px;border-radius:4px;font-size:14.5px}
.model.show{display:block}
.sec-h{color:var(--grey);font-weight:500;font-size:20px;margin:34px 0 -8px;padding-top:12px;border-top:1px solid #e3e4e5}
"""

FL = [("an arrangement to keep a hotel room for you", "reservation", "make a reservation", 0),
      ("a journey by plane", "flight", "take / catch a flight", 0),
      ("a car, van or bus", "vehicle", "hire a vehicle", 0),
      ("an app to order a car with a driver", "ridesharing app", "use a ridesharing app", 0),
      ("the door where you get on the plane", "gate", "at gate 12", 0),
      ("the time you spend in a hotel", "stay", "a comfortable stay", 0),
      ("a room where you wait for your flight", "lounge", "the departure lounge", 0),
      ("where something is", "location", "a great location", 0),
      ("buses, trains and the metro", "public transportation", "take public transportation", 0),
      ("to or in another country", "abroad", "go abroad", 0),
      ("late because of a problem", "delayed", "delayed by two hours", 0),
      ("the action of leaving", "departure", "departure time", 0),
      ("a short stop between two flights", "layover", "a layover in Vienna", 1),
      ("a night flight that arrives in the morning", "red-eye", "take the red-eye", 1),
      ("a small bag you take on the plane", "carry-on", "one carry-on only", 1),
      ("the plan of your trip", "itinerary", "send the itinerary", 1),
      ("money per day for food on a trip", "per diem", "a $60 per diem", 1),
      ("to pay back money you spent", "reimburse", "reimburse expenses", 1),
      ("tiredness after a flight across time zones", "jet lag", "I’m jet-lagged", 1),
      ("the document to get on the plane", "boarding pass", "show your boarding pass", 1)]

COL = [("___ a reservation", ["make", "do", "take"], "make", "We say <b>make a reservation</b> (= book). <i>Do</i> is for tasks/activities: do the shopping.", "Кажемо <b>make a reservation</b>. <i>Do</i> — для дій/справ: do the shopping."),
       ("___ a flight (= get on it in time)", ["catch", "take up", "hold"], "catch", "<b>catch a flight</b> = get to it in time. The opposite is <b>miss a flight</b>.", "<b>catch a flight</b> = встигнути на рейс. Протилежне — <b>miss a flight</b>."),
       ("___ a car for a week", ["hire / rent", "lend", "borrow"], "hire / rent", "<b>hire / rent a car</b> = pay to use it. <i>Borrow</i> is free, from a friend.", "<b>hire / rent a car</b> — орендувати за гроші. <i>Borrow</i> — позичити безкоштовно."),
       ("___ at the hotel at 3 pm", ["check in", "check up", "check on"], "check in", "<b>check in</b> = register when you arrive; <b>check out</b> = leave and pay.", "<b>check in</b> — заселитися; <b>check out</b> — виселитися й розрахуватися."),
       ("___ an expense report", ["submit", "send up", "give in to"], "submit", "<b>submit an expense report</b> = officially give it to the company.", "<b>submit an expense report</b> — подати звіт про витрати."),
       ("___ the plane", ["board", "enter in", "go on to"], "board", "<b>board the plane</b> = get on the plane. Boarding pass = the document for this.", "<b>board the plane</b> — сісти в літак. Звідси boarding pass.")]

PREP = [("My flight was delayed ___ two hours.", ["by", "on", "for"], "by", "Use <b>by</b> for the size of a change: delayed by two hours, prices went up by 5%.", "<b>by</b> показує, на скільки щось змінилося: delayed by two hours."),
        ("I’ll meet you ___ the gate.", ["at", "on", "in"], "at", "<b>at</b> for a point/place where you meet: at the gate, at the reception.", "<b>at</b> — для точки/місця зустрічі: at the gate."),
        ("I go ___ twice a year for work.", ["abroad", "to abroad", "in abroad"], "abroad", "<b>abroad</b> is an adverb — no preposition: go abroad, live abroad.", "<b>abroad</b> — прислівник, без прийменника: go abroad."),
        ("We stayed ___ a business hotel.", ["at", "on", "by"], "at", "<b>stay at</b> a hotel (also <i>in</i> a hotel). Never <i>on</i>.", "<b>stay at</b> a hotel (можна <i>in</i>). Ніколи не <i>on</i>."),
        ("We arrived ___ Berlin late at night.", ["in", "at", "to"], "in", "<b>arrive in</b> a city/country, <b>arrive at</b> a building/airport. Never <i>arrive to</i>.", "<b>arrive in</b> місто/країна, <b>arrive at</b> будівля/аеропорт. Не <i>arrive to</i>."),
        ("It’s quicker to go ___ train.", ["by", "with", "on the"], "by", "<b>by</b> + transport without article: by train, by plane, by taxi. But <i>on foot</i>.", "<b>by</b> + транспорт без артикля: by train. Але <i>on foot</i>.")]

ERR = [("I did a reservation for two nights.", ["made a reservation"], "made a reservation", "make, not do, with reservation.", "З reservation — make, а не do."),
       ("The flight was late on two hours.", ["delayed by two hours", "late by two hours", "two hours late"], "delayed by two hours / two hours late", "Use <b>by</b> or the structure <i>two hours late</i>.", "Потрібно <b>by</b> або <i>two hours late</i>."),
       ("Public transportations is cheap here.", ["public transportation is cheap here"], "Public transportation is cheap here.", "<i>Transportation</i> is uncountable — no -s.", "<i>Transportation</i> незлічуване — без -s."),
       ("We arrived to the airport at 6.", ["arrived at the airport"], "arrived at the airport", "<b>arrive at</b> (airport, office), <b>arrive in</b> (city).", "<b>arrive at</b> (аеропорт), <b>arrive in</b> (місто)."),
       ("I travel to abroad a lot.", ["travel abroad"], "travel abroad", "No <i>to</i> before abroad.", "Перед abroad немає <i>to</i>."),
       ("The flight was very bored.", ["very boring", "the flight was very boring"], "very boring", "<b>-ing</b> describes the thing (boring flight); <b>-ed</b> describes how you feel (I was bored).", "<b>-ing</b> — про річ (boring flight), <b>-ed</b> — про почуття людини (I was bored).")]

SLACK = [("Your flight to Warsaw is delayed by 3 hours. You’ll miss the 11 am client meeting. Write to your team chat.",
          "Hi team, my flight is delayed by three hours, so I’ll miss the 11 am meeting with the client. Can someone start without me? I’ll join online if I can. Sorry!"),
         ("A colleague asks: “Where should I stay in your city?” Reply in 2–3 sentences.",
          "I’d recommend the City Hotel — it’s quiet and in a great location, near the office. You can take public transportation from the airport, or use a ridesharing app."),
         ("The hotel lost your reservation. Write to your manager and ask what to do.",
          "Hi Anna, the hotel can’t find my reservation and there are no free rooms. Can I book another hotel nearby? It’s about €20 more per night. Please let me know.")]


def fb(k, en, ua):
    return f'<div class="fb" id="fb_{k}"><div class="h"></div><div class="en">{en}</div><div class="ua">{ua}</div></div>'


def mc_block(key, items):
    out = '<ol class="it">'
    for i, (s, opts, ans, en, ua) in enumerate(items, 1):
        sel = f'<select data-k="{key}{i}" data-a="{ans}"><option value="">–</option>' + "".join(f'<option>{o}</option>' for o in opts) + '</select>'
        out += f'<li><span class="i">{i}</span><span class="t">{s.replace("___", sel)}{fb(f"{key}{i}", en, ua)}</span></li>'
    return out + '</ol>'


flash = "".join(f'<div class="fc{" adv" if a else ""}" onclick="this.classList.toggle(\'flip\')"><div class="in"><div class="f">{d}<small>{"★ next level · " if a else ""}tap to flip</small></div><div class="b">{w}<i>{c}</i></div></div></div>' for d, w, c, a in FL)
err = '<ol class="it">' + "".join(
    f'<li><span class="i">{i}</span><span class="t"><s style="color:#c0392b">{s}</s><br><input class="g wide" data-k="er{i}" data-a=\'{json.dumps(acc)}\' data-show="{show}" placeholder="Write the correct version">{fb(f"er{i}", en, ua)}</span></li>'
    for i, (s, acc, show, en, ua) in enumerate(ERR, 1)) + '</ol>'
slack = "".join(f'<div class="msg"><div class="bubble"><b>Task {i}</b>{t}</div><textarea placeholder="Write your message…"></textarea><div class="chk" style="margin-left:0"><button class="l" onclick="this.parentNode.nextElementSibling.classList.toggle(\'show\')">Show a model answer</button></div><div class="model"><b>Model:</b> {m}</div></div><br>' for i, (t, m) in enumerate(SLACK, 1))

html = f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>1.1 Business travel — Extra materials</title>
<link href="https://fonts.googleapis.com/css2?family=Fira+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>{css}</style></head><body>
<header><div class="n">1.1</div><h1>Business travel</h1><div class="t">EXTRA</div></header>
<a class="back" href="../../../index.html">← Contents</a>
<main>
<p class="ins" style="margin-top:14px"><b>★</b>Extra practice for Lesson 1.1. Do as much as you want — check your answers yourself.</p>

<div class="sec-h">Vocabulary</div>
<div class="ex"><div class="q"><span class="n">1</span><span>Flashcards. Read the explanation, say the word, then tap the card to check.<small>Gold cards = next level words.</small></span></div>
 <div class="flash">{flash}</div></div>

<div class="ex"><div class="q"><span class="n">2</span><span>Collocations. Choose the verb that goes with the noun.</span></div>
 {mc_block("co", COL)}
 <div class="chk"><button onclick="chkSel('co')">Check</button><span id="r_co"></span></div></div>

<div class="sec-h">Grammar & accuracy</div>
<div class="ex"><div class="q"><span class="n">3</span><span>Prepositions. Choose the correct option.</span></div>
 {mc_block("pr", PREP)}
 <div class="chk"><button onclick="chkSel('pr')">Check</button><span id="r_pr"></span></div></div>

<div class="ex"><div class="q"><span class="n">4</span><span>Find and fix the mistake. Write the correct sentence or the correct part.</span></div>
 {err}
 <div class="chk"><button onclick="chkErr()">Check</button><span id="r_er"></span></div></div>

<div class="sec-h">Writing for real life</div>
<div class="ex"><div class="q"><span class="n">5</span><span>Write a short chat message (Slack / Telegram / Teams). Then compare with the model.</span></div>
 {slack}</div>
</main>
<script>
const norm=s=>s.trim().toLowerCase().replace(/[.!?]$/,"").replace(/\\s+/g," ");
function show(k,ok,ans){{const f=document.getElementById("fb_"+k);f.className="fb show "+(ok?"ok":"no");f.querySelector(".h").innerHTML=ok?"✓ Correct! / Правильно!":"✗ Correct answer / Правильна відповідь: <b>"+ans+"</b>"}}
function chkSel(p){{let n=0,t=0;document.querySelectorAll(`select[data-k^="${{p}}"]`).forEach(s=>{{t++;const ok=s.value===s.dataset.a;if(ok)n++;s.classList.remove("right","wrong");s.classList.add(ok?"right":"wrong");show(s.dataset.k,ok,s.dataset.a)}});document.getElementById("r_"+p).textContent=n+" / "+t+" correct"}}
function chkErr(){{let n=0,t=0;document.querySelectorAll('input[data-k^="er"]').forEach(i=>{{t++;const acc=JSON.parse(i.dataset.a);const v=norm(i.value);const ok=v&&acc.some(a=>v.includes(norm(a)));if(ok)n++;i.classList.remove("right","wrong");i.classList.add(ok?"right":"wrong");show(i.dataset.k,ok,i.dataset.show)}});document.getElementById("r_er").textContent=n+" / "+t+" correct"}}
</script></body></html>'''
open('/home/claude/extra11/extra.html', 'w').write(html)
