"""Zvenyhora / Savencia (hard cheese) B2+ 1.1 Market research: hard cheese — lesson page.
Reuses the layout and code of build_b2p_lesson_1-1.py and swaps the content.
Usage: python3 build_zv_lesson_1-1.py ../lessons/1-1/all/lesson.html OUT.html
"""
import ast, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, "build_b2p_lesson_1-1.py")).read()

NEW = {}
NEW["VOC_UP"] = '''VOC_UP = ["blind tasting", "sensory panel", "grader", "maturation / ripening", "rind", "shelf life", "SKU", "private label", "retail audit", "market share", "PDO (protected designation of origin)", "counterfeit"]'''

NEW["D"] = r'''D = {
 "w": [
  "Why do you think cheese companies need market research?",
  "Have you ever tasted cheese at a promo stand in a supermarket? Did you buy it afterwards? Why / why not?",
  "What kind of information do cheese producers try to get about their products and the people who buy them?",
  "When you choose hard cheese in a shop, what do you look at first: price, brand, age, origin, fat content or the pack?",
  "Think of a cheese you stopped buying. Why? Did the brand ever find out?",
  "How does your company find out if a new cheese or a new pack was a success?",
  "If you could ask your customers — shoppers or retail buyers — one question about cheese, what would it be?",
  "Who in your company actually talks to shoppers, retail buyers or restaurants? Is it enough?"],
 "wp": [
  "A wheel of parmesan costs over $1,000. What makes shoppers pay a premium for cheese: taste, origin, story or brand?",
  "Shoppers say they want ‘real, natural cheese’, but many buy the cheapest ‘cheese product’. Should a brand listen to what people say or watch what they buy?",
  "Retail chains sell private-label cheese. Is that a threat or an opportunity for a producer like Zveni Hora?",
  "Should a Ukrainian hard cheese have a protected origin, like Parmigiano Reggiano? Would shoppers pay more for it?",
  "Fake and low-quality cheese is a big business. Whose job is it to protect shoppers: producers, retailers or the state?",
  "Can AI predict which new cheese will sell, or do you always need a real tasting?"],
 "p": [
  ["Why are sales of our 200 g sliced cheese falling in one region?", "Sales data by region and store (quantitative) + a few interviews with shoppers and store managers (qualitative)."],
  ["Which of two new flavoured cheeses do shoppers prefer?", "A blind tasting with target customers — primary, quantitative."],
  ["How big is the hard cheese market in Ukraine, and is it growing?", "Desk research: industry reports, statistics — secondary, quantitative."],
  ["Do shoppers notice our new pack on the cheese shelf?", "In-store observation / shelf test + a short intercept survey — primary."],
  ["Do restaurants want our cheese in 1 kg blocks or pre-grated?", "Phone or face-to-face interviews with chefs and buyers — qualitative, primary."],
  ["What prices and promotions do competitors use for hard cheese?", "A retail audit / store checks and competitors’ websites."],
  ["Shoppers complain online that the cheese is ‘rubbery’. What exactly is wrong?", "Analyse reviews (AI can group them), then a sensory panel and a few follow-up calls."],
  ["Will shoppers pay more for a cheese aged 12 months?", "A price test / survey with different price points + a small test launch."]],
 "bp": [
  ["a test where people taste products without knowing the brand", "blind tasting", "In the blind tasting our cheese beat the market leader."],
  ["a trained group of people who evaluate taste, smell and texture", "sensory panel", "The sensory panel said the new cheese was too salty."],
  ["an expert who checks the quality of cheese wheels", "grader", "The master grader checks every wheel after a year."],
  ["the time cheese is left to age and develop flavour", "maturation / ripening", "A longer maturation makes the price go higher."],
  ["the hard outer layer of a cheese", "rind", "The rind protects the cheese while it matures."],
  ["one product variant (weight, slice, fat) with its own code", "SKU (stock keeping unit)", "We’re launching two new SKUs: 150 g slices and a 500 g block."],
  ["products sold under a retailer’s own brand", "private label", "We also produce private-label cheese for a supermarket chain."],
  ["a legal label that proves a food comes from one area", "PDO (protected designation of origin)", "Parmigiano Reggiano is protected as a PDO in the EU."],
  ["a fake copy sold as the real product", "counterfeit", "Counterfeit cheese damages the real brand."],
  ["checking prices, promotions and shelf position in shops", "retail audit", "The retail audit showed our cheese on the bottom shelf."]],
 "op": [
  ["___ research", "carry out / conduct / commission / outsource"],
  ["___ data", "gather / collect / analyse / interpret"],
  ["___ a survey", "design / run / send out / fill in / complete"],
  ["___ feedback", "get / collect / act on / ignore"],
  ["___ a product", "launch / test / roll out / withdraw / relaunch"],
  ["___ cheese", "make / age / grade / slice / grate / taste"]],
 "ch": [
  ["“Is that hard data, or just compliments from the tasting?”", ""],
  ["“Fifteen people? That’s not a sample size.”", ""],
  ["“Aren’t you focusing on the product instead of the shopper’s problem?”", ""],
  ["“Why should a retail chain give us more shelf space for this cheese?”", ""],
  ["“Who’s your target audience, exactly?”", ""],
  ["“What price point? Shoppers won’t pay more for cheese right now.”", ""],
  ["“Our competitor is formidable. Why would shoppers switch?”", ""]],
 "pp": [
  ["You have one month and a small budget. Find out why young families buy cheaper ‘cheese products’ instead of your hard cheese.", "Make a plan: method, sample, what you’ll ask, how you’ll report it."],
  ["Head office in France wants to know if Ukrainian shoppers would buy a premium aged cheese. What do you research first — and how?", ""],
  ["Sales data says a new cheese sells well, but the retail chain wants to delist it. How do you find out the truth?", ""],
  ["Your manager says: “Just ask ChatGPT which cheese Ukrainians want.” Respond.", "Agree with part of it, then explain the limits."],
  ["A focus group of 8 people hated the new pack. Should you cancel the relaunch?", "Think about sample size and who was in the group."]],
}'''

