"""Zvenyhora (dairy) B2+ 1.1 Market research in dairy — lesson page.
Reuses the layout and code of build_b2p_lesson_1-1.py and swaps the content.
Usage: python3 build_zv_lesson_1-1.py ../lessons/1-1/all/lesson.html OUT.html
"""
import ast, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "build_b2p_lesson_1-1.py")).read()

NEW = {}
NEW["VOC_UP"] = '''VOC_UP = ["taste test", "blind tasting", "sensory panel", "shelf life", "SKU", "private label", "retail audit", "market share", "shelf space", "price point", "category manager", "mystery shopping"]'''

NEW["D"] = r'''D = {
 "w": [
  "Why do you think food companies need market research?",
  "Have you ever completed a survey or taken part in a tasting in a supermarket? What was it about?",
  "What kind of information do dairy companies try to get about their products and the people who buy them?",
  "Think of a dairy product you stopped buying. Why? Did the brand ever find out?",
  "What do you look at first when you choose milk, kefir or yoghurt: price, brand, fat content, shelf life or the pack?",
  "How does your company find out if a new product or a new pack design was a success?",
  "If you could ask your customers — shoppers or retail buyers — one question, what would it be?",
  "Who in your company actually talks to shoppers or retail buyers? Is it enough?"],
 "wp": [
  "Before Chobani, the data said Greek yoghurt was a tiny niche in the US. Should companies follow the data or their instinct?",
  "Shoppers say they want ‘natural’ and ‘no additives’, but often buy the cheapest pack. Should a brand listen to what people say or watch what they do?",
  "Retail chains sell their own private labels. Is that a threat or an opportunity for a dairy producer?",
  "Is it fair to make a pack smaller but keep the price (‘shrinkflation’)? Do shoppers notice?",
  "Plant-based drinks, protein yoghurts, lactose-free milk: a trend or the future of dairy? How would you find out?",
  "Can AI predict which new flavour will sell, or do you always need a real taste test?"],
 "p": [
  ["Why are sales of our kefir falling in summer?", "Sales data analysis (quantitative) + a few in-depth interviews with shoppers (qualitative)."],
  ["Which of two new yoghurt flavours do shoppers prefer?", "A blind taste test with target customers — primary, quantitative."],
  ["How big is the market for lactose-free milk in Ukraine?", "Desk research: industry reports, retail statistics — secondary, quantitative."],
  ["Do shoppers notice our new pack design on the shelf?", "In-store observation or a shelf test + a short intercept survey — primary."],
  ["How satisfied are retail chains with our deliveries?", "An online survey of category managers + a few phone interviews — quantitative + qualitative."],
  ["What prices and promotions do competitors use in supermarkets?", "A retail audit / store checks and competitors’ websites."],
  ["Shoppers complain online that the sour cream is too thin. What exactly is wrong?", "Analyse reviews and complaints (AI can group them), then a sensory panel and follow-up calls."],
  ["Is there demand for a high-protein kefir before we produce it?", "A concept test with target customers, then a small test launch in a few stores."]],
 "bp": [
  ["a test where people taste products without knowing the brand", "blind tasting", "In the blind tasting our sour cream beat the market leader."],
  ["a trained group of people who evaluate taste, smell and texture", "sensory panel", "The sensory panel said the new yoghurt was too sweet."],
  ["how long a product stays safe and good to eat", "shelf life", "Shoppers want natural products with a long shelf life — that’s a challenge."],
  ["one product variant (size, flavour, fat content) with its own code", "SKU (stock keeping unit)", "We’re cutting five slow-selling SKUs."],
  ["products sold under a retailer’s own brand", "private label", "We also produce private-label milk for a supermarket chain."],
  ["checking prices, promotions and shelf position in shops", "retail audit", "The retail audit showed our kefir on the bottom shelf."],
  ["the percentage of all sales in a market that one company has", "market share", "Our market share in the region grew by two percent."],
  ["the person at a retail chain who decides which products go on the shelf", "category manager", "The category manager asked for a promo price."],
  ["a researcher pretends to be a normal customer to check a shop", "mystery shopping", "Mystery shopping showed the fridge was too warm."]],
 "op": [
  ["___ research", "carry out / conduct / commission / outsource"],
  ["___ data", "gather / collect / analyse / interpret"],
  ["___ a survey", "design / run / send out / fill in / complete"],
  ["___ feedback", "get / collect / act on / ignore"],
  ["___ a product", "launch / test / roll out / withdraw / relaunch"],
  ["___ a taste test", "run / carry out / take part in / pass"]],
 "ch": [
  ["“Is that hard data, or just compliments from the tasting?”", ""],
  ["“Fifteen people? That’s not a sample size.”", ""],
  ["“Aren’t you focusing on the product instead of the shopper’s problem?”", ""],
  ["“Why should a retail chain give us shelf space for this?”", ""],
  ["“Who’s your target audience, exactly?”", ""],
  ["“What price point? Shoppers won’t pay more.”", ""],
  ["“Our competitor is formidable. Why would shoppers switch?”", ""]],
 "pp": [
  ["You have one month and a small budget. Find out why young families buy competitors’ yoghurt, not yours.", "Make a plan: method, sample, what you’ll ask, how you’ll report it."],
  ["Your CEO wants to export cheese to Poland next year. What do you research first — and how?", ""],
  ["Sales data says the new flavour sells well, but the retail chain wants to delist it. How do you find out the truth?", ""],
  ["Your manager says: “Just ask ChatGPT which flavour Ukrainians want.” Respond.", "Agree with part of it, then explain the limits."],
  ["A focus group of 8 people hated the new pack design. Should you cancel the relaunch?", "Think about sample size and who was in the group."]],
}'''

