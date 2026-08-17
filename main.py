#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
FREE TOOLS HUB — EMPIRE ENGINE V5
==================================

مولّد موقع أدوات عالمي.

المميزات:
- توليد صفحات أدوات ثابتة
- Registry مركزي للأدوات
- SEO لكل أداة
- Sitemap
- Robots.txt
- Categories
- Search index
- صفحات متوافقة مع GitHub Pages
- مكان مركزي للإعلان/Monetization
- لا يتم إنشاء أدوات وهمية على أنها أدوات حقيقية

تشغيل:
    python main.py
"""

from pathlib import Path
from datetime import datetime
import json
import html
import re


# ============================================================
# CONFIG
# ============================================================

SITE_NAME = "Free Tools Hub"

SITE_URL = "https://rooni3033-alt.github.io/free_tools_hub"

LANGUAGE = "en"

OUTPUT_DIR = Path(".")

TOOLS_DIR = OUTPUT_DIR / "tools"
CATEGORIES_DIR = OUTPUT_DIR / "categories"
ASSETS_DIR = OUTPUT_DIR / "assets"

DB_FILE = OUTPUT_DIR / "database.json"

# غيّر الرابط من هنا فقط
AD_LINK = "https://omg10.com/4/11349784"

# عدد الأدوات المستهدف
TARGET_TOOLS = 1000


# ============================================================
# DIRECTORIES
# ============================================================

def create_directories():
    TOOLS_DIR.mkdir(parents=True, exist_ok=True)
    CATEGORIES_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# HELPERS
# ============================================================

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def esc(text):
    return html.escape(str(text), quote=True)


def write_file(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# ============================================================
# DATABASE
# ============================================================

def load_database():

    if not DB_FILE.exists():
        return {
            "version": 5,
            "tools": [],
            "categories": [],
            "updated": None
        }

    try:

        with open(DB_FILE, "r", encoding="utf-8") as f:
            db = json.load(f)

        if not isinstance(db, dict):
            raise ValueError("Invalid database")

        db.setdefault("tools", [])
        db.setdefault("categories", [])

        return db

    except Exception:

        return {
            "version": 5,
            "tools": [],
            "categories": [],
            "updated": None
        }


def save_database(db):

    db["version"] = 5
    db["updated"] = datetime.utcnow().isoformat()

    write_file(
        DB_FILE,
        json.dumps(
            db,
            ensure_ascii=False,
            indent=2
        )
    )


# ============================================================
# MONETIZATION
# ============================================================

def ad_block():

    if not AD_LINK:
        return ""

    return f"""
<section class="monetization">
    <div class="ad-label">Sponsored</div>

    <a
        href="{esc(AD_LINK)}"
        target="_blank"
        rel="nofollow sponsored noopener"
    >
        Discover useful tools & offers
    </a>
</section>
"""


# ============================================================
# GLOBAL CSS
# ============================================================

GLOBAL_CSS = r"""
:root {
    --bg: #07111f;
    --surface: #0d1b2a;
    --surface2: #12243a;
    --border: #263b52;
    --text: #edf6ff;
    --muted: #9fb3c8;
    --primary: #38bdf8;
    --success: #22c55e;
    --danger: #ef4444;
    --radius: 14px;
}

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    background: var(--bg);
    color: var(--text);
    font-family:
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;

    line-height: 1.7;
}

a {
    color: var(--primary);
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

.container {
    width: min(1100px, calc(100% - 32px));
    margin: auto;
}

header {
    border-bottom: 1px solid var(--border);
    background: rgba(7,17,31,.96);
    position: sticky;
    top: 0;
    z-index: 20;
    backdrop-filter: blur(12px);
}

.nav {
    min-height: 68px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 20px;
}

.logo {
    font-size: 1.25rem;
    font-weight: 800;
}

.logo span {
    color: var(--primary);
}

.nav-links {
    display: flex;
    gap: 18px;
    flex-wrap: wrap;
}

.hero {
    padding: 70px 0 45px;
    text-align: center;
}

.hero h1 {
    font-size: clamp(2rem, 5vw, 4rem);
    line-height: 1.1;
    margin: 0 0 18px;
}

.hero p {
    max-width: 700px;
    margin: auto;
    color: var(--muted);
    font-size: 1.1rem;
}

.search {
    width: min(700px, 100%);
    margin: 30px auto 0;
}

.search input {
    width: 100%;
    padding: 16px 18px;
    background: var(--surface);
    border: 1px solid var(--border);
    color: var(--text);
    border-radius: 12px;
    font-size: 1rem;
    outline: none;
}

.grid {
    display: grid;
    grid-template-columns:
        repeat(auto-fill, minmax(240px, 1fr));
    gap: 16px;
}

.card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 20px;
    transition: transform .15s ease,
                border-color .15s ease;
}

