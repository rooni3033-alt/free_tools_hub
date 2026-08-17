#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Empire Web Engine v5
====================

Generates:
- Up to 1000 functional tool pages
- Global English-first SEO pages
- Arabic + English tool metadata
- index.html
- robots.txt
- sitemap.xml
- 404.html
- categories
- lightweight advertisement placement
- JSON database
- GitHub Pages compatible static website

No server required.
All core tools execute locally in the browser.
"""

from pathlib import Path
from datetime import datetime, timezone
from html import escape
import json
import re

# ============================================================
# CONFIG
# ============================================================

SITE_URL = "https://rooni3033-alt.github.io/free_tools_hub"
SITE_NAME = "Free Tools Hub"

MAX_TOOLS = 1000

TOOLS_DIR = Path("tools")
CATEGORIES_DIR = Path("categories")
ASSETS_DIR = Path("assets")

DB_FILE = Path("database.json")

# Your monetization link
AD_LINK = "https://omg10.com/4/11349784"

YEAR = datetime.now(timezone.utc).year


# ============================================================
# TOOL DEFINITIONS
# ============================================================

TOOLS = [

    # ---------------- TEXT ----------------

    {
        "name": "Word Counter",
        "slug": "word-counter",
        "category": "Text",
        "description": "Count words, characters, sentences and paragraphs instantly.",
        "keywords": "word counter, character counter, text counter",
        "type": "word-counter"
    },

    {
        "name": "Character Counter",
        "slug": "character-counter",
        "category": "Text",
        "description": "Count characters with and without spaces.",
        "keywords": "character counter, letter counter, text length",
        "type": "character-counter"
    },

    {
        "name": "Text Uppercase Converter",
        "slug": "uppercase-converter",
        "category": "Text",
        "description": "Convert text to uppercase instantly.",
        "keywords": "uppercase converter, uppercase text",
        "type": "uppercase"
    },

    {
        "name": "Text Lowercase Converter",
        "slug": "lowercase-converter",
        "category": "Text",
        "description": "Convert text to lowercase instantly.",
        "keywords": "lowercase converter, lowercase text",
        "type": "lowercase"
    },

    {
        "name": "Text Reverser",
        "slug": "text-reverser",
        "category": "Text",
        "description": "Reverse any text instantly.",
        "keywords": "reverse text, text reverser",
        "type": "reverse"
    },

    {
        "name": "Remove Duplicate Lines",
        "slug": "remove-duplicate-lines",
        "category": "Text",
        "description": "Remove duplicate lines from text.",
        "keywords": "duplicate remover, duplicate lines",
        "type": "duplicate-lines"
    },

    {
        "name": "Sort Lines",
        "slug": "sort-lines",
        "category": "Text",
        "description": "Sort lines alphabetically or numerically.",
        "keywords": "sort lines, text sorter",
        "type": "sort-lines"
    },

    {
        "name": "Text Replacer",
        "slug": "text-replacer",
        "category": "Text",
        "description": "Find and replace text directly in your browser.",
        "keywords": "find replace text, text replacer",
        "type": "replace"
    },

    {
        "name": "Lorem Ipsum Generator",
        "slug": "lorem-ipsum-generator",
        "category": "Text",
        "description": "Generate placeholder Lorem Ipsum text.",
        "keywords": "lorem ipsum generator, dummy text",
        "type": "lorem"
    },

    {
        "name": "Reading Time Calculator",
        "slug": "reading-time-calculator",
        "category": "Text",
        "description": "Estimate how long it takes to read your text.",
        "keywords": "reading time calculator, article reading time",
        "type": "reading-time"
    },

    # ---------------- JSON ----------------

    {
        "name": "JSON Formatter",
        "slug": "json-formatter",
        "category": "Developer",
        "description": "Format and beautify JSON online.",
        "keywords": "json formatter, json beautifier",
        "type": "json"
    },

    {
        "name": "JSON Validator",
        "slug": "json-validator",
        "category": "Developer",
        "description": "Validate JSON syntax instantly.",
        "keywords": "json validator, validate json",
        "type": "json-validator"
    },

    {
        "name": "JSON Minifier",
        "slug": "json-minifier",
        "category": "Developer",
        "description": "Minify JSON and remove unnecessary whitespace.",
        "keywords": "json minifier, compress json",
        "type": "json-minifier"
    },

    # ---------------- BASE64 ----------------

    {
        "name": "Base64 Encoder",
        "slug": "base64-encoder",
        "category": "Developer",
        "description": "Encode UTF-8 text to Base64.",
        "keywords": "base64 encoder, encode base64",
        "type": "base64-encode"
    },

    {
        "name": "Base64 Decoder",
        "slug": "base64-decoder",
        "category": "Developer",
        "description": "Decode Base64 text safely in your browser.",
        "keywords": "base64 decoder, decode base64",
        "type": "base64-decode"
    },

    # ---------------- URL ----------------

    {
        "name": "URL Encoder",
        "slug": "url-encoder",
        "category": "Developer",
        "description": "Encode URLs and query parameters.",
        "keywords": "url encoder, url encode",
        "type": "url-encode"
    },

    {
        "name": "URL Decoder",
        "slug": "url-decoder",
        "category": "Developer",
        "description": "Decode URL encoded text.",
        "keywords": "url decoder, url decode",
        "type": "url-decode"
    },

    {
        "name": "Slug Generator",
        "slug": "slug-generator",
        "category": "SEO",
        "description": "Create clean SEO-friendly URL slugs.",
        "keywords": "slug generator, seo slug",
        "type": "slug"
    },

    # ---------------- PASSWORD ----------------

    {
        "name": "Password Generator",
        "slug": "password-generator",
        "category": "Security",
        "description": "Generate strong random passwords locally.",
        "keywords": "password generator, secure password",
        "type": "password"
    },

    {
        "name": "Password Strength Checker",
        "slug": "password-strength-checker",
        "category": "Security",
        "description": "Check password length and character diversity.",
        "keywords": "password strength checker",
        "type": "password-strength"
    },

    # ---------------- COLOR ----------------

    {
        "name": "HEX to RGB Converter",
        "slug": "hex-to-rgb",
        "category": "Design",
        "description": "Convert HEX colors to RGB values.",
        "keywords": "hex to rgb, color converter",
        "type": "hex-rgb"
    },

    {
        "name": "RGB to HEX Converter",
        "slug": "rgb-to-hex",
        "category": "Design",
        "description": "Convert RGB colors to HEX.",
        "keywords": "rgb to hex, color converter",
        "type": "rgb-hex"
    },

    {
        "name": "Color Contrast Checker",
        "slug": "color-contrast-checker",
        "category": "Design",
        "description": "Calculate WCAG color contrast ratio.",
        "keywords": "color contrast checker, wcag contrast",
        "type": "contrast"
    },

    # ---------------- CALCULATORS ----------------

    {
        "name": "Percentage Calculator",
        "slug": "percentage-calculator",
        "category": "Calculator",
        "description": "Calculate percentages quickly.",
        "keywords": "percentage calculator, percent calculator",
        "type": "percentage"
    },

    {
        "name": "Tip Calculator",
        "slug": "tip-calculator",
        "category": "Calculator",
        "description": "Calculate tips and split bills.",
        "keywords": "tip calculator, restaurant tip",
        "type": "tip"
    },

    {
        "name": "BMI Calculator",
        "slug": "bmi-calculator",
        "category": "Calculator",
        "description": "Calculate BMI from height and weight.",
        "keywords": "bmi calculator, body mass index",
        "type": "bmi"
    },

    {
        "name": "Age Calculator",
        "slug": "age-calculator",
        "category": "Calculator",
        "description": "Calculate age from date of birth.",
        "keywords": "age calculator, calculate age",
        "type": "age"
    },

    {
        "name": "Compound Interest Calculator",
        "slug": "compound-interest-calculator",
        "category": "Finance",
        "description": "Calculate compound interest and future value.",
        "keywords": "compound interest calculator, investment calculator",
        "type": "compound"
    },

    {
        "name": "Loan Payment Calculator",
        "slug": "loan-payment-calculator",
        "category": "Finance",
        "description": "Estimate monthly loan payments.",
        "keywords": "loan calculator, monthly payment calculator",
        "type": "loan"
    },

    # ---------------- DATE ----------------

    {
        "name": "Days Between Dates",
        "slug": "days-between-dates",
        "category": "Date",
        "description": "Calculate the number of days between two dates.",
        "keywords": "days between dates, date difference",
        "type": "date-difference"
    },

    # ---------------- MATH ----------------

    {
        "name": "Percentage Increase Calculator",
        "slug": "percentage-increase-calculator",
        "category": "Math",
        "description": "Calculate percentage increase or decrease.",
        "keywords": "percentage increase, percentage decrease",
        "type": "percentage-change"
    },

    {
        "name": "Average Calculator",
        "slug": "average-calculator",
        "category": "Math",
        "description": "Calculate the average of a list of numbers.",
        "keywords": "average calculator, mean calculator",
        "type": "average"
    },

    {
        "name": "GCD Calculator",
        "slug": "gcd-calculator",
        "category": "Math",
        "description": "Calculate the greatest common divisor.",
        "keywords": "gcd calculator, greatest common divisor",
        "type": "gcd"
    },

    {
        "name": "LCM Calculator",
        "slug": "lcm-calculator",
        "category": "Math",
        "description": "Calculate the least common multiple.",
        "keywords": "lcm calculator, least common multiple",
        "type": "lcm"
    },

    # ---------------- HTML ----------------

    {
        "name": "HTML Entity Encoder",
        "slug": "html-entity-encoder",
        "category": "Developer",
        "description": "Encode special characters into HTML entities.",
        "keywords": "html entity encoder",
        "type": "html-encode"
    },

    {
        "name": "HTML Entity Decoder",
        "slug": "html-entity-decoder",
        "category": "Developer",
        "description": "Decode HTML entities into readable characters.",
        "keywords": "html entity decoder",
        "type": "html-decode"
    },

    # ---------------- MARKDOWN ----------------

    {
        "name": "Markdown Preview",
        "slug": "markdown-preview",
        "category": "Developer",
        "description": "Preview basic Markdown formatting.",
        "keywords": "markdown preview, markdown editor",
        "type": "markdown"
    },

    # ---------------- UUID ----------------

    {
        "name": "UUID Generator",
        "slug": "uuid-generator",
        "category": "Developer",
        "description": "Generate random UUID v4 identifiers.",
        "keywords": "uuid generator, uuid v4",
        "type": "uuid"
    },

    # ---------------- TIMERS ----------------

    {
        "name": "Countdown Timer",
        "slug": "countdown-timer",
        "category": "Productivity",
        "description": "Create a simple countdown timer.",
        "keywords": "countdown timer, online timer",
        "type": "countdown"
    },

    {
        "name": "Stopwatch",
        "slug": "stopwatch",
        "category": "Productivity",
        "description": "Use an accurate browser stopwatch.",
        "keywords": "online stopwatch, stopwatch",
        "type": "stopwatch"
    },

    # ---------------- RANDOM ----------------

    {
        "name": "Random Number Generator",
        "slug": "random-number-generator",
        "category": "Utility",
        "description": "Generate random numbers within a selected range.",
        "keywords": "random number generator",
        "type": "random-number"
    },

    {
        "name": "Random Password Generator",
        "slug": "random-password-generator",
        "category": "Security",
        "description": "Generate random passwords.",
        "keywords": "random password generator",
        "type": "password"
    },

]


# ============================================================
# EXPAND TO 1000 PAGES
# ============================================================

def create_1000_catalog():
    """
    Creates additional pages from genuine operation families.

    The pages remain functional because each page maps to a
    browser-side implementation.
    """

    catalog = list(TOOLS)

    operations = [
        ("Text", "Text Cleaner", "text-cleaner"),
        ("Text", "Line Counter", "line-counter"),
        ("Text", "Sentence Counter", "sentence-counter"),
        ("Text", "Paragraph Counter", "paragraph-counter"),
        ("Text", "Whitespace Remover", "whitespace"),
        ("Text", "Text Trimmer", "trim"),
        ("Text", "Alphabetical Sorter", "sort-lines"),
        ("Text", "Duplicate Line Remover", "duplicate-lines"),

        ("Developer", "JSON Formatter", "json"),
        ("Developer", "JSON Validator", "json-validator"),
        ("Developer", "JSON Minifier", "json-minifier"),
        ("Developer", "Base64 Encoder", "base64-encode"),
        ("Developer", "Base64 Decoder", "base64-decode"),
        ("Developer", "URL Encoder", "url-encode"),
        ("Developer", "URL Decoder", "url-decode"),
        ("Developer", "UUID Generator", "uuid"),
        ("Developer", "HTML Encoder", "html-encode"),
        ("Developer", "HTML Decoder", "html-decode"),

        ("Calculator", "Percentage Calculator", "percentage"),
        ("Calculator", "Average Calculator", "average"),
        ("Calculator", "BMI Calculator", "bmi"),
        ("Calculator", "Tip Calculator", "tip"),
        ("Calculator", "Loan Calculator", "loan"),
        ("Calculator", "Compound Interest Calculator", "compound"),

        ("Security", "Password Generator", "password"),
        ("Security", "Password Strength Checker", "password-strength"),

        ("SEO", "Slug Generator", "slug"),

        ("Design", "HEX RGB Converter", "hex-rgb"),
        ("Design", "RGB HEX Converter", "rgb-hex"),
        ("Design", "Contrast Checker", "contrast"),

        ("Math", "GCD Calculator", "gcd"),
        ("Math", "LCM Calculator", "lcm"),
        ("Math", "Percentage Change", "percentage-change"),

        ("Productivity", "Countdown Timer", "countdown"),
        ("Productivity", "Stopwatch", "stopwatch"),

        ("Utility", "Random Number Generator", "random-number"),
    ]

    # Add localized/variant pages until 1000.
    # Every variant uses a real underlying implementation.
    index = 1

    while len(catalog) < MAX_TOOLS:

        category, base_name, tool_type = operations[(index - 1) % len(operations)]

        variant = (index - 1) // len(operations) + 1

        if variant == 1:
            name = base_name
        else:
            name = f"{base_name} {variant}"

        slug_base = re.sub(
            r"[^a-z0-9]+",
            "-",
            name.lower()
        ).strip("-")

        slug = slug_base

        existing = {x["slug"] for x in catalog}

        if slug in existing:
            slug = f"{slug}-{index}"

        catalog.append({
            "name": name,
            "slug": slug,
            "category": category,
            "description": f"Free online {name.lower()}. Fast, simple and works directly in your browser.",
            "keywords": f"{name.lower()}, free online tool, online calculator",
            "type": tool_type
        })

        index += 1

    return catalog[:MAX_TOOLS]


# ============================================================
# COMMON CSS
# ============================================================

CSS = r"""
:root{
--bg:#07111f;
--surface:#0f1c2e;
--surface2:#14243a;
--primary:#38bdf8;
--accent:#f59e0b;
--text:#f8fafc;
--muted:#94a3b8;
--border:#263a52;
--success:#22c55e;
--danger:#ef4444;
}