NEW["VA"] = '''VA = dict(id="ZgjWOo7IqQY", title="Why Parmesan Cheese Is So Expensive | Regional Eats", who="Food Insider · Claudia Romeo", slogan="The king of cheeses")'''
NEW["VB"] = "VB = VA"
NEW["FRAG"] = r'''FRAG = {
 "A": [
  ("00:00–02:23", 0, 143, "A $1,000 wheel", [
    ("How much can one wheel of parmesan cost, and how much does it weigh?", "Over $1,000; the average wheel weighs 88 pounds (about 40 kg), so over $11 per pound."),
    ("How does its price compare with cheddar?", "It’s more than double the price of average cheddar."),
    ("How big is the parmesan business for Italy?", "About 3.6 million wheels a year; the industry is worth €2.2 billion — one of Italy’s biggest exports."),
    ("Where can it be made, and why only there?", "Only in a restricted area of northern Italy (Emilia-Romagna); 329 certified dairies. It’s about three good bacteria that grow only in this territory."),
    ("What are the only three ingredients?", "Cow’s milk, salt and rennet.")]),
  ("06:11–07:58", 371, 478, "Mark of origin, maturation and price", [
    ("What does the stencil on the wheel show customers?", "The mark of origin — that this is the real thing from the restricted area."),
    ("What information is on the ID plaque?", "Where and when the cheese was produced."),
    ("What happens after one year?", "A master grader inspects the wheels and brands them."),
    ("Why does a longer maturation make the price higher?", "Older cheese (2 years on average, up to 10) has a stronger, nuttier taste; three-year-old ‘vecchio’ costs about €13 per pound.")]),
  ("07:58–09:46", 478, 586, "Counterfeits and how to spot the real thing", [
    ("What problem does the high price create?", "A black market of counterfeit parmesan products."),
    ("How big is the fake-food industry in Italy?", "Estimated at about €100 billion."),
    ("Where is parmesan protected, and where is it not?", "It is protected in the EU as a PDO, but it struggles to get recognition in the rest of the world."),
    ("How can a shopper recognise real parmesan?", "The dotted stencil on the rind, or the official logo and the PDO mark on the pack.")])]}
FRAG["B"] = FRAG["A"]'''
NEW["TFA"] = r'''TFA = [
 ("A wheel of parmesan costs about the same per pound as cheddar.", False, "It’s more than double the price of average cheddar."),
 ("Parmesan can be made anywhere in Italy if the recipe is followed.", False, "Only in a restricted area of northern Italy, by 329 certified dairies."),
 ("Real parmesan has only three ingredients.", True, "Cow’s milk, salt and rennet."),
 ("Each wheel gets an ID that shows where and when it was made.", True, "A plaque made from milk protein."),
 ("The longer the cheese matures, the cheaper it gets.", False, "A longer maturation makes the price go higher."),
 ("Parmesan is protected as a PDO everywhere in the world.", False, "It’s protected in the EU but struggles to get recognition in the rest of the world."),
]'''
NEW["TFB"] = "TFB = TFA"
NEW["VOC_PARTS"] = r'''VOC_PARTS = {
 "A": [["a wheel of cheese", "it costs over … per pound", "more than double the price of", "age / be aged", "a big business", "be worth an eye-popping …", "one of the biggest exports", "a restricted area", "certified dairies"],
       ["a mark of origin", "the real thing", "a master grader", "inspect / brand the wheels", "maturation", "a stronger, nuttier taste", "make the price go higher"],
       ["a black market", "counterfeit products", "fakes", "fight copycats", "protected designation of origin", "get the recognition it deserves", "legit", "the official logo"]]}
VOC_PARTS["B"] = VOC_PARTS["A"]'''

