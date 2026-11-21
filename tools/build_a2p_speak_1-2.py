"""Business Partner A2+ · 1.2 Events management — SPEAKING: BUSINESS SITUATIONS (closes 1.2, no warm-up games).
Six real work situations with role cards; the student talks from minute one and must reach a result. Teacher = Student B
(B cards with hidden conditions are shown only in the template; on the student site they are removed).
1 Client meeting: plan the evening event · 2 Negotiate with the caterer · 3 Brief your assistant · 4 Problem: more guests than the venue takes
5 After the event: the client complains · 6 Your own business: brief an event agency · 7 Follow-up email + self-assessment
Usage: python3 build_a2p_speak_1-2.py OUT.html [STUDENT_CODE]
"""
import sys, os, re
from bp_page import page, ta, inp, SELF
from vocab_a2p import lesson
import vcard
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#3fa9ad", "#e6f4f4", "#2b8185", "#5cc1c4"
_, GROUPS = lesson("1.2")
VOC, VJS = vcard.build(GROUPS, ACC, ACC2, DARK)

def sit(n, title, task, card_a, card_b, phrases, key, ph):
    return ('<div class="bsec wr">Situation %d</div><p class="ins"><b class="x">%d</b><b>%s</b> %s</p>' % (n, n, title, task) +
            '<div class="rp"><div class="rh">🅰 You</div><ul>%s</ul></div>' % "".join("<li>%s</li>" % x for x in card_a) +
            '<details class="tch"><summary>🔒 Card B — for the teacher</summary><ul>%s</ul></details>' % "".join("<li>%s</li>" % x for x in card_b) +
            '<div class="ul">💬 %s</div>' % " · ".join("<i>%s</i>" % p for p in phrases) +
            '<p class="ins" style="margin-top:14px">📝 Result: what did you agree?</p>' + ta(key, ph, 60))

VEN = ('<table class="tb"><tr><th></th><th>Rooftop terrace<br><span>city centre</span></th><th>Winery<br><span>40 min by bus</span></th><th>Boat restaurant<br><span>old port</span></th></tr>'
       '<tr><td>Guests</td><td>up to 120</td><td>up to 80</td><td>up to 200</td></tr><tr><td>Food</td><td>tapas · €45 per person</td><td>Catalan menu + vegan · €70</td><td>paella (seafood / vegetable) · €90</td></tr>'
       '<tr><td>Entertainment</td><td>DJ</td><td>live guitar, wine tasting</td><td>jazz band</td></tr><tr><td>Free dates</td><td>Thu 14 or Fri 15 May</td><td>Fri 15 May only</td><td>Thu 14 May only</td></tr>'
       '<tr><td>Extra</td><td>no roof — weather!</td><td>bus €600</td><td>can stream the talks (hybrid)</td></tr></table>')
NOTES = [("venue", "Venue"), ("date", "Date"), ("guests", "Number of guests"), ("food", "Food (vegan / gluten-free?)"), ("ent", "Entertainment"), ("budget", "Budget"), ("next", "Next step")]
s1 = ('<div class="bsec wr">Situation 1</div><p class="ins"><b class="x">1</b><b>Client meeting.</b> You are an event manager at BCN Smart Events. The client (your teacher) has a two-day conference in Barcelona, 14–15 May, and needs an evening event. '
      'Get the information, compare the venues, recommend one and agree on the plan.</p>'
      '<div class="rp"><div class="rh">🅰 You — event manager</div><ul><li>Ask: number of guests, budget, special food, online guests.</li><li>Recommend one venue and explain why (<i>cheaper than, the best option for …</i>).</li>'
      '<li>You have a 10% discount at the winery — try to sell it.</li><li>Finish with a clear next step.</li></ul></div>' + VEN +
      '<details class="tch"><summary>🔒 Card B — for the teacher (client)</summary><ul><li>HR director of a law firm, Vega Legal. 140 guests, 25 join online.</li>'
      '<li>Budget about €8,000 for food + entertainment. 10 vegan, 4 gluten-free.</li><li>The CEO loves jazz; you think the boat is too expensive; you worry about rain on the rooftop.</li>'
      '<li>Ask: What happens if it rains? Is the price with drinks? Can online guests see the event?</li><li>Don’t agree too fast — make her give real arguments and numbers.</li></ul></details>'
      '<div class="ul">💬 <i>Let’s start with …</i> · <i>How many guests do you expect?</i> · <i>I recommend … because …</i> · <i>It’s cheaper / bigger than …</i> · <i>So, we agree on …</i></div>'
      '<p class="ins" style="margin-top:14px">📝 Meeting notes</p><div class="notes">' + "".join('<label>%s</label>%s' % (l, inp("n1_" + k, 420)) for k, l in NOTES) + '</div>')