NEW["VA"] = '''VA = dict(id="7TY6JxR15og", title="Chobani founder on the billion-dollar Greek yogurt business", who="NBC News, Rock Center · 2012", slogan="He changed what Americans eat")'''
NEW["VB"] = "VB = VA"
NEW["FRAG"] = r'''FRAG = {
 "A": [
  ("00:00–02:36", 0, 156, "The Chobani story", [
    ("What was Hamdi Ulukaya’s business before Chobani?", "A small feta cheese company in upstate New York."),
    ("What did he see on the factory tour in 2005?", "A 100-year-old yogurt factory that was being shut down."),
    ("When did Chobani launch, and how big did it grow?", "In 2007. It grew into a $1 billion business."),
    ("How did the yogurt market in the US change?", "Before Chobani, Greek yogurt sales were nearly non-existent. Now more than a third of the yogurt Americans eat is Greek."),
    ("What did Chobani do for the local community?", "It employs more than 1,300 people and invested $193 million in the old factory.")])]}
FRAG["B"] = FRAG["A"]'''
NEW["TFA"] = r'''TFA = [
 ("Before Chobani, Hamdi Ulukaya had a small cheese business.", True, "He owned a small feta cheese company in upstate New York."),
 ("He built a brand-new factory for Chobani.", False, "He bought an old yogurt factory that was being shut down."),
 ("Chobani launched in 2007.", True, "Since 2007 it has grown into a $1 billion business."),
 ("Greek yogurt was already popular in the US before Chobani.", False, "Greek yogurt sales were nearly non-existent before Chobani."),
 ("Chobani priced its yogurt above other Greek yogurts.", False, "About $1 a cup — between normal yogurt (about 65 cents) and premium Greek yogurt ($1.34)."),
 ("Chobani wanted to be in the normal dairy aisle, not the gourmet section.", True, "Mass supermarkets, not expensive specialty shops."),
]'''
NEW["TFB"] = "TFB = TFA"
NEW["VOC_PARTS"] = r'''VOC_PARTS = {
 "A": [["take a tour", "shut a factory down", "grow into a $1 billion business", "with no signs of slowing down", "change what people eat",
        "nearly non-existent", "the biggest seller", "capital investment", "a niche market", "price point", "the dairy aisle",
        "specialty stores", "word of mouth", "twice the protein", "no preservatives"]]}
VOC_PARTS["B"] = VOC_PARTS["A"]'''

