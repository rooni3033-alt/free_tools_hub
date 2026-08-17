#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Empire Web Engine — Global Tools Hub
Version: 5.0

Purpose:
- Generate a global static tools website
- Generate real browser-based tools
- Generate SEO-friendly pages
- Generate sitemap.xml
- Generate robots.txt
- Generate manifest.json
- Generate tool index
- Generate article index
- Add advertisement placement naturally
- Designed for GitHub Pages + GitHub Actions

IMPORTANT:
This engine only claims a tool is functional when its implementation
is actually included in this file.
"""

from pathlib import Path
from datetime import datetime, timezone
import html
import json
import re
import hashlib
import random


# ============================================================
# CONFIGURATION
# ============================================================

SITE_URL = "https://rooni3033-alt.github.io/free_tools_hub"

SITE_NAME = "Free Tools Hub"

SITE_DESCRIPTION = (
    "Free online tools for developers, designers, SEO professionals, "
    "students, businesses and everyday users."
)

LANGUAGE = "en"

# Advertisement destination
AD_LINK = "https://omg10.com/4/11349784"

# Maximum number of tool pages that the engine is allowed to build.
# The system can be expanded later without changing the architecture.
MAX_TOOLS = 1000

# Number of new articles generated per build.
ARTICLES_PER_BUILD = 3

# Directories
ROOT = Path(".")
TOOLS_DIR = ROOT / "tools"
ARTICLES_DIR = ROOT / "articles"
ASSETS_DIR = ROOT / "assets"

DB_FILE = ROOT / "database.json"

SITEMAP_FILE = ROOT / "sitemap.xml"
ROBOTS_FILE = ROOT / "robots.txt"
MANIFEST_FILE = ROOT / "manifest.json"


# ============================================================
# TOOL REGISTRY
# ============================================================

"""
Every real tool is registered here.

A tool has:
    id
    name
    slug
    category
    description
    keywords
    builder

The builder must generate actual working HTML/JavaScript.
"""

TOOLS = [

    {
        "id": "json-formatter",
        "name": "JSON Formatter",
        "slug": "json-formatter",
        "category": "Developer",
        "description": (
            "Format, validate and minify JSON directly in your browser."
        ),
        "keywords": [
            "json formatter",
            "json beautifier",
            "json validator",
            "json minifier"
        ],
        "builder": "json_formatter",
    },

    {
        "id": "base64-encoder-decoder",
        "name": "Base64 Encoder & Decoder",
        "slug": "base64-encoder-decoder",
        "category": "Developer",
        "description": (
            "Encode text to Base64 or decode Base64 text instantly."
        ),
        "keywords": [
            "base64 encoder",
            "base64 decoder",
            "base64 converter"
        ],
        "builder": "base64",
    },

    {
        "id": "password-generator",
        "name": "Password Generator",
        "slug": "password-generator",
        "category": "Security",
        "description": (
            "Generate strong random passwords locally in your browser."
        ),
        "keywords": [
            "password generator",
            "strong password",
            "secure password"
        ],
        "builder": "password_generator",
    },

    {
        "id": "word-counter",
        "name": "Word Counter",
        "slug": "word-counter",
        "category": "Writing",
        "description": (
            "Count words, characters, sentences and paragraphs online."
        ),
        "keywords": [
            "word counter",
            "character counter",
            "word count"
        ],
        "builder": "word_counter",
    },

    {
        "id": "color-converter",
        "name": "Color Converter",
        "slug": "color-converter",
        "category": "Design",
        "description": (
            "Convert HEX colors to RGB and RGB colors to HEX."
        ),
        "keywords": [
            "color converter",
            "hex to rgb",
            "rgb to hex"
        ],
        "builder": "color_converter",
    },

    {
        "id": "unit-converter",
        "name": "Unit Converter",
        "slug": "unit-converter",
        "category": "Converter",
        "description": (
            "Convert common length units quickly and accurately."
        ),
        "keywords": [
            "unit converter",
            "length converter",
            "meters to feet"
        ],
        "builder": "unit_converter",
    },

    {
        "id": "percentage-calculator",
        "name": "Percentage Calculator",
        "slug": "percentage-calculator",
        "category": "Calculator",
        "description": (
            "Calculate percentages, percentage increases and decreases."
        ),
        "keywords": [
            "percentage calculator",
            "percent calculator",
            "percentage increase"
        ],
        "builder": "percentage_calculator",
    },

    {
        "id": "slug-generator",
        "name": "URL Slug Generator",
        "slug": "url-slug-generator",
        "category": "SEO",
        "description": (
            "Create clean SEO-friendly URL slugs from text."
        ),
        "keywords": [
            "slug generator",
            "url slug",
            "seo slug generator"
        ],
        "builder": "slug_generator",
    },

    {
        "id": "text-case-converter",
        "name": "Text Case Converter",
        "slug": "text-case-converter",
        "category": "Writing",
        "description": (
            "Convert text between uppercase, lowercase and title case."
        ),
        "keywords": [
            "case converter",
            "uppercase converter",
            "lowercase converter"
        ],
        "builder": "case_converter",
    },

    {
        "id": "random-number-generator",
        "name": "Random Number Generator",
        "slug": "random-number-generator",
        "category": "Utility",
        "description": (
            "Generate random numbers between any minimum and maximum."
        ),
        "keywords": [
            "random number generator",
            "random number",
            "number generator"
        ],
        "builder": "random_number",
    },

    {
        "id": "uuid-generator",
        "name": "UUID Generator",
        "slug": "uuid-generator",
        "category": "Developer",
        "description": (
            "Generate UUID v4 identifiers instantly in your browser."
        ),
        "keywords": [
            "uuid generator",
            "uuid v4",
            "guid generator"
        ],
        "builder": "uuid_generator",
    },

    {
        "id": "timestamp-converter",
        "name": "Unix Timestamp Converter",
        "slug": "unix-timestamp-converter",
        "category": "Developer",
        "description": (
            "Convert Unix timestamps to readable dates and vice versa."
        ),
        "keywords": [
            "unix timestamp",
            "timestamp converter",
            "epoch converter"
        ],
        "builder": "timestamp_converter",
    },

    {
        "id": "text-reverser",
        "name": "Text Reverser",
        "slug": "text-reverser",
        "category": "Text",
        "description": (
            "Reverse text instantly while preserving your original input."
        ),
        "keywords": [
            "text reverser",
            "reverse text",
            "reverse string"
        ],
        "builder": "text_reverser",
    },

    {
        "id": "duplicate-line-remover",
        "name": "Duplicate Line Remover",
        "slug": "duplicate-line-remover",
        "category": "Text",
        "description": (
            "Remove duplicate lines from text while keeping unique entries."
        ),
        "keywords": [
            "remove duplicate lines",
            "duplicate remover",
            "unique lines"
        ],
        "builder": "duplicate_lines",
    },

    {
        "id": "html-entities-converter",
        "name": "HTML Entities Converter",
        "slug": "html-entities-converter",
        "category": "Developer",
        "description": (
            "Encode and decode HTML entities directly in your browser."
        ),
        "keywords": [
            "html entities",
            "html encoder",
            "html decoder"
        ],
        "builder": "html_entities",
    },

]


# ============================================================
# CATEGORY DEFINITIONS
# ============================================================

CATEGORIES = {
    "Developer": "Developer Tools",
    "Security": "Security Tools",
    "Writing": "Writing Tools",
    "Design": "Design Tools",
    "Converter": "Converters",
    "Calculator": "Calculators",
    "SEO": "SEO Tools",
    "Utility": "Utilities",
    "Text": "Text Tools",
}


# ============================================================
# ARTICLE TOPICS
# ============================================================

ARTICLE_TOPICS = [
    "Free Developer Tools",
    "SEO Tools for Beginners",
    "Useful Online Calculators",
    "Free Writing Tools",
    "Web Design Tools",
    "Cybersecurity Tools",
    "Productivity Tools",
    "Text Processing Tools",
    "Online Converters",
    "Tools for Small Businesses",
    "Tools for Students",
    "Tools for Freelancers",
    "Tools for Content Creators",
]


# ============================================================
# DATABASE
# ============================================================

def load_database():
    """
    Load database.json safely.
    """

    if not DB_FILE.exists():
        return {
            "tools": [],
            "articles": [],
            "generated_at": None,
            "version": "5.0",
        }

    try:
        with DB_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("Database must be an object")

        data.setdefault("tools", [])
        data.setdefault("articles", [])
        data.setdefault("generated_at", None)
        data.setdefault("version", "5.0")

        return data

    except Exception:
        return {
            "tools": [],
            "articles": [],
            "generated_at": None,
            "version": "5.0",
        }


def save_database(database):
    """
    Save database.json.
    """

    database["generated_at"] = datetime.now(
        timezone.utc
    ).isoformat()

    with DB_FILE.open("w", encoding="utf-8") as file:
        json.dump(
            database,
            file,
            ensure_ascii=False,
            indent=2
        )


# ============================================================
# FILESYSTEM
# ============================================================

def ensure_directories():
    """
    Create all required directories.
    """

    TOOLS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    ARTICLES_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    ASSETS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


# ============================================================
# SECURITY / HTML HELPERS
# ============================================================

def esc(value):
    """
    Safely escape text before inserting it into HTML.
    """

    return html.escape(
        str(value),
        quote=True
    )


def slugify(text):
    """
    Convert arbitrary text to an SEO-friendly slug.
    """

    text = str(text).strip().lower()

    text = re.sub(
        r"[^a-z0-9\s-]",
        "",
        text
    )

    text = re.sub(
        r"\s+",
        "-",
        text
    )

    text = re.sub(
        r"-+",
        "-",
        text
    )

    return text.strip("-")


def sha_id(text):
    """
    Generate a stable short identifier.
    """

    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()[:12]


# ============================================================
# ADVERTISEMENT COMPONENT
# ============================================================

def advertisement_html():
    """
    Natural advertisement placement.

    It is intentionally not disguised as website navigation.
    """

    return f"""