s2 = sit(2, "Negotiate with the caterer.", "The boat restaurant’s caterer sent a quote: €95 per person for 140 guests (€13,300). Your client’s budget is €8,000. Call the caterer (your teacher) and get a better price.",
         ["Explain the budget and the number of guests.", "Ask what is in the price: drinks? service? the jazz band?", "Suggest ways to make it cheaper: a buffet, fewer courses, a shorter drinks package, a smaller band.",
          "Don’t accept the first offer. Your aim: €60 per person or less."],
         ["You start at €95, then €85. Your minimum is €62 per person.", "€62 is possible only with a buffet, house wine for 2 hours and a jazz duo, not the band.",
          "You want a 30% deposit by 1 May. Ask for it at the end."],
         ["Our budget is …", "What’s included in the price?", "That’s too expensive for us.", "How about a buffet?", "Can you do it for …?", "If we …, can you …?", "OK, it’s a deal."], "r2", "Price per person: … · What’s included: … · Deposit: …")

s3 = sit(3, "Brief your assistant.", "You have a 10-minute call with your new assistant (your teacher). The event is in three weeks. Explain what needs to be done, who does what and the deadlines.",
         ["Tasks: book the bus to the venue · send the guest list to the caterer · check the special menus (10 vegan, 4 gluten-free) · test the streaming for 25 online guests · print name badges.",
          "Give each task a deadline.", "Check that your assistant understands — ask him/her to repeat the plan."],
         ["You are new and a bit nervous. Ask questions: Which bus company? Who has the guest list? What do I do if the streaming doesn’t work?",
          "Say you can’t do the name badges by Friday — you’re on a training course.", "At the end, repeat the plan with one mistake — the student must correct you."],
         ["First, could you …?", "The deadline is …", "Please send … to …", "Let me check: …", "If you have a problem, call me.", "No, not Thursday — Friday."], "r3", "Tasks and deadlines: …")

s4 = sit(4, "A problem with the venue.", "Two weeks before the event the client now has 170 guests, not 140. The venue takes 120–140. Call the venue manager (your teacher) and find a solution.",
         ["Explain the problem clearly.", "Ask for options and compare them.", "You can’t pay more than €1,000 extra.", "Agree on a solution and on a date to confirm."],
         ["Option 1: the terrace next door, +50 guests, €1,500.", "Option 2: two sittings — 140 guests from 19:00, 30 more from 21:00 for the party.",
          "You need 2 more staff (€400). 10% discount if she confirms today."],
         ["We have a problem with …", "Is it possible to …?", "What are our options?", "That’s more than our budget.", "What’s the best you can do?", "Let’s agree on …"], "r4", "Solution: … · Extra cost: … · Confirm by: …")

s5 = sit(5, "After the event: the client complains.", "The day after the event the client (your teacher) calls you. She is not happy. Listen, apologise, explain and offer a solution — keep the client for next year.",
         ["Find out exactly what went wrong.", "Apologise and explain (only real reasons, no excuses).", "Offer something: a discount, a free extra next time, a refund for one part.",
          "Agree on the next step and ask about next year."],
         ["Complaints: dinner was 40 minutes late; online guests couldn’t hear the speakers for 20 minutes; there were not enough vegan dishes.",
          "Good things: the venue and the jazz were great.", "You want 20% back. Accept 10% + a free photographer next year if the student is professional."],
         ["I’m very sorry about …", "Can you tell me exactly what happened?", "The reason was …", "What we can do is …", "We’d like to offer …", "Can we work together next year?"], "r5", "What went wrong: … · Our offer: … · Next step: …")