NEW["GAPS"] = r'''GAPS = [
 ("Many dairy brands now collect feedback through", "surveys on their websites and social media.", "online"),
 ("", "groups are small, but they can show how shoppers react to a new flavour.", "focus"),
 ("Complaints and repeat purchases tell you about the level of", "satisfaction.", "customer"),
 ("To understand why parents choose a yoghurt for their kids, you can hold", "interviews with them.", "in-depth"),
 ("Reading industry reports about the dairy market is", "research.", "desk"),
 ("Before you", "a new kefir, check what competitors already sell.", "launch"),
 ("People who go to the gym are the", "audience for a high-protein yoghurt.", "target"),
 ("A tasting with 15 people is cheap, but the", "size is too small for big decisions.", "sample"),
]'''
NEW["OPT"] = r'''OPT = [
 ("<u>Qualitative research</u> gives you", ["exact sales figures for each SKU", "information about why shoppers like or dislike a product"], 1, "."),
 ("<u>Primary research</u> means", ["collecting new data, e.g. running your own tasting", "reading reports that already exist"], 0, "."),
 ("A dairy company can measure <u>customer satisfaction</u> by", ["using research tools such as surveys, complaints and repeat-purchase data", "producing more milk"], 0, "."),
 ("A <u>viable</u> product", ["has", "doesn’t have"], 0, " a good chance of success."),
 ("The <u>sample size</u> is the number of", ["products", "people"], 1, " you need to get reliable information."),
 ("To <u>gauge</u> how shoppers may react to a new flavour, you can", ["watch their reactions in a taste test", "ask them if they have already bought it"], 0, "."),
]'''
NEW["PROFILE"] = r'''PROFILE = [("Attract", "How does the brand attract customers? What does it offer them?", ["target audience", "launch a product"]),
           ("Promise", "What does the brand promise to do?", ["customer satisfaction", "shelf life"]),
           ("Visibility", "What makes it visible or memorable on the shelf?", ["shelf space", "a formidable competitor"]),
           ("Ideal customer", "Who is the ideal customer for the brand?", ["pain points", "price point"])]'''
NEW["USE_A"] = '''USE_A = ["target audience", "launch a product", "customer satisfaction", "viable", "impact", "a formidable competitor", "pain points", "price point", "shelf space", "gauge"]'''
NEW["FIX"] = r'''FIX = [("Would you buy a mango-flavoured kefir?", "Tell me about the last time you bought kefir. Which one did you choose and why?"),
       ("Do you like our new pack design?", "What do you look at first when you choose yoghurt on the shelf?"),
       ("Which new flavours do you want?", "Which flavours have you tried recently? What didn’t you like about them?"),
       ("You’d pay 10 hryvnias more for organic milk, wouldn’t you?", "How much do you usually pay for milk? When do you choose a more expensive one? (Careful: a question tag can bias the answer!)")]'''
NEW["PERSONAS"] = r'''PERSONAS = [("Olena", "Category manager at a national supermarket chain, Kyiv", "Has limited shelf space and about 40 dairy suppliers. Delists products that don’t sell in 8 weeks. Complains that producers bring new SKUs without any data and miss delivery windows."),
            ("Iryna", "Mother of two, buys dairy twice a week", "Reads labels and worries about sugar and additives in kids’ yoghurts. Tried ‘natural’ brands — “they go sour in two days.” Chooses by shelf life and price."),
            ("Andrii", "Owner of three coffee shops, Lviv", "Needs milk that foams well for lattes and a stable supply. Changed suppliers twice last year — “the quality changed from batch to batch.” Some customers ask for oat or lactose-free milk.")]'''