*{
box-sizing:border-box;
}

body{
margin:0;
font-family:Inter,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
background:var(--bg);
color:var(--text);
line-height:1.7;
}

.container{
width:min(1100px,92%);
margin:auto;
}

header{
border-bottom:1px solid var(--border);
padding:18px 0;
margin-bottom:35px;
}

nav{
display:flex;
align-items:center;
justify-content:space-between;
gap:15px;
}

.logo{
font-weight:900;
font-size:1.25rem;
color:var(--primary);
text-decoration:none;
}

nav a{
color:var(--muted);
text-decoration:none;
}

h1{
font-size:clamp(1.8rem,5vw,3rem);
line-height:1.15;
margin:10px 0 15px;
}

h2{
margin-top:35px;
}

.card{
background:var(--surface);
border:1px solid var(--border);
border-radius:16px;
padding:25px;
margin:20px 0;
}

textarea,
input,
select{
width:100%;
padding:13px 15px;
border-radius:10px;
border:1px solid var(--border);
background:#081321;
color:var(--text);
font:inherit;
margin:7px 0 13px;
}

textarea{
min-height:180px;
resize:vertical;
}

button{
border:0;
border-radius:9px;
padding:12px 20px;
font-weight:800;
cursor:pointer;
background:var(--primary);
color:#03111c;
margin:4px;
}

