"""Business Partner B2 · 1.2 Employee retention — HOMEWORK: six people's comments about AI layoffs (Reddit-style) + lexis.
Comments 1–4 are retold from real Reddit comments (collected by BuzzFeed); 5–6 are written for the course in the same style.
Usage: python3 build_b2_hw_1-2.py OUT.html [STUDENT_CODE]
"""
import sys, os
from bp_page import page, fb, sel, inp, ta, ctl, SELF
from vocab_b2 import lesson
import vcard
from b2_1_2_data import REVIEWS
OUT = sys.argv[1]; CODE = sys.argv[2] if len(sys.argv) > 2 else ""
ACC, ACC2, DARK, GR2 = "#5b5fc7", "#e8e9fa", "#4044a8", "#7b7fe0"
_, GROUPS = lesson("1.2")
VOC, VJS = vcard.build(GROUPS, ACC, ACC2, DARK)
K = {}
def radio(k, opts):
    return "".join('<label class="opt" style="display:inline;margin:0 10px 0 0"><input type="radio" name="%s" data-k="%s" value="%s"> %s</label>' % (k, k, o, o) for o in opts)
LAB = {"reddit": "Retold from a Reddit comment", "style": "Written for this course in the same style"}
CARDS = "".join('<div class="cm"><div class="ch"><span class="no">%d</span><b>%s</b><span class="lb">%s</span></div><p>%s</p></div>' % (i + 1, t, LAB[src], txt)
                for i, (t, txt, src, _) in enumerate(REVIEWS))

# A Who is writing?
WHO = {"friend": "a friend of someone who lost a job", "employee": "someone who lost their own job", "manager": "a manager", "customer": "a customer"}
WOPT = sorted(WHO.values())
for i, r in enumerate(REVIEWS): K["a_%d" % (i + 1)] = [WHO[r[3]]]
s1 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">A</b>Read six comments from people about AI and jobs. Who is writing each comment?</p>' + CARDS +
      "".join('<div class="row">Comment %d: %s%s</div>' % (i + 1, sel("a_%d" % (i + 1), WOPT, 300), fb("a_%d" % (i + 1))) for i in range(len(REVIEWS))) + ctl("a"))

# B True / False
TF = [("In comment 1, the assistant was invited to a goodbye party.", "F"), ("In comment 2, the company paid more to get the knowledge back.", "T"),
      ("In comment 3, the manager was an expert in design.", "F"), ("In comment 4, the developer knew his work was used to train AI.", "F"),
      ("In comment 5, cutting the juniors saved the company money.", "F"), ("In comment 6, the writer may change banks.", "T")]
for i, (_, a) in enumerate(TF): K["b_%d" % (i + 1)] = [a]
s2 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">B</b>Are these sentences <i>true</i> (T) or <i>false</i> (F)?</p>'
      '<details class="rd"><summary>💬 Open the comments</summary>%s</details>' % CARDS +
      "".join('<div class="tf"><span class="q">%d. %s</span>%s%s</div>' % (i + 1, q, radio("b_%d" % (i + 1), "TF"), fb("b_%d" % (i + 1))) for i, (q, _) in enumerate(TF)) + ctl("b", "chkRad"))

# C Find the chunks
CH = [("a polite way to say ‘she lost her job’ (comment 1)", "was let go|let go|she was let go"),
      ("lost his job because the company needed fewer people (comment 2)", "was laid off|laid off"),
      ("employed him again, as an adviser (comment 2)", "took him back as a consultant|took him back"),
      ("very surprised and impressed by (comment 3)", "was amazed by|amazed by"),
      ("old software the company still depends on (comment 5)", "legacy system|our legacy system|a legacy system"),
      ("answered the phone (comment 6)", "picked up|finally picked up")]
