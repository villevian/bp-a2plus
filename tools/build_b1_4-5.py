"""Business Partner B1 · 4.5 Writing — Updated (order confirmation in Slack Connect / CRM) + Classic (letter confirming an order).
Usage: python3 build_b1_4-5.py LESSONDIR [STUDENT_CODE]  -> LESSONDIR/all/lesson.html (Updated), LESSONDIR/all-classic/lesson.html (Classic)
"""
import sys, os
from bp_page import page, fb, sel, inp, ta, ctl, radios, SELF
ROOT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
FUNCS = ["Greeting", "Opening", "Order details", "Delivery details", "Payment terms", "Enclosures", "Ending", "Closing"]
ORDER = ('<div class="ordf"><div class="oh">ORDER FORM · Gadget Office Supplies</div><table>'
         '<tr><td>Order no.</td><td><b>WT3488</b></td></tr><tr><td>Customer</td><td>Ms Mei Liang, Purchasing Manager, Lynx Logistics</td></tr>'
         '<tr><td>Product</td><td>100 × PR765 printers</td></tr><tr><td>Unit price</td><td>€230</td></tr>'
         '<tr><td>Discount</td><td>8% for orders over 80 units <span class="hw">✍ agreed at our meeting last week!</span></td></tr>'
         '<tr><td>Delivery</td><td>5 May · warehouse, Felton Business Park</td></tr><tr><td>Payment</td><td>30 days after the date of the invoice</td></tr>'
         '<tr><td>Notes</td><td><span class="hw">✍ order received this morning · send our terms & conditions · thank her, hope for more orders</span></td></tr></table></div>')
VP = ('<div class="gbox"><div class="gh">Verbs + prepositions (from the letter)</div><p>write <b>to</b> sb · confirm sth · talk <b>about</b> sth · pay <b>for</b> sth · deliver <b>to</b> a place · thank sb <b>for</b> sth · look forward <b>to</b> + -ing · apply <b>for</b> · agree <b>on</b> a price</p></div>')
CSS = ('const st=document.createElement("style");st.textContent=".letter{background:#fbfbf8;border:1px solid #ddd;box-shadow:2px 2px 0 #e6e6e6;padding:16px 22px;font-family:Georgia,serif;font-size:16px;line-height:2.1;max-width:780px}.letter input{font-family:Georgia,serif}'
       '.ordf{border:1.5px solid #c8c9cb;border-radius:6px;max-width:640px;margin:10px 0}.ordf .oh{background:#eef0f2;padding:6px 12px;font-weight:600}.ordf table{border-collapse:collapse;width:100%;font-size:15.5px}.ordf td{border-top:1px solid #e3e3e3;padding:5px 12px;vertical-align:top}.ordf td:first-child{width:120px;color:#6d6e70}'
       '.hw{font-family:\'Comic Sans MS\',\'Segoe Print\',cursive;color:#1f4fa8;font-size:14.5px}.chat{border:1px solid #ddd;border-radius:8px;padding:12px 16px;max-width:760px;background:#fff;line-height:2.1}.chat .who{font-weight:600}.chat .tm{color:#8a8b8d;font-size:13px;margin-left:6px}.chat .ch{color:#8a8b8d;font-size:13px;margin-bottom:6px}'
       '.chk2 span{display:inline-block;background:#f3f4f5;border-radius:14px;padding:3px 10px;margin:3px;font-size:14.5px}.chk2 span.on{background:#d9f2e2;color:#1e6b3d}";document.head.appendChild(st);')
def counter_js(field, lo, hi, pats):
    return (r"""(function(){const P=%s;const f=document.querySelector('[data-k=%s]');const ch=document.getElementById('chk_%s');const wc=document.getElementById('wc_%s');
ch.innerHTML=P.map(p=>'<span>'+p[0]+'</span>').join('');function u(){const v=(f.value||'').toLowerCase().replace(/[’]/g,"'");const n=(v.match(/\S+/g)||[]).length;let k=0;
[...ch.children].forEach((s,i)=>{const on=P[i][1].some(x=>v.includes(x));s.classList.toggle('on',on);if(on)k++});wc.textContent=n+' words (%d–%d) · '+k+' / '+P.length+' parts of the message'+(n>=%d&&n<=%d&&k>=P.length-1?' ✓':'')}
f.addEventListener('input',u);const old=window.afterFill;window.afterFill=()=>{if(old)old();u()};u()})();""" % (pats, field, field, field, lo, hi, lo, hi))