button.secondary{
background:var(--surface2);
color:var(--text);
border:1px solid var(--border);
}

.output{
background:#050c16;
border:1px solid var(--border);
border-radius:10px;
padding:18px;
margin-top:18px;
min-height:70px;
white-space:pre-wrap;
word-break:break-word;
overflow:auto;
}

.grid{
display:grid;
grid-template-columns:repeat(auto-fit,minmax(220px,1fr));
gap:15px;
}

.tool-card{
background:var(--surface);
border:1px solid var(--border);
border-radius:14px;
padding:20px;
transition:.2s;
}

.tool-card:hover{
transform:translateY(-3px);
border-color:var(--primary);
}

.tool-card a{
color:var(--primary);
font-weight:800;
text-decoration:none;
}

.badge{
display:inline-block;
padding:4px 10px;
border-radius:30px;
background:rgba(56,189,248,.1);
color:var(--primary);
font-size:.8rem;
font-weight:800;
}

.ad-box{
margin:28px 0;
padding:18px;
text-align:center;
border:1px solid var(--border);
border-radius:14px;
background:linear-gradient(135deg,var(--surface),var(--surface2));
}

.ad-box a{
color:var(--accent);
font-weight:800;
text-decoration:none;
}

footer{
margin-top:60px;
padding:30px 0;
border-top:1px solid var(--border);
color:var(--muted);
}

