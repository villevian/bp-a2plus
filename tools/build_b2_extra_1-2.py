"""Business Partner B2 · 1.2 Employee retention — EXTRA: Lexical lab (lexical approach: collocations, chunks, nuance, recall, lexical sets, personalisation).
Usage: python3 build_b2_extra_1-2.py OUT.html [STUDENT_CODE]
"""
import sys, os, json, random
from bp_page import page, fb, sel, inp, ta, ctl, SELF
from vocab_b2 import lesson
import vcard
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#5b5fc7", "#e8e9fa", "#4044a8", "#7b7fe0"
_, GROUPS = lesson("1.2")
VOC, VJS = vcard.build(GROUPS, ACC, ACC2, DARK)
K = {}
random.seed(212)
def shuf(o): o = list(o); random.shuffle(o); return o
def hid(k): return '<input type="hidden" class="g" data-k="%s">' % k
def how(t): return '<div class="how"><b>💡 Lexical tip</b>%s</div>' % t

# L1 Collocation forks: which words go with the verb? (choose all)
FORKS = [("cut", ["headcount", "costs", "jobs"], ["a mistake"]), ("admit", ["a mistake", "an error"], ["a backlash", "headcount"]),
         ("reverse", ["a decision", "course"], ["staff", "a premium"]), ("lose", ["institutional knowledge", "talent"], ["a sabbatical", "a backlash"]),
         ("face", ["a backlash", "layoffs"], ["a pipeline", "a promotion"]), ("poach", ["staff", "talent"], ["a decision", "menial tasks"])]
FK = {i: sorted(ok) for i, (_, ok, _) in enumerate(FORKS)}
s1 = ('<div class="bsec">Lexical lab</div>' +
      how('<p>Words live with “partners”. Learn the verb together with the nouns it goes with: not <i>decision</i>, but <i>reverse a decision</i>.</p>') +
      '<p class="ins"><b class="x">1</b>Collocation forks. Click <b>all</b> the words that go with each verb. Then check.</p>' +
      "".join('<div class="fork" data-i="%d"><span class="fv">%s</span><span class="fo">%s</span>%s</div>' % (
          i, v, "".join('<button>%s</button>' % w for w in shuf(ok + no)), hid("fk_%d" % i)) for i, (v, ok, no) in enumerate(FORKS)) +
      '<div class="ctl"><button class="btn" onclick="forkChk()">Check</button><span class="res" id="r_fk"></span></div>')

# L2 Nuance: five ways to say someone loses a job
NU = [("He was ___ for stealing company laptops.", "fired"), ("We’re very sorry, but we have to ___.", "let you go"),
      ("(HR letter) We regret to inform you that you have been ___.", "made redundant"), ("(Newspaper headline) Bank ___ 45 jobs for voice bot", "axes"),
      ("US tech companies ___ about 139,000 workers in the first half of 2026.", "laid off")]
NOPT = sorted(a for _, a in NU)
for i, (_, a) in enumerate(NU): K["nu_%d" % (i + 1)] = [a]
s2 = ('<div class="bsec">Lexical lab</div>' +
      how('<p>Similar meaning ≠ same use. <b>fire</b> = because of bad performance or behaviour · <b>lay off</b> = the company needs fewer people (neutral) · '
          '<b>make redundant</b> = formal, British HR language · <b>let somebody go</b> = polite, soft · <b>axe</b> = informal, newspaper headlines.</p>') +
      '<p class="ins"><b class="x">2</b>Choose the best option for each sentence.</p>' +
      "".join('<div class="row">%d. %s %s%s</div>' % (i + 1, q.replace("___", sel("nu_%d" % (i + 1), NOPT, 160)), "", fb("nu_%d" % (i + 1))) for i, (q, _) in enumerate(NU)) + ctl("nu") +
      '<p class="ins" style="margin-top:14px">Which word would you <b>never</b> use about the Commonwealth Bank staff? Why?</p>' + inp("nu_why", 520, "I would never say they were … because …"))

# L3 Recall from memory (first letters)
RC = [("The cuts were a c___-c______ e_______ dressed up as innovation.", "cost-cutting exercise|a cost-cutting exercise"),
      ("When experienced people leave, i____________ k________ leaves with them.", "institutional knowledge"),
      ("IBM is tripling its e____-l____ h_____.", "entry-level hiring"),
      ("Klarna’s CEO a_______ a m______ and started hiring people again.", "admitted a mistake"),
      ("Many people stay in their jobs out of fear, not loyalty. It’s called j__ h______.", "job hugging"),
      ("In a few years, companies will be p_______ s____ from their rivals at a premium.", "poaching staff"),
      ("The bank r_______ its d_______ when calls went up.", "reversed its decision|reversed the decision"),
      ("AI should a______ people, not r______ them.", "augment people, not replace them|augment, replace|augment people not replace them")]