# ======================= CLASSIC =======================
K = {}
L1 = ["order", "received", "agreed", "Payment", "enclose", "thank", "hesitate", "sincerely"]
for i, a in enumerate(L1): K["c1_%d" % (i + 1)] = [a]
g = lambda n, w=120: '<sup>%d</sup>%s' % (n, inp("c1_%d" % n, w))
letter = ('<div class="letter">Dear Mr Chahal,<br>ORDER CONFIRMATION<br>We <b>are writing to</b> you to confirm your %s number 674190 for 1,000 123/XC units a week for 12 weeks, which we %s this morning.<br>'
          'As %s at the meeting last week when we <b>talked about</b> your order, I confirm that we will deliver the goods to your factory in Mumbai every week for a twelve-week period at a price of $4.40 per unit. '
          'Last week we discussed a discount of 10 percent providing you <b>pay for</b> the goods on time. You will be pleased to know that this is included in the final price of $4,000 per month. We also confirm that the first delivery will be on 05/11.<br>'
          '%s terms are $4,000 monthly, 30 days after the date of the invoice and we %s full terms and conditions for your records.<br>'
          'We %s you for your business and look forward to working with you. If you have any queries, please do not %s to contact us.<br>Yours %s,</div>') % tuple(g(i + 1) for i in range(8))
c1 = ('<div class="bsec">Lead-in</div><p class="ins"><b class="x">1</b>Read the order confirmation letter and complete it with the words in the box.</p><div class="box">agreed · enclose · hesitate · order · payment · received · sincerely · thank</div>' +
      letter + "".join(fb("c1_%d" % (i + 1)).replace('<span class="h">', '<sup>%d</sup> <span class="h">' % (i + 1)) for i in range(8)) + ctl("c1"))
T2 = [("Dear Sir/Madam,", 0), ("We are writing to you to confirm your order", 1), ("this is to confirm your order", 1), ("we are pleased to confirm your order", 1),
      ("order number 674190 for 1,000 123/XC units a week for 12 weeks", 2), ("order number 01 for five chairs", 2),
      ("we will deliver the goods to your factory in Mumbai", 3), ("the first delivery will be on 05/11", 3), ("we will deliver the goods to your head office", 3),
      ("Payment terms are $4,000 monthly, 30 days after the date of the invoice", 4), ("cash on delivery", 4), ("payment in advance", 4),
      ("We enclose full terms and conditions for your records.", 5), ("details of our new range are enclosed", 5),
      ("We thank you for your business and look forward to working with you.", 6), ("If you have any queries, please do not hesitate to contact us.", 6), ("we look forward to supplying you again in the future", 6),
      ("Yours sincerely,", 7), ("Yours faithfully,", 7)]
for i, (p, f) in enumerate(T2): K["c2_%d" % (i + 1)] = [FUNCS[f]]
c2 = ('<div class="bsec">Functional language</div><p class="ins"><b class="x">2</b>Complete the table with phrases or sentences from the letter, then add the phrases in the box to the table. Choose the function for each phrase.</p>'
      '<div class="row"><i>Dear Mr Chahal,</i> → <b>Greeting</b> (example)</div>' +
      "".join('<div class="row"><span style="display:inline-block;min-width:520px">%s</span>%s%s</div>' % (p, sel("c2_%d" % (i + 1), FUNCS, 170), fb("c2_%d" % (i + 1))) for i, (p, f) in enumerate(T2)) + ctl("c2") +
      '<div class="gbox"><div class="gh">Remember</div><p><b>Dear Mr / Ms + surname</b> → <b>Yours sincerely</b> · <b>Dear Sir/Madam</b> (no name) → <b>Yours faithfully</b></p><p><b>enclose</b> = put in the same envelope (letter) · <b>attach</b> = send with an email</p></div>' + VP)