def swap(source, name, new_code):
    tree = ast.parse(source)
    lines = source.split("\n")
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(getattr(t, "id", None) == name for t in node.targets):
            a, b = node.lineno - 1, node.end_lineno
            return "\n".join(lines[:a] + new_code.split("\n") + lines[b:])
    raise KeyError(name)

for name in ["VOC_UP", "D", "VA", "VB", "FRAG", "TFA", "TFB", "VOC_PARTS", "GAPS", "OPT", "PROFILE", "USE_A", "FIX", "PERSONAS"]:
    src = swap(src, name, NEW[name])

CASE = ('<div class="case"><b>Case file: Chobani</b><ul>'
        '<li><b>Product:</b> thick Greek-style yogurt with about twice the protein of regular yogurt and no preservatives. The recipe was tested and improved for more than a year before launch.</li>'
        '<li><b>Target audience:</b> not only women (the usual target) — also men and people who did not like yogurt before.</li>'
        '<li><b>Place:</b> the normal dairy aisle of big supermarkets, not expensive specialty stores or the gourmet section.</li>'
        '<li><b>Price point:</b> about $1 a cup — normal yogurt cost about 65 cents, premium Greek yogurt $1.34.</li>'
        '<li><b>Promotion:</b> mostly word of mouth, social media and talking directly to customers.</li>'
        '<li><b>Result:</b> Greek yogurt grew from under 1% of the US yogurt market (2006) to about half of it (2014).</li></ul>'
        '<p class="ins" style="margin:8px 0 4px">Read the case file. Why do you think the price point and the place on the shelf were so important?</p></div>')