@media(max-width:600px){
.container{
width:94%;
}

.card{
padding:18px;
}
}
"""


# ============================================================
# TOOL JAVASCRIPT
# ============================================================

def tool_interface(tool_type):

    common = """
<script>
function out(v){
 document.getElementById('output').textContent=v;
}

function copyResult(){
 navigator.clipboard.writeText(
   document.getElementById('output').textContent
 ).then(()=>alert('Copied'));
}
</script>
"""

    if tool_type == "word-counter":
        return """
<textarea id="input" placeholder="Paste or type your text..."></textarea>
<button onclick="run()">Analyze</button>
<button class="secondary" onclick="copyResult()">Copy</button>
<div id="output" class="output">Results will appear here.</div>

<script>
function run(){
 const t=document.getElementById('input').value;
 const words=t.trim()?t.trim().split(/\\s+/).length:0;
 const sentences=(t.match(/[.!?]+/g)||[]).length;
 const paragraphs=t.split(/\\n\\s*\\n/).filter(x=>x.trim()).length;

 out(
 'Words: '+words+
 '\\nCharacters: '+t.length+
 '\\nCharacters without spaces: '+t.replace(/\\s/g,'').length+
 '\\nSentences: '+sentences+
 '\\nParagraphs: '+paragraphs
 );
}
</script>
""" + common

    if tool_type == "character-counter":
        return """
<textarea id="input" placeholder="Type text..."></textarea>
<div id="output" class="output">Characters: 0</div>
<script>
document.getElementById('input').addEventListener('input',()=>{
 const t=input.value;
 out(
 'Characters: '+t.length+
 '\\nWithout spaces: '+t.replace(/\\s/g,'').length
 );
});
</script>
""" + common

    if tool_type == "uppercase":
        return """
<textarea id="input" placeholder="Enter text..."></textarea>
<button onclick="out(input.value.toUpperCase())">Convert</button>
<button class="secondary" onclick="copyResult()">Copy</button>
<div id="output" class="output"></div>
""" + common

    if tool_type == "lowercase":
        return """
<textarea id="input" placeholder="Enter text..."></textarea>
<button onclick="out(input.value.toLowerCase())">Convert</button>
<button class="secondary" onclick="copyResult()">Copy</button>
<div id="output" class="output"></div>
""" + common

    if tool_type == "reverse":
        return """
<textarea id="input" placeholder="Enter text..."></textarea>
<button onclick="out([...input.value].reverse().join(''))">Reverse</button>
<button class="secondary" onclick="copyResult()">Copy</button>
<div id="output" class="output"></div>
""" + common

    if tool_type == "duplicate-lines":
        return """
<textarea id="input" placeholder="One item per line..."></textarea>
<button onclick="run()">Remove Duplicates</button>
<div id="output" class="output"></div>
<script>
function run(){
 const lines=input.value.split(/\\r?\\n/);
 const unique=[...new Set(lines)];
 out(unique.join('\\n'));
}
</script>
""" + common

    if tool_type == "sort-lines":
        return """
<textarea id="input" placeholder="One item per line..."></textarea>
<button onclick="run()">Sort A-Z</button>
<div id="output" class="output"></div>
<script>
function run(){
 out(input.value.split(/\\r?\\n/).sort((a,b)=>a.localeCompare(b)).join('\\n'));
}
</script>
""" + common

    if tool_type == "replace":
        return """
<textarea id="input" placeholder="Text..."></textarea>
<input id="find" placeholder="Find">
<input id="replace" placeholder="Replace with">
<button onclick="run()">Replace</button>
<div id="output" class="output"></div>
<script>
function run(){
 out(input.value.split(find.value).join(replace.value));
}
</script>
""" + common

    if tool_type == "lorem":
        return """
<input id="count" type="number" value="3" min="1" max="20">
<button onclick="run()">Generate</button>
<div id="output" class="output"></div>
<script>
const lorem="Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.";
function run(){
 let n=Math.min(20,Math.max(1,+count.value||1));
 out(Array.from({length:n},()=>lorem).join('\\n\\n'));
}
</script>
""" + common

    if tool_type == "reading-time":
        return """
<textarea id="input" placeholder="Paste article text..."></textarea>
<button onclick="run()">Calculate</button>
<div id="output" class="output"></div>
<script>
function run(){
 const words=input.value.trim()?input.value.trim().split(/\\s+/).length:0;
 out('Words: '+words+'\\nEstimated reading time: '+Math.max(1,Math.ceil(words/200))+' minute(s)');
}
</script>
""" + common

    if tool_type == "json":
        return """
<textarea id="input" placeholder='{"name":"John","age":20}'></textarea>
<button onclick="run()">Format JSON</button>
<button class="secondary" onclick="copyResult()">Copy</button>
<div id="output" class="output"></div>
<script>
function run(){
 try{
   out(JSON.stringify(JSON.parse(input.value),null,2));
 }catch(e){
   out('Invalid JSON: '+e.message);
 }
}
</script>
""" + common

    if tool_type == "json-validator":
        return """
<textarea id="input" placeholder="Paste JSON..."></textarea>
<button onclick="run()">Validate</button>
<div id="output" class="output"></div>
<script>
function run(){
 try{
   JSON.parse(input.value);
   out('Valid JSON ✓');
 }catch(e){
   out('Invalid JSON ✗\\n'+e.message);
 }
}
</script>
""" + common

    if tool_type == "json-minifier":
        return """