<section class="ad-box" aria-label="Advertisement">
    <span class="ad-label">ADVERTISEMENT</span>

    <p>
        Explore more useful digital tools and online resources.
    </p>

    <a
        href="{esc(AD_LINK)}"
        target="_blank"
        rel="nofollow sponsored noopener"
    >
        Discover more tools →
    </a>
</section>
"""


# ============================================================
# GLOBAL CSS
# ============================================================

def global_css():
    return """
:root {
    --bg: #07111f;
    --surface: #101c2d;
    --surface2: #16243a;
    --text: #edf5ff;
    --muted: #91a4bb;
    --primary: #38bdf8;
    --border: #263a54;
    --danger: #ef4444;
    --success: #22c55e;
}

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    padding: 0;
    background: var(--bg);
    color: var(--text);
    font-family:
        Inter,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
    line-height: 1.7;
}

a {
    color: var(--primary);
}

.container {
    width: min(1100px, calc(100% - 32px));
    margin: auto;
}

header {
    padding: 24px 0;
    border-bottom: 1px solid var(--border);
}

.logo {
    font-size: 1.35rem;
    font-weight: 800;
    text-decoration: none;
    color: var(--text);
}

main {
    padding: 45px 0;
}

h1 {
    font-size: clamp(2rem, 5vw, 3rem);
    line-height: 1.15;
    margin: 0 0 12px;
}

h2 {
    line-height: 1.25;
}

.subtitle {
    color: var(--muted);
    max-width: 750px;
}

.card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 24px;
    margin: 20px 0;
}

.tool-grid {
    display: grid;
    grid-template-columns:
        repeat(auto-fit, minmax(240px, 1fr));
    gap: 16px;
    margin-top: 30px;
}

.tool-card {
    display: block;
    text-decoration: none;
    color: var(--text);
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 20px;
    transition: transform .15s ease,
                border-color .15s ease;
}

.tool-card:hover {
    transform: translateY(-3px);
    border-color: var(--primary);
}

.tool-card h2 {
    font-size: 1.05rem;
    margin: 0 0 8px;
}

.tool-card p {
    color: var(--muted);
    font-size: .92rem;
    margin: 0;
}

.badge {
    display: inline-block;
    padding: 4px 9px;
    border-radius: 999px;
    background: rgba(56,189,248,.1);
    color: var(--primary);
    font-size: .75rem;
    font-weight: 700;
    margin-bottom: 12px;
}

textarea,
input,
select {
    width: 100%;
    padding: 13px 14px;
    margin: 6px 0 12px;
    border-radius: 10px;
    border: 1px solid var(--border);
    background: #091525;
    color: var(--text);
    font: inherit;
}

textarea {
    min-height: 180px;
    resize: vertical;
}

button,
.btn {
    border: 0;
    border-radius: 10px;
    padding: 11px 18px;
    background: var(--primary);
    color: #03111d;
    font-weight: 800;
    cursor: pointer;
}

button:hover,
.btn:hover {
    filter: brightness(1.08);
}

.output {
    white-space: pre-wrap;
    word-break: break-word;
    background: #091525;
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 16px;
    min-height: 70px;
    margin-top: 15px;
}

.ad-box {
    position: relative;
    margin: 35px 0;
    padding: 24px;
    text-align: center;
    border: 1px solid var(--border);
    border-radius: 16px;
    background: var(--surface2);
}

.ad-label {
    display: block;
    color: var(--muted);
    font-size: .68rem;
    letter-spacing: .08em;
    margin-bottom: 8px;
}

.ad-box a {
    font-weight: 800;
    text-decoration: none;
}

footer {
    margin-top: 60px;
    padding: 30px 0;
    border-top: 1px solid var(--border);
    color: var(--muted);
    font-size: .9rem;
}

@media (max-width: 600px) {
    .container {
        width: min(100% - 22px, 1100px);
    }

    main {
        padding: 30px 0;
    }

    .card {
        padding: 18px;
    }
}
"""


# ============================================================
# BASE HTML DOCUMENT
# ============================================================

def page_html(
    title,
    description,
    content,
    canonical=None
):
    """
    Create a complete HTML document.
    """

    canonical = canonical or SITE_URL

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport"
      content="width=device-width, initial-scale=1">

<title>{esc(title)}</title>

<meta
    name="description"
    content="{esc(description)}"
>

<meta
    name="robots"
    content="index,follow,max-image-preview:large"
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
{global_css()}
</style>
</head>

<body>

<header>
<div class="container">
<a class="logo" href="{SITE_URL}/">
    {esc(SITE_NAME)}
</a>
</div>
</header>

<main>
<div class="container">

{content}

{advertisement_html()}

</div>
</main>

<footer>
<div class="container">
    <div>{esc(SITE_NAME)}</div>
    <div>
        Free browser-based tools.
        No account required for basic tools.
    </div>
</div>
</footer>

</body>
</html>
"""


# ============================================================
# TOOL UI HELPERS
# ============================================================

def tool_header(tool):
    """
    Standard heading for every tool.
    """

    return f"""
<div class="badge">
    {esc(tool["category"])}
</div>

<h1>{esc(tool["name"])}</h1>

<p class="subtitle">
    {esc(tool["description"])}
</p>

<div class="card">
"""


def tool_footer():
    return """
</div>

<p>
    <a href="../index.html">
        ← Back to Free Tools Hub
    </a>
</p>
"""


# ============================================================
# REAL TOOL IMPLEMENTATIONS — SECTION 1
# ============================================================

def build_json_formatter():
    return """
<textarea
    id="jsonInput"
    placeholder='Paste JSON here...'
></textarea>

<button onclick="formatJSON()">
    Format JSON
</button>

<button onclick="minifyJSON()">
    Minify
</button>

<button onclick="validateJSON()">
    Validate
</button>

<div id="jsonOutput" class="output">
    Result will appear here.
</div>

<script>
function getJSONInput() {
    return document.getElementById("jsonInput").value;
}

function showJSON(message, success = true) {
    const el = document.getElementById("jsonOutput");

    el.textContent = message;

    el.style.color =
        success
            ? "var(--success)"
            : "var(--danger)";
}

function formatJSON() {
    try {
        const value =
            JSON.parse(getJSONInput());

        document.getElementById(
            "jsonOutput"
        ).textContent =
            JSON.stringify(value, null, 2);

    } catch (error) {
        showJSON(
            "Invalid JSON: " +
            error.message,
            false
        );
    }
}

function minifyJSON() {
    try {
        const value =
            JSON.parse(getJSONInput());

        document.getElementById(
            "jsonOutput"
        ).textContent =
            JSON.stringify(value);

    } catch (error) {
        showJSON(
            "Invalid JSON: " +
            error.message,
            false
        );
    }
}

function validateJSON() {
    try {
        JSON.parse(getJSONInput());

        showJSON(
            "Valid JSON ✓"
        );

    } catch (error) {
        showJSON(
            "Invalid JSON: " +
            error.message,
            false
        );
    }
}
</script>
"""