NEW["GAPS"] = r'''GAPS = [
 ("Many cheese brands now collect feedback through", "surveys on their websites and social media.", "online"),
 ("", "groups are small, but they can show how shoppers react to a new cheese.", "focus"),
 ("Complaints and repeat purchases tell you about the level of", "satisfaction.", "customer"),
 ("To understand why chefs choose one hard cheese over another, you can hold", "interviews with them.", "in-depth"),
 ("Reading industry reports about the Ukrainian cheese market is", "research.", "desk"),
 ("Before you", "a new aged cheese, check what competitors already sell.", "launch"),
 ("Cheese lovers who cook Italian food are the", "audience for a parmesan-style cheese.", "target"),
 ("A tasting with 15 people is cheap, but the", "size is too small for big decisions.", "sample"),
]'''
NEW["OPT"] = r'''OPT = [
 ("<u>Qualitative research</u> gives you", ["exact sales figures for each SKU", "information about why shoppers like or dislike a cheese"], 1, "."),
 ("<u>Primary research</u> means", ["collecting new data, e.g. running your own tasting", "reading reports that already exist"], 0, "."),
 ("A cheese company can measure <u>customer satisfaction</u> by", ["using research tools such as surveys, complaints and repeat-purchase data", "producing more cheese"], 0, "."),
 ("A <u>viable</u> product", ["has", "doesn’t have"], 0, " a good chance of success."),
 ("The <u>sample size</u> is the number of", ["cheeses", "people"], 1, " you need to get reliable information."),
 ("To <u>gauge</u> how shoppers may react to a new cheese, you can", ["watch their reactions in a blind tasting", "ask them if they have already bought it"], 0, "."),
]'''
NEW["PROFILE"] = r'''PROFILE = [("Attract", "How does the brand attract customers? What does it offer them?", ["target audience", "launch a product"]),
           ("Promise", "What does the brand promise to do?", ["customer satisfaction", "maturation"]),
           ("Visibility", "What makes it visible or memorable on the cheese shelf?", ["shelf space", "a formidable competitor"]),
           ("Ideal customer", "Who is the ideal customer for the brand?", ["pain points", "price point"])]'''