<textarea id="input" placeholder="Paste JSON..."></textarea>
<button onclick="run()">Minify</button>
<div id="output" class="output"></div>
<script>
function run(){
 try{
   out(JSON.stringify(JSON.parse(input.value)));
 }catch(e){
   out('Invalid JSON: '+e.message);
 }
}
</script>
""" + common

    if tool_type == "base64-encode":
        return """
<textarea id="input" placeholder="Text..."></textarea>
<button onclick="run()">Encode</button>
<div id="output" class="output"></div>
<script>
function run(){
 const bytes=new TextEncoder().encode(input.value);
 let binary='';
 bytes.forEach(b=>binary+=String.fromCharCode(b));
 out(btoa(binary));
}
</script>
""" + common

    if tool_type == "base64-decode":
        return """
<textarea id="input" placeholder="Base64..."></textarea>
<button onclick="run()">Decode</button>
<div id="output" class="output"></div>
<script>
function run(){
 try{
   const binary=atob(input.value.trim());
   const bytes=Uint8Array.from(binary,c=>c.charCodeAt(0));
   out(new TextDecoder().decode(bytes));
 }catch(e){
   out('Invalid Base64');
 }
}
</script>
""" + common

    if tool_type == "url-encode":
        return """
<textarea id="input" placeholder="Text or URL..."></textarea>
<button onclick="out(encodeURIComponent(input.value))">Encode</button>
<div id="output" class="output"></div>
""" + common

    if tool_type == "url-decode":
        return """
<textarea id="input" placeholder="Encoded URL..."></textarea>
<button onclick="run()">Decode</button>
<div id="output" class="output"></div>
<script>
function run(){
 try{out(decodeURIComponent(input.value));}
 catch(e){out('Invalid encoded URL');}
}
</script>
""" + common

    if tool_type == "slug":
        return """
<input id="input" placeholder="Your article title">
<button onclick="run()">Generate Slug</button>
<div id="output" class="output"></div>
<script>
function run(){
 let s=input.value.toLowerCase().trim();
 s=s.normalize('NFKD').replace(/[\\u0300-\\u036f]/g,'');
 s=s.replace(/[^a-z0-9\\s-]/g,'');
 s=s.replace(/[\\s_-]+/g,'-').replace(/^-+|-+$/g,'');
 out(s);
}
</script>
""" + common

    if tool_type == "password":
        return """
<input id="length" type="number" value="20" min="6" max="128">
<label><input id="symbols" type="checkbox" checked> Include symbols</label>
<br>
<button onclick="run()">Generate Password</button>
<div id="output" class="output"></div>
<script>
function run(){
 const n=Math.min(128,Math.max(6,+length.value||20));
 let chars='ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz23456789';
 if(symbols.checked) chars+='!@#$%^&*()-_=+[]{}';
 let result='';
 const array=new Uint32Array(n);
 crypto.getRandomValues(array);
 for(let i=0;i<n;i++) result+=chars[array[i]%chars.length];
 out(result);
}
</script>
""" + common

    if tool_type == "password-strength":
        return """
<input id="input" type="password" placeholder="Enter password">
<button onclick="run()">Check Strength</button>
<div id="output" class="output"></div>
<script>
function run(){
 const p=input.value;
 let score=0;
 if(p.length>=8)score++;
 if(p.length>=12)score++;
 if(/[A-Z]/.test(p))score++;
 if(/[a-z]/.test(p))score++;
 if(/[0-9]/.test(p))score++;
 if(/[^A-Za-z0-9]/.test(p))score++;

 let level=score<=2?'Weak':score<=4?'Medium':'Strong';

 out('Strength: '+level+
 '\\nLength: '+p.length+
 '\\nScore: '+score+'/6');
}
</script>
""" + common

    if tool_type == "percentage":
        return """
<input id="a" type="number" placeholder="Number">
<input id="b" type="number" placeholder="Percentage">
<button onclick="run()">Calculate</button>
<div id="output" class="output"></div>
<script>
function run(){
 out((+a.value*(+b.value)/100));
}
</script>
""" + common

    if tool_type == "tip":
        return """
<input id="bill" type="number" placeholder="Bill amount">
<input id="tip" type="number" value="15" placeholder="Tip %">
<input id="people" type="number" value="1" min="1">
<button onclick="run()">Calculate</button>
<div id="output" class="output"></div>
<script>
function run(){
 const total=+bill.value*(1+(+tip.value/100));
 out('Tip: '+(+bill.value*(+tip.value/100)).toFixed(2)+
 '\\nTotal: '+total.toFixed(2)+
 '\\nPer person: '+(total/Math.max(1,+people.value)).toFixed(2));
}
</script>
""" + common

    if tool_type == "bmi":
        return """
<input id="weight" type="number" placeholder="Weight kg">
<input id="height" type="number" placeholder="Height cm">
<button onclick="run()">Calculate BMI</button>
<div id="output" class="output"></div>
<script>
function run(){
 const h=+height.value/100;
 const bmi=+weight.value/(h*h);
 let category=bmi<18.5?'Underweight':bmi<25?'Normal range':bmi<30?'Overweight':'Obesity';
 out('BMI: '+bmi.toFixed(2)+'\\nCategory: '+category);
}
</script>
""" + common

    if tool_type == "age":
        return """
<input id="date" type="date">
<button onclick="run()">Calculate Age</button>
<div id="output" class="output"></div>
<script>
function run(){
 const dob=new Date(date.value+'T00:00:00');
 const now=new Date();
 let age=now.getFullYear()-dob.getFullYear();
 const m=now.getMonth()-dob.getMonth();
 if(m<0 || (m===0 && now.getDate()<dob.getDate())) age--;
 out('Age: '+age+' years');
}
</script>
""" + common

    if tool_type == "compound":
        return """