def build_base64():
    return """
<textarea
    id="base64Input"
    placeholder="Enter text or Base64..."
></textarea>

<button onclick="encodeBase64()">
    Encode
</button>

<button onclick="decodeBase64()">
    Decode
</button>

<button onclick="copyBase64()">
    Copy Result
</button>

<div id="base64Output" class="output">
    Result will appear here.
</div>

<script>
function encodeBase64() {
    const input =
        document.getElementById(
            "base64Input"
        ).value;

    try {
        const bytes =
            new TextEncoder().encode(input);

        let binary = "";

        bytes.forEach(
            byte => binary +=
                String.fromCharCode(byte)
        );

        document.getElementById(
            "base64Output"
        ).textContent =
            btoa(binary);

    } catch (error) {
        document.getElementById(
            "base64Output"
        ).textContent =
            "Encoding error.";
    }
}

function decodeBase64() {
    const input =
        document.getElementById(
            "base64Input"
        ).value.trim();

    try {
        const binary = atob(input);

        const bytes =
            Uint8Array.from(
                binary,
                char => char.charCodeAt(0)
            );

        document.getElementById(
            "base64Output"
        ).textContent =
            new TextDecoder().decode(bytes);

    } catch (error) {
        document.getElementById(
            "base64Output"
        ).textContent =
            "Invalid Base64.";
    }
}

function copyBase64() {
    const value =
        document.getElementById(
            "base64Output"
        ).textContent;

    navigator.clipboard.writeText(value);
}
</script>
"""


def build_password_generator():
    return """
<div class="card">

<label>
    Password length
</label>

<input
    id="passwordLength"
    type="number"
    value="20"
    min="4"
    max="128"
>

<label>
    <input
        id="uppercase"
        type="checkbox"
        checked
    >
    Uppercase
</label>

<label>
    <input
        id="lowercase"
        type="checkbox"
        checked
    >
    Lowercase
</label>

<label>
    <input
        id="numbers"
        type="checkbox"
        checked
    >
    Numbers
</label>

<label>
    <input
        id="symbols"
        type="checkbox"
        checked
    >
    Symbols
</label>

<br><br>

<button onclick="generatePassword()">
    Generate Password
</button>

<div
    id="passwordOutput"
    class="output"
>
    Your password will appear here.
</div>

</div>

<script>
function generatePassword() {

    const length =
        Number(
            document.getElementById(
                "passwordLength"
            ).value
        );

    let chars = "";

    if (
        document.getElementById(
            "uppercase"
        ).checked
    ) {
        chars +=
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    }

    if (
        document.getElementById(
            "lowercase"
        ).checked
    ) {
        chars +=
            "abcdefghijklmnopqrstuvwxyz";
    }

    if (
        document.getElementById(
            "numbers"
        ).checked
    ) {
        chars +=
            "0123456789";
    }

    if (
        document.getElementById(
            "symbols"
        ).checked
    ) {
        chars +=
            "!@#$%^&*()-_=+[]{}";
    }

    if (!chars) {
        document.getElementById(
            "passwordOutput"
        ).textContent =
            "Select at least one character set.";

        return;
    }

    const values =
        new Uint32Array(length);

    crypto.getRandomValues(values);

    let password = "";

    for (let i = 0; i < length; i++) {
        password +=
            chars[
                values[i] % chars.length
            ];
    }

    document.getElementById(
        "passwordOutput"
    ).textContent =
        password;
}
</script>
"""


def build_word_counter():
    return """
<textarea
    id="counterInput"
    placeholder="Paste or type your text..."
></textarea>

<div class="tool-grid">

<div class="card">
    <strong id="words">0</strong>
    <br>
    Words
</div>

<div class="card">
    <strong id="characters">0</strong>
    <br>
    Characters
</div>

<div class="card">
    <strong id="sentences">0</strong>
    <br>
    Sentences
</div>

<div class="card">
    <strong id="paragraphs">0</strong>
    <br>
    Paragraphs
</div>

</div>

<script>
const counterInput =
    document.getElementById(
        "counterInput"
    );

counterInput.addEventListener(
    "input",
    updateCounter
);

function updateCounter() {

    const text =
        counterInput.value;

    const trimmed =
        text.trim();

    const words =
        trimmed
            ? trimmed.split(/\\s+/).length
            : 0;

    const sentences =
        trimmed
            ? trimmed
                .split(/[.!?]+/)
                .filter(Boolean)
                .length
            : 0;

    const paragraphs =
        trimmed
            ? trimmed
                .split(/\\n+/)
                .filter(Boolean)
                .length
            : 0;

    document.getElementById(
        "words"
    ).textContent = words;

    document.getElementById(
        "characters"
    ).textContent = text.length;

    document.getElementById(
        "sentences"
    ).textContent = sentences;

    document.getElementById(
        "paragraphs"
    ).textContent = paragraphs;
}
</script>
"""
# ============================================================
# REAL TOOL IMPLEMENTATIONS — SECTION 2
# ============================================================

def build_color_converter():
    return """
<div class="tool-grid">

<div>
    <label>HEX Color</label>

    <input
        id="hexColor"
        value="#38bdf8"
        placeholder="#38bdf8"
    >
</div>

<div>
    <label>RGB Color</label>

    <input
        id="rgbColor"
        placeholder="rgb(56, 189, 248)"
    >
</div>

</div>

<button onclick="hexToRGB()">
    HEX → RGB
</button>

<button onclick="rgbToHEX()">
    RGB → HEX
</button>

<div
    id="colorPreview"
    style="
        height:120px;
        margin-top:20px;
        border-radius:14px;
        background:#38bdf8;
        border:1px solid var(--border);
    "
></div>

<div
    id="colorOutput"
    class="output"
>
    Color result will appear here.
</div>

<script>

function hexToRGB() {

    let hex =
        document.getElementById(
            "hexColor"
        ).value.trim();

    if (!hex.startsWith("#")) {
        hex = "#" + hex;
    }

    if (
        !/^#[0-9a-fA-F]{6}$/.test(hex)
    ) {

        document.getElementById(
            "colorOutput"
        ).textContent =
            "Invalid HEX color.";

        return;
    }

    const r =
        parseInt(hex.substring(1, 3), 16);

    const g =
        parseInt(hex.substring(3, 5), 16);

    const b =
        parseInt(hex.substring(5, 7), 16);

    const rgb =
        `rgb(${r}, ${g}, ${b})`;

    document.getElementById(
        "rgbColor"
    ).value = rgb;

    document.getElementById(
        "colorPreview"
    ).style.background = hex;

    document.getElementById(
        "colorOutput"
    ).textContent =
        "HEX: " + hex +
        "\\nRGB: " + rgb;
}


function rgbToHEX() {

    const value =
        document.getElementById(
            "rgbColor"
        ).value.trim();

    const match =
        value.match(
            /rgb\\s*\\(\\s*(\\d+)\\s*,\\s*(\\d+)\\s*,\\s*(\\d+)\\s*\\)/i
        );

    if (!match) {

        document.getElementById(
            "colorOutput"
        ).textContent =
            "Invalid RGB format.";

        return;
    }

    const r =
        Number(match[1]);

    const g =
        Number(match[2]);

    const b =
        Number(match[3]);

    if (
        r > 255 ||
        g > 255 ||
        b > 255
    ) {

        document.getElementById(
            "colorOutput"
        ).textContent =
            "RGB values must be between 0 and 255.";

        return;
    }

    const hex =
        "#" +
        [r, g, b]
            .map(
                value =>
                    value
                        .toString(16)
                        .padStart(2, "0")
                )
            .join("");

    document.getElementById(
        "hexColor"
    ).value = hex;

    document.getElementById(
        "colorPreview"
    ).style.background = hex;

    document.getElementById(
        "colorOutput"
    ).textContent =
        "RGB: rgb(" +
        r + ", " +
        g + ", " +
        b +
        ")\\nHEX: " +
        hex;
}

hexToRGB();

</script>
"""


