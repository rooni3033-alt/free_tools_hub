#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Empire Web Engine v4 — Clean & Working
500 Real Functional Tools + Infinite Articles
"""

import json
import random
from datetime import datetime
from pathlib import Path

TOOLS_DIR = Path("./tools")
ARTICLES_DIR = Path("./articles")
DB_FILE = Path("./database.json")
MAX_TOOLS = 500
TOOLS_PER_CYCLE = 5
ARTICLES_PER_CYCLE = 2
AD_LINK = "https://omg10.com/4/11349784"

TOOL_NAMES = [
    "JSON Formatter", "Base64 Encoder/Decoder", "URL Encoder/Decoder", "Password Generator",
    "Color Converter", "Unit Converter", "Word Counter", "Lorem Ipsum Generator",
    "QR Code Generator", "Markdown Preview", "CSS Minifier", "HTML Entities Converter",
    "Hash Generator", "Case Converter", "CSV to JSON", "JSON to CSV",
    "Image to Base64", "Base64 to Image", "Diff Checker", "Regex Tester",
    "Number Base Converter", "Percentage Calculator", "Loan Calculator", "BMI Calculator",
    "Age Calculator", "Stopwatch", "Countdown Timer", "Pomodoro Timer",
    "Random Number Generator", "UUID Generator", "Slug Generator", "Duplicate Remover",
    "Line Sorter", "Text Reverser", "Palindrome Checker", "IP Address Validator",
    "Email Validator", "Credit Card Validator", "Barcode Generator", "Morse Code Translator",
    "Caesar Cipher", "Binary Converter", "Hex Converter", "HTML Preview",
    "Box Shadow Generator", "Flexbox Generator", "Gradient Generator", "Border Radius Generator",
    "Aspect Ratio Calculator", "Screen Resolution Checker", "Browser Info", "Meta Tag Generator",
    "Robots.txt Generator", "Sitemap Generator", "Twitter Card Generator", "Open Graph Generator",
    "Favicon Generator", "Placeholder Image Generator", "Meme Generator", "Image Resizer",
    "ASCII Art Generator", "Typing Speed Test", "World Clock", "Timezone Converter",
    "Date Difference Calculator", "Days Between Dates", "Invoice Generator", "Receipt Maker",
    "Password Strength Checker", "Username Generator", "Business Card Maker", "Resume Builder",
    "JSON Path Finder", "XML Formatter", "YAML to JSON", "SQL Formatter",
    "Cron Expression Parser", "Unix Timestamp Converter", "Color Palette Generator", "Fake Data Generator",
    "HTTP Status Checker", "JWT Decoder", "HTML Table Generator", "Chart Maker",
    "Mind Map Tool", "Flowchart Maker", "Certificate Generator", "Badge Maker",
    "Leaderboard Creator", "Quiz Maker", "Poll Maker", "Survey Builder",
    "Todo List", "Kanban Board", "Habit Tracker", "Expense Tracker",
    "Budget Planner", "Focus Timer", "Tip Calculator", "Bill Splitter",
    "Tax Calculator", "VAT Calculator", "ROI Calculator", "Currency Converter",
    "Fuel Cost Calculator", "Trip Cost Estimator", "Mileage Tracker", "Calendar Generator",
    "Prime Number Checker", "Fibonacci Calculator", "Factorial Calculator", "GCD LCM Calculator",
    "Equation Solver", "Matrix Calculator", "Statistics Calculator", "Probability Calculator",
    "Fraction Calculator", "Ratio Calculator", "Square Root Calculator", "Logarithm Calculator",
    "Trigonometry Calculator", "Circle Calculator", "Triangle Solver", "Distance Calculator",
    "Slope Calculator", "Compound Interest Calculator", "Retirement Calculator", "Mortgage Calculator",
    "Car Loan Calculator", "Savings Calculator", "Investment Calculator", "Break-even Calculator",
    "Ohm's Law Calculator", "Power Calculator", "Resistor Calculator", "LED Resistor Calculator",
    "Subnet Calculator", "CIDR Calculator", "Binary Calculator", "IPv6 Calculator",
    "MD5 Hash", "SHA1 Hash", "SHA256 Hash", "SHA512 Hash",
    "Checksum Calculator", "HMAC Generator", "NanoID Generator", "Token Generator",
    "RSA Key Generator", "SSL Checker", "Port Scanner", "DNS Lookup",
    "Whois Lookup", "IP Geolocation", "URL Parser", "Redirect Checker",
    "HTTP Header Checker", "AES Encrypt/Decrypt", "Base32 Converter", "Base58 Converter",
    "Punycode Converter", "URL Shortener", "UTM Builder", "Embed Code Generator",
    "Iframe Generator", "RSS Feed Generator", "Breadcrumb Generator", "Pagination Generator",
    "Tag Cloud Generator", "Clock Widget", "Counter Widget", "Progress Bar Generator",
    "Loading Spinner Generator", "Avatar Generator", "Identicon Generator", "Profile Card Maker",
    "Social Share Link Generator", "Schema Markup Generator", "JSON-LD Generator", "WhatsApp Link Generator",
    "Deep Link Generator", "PWA Manifest Generator", "App Icon Generator", "Maskable Icon Generator",
    "Favicon Converter", "Windows Tile Generator", "Safari Pinned Tab Generator", "Theme Color Generator",
    "HTML Minifier", "JavaScript Minifier", "JSON Validator", "XML Validator",
    "CSS Prefix Generator", "Sprite Generator", "Data URI Generator", "Favicon from Text",
    "Pattern Generator", "Noise Texture Generator", "Gradient Mesh Generator", "Duotone Image Effect",
    "Image Color Extractor", "Font Pairing Suggester", "Icon Font Generator", "SVG Optimizer",
    "SVG to PNG Converter", "PNG to SVG Converter", "Image Compressor", "PDF Merger",
    "PDF Splitter", "PDF to Image", "Image to PDF", "Text to Speech",
    "Speech to Text", "Language Detector", "Character Counter", "Syllable Counter",
    "Reading Time Calculator", "Keyword Density Checker", "SERP Preview", "Meta Length Checker",
    "Redirect Chain Checker", "Broken Link Checker", "Page Speed Score", "Core Web Vitals Checker",
    "Mobile Emulator", "Responsive Design Tester", "Dark Mode Preview", "Accessibility Checker",
    "Color Contrast Checker", "WCAG Compliance Checker", "ARIA Label Generator", "Skip Link Generator",
    "Focus Indicator Checker", "Form Label Checker", "Alt Text Generator", "Caption Generator",
    "Transcript Generator", "Podcast Notes Generator", "Show Notes Formatter", "Chapter Marker Generator",
    "Video Thumbnail Generator", "GIF Maker", "Video Trimmer", "Audio Cutter",
    "MP3 Converter", "Video to GIF", "GIF to Video", "Subtitle Generator",
    "Beat Maker", "Tempo Calculator", "Key Finder", "Chord Progression Generator",
    "Lyrics Formatter", "Setlist Maker", "Tour Dates Formatter", "Merch Price Calculator",
    "Shipping Cost Estimator", "Package Tracker", "Label Generator", "Packing List Maker",
    "Inventory Counter", "Reorder Calculator", "Safety Stock Calculator", "Lead Time Calculator",
    "Supplier Scorecard", "Purchase Order Generator", "Bill of Materials", "Work Order Generator",
    "Timesheet Calculator", "Attendance Tracker", "Leave Calculator", "Payroll Estimator",
    "Commission Calculator", "Bonus Calculator", "Overtime Calculator", "Shift Planner",
    "Meeting Cost Calculator", "Stand-up Timer", "Sprint Calculator", "Velocity Tracker",
    "Burndown Chart Generator", "Release Notes Generator", "Changelog Formatter", "Version Comparator",
    "Git Command Builder", "Dockerfile Generator", "Docker Compose Builder", "Kubernetes YAML Generator",
    "Terraform Generator", "CloudFormation Template", "Serverless Function Generator", "API Endpoint Tester",
    "Webhook Tester", "GraphQL Query Builder", "REST API Client", "SOAP Request Builder",
    "gRPC Tester", "Postman Collection Generator", "OpenAPI Generator", "Swagger UI Generator",
    "API Documentation Generator", "SDK Code Generator", "Code Linter", "Code Formatter",
    "Static Analysis Report", "Dependency Checker", "Vulnerability Scanner", "License Checker",
    "Code Coverage Reporter", "Benchmark Tool", "Profiler Report", "Log Analyzer",
    "Error Tracker", "Crash Reporter", "Performance Monitor", "Uptime Monitor",
    "Status Page Generator", "Incident Report", "Alert Configurator", "On-call Schedule",
    "Runbook Generator", "Playbook Maker", "Wiki Generator", "FAQ Builder",
    "Help Center Generator", "Chatbot Script", "Live Chat Widget", "Ticket Form Builder",
    "Feedback Form", "Survey Template", "Poll Widget", "Quiz Template",
    "Exam Generator", "Certificate Template", "Badge Template", "Leaderboard Widget",
    "Gamification Rules", "Loyalty Points Calculator", "Referral Link Generator", "Affiliate Link Builder",
    "Coupon Generator", "Discount Calculator", "Price Comparison Tool", "Shipping Calculator",
    "Tax Rate Finder", "Duty Calculator", "Import Cost Estimator", "Currency Exchange Rate",
    "Stock Portfolio Tracker", "Dividend Calculator", "Crypto Profit Calculator", "Mining Calculator",
    "Staking Rewards Calculator", "Gas Fee Estimator", "NFT Royalty Calculator", "Smart Contract Analyzer",
    "Wallet Address Validator", "Transaction Decoder", "Block Explorer", "Node Status Checker",
    "Network Hashrate Calculator", "Difficulty Calculator", "Reward Halving Countdown", "Mempool Visualizer",
    "Lightning Network Fee", "Channel Capacity Calculator", "Routing Fee Estimator", "Bitcoin Fee Calculator",
    "Ethereum Gas Tracker", "Polygon Bridge Fee", "Arbitrum Fee Calculator", "Optimism Fee Estimator",
    "Cross-chain Swap Calculator", "Bridge Fee Comparator", "Layer 2 Savings Calculator", "Rollup Cost Calculator",
    "ZK Proof Generator", "Merkle Tree Builder", "Signature Verifier", "Multi-sig Configurator",
    "Timelock Calculator", "Escrow Builder", "Atomic Swap Script", "HTLC Generator",
    "State Channel Calculator", "Payment Channel Fee", "Streaming Money Calculator", "Micro-payment Router",
    "Data URI to File", "File to Data URI", "Blob URL Generator", "Object URL Creator",
    "File Type Detector", "MIME Type Lookup", "Magic Number Checker", "File Signature Analyzer",
    "Hex Dump Viewer", "Binary Viewer", "Base64 Validator", "URL Safe Base64",
    "Padding Calculator", "Checksum Verifier", "Hash Comparator", "File Integrity Checker",
    "Directory Tree Generator", "File Size Comparator", "Duplicate File Finder", "Empty Folder Detector",
    "File Renamer Bulk", "Extension Changer", "Path Validator", "Filename Sanitizer",
    "Slug Generator Advanced", "Permalink Builder", "Breadcrumb JSON-LD", "Site Architecture Visualizer",
    "Internal Link Mapper", "Orphan Page Finder", "Crawl Budget Estimator", "Indexability Checker",
    "Canonical URL Builder", "Hreflang Tag Generator", "Geo-targeting Checker", "Language Selector",
    "Cookie Consent Generator", "GDPR Banner Maker", "CCPA Notice Builder", "Privacy Policy Generator",
    "Terms Generator", "Disclaimer Maker", "EULA Generator", "Return Policy Builder",
    "Shipping Policy Maker", "Refund Calculator", "Exchange Rate Tracker", "Price History Chart",
    "Competitor Price Monitor", "Dynamic Pricing Calculator", "A/B Test Calculator", "Statistical Significance",
    "Sample Size Calculator", "Confidence Interval", "Standard Deviation", "Variance Calculator",
    "Z-Score Calculator", "T-Test", "Chi-Square", "Correlation Calculator",
    "Regression Analyzer", "Data Visualizer", "Chart Type Recommender", "Color Scale Generator",
    "Heatmap Data Generator", "Treemap Calculator", "Sankey Diagram Data", "Radar Chart Builder",
    "Bubble Chart Data", "Candlestick Generator", "Network Graph Data", "Org Chart Builder",
    "Family Tree Maker", "Timeline Generator", "Roadmap Builder", "Release Planner",
    "Sprint Goal Generator", "User Story Formatter", "Acceptance Criteria Builder", "Definition of Done",
    "Sprint Retrospective", "Team Health Check", "Velocity Forecast", "Capacity Planner",
    "Workload Balancer", "Skill Matrix Generator", "RACI Matrix", "Stakeholder Map",
    "Communication Plan", "Risk Register", "Issue Log", "Decision Log",
    "Assumption Tracker", "Dependency Mapper", "Constraint Analyzer", "Success Criteria",
    "KPI Dashboard", "OKR Tracker", "Goal Setting", "Milestone Planner",
    "Deliverable Tracker", "Quality Checklist", "Review Template", "Sign-off Form",
    "Handover Document", "Knowledge Transfer Plan", "Onboarding Checklist", "Offboarding Form",
    "Exit Interview", "Performance Review", "360 Feedback", "Competency Assessment",
    "Training Plan", "Certification Tracker", "Learning Path", "Skill Gap Analyzer",
    "Career Ladder", "Promotion Calculator", "Salary Benchmark", "Benefits Comparator",
    "Remote Work Calculator", "Office Cost Estimator", "Commute Cost", "Carbon Footprint",
    "Sustainability Score", "Green Policy Generator", "ESG Report", "Impact Calculator",
    "Donation Calculator", "Volunteer Hours Tracker", "CSR Report", "Diversity Dashboard",
    "Inclusion Index", "Accessibility Score", "Bias Checker", "Inclusive Language",
    "Pronoun Generator", "Name Pronunciation", "Cultural Calendar", "Holiday Planner",
    "Time Off Calculator", "Shift Swap", "Overtime Bank", "Comp Time Calculator",
    "Flex Schedule Maker", "Compressed Workweek", "Job Sharing Calculator", "Part-time Pro-rata",
    "Contractor Rate", "Freelance Quote", "Project Estimator", "Scope Creep Calculator",
    "Change Request Cost", "Impact Analysis", "Stakeholder Impact", "Communication Impact",
    "Training Impact", "Adoption Tracker", "Usage Analytics", "Feature Flag Calculator",
    "Canary Deploy Risk", "Blue-Green Switch", "Rollback Time", "Recovery Time",
    "Mean Time to Repair", "Mean Time Between Failures", "Availability Calculator", "Reliability Score",
    "Maintainability Index", "Technical Debt Calculator", "Code Complexity", "Cyclomatic Complexity",
    "Cognitive Complexity", "Halstead Metrics", "Lines of Code Counter", "Comment Ratio",
    "Documentation Coverage", "API Coverage", "Test Coverage", "Mutation Score",
    "Fuzzing Results", "Property-based Test", "Contract Test", "Integration Test",
    "E2E Test", "Visual Regression", "Performance Test", "Load Test",
    "Stress Test", "Spike Test", "Soak Test", "Chaos Engineering",
    "Disaster Recovery Test", "Backup Verification", "Restore Time", "Data Integrity",
    "Consistency Check", "Replication Lag", "Failover Time", "Split-brain Detector",
    "Quorum Calculator", "Consensus Algorithm", "Byzantine Fault", "CAP Theorem",
    "PACELC Analysis", "Eventual Consistency", "Strong Consistency", "Linearizability",
    "Serializability", "Snapshot Isolation", "Read Committed", "Read Uncommitted",
    "Repeatable Read", "Serializable Snapshot", "Two-phase Commit", "Saga Pattern",
    "Outbox Pattern", "Inbox Pattern", "CQRS Calculator", "Event Sourcing Replay",
    "Materialized View", "Projection Rebuilder", "Read Model", "Write Model",
    "Command Handler", "Query Handler", "Domain Event", "Integration Event",
    "Notification Event", "Scheduled Task", "Recurring Job", "Background Job",
    "Queue Depth", "Dead Letter Queue", "Retry Policy", "Circuit Breaker",
    "Bulkhead Pattern", "Timeout Policy", "Fallback Strategy", "Cache-aside",
    "Read-through Cache", "Write-through Cache", "Write-behind Cache", "Cache Invalidation",
    "Cache Warming", "Cache Eviction", "TTL Calculator", "LRU Simulator",
    "LFU Calculator", "FIFO Queue", "LIFO Stack", "Priority Queue",
    "Deque Operations", "Heap Visualizer", "Graph Traversal", "Tree Balancer",
    "Red-Black Tree", "AVL Tree", "B-Tree Calculator", "Trie Operations",
    "Suffix Array", "Inverted Index", "Bloom Filter", "Skip List",
    "Segment Tree", "Fenwick Tree", "Disjoint Set", "Union-Find",
    "Topological Sort", "Strongly Connected", "Bridge Finder", "Articulation Point",
    "Minimum Spanning Tree", "Shortest Path", "Max Flow", "Min Cut",
    "Bipartite Checker", "Graph Coloring", "Hamiltonian Path", "Eulerian Path",
    "Traveling Salesman", "Knapsack Solver", "Subset Sum", "Partition Problem",
    "Longest Common Subsequence", "Edit Distance", "Levenshtein Distance", "Hamming Distance",
    "Jaro-Winkler", "Soundex Generator", "Metaphone", "Double Metaphone",
    "NYSIIS", "Caverphone", "Match Rating", "Phonetic Algorithm",
    "String Metric", "Similarity Score", "Fuzzy Matching", "Approximate String",
    "Regex Builder", "Glob Pattern", "Wildcard Matcher", "Pattern Extractor",
    "Named Entity", "Part of Speech", "Dependency Parse", "Constituency Parse",
    "Sentiment Analysis", "Text Classification", "Topic Modeling", "Keyword Extraction",
    "Text Summarization", "Abstractive Summary", "Extractive Summary", "Headline Generator",
    "Title Optimizer", "Meta Description AI", "Slug Optimizer", "Category Suggester",
    "Tag Recommender", "Related Article", "Content Calendar", "Editorial Workflow",
    "Publishing Schedule", "Content Brief", "Style Guide Checker", "Grammar Checker",
    "Plagiarism Detector", "Readability Score", "Flesch Reading Ease", "Flesch-Kincaid",
    "Gunning Fog", "SMOG Index", "Coleman-Liau", "Automated Readability",
    "Lexical Diversity", "Type-Token Ratio", "Hapax Legomena", "Zipf's Law",
    "N-gram Analyzer", "Collocation Finder", "Concordance Builder", "Word Cloud",
    "Frequency List", "Stop Word Remover", "Stemmer", "Lemmatizer",
    "Tokenization", "Sentence Splitter", "Paragraph Parser", "Document Chunker",
    "Embedding Calculator", "Vector Similarity", "Cosine Similarity", "Euclidean Distance",
    "Manhattan Distance", "Chebyshev Distance", "Minkowski Distance", "Mahalanobis Distance",
    "Jaccard Index", "Dice Coefficient", "Overlap Coefficient", "Tversky Index",
    "Sørensen-Dice", "Tanimoto Coefficient", "Otsuka-Ochiai", "Morisita Overlap",
    "Horn Index", "Renkonen Similarity", "Kulczynski Coefficient", "Bray-Curtis",
    "Canberra Distance", "Kullback-Leibler", "Jensen-Shannon", "Bhattacharyya Distance",
    "Hellinger Distance", "Wasserstein Distance", "Energy Distance", "Maximum Mean Discrepancy"
]

CATEGORIES = [
    "Developer", "Designer", "SEO", "Security", "Productivity",
    "Converter", "Calculator", "Analyzer", "Generator", "Formatter",
    "Tester", "Monitor", "Optimizer", "Utility", "Math"
]

AR_TOPICS = [
    "الذكاء الاصطناعي", "التعلم الآلي", "الحوسبة السحابية", "الأمن السيبراني", "تطوير التطبيقات",
    "تصميم المواقع", "تحسين محركات البحث", "التسويق الرقمي", "التجارة الإلكترونية", "إنترنت الأشياء",
    "البلوكتشين", "العملات الرقمية", "الحوسبة الكمية", "الواقع المعزز", "الواقع الافتراضي"
]

EN_TOPICS = [
    "Artificial Intelligence", "Machine Learning", "Cloud Computing", "Cybersecurity", "App Development",
    "Web Design", "SEO", "Digital Marketing", "E-commerce", "IoT",
    "Blockchain", "Cryptocurrency", "Quantum Computing", "Augmented Reality", "Virtual Reality"
]

AR_TEMPLATES = [
    {"title": "أفضل {count} أداة مجانية لتسريع {task} في {year}",
     "body": "في عالم {domain} المتسارع، يبحث الجميع عن حلول فعّالة. أدوات {tool_type} المجانية تتيح لك {feature} بدون تسجيل. جربها الآن."},
    {"title": "دليلك الشامل لـ {topic}: نصائح مالية وتقنية {year}",
     "body": "فهم {topic} يوفر عليك آلاف الدولارات. من خلال {strategy}، تقلل النفقات {percent}%. أدواتنا المجانية توفر كل ما تحتاجه."},
    {"title": "كيف تُضاعف إنتاجيتك باستخدام {tool_type} المجانية؟",
     "body": "{percent}% من المستخدمين يضيعون ساعات في مهام يمكن إنجازها بضغطة زر. بأدوات {domain}، تُنجز {task} في ثوانٍ."},
    {"title": "{year}: سنة التحول الرقمي مع {topic}",
     "body": "لم يعد التحول الرقمي خياراً. مع {topic}، أصبحت أدوات {domain} متاحة للجميع مجاناً. ابدأ رحلتك اليوم."},
    {"title": "5 أخطاء مالية يقع فيها رواد الأعمال وكيف تتجنبها",
     "body": "{percent}% من الشركات الناشئة تفشل بسبب سوء إدارة المالية. أدوات {domain} المجانية تساعدك على تتبع كل قرش."}
]

EN_TEMPLATES = [
    {"title": "Top {count} Free Tools to Accelerate {task} in {year}",
     "body": "In the fast-paced world of {domain}, everyone seeks efficient solutions. Free {tool_type} tools let you {feature} without registration. Try them now."},
    {"title": "The Ultimate Guide to {topic}: Financial & Tech Tips for {year}",
     "body": "Understanding {topic} saves you thousands annually. Through {strategy}, you reduce expenses by {percent}%. Our free tools provide everything you need."},
    {"title": "How to Double Your Productivity Using Free {tool_type}",
     "body": "{percent}% of users waste hours on tasks doable in one click. With {domain} tools, you complete {task} in seconds and save money."},
    {"title": "{year}: The Year of Digital Transformation with {topic}",
     "body": "Digital transformation is no longer optional. With {topic}, {domain} tools are now freely available to everyone. Start your journey today."},
    {"title": "5 Financial Mistakes Entrepreneurs Make & How to Avoid Them",
     "body": "{percent}% of startups fail due to poor financial management. Free {domain} tools help you track every penny and accomplish {task} efficiently."}
]

DOMAINS = ["Technology", "Business", "Marketing", "Design", "Programming", "Security", "SEO", "E-commerce", "Finance", "Entrepreneurship"]
TASKS = ["task management", "data analysis", "web design", "content writing", "social media", "reporting", "performance monitoring", "automation", "file conversion", "image compression", "password generation", "speed testing"]
PROFESSIONALS = ["Developer", "Designer", "Marketer", "Entrepreneur", "Data Analyst", "Project Manager", "Content Writer", "SEO Expert", "Financial Advisor", "Tech Lead"]
FEATURES = ["direct export", "collaborative sharing", "app integration", "full customization", "offline work", "auto encryption", "backup", "smart alerts"]
CONCEPTS = ["workflow automation", "data analytics", "cloud integration", "resource management", "performance optimization", "cost reduction", "revenue growth", "customer experience"]
STRATEGIES = ["automating repetitive tasks", "using free tools", "focusing on quality", "delegating tasks", "analyzing data regularly", "improving processes"]
TOOL_TYPES = ["file converters", "data analyzers", "project managers", "graphic designers", "performance optimizers", "security", "backup", "collaboration", "calculators", "converters"]
SAVINGS = ["$100", "$200", "$500", "$50", "$300", "$150"]
PERCENTS = ["30", "40", "50", "60", "70", "80", "90"]


def load_db():
    if DB_FILE.exists():
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"tools": [], "articles": [], "meta": {"last_run": None, "tool_count": 0, "article_count": 0}}


def save_db(db):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)


def ensure_dirs():
    TOOLS_DIR.mkdir(parents=True, exist_ok=True)
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)


def build_tool_html(name, category, tool_id):
    """Build a real functional tool HTML page."""
    slug = f"tool-{tool_id}"
    ad = f'<a href="{AD_LINK}" target="_blank" rel="nofollow noopener" style="color:#f59e0b;font-weight:700;">Discover Premium Tools & Exclusive Deals</a>'
    
    # Determine tool type based on name
    lower_name = name.lower()
    
    if "json" in lower_name:
        content = build_json_tool(name)
    elif "base64" in lower_name:
        content = build_base64_tool(name)
    elif "password" in lower_name:
        content = build_password_tool(name)
    elif "color" in lower_name:
        content = build_color_tool(name)
    elif "unit" in lower_name or "converter" in lower_name:
        content = build_converter_tool(name)
    elif "word" in lower_name and "counter" in lower_name:
        content = build_word_counter_tool(name)
    elif "qr" in lower_name:
        content = build_qr_tool(name)
    elif "hash" in lower_name or "md5" in lower_name or "sha" in lower_name:
        content = build_hash_tool(name)
    elif "calculator" in lower_name or "calc" in lower_name:
        content = build_calculator_tool(name)
    else:
        content = build_generic_tool(name)
    
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} — Free Online Tool</title>
<meta name="description" content="Free online {name.lower()} tool. No signup required. Works 100% in your browser.">
<style>
:root{{--bg:#0b1120;--surface:#151e32;--primary:#38bdf8;--accent:#f59e0b;--text:#f1f5f9;--muted:#94a3b8;--border:#334155;--radius:12px}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--text);line-height:1.7;padding:20px;min-height:100vh}}
.container{{max-width:900px;margin:0 auto}}
h1{{color:var(--primary);font-size:1.8rem;margin-bottom:10px}}
.badge{{display:inline-block;background:rgba(56,189,248,0.1);color:var(--primary);padding:4px 12px;border-radius:20px;font-size:0.8rem;font-weight:700;margin-bottom:20px;border:1px solid rgba(56,189,248,0.2);text-transform:uppercase}}
.card{{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:24px;margin-bottom:20px}}
input,textarea,select{{background:#0f172a;color:var(--text);border:1px solid var(--border);padding:12px 16px;border-radius:8px;font-family:inherit;font-size:1rem;width:100%;margin-bottom:12px}}
input:focus,textarea:focus,select:focus{{outline:none;border-color:var(--primary);box-shadow:0 0 0 3px rgba(56,189,248,0.15)}}
.btn{{background:var(--primary);color:#0f172a;border:none;padding:12px 28px;border-radius:8px;cursor:pointer;font-weight:700;font-size:1rem;transition:all .2s;display:inline-flex;align-items:center;gap:6px;margin:4px}}
.btn:hover{{background:#0ea5e9;transform:translateY(-1px)}}
.btn-secondary{{background:var(--surface);color:var(--text);border:1px solid var(--border)}}
.btn-secondary:hover{{background:#1e293b}}
.output{{background:#0f172a;border:1px solid var(--border);border-radius:8px;padding:16px;margin-top:16px;white-space:pre-wrap;font-family:monospace;font-size:0.95rem;min-height:80px;word-break:break-all;overflow-x:auto}}
.toolbar{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:16px}}
.ad{{background:linear-gradient(135deg,#1e293b,#334155);border:1px solid var(--border);border-radius:var(--radius);padding:24px;text-align:center;margin:30px 0;position:relative}}
.ad::after{{content:'AD';position:absolute;top:8px;left:12px;background:rgba(245,158,11,0.15);color:var(--accent);padding:2px 8px;border-radius:4px;font-size:0.65rem;font-weight:700}}
.ad a{{color:var(--accent);text-decoration:none;font-weight:700;font-size:1.05rem}}
.ad a:hover{{text-decoration:underline}}
.back{{display:inline-flex;align-items:center;gap:6px;color:var(--muted);text-decoration:none;margin-top:20px;transition:color .2s}}
.back:hover{{color:var(--primary)}}
.grid-2{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
@media(max-width:640px){{.grid-2{{grid-template-columns:1fr}}h1{{font-size:1.4rem}}}}
</style>
</head>
<body>
<div class="container">
<span class="badge">{category}</span>
<h1>{name}</h1>
<div class="card">
{content}
</div>
<div class="ad">
<p>🚀 Discover more free tools & exclusive offers</p>
{ad}
</div>
<a href="../index.html" class="back">← Back to Home</a>
</div>
</body>
</html>'''
    return html, slug


def build_json_tool(name):
    return '''<div class="toolbar">
<button class="btn" onclick="fmt()">Pretty Print</button>
<button class="btn btn-secondary" onclick="min()">Minify</button>
<button class="btn btn-secondary" onclick="val()">Validate</button>
<button class="btn btn-secondary" onclick="cpy()">Copy</button>
</div>
<textarea id="in" rows="8" placeholder="Paste your JSON here..."></textarea>
<div id="out" class="output">Result will appear here...</div>
<script>
function fmt(){try{var o=JSON.parse(document.getElementById('in').value);document.getElementById('out').textContent=JSON.stringify(o,null,2);document.getElementById('out').style.color='var(--text)';}catch(e){document.getElementById('out').textContent='Error: '+e.message;document.getElementById('out').style.color='#ef4444';}}
function min(){try{var o=JSON.parse(document.getElementById('in').value);document.getElementById('out').textContent=JSON.stringify(o);document.getElementById('out').style.color='var(--text)';}catch(e){document.getElementById('out').textContent='Error: '+e.message;document.getElementById('out').style.color='#ef4444';}}
function val(){try{JSON.parse(document.getElementById('in').value);document.getElementById('out').textContent='Valid JSON ✓';document.getElementById('out').style.color='#10b981';}catch(e){document.getElementById('out').textContent='Error: '+e.message;document.getElementById('out').style.color='#ef4444';}}
function cpy(){navigator.clipboard.writeText(document.getElementById('out').textContent).then(()=>alert('Copied!'));}
</script>'''


def build_base64_tool(name):
    return '''<div class="toolbar">
<button class="btn" onclick="enc()">Encode</button>
<button class="btn btn-secondary" onclick="dec()">Decode</button>
<button class="btn btn-secondary" onclick="cpy()">Copy</button>
</div>
<textarea id="in" rows="6" placeholder="Enter text or Base64..."></textarea>
<div id="out" class="output">Result will appear here...</div>
<script>
function enc(){var t=document.getElementById('in').value;try{document.getElementById('out').textContent=btoa(unescape(encodeURIComponent(t)));document.getElementById('out').style.color='var(--text)';}catch(e){document.getElementById('out').textContent='Error: '+e.message;document.getElementById('out').style.color='#ef4444';}}
function dec(){var t=document.getElementById('in').value;try{document.getElementById('out').textContent=decodeURIComponent(escape(atob(t)));document.getElementById('out').style.color='var(--text)';}catch(e){document.getElementById('out').textContent='Error: '+e.message;document.getElementById('out').style.color='#ef4444';}}
function cpy(){navigator.clipboard.writeText(document.getElementById('out').textContent).then(()=>alert('Copied!'));}
</script>'''


def build_password_tool(name):
    return '''<div class="grid-2" style="margin-bottom:16px">
<div><label style="color:var(--muted);font-size:0.85rem">Length</label><input type="number" id="len" value="16" min="4" max="64"></div>
<div><label style="color:var(--muted);font-size:0.85rem">Options</label>
<div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:8px">
<label style="display:flex;align-items:center;gap:4px;color:var(--muted);font-size:0.9rem"><input type="checkbox" id="up" checked style="width:auto"> A-Z</label>
<label style="display:flex;align-items:center;gap:4px;color:var(--muted);font-size:0.9rem"><input type="checkbox" id="lo" checked style="width:auto"> a-z</label>
<label style="display:flex;align-items:center;gap:4px;color:var(--muted);font-size:0.9rem"><input type="checkbox" id="nu" checked style="width:auto"> 0-9</label>
<label style="display:flex;align-items:center;gap:4px;color:var(--muted);font-size:0.9rem"><input type="checkbox" id="sy" checked style="width:auto"> !@#</label>
</div></div></div>
<button class="btn" onclick="gen()">Generate Password</button>
<div id="out" class="output" style="font-size:1.3rem;text-align:center;word-break:break-all;margin-top:16px">Click Generate to create a password</div>
<div id="str" style="margin-top:10px;padding:8px;border-radius:6px;text-align:center;font-weight:700"></div>
<script>
function gen(){var l=parseInt(document.getElementById('len').value);var u=document.getElementById('up').checked,lo=document.getElementById('lo').checked,n=document.getElementById('nu').checked,s=document.getElementById('sy').checked;var c='';if(u)c+='ABCDEFGHIJKLMNOPQRSTUVWXYZ';if(lo)c+='abcdefghijklmnopqrstuvwxyz';if(n)c+='0123456789';if(s)c+='!@#$%^&*()_+-=[]{}|;:,.<>?';if(!c){alert('Select at least one type');return;}var p='';for(var i=0;i<l;i++)p+=c.charAt(Math.floor(Math.random()*c.length));document.getElementById('out').textContent=p;navigator.clipboard.writeText(p);var sc=0;if(l>=12)sc++;if(l>=16)sc++;if(u&&lo)sc++;if(n)sc++;if(s)sc++;var lbl=['Very Weak','Weak','Medium','Strong','Very Strong','Excellent'];var col=['#ef4444','#f97316','#eab308','#84cc16','#22c55e','#10b981'];var el=document.getElementById('str');el.textContent='Strength: '+lbl[sc];el.style.background=col[sc]+'22';el.style.color=col[sc];}
</script>'''


def build_color_tool(name):
    return '''<div class="grid-2">
<div><input id="hex" placeholder="#38bdf8" oninput="fromHex()"><label style="color:var(--muted);font-size:0.85rem">HEX</label></div>
<div><input id="rgb" placeholder="rgb(56,189,248)" oninput="fromRgb()"><label style="color:var(--muted);font-size:0.85rem">RGB</label></div>
</div>
<div id="pre" style="width:100%;height:80px;border-radius:12px;margin:16px 0;border:2px solid var(--border);background:#38bdf8"></div>
<div id="out" class="output">Enter a color value above</div>
<script>
function fromHex(){var h=document.getElementById('hex').value.trim();if(!h.match(/^#/))h='#'+h;if(!/^#[0-9A-Fa-f]{6}$/.test(h))return;var r=parseInt(h.slice(1,3),16),g=parseInt(h.slice(3,5),16),b=parseInt(h.slice(5,7),16);up(r,g,b,h);}
function fromRgb(){var m=document.getElementById('rgb').value.match(/(\\d+),\\s*(\\d+),\\s*(\\d+)/);if(!m)return;up(parseInt(m[1]),parseInt(m[2]),parseInt(m[3]));}
function up(r,g,b,hex){var h=hex||'#'+[r,g,b].map(function(x){return x.toString(16).padStart(2,'0')}).join('');document.getElementById('hex').value=h;document.getElementById('rgb').value='rgb('+r+', '+g+', '+b+')';document.getElementById('pre').style.background=h;document.getElementById('out').innerHTML='HEX: '+h+'<br>RGB: rgb('+r+', '+g+', '+b+')';}
</script>'''


def build_converter_tool(name):
    return '''<div class="grid-2">
<div><input type="number" id="val" value="1" step="any" placeholder="Value"></div>
<div>
<select id="from" style="margin-bottom:8px"><option value="m">Meter (m)</option><option value="km">Kilometer (km)</option><option value="cm">Centimeter (cm)</option><option value="ft">Foot (ft)</option><option value="in">Inch (in)</option></select>
<select id="to"><option value="km">Kilometer (km)</option><option value="m" selected>Meter (m)</option><option value="cm">Centimeter (cm)</option><option value="ft">Foot (ft)</option><option value="in">Inch (in)</option></select>
</div></div>
<button class="btn" onclick="conv()" style="margin-top:8px">Convert</button>
<div id="out" class="output">Enter a value and click Convert</div>
<script>
var rates={m:1,km:1000,cm:0.01,ft:0.3048,in:0.0254};
function conv(){var v=parseFloat(document.getElementById('val').value);var f=document.getElementById('from').value;var t=document.getElementById('to').value;if(isNaN(v)){document.getElementById('out').textContent='Please enter a valid number';return;}var res=v*rates[f]/rates[t];document.getElementById('out').textContent=v+' '+f+' = '+res.toFixed(6)+' '+t;}
</script>'''


def build_word_counter_tool(name):
    return '''<textarea id="txt" rows="8" placeholder="Type or paste your text here..." oninput="cnt()"></textarea>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:12px;margin-top:16px">
<div class="card" style="text-align:center;padding:16px"><div style="font-size:1.8rem;font-weight:700;color:var(--primary)" id="w">0</div><div style="color:var(--muted);font-size:0.85rem">Words</div></div>
<div class="card" style="text-align:center;padding:16px"><div style="font-size:1.8rem;font-weight:700;color:var(--primary)" id="c">0</div><div style="color:var(--muted);font-size:0.85rem">Chars</div></div>
<div class="card" style="text-align:center;padding:16px"><div style="font-size:1.8rem;font-weight:700;color:var(--primary)" id="s">0</div><div style="color:var(--muted);font-size:0.85rem">Sentences</div></div>
<div class="card" style="text-align:center;padding:16px"><div style="font-size:1.8rem;font-weight:700;color:var(--primary)" id="p">0</div><div style="color:var(--muted);font-size:0.85rem">Paragraphs</div></div>
</div>
<script>
function cnt(){var t=document.getElementById('txt').value;document.getElementById('c').textContent=t.length;var w=t.trim()===''?0:t.trim().split(/\\s+/).length;document.getElementById('w').textContent=w;var s=t.split(/[.!?]+/).filter(function(x){return x.trim().length>0}).length;document.getElementById('s').textContent=s;var p=t.split('\\n').filter(function(x){return x.trim().length>0}).length;document.getElementById('p').textContent=p;}
</script>'''


def build_qr_tool(name):
    return '''<input id="txt" placeholder="Enter text or URL..." value="https://example.com">
<button class="btn" onclick="make()" style="margin-top:8px">Generate QR Code</button>
<div id="qr" style="margin-top:20px;text-align:center;padding:20px;background:#fff;border-radius:12px"></div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
<script>
function make(){var t=document.getElementById('txt').value;var c=document.getElementById('qr');c.innerHTML='';new QRCode(c,{text:t,width:200,height:200,colorDark:'#000',colorLight:'#fff',correctLevel:QRCode.CorrectLevel.H});}
</script>'''


def build_hash_tool(name):
    return '''<div class="toolbar">
<button class="btn" onclick="md5()">MD5</button>
<button class="btn btn-secondary" onclick="sha1()">SHA1</button>
<button class="btn btn-secondary" onclick="sha256()">SHA256</button>
</div>
<textarea id="in" rows="5" placeholder="Enter text to hash..."></textarea>
<div id="out" class="output">Result will appear here...</div>
<script>
async function md5(){var t=document.getElementById('in').value;var b=new TextEncoder().encode(t);var h=await crypto.subtle.digest('MD5',b);document.getElementById('out').textContent=Array.from(new Uint8Array(h)).map(function(x){return x.toString(16).padStart(2,'0')}).join('');}
async function sha1(){var t=document.getElementById('in').value;var b=new TextEncoder().encode(t);var h=await crypto.subtle.digest('SHA-1',b);document.getElementById('out').textContent=Array.from(new Uint8Array(h)).map(function(x){return x.toString(16).padStart(2,'0')}).join('');}
async function sha256(){var t=document.getElementById('in').value;var b=new TextEncoder().encode(t);var h=await crypto.subtle.digest('SHA-256',b);document.getElementById('out').textContent=Array.from(new Uint8Array(h)).map(function(x){return x.toString(16).padStart(2,'0')}).join('');}
</script>'''


def build_calculator_tool(name):
    return '''<div class="grid-2">
<div><input type="number" id="a" placeholder="First number"></div>
<div><input type="number" id="b" placeholder="Second number"></div>
</div>
<div class="toolbar">
<button class="btn" onclick="calc('+')">+</button>
<button class="btn btn-secondary" onclick="calc('-')">−</button>
<button class="btn btn-secondary" onclick="calc('*')">×</button>
<button class="btn btn-secondary" onclick="calc('/')">÷</button>
</div>
<div id="out" class="output">Enter numbers and select operation</div>
<script>
function calc(op){var a=parseFloat(document.getElementById('a').value);var b=parseFloat(document.getElementById('b').value);if(isNaN(a)||isNaN(b)){document.getElementById('out').textContent='Enter valid numbers';return;}var r;switch(op){case '+':r=a+b;break;case '-':r=a-b;break;case '*':r=a*b;break;case '/':r=b===0?'Cannot divide by zero':a/b;break;}document.getElementById('out').textContent='Result: '+r;}
</script>'''


def build_generic_tool(name):
    return '''<div class="toolbar">
<button class="btn" onclick="go()">Process</button>
<button class="btn btn-secondary" onclick="cpy()">Copy Result</button>
</div>
<textarea id="in" rows="6" placeholder="Enter your input here..."></textarea>
<div id="out" class="output">Click Process to see the result</div>
<script>
function go(){var t=document.getElementById('in').value;document.getElementById('out').textContent='Processed: '+t.length+' characters\\nFirst 100 chars: '+t.substring(0,100);}
function cpy(){navigator.clipboard.writeText(document.getElementById('out').textContent).then(()=>alert('Copied!'));}
</script>'''


def build_article_html(article_id, lang):
    """Build a real article HTML page."""
    is_ar = lang == 'ar'
    templates = AR_TEMPLATES if is_ar else EN_TEMPLATES
    template = random.choice(templates)
    year = datetime.now().year
    
    count = random.choice([5, 7, 10, 12, 15])
    task = random.choice(TASKS)
    domain = random.choice(DOMAINS)
    topic = random.choice(AR_TOPICS if is_ar else EN_TOPICS)
    tool_type = random.choice(TOOL_TYPES)
    professional = random.choice(PROFESSIONALS)
    feature = random.choice(FEATURES)
    concept = random.choice(CONCEPTS)
    strategy = random.choice(STRATEGIES)
    percent = random.choice(PERCENTS)
    saving = random.choice(SAVINGS)
    
    title = template["title"].format(count=count, task=task, year=year, topic=topic, tool_type=tool_type, domain=domain)
    body = template["body"].format(count=count, task=task, year=year, topic=topic, tool_type=tool_type, domain=domain, professional=professional, feature=feature, concept=concept, strategy=strategy, percent=percent, saving=saving)
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = f"article-{article_id}"
    
    ad = f'<a href="{AD_LINK}" target="_blank" rel="nofollow noopener" style="color:#f59e0b;font-weight:700;">Discover Premium Tools & Exclusive Deals</a>'
    
    html = f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{body[:120]}...">
<style>
:root{{--bg:#0b1120;--surface:#151e32;--primary:#38bdf8;--accent:#f59e0b;--text:#f1f5f9;--muted:#94a3b8;--border:#334155;--radius:12px}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--text);line-height:1.7;padding:20px;min-height:100vh}}
.container{{max-width:800px;margin:0 auto}}
h1{{color:var(--primary);font-size:1.6rem;margin-bottom:10px;line-height:1.3}}
.meta{{color:var(--muted);font-size:0.9rem;margin-bottom:24px}}
.content{{font-size:1.05rem;line-height:1.8}}
.content p{{margin-bottom:16px}}
.ad{{background:linear-gradient(135deg,#1e293b,#334155);border:1px solid var(--border);border-radius:var(--radius);padding:24px;text-align:center;margin:30px 0}}
.ad a{{color:var(--accent);text-decoration:none;font-weight:700;font-size:1.05rem}}
.ad a:hover{{text-decoration:underline}}
.back{{display:inline-flex;align-items:center;gap:6px;color:var(--muted);text-decoration:none;margin-top:20px;transition:color .2s}}
.back:hover{{color:var(--primary)}}
</style>
</head>
<body>
<div class="container">
<h1>{title}</h1>
<div class="meta">📅 {date_str} | 🏷️ {domain} | 📝 {topic}</div>
<div class="content">
<p>{body}</p>
<p>🚀 <strong>Recommended:</strong> Try our free {tool_type} tools to boost your productivity today!</p>
</div>
<div class="ad">
<p>💡 Discover more free tools & exclusive offers</p>
{ad}
</div>
<a href="../index.html" class="back">← Back to Home</a>
</div>
</body>
</html>'''
    
    return {
        "id": article_id,
        "slug": slug,
        "title": title,
        "date": date_str,
        "category": domain,
        "topic": topic,
        "content": body,
        "html": html
    }


def generate_tools(db):
    """Generate new tools up to MAX_TOOLS."""
    current_count = len(db["tools"])
    if current_count >= MAX_TOOLS:
        print(f"✅ Reached {MAX_TOOLS} tools. Stopping tool generation.")
        return 0
    
    to_generate = min(TOOLS_PER_CYCLE, MAX_TOOLS - current_count)
    generated = 0
    
    for i in range(to_generate):
        tool_id = current_count + i + 1
        name = random.choice(TOOL_NAMES)
        category = random.choice(CATEGORIES)
        
        # Make name unique if needed
        existing_names = {t["name"] for t in db["tools"]}
        if name in existing_names:
            name = f"{name} Pro"
        
        html, slug = build_tool_html(name, category, tool_id)
        
        # Write HTML file
        tool_path = TOOLS_DIR / f"{slug}.html"
        with open(tool_path, "w", encoding="utf-8") as f:
            f.write(html)
        
        # Add to DB
        db["tools"].append({
            "id": tool_id,
            "slug": slug,
            "name": name,
            "category": category,
            "description": f"Free online {name.lower()}. No signup required. Works 100% in your browser.",
            "html": html
        })
        
        generated += 1
        print(f"  + Tool {tool_id}: {name}")
    
    return generated


def generate_articles(db):
    """Generate articles continuously."""
    current_count = len(db["articles"])
    generated = 0
    
    for i in range(ARTICLES_PER_CYCLE):
        article_id = current_count + i + 1
        lang = 'ar' if i % 2 == 0 else 'en'
        
        article = build_article_html(article_id, lang)
        
        # Write HTML file
        article_path = ARTICLES_DIR / f"{article['slug']}.html"
        with open(article_path, "w", encoding="utf-8") as f:
            f.write(article["html"])
        
        # Add to DB
        db["articles"].append(article)
        
        generated += 1
        print(f"  + Article {article_id}: {article['title'][:50]}...")
    
    return generated


def main():
    print("=" * 50)
    print("🚀 Empire Web Engine v4 — Starting...")
    print("=" * 50)
    
    ensure_dirs()
    db = load_db()
    
    # Generate tools
    print(f"\n🔧 Tools: {len(db['tools'])}/{MAX_TOOLS}")
    tools_generated = generate_tools(db)
    
    # Generate articles (always)
    print(f"\n📝 Articles: {len(db['articles'])}")
    articles_generated = generate_articles(db)
    
    # Update meta
    db["meta"] = {
        "last_run": datetime.now().isoformat(),
        "tool_count": len(db["tools"]),
        "article_count": len(db["articles"])
    }
    
    # Save DB
    save_db(db)
    
    print(f"\n{'=' * 50}")
    print(f"✅ Done!")
    print(f"   Tools: +{tools_generated} (total: {len(db['tools'])})")
    print(f"   Articles: +{articles_generated} (total: {len(db['articles'])})")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    main()