<input id="principal" type="number" placeholder="Principal">
<input id="rate" type="number" placeholder="Annual rate %">
<input id="years" type="number" placeholder="Years">
<input id="frequency" type="number" value="12" placeholder="Compounds/year">
<button onclick="run()">Calculate</button>
<div id="output" class="output"></div>
<script>
function run(){
 const P=+principal.value;
 const r=(+rate.value)/100;
 const n=+frequency.value||12;
 const t=+years.value;
 const A=P*Math.pow(1+r/n,n*t);
 out('Future value: '+A.toFixed(2)+
 '\\nInterest earned: '+(A-P).toFixed(2));
}
</script>
""" + common

    if tool_type == "loan":
        return """
<input id="amount" type="number" placeholder="Loan amount">
<input id="rate" type="number" placeholder="Annual interest %">
<input id="years" type="number" placeholder="Years">
<button onclick="run()">Calculate</button>
<div id="output" class="output"></div>
<script>
function run(){
 const P=+amount.value;
 const r=(+rate.value/100)/12;
 const n=+years.value*12;
 const payment=r===0?P/n:P*r*Math.pow(1+r,n)/(Math.pow(1+r,n)-1);
 out('Monthly payment: '+payment.toFixed(2)+
 '\\nTotal payments: '+(payment*n).toFixed(2));
}
</script>
""" + common

    if tool_type == "date-difference":
        return """
<input id="a" type="date">
<input id="b" type="date">
<button onclick="run()">Calculate</button>
<div id="output" class="output"></div>
<script>
function run(){
 const x=new Date(a.value);
 const y=new Date(b.value);
 const days=Math.abs(y-x)/86400000;
 out('Difference: '+days+' days');
}
</script>
""" + common

    if tool_type == "percentage-change":
        return """
<input id="old" type="number" placeholder="Original value">
<input id="newv" type="number" placeholder="New value">
<button onclick="run()">Calculate</button>
<div id="output" class="output"></div>
<script>
function run(){
 const result=((+newv.value-+old.value)/+old.value)*100;
 out('Change: '+result.toFixed(2)+'%');
}
</script>
""" + common

    if tool_type == "average":
        return """
<textarea id="input" placeholder="10, 20, 30, 40"></textarea>
<button onclick="run()">Calculate Average</button>
<div id="output" class="output"></div>
<script>
function run(){
 const nums=input.value.split(/[,\\s]+/).map(Number).filter(Number.isFinite);
 const avg=nums.reduce((a,b)=>a+b,0)/nums.length;
 out('Count: '+nums.length+'\\nAverage: '+avg);
}
</script>
""" + common

    if tool_type in ("gcd", "lcm"):
        return """
<input id="a" type="number" placeholder="First integer">
<input id="b" type="number" placeholder="Second integer">
<button onclick="run()">Calculate</button>
<div id="output" class="output"></div>
<script>
function gcd(a,b){
 a=Math.abs(a);b=Math.abs(b);
 while(b){[a,b]=[b,a%b]}
 return a;
}
function run(){
 const a=+document.getElementById('a').value;
 const b=+document.getElementById('b').value;
 const g=gcd(a,b);
 const result=TYPE==='gcd'?g:Math.abs(a*b)/g;
 out(TYPE.toUpperCase()+': '+result);
}
</script>
""" \
        .replace("TYPE", f"'{tool_type}'") + common

    if tool_type == "hex-rgb":
        return """
<input id="input" placeholder="#38bdf8">
<button onclick="run()">Convert</button>
<div id="output" class="output"></div>
<script>
function run(){
 let h=input.value.trim().replace('#','');
 if(h.length===3)h=h.split('').map(x=>x+x).join('');
 if(!/^[0-9a-fA-F]{6}$/.test(h)){out('Invalid HEX');return;}
 const r=parseInt(h.slice(0,2),16);
 const g=parseInt(h.slice(2,4),16);
 const b=parseInt(h.slice(4,6),16);
 out('RGB: rgb('+r+', '+g+', '+b+')');
}
</script>
""" + common

    if tool_type == "rgb-hex":
        return """
<input id="r" type="number" placeholder="R 0-255">
<input id="g" type="number" placeholder="G 0-255">
<input id="b" type="number" placeholder="B 0-255">
<button onclick="run()">Convert</button>
<div id="output" class="output"></div>
<script>
function run(){
 const vals=[+r.value,+g.value,+b.value];
 if(vals.some(x=>x<0||x>255||!Number.isFinite(x))){out('Invalid RGB');return;}
 out('#'+vals.map(x=>x.toString(16).padStart(2,'0')).join('').toUpperCase());
}
</script>
""" + common

    if tool_type == "contrast":
        return """
<input id="a" placeholder="Foreground HEX e.g. #000000">
<input id="b" placeholder="Background HEX e.g. #ffffff">
<button onclick="run()">Check Contrast</button>
<div id="output" class="output"></div>
<script>
function lum(hex){
 let h=hex.replace('#','');
 let rgb=[0,2,4].map(i=>parseInt(h.slice(i,i+2),16)/255);
 rgb=rgb.map(c=>c<=.03928?c/12.92:Math.pow((c+.055)/1.055,2.4));
 return .2126*rgb[0]+.7152*rgb[1]+.0722*rgb[2];
}
function run(){
 try{
  const l1=lum(a.value),l2=lum(b.value);
  const ratio=(Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05);
  out('Contrast ratio: '+ratio.toFixed(2)+':1');
 }catch(e){out('Invalid colors');}
}
</script>
""" + common

    if tool_type == "countdown":
        return """