def build_unit_converter():
    return """
<div class="tool-grid">

<div>

<label>
    Value
</label>

<input
    id="unitValue"
    type="number"
    value="1"
    step="any"
>

<label>
    From
</label>

<select id="unitFrom">

    <option value="meter">
        Meter
    </option>

    <option value="kilometer">
        Kilometer
    </option>

    <option value="centimeter">
        Centimeter
    </option>

    <option value="millimeter">
        Millimeter
    </option>

    <option value="mile">
        Mile
    </option>

    <option value="yard">
        Yard
    </option>

    <option value="foot">
        Foot
    </option>

    <option value="inch">
        Inch
    </option>

</select>

</div>


<div>

<label>
    To
</label>

<select id="unitTo">

    <option value="meter">
        Meter
    </option>

    <option value="kilometer">
        Kilometer
    </option>

    <option value="centimeter">
        Centimeter
    </option>

    <option value="millimeter">
        Millimeter
    </option>

    <option value="mile">
        Mile
    </option>

    <option value="yard">
        Yard
    </option>

    <option value="foot">
        Foot
    </option>

    <option value="inch">
        Inch
    </option>

</select>

</div>

</div>

<button onclick="convertUnits()">
    Convert
</button>

<div
    id="unitOutput"
    class="output"
>
    Result will appear here.
</div>

<script>

const unitMeters = {

    meter: 1,

    kilometer: 1000,

    centimeter: 0.01,

    millimeter: 0.001,

    mile: 1609.344,

    yard: 0.9144,

    foot: 0.3048,

    inch: 0.0254

};


function convertUnits() {

    const value =
        Number(
            document.getElementById(
                "unitValue"
            ).value
        );

    const from =
        document.getElementById(
            "unitFrom"
        ).value;

    const to =
        document.getElementById(
            "unitTo"
        ).value;

    if (!Number.isFinite(value)) {

        document.getElementById(
            "unitOutput"
        ).textContent =
            "Please enter a valid number.";

        return;
    }

    const meters =
        value * unitMeters[from];

    const result =
        meters / unitMeters[to];

    document.getElementById(
        "unitOutput"
    ).textContent =
        value +
        " " +
        from +
        " = " +
        result.toLocaleString(
            undefined,
            {
                maximumFractionDigits: 12
            }
        ) +
        " " +
        to;
}

</script>
"""


def build_percentage_calculator():
    return """
<div class="card">

<label>
    What is X% of Y?
</label>

<input
    id="percentX"
    type="number"
    value="10"
    step="any"
>

<input
    id="percentY"
    type="number"
    value="100"
    step="any"
>

<button onclick="calculatePercentage()">
    Calculate
</button>

<div
    id="percentageOutput"
    class="output"
>
    Result will appear here.
</div>

</div>


<div class="card">

<label>
    Percentage increase / decrease
</label>

<input
    id="oldValue"
    type="number"
    placeholder="Original value"
    step="any"
>

<input
    id="newValue"
    type="number"
    placeholder="New value"
    step="any"
>

<button onclick="calculateChange()">
    Calculate Change
</button>

<div
    id="changeOutput"
    class="output"
>
    Result will appear here.
</div>

</div>


<script>

function calculatePercentage() {

    const x =
        Number(
            document.getElementById(
                "percentX"
            ).value
        );

    const y =
        Number(
            document.getElementById(
                "percentY"
            ).value
        );

    if (
        !Number.isFinite(x) ||
        !Number.isFinite(y)
    ) {

        document.getElementById(
            "percentageOutput"
        ).textContent =
            "Enter valid numbers.";

        return;
    }

    const result =
        (x / 100) * y;

    document.getElementById(
        "percentageOutput"
    ).textContent =
        `${x}% of ${y} = ${result}`;
}


function calculateChange() {

    const oldValue =
        Number(
            document.getElementById(
                "oldValue"
            ).value
        );

    const newValue =
        Number(
            document.getElementById(
                "newValue"
            ).value
        );

    if (
        !Number.isFinite(oldValue) ||
        !Number.isFinite(newValue)
    ) {

        document.getElementById(
            "changeOutput"
        ).textContent =
            "Enter valid numbers.";

        return;
    }

    if (oldValue === 0) {

        document.getElementById(
            "changeOutput"
        ).textContent =
            "Original value cannot be zero.";

        return;
    }

    const difference =
        newValue - oldValue;

    const percentage =
        (difference / oldValue) * 100;

    const direction =
        percentage >= 0
            ? "increase"
            : "decrease";

    document.getElementById(
        "changeOutput"
    ).textContent =
        `${Math.abs(percentage).toFixed(2)}% ${direction}`;
}

</script>
"""


def build_slug_generator():
    return """
<textarea
    id="slugInput"
    placeholder="Enter your page title..."
></textarea>

<label>
    Separator
</label>

<select id="slugSeparator">

    <option value="-">
        Hyphen -
    </option>

    <option value="_">
        Underscore _
    </option>

</select>

<br><br>

<button onclick="generateSlug()">
    Generate Slug
</button>

<button onclick="copySlug()">
    Copy
</button>

<div
    id="slugOutput"
    class="output"
>
    Your SEO-friendly slug will appear here.
</div>

<script>

function generateSlug() {

    const input =
        document.getElementById(
            "slugInput"
        ).value.trim();

    const separator =
        document.getElementById(
            "slugSeparator"
        ).value;

    let slug =
        input.toLowerCase();

    /*
     * Keep Latin letters, numbers,
     * spaces and hyphens.
     */

    slug =
        slug.replace(
            /[^a-z0-9\\s-]/g,
            ""
        );

    slug =
        slug.replace(
            /[\\s_-]+/g,
            separator
        );

    slug =
        slug.replace(
            new RegExp(
                "^" +
                escapeRegExp(separator) +
                "|" +
                escapeRegExp(separator) +
                "$",
                "g"
            ),
            ""
        );

    document.getElementById(
        "slugOutput"
    ).textContent =
        slug;
}


function escapeRegExp(value) {

    return value.replace(
        /[.*+?^${}()|[\\]\\\\]/g,
        "\\\\$&"
    );
}


function copySlug() {

    const value =
        document.getElementById(
            "slugOutput"
        ).textContent;

    if (value) {
        navigator.clipboard.writeText(value);
    }
}

</script>
"""


def build_case_converter():
    return """
<textarea
    id="caseInput"
    placeholder="Enter your text..."
></textarea>

<div class="tool-grid">

<button onclick="toUpper()">
    UPPERCASE
</button>

<button onclick="toLower()">
    lowercase
</button>

<button onclick="toTitle()">
    Title Case
</button>

<button onclick="toSentence()">
    Sentence case
</button>

</div>

<div
    id="caseOutput"
    class="output"
>
    Converted text will appear here.
</div>

<script>

function getCaseText() {

    return document.getElementById(
        "caseInput"
    ).value;
}


function showCase(value) {

    document.getElementById(
        "caseOutput"
    ).textContent =
        value;
}


function toUpper() {

    showCase(
        getCaseText().toUpperCase()
    );
}


function toLower() {

    showCase(
        getCaseText().toLowerCase()
    );
}


function toTitle() {

    const text =
        getCaseText().toLowerCase();

    showCase(
        text.replace(
            /\\b\\w/g,
            char => char.toUpperCase()
        )
    );
}


function toSentence() {

    const text =
        getCaseText()
            .toLowerCase()
            .trim();

    if (!text) {
        showCase("");
        return;
    }

    const result =
        text.replace(
            /(^|[.!?]\\s+)([a-z])/g,
            function(
                match,
                separator,
                letter
            ) {

                return (
                    separator +
                    letter.toUpperCase()
                );
            }
        );

    showCase(result);
}

</script>
"""


def build_random_number():
    return """
<div class="tool-grid">

<div>

<label>
    Minimum
</label>

<input
    id="randomMin"
    type="number"
    value="1"
>

</div>

<div>

<label>
    Maximum
</label>

<input
    id="randomMax"
    type="number"
    value="100"
>

</div>

</div>

<button onclick="generateRandom()">
    Generate
</button>

<div
    id="randomOutput"
    class="output"
>
    Your random number will appear here.
</div>

<script>

function generateRandom() {

    const min =
        Math.ceil(
            Number(
                document.getElementById(
                    "randomMin"
                ).value
            )
        );

    const max =
        Math.floor(
            Number(
                document.getElementById(
                    "randomMax"
                ).value
            )
        );

    if (
        !Number.isFinite(min) ||
        !Number.isFinite(max) ||
        min > max
    ) {

        document.getElementById(
            "randomOutput"
        ).textContent =
            "Enter a valid range.";

        return;
    }

    const random =
        new Uint32Array(1);

    crypto.getRandomValues(random);

    const result =
        min +
        (random[0] %
            (max - min + 1));

    document.getElementById(
        "randomOutput"
    ).textContent =
        result;
}

</script>
"""