.card:hover {
    transform: translateY(-2px);
    border-color: var(--primary);
}

.card h2,
.card h3 {
    margin-top: 0;
}

.muted {
    color: var(--muted);
}

.badge {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 999px;
    background: rgba(56,189,248,.1);
    border: 1px solid rgba(56,189,248,.25);
    color: var(--primary);
    font-size: .8rem;
}

.tool-page {
    padding: 45px 0;
}

.tool-box {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
    padding: 24px;
}

textarea,
input,
select {
    width: 100%;
    padding: 12px 14px;
    border-radius: 9px;
    border: 1px solid var(--border);
    background: #071421;
    color: var(--text);
    font: inherit;
    margin-bottom: 12px;
}

textarea {
    resize: vertical;
}

button {
    border: 0;
    border-radius: 9px;
    padding: 11px 18px;
    background: var(--primary);
    color: #03111c;
    font-weight: 800;
    cursor: pointer;
}

button:hover {
    opacity: .9;
}

.output {
    margin-top: 18px;
    padding: 16px;
    min-height: 80px;
    border-radius: 9px;
    border: 1px solid var(--border);
    background: #06101c;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
}

.monetization {
    margin: 35px 0;
    padding: 18px;
    border: 1px solid var(--border);
    border-radius: var(--radius);
    background: var(--surface2);
    text-align: center;
}

.ad-label {
    font-size: .7rem;
    text-transform: uppercase;
    letter-spacing: .08em;
    color: var(--muted);
    margin-bottom: 6px;
}

footer {
    margin-top: 70px;
    padding: 35px 0;
    border-top: 1px solid var(--border);
    color: var(--muted);
}

@media (max-width: 650px) {

    .nav {
        flex-direction: column;
        padding: 15px 0;
    }

    .hero {
        padding-top: 45px;
    }

    .grid {
        grid-template-columns: 1fr;
    }
}
"""


# ============================================================
# HTML SHELL
# ============================================================

def page_shell(
    title,
    description,
    body,
    canonical=None
):

    canonical = canonical or SITE_URL

    return f"""<!doctype html>
<html lang="{LANGUAGE}">
<head>

<meta charset="utf-8">

<meta
    name="viewport"
    content="width=device-width,initial-scale=1"
>

<title>{esc(title)}</title>

<meta
    name="description"
    content="{esc(description)}"
>

<link
    rel="canonical"
    href="{esc(canonical)}"
>

<meta
    property="og:type"
    content="website"
>

<meta
    property="og:title"
    content="{esc(title)}"
>

<meta
    property="og:description"
    content="{esc(description)}"
>

<meta
    property="og:url"
    content="{esc(canonical)}"
>

<style>
{GLOBAL_CSS}
</style>

</head>

<body>

<header>

<div class="container nav">

<a class="logo" href="{SITE_URL}/">
    Free <span>Tools Hub</span>
</a>

<nav class="nav-links">
    <a href="{SITE_URL}/">Home</a>
    <a href="{SITE_URL}/#tools">Tools</a>
    <a href="{SITE_URL}/#categories">Categories</a>
</nav>

</div>

</header>

<main>

{body}

</main>

<footer>

<div class="container">

Free Tools Hub — Free browser-based utilities.

</div>

</footer>