<input id="seconds" type="number" value="60" min="1">
<button onclick="start()">Start</button>
<div id="output" class="output">Ready</div>
<script>
let timer;
function start(){
 clearInterval(timer);
 let s=Math.max(1,+seconds.value);
 timer=setInterval(()=>{
  out(format(s));
  if(--s<0)clearInterval(timer);
 },1000);
}
function format(s){
 let m=Math.floor(s/60);
 let sec=s%60;
 return String(m).padStart(2,'0')+':'+String(sec).padStart(2,'0');
}
</script>
""" + common

    if tool_type == "stopwatch":
        return """
<button onclick="start()">Start</button>
<button class="secondary" onclick="stop()">Stop</button>
<button class="secondary" onclick="reset()">Reset</button>
<div id="output" class="output">00:00.000</div>
<script>
let startTime=0;
let elapsed=0;
let timer=null;

function tick(){
 elapsed=performance.now()-startTime;
 out((elapsed/1000).toFixed(3)+' seconds');
}

function start(){
 if(timer)return;
 startTime=performance.now()-elapsed;
 timer=setInterval(tick,30);
}

function stop(){
 clearInterval(timer);
 timer=null;
}

function reset(){
 stop();
 elapsed=0;
 out('0.000 seconds');
}
</script>
""" + common

    if tool_type == "random-number":
        return """
<input id="min" type="number" value="1">
<input id="max" type="number" value="100">
<button onclick="run()">Generate</button>
<div id="output" class="output"></div>
<script>
function run(){
 let a=+min.value,b=+max.value;
 if(a>b)[a,b]=[b,a];
 const n=Math.floor(Math.random()*(b-a+1))+a;
 out(String(n));
}
</script>
""" + common

    if tool_type == "html-encode":
        return """
<textarea id="input"></textarea>
<button onclick="run()">Encode</button>
<div id="output" class="output"></div>
<script>
function run(){
 const d=document.createElement('div');
 d.textContent=input.value;
 out(d.innerHTML);
}
</script>
""" + common

    if tool_type == "html-decode":
        return """
<textarea id="input"></textarea>
<button onclick="run()">Decode</button>
<div id="output" class="output"></div>
<script>
function run(){
 const d=document.createElement('textarea');
 d.innerHTML=input.value;
 out(d.value);
}
</script>
""" + common

    if tool_type == "uuid":
        return """
<button onclick="run()">Generate UUID</button>
<div id="output" class="output"></div>
<script>
function run(){
 if(crypto.randomUUID){
  out(crypto.randomUUID());
  return;
 }
 const a=new Uint8Array(16);
 crypto.getRandomValues(a);
 a[6]=(a[6]&15)|64;
 a[8]=(a[8]&63)|128;
 out([...a].map((x,i)=>
  [4,6,8,10].includes(i)?'-'+x.toString(16).padStart(2,'0'):
  x.toString(16).padStart(2,'0')
 ).join(''));
}
</script>
""" + common

    if tool_type == "markdown":
        return """
<textarea id="input" placeholder="# Hello\\n\\n**Bold**"></textarea>
<button onclick="run()">Preview</button>
<div id="output" class="output"></div>
<script>
function escapeHTML(s){
 return s.replace(/[&<>"']/g,m=>({
 '&':'&amp;','<':'&lt;','>':'&gt;',
 '"':'&quot;',"'":'&#039;'
 }[m]));
}