NEW["USE_A"] = '''USE_A = ["target audience", "launch a product", "customer satisfaction", "viable", "impact", "a formidable competitor", "pain points", "price point", "shelf space", "gauge"]'''
NEW["FIX"] = r'''FIX = [("Would you buy a hard cheese with truffle?", "Tell me about the last time you bought hard cheese. Which one did you choose and why?"),
       ("Do you like our new pack design?", "What do you look at first when you choose cheese on the shelf?"),
       ("Which new cheeses do you want?", "Which cheeses have you tried recently? What didn’t you like about them?"),
       ("You’d pay 50 hryvnias more for a cheese aged 12 months, wouldn’t you?", "How much do you usually pay for hard cheese? When do you choose a more expensive one? (Careful: a question tag can bias the answer!)")]'''
NEW["PERSONAS"] = r'''PERSONAS = [("Olena", "Category manager (cheese & deli) at a national supermarket chain, Kyiv", "Has limited shelf space and about 30 cheese suppliers. Delists products that don’t sell in 8 weeks. Says shoppers are switching to cheaper ‘cheese products’ and private label. Complains that producers bring new SKUs without data."),
            ("Iryna", "Mother of two, buys cheese every week", "Buys hard cheese for sandwiches and pasta. Reads labels — wants real cheese, not a ‘cheese product’ with palm oil. Says good cheese is expensive, so she waits for promotions. Doesn’t trust cheese that is ‘rubbery’ or has no smell."),
            ("Andrii", "Chef and owner of two Italian restaurants, Lviv", "Uses about 40 kg of hard cheese a month for pasta and pizza. Imported parmesan is too expensive, so he tested two Ukrainian hard cheeses — “one melted badly, the other was too salty.” Wants stable quality from batch to batch and pre-grated packs.")]'''

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

CASE = ('<div class="case"><b>Case file: research on cheese buyers</b><ul>'
        '<li><b>Award stickers vs taste descriptions.</b> Oregon State University showed 488 cheese buyers pictures of familiar cheeses (brie, cheddar) and unfamiliar ones (Coulommiers, Cantal), with prices, award stickers or short taste descriptions. Shoppers who like trying new food paid more for unfamiliar cheese with an award sticker. Shoppers who prefer familiar cheese cared more about the taste description.</li>'
        '<li><b>What shoppers buy.</b> In a survey of 1,821 people in Canada and the US, more than a third preferred hard or firm cheese. Most bought pre-packed blocks (91%), shredded (80%) or sliced cheese (79%). For more than 80%, local production was not an important factor.</li>'
        '<li><b>Ukraine.</b> Ukrainian cheese production fell to 57,000 tonnes in 2024 — about 20% less than in 2023 — because of lower milk yields and fewer cows. Exports were about 6,000 tonnes, around 11% of production.</li></ul>'
        '<p class="ins" style="margin:8px 0 4px">Read the case file. What would you test first for a Ukrainian hard cheese: an award sticker, a taste description, the pack format or the price?</p></div>')