BAD = ('<div class="letter" style="line-height:1.7">Hi Ms Liang!<br>Thanks a lot for the order, we got it. The printers will come to you soon. Like we said, there is a discount. '
       'You can pay us later when you get the bill. I put some papers in with this letter. Any problems just call me.<br>Cheers,<br>Tom</div>')
c3 = ('<div class="bsec wr">TASK</div><p class="ins"><b class="x">3</b><b>A</b> Read the letter. In pairs, discuss how you could improve it.</p>' + BAD + ta("c3a", "1 The greeting is too informal → Dear Ms Liang, …\n2 …", 100) +
      '<button class="btn l" onclick="model(\'m3a\')" style="margin-top:6px">Show ideas</button><div class="model" id="m3a">• Too informal: <i>Hi … ! / Thanks a lot / Cheers</i> → <i>Dear Ms Liang, / We thank you for your business / Yours sincerely</i><br>'
      '• No order number, product, quantity or price.<br>• No delivery date or place (<i>soon, to you</i>).<br>• Discount not specified (8% for orders over 80 units).<br>• Payment terms unclear (<i>later</i> → 30 days after the date of the invoice).<br>'
      '• <i>some papers</i> → We enclose our terms and conditions for your records.<br>• <i>Any problems just call me</i> → If you have any queries, please do not hesitate to contact us.</div>' +
      '<p class="ins"><b>B</b> Look at the order form and handwritten notes. Write an order confirmation letter to Ms Liang in around 150 words.</p>' + ORDER +
      ta("c3b", "Dear Ms Liang,\n…", 230) + '<div class="res" id="wc_c3b"></div><div class="chk2" id="chk_c3b"></div>' +
      '<button class="btn l" onclick="model(\'m3b\')" style="margin-top:8px">Show model answer</button><div class="model" id="m3b">Dear Ms Liang,\n\nWe are writing to confirm your order number WT3488 for 100 PR765 printers, which we received this morning. The unit price of the printers is €230. I am pleased to confirm that, as we agreed at our meeting last week, there is a discount of 8 percent for any orders over 80 units. We will deliver the goods to your warehouse in Felton Business Park on 5 May.\n\nWe confirm that our payment terms are 30 days after the date of the invoice. We enclose our business terms and conditions for your records.\n\nWe thank you for your business and look forward to supplying you again in the future. If you have any queries, please do not hesitate to contact us.\n\nYours sincerely,</div>' +
      '<p class="ins"><b>C</b> Exchange letters with your partner. Did your partner use different language from you? How many phrases from the functional language box did your partner use?</p>' + ta("c3c", "", 60) +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How successfully have you achieved the lesson outcome?"))
PAT_L = '[["Greeting",["dear ms liang","dear sir"]],["Opening",["confirm your order","writing to confirm","pleased to confirm"]],["Order details",["wt3488","pr765"]],["Delivery",["deliver","delivery"]],["Payment terms",["payment","30 days","invoice"]],["Enclosures",["enclose"]],["Ending",["thank you for","look forward","hesitate"]],["Closing",["yours sincerely","yours faithfully"]]]'
VOC_C = [("Order confirmation", ["confirm an order", "order number", "unit / unit price", "discount", "deliver the goods", "first delivery", "payment terms", "invoice", "terms and conditions", "cash on delivery", "payment in advance", "queries"]),
         ("Letter phrases", ["We are writing to confirm …", "We are pleased to confirm …", "As agreed …", "We enclose …", "We thank you for your business.", "We look forward to …", "Please do not hesitate to contact us.", "Yours sincerely / faithfully"]),
         ("Verbs + prepositions", ["write to", "talk about", "pay for", "deliver to", "thank sb for", "look forward to"])]
os.makedirs(os.path.join(ROOT, "all-classic"), exist_ok=True)
open(os.path.join(ROOT, "all-classic", "lesson.html"), "w").write(page("4.5", "Letter confirming an order", "WRITING · CLASSIC", "Learners can write an order confirmation letter.",
    "BP B1 4.5 Confirming an order · Classic", CODE, [("1", c1), ("2", c2), ("3", c3)], K, VOC_C, extra_js=CSS + counter_js("c3b", 130, 170, PAT_L)))

# ======================= UPDATED =======================
K = {}
U1 = ["order", "received", "agreed", "Payment", "attached", "Thanks", "hesitate", "regards"]
for i, a in enumerate(U1): K["u1_%d" % (i + 1)] = [a]
h = lambda n, w=115: '<sup>%d</sup>%s' % (n, inp("u1_%d" % n, w))
chat = ('<div class="chat"><div class="ch"># gadget-x-mumbai-steel · Slack Connect</div><span class="who">Anna Kowalska</span><span class="tm">10:42</span><br>'
        'Hi Mr Chahal 👋 Quick confirmation of your %s #674190 — %s this morning ✅<br>'
        'As %s on our call last week:<br>• 1,000 × 123/XC units a week for 12 weeks<br>• delivery every Monday to your factory in Mumbai, first delivery 5 Nov<br>• $4.40/unit incl. the 10%% discount for payment on time → <b>$4,000/month</b><br>'
        '%s terms: 30 days after the invoice date. Our T&amp;Cs are %s 📎<br>%s for your business! If anything is unclear, don’t %s to message me here.<br>Best %s,<br>Anna</div>') % tuple(h(i + 1) for i in range(8))
u1 = ('<div class="bsec">Lead-in</div><p class="ins"><b class="x">1</b>Read the order confirmation message in a shared Slack channel with a client and complete it with the words in the box.</p><div class="box">agreed · attached · hesitate · order · payment · received · regards · thanks</div>' +
      chat + "".join(fb("u1_%d" % (i + 1)).replace('<span class="h">', '<sup>%d</sup> <span class="h">' % (i + 1)) for i in range(8)) + ctl("u1") +
      '<p class="hint">💡 <b>Slack Connect</b> = a channel shared with people from another company (client, supplier). Many teams also send confirmations from a CRM (HubSpot, Salesforce) as a short email template.</p>')
T2U = [("Hi Mr Chahal 👋", 0), ("Hi team,", 0), ("Quick confirmation of your order #674190", 1), ("Just confirming your order — received this morning ✅", 1),
       ("1,000 × 123/XC units a week for 12 weeks", 2), ("Order #01: 5 chairs", 2), ("delivery every Monday to your factory in Mumbai", 3), ("ETA: 5 May, warehouse, Felton Business Park", 3),
       ("Payment terms: 30 days after the invoice date", 4), ("paid by card on delivery", 4), ("Our T&Cs are attached 📎", 5), ("The invoice is in the thread 🧵", 5),
       ("Thanks for your business!", 6), ("If anything is unclear, don’t hesitate to message me here.", 6), ("Best regards,", 7), ("Cheers,", 7)]
for i, (p, f) in enumerate(T2U): K["u2_%d" % (i + 1)] = [FUNCS[f]]
u2 = ('<div class="bsec">Functional language</div><p class="ins"><b class="x">2</b>Which part of the message is it? Choose the function for each phrase.</p>' +
      "".join('<div class="row"><span style="display:inline-block;min-width:480px">%s</span>%s%s</div>' % (p, sel("u2_%d" % (i + 1), FUNCS, 170), fb("u2_%d" % (i + 1))) for i, (p, f) in enumerate(T2U)) + ctl("u2") +
      '<div class="gbox"><div class="gh">Letter → chat: what changes?</div><table class="tt2" style="border-collapse:collapse;font-size:15px">'
      + "".join('<tr><td style="padding:3px 14px 3px 0"><b>%s</b></td><td style="padding:3px 14px 3px 0">%s</td><td>%s</td></tr>' % r for r in [
          ("Greeting", "Dear Mr Chahal,", "Hi Mr Chahal 👋 / Hi Mei"), ("Opening", "We are writing to confirm your order …", "Quick confirmation of your order #…"),
          ("Details", "long sentences", "short lines, bullet points, numbers in bold"), ("Enclosures", "We enclose …", "… attached 📎 / in the thread 🧵"),
          ("Ending", "Please do not hesitate to contact us.", "Don’t hesitate to message me here."), ("Closing", "Yours sincerely,", "Best regards, / Thanks,")]) +
      '</table><p style="margin-top:8px">Still professional: full information, correct numbers, no slang, max 1–2 emoji. With a new client — <i>Mr / Ms + surname</i>; with a client you know well — first name.</p></div>' + VP)
BADU = ('<div class="chat"><div class="ch"># gadget-x-lynx-logistics · Slack Connect</div><span class="who">Tom</span><span class="tm">16:05</span><br>hey!! got ur order 👍👍 printers coming soon 🚚 discount is ok like we said. pay whenever. sending some docs. ping me if smth lol</div>')
u3 = ('<div class="bsec wr">TASK</div><p class="ins"><b class="x">3</b><b>A</b> Read the message. In pairs, discuss how you could improve it.</p>' + BADU + ta("u3a", "1 … is too informal → …\n2 …", 100) +
      '<button class="btn l" onclick="model(\'m3a\')" style="margin-top:6px">Show ideas</button><div class="model" id="m3a">• Too informal for a client: <i>hey!!, ur, lol, smth</i>, too many emoji.<br>• No order number, product, quantity or price.<br>• <i>coming soon</i> → exact date and place.<br>• <i>discount is ok</i> → 8% for orders over 80 units.<br>• <i>pay whenever</i> → payment terms: 30 days after the invoice date.<br>• <i>some docs</i> → Our T&amp;Cs are attached 📎.<br>• Ending: <i>Thanks for your business! If anything is unclear, don’t hesitate to message me here.</i></div>' +
      '<p class="ins"><b>B</b> Look at the order form and handwritten notes. Write an order confirmation message to Ms Liang in your shared Slack channel (60–90 words).</p>' + ORDER +
      ta("u3b", "Hi Ms Liang 👋 …", 200) + '<div class="res" id="wc_u3b"></div><div class="chk2" id="chk_u3b"></div>' +
      '<button class="btn l" onclick="model(\'m3b\')" style="margin-top:8px">Show model answer</button><div class="model" id="m3b">Hi Ms Liang 👋\nQuick confirmation of your order #WT3488 — received this morning ✅\nAs agreed at our meeting last week:\n• 100 × PR765 printers at €230/unit\n• 8% discount (orders over 80 units)\n• delivery on 5 May to your warehouse in Felton Business Park\nPayment terms: 30 days after the invoice date. Our terms &amp; conditions are attached 📎\nThanks for your business — we look forward to supplying you again! If anything is unclear, don’t hesitate to message me here.\nBest regards,\nKate</div>' +
      '<p class="ins"><b>C</b> Exchange messages with your partner. Did your partner use different language from you? How many phrases from Exercise 2 did your partner use?</p>' + ta("u3c", "", 60) +
      '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you write an order confirmation message?"))
PAT_U = '[["Greeting",["hi ms liang","dear ms liang","hello ms liang"]],["Opening",["confirm","confirmation"]],["Order details",["wt3488","pr765"]],["Delivery",["deliver","5 may","felton"]],["Payment terms",["payment","30 days","invoice"]],["Attachments",["attached","thread"]],["Ending",["thanks for","thank you for","hesitate","look forward"]],["Closing",["best regards","regards","best,","thanks,"]]]'
VOC_U = [("Order confirmation", ["confirm an order", "order #", "unit price", "discount", "delivery / ETA", "payment terms", "invoice", "T&Cs (terms and conditions)", "attached 📎", "in the thread"]),
         ("Chat phrases", ["Quick confirmation of your order …", "Just confirming …", "As agreed …", "Our T&Cs are attached.", "Thanks for your business!", "Don’t hesitate to message me here.", "Best regards,"]),
         ("Verbs + prepositions", ["write to", "talk about", "pay for", "deliver to", "thank sb for", "look forward to"])]
os.makedirs(os.path.join(ROOT, "all"), exist_ok=True)
open(os.path.join(ROOT, "all", "lesson.html"), "w").write(page("4.5", "Confirming an order", "WRITING · UPDATED", "Learners can write an order confirmation message to a client in Slack or a CRM.",
    "BP B1 4.5 Confirming an order · Updated", CODE, [("1", u1), ("2", u2), ("3", u3)], K, VOC_U, extra_js=CSS + counter_js("u3b", 60, 90, PAT_U)))
print("ok")
