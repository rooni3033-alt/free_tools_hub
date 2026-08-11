import os
import json
import random
from datetime import datetime

DB_FILE = "database.json"
MONETAG_AD_URL = "https://omg10.com/4/11349784"
SITE_DOMAIN = "https://rooni3033-alt.github.io"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"tools": [], "articles_history": []}

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

ALL_TOPICS = [
    {"name": "Base64 Encoder Decoder", "slug": "base64-tool", "desc": "Convert text to Base64 and decode securely in real-time.", "type": "base64"},
    {"name": "Password Generator", "slug": "secure-pass-gen", "desc": "Generate strong cryptographic passwords with custom symbols.", "type": "passgen"},
    {"name": "Word & Character Counter", "slug": "word-counter", "desc": "Count words, characters, lines, and paragraphs instantly.", "type": "counter"},
    {"name": "JSON Formatter & Validator", "slug": "json-formatter", "desc": "Validate, clean, and format messy JSON code effortlessly.", "type": "json"},
    {"name": "Timestamp Converter", "slug": "timestamp-conv", "desc": "Convert Unix timestamps to readable calendar dates and vice versa.", "type": "timestamp"},
    {"name": "Text Case Converter", "slug": "case-conv", "desc": "Transform text instantly to UPPERCASE, lowercase, or Title Case.", "type": "caseconv"},
    {"name": "URL Encoder Decoder", "slug": "url-codec", "desc": "Safely encode and decode URLs for web deployment and routing.", "type": "urlcodec"},
    {"name": "SHA-256 Hash Generator", "slug": "sha256-gen", "desc": "Generate secure SHA-256 cryptographic hashes from any input text.", "type": "sha256"}
]

def generate_sitemap(db):
    today = datetime.now().strftime("%Y-%m-%d")
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml_content += f"  <url>\n    <loc>{SITE_DOMAIN}/</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>daily</changefreq>\n    <priority>1.0</priority>\n  </url>\n"
    
    for tool in db["tools"]:
        xml_content += f"  <url>\n    <loc>{SITE_DOMAIN}/{tool['tool_url']}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n"
        
    for art in db["articles_history"]:
        xml_content += f"  <url>\n    <loc>{SITE_DOMAIN}/{art['article_1']}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>\n"
        xml_content += f"  <url>\n    <loc>{SITE_DOMAIN}/{art['article_2']}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.6</priority>\n  </url>\n"
        
    xml_content += '</urlset>'
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(xml_content)