for i, (_, a) in enumerate(RC): K["rc_%d" % (i + 1)] = [x.strip() for x in a.split("|")]
s3 = ('<div class="bsec">Lexical lab</div>' +
      how('<p>Try from memory first — don’t open the vocabulary. Remembering is what makes words stay. Then check and open the cards for the ones you missed.</p>') +
      '<p class="ins"><b class="x">3</b>Complete the chunks from the article. The first letters help you.</p>' +
      "".join('<div class="row">%d. %s<br>%s%s</div>' % (i + 1, q, inp("rc_%d" % (i + 1), 330), fb("rc_%d" % (i + 1))) for i, (q, _) in enumerate(RC)) + ctl("rc"))

# L4 Lexical sets: sort chunks
SETS = [("Cutting jobs", ["cut headcount", "let somebody go", "make somebody redundant", "a cost-cutting exercise"]),
        ("Bringing people back", ["rehire staff", "reverse a decision", "do a U-turn", "take somebody back as a consultant"]),
        ("Keeping people", ["build the talent pipeline", "offer diverse work", "invest in learning", "a clear promotion path"])]
SW = [w for _, ws in SETS for w in ws]; SG = {w: g for g, ws in SETS for w in ws}
s4 = ('<div class="bsec">Lexical lab</div>' +
      how('<p>Organise vocabulary by topic, not alphabet. Click a chunk, then click a group.</p>') +
      '<p class="ins"><b class="x">4</b>Sort the chunks into three groups.</p><div class="pool" id="pool">%s</div><div class="bins">%s</div>' % (
          "".join('<span class="chip" data-w="%s">%s</span>' % (w, w) for w in shuf(SW)),
          "".join('<div class="bin" data-g="%s"><b>%s</b><div class="in"></div></div>' % (g, g) for g, _ in SETS)) +
      "".join(hid("srt_%d" % i) for i in range(len(SW))) +
      '<div class="ctl"><button class="btn" onclick="sortChk()">Check</button><span class="res" id="r_srt"></span></div>')

