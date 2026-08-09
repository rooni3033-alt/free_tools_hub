import os
import json
import random
from datetime import datetime

DB_FILE = "database.json"
MONETAG_AD_URL = "https://omg10.com/4/11349784"

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"tools": [], "articles_history": []}

def save_db(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

ALL_TOPICS = [
    {"name": "Base64 Encoder Decoder", "slug": "base64-tool", "desc": "Convert text to Base64 and vice versa instantly."},
    {"name": "JSON Formatter & Validator", "slug": "json-formatter", "desc": "Clean and format messy JSON code effortlessly."},
    {"name": "Password Generator", "slug": "secure-pass-gen", "desc": "Generate strong, secure cryptographic passwords."},
    {"name": "Word & Character Counter", "slug": "word-counter", "desc": "Count words, characters, and paragraphs in real-time."},
    {"name": "Image Compressor Pro", "slug": "image-compressor", "desc": "Compress images online without quality loss."},
    {"name": "QR Code Generator", "slug": "qr-code-gen", "desc": "Generate custom QR codes instantly for links and text."},
    {"name": "Markdown to HTML", "slug": "markdown-to-html", "desc": "Convert markdown text to clean HTML code instantly."},
    {"name": "Color Palette Extractor", "slug": "color-palette", "desc": "Extract color codes from images and styles."},
    {"name": "Timestamp Converter", "slug": "timestamp-conv", "desc": "Convert unix timestamps to human-readable dates."},
    {"name": "CSS Box Shadow Generator", "slug": "box-shadow-gen", "desc": "Design modern CSS shadows visually and copy code."}
]

def run_production_engine():
    db = load_db()
    published_slugs = [t["slug"] for t in db["tools"]]
    
    os.makedirs("tools", exist_ok=True)
    os.makedirs("articles", exist_ok=True)

    available_new = [t for t in ALL_TOPICS if t["slug"] not in published_slugs]
    to_deploy = random.sample(available_new, min(5, len(available_new))) if available_new else []

    for tool in to_deploy:
        slug = tool["slug"]
        name = tool["name"]
        desc = tool["desc"]

        tool_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{name} - Free Online Tool</title>
    <meta name="description" content="{desc}">
    <style>body{{font-family:sans-serif;padding:30px;background:#0f172a;color:#fff;text-align:center;}} .box{{background:#1e293b;padding:25px;border-radius:12px;display:inline-block;max-width:500px;width:100%;}} input, button{{width:100%;padding:10px;margin-top:10px;border-radius:6px;border:none;}} button{{background:#4f46e5;color:#fff;font-weight:bold;cursor:pointer;}}</style>
</head>
<body>
    <div class="box">
        <h1>{name}</h1>
        <p>{desc}</p>
        <input type="text" id="input" placeholder="Enter input data...">
        <button onclick="processTool()">Run Tool</button>
        <div id="result" style="margin-top:15px;font-weight:bold;"></div>
    </div>
    <script>
        function processTool() {{
            document.getElementById('result').innerText = "Processed successfully!";
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

    all_tools = db["tools"]
    if all_tools:
        target_tools = random.sample(all_tools, min(8, len(all_tools)))

        for tool in target_tools:
            slug = tool["slug"]
            name = tool["name"]

            sample_links = random.sample(all_tools, min(5, len(all_tools)))
            internal_links_html = "<h3>Related Free Utilities:</h3><ul>"
            for link in sample_links:
                internal_links_html += f"<li><a href='../tools/{link['slug']}.html'>{link['name']}</a></li>"
            internal_links_html += "</ul>"

            unique_id = datetime.now().strftime("%Y%m%d%H%M%S%f")

            article_1 = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Advanced Guide & Tips for {name}</title>
    <style>body{{font-family:sans-serif;max-width:800px;margin:auto;padding:20px;line-height:1.7;color:#333;}} .btn{{background:#4f46e5;color:#fff;padding:12px 24px;text-decoration:none;border-radius:6px;display:inline-block;font-weight:bold;margin:20px 0;}}</style>
</head>
<body>
    <h1>Everything You Need to Know About {name}</h1>
    <p>Explore professional workflows and deep insights on optimizing your tasks using our dedicated web utility.</p>
    <a class="btn" href="../tools/{slug}.html">Launch {name} Now</a>
    <h2>Why This Tool Ranks as Best in Class</h2>
    <p>Completely free, fast execution, and zero registration required makes it the ideal choice for modern developers and creators.</p>
    <hr>
    {internal_links_html}
</body>
</html>"""

            article_2 = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>How to Solve Daily Bottlenecks with {name}</title>
    <style>body{{font-family:sans-serif;max-width:800px;margin:auto;padding:20px;line-height:1.7;color:#333;}} .btn{{background:#10b981;color:#fff;padding:12px 24px;text-decoration:none;border-radius:6px;display:inline-block;font-weight:bold;margin:20px 0;}}</style>
</head>
<body>
    <h1>Boost Productivity Using {name} Online</h1>
    <p>Streamline your digital operations instantly with our zero-bloat browser solution.</p>
    <a class="btn" href="../tools/{slug}.html">Access {name} Free</a>
    <h2>Get Instant Results</h2>
    <p>Save this resource to your bookmarks for fast access whenever you face complex tasks.</p>
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

    save_db(db)
    print("Full production pipeline with integrated Monetag ads executed successfully.")

if __name__ == "__main__":
    run_production_engine()