s6 = sit(6, "Your own business.", "Now you are the client. Your company wants to organise an event for its clients (for example a seminar on new tax rules, an end-of-year evening or a team offsite). Brief an event agency (your teacher) with <b>real information</b> about your business.",
         ["Explain: who you are, what the event is for and who comes.", "Give the facts: date, number of guests, place (in person / online / hybrid), budget.",
          "Say what is most important for you and what you don’t want.", "Ask the agency for two options and a price by a date."],
         ["You work for an event agency. Ask follow-up questions: Why this event now? What does success look like? Who decides? What was the worst event you went to — and why?",
          "Push back on one thing: the budget is too small, or the date is too close.", "At the end, repeat her brief in 3 sentences — she corrects you if needed."],
         ["We are a … company.", "The aim of the event is to …", "We expect about … guests.", "Our budget is about …", "For us, the most important thing is …", "Could you send us two options by …?"], "r6", "My brief: …")

MODEL = ("Hi Ana,\nThank you for the meeting today. Let me confirm what we agreed:\n• Venue: the boat restaurant in the old port, Thursday 14 May, 19:00.\n• 140 guests (25 join online — we stream the talks).\n"
         "• Food: buffet, €62 per person, 10 vegan and 4 gluten-free menus.\n• Entertainment: a jazz duo.\nNext step: please confirm the final number of guests by 1 May.\nBest regards,\nLarysa")
s7 = ('<div class="bsec wr">After the meetings</div><p class="ins"><b class="x">7</b>Write a follow-up email to the client from Situation 1 (60–100 words). Confirm what you agreed — use your notes and the price from Situation 2.</p>'
      '<div class="ul">💬 <i>Thank you for the meeting today.</i> · <i>Let me confirm what we agreed: …</i> · <i>Next step: …</i> · <i>Best regards,</i></div>' +
      ta("w7", "Hi …, Thank you for the meeting today. Let me confirm what we agreed: …", 180) + '<p class="hint" id="w7c"></p>'
      '<button class="btn l" onclick="model(\'m7\')">Show a model email</button><div class="model" id="m7">%s</div>' % MODEL +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you plan an event, negotiate and solve problems in English?"))

XJS = VJS + r"""
document.head.insertAdjacentHTML("beforeend",`<style>
.rp{border:1.5px solid __ACC__;border-radius:10px;padding:10px 16px;margin:10px 0;background:#fff}.rh{font-weight:600;color:__DARK__;margin-bottom:4px}.rp ul,.tch ul{margin:4px 0;padding-left:20px}.rp li,.tch li{margin:3px 0}
.tch{background:#fff8e6;border:1px dashed #e0b43c;border-radius:10px;padding:8px 14px;margin:10px 0}.tch summary{cursor:pointer;font-weight:500}
.ul{background:__ACC2__;border-radius:8px;padding:8px 14px;font-size:15px;line-height:1.7}
table.tb{border-collapse:collapse;width:100%;margin:10px 0;font-size:15px}table.tb th,table.tb td{border:1px solid #c8c9cb;padding:6px 8px;text-align:center}table.tb th{background:__ACC2__;color:__DARK__}table.tb th span{font-weight:300;font-size:13px}table.tb td:first-child{text-align:left;font-weight:500}
.notes{display:grid;grid-template-columns:220px 1fr;gap:6px 12px;align-items:center;max-width:720px}.notes label{font-size:15px;color:#4d4d4f}@media(max-width:800px){.notes{grid-template-columns:1fr}}
</style>`);
function wc(){const t=document.querySelector('.g[data-k="w7"]');if(!t)return;const n=(t.value.trim().match(/\S+/g)||[]).length;document.getElementById("w7c").textContent=n+" words (aim: 60–100)"}
document.addEventListener("input",e=>{if(e.target.dataset&&e.target.dataset.k==="w7")wc()});window.afterFill=wc;
""".replace("__ACC2__", ACC2).replace("__ACC__", ACC).replace("__DARK__", DARK)
h = page("1.2", "Events management", "SPEAKING · BUSINESS SITUATIONS", "Use the 1.2 vocabulary in real work situations: plan, negotiate, brief, solve problems, handle a complaint.",
         "BP A2+ 1.2 Events · Speaking", CODE, [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5), ("6", s6), ("7", s7)], {}, VOC,
         acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, footer="Speaking lesson to close 1.2. Teacher = Student B. ", extra_js=XJS)
if CODE:
    h = re.sub(r'<details class="tch">.*?</details>', '', h, flags=re.S)
os.makedirs(os.path.dirname(OUT), exist_ok=True); open(OUT, "w").write(h); print("ok", OUT, len(h))