def build_uuid_generator():
    return """
<button onclick="generateUUID()">
    Generate UUID v4
</button>

<button onclick="copyUUID()">
    Copy
</button>

<div
    id="uuidOutput"
    class="output"
>
    UUID will appear here.
</div>

<script>

function generateUUID() {

    const uuid =
        crypto.randomUUID();

    document.getElementById(
        "uuidOutput"
    ).textContent =
        uuid;
}


function copyUUID() {

    const value =
        document.getElementById(
            "uuidOutput"
        ).textContent;

    if (
        value &&
        value !==
        "UUID will appear here."
    ) {
        navigator.clipboard.writeText(value);
    }
}

</script>
"""


def build_timestamp_converter():
    return """
<div class="card">

<label>
    Unix Timestamp
</label>

<input
    id="timestampInput"
    type="number"
    placeholder="Example: 1750000000"
>

<button onclick="timestampToDate()">
    Timestamp → Date
</button>

<div
    id="timestampOutput"
    class="output"
>
    Result will appear here.
</div>

</div>


<div class="card">

<button onclick="dateToTimestamp()">
    Current Date → Unix Timestamp
</button>

<div
    id="currentTimestamp"
    class="output"
>
    Result will appear here.
</div>

</div>


<script>

function timestampToDate() {

    const value =
        Number(
            document.getElementById(
                "timestampInput"
            ).value
        );

    if (!Number.isFinite(value)) {

        document.getElementById(
            "timestampOutput"
        ).textContent =
            "Enter a valid Unix timestamp.";

        return;
    }

    /*
     * Detect seconds vs milliseconds.
     */

    const milliseconds =
        Math.abs(value) < 100000000000
            ? value * 1000
            : value;

    const date =
        new Date(milliseconds);

    if (Number.isNaN(date.getTime())) {

        document.getElementById(
            "timestampOutput"
        ).textContent =
            "Invalid timestamp.";

        return;
    }

    document.getElementById(
        "timestampOutput"
    ).textContent =
        date.toISOString();
}


function dateToTimestamp() {

    const timestamp =
        Math.floor(
            Date.now() / 1000
        );

    document.getElementById(
        "currentTimestamp"
    ).textContent =
        timestamp;
}

</script>
"""


def build_text_reverser():
    return """
<textarea
    id="reverseInput"
    placeholder="Enter text..."
></textarea>

<button onclick="reverseText()">
    Reverse Text
</button>

<button onclick="copyReversed()">
    Copy
</button>

<div
    id="reverseOutput"
    class="output"
>
    Result will appear here.
</div>

<script>

function reverseText() {

    const text =
        document.getElementById(
            "reverseInput"
        ).value;

    /*
     * Array.from handles Unicode
     * code points better than split("").
     */

    const result =
        Array.from(text)
            .reverse()
            .join("");

    document.getElementById(
        "reverseOutput"
    ).textContent =
        result;
}


function copyReversed() {

    const value =
        document.getElementById(
            "reverseOutput"
        ).textContent;

    navigator.clipboard.writeText(value);
}

</script>
"""


def build_duplicate_lines():
    return """
<textarea
    id="duplicateInput"
    placeholder="Paste one item per line..."
></textarea>

<label>
    <input
        id="ignoreCase"
        type="checkbox"
    >
    Ignore letter case
</label>

<br><br>

<button onclick="removeDuplicates()">
    Remove Duplicates
</button>

<button onclick="copyUnique()">
    Copy Result
</button>

<div
    id="duplicateOutput"
    class="output"
>
    Result will appear here.
</div>

<script>

function removeDuplicates() {

    const text =
        document.getElementById(
            "duplicateInput"
        ).value;

    const ignoreCase =
        document.getElementById(
            "ignoreCase"
        ).checked;

    const lines =
        text.split(/\\r?\\n/);

    const seen =
        new Set();

    const result = [];

    for (const line of lines) {

        const key =
            ignoreCase
                ? line.toLowerCase()
                : line;

        if (!seen.has(key)) {

            seen.add(key);

            result.push(line);
        }
    }

    document.getElementById(
        "duplicateOutput"
    ).textContent =
        result.join("\\n");
}


function copyUnique() {

    const value =
        document.getElementById(
            "duplicateOutput"
        ).textContent;

    navigator.clipboard.writeText(value);
}

</script>
"""


def build_html_entities():
    return """
<textarea
    id="entityInput"
    placeholder="Enter HTML or text..."
></textarea>

<button onclick="encodeEntities()">
    Encode
</button>

<button onclick="decodeEntities()">
    Decode
</button>

<div
    id="entityOutput"
    class="output"
>
    Result will appear here.
</div>

<script>

function encodeEntities() {

    const value =
        document.getElementById(
            "entityInput"
        ).value;

    const div =
        document.createElement("div");

    div.textContent =
        value;

    document.getElementById(
        "entityOutput"
    ).textContent =
        div.innerHTML;
}


function decodeEntities() {

    const value =
        document.getElementById(
            "entityInput"
        ).value;

    const div =
        document.createElement("textarea");

    div.innerHTML =
        value;
the
    document.getElementById(
        "entityOutput"
    ).textContent =
        div.value;
}

</script>
"""
# ============================================================
# SECTION 3/4 — TOOL ENGINE
# Empire Web Global Tools Engine
# ============================================================

def html_page(title, description, category, tool_body, slug):
    """
    Creates a complete responsive HTML page for a tool.
    Tool processing is client-side whenever possible.
    """

    safe_title = html.escape(str(title))
    safe_description = html.escape(str(description))
    safe_category = html.escape(str(category))

    site_url = SITE_URL.rstrip("/")
    canonical_url = f"{site_url}/tools/{slug}.html"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{safe_title} | Free Online Tool</title>

<meta name="description" content="{safe_description}">
<meta name="robots" content="index,follow">

<link rel="canonical" href="{canonical_url}">

<meta property="og:type" content="website">
<meta property="og:title" content="{safe_title}">
<meta property="og:description" content="{safe_description}">
<meta property="og:url" content="{canonical_url}">

<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{safe_title}">
<meta name="twitter:description" content="{safe_description}">

<style>

:root {{
    --bg:#0b1120;
    --card:#111827;
    --card2:#172033;
    --primary:#38bdf8;
    --primary2:#0ea5e9;
    --text:#f8fafc;
    --muted:#94a3b8;
    --border:#263449;
    --success:#22c55e;
    --danger:#ef4444;
    --warning:#f59e0b;
}}

* {{
    box-sizing:border-box;
}}

html {{
    scroll-behavior:smooth;
}}

body {{
    margin:0;
    padding:0;
    background:var(--bg);
    color:var(--text);
    font-family:
        Inter,
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
    line-height:1.6;
}}

a {{
    color:var(--primary);
    text-decoration:none;
}}

a:hover {{
    text-decoration:underline;
}}

.container {{
    width:min(100% - 30px, 1100px);
    margin:auto;
}}

.header {{
    padding:25px 0 10px;
}}

.logo {{
    font-size:1.1rem;
    font-weight:800;
}}

.breadcrumb {{
    margin-top:15px;
    color:var(--muted);
    font-size:.9rem;
}}

.hero {{
    padding:25px 0;
}}

.badge {{
    display:inline-block;
    padding:5px 12px;
    border:1px solid rgba(56,189,248,.25);
    border-radius:999px;
    color:var(--primary);
    background:rgba(56,189,248,.08);
    font-size:.78rem;
    font-weight:700;
    text-transform:uppercase;
}}

h1 {{
    font-size:clamp(1.8rem,5vw,3rem);
    line-height:1.15;
    margin:15px 0 10px;
}}

h2 {{
    line-height:1.25;
}}

.subtitle {{
    color:var(--muted);
    max-width:800px;
}}

.tool-card {{
    background:var(--card);
    border:1px solid var(--border);
    border-radius:18px;
    padding:25px;
    margin:20px 0;
    box-shadow:0 10px 30px rgba(0,0,0,.15);
}}

input,
textarea,
select {{
    width:100%;
    padding:12px 14px;
    margin:7px 0 12px;
    border-radius:9px;
    border:1px solid var(--border);
    background:#0b1220;
    color:var(--text);
    font:inherit;
}}

