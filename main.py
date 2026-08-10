import os
import json
import random
from datetime import datetime

DB_FILE = "database.json"
MONETAG_AD_URL = "https://omg10.com/4/11349784"
SITE_DOMAIN = "https://yourusername.github.io/your-repo-name" # استبدل برابط موقعك الحقيقي على غيت هوب

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"tools": [], "articles_history": []}

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

ALL_TOPICS = [
    {"name": "Base64 Encoder Decoder", "slug": "base64-tool", "desc": "Convert text to Base64 and vice versa instantly.", "type": "base64"},
    {"name": "JSON Formatter & Validator", "slug": "json-formatter", "desc": "Clean and format messy JSON code effortlessly.", "type": "json"},
    {"name": "Password Generator", "slug": "secure-pass-gen", "desc": "Generate strong, secure cryptographic passwords.", "type": "passgen"},
    {"name": "Word & Character Counter", "slug": "word-counter", "desc": "Count words, characters, and paragraphs in real-time.", "type": "counter"},
    {"name": "Image Compressor Pro", "slug": "image-compressor", "desc": "Compress images online without quality loss.", "type": "compressor"},
    {"name": "QR Code Generator", "slug": "qr-code-gen", "desc": "Generate custom QR codes instantly for links and text.", "type": "qrcode"},
    {"name": "Markdown to HTML", "slug": "markdown-to-html", "desc": "Convert markdown text to clean HTML code instantly.", "type": "markdown"},
    {"name": "Color Palette Extractor", "slug": "color-palette", "desc": "Extract color codes from images and styles.", "type": "color"},
    {"name": "Timestamp Converter", "slug": "timestamp-conv", "desc": "Convert unix timestamps to human-readable dates.", "type": "timestamp"},
    {"name": "CSS Box Shadow Generator", "slug": "box-shadow-gen", "desc": "Design modern CSS shadows visually and copy code.", "type": "shadow"}
]