</body>
</html>
"""


# ============================================================
# TOOL REGISTRY
# ============================================================

TOOLS = [

    {
        "name": "JSON Formatter",
        "category": "Developer",
        "description":
            "Format and pretty-print JSON directly in your browser.",
        "engine": "json_formatter"
    },

    {
        "name": "JSON Validator",
        "category": "Developer",
        "description":
            "Validate JSON syntax instantly in your browser.",
        "engine": "json_validator"
    },

    {
        "name": "JSON Minifier",
        "category": "Developer",
        "description":
            "Minify JSON by removing unnecessary whitespace.",
        "engine": "json_minifier"
    },

    {
        "name": "Base64 Encoder",
        "category": "Developer",
        "description":
            "Encode text to Base64 locally in your browser.",
        "engine": "base64_encode"
    },

    {
        "name": "Base64 Decoder",
        "category": "Developer",
        "description":
            "Decode Base64 text directly in your browser.",
        "engine": "base64_decode"
    },

    {
        "name": "URL Encoder",
        "category": "Developer",
        "description":
            "Encode URLs and URL components safely.",
        "engine": "url_encode"
    },

    {
        "name": "URL Decoder",
        "category": "Developer",
        "description":
            "Decode URL encoded text.",
        "engine": "url_decode"
    },

    {
        "name": "Password Generator",
        "category": "Security",
        "description":
            "Generate strong random passwords locally.",
        "engine": "password_generator"
    },

    {
        "name": "Word Counter",
        "category": "Text",
        "description":
            "Count words, characters, sentences and paragraphs.",
        "engine": "word_counter"
    },

    {
        "name": "Character Counter",
        "category": "Text",
        "description":
            "Count characters in any text instantly.",
        "engine": "character_counter"
    },

    {
        "name": "Text Reverser",
        "category": "Text",
        "description":
            "Reverse text instantly.",
        "engine": "text_reverser"
    },

    {
        "name": "Duplicate Line Remover",
        "category": "Text",
        "description":
            "Remove duplicate lines from text.",
        "engine": "duplicate_lines"
    },

    {
        "name": "Percentage Calculator",
        "category": "Calculator",
        "description":
            "Calculate percentages quickly and accurately.",
        "engine": "percentage"
    },

    {
        "name": "Average Calculator",
        "category": "Calculator",
        "description":
            "Calculate the average of a list of numbers.",
        "engine": "average"
    },

    {
        "name": "BMI Calculator",
        "category": "Health",
        "description":
            "Calculate BMI from height and weight.",
        "engine": "bmi"
    },

    {
        "name": "Age Calculator",
        "category": "Calculator",
        "description":
            "Calculate age from a date of birth.",
        "engine": "age"
    },

    {
        "name": "Slug Generator",
        "category": "SEO",
        "description":
            "Convert text into clean URL slugs.",
        "engine": "slug"
    },

    {
        "name": "Color HEX Converter",
        "category": "Design",
        "description":
            "Convert HEX colors to RGB and preview them.",
        "engine": "hex_color"
    },

    {
        "name": "Unit Converter",
        "category": "Converter",
        "description":
            "Convert common metric and imperial units.",
        "engine": "unit"
    },

    {
        "name": "UUID Generator",
        "category": "Developer",
        "description":
            "Generate UUID v4 identifiers in your browser.",
        "engine": "uuid"
    },

]


# ============================================================
# TOOL ENGINES
# ============================================================

def engine_json_formatter():

    return """
<textarea id="input" rows="12"
placeholder="Paste JSON here..."></textarea>

<button onclick="run()">Format JSON</button>

<div id="output" class="output"></div>

<script>
function run() {

    const input =
        document.getElementById("input").value;

    try {

        const parsed = JSON.parse(input);

        document.getElementById("output")
            .textContent =
            JSON.stringify(parsed, null, 2);

    } catch (error) {

        document.getElementById("output")
            .textContent =
            "Invalid JSON: " + error.message;
    }
}
</script>
"""


def engine_json_validator():

    return """
<textarea id="input" rows="10"
placeholder="Paste JSON here..."></textarea>

<button onclick="run()">Validate</button>

<div id="output" class="output">
Waiting for JSON...
</div>

<script>
function run() {

    const value =
        document.getElementById("input").value;

    try {

        JSON.parse(value);

        document.getElementById("output")
            .textContent =
            "Valid JSON ✓";

    } catch (error) {

        document.getElementById("output")
            .textContent =
            "Invalid JSON ✗\\n" +
            error.message;
    }
}
</script>
"""


def engine_json_minifier():

    return """
<textarea id="input" rows="10"
placeholder="Paste JSON here..."></textarea>

<button onclick="run()">Minify</button>

<div id="output" class="output"></div>