textarea {{
    min-height:150px;
    resize:vertical;
}}

input:focus,
textarea:focus,
select:focus {{
    outline:none;
    border-color:var(--primary);
    box-shadow:0 0 0 3px rgba(56,189,248,.12);
}}

button {{
    border:0;
    border-radius:9px;
    padding:11px 18px;
    background:var(--primary);
    color:#06111c;
    font-weight:800;
    cursor:pointer;
    margin:4px;
}}

button:hover {{
    background:var(--primary2);
}}

button.secondary {{
    background:#1e293b;
    color:var(--text);
}}

button.danger {{
    background:var(--danger);
    color:white;
}}

.output {{
    background:#070d18;
    border:1px solid var(--border);
    border-radius:10px;
    padding:16px;
    margin-top:15px;
    min-height:70px;
    white-space:pre-wrap;
    overflow:auto;
    word-break:break-word;
}}

.grid {{
    display:grid;
    grid-template-columns:repeat(2,minmax(0,1fr));
    gap:15px;
}}

.stats {{
    display:grid;
    grid-template-columns:repeat(4,minmax(0,1fr));
    gap:12px;
    margin-top:15px;
}}

.stat {{
    background:var(--card2);
    border:1px solid var(--border);
    border-radius:12px;
    padding:15px;
    text-align:center;
}}

.stat strong {{
    display:block;
    font-size:1.5rem;
    color:var(--primary);
}}

.ad-box {{
    margin:30px 0;
    padding:18px;
    border:1px solid rgba(245,158,11,.2);
    background:rgba(245,158,11,.05);
    border-radius:14px;
    text-align:center;
}}

.ad-box small {{
    display:block;
    color:var(--muted);
    font-size:.7rem;
    margin-bottom:5px;
}}

.footer {{
    padding:35px 0;
    color:var(--muted);
    border-top:1px solid var(--border);
    margin-top:40px;
    font-size:.85rem;
}}

@media(max-width:700px) {{

    .grid {{
        grid-template-columns:1fr;
    }}

    .stats {{
        grid-template-columns:repeat(2,1fr);
    }}

    .tool-card {{
        padding:17px;
    }}
}}

</style>
</head>

<body>

<div class="container">

<header class="header">

    <div class="logo">
        <a href="{SITE_URL}">
            Empire Web Tools
        </a>
    </div>

    <div class="breadcrumb">
        <a href="{SITE_URL}">Home</a>
        →
        {safe_category}
        →
        {safe_title}
    </div>

</header>

<section class="hero">

    <span class="badge">
        {safe_category}
    </span>

    <h1>
        {safe_title}
    </h1>

    <p class="subtitle">
        {safe_description}
        Free to use directly in your browser.
        No registration required.
    </p>

</section>

<main>

<div class="tool-card">

{tool_body}

</div>

<div class="ad-box">

    <small>ADVERTISEMENT</small>

    <a href="{html.escape(str(AD_LINK), quote=True)}"
       target="_blank"
       rel="nofollow sponsored noopener">
       Discover useful tools and offers →
    </a>

</div>

<section class="tool-card">

<h2>About this tool</h2>

<p>
This free online tool is designed to help users complete
common digital tasks quickly and directly in their browser.
No account is required for basic usage.
</p>

<p>
Your input is processed locally whenever the tool supports
client-side processing.
</p>

</section>

</main>

<footer class="footer">

<p>
© {datetime.now().year} Empire Web Tools.
Free online utilities for developers, creators,
marketers and everyday users.
</p>

<p>
<a href="{SITE_URL}">
All Tools
</a>
</p>

</footer>

</div>

</body>
</html>
"""


# ============================================================
# JSON TOOL
# ============================================================

def tool_json_formatter():

    return """
<h2>JSON Formatter & Validator</h2>

<textarea id="jsonInput"
placeholder='Paste JSON here...
Example:
{"name":"John","age":20}'></textarea>

<button onclick="formatJSON()">Format</button>
<button class="secondary" onclick="minifyJSON()">Minify</button>
<button class="secondary" onclick="validateJSON()">Validate</button>
<button class="secondary" onclick="copyResult()">Copy</button>

<div id="jsonOutput" class="output">
Result will appear here...
</div>

<script>

function getJSON() {
    return JSON.parse(
        document.getElementById("jsonInput").value
    );
}

function formatJSON() {

    try {

        const obj = getJSON();

        document.getElementById("jsonOutput")
            .textContent =
            JSON.stringify(obj, null, 2);

    } catch (e) {

        document.getElementById("jsonOutput")
            .textContent =
            "Invalid JSON: " + e.message;
    }
}

function minifyJSON() {

    try {

        const obj = getJSON();

        document.getElementById("jsonOutput")
            .textContent =
            JSON.stringify(obj);

    } catch (e) {

        document.getElementById("jsonOutput")
            .textContent =
            "Invalid JSON: " + e.message;
    }
}

function validateJSON() {

    try {

        getJSON();

        document.getElementById("jsonOutput")
            .textContent =
            "✓ Valid JSON";

    } catch (e) {

        document.getElementById("jsonOutput")
            .textContent =
            "✗ Invalid JSON\\n" + e.message;
    }
}

async function copyResult() {

    const text =
        document.getElementById("jsonOutput")
            .textContent;

    try {

        await navigator.clipboard.writeText(text);

    } catch (e) {

        alert("Copy failed.");
    }
}

</script>
"""


# ============================================================
# BASE64 TOOL
# ============================================================

def tool_base64():

    return """
<h2>Base64 Encoder & Decoder</h2>

<textarea id="baseInput"
placeholder="Enter text or Base64..."></textarea>

<button onclick="encodeBase64()">Encode</button>

<button class="secondary"
onclick="decodeBase64()">Decode</button>

<button class="secondary"
onclick="copyBase64()">Copy</button>

<div id="baseOutput" class="output">
Result will appear here...
</div>

<script>

function encodeBase64() {

    const text =
        document.getElementById("baseInput").value;

    try {

        const bytes =
            new TextEncoder().encode(text);

        let binary = "";

        bytes.forEach(
            byte => binary += String.fromCharCode(byte)
        );

        document.getElementById("baseOutput")
            .textContent =
            btoa(binary);

    } catch (e) {

        document.getElementById("baseOutput")
            .textContent =
            "Encoding failed.";
    }
}

function decodeBase64() {

    const text =
        document.getElementById("baseInput")
            .value.trim();

    try {

        const binary = atob(text);

        const bytes =
            Uint8Array.from(
                binary,
                c => c.charCodeAt(0)
            );

        document.getElementById("baseOutput")
            .textContent =
            new TextDecoder().decode(bytes);

    } catch (e) {

        document.getElementById("baseOutput")
            .textContent =
            "Invalid Base64.";
    }
}

async function copyBase64() {

    const text =
        document.getElementById("baseOutput")
            .textContent;

    try {

        await navigator.clipboard.writeText(text);

    } catch (e) {

        alert("Copy failed.");
    }
}

</script>
"""


# ============================================================
# WORD COUNTER
# ============================================================

def tool_word_counter():

    return """
<h2>Word & Character Counter</h2>

<textarea id="counterText"
placeholder="Type or paste your text..."
oninput="updateCounter()"></textarea>

<div class="stats">

<div class="stat">
<strong id="words">0</strong>
Words
</div>

<div class="stat">
<strong id="characters">0</strong>
Characters
</div>

<div class="stat">
<strong id="charactersNoSpaces">0</strong>
No Spaces
</div>

<div class="stat">
<strong id="sentences">0</strong>
Sentences
</div>

</div>

<script>

function updateCounter() {

    const text =
        document.getElementById("counterText").value;

    const words =
        text.trim()
        ? text.trim().split(/\\s+/u).length
        : 0;

    const sentences =
        text.split(/[.!?]+/)
        .filter(x => x.trim()).length;

    document.getElementById("words")
        .textContent = words;

    document.getElementById("characters")
        .textContent = text.length;

    document.getElementById("charactersNoSpaces")
        .textContent =
        text.replace(/\\s/g, "").length;

    document.getElementById("sentences")
        .textContent = sentences;
}

</script>
"""


# ============================================================
# CASE CONVERTER
# ============================================================

def tool_case_converter():

    return """
<h2>Text Case Converter</h2>

<textarea id="caseInput"
placeholder="Enter text..."></textarea>

<button onclick="toUpper()">UPPERCASE</button>