COLOR_THEMES = [
    {"bg": "#0f172a", "box": "#1e293b", "btn": "#4f46e5"},
    {"bg": "#18181b", "box": "#27272a", "btn": "#059669"},
    {"bg": "#09090b", "box": "#18181b", "btn": "#dc2626"},
    {"bg": "#172554", "box": "#1e3a8a", "btn": "#2563eb"},
    {"bg": "#2e1065", "box": "#4c1d95", "btn": "#7c3aed"}
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

    # 1. نشر أدوات جديدة إذا توفرت
    available_new = [t for t in ALL_TOPICS if t["slug"] not in published_slugs]
    to_deploy_tools = random.sample(available_new, min(3, len(available_new))) if available_new else []

    for tool in to_deploy_tools:
        slug = tool["slug"]
        name = tool["name"]
        desc = tool["desc"]
        tool_type = tool["type"]
        theme = random.choice(COLOR_THEMES)

        js_logic = ""
        if tool_type == "base64":
            js_logic = """try { document.getElementById('result').innerText = btoa(document.getElementById('input').value); } catch(e) { document.getElementById('result').innerText = "Error encoding text."; }"""
        elif tool_type == "passgen":
            js_logic = """const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%&*!"; let pass = ""; for(let i=0; i<16; i++) pass += chars.charAt(Math.floor(Math.random() * chars.length)); document.getElementById('result').innerText = pass;"""
        elif tool_type == "counter":
            js_logic = """const text = document.getElementById('input').value; const words = text.trim() ? text.trim().split(/\\s+/).length : 0; const chars = text.length; document.getElementById('result').innerText = `Words / كلمات: ${words} | Characters / حروف: ${chars}`;"""
        elif tool_type == "json":
            js_logic = """try { const parsed = JSON.parse(document.getElementById('input').value); document.getElementById('result').innerText = JSON.stringify(parsed, null, 4); } catch(e) { document.getElementById('result').innerText = "Invalid JSON format!"; }"""
        else:
            js_logic = """document.getElementById('result').innerText = "Processed / تمت المعالجة: " + document.getElementById('input').value;"""

        tool_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{name} - Global Free Online Tool</title>
    <meta name="description" content="{desc}">
    <style>
        body {{ font-family: sans-serif; padding: 20px; background: {theme['bg']}; color: #fff; text-align: center; }}
        .lang-bar {{ margin-bottom: 15px; }}
        .lang-bar select {{ padding: 5px 10px; border-radius: 5px; background: {theme['box']}; color: #fff; border: 1px solid #444; }}
        .box {{ background: {theme['box']}; padding: 25px; border-radius: 12px; display: inline-block; max-width: 500px; width: 100%; box-shadow: 0 4px 6px rgba(0,0,0,0.3); }}
        textarea, button {{ width: 100%; padding: 10px; margin-top: 10px; border-radius: 6px; border: none; box-sizing: border-box; }}
        textarea {{ height: 100px; background: {theme['bg']}; color: #fff; }}
        button {{ background: {theme['btn']}; color: #fff; font-weight: bold; cursor: pointer; transition: 0.2s; }}
        button:hover {{ opacity: 0.9; }}
        #result {{ margin-top: 15px; font-weight: bold; white-space: pre-wrap; word-break: break-all; background: {theme['bg']}; padding: 10px; border-radius: 6px; text-align: left; }}
    </style>
</head>
<body>
    <div class="lang-bar">
        <label for="langSelect">🌐 Language / اللغة: </label>
        <select id="langSelect" onchange="changeLanguage()">
            <option value="en">English</option>
            <option value="ar">العربية</option>
            <option value="fr">Français</option>
            <option value="es">Español</option>
        </select>
    </div>
    <div class="box">
        <h1 id="toolTitle">{name}</h1>
        <p id="toolDesc">{desc}</p>
        <textarea id="input" placeholder="Enter input data..."></textarea>
        <button id="runBtn" onclick="processTool()">Run Tool</button>
        <div id="result">Result will appear here...</div>
    </div>
    <script>
        const translations = {{
            en: {{ placeholder: "Enter input data...", btn: "Run Tool", result: "Result will appear here..." }},
            ar: {{ placeholder: "أدخل البيانات هنا...", btn: "تشغيل الأداة", result: "النتيجة ستظهر هنا..." }},
            fr: {{ placeholder: "Entrez les données...", btn: "Exécuter", result: "Le résultat aparecerá ici..." }},
            es: {{ placeholder: "Ingrese los datos...", btn: "Ejecutar herramienta", result: "El resultado aparecerá aquí..." }}
        }};
        function changeLanguage() {{
            const lang = document.getElementById('langSelect').value;
            document.getElementById('input').placeholder = translations[lang].placeholder;
            document.getElementById('runBtn').innerText = translations[lang].btn;
            document.getElementById('result').innerText = translations[lang].result;
        }}
        function processTool() {{
            {js_logic}
            const adUrl = "{MONETAG_AD_URL}";
            if(!window.adOpened) {{
                window.adOpened = true;
                window.open(adUrl, '_blank');
            }}
        }}
    </script>
</body>
</html>"""
        with open(f"tools/{slug}.html", "w", encoding="utf-8") as f:
            f.write(tool_html)

        db["tools"].append({
            "name": name,
            "slug": slug,
            "tool_url": f"tools/{slug}.html",
            "date": str(datetime.now())
        })

    # 2. توليد مستمر للمقالات (مقالتين لكل أداة مختارة في كل دورة)
    all_tools = db["tools"]
    if all_tools:
        target_tools = random.sample(all_tools, min(5, len(all_tools)))

        for tool in target_tools:
            slug = tool["slug"]
            name = tool["name"]

            sample_links = random.sample(all_tools, min(4, len(all_tools)))
            internal_links_html = "<h3>Related Global Utilities:</h3><ul>"
            for link in sample_links:
                internal_links_html += f"<li><a href='../tools/{link['slug']}.html'>{link['name']}</a></li>"
            internal_links_html += "</ul>"

            unique_id = datetime.now().strftime("%Y%m%d%H%M%S%f")

            article_1 = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Advanced Guide & Professional Tips for {name}</title>
    <style>body{{font-family:sans-serif;max-width:800px;margin:auto;padding:20px;line-height:1.7;color:#333;}} .btn{{background:#4f46e5;color:#fff;padding:12px 24px;text-decoration:none;border-radius:6px;display:inline-block;font-weight:bold;margin:20px 0;}}</style>
</head>
<body>
    <h1>Everything You Need to Know About {name}</h1>
    <p>Explore professional workflows and deep insights on optimizing your daily tasks using our dedicated web utility.</p>
    <a class="btn" href="../tools/{slug}.html">Launch {name} Now</a>
    <h2>Why This Tool Ranks as Best in Class</h2>
    <p>Completely free, fast execution, and zero registration required makes it the ideal choice for modern developers and creators worldwide.</p>
    <hr>
    {internal_links_html}
</body>
</html>"""

            article_2 = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>How to Solve Daily Bottlenecks and Optimize Workflows with {name}</title>
    <style>body{{font-family:sans-serif;max-width:800px;margin:auto;padding:20px;line-height:1.7;color:#333;}} .btn{{background:#10b981;color:#fff;padding:12px 24px;text-decoration:none;border-radius:6px;display:inline-block;font-weight:bold;margin:20px 0;}}</style>
</head>
<body>
    <h1>Boost Productivity Using {name} Online</h1>
    <p>Streamline your digital operations instantly with our zero-bloat browser solution designed for maximum efficiency.</p>
    <a class="btn" href="../tools/{slug}.html">Access {name} Free</a>
    <h2>Get Instant Results</h2>
    <p>Save this resource to your bookmarks for fast access whenever you face complex computational tasks.</p>
    <hr>
    {internal_links_html}
</body>
</html>"""

            art_path_1 = f"articles/{slug}-guide-{unique_id}.html"
            art_path_2 = f"articles/{slug}-tips-{unique_id}.html"

            with open(art_path_1, "w", encoding="utf-8") as f:
                f.write(article_1)
            with open(art_path_2, "w", encoding="utf-8") as f:
                f.write(article_2)

            db["articles_history"].append({
                "tool_slug": slug,
                "article_1": art_path_1,
                "article_2": art_path_2,
                "date": str(datetime.now())
            })

    generate_sitemap(db)
    save_db(db)
    print("Full production pipeline executed successfully.")

if __name__ == "__main__":
    run_production_engine()