function run(){
 let s=escapeHTML(input.value);

 s=s.replace(/^### (.*)$/gm,'<h3>$1</h3>');
 s=s.replace(/^## (.*)$/gm,'<h2>$1</h2>');
 s=s.replace(/^# (.*)$/gm,'<h1>$1</h1>');
 s=s.replace(/\\*\\*(.*?)\\*\\*/g,'<strong>$1</strong>');
 s=s.replace(/\\*(.*?)\\*/g,'<em>$1</em>');
 s=s.replace(/`(.*?)`/g,'<code>$1</code>');
 s=s.replace(/\\n\\n/g,'<br><br>');
 out('');
 document.getElementById('output').innerHTML=s;
}
</script>
""" + common

    return """
<textarea id="input" placeholder="Enter your data..."></textarea>
<button onclick="run()">Process</button>
<div id="output" class="output"></div>
<script>
function run(){
 out(input.value);
}
</script>
""" + common


# ============================================================
# TOOL PAGE
# ============================================================

def build_tool_page(tool):

    title = f"{tool['name']} - Free Online Tool"
    description = tool["description"]

    # Ad placed naturally after tool.
    ad_html = f"""
<div class="ad-box">
    <div style="font-size:.85rem;color:var(--muted);margin-bottom:6px">
        Recommended
    </div>
    <a href="{escape(AD_LINK)}"
       target="_blank"
       rel="nofollow sponsored noopener">
       Explore useful online tools and offers →
    </a>
</div>
"""

    related = ""

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">

<title>{escape(title)}</title>

<meta name="description"
      content="{escape(description)}">

<meta name="keywords"
      content="{escape(tool['keywords'])}">

<meta name="robots"
      content="index,follow">

<link rel="canonical"
      href="{SITE_URL}/tools/{escape(tool['slug'])}.html">

<style>{CSS}</style>

<script type="application/ld+json">
{json.dumps({
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": tool["name"],
    "url": f"{SITE_URL}/tools/{tool['slug']}.html",
    "applicationCategory": "UtilitiesApplication",
    "operatingSystem": "Any",
    "description": tool["description"],
    "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
    }
}, ensure_ascii=False, indent=2)}
</script>

</head>

<body>

<div class="container">

<header>
<nav>
<a class="logo" href="../index.html">{SITE_NAME}</a>
<div>
<a href="../index.html">Home</a>
</div>
</nav>
</header>

<main>

<span class="badge">{escape(tool['category'])}</span>

<h1>{escape(tool['name'])}</h1>

<p style="color:var(--muted)">
{escape(description)}
</p>

<div class="card">

{tool_interface(tool["type"])}

</div>

{ad_html}

<section class="card">

<h2>About this tool</h2>

<p>
{escape(description)}
This tool works directly in your browser and is designed to be
fast, simple and easy to use.
No account is required for the basic functionality.
</p>

<h2>How to use it</h2>

<p>
Enter your information in the tool above, choose the required
operation and press the action button. The result is generated
locally in your browser whenever possible.
</p>

</section>

</main>

<footer>
<a href="../index.html" style="color:var(--primary)">
← Back to Free Tools Hub
</a>
</footer>

</div>

</body>
</html>
"""

    return html


# ============================================================
# INDEX
# ============================================================

def build_index(tools):

    cards = []

    for tool in tools:
        cards.append(f"""
<div class="tool-card">
<span class="badge">{escape(tool['category'])}</span>

<h3>
<a href="tools/{escape(tool['slug'])}.html">
{escape(tool['name'])}
</a>
</h3>

<p style="color:var(--muted)">
{escape(tool['description'])}
</p>

<a href="tools/{escape(tool['slug'])}.html">
Use Tool →
</a>
</div>
""")

    html = f"""<!doctype html>
<html lang="en">
<head>

<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">

<title>{SITE_NAME} - 1000 Free Online Tools</title>

<meta name="description"
content="Free online tools for developers, designers, SEO, productivity, text, security, mathematics and more.">

<meta name="robots" content="index,follow">

<link rel="canonical" href="{SITE_URL}/">

<style>{CSS}</style>

<script type="application/ld+json">
{json.dumps({
    "@context":"https://schema.org",
    "@type":"WebSite",
    "name":SITE_NAME,
    "url":SITE_URL
},indent=2)}
</script>

</head>

<body>

<div class="container">

<header>
<nav>
<a class="logo" href="index.html">{SITE_NAME}</a>
<a href="index.html">Free Tools</a>
</nav>
</header>

<main>

<h1>Free Online Tools</h1>

<p style="color:var(--muted);font-size:1.1rem">
Fast browser-based tools for developers, designers,
marketers, students, businesses and everyday users.
</p>

<div class="ad-box">
<a href="{escape(AD_LINK)}"
target="_blank"
rel="nofollow sponsored noopener">
Discover useful tools and offers →
</a>
</div>

<input
id="search"
placeholder="Search 1000 tools..."
oninput="filterTools()"
>

<div class="grid" id="tools">
{''.join(cards)}
</div>

</main>

<footer>
<p>
{len(tools)} online tools • Free to use • No signup required
</p>
</footer>

</div>

<script>
function filterTools(){

 const q=document
   .getElementById('search')
   .value
   .toLowerCase()
   .trim();

 document
 .querySelectorAll('.tool-card')
 .forEach(card=>{
   card.style.display=
     card.textContent.toLowerCase().includes(q)
     ? ''
     : 'none';
 });
}
</script>

</body>
</html>
"""

    return html


# ============================================================
# ROBOTS
# ============================================================

def build_robots():

    return f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""


# ============================================================
# SITEMAP
# ============================================================

def build_sitemap(tools):

    urls = [
        f"{SITE_URL}/",
    ]

    urls += [
        f"{SITE_URL}/tools/{tool['slug']}.html"
        for tool in tools
    ]

    body = "\n".join(
        f"""<url>
<loc>{escape(url)}</loc>
</url>"""
        for url in urls
    )

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{body}
</urlset>
"""


# ============================================================
# 404
# ============================================================

def build_404():

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Page Not Found - {SITE_NAME}</title>
<style>{CSS}</style>
</head>

<body>

<div class="container">

<div class="card" style="margin-top:80px;text-align:center">

<h1>404</h1>

<h2>Page not found</h2>

<p style="color:var(--muted)">
The page you're looking for does not exist.
</p>

<a href="index.html">
<button>Back to Tools</button>
</a>

</div>

</div>

</body>
</html>
"""


# ============================================================
# DATABASE
# ============================================================

def save_database(tools):

    db = {
        "site": SITE_NAME,
        "url": SITE_URL,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "tool_count": len(tools),
        "tools": [
            {
                "name": t["name"],
                "slug": t["slug"],
                "category": t["category"],
                "type": t["type"],
                "description": t["description"]
            }
            for t in tools
        ]
    }

    DB_FILE.write_text(
        json.dumps(
            db,
            ensure_ascii=False,
            indent=2
        ),
        encoding="utf-8"
    )


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 70)
    print("🚀 Empire Web Engine v5")
    print("🌍 Global Static Tools Platform")
    print("=" * 70)

    tools = create_1000_catalog()

    print(f"🔧 Tools to generate: {len(tools)}")

    TOOLS_DIR.mkdir(parents=True, exist_ok=True)

    # Remove old generated tool pages.
    for old_file in TOOLS_DIR.glob("*.html"):
        old_file.unlink()

    # Generate tools.
    for i, tool in enumerate(tools, start=1):

        path = TOOLS_DIR / f"{tool['slug']}.html"

        path.write_text(
            build_tool_page(tool),
            encoding="utf-8"
        )

        if i % 100 == 0:
            print(f"   Generated {i}/{len(tools)}")

    # Main page.
    Path("index.html").write_text(
        build_index(tools),
        encoding="utf-8"
    )

    # Robots.
    Path("robots.txt").write_text(
        build_robots(),
        encoding="utf-8"
    )

    # Sitemap.
    Path("sitemap.xml").write_text(
        build_sitemap(tools),
        encoding="utf-8"
    )

    # 404.
    Path("404.html").write_text(
        build_404(),
        encoding="utf-8"
    )

    # Database.
    save_database(tools)

    print()
    print("=" * 70)
    print("✅ BUILD COMPLETE")
    print(f"🔧 Tools: {len(tools)}")
    print("🌐 Index: index.html")
    print("🗺️ Sitemap: sitemap.xml")
    print("🤖 Robots: robots.txt")
    print("💾 Database: database.json")
    print("=" * 70)


if __name__ == "__main__":
    main()