<button class="secondary"
onclick="toLower()">lowercase</button>

<button class="secondary"
onclick="toTitle()">Title Case</button>

<button class="secondary"
onclick="toSentence()">Sentence case</button>

<div id="caseOutput" class="output"></div>

<script>

function output(text) {

    document.getElementById("caseOutput")
        .textContent = text;
}

function getText() {

    return document.getElementById("caseInput")
        .value;
}

function toUpper() {

    output(getText().toUpperCase());
}

function toLower() {

    output(getText().toLowerCase());
}

function toTitle() {

    output(
        getText()
        .toLowerCase()
        .replace(/\\b\\w/g,
            c => c.toUpperCase())
    );
}

function toSentence() {

    const text =
        getText().toLowerCase();

    output(
        text.replace(
            /(^\\s*|[.!?]\\s+)([a-z])/g,
            (m, p, c) =>
                p + c.toUpperCase()
        )
    );
}

</script>
"""


# ============================================================
# DUPLICATE REMOVER
# ============================================================

def tool_duplicate_remover():

    return """
<h2>Duplicate Line Remover</h2>

<textarea id="duplicateInput"
placeholder="Enter one item per line..."></textarea>

<button onclick="removeDuplicates()">
Remove Duplicates
</button>

<button class="secondary"
onclick="sortLines()">
Sort Lines
</button>

<div id="duplicateOutput" class="output"></div>

<script>

function lines() {

    return document
        .getElementById("duplicateInput")
        .value
        .split(/\\r?\\n/);
}

function show(arr) {

    document
        .getElementById("duplicateOutput")
        .textContent =
        arr.join("\\n");
}

function removeDuplicates() {

    const unique =
        [...new Set(lines())];

    show(unique);
}

function sortLines() {

    const sorted =
        lines()
        .filter(x => x.trim())
        .sort(
            (a, b) =>
                a.localeCompare(b)
        );

    show(sorted);
}

</script>
"""


# ============================================================
# SECURE PASSWORD GENERATOR
# ============================================================

def tool_password_generator():

    return """
<h2>Secure Password Generator</h2>

<div class="grid">

<div>

<label>Password Length</label>

<input
id="passwordLength"
type="number"
min="4"
max="128"
value="20">

</div>

<div>

<label>Character Set</label>

<select id="passwordType">

<option value="all">
Letters + Numbers + Symbols
</option>

<option value="letters">
Letters Only
</option>

<option value="numbers">
Numbers Only
</option>

<option value="lettersnumbers">
Letters + Numbers
</option>

</select>

</div>

</div>

<button onclick="generatePassword()">
Generate Password
</button>

<button class="secondary"
onclick="copyPassword()">
Copy
</button>

<div id="passwordOutput"
class="output">
Click Generate Password
</div>

<script>

function secureRandomIndex(max) {

    const array =
        new Uint32Array(1);

    const limit =
        Math.floor(
            4294967296 / max
        ) * max;

    let value;

    do {

        crypto.getRandomValues(array);
        value = array[0];

    } while (value >= limit);

    return value % max;
}

function generatePassword() {

    const length =
        Math.min(
            128,
            Math.max(
                4,
                parseInt(
                    document.getElementById(
                        "passwordLength"
                    ).value,
                    10
                ) || 20
            )
        );

    const type =
        document.getElementById(
            "passwordType"
        ).value;

    let chars = "";

    if (
        type === "all" ||
        type === "letters" ||
        type === "lettersnumbers"
    ) {

        chars +=
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ" +
            "abcdefghijklmnopqrstuvwxyz";
    }

    if (
        type === "all" ||
        type === "numbers" ||
        type === "lettersnumbers"
    ) {

        chars +=
            "0123456789";
    }

    if (type === "all") {

        chars +=
            "!@#$%^&*()-_=+[]{};:,.?";
    }

    let result = "";

    for (let i = 0; i < length; i++) {

        result +=
            chars[
                secureRandomIndex(chars.length)
            ];
    }

    document.getElementById(
        "passwordOutput"
    ).textContent = result;
}

async function copyPassword() {

    const text =
        document.getElementById(
            "passwordOutput"
        ).textContent;

    try {

        await navigator.clipboard.writeText(text);

    } catch (e) {

        alert("Copy failed.");
    }
}

</script>
"""


# ============================================================
# BASIC CALCULATOR
# ============================================================

def tool_basic_calculator():

    return """
<h2>Online Calculator</h2>

<div class="grid">

<input
id="calcA"
type="number"
step="any"
placeholder="First number">

<input
id="calcB"
type="number"
step="any"
placeholder="Second number">

</div>

<button onclick="calculate('+')">+</button>
<button onclick="calculate('-')">−</button>
<button onclick="calculate('*')">×</button>
<button onclick="calculate('/')">÷</button>
<button onclick="calculate('%')">%</button>

<div id="calcOutput" class="output">
Result will appear here...
</div>

<script>

function calculate(operator) {

    const a =
        parseFloat(
            document.getElementById("calcA").value
        );

    const b =
        parseFloat(
            document.getElementById("calcB").value
        );

    if (
        Number.isNaN(a) ||
        Number.isNaN(b)
    ) {

        document.getElementById("calcOutput")
            .textContent =
            "Please enter valid numbers.";

        return;
    }

    let result;

    switch (operator) {

        case "+":
            result = a + b;
            break;

        case "-":
            result = a - b;
            break;

        case "*":
            result = a * b;
            break;

        case "/":
            result =
                b === 0
                ? "Cannot divide by zero"
                : a / b;
            break;

        case "%":
            result =
                b === 0
                ? "Cannot divide by zero"
                : a % b;
            break;

        default:
            result = "Unknown operation";
    }

    document.getElementById("calcOutput")
        .textContent =
        "Result: " + result;
}

</script>
"""


# ============================================================
# PERCENTAGE CALCULATOR
# ============================================================

def tool_percentage():

    return """
<h2>Percentage Calculator</h2>

<label>Percentage</label>

<input
id="percentValue"
type="number"
step="any"
placeholder="Example: 15">

<label>Number</label>

<input
id="percentNumber"
type="number"
step="any"
placeholder="Example: 200">

<button onclick="calculatePercentage()">
Calculate
</button>

<div id="percentOutput"
class="output"></div>

<script>

function calculatePercentage() {

    const p =
        parseFloat(
            document.getElementById(
                "percentValue"
            ).value
        );

    const n =
        parseFloat(
            document.getElementById(
                "percentNumber"
            ).value
        );

    if (
        Number.isNaN(p) ||
        Number.isNaN(n)
    ) {

        document.getElementById(
            "percentOutput"
        ).textContent =
            "Enter valid numbers.";

        return;
    }

    const result =
        n * p / 100;

    document.getElementById(
        "percentOutput"
    ).textContent =
        p + "% of " + n +
        " = " + result;
}

</script>
"""


# ============================================================
# COLOR CONVERTER
# ============================================================

def tool_color_converter():

    return """
    # ============================================================
# SECTION 4/4 — BUILD, INDEX, SITEMAP & DEPLOYMENT
# Empire Web Global Auto Builder
# ============================================================

import json
from datetime import datetime, timezone


# ============================================================
# CONFIGURATION
# ============================================================

# Smartlink / Advertisement URL
AD_LINK = "https://omg10.com/4/11349784"

# Maximum number of tools to generate.
# This uses however many names exist in TOOL_NAMES.
MAX_TOOLS = 1000


# ============================================================
# SAFE DIRECTORY SETUP
# ============================================================

def ensure_directories():

    TOOLS_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


# ============================================================
# BUILD ALL TOOLS
# ============================================================

def build_all_tools():

    ensure_directories()

    tools = prepare_tool_list()

    # Protect against accidentally generating
    # more tools than intended.
    tools = tools[:MAX_TOOLS]

    generated = write_tool_files(tools)

    return generated


# ============================================================
# GENERATE TOOLS INDEX
# ============================================================