for i, (_, a) in enumerate(CH): K["c_%d" % (i + 1)] = [x.strip() for x in a.split("|")]
s3 = ('<div class="bsec">Vocabulary</div><p class="ins"><b class="x">C</b>Find chunks (groups of words) in the comments that mean the same as these phrases.</p>'
      '<details class="rd"><summary>💬 Open the comments</summary>%s</details>' % CARDS +
      "".join('<div class="row">%d. %s → %s%s</div>' % (i + 1, q, inp("c_%d" % (i + 1), 260), fb("c_%d" % (i + 1))) for i, (q, _) in enumerate(CH)) + ctl("c") +
      '<p class="hint">Learn chunks, not single words: not just <i>go</i>, but <i>let somebody go</i>.</p>')

# D Link to the article
LINK = [("Experienced people take institutional knowledge with them.", "1|5"), ("Rehiring can cost more than the company saved.", "2|5"),
        ("Some managers are excited about AI without understanding the work.", "3"), ("Customers can react badly when bots replace people.", "6")]
NUMS = ["1", "2", "3", "4", "5", "6"]
for i, (_, a) in enumerate(LINK): K["d_%d" % (i + 1)] = a.split("|")
s4 = ('<div class="bsec">Reading</div><p class="ins"><b class="x">D</b>Which comment is an example of these ideas from the article? (Some ideas have two possible answers.)</p>'
      '<details class="rd"><summary>💬 Open the comments</summary>%s</details>' % CARDS +
      "".join('<div class="row">%d. %s → comment %s%s</div>' % (i + 1, q, sel("d_%d" % (i + 1), NUMS, 70), fb("d_%d" % (i + 1))) for i, (q, _) in enumerate(LINK)) + ctl("d"))

# E Writing
s5 = ('<div class="bsec wr">Writing</div><p class="ins"><b class="x">E</b>Write your own comment for the same Reddit thread (60–80 words). Has AI changed your job or company? Use at least <b>three chunks</b> from the lesson vocabulary and <b>two</b> Future Continuous or Future Perfect forms.</p>'
      '<div class="card"><i>By 2030, AI will have taken over most menial tasks in my team, but we will still be …</i></div>' +
      ta("e", "Write your comment here …", 170) + '<p class="hint" id="ewc"></p>' + '<div style="margin-top:20px">%s</div>' % (SELF % "How well can you talk about AI and jobs now?"))

XJS = VJS + r"""
document.head.insertAdjacentHTML("beforeend",`<style>
.cm{border:1px solid #dcdde0;border-left:4px solid #ff4500;border-radius:8px;padding:10px 16px;margin:10px 0;background:#fff}.cm .ch{display:flex;align-items:center;gap:10px;flex-wrap:wrap}
.cm .no{background:#ff4500;color:#fff;border-radius:50%;width:24px;height:24px;display:inline-flex;align-items:center;justify-content:center;font-size:13px;font-weight:600}.cm .lb{font-size:12px;color:#888;margin-left:auto}.cm p{margin:6px 0 2px}
details.rd summary{cursor:pointer;color:#4044a8;font-weight:500;margin:6px 0}</style>`);
function ewc(){const t=document.querySelector('.g[data-k="e"]');if(!t)return;const n=(t.value.trim().match(/\S+/g)||[]).length;document.getElementById("ewc").textContent=n+" words"+(n>=60&&n<=80?" ✓":" (60–80)")}
document.addEventListener("input",e=>{if(e.target.dataset&&e.target.dataset.k==="e")ewc()});window.afterFill=ewc;"""
secs = [("A", s1), ("B", s2), ("C", s3), ("D", s4), ("E", s5)]
h = page("1.2", "Employee retention", "HOMEWORK", "Read real people’s stories about AI layoffs, notice useful chunks and write your own comment.",
         "BP B2 1.2 Employee retention · Homework", CODE, secs, K, VOC, acc=ACC, acc2=ACC2, dark=DARK, grad2=GR2,
         footer="Comments 1–4 are retold from Reddit comments; 5–6 were written for this course. ", extra_js=XJS)
os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True); open(OUT, "w").write(h); print("ok hw", len(h))