<script>
function run() {

    try {

        const value =
            JSON.parse(
                document.getElementById("input").value
            );

        document.getElementById("output")
            .textContent =
            JSON.stringify(value);

    } catch (error) {

        document.getElementById("output")
            .textContent =
            "Invalid JSON: " +
            error.message;
    }
}
</script>
"""


def engine_base64_encode():

    return """
<textarea id="input" rows="8"
placeholder="Enter text..."></textarea>

<button onclick="run()">Encode</button>

<div id="output" class="output"></div>

<script>
function run() {

    const text =
        document.getElementById("input").value;

    const bytes =
        new TextEncoder().encode(text);

    let binary = "";

    bytes.forEach(
        b => binary += String.fromCharCode(b)
    );

    document.getElementById("output")
        .textContent =
        btoa(binary);
}
</script>
"""


def engine_base64_decode():

    return """
<textarea id="input" rows="8"
placeholder="Enter Base64..."></textarea>

<button onclick="run()">Decode</button>

<div id="output" class="output"></div>

<script>
function run() {

    try {

        const binary =
            atob(
                document.getElementById("input").value
            );

        const bytes =
            Uint8Array.from(
                binary,
                c => c.charCodeAt(0)
            );

        document.getElementById("output")
            .textContent =
            new TextDecoder().decode(bytes);

    } catch (error) {

        document.getElementById("output")
            .textContent =
            "Invalid Base64";
    }
}
</script>
"""


def engine_url_encode():

    return """
<textarea id="input" rows="6"
placeholder="Enter text or URL..."></textarea>

<button onclick="run()">Encode URL</button>

<div id="output" class="output"></div>

<script>
function run() {

    document.getElementById("output")
        .textContent =
        encodeURIComponent(
            document.getElementById("input").value
        );
}
</script>
"""


def engine_url_decode():

    return """
<textarea id="input" rows="6"
placeholder="Enter encoded URL..."></textarea>

<button onclick="run()">Decode URL</button>

<div id="output" class="output"></div>

<script>
function run() {

    try {

        document.getElementById("output")
            .textContent =
            decodeURIComponent(
                document.getElementById("input").value
            );

    } catch {

        document.getElementById("output")
            .textContent =
            "Invalid encoded URL";
    }
}
</script>
"""


def engine_password_generator():

    return """
<div>

<label>
Length
</label>

<input
    id="length"
    type="number"
    value="20"
    min="4"
    max="128"
>

</div>

<button onclick="run()">
Generate Password
</button>

<div id="output" class="output"></div>

<script>
function run() {

    const length =
        Math.min(
            128,
            Math.max(
                4,
                Number(
                    document.getElementById("length").value
                )
            )
        );

    const chars =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ" +
        "abcdefghijklmnopqrstuvwxyz" +
        "0123456789" +
        "!@#$%^&*()-_=+";

    const values =
        new Uint32Array(length);

    crypto.getRandomValues(values);

    let result = "";

    for (let i = 0; i < length; i++) {

        result +=
            chars[values[i] % chars.length];
    }

    document.getElementById("output")
        .textContent = result;
}
</script>
"""


def engine_word_counter():

    return """
<textarea id="input"
rows="12"
placeholder="Type or paste your text..."
oninput="run()"></textarea>

<div class="grid">

<div class="card">
<strong id="words">0</strong>
<div class="muted">Words</div>
</div>

<div class="card">
<strong id="chars">0</strong>
<div class="muted">Characters</div>
</div>

<div class="card">
<strong id="sentences">0</strong>
<div class="muted">Sentences</div>
</div>

</div>

<script>
function run() {

    const text =
        document.getElementById("input").value;

    const words =
        text.trim()
        ? text.trim().split(/\\s+/).length
        : 0;

    const sentences =
        text.match(/[.!?]+/g)?.length || 0;

    document.getElementById("words")
        .textContent = words;

    document.getElementById("chars")
        .textContent = text.length;

    document.getElementById("sentences")
        .textContent = sentences;
}
</script>
"""


def engine_character_counter():

    return """
<textarea
id="input"
rows="10"
oninput="run()"
placeholder="Enter text..."
></textarea>

<div id="output" class="output">
Characters: 0
</div>

<script>
function run() {

    const text =
        document.getElementById("input").value;

    document.getElementById("output")
        .textContent =
        "Characters: " + text.length;
}
</script>
"""


def engine_text_reverser():

    return """