# L5 Personalise + debate
s5 = ('<div class="bsec wr">Lexical lab</div>' +
      how('<p>A chunk becomes yours when you use it about <b>your</b> life. Write true sentences.</p>') +
      '<p class="ins"><b class="x">5</b><b>A</b> Write five true sentences about your company or industry. Use a different chunk from this page in each one.</p>' +
      ta("p5a", "1 In my company, we …\n2 …\n3 …\n4 …\n5 …", 150) +
      '<p class="ins" style="margin-top:18px"><b>B</b> Debate. IBM is <i>tripling entry-level hiring</i>. Salesforce <i>cut its support headcount</i> from 9,000 to about 5,000. Which company made the smarter decision? Prepare three arguments for class.</p>' +
      ta("p5b", "I think … made the smarter decision because …", 100) + '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you use these chunks now?"))

JS = r"""
const SW=__SW__,SG=__SG__,FK=__FK__;
const $q=(s,r=document)=>r.querySelector(s),$a=(s,r=document)=>[...r.querySelectorAll(s)];
function hv(k){const e=$q(`.g[data-k="${k}"]`);return e?e.value:""}
function setH(k,v){const e=$q(`.g[data-k="${k}"]`);if(e){e.value=v;e.dispatchEvent(new Event("input",{bubbles:true}))}}
/* forks */
document.addEventListener("click",e=>{const b=e.target.closest(".fork .fo button");if(!b)return;b.classList.toggle("on");b.classList.remove("ok","no");const f=b.closest(".fork");
 setH("fk_"+f.dataset.i,$a(".fo button.on",f).map(x=>x.textContent).sort().join("|"))});
function forkChk(){let n=0;$a(".fork").forEach(f=>{const ok=FK[f.dataset.i];$a(".fo button",f).forEach(b=>{b.classList.remove("ok","no","miss");const want=ok.includes(b.textContent),on=b.classList.contains("on");
  if(on&&want)b.classList.add("ok");else if(on&&!want)b.classList.add("no");else if(!on&&want)b.classList.add("miss")});
  if($a(".fo button.on",f).map(x=>x.textContent).sort().join("|")===ok.join("|"))n++});
 $q("#r_fk").textContent=n+" / "+$a(".fork").length+(n===$a(".fork").length?" ✓ Well done!":" · dashed = you missed it, red = doesn’t go")}
/* sort */
let csel=null;
function chipTo(c,g){c.classList.remove("sel","ok","no");if(g){$q(`.bin[data-g="${g}"] .in`).appendChild(c)}else $q("#pool").appendChild(c)}
document.addEventListener("click",e=>{const c=e.target.closest(".chip");if(c){e.stopPropagation();const w=c.dataset.w;
  if(c.closest(".bin")&&csel&&csel!==c){const g=c.closest(".bin").dataset.g;chipTo(csel,g);setH("srt_"+SW.indexOf(csel.dataset.w),g);csel=null;return}
  if(c.closest(".bin")){chipTo(c,null);setH("srt_"+SW.indexOf(w),"");return}
  $a(".chip.sel").forEach(x=>x!==c&&x.classList.remove("sel"));c.classList.toggle("sel");csel=c.classList.contains("sel")?c:null;return}
 const b=e.target.closest(".bin");if(b&&csel){const w=csel.dataset.w;chipTo(csel,b.dataset.g);setH("srt_"+SW.indexOf(w),b.dataset.g);csel=null}},true);
function sortChk(){let n=0,left=$a("#pool .chip").length;$a(".bin .chip").forEach(c=>{const ok=SG[c.dataset.w]===c.closest(".bin").dataset.g;c.classList.add(ok?"ok":"no");if(ok)n++});
 $q("#r_srt").textContent=n+" / "+SW.length+(left?" · "+left+" not sorted yet":n===SW.length?" ✓ Well done!":" · red chunks are in the wrong group")}
function wRestore(){SW.forEach((w,i)=>{const g=hv("srt_"+i),c=$q(`.chip[data-w="${w}"]`);if(c)chipTo(c,g||null)});
 $a(".fork").forEach(f=>{const v=(hv("fk_"+f.dataset.i)||"").split("|");$a(".fo button",f).forEach(b=>b.classList.toggle("on",v.includes(b.textContent)))})}
window.afterFill=wRestore;
document.head.insertAdjacentHTML("beforeend",`<style>
.how{background:#fff8e6;border-left:4px solid #f2b631;border-radius:6px;padding:8px 16px;margin:10px 0 14px;font-size:15px}.how>b{display:block;color:#9a6b00;margin-bottom:2px}.how p{margin:3px 0}
.fork{display:flex;flex-wrap:wrap;align-items:center;gap:8px;padding:8px 0;border-bottom:1px solid #eee}.fork .fv{min-width:90px;font-weight:600;color:#4044a8}
.fo button,.chip{font:inherit;font-size:15px;padding:4px 12px;border:1.5px solid #c8c9cb;border-radius:16px;background:#fff;cursor:pointer;margin:2px}
.fo button.on{border-color:#5b5fc7;background:#e8e9fa}.fo button.ok,.chip.ok{border-color:#2e9b57;background:#e7f6ec;color:#1e7a43}.fo button.no,.chip.no{border-color:#d9534f;background:#fdecec;color:#b52b27}.fo button.miss{border:1.5px dashed #2e9b57}
.pool{display:flex;flex-wrap:wrap;gap:6px;min-height:44px;padding:10px;border:1.5px dashed #c8c9cb;border-radius:8px;margin:8px 0 12px}.chip{border-color:#5b5fc7;color:#4044a8;user-select:none}.chip.sel{background:#5b5fc7;color:#fff}
.bins{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}@media(max-width:700px){.bins{grid-template-columns:1fr}}.bin{border:1.5px solid #c8c9cb;border-radius:8px;padding:8px;min-height:130px;cursor:pointer;background:#fafaff}.bin b{display:block;color:#4044a8;margin-bottom:6px}.bin .in{display:flex;flex-wrap:wrap;gap:4px}
</style>`);"""
XJS = VJS + JS.replace("__SW__", json.dumps(SW)).replace("__SG__", json.dumps(SG)).replace("__FK__", json.dumps(FK))
secs = [("1", s1), ("2", s2), ("3", s3), ("4", s4), ("5", s5)]
h = page("1.2", "Employee retention", "EXTRA", "Lexical lab: collocations, chunks and nuance for talking about layoffs, rehiring and keeping people.",
         "BP B2 1.2 Employee retention · Extra", CODE, secs, K, VOC, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2, extra_js=XJS)
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True); open(OUT, "w").write(h); print("ok extra", len(h))