R = [
 ("<h1>Research in tech</h1>", "<h1>Market research in dairy</h1>"),
 ("related to market and user research.</div>", "related to market research in the dairy business.</div>"),
 ("<h4>From the video (Exercises 2–5) — Video A: How To Talk To Users</h4>", "<h4>From the video and the case file (Exercises 2–5)</h4>"),
 (" <h4>From the video — Video B: Eric Migicovsky</h4>__VVB__\n", ""),
 ("<h4>Book word → what people in tech often say today</h4>", "<h4>Book word → what people in the dairy business often say</h4>"),
 ("<tr><th>In the book</th><th>In tech today</th></tr>", "<tr><th>In the book</th><th>In dairy / FMCG</th></tr>"),
 ("<tr><td>focus group</td><td>user interviews, usability tests (focus groups are still used in marketing)</td></tr>", "<tr><td>focus group</td><td>focus groups, taste tests, sensory panels</td></tr>"),
 ("<tr><td>product tester</td><td>beta tester, early adopter</td></tr>", "<tr><td>product tester</td><td>taster, sensory panel member</td></tr>"),
 ("<tr><td>desk research</td><td>competitor analysis, market research reports, social listening</td></tr>", "<tr><td>desk research</td><td>market reports, retail sales data, competitor analysis</td></tr>"),
 ("<tr><td>customer satisfaction</td><td>CSAT, NPS, app ratings</td></tr>", "<tr><td>customer satisfaction</td><td>repeat purchases, complaints, reviews, NPS</td></tr>"),
 ("<tr><td>online surveys</td><td>in-app surveys, pop-up polls</td></tr>", "<tr><td>online surveys</td><td>social media polls, QR-code surveys on the pack</td></tr>"),
 ("<tr><td>viable</td><td>MVP (minimum viable product), product-market fit</td></tr>", "<tr><td>viable</td><td>a viable SKU, a test launch</td></tr>"),
 ("<h4>★ Level up: research words people use in tech</h4>", "<h4>★ Level up: research words in the dairy business</h4>"),
 ("<p class=\"ins\"><b>2</b>You are going to watch parts of a talk by a Y Combinator partner who used to work at Airbnb. Who should a start-up talk to before it builds a product? What would you ask them? Make a list.</p>",
  "<p class=\"ins\"><b>2</b>You are going to watch a short TV report about Chobani, a yoghurt company that started in an old factory and changed what Americans eat. How can a dairy company find out what shoppers want before it launches a new product? Make a list.</p>"),
 ("<p class=\"ins\"><b>3</b>Watch the parts of the video. Were any of your ideas from Exercise 2 mentioned? Answer the questions for each part.</p>",
  "<p class=\"ins\"><b>3</b>Watch the video. Were any of your ideas from Exercise 2 mentioned? Answer the questions. Then read the case file.</p>"),
 ("<div class=\"vA\">__FA__</div>", "<div class=\"vA\">__FA__" + CASE + "</div>"),
 ("<p class=\"ins\"><b>4</b>Watch again and decide", "<p class=\"ins\"><b>4</b>Watch again and use the case file. Decide"),
 ("<div class=\"vA\"><p class=\"ins\"><b>5</b>Discuss. He says users usually have good problems but bad solutions. What does he mean? Has a client or manager ever asked you for a feature that turned out to be the wrong solution? Who talks to users in your company?</p></div>",
  "<div class=\"vA\"><p class=\"ins\"><b>5</b>Discuss. Before Chobani, the data said Greek yoghurt was a tiny niche — but the founder believed shoppers deserved better yoghurt. Was he right to ignore the data? Which ‘niche’ dairy product could grow in Ukraine? How would you find out?</p></div>"),
 ("Research words people use in tech. Read the explanation and say the word. Then tell a short story from your work where you use it.",
  "Research words in the dairy business. Read the explanation and say the word. Then tell a short story from your work where you use it."),
 ("<b>10A</b>Think of an everyday product or app you use. Choose two well-known brands for it", "<b>10A</b>Think of a dairy product you know well. Choose two well-known brands for it"),
 ("<div class=\"chips\"><span>Notion vs Obsidian</span><span>Duolingo vs Babbel</span><span>Spotify vs Apple Music</span><span>Revolut vs Monobank</span><span>Slack vs Microsoft Teams</span><span>Figma vs Canva</span></div>",
  "<div class=\"chips\"><span>Halychyna vs Yahotynske (kefir)</span><span>Activia vs a private-label yoghurt</span><span>Président vs Ferma (butter)</span><span>Alpro vs a local oat drink</span><span>Chobani vs Danone (Greek yoghurt)</span><span>Our brand vs our main competitor</span></div>"),
 ("placeholder=\"e.g. an AI meeting summary inside Slack\"", "placeholder=\"e.g. a high-protein kefir in a 0.5 l bottle\""),
 ("<div><b>Their life, not your idea</b>Don’t pitch the feature. Ask how they do things now.</div>", "<div><b>Their life, not your idea</b>Don’t pitch the product. Ask how they shop and use dairy now.</div>"),
 ("In 10D, present to a sceptical US stakeholder — your teacher.", "In 10D, present to a sceptical retail buyer or CEO — your teacher."),
 ("<i>gauge interest in a feature</i>", "<i>gauge interest in a new flavour</i>"),
 ("'<title>1.1 Research in tech — Lesson</title>\\n'", "'<title>1.1 Market research in dairy — Lesson</title>\\n'"),
 ("<a href=\"../../../index.html\"", "<a href=\"../../../index.html\""),
]
for a, b in R:
    if a not in src:
        raise SystemExit("not found: " + a[:80])
    src = src.replace(a, b)

# one video only: no A/B switch
src = src.replace('rep = {"__VSW__": VSW,', 'rep = {"__VSW__": "",')
src = src.replace('@media(max-width:700px){.match,.cls',
                  '.case{background:#fdf7e6;border-left:5px solid var(--gold);padding:10px 16px;margin:6px 0 10px;font-size:15.5px}.case ul{margin:6px 0;padding-left:20px}.case li{margin:3px 0}\n@media(max-width:700px){.match,.cls', 1)
exec(compile(src, "build_zv_lesson_1-1", "exec"), {"__name__": "__main__"})