<textarea
id="input"
rows="8"
placeholder="Enter text..."
></textarea>

<button onclick="run()">
Reverse
</button>

<div id="output" class="output"></div>

<script>
function run() {

    const value =
        document.getElementById("input").value;

    document.getElementById("output")
        .textContent =
        [...value].reverse().join("");
}
</script>
"""


def engine_duplicate_lines():

    return """
<textarea
id="input"
rows="12"
placeholder="One item per line..."
></textarea>

<button onclick="run()">
Remove Duplicates
</button>

<div id="output" class="output"></div>

<script>
function run() {

    const lines =
        document.getElementById("input")
        .value
        .split(/\\r?\\n/);

    const unique =
        [...new Set(lines)];

    document.getElementById("output")
        .textContent =
        unique.join("\\n");
}
</script>
"""


def engine_percentage():

    return """
<input
id="value"
type="number"
placeholder="Value"
>

<input
id="percent"
type="number"
placeholder="Percentage"
>

<button onclick="run()">
Calculate
</button>

<div id="output" class="output"></div>

<script>
function run() {

    const value =
        Number(
            document.getElementById("value").value
        );

    const percent =
        Number(
            document.getElementById("percent").value
        );

    document.getElementById("output")
        .textContent =
        percent + "% of " +
        value +
        " = " +
        (value * percent / 100);
}
</script>
"""


def engine_average():

    return """
<textarea
id="input"
rows="6"
placeholder="10, 20, 30, 40"
></textarea>

<button onclick="run()">
Calculate Average
</button>

<div id="output" class="output"></div>

<script>
function run() {

    const values =
        document.getElementById("input")
        .value
        .split(/[,\\s]+/)
        .map(Number)
        .filter(Number.isFinite);

    if (!values.length) {

        document.getElementById("output")
            .textContent =
            "Enter numbers.";

        return;
    }

    const total =
        values.reduce(
            (sum, value) => sum + value,
            0
        );

    document.getElementById("output")
        .textContent =
        "Average: " +
        (total / values.length);
}
</script>
"""


def engine_bmi():

    return """
<input
id="weight"
type="number"
placeholder="Weight (kg)"
>

<input
id="height"
type="number"
placeholder="Height (cm)"
>

<button onclick="run()">
Calculate BMI
</button>

<div id="output" class="output"></div>

<script>
function run() {

    const weight =
        Number(
            document.getElementById("weight").value
        );

    const height =
        Number(
            document.getElementById("height").value
        ) / 100;

    if (
        !weight ||
        !height
    ) {

        document.getElementById("output")
            .textContent =
            "Enter valid values.";

        return;
    }

    const bmi =
        weight / (height * height);

    document.getElementById("output")
        .textContent =
        "BMI: " + bmi.toFixed(2);
}
</script>
"""


def engine_age():

    return """
<input
id="date"
type="date"
>

<button onclick="run()">
Calculate Age
</button>

<div id="output" class="output"></div>

<script>
function run() {

    const birth =
        new Date(
            document.getElementById("date").value
        );

    if (isNaN(birth)) return;

    const now = new Date();

    let age =
        now.getFullYear() -
        birth.getFullYear();

    const month =
        now.getMonth() -
        birth.getMonth();

    if (
        month < 0 ||
        (
            month === 0 &&
            now.getDate() < birth.getDate()
        )
    ) {
        age--;
    }

    document.getElementById("output")
        .textContent =
        "Age: " + age + " years";
}
</script>
"""


def engine_slug():

    return """
<input
id="input"
placeholder="Enter title..."
>

<button onclick="run()">
Generate Slug
</button>

<div id="output" class="output"></div>

<script>
function run() {

    const value =
        document.getElementById("input").value;

    const slug =
        value
        .toLowerCase()
        .trim()
        .replace(/[^a-z0-9\\s-]/g, "")
        .replace(/\\s+/g, "-")
        .replace(/-+/g, "-");

    document.getElementById("output")
        .textContent = slug;
}
</script>
"""


def engine_hex_color():

    return """
<input
id="color"
type="text"
value="#38bdf8"
placeholder="#38bdf8"
>

<button onclick="run()">
Convert
</button>