def generate_tools_index(tools):

    site_url = SITE_URL.rstrip("/")

    cards = []

    for tool in tools:

        name = html.escape(
            str(tool["name"])
        )

        category = html.escape(
            str(tool["category"])
        )

        description = html.escape(
            str(tool.get(
                "description",
                f"Free online {name}."
            ))
        )

        slug = tool["slug"]

        cards.append(
            f"""
            <article class="tool-card">

                <span class="badge">
                    {category}
                </span>

                <h2>
                    <a href="/tools/{slug}.html">
                        {name}
                    </a>
                </h2>

                <p>
                    {description}
                </p>

                <a href="/tools/{slug}.html">
                    Open Tool →
                </a>

            </article>
            """
        )

    cards_html = "\n".join(cards)

    page = f"""<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>Empire Web Tools — Free Online Tools</title>

<meta name="description"
content="Free online tools for developers, creators, marketers, writers and everyday users.">

<meta name="robots"
content="index,follow">

<link rel="canonical"
href="{site_url}/">

<style>

:root {{
    --bg:#0b1120;
    --card:#111827;
    --primary:#38bdf8;
    --text:#f8fafc;
    --muted:#94a3b8;
    --border:#263449;
}}

* {{
    box-sizing:border-box;
}}

body {{
    margin:0;
    background:var(--bg);
    color:var(--text);
    font-family:
        system-ui,
        -apple-system,
        BlinkMacSystemFont,
        "Segoe UI",
        sans-serif;
    line-height:1.6;
}}

.container {{
    width:min(100% - 30px,1200px);
    margin:auto;
}}

header {{
    padding:50px 0 25px;
}}

.logo {{
    font-size:1.5rem;
    font-weight:900;
}}

.hero {{
    padding:20px 0 35px;
}}

h1 {{
    font-size:clamp(2rem,6vw,4rem);
    line-height:1.1;
    margin:10px 0;
}}

.hero p {{
    color:var(--muted);
    max-width:750px;
}}

.search {{
    width:100%;
    padding:15px;
    border-radius:12px;
    border:1px solid var(--border);
    background:#080e1a;
    color:white;
    font-size:1rem;
    margin:20px 0 30px;
}}

.tools {{
    display:grid;
    grid-template-columns:
        repeat(auto-fill,minmax(260px,1fr));
    gap:18px;
}}

.tool-card {{
    background:var(--card);
    border:1px solid var(--border);
    border-radius:16px;
    padding:20px;
}}

.tool-card h2 {{
    font-size:1.15rem;
}}

.tool-card p {{
    color:var(--muted);
    min-height:50px;
}}

a {{
    color:var(--primary);
    text-decoration:none;
}}

a:hover {{
    text-decoration:underline;
}}

.badge {{
    display:inline-block;
    font-size:.7rem;
    padding:4px 9px;
    border-radius:999px;
    border:1px solid rgba(56,189,248,.25);
    color:var(--primary);
}}

.ad-box {{
    margin:35px 0;
    padding:20px;
    text-align:center;
    border:1px solid var(--border);
    border-radius:14px;
}}

.ad-box small {{
    display:block;
    color:var(--muted);
    margin-bottom:6px;
}}

footer {{
    margin-top:50px;
    padding:30px 0;
    border-top:1px solid var(--border);
    color:var(--muted);
}}

@media(max-width:600px) {{

    .tools {{
        grid-template-columns:1fr;
    }}

}}

</style>

</head>

<body>

<div class="container">

<header>

<div class="logo">
<a href="{site_url}">
Empire Web Tools
</a>
</div>

</header>

<section class="hero">

<h1>
Free Online Tools
</h1>

<p>
A growing collection of useful browser-based
tools for developers, creators, marketers,
writers and everyday users.
</p>

</section>

<input
class="search"
id="toolSearch"
type="search"
placeholder="Search tools..."
aria-label="Search tools">

<div class="ad-box">

<small>ADVERTISEMENT</small>

<a
href="{html.escape(AD_LINK, quote=True)}"
target="_blank"
rel="nofollow sponsored noopener">
Discover useful tools and offers →
</a>

</div>

<main
class="tools"
id="toolsList">

{cards_html}

</main>

<footer>

<p>
© {datetime.now().year} Empire Web Tools.
All tools are free to use.
</p>

</footer>

</div>

<script>

const searchInput =
    document.getElementById("toolSearch");

const toolCards =
    document.querySelectorAll(".tool-card");

searchInput.addEventListener(
    "input",
    function() {{

        const query =
            this.value
            .toLowerCase()
            .trim();

        toolCards.forEach(
            card => {{

                const text =
                    card.textContent
                    .toLowerCase();

                card.style.display =
                    text.includes(query)
                    ? ""
                    : "none";
            }}
        );
    }}
);

</script>

</body>
</html>
"""

    Path("index.html").write_text(
        page,
        encoding="utf-8"
    )


# ============================================================
# GENERATE SITEMAP
# ============================================================

def generate_sitemap(tools):

    site_url = SITE_URL.rstrip("/")

    urls = [
        f"""
    <url>
        <loc>{site_url}/</loc>
        <changefreq>daily</changefreq>
        <priority>1.0</priority>
    </url>
"""
    ]

    for tool in tools:

        slug = html.escape(
            str(tool["slug"])
        )

        urls.append(
            f"""
    <url>
        <loc>{site_url}/tools/{slug}.html</loc>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
"""
        )

    sitemap = f"""<?xml version="1.0"
encoding="UTF-8"?>

<urlset
xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

{"".join(urls)}

</urlset>
"""

    Path("sitemap.xml").write_text(
        sitemap,
        encoding="utf-8"
    )


# ============================================================
# GENERATE ROBOTS.TXT
# ============================================================

def generate_robots():

    site_url = SITE_URL.rstrip("/")

    robots = f"""User-agent: *
Allow: /

Sitemap: {site_url}/sitemap.xml
"""

    Path("robots.txt").write_text(
        robots,
        encoding="utf-8"
    )


# ============================================================
# GENERATE TOOL MANIFEST
# ============================================================

def generate_manifest(tools):

    data = {
        "project": "Empire Web Tools",
        "generated_at": datetime.now(
            timezone.utc
        ).isoformat(),
        "tool_count": len(tools),
        "tools": [
            {
                "id": tool["id"],
                "name": tool["name"],
                "slug": tool["slug"],
                "category": tool["category"],
            }
            for tool in tools
        ]
    }

    Path("tools.json").write_text(
        json.dumps(
            data,
            indent=2,
            ensure_ascii=False
        ),
        encoding="utf-8"
    )


# ============================================================
# BUILD REPORT
# ============================================================

def generate_build_report(tools):

    report = {
        "status": "success",
        "generated_at": datetime.now(
            timezone.utc
        ).isoformat(),
        "tools_generated": len(tools),
        "real_implementations": sum(
            1
            for tool in tools
            if tool["slug"] in REAL_TOOLS
        ),
        "fallback_tools": sum(
            1
            for tool in tools
            if tool["slug"] not in REAL_TOOLS
        )
    }

    Path("build-report.json").write_text(
        json.dumps(
            report,
            indent=2
        ),
        encoding="utf-8"
    )

    return report


# ============================================================
# MAIN BUILD PIPELINE
# ============================================================

def run_build():

    print("=" * 60)
    print("EMPIRE WEB — GLOBAL BUILD")
    print("=" * 60)

    print("[1/6] Preparing directories...")

    ensure_directories()

    print("[2/6] Preparing tool catalog...")

    tools = prepare_tool_list()

    tools = tools[:MAX_TOOLS]

    print(
        f"      Tools in catalog: {len(tools)}"
    )

    print("[3/6] Generating tool pages...")

    generated = write_tool_files(tools)

    print(
        f"      Generated pages: {len(generated)}"
    )

    print("[4/6] Generating homepage...")

    generate_tools_index(
        generated
    )

    print("[5/6] Generating SEO files...")

    generate_sitemap(
        generated
    )

    generate_robots()

    generate_manifest(
        generated
    )

    print("[6/6] Generating build report...")

    report = generate_build_report(
        generated
    )

    print()
    print("=" * 60)
    print("BUILD COMPLETE")
    print("=" * 60)

    print(
        f"Total tools: "
        f"{report['tools_generated']}"
    )

    print(
        f"Real implementations: "
        f"{report['real_implementations']}"
    )

    print(
        f"Fallback tools: "
        f"{report['fallback_tools']}"
    )

    print()
    print("Generated:")
    print(" - index.html")
    print(" - sitemap.xml")
    print(" - robots.txt")
    print(" - tools.json")
    print(" - build-report.json")
    print(" - tools/*.html")
    print("=" * 60)


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":

    try:

        run_build()

    except Exception as error:

        print()
        print("=" * 60)
        print("BUILD FAILED")
        print("=" * 60)

        print(
            f"{type(error).__name__}: {error}"
        )

        raise
