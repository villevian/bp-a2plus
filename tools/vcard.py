"""Clickable vocabulary chips -> card (UA translation, meaning, collocations, example, 🔊). Shared by lesson builders.
Usage:  VOC, VJS = vcard.build(groups, acc, acc2, dark)   then page(..., vocab=VOC, extra_js=VJS + other_js)
groups = [(group_title, [(en, uk, definition, example, [collocations]), ...]), ...]
"""
import json

CSS = r"""
document.head.insertAdjacentHTML("beforeend",`<style>
.vg a.vw{display:inline-block;background:@ACC2@;border-radius:12px;padding:2px 10px;margin:2px;font-size:14px;cursor:pointer;color:#231f20;text-decoration:none;border:1px solid transparent}
.vg a.vw:hover{border-color:@ACC@}.vg span:has(a){background:none;padding:0;margin:0}
.vg a.vw small{color:#6d6e70;font-size:12px;margin-left:4px}
.vcard{position:fixed;inset:0;background:rgba(30,40,60,.25);display:none;align-items:center;justify-content:center;z-index:50}.vcard.on{display:flex}
.vbox{background:#fff;border-radius:12px;max-width:460px;width:92%;padding:20px 24px;box-shadow:0 8px 30px rgba(0,0,0,.15);border-top:5px solid @ACC@}
.vbox .en{font-size:26px;font-weight:500}.vbox .uk{font-size:18px;color:@DARK@;margin:2px 0 10px}.vbox .lb{font-size:12px;font-weight:600;color:#8a8b8d;text-transform:uppercase;margin-top:10px}
.vbox ul{margin:4px 0;padding-left:18px}.vbox .ex{font-style:italic}.vbox .x{float:right;border:0;background:none;font-size:22px;cursor:pointer;color:#8a8b8d}
.vnav{display:flex;justify-content:space-between;margin-top:14px}
</style>`);
"""
JS = r"""
const VI=__VI__;let vcur=0;
document.body.insertAdjacentHTML("beforeend",'<div class="vcard" id="vcard" onclick="if(event.target===this)vclose()"><div class="vbox" id="vbox"></div></div>');
function say1(t){try{speechSynthesis.cancel();const u=new SpeechSynthesisUtterance(t);u.lang="en-GB";u.rate=.9;const v=speechSynthesis.getVoices().find(x=>/^en/i.test(x.lang));if(v)u.voice=v;speechSynthesis.speak(u)}catch(e){}}
function vshow(i){vcur=(i+VI.length)%VI.length;const v=VI[vcur];document.getElementById("vbox").innerHTML=`<button class="x" onclick="vclose()">×</button><div class="en">${v.en} <button class="btn l" style="padding:2px 10px" onclick="say1(VI[${vcur}].en)">🔊</button></div><div class="uk">${v.uk}</div>`+
 `<div class="lb">Meaning</div><div>${v.df}</div><div class="lb">Collocations</div><ul>${v.co.map(c=>"<li>"+c+"</li>").join("")}</ul><div class="lb">Example</div><div class="ex">${v.ex} <button class="btn l" style="padding:1px 8px" onclick="say1(VI[${vcur}].ex)">🔊</button></div>`+
 `<div class="vnav"><button class="btn l" onclick="vshow(${vcur-1})">← prev</button><button class="btn l" onclick="vshow(${vcur+1})">next →</button></div>`;document.getElementById("vcard").classList.add("on")}
function vclose(){document.getElementById("vcard").classList.remove("on")}
document.addEventListener("keydown",e=>{if(!document.getElementById("vcard").classList.contains("on"))return;if(e.key==="Escape")vclose();if(e.key==="ArrowRight")vshow(vcur+1);if(e.key==="ArrowLeft")vshow(vcur-1)});
document.querySelectorAll("a.vw").forEach(a=>a.onclick=e=>{e.preventDefault();vshow(+a.dataset.i)});
"""

def build(groups, acc, acc2, dark, show_uk=False):
    items, voc = [], []
    for g, ws in groups:
        chips = []
        for en, uk, df, ex, co in ws:
            items.append({"en": en, "uk": uk, "df": df, "ex": ex, "co": co})
            chips.append('<a class="vw" data-i="%d">%s%s</a>' % (len(items) - 1, en, "<small>%s</small>" % uk if show_uk else ""))
        voc.append((g, chips))
    js = CSS.replace("@ACC2@", acc2).replace("@ACC@", acc).replace("@DARK@", dark) + JS.replace("__VI__", json.dumps(items, ensure_ascii=False))
    return voc, js