<div
id="preview"
style="
height:100px;
border-radius:12px;
margin-top:15px;
background:#38bdf8;
"
></div>

<div id="output" class="output"></div>

<script>
function run() {

    let hex =
        document.getElementById("color")
        .value
        .trim();

    if (!hex.startsWith("#"))
        hex = "#" + hex;

    if (!/^#[0-9a-fA-F]{6}$/.test(hex)) {

        document.getElementById("output")
            .textContent =
            "Invalid HEX color.";

        return;
    }

    const r =
        parseInt(hex.slice(1,3),16);

    const g =
        parseInt(hex.slice(3,5),16);

    const b =
        parseInt(hex.slice(5,7),16);

    document.getElementById("preview")
        .style.background = hex;

    document.getElementById("output")
        .textContent =
        "HEX: " + hex +
        "\\nRGB: rgb(" +
        r + ", " +
        g + ", " +
        b + ")";
}
</script>
"""


def engine_unit():

    return """
<input
id="value"
type="number"
value="1"
>

<select id="from">
<option value="m">Meter</option>
<option value="km">Kilometer</option>
<option value="cm">Centimeter</option>
<option value="ft">Foot</option>
<option value="in">Inch</option>
</select>

<select id="to">
<option value="m">Meter</option>
<option value="km">Kilometer</option>
<option value="cm">Centimeter</option>
<option value="ft">Foot</option>
<option value="in">Inch</option>
</select>

<button onclick="run()">
Convert
</button>

<div id="output" class="output"></div>

<script>
const rates = {
    m: 1,
    km: 1000,
    cm: 0.01,
    ft: 0.3048,
    in: 0.0254
};

function run() {

    const value =
        Number(
            document.getElementById("value").value
        );

    const from =
        document.getElementById("from").value;

    const to =
        document.getElementById("to").value;

    const result =
        value *
        rates[from] /
        rates[to];

    document.getElementById("output")
        .textContent =
        result;
}
</script>
"""


def engine_uuid():

    return """
<button onclick="run()">
Generate UUID
</button>

<div id="output" class="output"></div>

<script>
function run() {

    const uuid =
        crypto.randomUUID();

    document.getElementById("output")
        .textContent = uuid;
}
</script>
"""


ENGINE_MAP = {

    "json_formatter": engine_json_formatter,
    "json_validator": engine_json_validator,
    "json_minifier": engine_json_minifier,

    "base64_encode": engine_base64_encode,
    "base64_decode": engine_base64_decode,

    "url_encode": engine_url_encode,
    "url_decode": engine_url_decode,

    "password_generator": engine_password_generator,

    "word_counter": engine_word_counter,
    "character_counter": engine_character_counter,
    "text_reverser": engine_text_reverser,
    "duplicate_lines": engine_duplicate_lines,

    "percentage": engine_percentage,
    "average": engine_average,
    "bmi": engine_bmi,
    "age": engine_age,

    "slug": engine_slug,
    "hex_color": engine_hex_color,
    "unit": engine_unit,
    "uuid": engine_uuid,
}


# ============================================================
# TOOL PAGE
# ============================================================

def build_tool_page(tool):

    name = tool["name"]
    category = tool["category"]
    description = tool["description"]
    engine_name = tool["engine"]

    engine = ENGINE_MAP.get(engine_name)

    if engine is None:
        raise ValueError(
            f"No real engine registered for: {name}"
        )

    tool_ui = engine()

    slug = slugify(name)

    canonical =
        f"{SITE_URL}/tools/{slug}.html"

    body = f"""
<section class="tool-page">

<div class="container">

<span class="badge">
{esc(category)}
</span>

<h1>{esc(name)}</h1>

<p class="muted">
{esc(description)}
</p>

<div class="tool-box">

{tool_ui}

</div>

{ad_block()}

<section class="card">

<h2>About {esc(name)}</h2>

<p>
{esc(description)}
This tool runs directly in your browser whenever
possible, so your input does not need to be uploaded
to our server.
</p>

</section>

<a href="{SITE_URL}/">
← Back to Free Tools Hub
</a>

</div>