R = [
 ("<h1>Research in tech</h1>", "<h1>Market research: hard cheese</h1>"),
 ("related to market and user research.</div>", "related to market research in the cheese business.</div>"),
 ("<h4>From the video (Exercises 2–5) — Video A: How To Talk To Users</h4>", "<h4>From the video and the case file (Exercises 2–5)</h4>"),
 (" <h4>From the video — Video B: Eric Migicovsky</h4>__VVB__\n", ""),
 ("<h4>Book word → what people in tech often say today</h4>", "<h4>Book word → what people in the cheese business often say</h4>"),
 ("<tr><th>In the book</th><th>In tech today</th></tr>", "<tr><th>In the book</th><th>In dairy / FMCG</th></tr>"),
 ("<tr><td>focus group</td><td>user interviews, usability tests (focus groups are still used in marketing)</td></tr>", "<tr><td>focus group</td><td>focus groups, tastings, sensory panels</td></tr>"),
 ("<tr><td>product tester</td><td>beta tester, early adopter</td></tr>", "<tr><td>product tester</td><td>taster, sensory panel member, grader</td></tr>"),
 ("<tr><td>desk research</td><td>competitor analysis, market research reports, social listening</td></tr>", "<tr><td>desk research</td><td>market reports, retail sales data, competitor analysis</td></tr>"),
 ("<tr><td>customer satisfaction</td><td>CSAT, NPS, app ratings</td></tr>", "<tr><td>customer satisfaction</td><td>repeat purchases, complaints, reviews, NPS</td></tr>"),
 ("<tr><td>online surveys</td><td>in-app surveys, pop-up polls</td></tr>", "<tr><td>online surveys</td><td>social media polls, QR-code surveys on the pack</td></tr>"),
 ("<tr><td>viable</td><td>MVP (minimum viable product), product-market fit</td></tr>", "<tr><td>viable</td><td>a viable SKU, a test launch</td></tr>"),
 ("<h4>★ Level up: research words people use in tech</h4>", "<h4>★ Level up: research and cheese words</h4>"),
 ("<p class=\"ins\"><b>2</b>You are going to watch parts of a talk by a Y Combinator partner who used to work at Airbnb. Who should a start-up talk to before it builds a product? What would you ask them? Make a list.</p>",
  "<p class=\"ins\"><b>2</b>You are going to watch parts of a video about parmesan — one of the most expensive hard cheeses in the world. Why do you think shoppers pay so much for it? How can a cheese company find out what shoppers want before it launches a new cheese? Make two lists.</p>"),
 ("<p class=\"ins\"><b>3</b>Watch the parts of the video. Were any of your ideas from Exercise 2 mentioned? Answer the questions for each part.</p>",
  "<p class=\"ins\"><b>3</b>Watch the three parts of the video. Were any of your ideas from Exercise 2 mentioned? Answer the questions for each part. Then read the case file.</p>"),
 ("<div class=\"vA\">__FA__</div>", "<div class=\"vA\">__FA__" + CASE + "</div>"),
 ("<p class=\"ins\"><b>4</b>Watch again and decide", "<p class=\"ins\"><b>4</b>Watch again and use the case file. Decide"),
 ("<div class=\"vA\"><p class=\"ins\"><b>5</b>Discuss. He says users usually have good problems but bad solutions. What does he mean? Has a client or manager ever asked you for a feature that turned out to be the wrong solution? Who talks to users in your company?</p></div>",
  "<div class=\"vA\"><p class=\"ins\"><b>5</b>Discuss. Parmesan sells a story: origin, tradition, a long maturation and a protected name. Could a Ukrainian hard cheese do the same? What would shoppers need to believe — and how would you find out if they would pay more?</p></div>"),
 ("Research words people use in tech. Read the explanation and say the word. Then tell a short story from your work where you use it.",
  "Research and cheese words. Read the explanation and say the word. Then tell a short story from your work where you use it."),
 ("<b>10A</b>Think of an everyday product or app you use. Choose two well-known brands for it", "<b>10A</b>Think of a hard cheese you know well. Choose two well-known brands for it"),
 ("<div class=\"chips\"><span>Notion vs Obsidian</span><span>Duolingo vs Babbel</span><span>Spotify vs Apple Music</span><span>Revolut vs Monobank</span><span>Slack vs Microsoft Teams</span><span>Figma vs Canva</span></div>",
  "<div class=\"chips\"><span>Zveni Hora vs Pyriatyn</span><span>Parmigiano Reggiano vs Grana Padano</span><span>Dutch Gouda vs a Ukrainian gouda</span><span>A brand vs a private-label cheese</span><span>Hard cheese vs a ‘cheese product’</span><span>Our brand vs our main competitor</span></div>"),
 ("placeholder=\"e.g. an AI meeting summary inside Slack\"", "placeholder=\"e.g. a 12-month aged hard cheese, pre-grated, 150 g\""),
 ("<div><b>Their life, not your idea</b>Don’t pitch the feature. Ask how they do things now.</div>", "<div><b>Their life, not your idea</b>Don’t pitch the product. Ask how they buy and use cheese now.</div>"),
 ("In 10D, present to a sceptical US stakeholder — your teacher.", "In 10D, present to a sceptical retail buyer or CEO — your teacher."),
 ("<i>gauge interest in a feature</i>", "<i>gauge interest in a new cheese</i>"),
 ("'<title>1.1 Research in tech — Lesson</title>\\n'", "'<title>1.1 Market research: hard cheese — Lesson</title>\\n'"),
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