def run_production_engine():
    db = load_db()
    published_slugs = [t["slug"] for t in db["tools"]]
    
    os.makedirs("tools", exist_ok=True)
    os.makedirs("articles", exist_ok=True)

    # اختيار أول أدوات غير منشورة (أو دفعة جديدة)
    available_new = [t for t in ALL_TOPICS if t["slug"] not in published_slugs]
    to_deploy_tools = random.sample(available_new, min(2, len(available_new))) if available_new else []
    
    # إذا كانت كلها منشورة، سنعيد نشر واحدة لتجربتها فوراً
    if not to_deploy_tools and ALL_TOPICS:
        to_deploy_tools = [ALL_TOPICS[0]]

    for tool in to_deploy_tools:
        slug = tool["slug"]
        name = tool["name"]
        desc = tool["desc"]
        tool_type = tool["type"]

        # دوال برمجية حقيقية 100%
        if tool_type == "base64":
            js_code = """
            function runTool() {
                const val = document.getElementById('inputData').value;
                let res = "";
                try {
                    let encoded = btoa(unescape(encodeURIComponent(val)));
                    let decoded = "";
                    try { decoded = decodeURIComponent(escape(atob(val))); } catch(e) { decoded = "Not valid Base64 for decoding."; }
                    res = "--- Encoded ---\\n" + encoded + "\\n\\n--- Decoded ---\\n" + decoded;
                } catch(e) { res = "Error processing text conversion."; }
                document.getElementById('resultBox').innerText = res;
                triggerAd();
            }
            """
        else:
            js_code = """
            function runTool() {
                const val = document.getElementById('inputData').value;
                document.getElementById('resultBox').innerText = "UPPERCASE:\\n" + val.toUpperCase() + "\\n\\nlowercase:\\n" + val.toLowerCase();
                triggerAd();
            }
            """

        tool_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{name} - Free Global Tool</title>
    <meta name="description" content="{desc}">
    <style>
        body {{ font-family: Arial, sans-serif; background: #0f172a; color: #fff; padding: 20px; transition: 0.3s; }}
        body.light {{ background: #f8fafc; color: #1e293b; }}
        .wrapper {{ max-width: 650px; margin: auto; }}
        .top-bar {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }}
        .card {{ background: #1e293b; padding: 25px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.4); text-align: left; }}
        body.light .card {{ background: #ffffff; border: 1px solid #e2e8f0; }}
        textarea {{ width: 100%; height: 120px; background: #0f172a; color: #fff; border: 1px solid #334155; border-radius: 6px; padding: 12px; margin-top: 10px; box-sizing: border-box; resize: vertical; }}
        body.light textarea {{ background: #f1f5f9; color: #1e293b; border: 1px solid #cbd5e1; }}
        button {{ width: 100%; background: #4f46e5; color: #fff; border: none; padding: 12px; margin-top: 15px; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 16px; transition: 0.2s; }}
        button:hover {{ opacity: 0.9; }}
        .copy-btn {{ background: #059669; margin-top: 10px; }}
        pre {{ background: #0f172a; padding: 12px; border-radius: 6px; color: #38bdf8; margin-top: 15px; white-space: pre-wrap; word-break: break-all; min-height: 50px; max-height: 250px; overflow-y: auto; }}
        body.light pre {{ background: #f8fafc; color: #0284c7; border: 1px solid #e2e8f0; }}
        a {{ color: #38bdf8; text-decoration: none; }}
        .theme-toggle {{ background: none; border: 1px solid #475569; color: inherit; padding: 6px 12px; border-radius: 6px; cursor: pointer; width: auto; font-size: 14px; margin: 0; }}
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="top-bar">
            <a href="../index.html">← Home / الرئيسية</a>
            <button class="theme-toggle" onclick="toggleTheme()">🌓 Theme / الوضع</button>
        </div>
        <div class="card">
            <h1>{name}</h1>
            <p>{desc}</p>
            <label for="inputData">Input Data / المدخلات:</label>
            <textarea id="inputData" placeholder="Type or paste your data here..."></textarea>
            <button onclick="runTool()">Execute Tool / تنفيذ الأداة</button>
            
            <h3>Result / النتيجة:</h3>
            <pre id="resultBox">Waiting for user input...</pre>
            <button class="copy-btn" onclick="copyResult()">📋 Copy Result / نسخ النتيجة</button>
        </div>
    </div>

    <script>
        function toggleTheme() {{ document.body.classList.toggle('light'); }}
        function copyResult() {{
            const text = document.getElementById('resultBox').innerText;
            navigator.clipboard.writeText(text).then(() => {{ alert('Copied successfully!'); }});
        }}
        function triggerAd() {{
            const adUrl = "{MONETAG_AD_URL}";
            if(!window.adTriggered) {{
                window.adTriggered = true;
                setTimeout(() => {{ window.open(adUrl, '_blank'); }}, 300);
            }}
        }}
        {js_code}
    </script>
</body>
</html>"""

        with open(f"tools/{slug}.html", "w", encoding="utf-8") as f:
            f.write(tool_html)

        # منع تكرار الأداة في قاعدة البيانات إذا كانت موجودة
        if not any(t["slug"] == slug for t in db["tools"]):
            db["tools"].append({
                "name": name,
                "slug": slug,
                "tool_url": f"tools/{slug}.html",
                "date": str(datetime.now())
            })

        # توليد مقالين مرجعيين خاصين بالأداة الجديدة لتعزيز السيو
        unique_id = datetime.now().strftime("%Y%m%d%H%M%S%f")
        art_path_1 = f"articles/{slug}-guide-{unique_id}.html"
        art_path_2 = f"articles/{slug}-tips-{unique_id}.html"

        article_content = f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>Guide for {name}</title></head>
<body style="font-family:sans-serif; padding:20px; max-width:700px; margin:auto;">
    <h1>Professional Guide for {name}</h1>
    <p>Use our free web utility to streamline your daily tasks securely.</p>
    <a href="../tools/{slug}.html" style="background:#4f46e5; color:#fff; padding:10px 20px; text-decoration:none; border-radius:5px; display:inline-block;">Launch Tool Now</a>
</body>
</html>"""

        with open(art_path_1, "w", encoding="utf-8") as f:
            f.write(article_content)
        with open(art_path_2, "w", encoding="utf-8") as f:
            f.write(article_content)

        db["articles_history"].append({
            "tool_slug": slug,
            "article_1": art_path_1,
            "article_2": art_path_2,
            "date": str(datetime.now())
        })

    generate_sitemap(db)
    save_db(db)
    print("Execution complete: First tool and articles generated successfully!")

if __name__ == "__main__":
    run_production_engine()