</section>
"""

    return page_shell(
        title=f"{name} — Free Online Tool",
        description=description,
        body=body,
        canonical=canonical
    )


# ============================================================
# GENERATE TOOLS
# ============================================================

def generate_tools(db):

    existing = {
        tool["name"]
        for tool in db["tools"]
    }

    generated = 0

    for tool in TOOLS:

        if tool["name"] in existing:
            continue

        slug = slugify(tool["name"])

        path =
            TOOLS_DIR / f"{slug}.html"

        write_file(
            path,
            build_tool_page(tool)
        )

        db["tools"].append({
            **tool,
            "slug": slug,
            "url":
                f"{SITE_URL}/tools/{slug}.html"
        })

        generated += 1

    return generated


# ============================================================
# HOME PAGE
# ============================================================

def build_home(db):

    cards = ""

    for tool in db["tools"]:

        cards += f"""
<a
class="card"
href="{SITE_URL}/tools/{esc(tool['slug'])}.html"
>

<span class="badge">
{esc(tool["category"])}
</span>

<h3>
{esc(tool["name"])}
</h3>

<p class="muted">
{esc(tool["description"])}
</p>

</a>
"""

    categories = sorted(
        set(
            tool["category"]
            for tool in db["tools"]
        )
    )

    category_html = ""

    for category in categories:

        category_html += f"""
<a class="card"
href="#category-{slugify(category)}">

<h3>{esc(category)}</h3>

</a>
"""

    body = f"""
<section class="hero">

<div class="container">

<h1>
Free Online Tools
</h1>

<p>
Fast, useful browser-based tools for developers,
designers, marketers, students and businesses.
</p>

<div class="search">

<input
id="search"
placeholder="Search tools..."
oninput="searchTools()"
>

</div>

</div>

</section>

<section
class="container"
id="categories"
>

<h2>Categories</h2>

<div class="grid">

{category_html}

</div>

</section>

<section
class="container"
id="tools"
style="margin-top:50px"
>

<h2>All Tools</h2>

<div
id="tool-grid"
class="grid"
>

{cards}

</div>

</section>

{ad_block()}

<script>

function searchTools() {

    const query =
        document
        .getElementById("search")
        .value
        .toLowerCase();

    document
        .querySelectorAll("#tool-grid .card")
        .forEach(card => {

            const text =
                card.textContent
                .toLowerCase();

            card.style.display =
                text.includes(query)
                ? ""
                : "none";
        });
}

</script>
"""

    return page_shell(
        title="Free Tools Hub — Free Online Tools",
        description=
            "Free online tools for developers, designers, SEO, productivity and everyday tasks.",
        body=body,
        canonical=f"{SITE_URL}/"
    )


# ============================================================
# SITEMAP
# ============================================================

def build_sitemap(db):

    urls = [
        SITE_URL + "/"
    ]

    for tool in db["tools"]:

        urls.append(
            f"{SITE_URL}/tools/{tool['slug']}.html"
        )

    xml = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    ]

    for url in urls:

        xml.append(
            "<url>"
            f"<loc>{esc(url)}</loc>"
            "</url>"
        )

    xml.append("</urlset>")

    return "\n".join(xml)


# ============================================================
# ROBOTS
# ============================================================

def build_robots():

    return f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 60)

    print(
        "FREE TOOLS HUB — EMPIRE ENGINE V5"
    )

    print("=" * 60)

    create_directories()

    db = load_database()

    print(
        f"Existing tools: {len(db['tools'])}"
    )

    generated =
        generate_tools(db)

    print(
        f"New real tools generated: {generated}"
    )

    write_file(
        OUTPUT_DIR / "index.html",
        build_home(db)
    )

    write_file(
        OUTPUT_DIR / "sitemap.xml",
        build_sitemap(db)
    )

    write_file(
        OUTPUT_DIR / "robots.txt",
        build_robots()
    )

    save_database(db)

    print()
    print(
        f"Total registered tools: {len(db['tools'])}"
    )

    print(
        "Website generation completed."
    )

    if len(db["tools"]) < TARGET_TOOLS:

        print()
        print(
            "NOTE:"
        )

        print(
            f"The registry currently contains "
            f"{len(db['tools'])} real engines."
        )

        print(
            "Do NOT generate fake pages just to reach "
            f"{TARGET_TOOLS}."
        )

        print(
            "Add real engines to ENGINE_MAP and TOOLS "
            "to expand the platform."
        )

    print("=" * 60)


if __name__ == "__main__":
    main()
