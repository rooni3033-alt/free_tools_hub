#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Empire Web Engine - Mega Utility & Content Hub
Generates 500 tools (then stops) + infinite articles
Updates database.json every cycle
"""

import json
import os
import random
import textwrap
from datetime import datetime
from pathlib import Path

# ===================== CONFIG =====================
TOOLS_DIR = Path("./tools")
ARTICLES_DIR = Path("./articles")
DB_FILE = Path("./database.json")
MAX_TOOLS = 500
TOOLS_PER_CYCLE = 5
ARTICLES_PER_CYCLE = 2
AD_LINK = "https://omg10.com/4/11349784"

# ===================== DATA POOLS =====================
TOOL_CATEGORIES = [
    "Developer", "Designer", "SEO", "Security", "Productivity",
    "Converter", "Calculator", "Analyzer", "Generator", "Formatter",
    "Tester", "Monitor", "Optimizer", "Cleaner", "Tracker"
]

TOOL_PREFIXES = [
    "Smart", "Pro", "Ultra", "Mega", "Quick", "Auto", "Easy", "Super",
    "Fast", "Instant", "Advanced", "Dynamic", "Global", "Prime", "Elite"
]

TOOL_NAMES = [
    "JSON Formatter", "Base64 Encoder", "Password Generator", "Color Picker",
    "CSS Minifier", "Markdown Editor", "Regex Tester", "QR Code Generator",
    "URL Shortener", "Image Compressor", "PDF Merger", "Word Counter",
    "Lorem Ipsum Generator", "Diff Checker", "Code Beautifier", "HTML Encoder",
    "JWT Decoder", "Hash Generator", "IP Lookup", "SSL Checker", "DNS Lookup",
    "Whois Lookup", "Website Speed Test", "Meta Tag Analyzer", "Sitemap Generator",
    " robots.txt Generator", "Favicon Generator", "Gradient Generator",
    "Box Shadow Generator", "Flexbox Generator", "Grid Generator", "SVG Optimizer",
    "PNG to JPG", "WebP Converter", "Image to Base64", "Base64 to Image",
    "CSV to JSON", "JSON to CSV", "XML to JSON", "YAML to JSON", "SQL Formatter",
    "Cron Expression Generator", "Timestamp Converter", "Unit Converter",
    "Currency Converter", "Loan Calculator", "Percentage Calculator", "Age Calculator",
    "BMI Calculator", "Calorie Calculator", "Password Strength Checker",
    "Username Generator", "Domain Name Generator", "Logo Maker", "Icon Generator",
    "Favicon Generator", "Palette Generator", "Font Pairing", "Mockup Generator",
    "Screenshot Tool", "Screen Recorder", "Voice Recorder", "Text to Speech",
    "Speech to Text", "Translator", "Grammar Checker", "Plagiarism Checker",
    "Readability Score", "Keyword Density", "Backlink Checker", "SERP Simulator",
    "Page Authority Checker", "Domain Authority Checker", "Moz Rank Checker",
    "Alexa Rank Checker", "Social Counter", "Share Link Generator", "UTM Builder",
    "Email Validator", "Email Extractor", "Bulk Email Checker", "SMTP Tester",
    "Port Scanner", "Ping Tool", "Traceroute", "Subnet Calculator", "MAC Lookup",
    "Browser Info", "Screen Resolution", "What is My IP", "User Agent Parser",
    "HTTP Headers", "Redirect Checker", "Link Extractor", "Broken Link Checker",
    "Page Size Checker", "Source Code Viewer", "Website Snapshot", "Mobile Emulator",
    "Responsive Tester", "PageSpeed Insights", "Core Web Vitals", "AMP Validator",
    "Structured Data Test", "Rich Snippet Test", "Hreflang Checker", "Canonical Checker",
    "Open Graph Checker", "Twitter Card Validator", "Pinterest Rich Pins",
    "Instagram Downloader", "YouTube Thumbnail", "TikTok Downloader", "Twitter Video",
    "Facebook Video", "LinkedIn Post Maker", "Instagram Post Maker", "Story Maker",
    "Meme Generator", "GIF Maker", "Video Trimmer", "Audio Cutter", "MP3 Converter",
    "Video to GIF", "GIF to Video", "Subtitle Generator", "Transcript Generator",
    "Podcast Maker", "Audio Joiner", "Voice Changer", "Noise Reducer", "Beat Maker",
    "Invoice Generator", "Receipt Maker", "Quote Generator", "Proposal Maker",
    "Contract Generator", "NDA Generator", "Resume Builder", "CV Maker",
    "Portfolio Builder", "Business Card Maker", "Letterhead Maker", "Signature Maker",
    "Barcode Generator", "QR Scanner", "ISBN Lookup", "Credit Card Validator",
    "IBAN Checker", "SWIFT/BIC Lookup", "Tax Calculator", "VAT Calculator",
    "Tip Calculator", "Split Bill", "Expense Tracker", "Budget Planner",
    "Investment Calculator", "Compound Interest", "Retirement Calculator",
    "Mortgage Calculator", "Rent vs Buy", "Car Loan Calculator", "Fuel Cost Calculator",
    "Trip Cost Calculator", "Time Zone Converter", "World Clock", "Meeting Planner",
    "Countdown Timer", "Stopwatch", "Pomodoro Timer", "Focus Timer", "Habit Tracker",
    "To-Do List", "Kanban Board", "Gantt Chart", "Mind Map Maker", "Flowchart Maker",
    "Wireframe Tool", "Prototype Tool", "Mockup Tool", "Sitemap Maker", "User Persona",
    "Journey Map", "Competitor Analyzer", "SWOT Analysis", "PEST Analysis",
    "Business Model Canvas", "Value Proposition", "Elevator Pitch", "Pitch Deck Maker",
    "Financial Model", "Cash Flow Projection", "Break-Even Analysis", "ROI Calculator",
    "A/B Test Calculator", "Statistical Significance", "Sample Size Calculator",
    "Confidence Interval", "Standard Deviation", "Variance Calculator", "Z-Score",
    "T-Test Calculator", "Chi-Square Test", "Correlation Calculator", "Regression",
    "Data Visualizer", "Chart Maker", "Graph Plotter", "Pie Chart Maker", "Bar Chart",
    "Line Chart", "Scatter Plot", "Histogram Maker", "Box Plot", "Heat Map",
    "Tree Map", "Sankey Diagram", "Radar Chart", "Bubble Chart", "Candlestick",
    "Network Graph", "Org Chart Maker", "Family Tree", "Timeline Maker", "Roadmap",
    "Release Notes", "Changelog Generator", "Version Comparator", "Git Command Builder",
    "Dockerfile Generator", "Docker Compose", "Kubernetes YAML", "Terraform Generator",
    "CloudFormation", "Serverless Template", "API Endpoint Maker", "Webhook Tester",
    "GraphQL Builder", "REST Client", "SOAP Client", "gRPC Tester", "Postman Collection",
    "OpenAPI Generator", "Swagger UI", "API Documentation", "SDK Generator",
    "Code Linter", "Code Formatter", "Static Analysis", "Dependency Checker",
    "Vulnerability Scanner", "License Checker", "Code Coverage", "Benchmark Tool",
    "Profiler", "Debugger", "Log Analyzer", "Error Tracker", "Crash Reporter",
    "Performance Monitor", "Uptime Monitor", "Status Page", "Incident Manager",
    "Alert Manager", "On-Call Scheduler", "Runbook Generator", "Playbook Maker",
    "Wiki Generator", "Knowledge Base", "FAQ Generator", "Help Center", "Chatbot Builder",
    "Live Chat", "Ticket System", "Feedback Form", "Survey Maker", "Poll Maker",
    "Quiz Maker", "Exam Generator", "Certificate Maker", "Badge Generator",
    "Leaderboard", "Gamification", "Loyalty Program", "Referral Generator",
    "Affiliate Link", "Coupon Generator", "Discount Calculator", "Price Comparator",
    "Shipping Calculator", "Tracking Number", "Label Maker", "Packing List",
    "Inventory Manager", "Stock Tracker", "Reorder Point", "EOQ Calculator",
    "Safety Stock", "Lead Time Calculator", "Supplier Scorecard", "RFQ Generator",
    "Purchase Order", "GRN Maker", "Bill of Materials", "Work Order", "Job Card",
    "Timesheet", "Attendance Tracker", "Leave Manager", "Payroll Calculator",
    "Payslip Generator", "Tax Form Generator", "W-2 Maker", "1099 Generator",
    "Invoice Tracker", "Payment Reminder", "Receipt Scanner", "Expense Report",
    "Mileage Log", "Per Diem Calculator", "Reimbursement Form", "Petty Cash",
    "Budget vs Actual", "Forecasting Tool", "Scenario Planner", "What-If Analysis",
    "Monte Carlo", "Risk Matrix", "Decision Tree", "Priority Matrix", "Eisenhower",
    "Pareto Analysis", "Fishbone Diagram", "5 Whys", "Root Cause Analysis",
    "FMEA Calculator", "Control Chart", "Capability Index", "Six Sigma Calculator",
    "Lean Canvas", "Value Stream Map", "Kaizen Board", "5S Audit", "Gemba Walk",
    "Standard Work", "Work Instruction", "SOP Generator", "Checklist Maker",
    "Inspection Form", "Audit Report", "Non-Conformance", "CAPA Tracker",
    "Document Control", "Change Request", "ECN Generator", "Drawing Comparator",
    "BOM Comparator", "Revision Tracker", "ECO Manager", "PLM Connector",
    "CAD Viewer", "STEP Converter", "STL Viewer", "Mesh Repair", "3D Print Slicer",
    "G-Code Simulator", "CNC Calculator", "Feed Rate", "Spindle Speed", "Cutting Time",
    "Tool Life", "Wear Calculator", "Tolerance Stack", "GD&T Symbol", "Datum Reference",
    "Surface Finish", "Hardness Converter", "Material Selector", "Weight Calculator",
    "Center of Gravity", "Moment of Inertia", "Stress Analysis", "Deflection Calculator",
    "Beam Calculator", "Column Calculator", "Truss Analysis", "Frame Analysis",
    "Plate Calculator", "Shell Analysis", "Buckling Check", "Fatigue Life",
    "Fracture Mechanics", "Creep Calculator", "Thermal Expansion", "Heat Transfer",
    "Fluid Flow", "Pipe Sizer", "Pump Selector", "Valve Sizing", "Orifice Calculator",
    "Venturi Meter", "Manometer", "Reynolds Number", "Nusselt Number", "Prandtl Number",
    "Moody Chart", "Darcy-Weisbach", "Hazen-Williams", "Colebrook-White", "Fanning",
    "Compressor Power", "Turbine Efficiency", "Heat Exchanger", "Cooling Tower",
    "Boiler Efficiency", "Furnace Sizing", "HVAC Load", "Psychrometric Chart",
    "Refrigeration Cycle", "Absorption Chiller", "Heat Pump COP", "Solar Panel Sizer",
    "Wind Turbine", "Battery Bank", "Inverter Selector", "Charge Controller",
    "Cable Sizer", "Voltage Drop", "Short Circuit", "Arc Flash", "Grounding",
    "Lightning Protection", "Surge Arrester", "Transformer Sizing", "Motor Starter",
    "VFD Selector", "Soft Starter", "Power Factor", "Harmonic Filter", "UPS Sizer",
    "Generator Sizing", "Load Bank", "Energy Audit", "Power Quality", "Smart Meter",
    "Substation Design", "Protection Relay", "SCADA Simulator", "PLC Programmer",
    "HMI Designer", "DCS Configurator", "RTU Programmer", "Modbus Scanner",
    "OPC Client", "MQTT Broker", "LoRa Calculator", "Zigbee Network", "Bluetooth Range",
    "WiFi Planner", "5G Coverage", "Satellite Link", "Fiber Optic", "DWDM Calculator",
    "OTDR Trace", "Splice Loss", "Connector Loss", "Attenuation", "Bandwidth",
    "Latency Calculator", "Jitter", "Packet Loss", "Throughput", "QoS Calculator",
    "MPLS Design", "VPN Tunnel", "Firewall Rule", "ACL Generator", "NAT Table",
    "Load Balancer", "Reverse Proxy", "CDN Optimizer", "Cache Warmer", "Edge Node",
    "Origin Shield", "DDoS Mitigator", "WAF Rule", "Bot Detector", "Captcha Maker",
    "Rate Limiter", "Circuit Breaker", "Retry Policy", "Timeout Calculator",
    "Health Check", "Canary Deploy", "Blue-Green", "Rolling Update", "Feature Flag",
    "A/B Router", "Multivariate", "Funnel Analyzer", "Cohort Analysis", "Retention",
    "Churn Predictor", "LTV Calculator", "CAC Calculator", "NPS Calculator", "CSAT",
    "CES Score", "VOC Analyzer", "Sentiment Analysis", "Topic Modeling", "NER Tagger",
    "POS Tagger", "Dependency Parser", "Constituency", "Semantic Role", "Coreference",
    "Text Summarizer", "Keyword Extractor", "Entity Linker", "Relation Extractor",
    "Event Extractor", "Temporal Parser", "Spatial Parser", "Intent Classifier",
    "Slot Filler", "Dialogue Manager", "Response Generator", "Paraphrase Generator",
    "Question Generator", "Answer Generator", "Fact Checker", "Claim Verifier",
    "Evidence Retriever", "Argument Mapper", "Fallacy Detector", "Bias Checker",
    "Toxicity Filter", "Hate Speech", "Misinformation", "Deepfake Detector",
    "Image Classifier", "Object Detector", "Segmentation", "Face Detector",
    "OCR Engine", "Document Parser", "Table Extractor", "Form Recognizer",
    "Receipt Parser", "Invoice OCR", "ID Scanner", "Passport Reader", "Barcode OCR",
    "Handwriting", "Signature Verify", "Fingerprint Match", "Iris Scanner",
    "Voice Biometric", "Speaker ID", "Language ID", "Accent Detector", "Emotion Recognizer",
    "Age Estimator", "Gender Classifier", "Ethnicity", "Attractiveness", "Similarity",
    "Style Transfer", "Super Resolution", "Denoising", "Inpainting", "Colorization",
    "Sketch to Photo", "Photo to Sketch", "Cartoonizer", "Anime Maker", "Avatar Generator",
    "Face Swap", "Lip Sync", "Deep Nostalgia", "Motion Capture", "Pose Estimator",
    "Gesture Recognizer", "Sign Language", "Body Measurement", "Virtual Try-On",
    "Room Planner", "Furniture Arranger", "Color Matcher", "Paint Calculator",
    "Tile Calculator", "Flooring Estimator", "Roofing Calculator", "Siding Calculator",
    "Drywall Estimator", "Insulation Calculator", "HVAC Duct Sizer", "Airflow Balancer",
    "Refrigerant Charge", "Combustion Analysis", "Carbon Footprint", "Water Footprint",
    "Waste Calculator", "Recycling Sorter", "Composting Guide", "Solar Angle",
    "Shading Analysis", "Daylighting", "Glare Calculator", "Thermal Comfort",
    "Indoor Air Quality", "Ventilation Rate", "Filtration Efficiency", "MERV Rating",
    "HEPA Calculator", "UV Dose", "Ozone Generator", "Ionizer", "Humidifier Sizer",
    "Dehumidifier", "Air Purifier", "Water Filter", "Reverse Osmosis", "Softener",
    "Distillation", "Chlorination", "UV Sterilization", "Ozonation", "pH Calculator",
    "Alkalinity", "Hardness", "TDS Meter", "Conductivity", "Salinity", "Chlorine",
    "Bromine", "Cyanuric Acid", "Calcium Hardness", "Stabilizer", "Shock Treatment",
    "Algaecide", "Clarifier", "Flocculant", "Enzyme", "Phosphate Remover",
    "Metal Sequestrant", "Stain Preventer", "Scale Inhibitor", "Corrosion Inhibitor",
    "Biocide", "Dispersant", "Antifoam", "Defoamer", "Emulsifier", "Surfactant",
    "Solvent", "Thinner", "Reducer", "Catalyst", "Accelerator", "Inhibitor",
    "Promoter", "Initiator", "Crosslinker", "Curing Agent", "Hardener", "Plasticizer",
    "Stabilizer", "Antioxidant", "UV Absorber", "Flame Retardant", "Foaming Agent",
    "Blowing Agent", "Nucleating Agent", "Clarifier", "Optical Brightener", "Pigment",
    "Dye", "Lake", "Toner", "Extender", "Filler", "Reinforcement", "Nanocomposite",
    "Masterbatch", "Compound", "Alloy", "Blend", "Copolymer", "Terpolymer", "Elastomer",
    "Thermoset", "Thermoplastic", "Composite", "Ceramic", "Glass", "Metal", "Polymer",
    "Semiconductor", "Superconductor", "Ferroelectric", "Piezoelectric", "Pyroelectric",
    "Magnetostrictive", "Shape Memory", "Electroactive", "Photonic", "Phononic",
    "Metamaterial", "Plasmonic", "Spintronic", "Quantum Dot", "Graphene", "Carbon Nanotube",
    "Fullerene", "Diamond", "Graphite", "Charcoal", "Activated Carbon", "Biochar",
    "Compost", "Vermicompost", "Manure", "Fertilizer", "Pesticide", "Herbicide",
    "Fungicide", "Nematicide", "Molluscicide", "Rodenticide", "Avicide", "Piscicide",
    "Insect Growth Regulator", "Pheromone", "Attractant", "Repellent", "Antifeedant",
    "Chemosterilant", "Microbial", "Biological", "Botanical", "Mineral", "Organic",
    "Synthetic", "Neonicotinoid", "Pyrethroid", "Organophosphate", "Carbamate",
    "Glyphosate", "Paraquat", "Atrazine", "2,4-D", "Dicamba", "Chlorpyrifos",
    "Malathion", "Diazinon", "Dimethoate", "Methomyl", "Carbaryl", "Methiocarb",
    "Metaldehyde", "Methoprene", "Hydroprene", "Kinoprene", "Fenoxycarb", "Pyriproxyfen",
    "Diflubenzuron", "Teflubenzuron", "Novaluron", "Lufenuron", "Hexaflumuron",
    "Chitin Synthesis", "Juvenile Hormone", "Ecdysone", "Molting Accelerator",
    "Prothoracicotropic", "Allatostatin", "Allatotropin", "Tachykinin", "FMRFamide",
    "Proctolin", "Sulfakinin", "Corazonin", "Crustacean Cardioactive", "Ecdysis",
    "Bursicon", "ETH", "CCAP", "EH", "IVP", "PBAN", "DH", "AKH", "DILP", "IIS",
    "TOR", "AMPK", "Sirtuin", "FOXO", "HNF4", "HR96", "ERR", "PPAR", "RXR",
    "EcR", "USP", "FTZ-F1", "HR3", "HR4", "E75", "E78", "BR-C", "E93", "FTZ",
    "KNI", "KR", "HB", "GT", "BCD", "CAD", "TLL", "HKB", "KNI", "KR", "KNRL",
    "EGON", "SLO", "SNA", "EVE", "RUN", "FUSHI TARAZU", "ENGRAILED", "INVECTED",
    "WINGLESS", "PATCHED", "SMOOTHENED", "CUBITUS INTERRUPTUS", "DECAPENTAPLEGIC",
    "THICK VEINS", "MAD", "MEDEA", "SCHNURRI", "Daughters Against", "Dad", "Dpp",
    "Gbb", "Screw", "Activin", "Myo", "Mst", "Gdf", "Bmp", "Tgf", "Nodal", "Lefty",
    "Vg1", "Derriere", "Xnr", "Coco", "Cerberus", "Chordin", "Noggin", "Follistatin",
    "Gremlin", "DAN", "Sost", "Wise", "Twisted Gastrulation", "BAMBI", "USAG1",
    "RGM", "DRAGON", "HEMOJUVELIN", "NEOGENIN", "DCC", "UNC5", "ROBO", "SLIT",
    "NETRIN", "DCC", "NEO", "UNC5", "DAM", "RGM", "BMP", "WNT", "SHH", "HH",
    "IHH", "DHH", "PTCH", "PTCH2", "SMO", "SUFU", "GLI", "KIF7", "GAS1", "CDON",
    "BOC", "LRP", "FZD", "DVL", "AXIN", "APC", "GSK3B", "CK1", "Beta-Catenin",
    "TCF", "LEF", "SFRP", "DKK", "WIF", "RSPO", "ZNRF3", "RNF43", "LGR", "ROR",
    "RYK", "MUSK", "FRY", "VANGL", "SCRB", "DLG", "LLGL", "PKC", "CDC42", "RAC",
    "RHO", "ROCK", "MLC", "PAK", "PIX", "GIT", "NCK", "WASp", "WAVE", "ARP",
    "Cortactin", "Dynamin", "Clathrin", "AP2", "Epsin", "CALM", "SNARE", "Synaptobrevin",
    "Syntaxin", "SNAP25", "Complexin", "Synaptotagmin", "Munc13", "Munc18", "Rab",
    "Rab3GAP", "Rab3GEP", "RIM", "RBP", "Piccolo", "Bassoon", "CAST", "ELKS",
    "Liprin", "GIT", "PIX", "PAK", "Lamellipodin", "Mena", "VASP", "EVL", "Profilin",
    "Cofilin", "Arp2/3", "WASP", "N-WASP", "WAVE", "WHAMM", "JMY", "Cortactin",
    "HS1", "Dynamin2", "Amphiphysin", "Endophilin", "Intersectin", "FCHo", "Eps15",
    "AP180", "Stonin", "Syndapin", "PACSIN", "FBP17", "CIP4", "TOCA", "FNBP1",
    "Fer", "Fes", "Fps", "Ack", "TNK2", "STK", "PYK2", "FAK", "Src", "Lyn", "Fyn",
    "Yes", "Hck", "Lck", "Blk", "Brk", "Srm", "Frk", "Abl", "Arg", "BCR-ABL",
    "TEL-JAK2", "PCM1-JAK2", "BCR-PDGFR", "ETV6-PDGFRB", "FIP1L1-PDGFRA", "KIT-D816V",
    "FLT3-ITD", "NPM1", "CEBPA", "RUNX1", "ASXL1", "TP53", "IDH1", "IDH2", "TET2",
    "DNMT3A", "WT1", "SF3B1", "SRSF2", "U2AF1", "ZRSR2", "STAG2", "BCOR", "PHF6",
    "EZH2", "ASXL1", "CREBBP", "EP300", "KMT2A", "KMT2D", "NSD1", "SETD2", "KDM6A",
    "KDM5C", "ARID1A", "ARID1B", "SMARCA4", "SMARCB1", "PBRM1", "BRD4", "BRD2",
    "BRD3", "BRDT", "BET", "JQ1", "I-BET", "OTX015", "CPI-0610", "ABBV-075",
    "BMS-986158", "GS-5829", "INCB054329", "PFI-1", "RVX-208", "Apabetalone",
    "Resveratrol", "Pterostilbene", "Curcumin", "Quercetin", "Genistein", "Daidzein",
    "Glycitein", "Equol", "Enterolactone", "Enterodiol", "Urolithin", "Ellagitannin",
    "Punicalagin", "Punicalin", "Gallic Acid", "Epigallocatechin", "Epicatechin",
    "Catechin", "Theaflavin", "Thearubigin", "Chlorogenic", "Caffeic", "Ferulic",
    "Sinapic", "p-Coumaric", "Hydroxybenzoic", "Vanillic", "Syringic", "Salicylic",
    "Aspirin", "Ibuprofen", "Naproxen", "Diclofenac", "Celecoxib", "Rofecoxib",
    "Valdecoxib", "Lumiracoxib", "Etoricoxib", "Parecoxib", "Ketorolac", "Indomethacin",
    "Sulindac", "Etodolac", "Ketoprofen", "Flurbiprofen", "Oxaprozin", "Piroxicam",
    "Meloxicam", "Tenoxicam", "Lornoxicam", "Nabumetone", "Meclofenamate", "Mefenamic",
    "Tolfenamic", "Flufenamic", "Meclofenamic", "Diflunisal", "Salsalate", "Choline",
    "Magnesium", "Sodium", "Potassium", "Ammonium", "Lysine", "Arginine", "Ornithine",
    "Citrulline", "Homocitrulline", "Canavanine", "Canaline", "O-Acetylserine",
    "Cysteine", "Homocysteine", "Methionine", "Taurine", "Cystine", "Cystathionine",
    "Lanthionine", "Djenkolic", "Selenocysteine", "Selenomethionine", "Methylselenocysteine",
    "Se-Methylselenomethionine", "Gamma-Glutamylcysteine", "Glutathione", "S-Glutathionyl",
    "S-Nitrosoglutathione", "Sulfiredoxin", "Peroxiredoxin", "Thioredoxin", "Glutaredoxin",
    "Methionine Sulfoxide", "Methionine Sulfone", "Taurine", "Hypotaurine", "Taurocyamine",
    "Taurocholic", "Tauroursodeoxycholic", "Taurochenodeoxycholic", "Taurodeoxycholic",
    "Taurolithocholic", "Taurohyodeoxycholic", "Glycocholic", "Glycochenodeoxycholic",
    "Glycodeoxycholic", "Glycolithocholic", "Glycohyodeoxycholic", "Glycoursodeoxycholic",
    "Cholic", "Chenodeoxycholic", "Deoxycholic", "Lithocholic", "Hyodeoxycholic",
    "Ursodeoxycholic", "Muricholic", "Nordeoxycholic", "Apocholic", "Isocholic",
    "Beta-Muricholic", "Omega-Muricholic", "Alpha-Muricholic", "Hyocholic", "Murocholic"
]

ARTICLE_TEMPLATES = [
    {
        "title": "أفضل {count} أداة مجانية لتسريع {task} في {year}",
        "intro": "في عالم {domain} المتسارع، يبحث الجميع عن حلول فعّالة توفر الوقت والمال. إليك مجموعة من الأدوات المجانية التي ستغير طريقة عملك.",
        "body": "تُعدّ أدوات {tool_type} من أهم ما يحتاجه كل {professional} في {year}. من خلال تجربتنا المكثّفة، وجدنا أن الأدوات المجانية أحياناً تتفوّق على المدفوعة في الكفاءة.\n\nإحدى الميزات الرائعة هي القدرة على {feature} بدون تسجيل أو اشتراك. هذا يعني أنك تستطيع البدء فوراً.\n\nننصحك بزيارة أدواتنا المجانية المتخصصة في هذا المجال، فهي مصممة خصيصاً لمساعدتك في تحقيق أقصى إنتاجية.",
        "outro": "لا تنسَ مشاركة هذه الأدوات مع فريقك. ابدأ الآن واستفد من كل لحظة."
    },
    {
        "title": "دليلك الشامل لـ {topic}: نصائح مالية وتقنية {year}",
        "intro": "سواء كنت مبتدئاً أو محترفاً، فإن فهم {topic} يمكن أن يوفر عليك آلاف الدولارات سنوياً. في هذا الدليل، نكشف عن الأسرار التي يستخدمها الخبراء.",
        "body": "أولاً، يجب أن تفهم أن {concept} ليس مجرد مصطلح تقني، بل هو استثمار حقيقي في مستقبلك. من خلال تطبيق {strategy}، ستتمكن من تقليل النفقات بنسبة تصل إلى {percent}%.\n\nثانياً، الأدوات المجانية المتوفرة على منصتنا توفر لك كل ما تحتاجه للبدء. لا حاجة لشراء برامج باهظة الثمن.\n\nثالثاً، سرعة الأعمال تبدأ من اتخاذ القرار الصحيح في الوقت المناسب. كل دقيقة توفرها هذه الأدوات هي دقيقة تستثمرها في نمو مشروعك.",
        "outro": "تذكر: النجاح يأتي من التراكم اليومي للتحسينات الصغيرة. ابدأ بتطبيق نصيحة واحدة اليوم."
    },
    {
        "title": "كيف تُضاعف إنتاجيتك باستخدام {tool_type} المجانية؟",
        "intro": "الإنتاجية ليست عن العمل بجد، بل عن العمل بذكاء. وفي {year}، الذكاء يعني استخدام الأدوات الصحيحة.",
        "body": "لاحظنا أن {percent}% من المستخدمين يضيعون ساعات في مهام يمكن إنجازها بضغطة زر واحدة. هل أنت واحد منهم؟\n\nباستخدام أدوات {domain} المتوفرة لدينا، يمكنك:\n• إنجاز {task} في ثوانٍ بدلاً من ساعات\n• توفير {saving} شهرياً على الاشتراكات\n• تحسين جودة عملك بشكل ملحوظ\n\nالأدوات المجانية ليست بديلاً رديئاً، بل هي فرصة للتجربة قبل الالتزام بأي تكلفة.",
        "outro": "جرب الأدوات الآن وانضم لآلاف المستخدمين الذين غيّروا طريقة عملهم."
    },
    {
        "title": "{year}: سنة التحول الرقمي مع {topic}",
        "intro": "لم يعد التحول الرقمي خياراً، بل أصبح ضرورة. ومع {topic}، يمكنك أن تكون في المقدمة دون إنفاق ثروة.",
        "body": "في السابق، كانت أدوات {domain} تتطلب فرقاً كاملة وميزانيات ضخمة. أما اليوم، فبفضل التقنيات المفتوحة المصدر والأدوات المجانية، أصبح كل شيء متاحاً للجميع.\n\nنحن في منصتنا نؤمن بأن المعرفة يجب أن تكون متاحة. لذلك نوفر لك:\n- أدوات مجانية 100%\n- مقالات تقنية عميقة\n- نصائح مالية عملية\n- استراتيجيات تسريع الأعمال\n\n{concept} هو المستقبل، والمستقبل يبدأ الآن.",
        "outro": "لا تنتظر الغد. ابدأ رحلتك الرقمية اليوم مع أدواتنا المجانية."
    },
    {
        "title": "5 أخطاء مالية يقع فيها رواد الأعمال وكيف تتجنبها بـ {tool_type}",
        "intro": "أظهرت الدراسات أن {percent}% من الشركات الناشئة تفشل بسبب سوء إدارة المالية. لكن الأدوات الصحيحة يمكن أن تغير هذه الإحصائية.",
        "body": "الخطأ الأول: الاعتماد على برامج مدفوعة قبل التحقق من البدائل المجانية. أدواتنا توفر نفس الوظائف بدون أي تكلفة.\n\nالخطأ الثاني: عدم تتبع المصروفات الصغيرة. باستخدام أدوات {domain}، يمكنك مراقبة كل قرش.\n\nالخطأ الثالث: إهمال {task}. هذا يكلفك وقتك، ووقتك = مال.\n\nالخطأ الرابع والخامس... اكتشفهم بنفسك من خلال أدواتنا الذكية.",
        "outro": "الأدوات المجانية ليست فقط لتوفير المال، بل لبناء عادة الإدارة الرشيدة منذ اليوم الأول."
    }
]

TECH_TOPICS = [
    "الذكاء الاصطناعي", "التعلم الآلي", "البيانات الضخمة", "الحوسبة السحابية",
    "الأمن السيبراني", "تطوير التطبيقات", "تصميم المواقع", "تحسين محركات البحث",
    "التسويق الرقمي", "التجارة الإلكترونية", "إنترنت الأشياء", "البلوكتشين",
    "العملات الرقمية", "الحوسبة الكمية", "الواقع المعزز", "الواقع الافتراضي",
    "الروبوتات", "الأتمتة", "DevOps", "الحاويات", "الخوادم بدون خادم",
    "APIs", "الرسوميات ثلاثية الأبعاد", "معالجة اللغات الطبيعية", "رؤية الحاسوب",
    "الشبكات العصبية", "التعلم العميق", "نمذجة البيانات", "تحليل البيانات",
    "علم البيانات", "هندسة البيانات", "أنظمة التوصية", "الشات بوتات",
    "المساعدات الصوتية", "التعرف على الكلام", "التعرف على الوجوه", "التحليلات التنبؤية",
    "إدارة المشاريع", "العمل عن بُعد", "الأدوات التعاونية", "التخزين السحابي",
    "النسخ الاحتياطي", "استعادة البيانات", "مراقبة الأنظمة", "سجلات الأحداث",
    "إدارة الهوية", "التحقق الثنائي", "التشفير", "شهادات SSL", "جدران الحماية",
    "اختبار الاختراق", "البحث عن الثغرات", "إدارة التصحيحات", "الامتثال",
    "حماية الخصوصية", "GDPR", "CCPA", "إدارة المخاطر", "الاستمرارية",
    "التعافي من الكوارث", "توفر عالي", "موازنة الحمل", "التخزين المؤقت",
    "شبكات توصيل المحتوى", "التسريع", "ضغط البيانات", "تحسين الصور",
    "التنسيقات الحديثة", "الرسوميات المتجهة", "الخطوط", "الألوان", "التباين",
    "إمكانية الوصول", "تجربة المستخدم", "واجهة المستخدم", "التصميم المتجاوب",
    "التصميم التكيفي", "الوضع المظلم", "الرسوم المتحركة", "التفاعلية",
    "التصميم بدون كود", "المنصات منخفضة الكود", "أتمتة سير العمل",
    "التكامل", "الويب هوك", "زابير", "ماك", "إنتجريت", "أتمتة التسويق",
    "إدارة علاقات العملاء", "أنظمة ERP", "إدارة الموارد", "التخطيط المالي",
    "المحاسبة السحابية", "الفواتير الإلكترونية", "المدفوعات الرقمية",
    "المحافظ الإلكترونية", "التحويلات الدولية", "إدارة المخزون", "سلسلة التوريد",
    "الخدمات اللوجستية", "تتبع الشحنات", "إدارة المستودعات", "الجرد",
    "الباركود", "QR", "RFID", "GPS", "GIS", "الخرائط الرقمية",
    "التنقل", "تحليل الموقع", "الجغرافيا", "المدن الذكية", "الطاقة المتجددة",
    "الكفاءة الطاقية", "البيئة", "الاستدامة", "الاقتصاد الدائري",
    "إعادة التدوير", "المواد الخام", "الطباعة ثلاثية الأبعاد", "الصناعة 4.0",
    "التوأم الرقمي", "المحاكاة", "النماذج الأولية", "الاختبار السريع",
    "التصميم التكراري", "المنهجية الرشيقة", "سكروم", "كانبان", "سداسي",
    "تطوير البرمجيات", "البرمجة", "الخوارزميات", "هياكل البيانات",
    "أنظمة التشغيل", "قواعد البيانات", "SQL", "NoSQL", "NewSQL",
    "قواعد البيانات الرسمية", "الرسوميات", "الشبكات", "بروتوكولات الإنترنت",
    "TCP/IP", "HTTP/3", "QUIC", "WebSockets", "gRPC", "GraphQL",
    "REST", "SOAP", "XML", "JSON", "YAML", "TOML", "INI", "CSV",
    "Parquet", "ORC", "Avro", "Protocol Buffers", "Thrift", "MessagePack",
    "BSON", "CBOR", "FlexBuffers", "FlatBuffers", "Cap'n Proto", "ZeroMQ",
    "RabbitMQ", "Kafka", "Pulsar", "Redis", "Memcached", "Cassandra",
    "MongoDB", "DynamoDB", "Firestore", "Cosmos DB", "CockroachDB",
    "TiDB", "YugabyteDB", "PlanetScale", "Neon", "Supabase", "Hasura",
    "Prisma", "Drizzle", "TypeORM", "Sequelize", "Mongoose", "SQLAlchemy",
    "Django ORM", "Active Record", "Hibernate", "Entity Framework", "Dapper",
    "NHibernate", "MyBatis", "jOOQ", "QueryDSL", "JPA", "JDBC", "ODBC",
    "ADO.NET", "PDO", "mysqli", "pg_query", "sqlite3", "LevelDB", "RocksDB",
    "LMDB", "Berkeley DB", "Kyoto Cabinet", "Tokyo Cabinet", "Tkrzw",
    "UnQLite", "Vedis", "EJDB", "Upscaledb", "ForestDB", "Couchbase Lite",
    "Realm", "ObjectBox", "Room", "Core Data", "SQLite.swift", "GRDB",
    "FMDB", "WCDB", "GreenDAO", "ObjectBox", "Realm", "SugarORM", "ActiveAndroid",
    "ORMLite", "GreenDAO", "DBFlow", "Requery", "SQLDelight", "Exposed",
    "Ktorm", "Jdbi", "Spring Data", "Micronaut Data", "Quarkus Hibernate",
    "Panache", "ActiveJPA", "Ebean", "JOOQ", "Querydsl", "MyBatis-Plus",
    "TkMyBatis", "Fluent MyBatis", "Custom Mapper", "通用Mapper", "MP",
    "MyBatis-Flex", "MyBatis-Plus-Join", "MyBatisX", "MyBatis-Plus-Generator",
    "代码生成器", "逆向工程", " scaffolding", "脚手架", "模板引擎", "Thymeleaf",
    "FreeMarker", "Velocity", "JSP", "JSTL", "Facelets", "JSF", "PrimeFaces",
    "RichFaces", "IceFaces", "MyFaces", "Tomahawk", "Trinidad", "Tobago",
    "Portlet Bridge", "Spring Faces", "Spring Web Flow", "Web Flow", "Flow",
    "State Machine", "Spring Statemachine", "Squirrel", "Stateless4j", "Easy States",
    "State Machine", "Mason", "Stateless", "Automaton", "JState", "StateJ",
    "State", "Transition", "Event", "Action", "Guard", "Context", "State Pattern",
    "Strategy Pattern", "Command Pattern", "Observer Pattern", "Pub/Sub",
    "Event Sourcing", "CQRS", "Event Store", "Axon", "Eventuate", "NEventStore",
    "Marten", "Streamstone", "SQLStreamStore", "GetEventStore", "EventStoreDB",
    "LiteDB", "RavenDB", "Voron", "Esent", "Rocks", "FASTER", "Trill",
    "StreamInsight", "Reactive Extensions", "RxJava", "RxJS", "RxSwift",
    "RxKotlin", "RxScala", "RxRuby", "RxPHP", "RxGo", "RxRust", "RxCpp",
    "ReactiveUI", "Akka.NET", "Akka", "Vert.x", "Quarkus", "Micronaut",
    "Helidon", "Ktor", "Spring Boot", "Spring Framework", "Spring Cloud",
    "Spring Security", "Spring Data", "Spring Integration", "Spring Batch",
    "Spring Shell", "Spring HATEOAS", "Spring REST Docs", "Spring GraphQL",
    "Spring Native", "Spring WebFlux", "Project Reactor", "RSocket", "R2DBC",
    "Spring R2DBC", "Spring Cloud Gateway", "Spring Cloud Config", "Eureka",
    "Consul", "Zookeeper", "Nacos", "Etcd", "Kubernetes", "Docker", "Podman",
    "containerd", "CRI-O", "Buildah", "Skopeo", "Kaniko", "Jib", "Buildpacks",
    "Cloud Native Buildpacks", "Paketo", "Heroku", "Dokku", "Flynn", "Deis",
    "OpenShift", "Rancher", "K3s", "K3d", "Kind", "Minikube", "MicroK8s",
    "Docker Desktop", "Colima", "Lima", "Rancher Desktop", "Podman Desktop",
    "DevPod", "Gitpod", "GitHub Codespaces", "CodeSandbox", "StackBlitz",
    "Replit", "Glitch", "CodePen", "JSFiddle", "JSBin", "Plunker", "Dabblet",
    "Liveweave", "CSSDeck", "Bootply", "Runnable", "Codenvy", "Cloud9",
    "AWS Cloud9", "Azure Cloud Shell", "Google Cloud Shell", "Oracle Cloud Shell",
    "IBM Cloud Shell", "Alibaba Cloud Shell", "Tencent Cloud Shell", "Huawei Cloud Shell",
    "DigitalOcean Droplet", "Linode", "Vultr", "Hetzner", "UpCloud", "Scaleway",
    "OVHcloud", "Ionos", "1&1", "Namecheap", "GoDaddy", "Bluehost", "HostGator",
    "SiteGround", "DreamHost", "InMotion", "A2 Hosting", "GreenGeeks", "HostPapa",
    "iPage", "FatCow", "JustHost", "HostMonster", "Netfirms", "IPower", "Dotster",
    "Domain.com", "Register.com", "Network Solutions", "Enom", "Tucows", "OpenSRS",
    "ResellerClub", "Name.com", "NameSilo", "Porkbun", "Dynadot", "Google Domains",
    "AWS Route 53", "Cloudflare Registrar", "Azure DNS", "Google Cloud DNS",
    "DNSimple", "NS1", "Constellix", "Dyn", "UltraDNS", "EasyDNS", "Hurricane Electric",
    "DNS Made Easy", "ZoneEdit", "No-IP", "Dynu", "FreeDNS", "Afraid.org",
    "DuckDNS", "YDNS", "DNSExit", "EntryDNS", "Zonomi", "RcodeZero", "CSC",
    "MarkMonitor", "BrandShelter", "Safenames", "101domain", "Gandi", "OVH",
    "GABIA", "WhoisXML", "DomainTools", "WHOIS", "RDAP", "IRIS", "DAS",
    "Escrow", "Aftermarket", "Sedo", "Afternic", "Dan.com", "Uniregistry Market",
    "BrandBucket", "SquadHelp", "Brandpa", "Namerific", "Brandroot", "Brandable",
    "Atom", "Novanym", "Oyzta", "BrandDo", "Brandwise", "NamingForce",
    "Crowdspring", "99designs", "DesignCrowd", "LogoMyWay", "Hatchwise",
    "ZillionDesigns", "48hourslogo", "LogoTournament", "LogoArena", "Springboard",
    "LogoLounge", "Dribbble", "Behance", "Coroflot", "Portfoliobox", "Carbonmade",
    "Crevado", "Format", "Squarespace", "Wix", "Weebly", "Strikingly", "Tilda",
    "Readymag", "Webflow", "Framer", "Figma", "Sketch", "Adobe XD", "InVision",
    "Proto.io", "Marvel", "Principle", "Flinto", "Origami", "Axure", "Balsamiq",
    "Mockplus", "ProtoPie", "Kite", "Lottie", "Rive", "Haiku", "Bodymovin",
    "After Effects", "Premiere Pro", "DaVinci Resolve", "Final Cut Pro",
    "Motion", "Compressor", "Cinema 4D", "Blender", "Maya", "3ds Max", "Houdini",
    "Nuke", "Fusion", "Flame", "Smoke", "Mocha", "Syntheyes", "PFTrack",
    "Boujou", "MatchMover", "3DEqualizer", "Autodesk", "Adobe", "Maxon", "SideFX",
    "Foundry", "Blackmagic Design", "Apple", "Avid", "Corel", "Magix", "CyberLink",
    "Wondershare", "TechSmith", "Camtasia", "Snagit", "Bandicam", "OBS Studio",
    "Streamlabs", "XSplit", "vMix", "Wirecast", "Restream", "StreamYard",
    "Melon", "Riverside", "SquadCast", "Zencastr", "Anchor", "Buzzsprout",
    "Libsyn", "Podbean", "Transistor", "Captivate", "Simplecast", "Spreaker",
    "SoundCloud", "Mixcloud", "HearThis.at", "Audiomack", "Bandcamp", "DistroKid",
    "TuneCore", "CD Baby", "LANDR", "Amuse", "RouteNote", "ONErpm", "Symphonic",
    "The Orchard", "Believe", "FUGA", "Ditto Music", "ReverbNation", "Soundrop",
    "Level Music", "UnitedMasters", "Stem", "Vydia", "Monstercat", "Armada",
    "Spinnin' Records", "Anjunabeats", "A State of Trance", "Above & Beyond",
    "Armin van Buuren", "Tiësto", "Martin Garrix", "David Guetta", "Calvin Harris",
    "Swedish House Mafia", "Alesso", "Avicii", "Deadmau5", "Skrillex", "Diplo",
    "Major Lazer", "Jack Ü", "Zedd", "Chainsmokers", "Kygo", "Alan Walker",
    "Marshmello", "DJ Snake", "Steve Aoki", "Dimitri Vegas", "Like Mike",
    "Hardwell", "W&W", "Afrojack", "Nicky Romero", "Sander van Doorn",
    "Ferry Corsten", "Gareth Emery", "Paul van Dyk", "Paul Oakenfold", "John Digweed",
    "Sasha", "Carl Cox", "Richie Hawtin", "Adam Beyer", "Nina Kraviz", "Charlotte de Witte",
    "Amelie Lens", "Peggy Gou", "Helena Hauff", "Annie Mac", "Mary Anne Hobbs",
    "B.Traits", "Maya Jane Coles", "Jamie Jones", "Seth Troxler", "The Martinez Brothers",
    "Loco Dice", "Marco Carola", "Joseph Capriati", "Maceo Plex", "Tale of Us",
    "Mind Against", "Afterlife", "Drumcode", "Klockworks", "Ostgut Ton", "Berghain",
    "Tresor", "Watergate", "About Blank", "://about blank", "Sisyphos", "Kater Blau",
    "Else", "Ritter Butzke", "Gretchen", "KitKatClub", "Insomnia", "Tribehouse",
    "Omen", "Dorian Gray", "U60311", "Cocoon", "Amnesia", "Pacha", "Ushuaïa",
    "Hï Ibiza", "DC-10", "Privilege", "Space", "Sankeys", "Blue Marlin", "Destino",
    "Heart", "Lío", "Pacha", "Lio", "Heart", "Destino", "Talamanca", "Cala Jondal",
    "Es Cavallet", "Las Salinas", "Playa d'en Bossa", "Figueretas", "Cala Comte",
    "Cala Bassa", "Cala Tarida", "Cala d'Hort", "Cala Vadella", "Cala Carbo",
    "Cala Llentrisca", "Cala d'en Serra", "Portinatx", "Sant Joan", "Sant Antoni",
    "Santa Eulalia", "Es Canar", "Cala Llonga", "S'Argamassa", "Cala Pada",
    "Cala Martina", "Es Figueral", "Aigües Blanques", "Cala Boix", "Pou des Lleo",
    "Tagomago", "Illa de es Vedrà", "Sa Conillera", "Illa des Bosc", "S'Espalmador",
    "Formentera", "La Savina", "Es Pujols", "Sant Francesc", "El Pilar de la Mola",
    "Cap de Barbaria", "Punta Rasa", "Cala Saona", "Migjorn", "Es Arenals",
    "Es Calo", "La Mola", "Pilar", "Es Pujols", "La Savina", "Es Mal Pas",
    "Es Marjals", "Ses Salines", "Es Trucadors", "S'Alga", "Punta Prima",
    "Cala en Baster", "Cala Codolar", "Platja de ses Illetes", "Llevant",
    "Trocadors", "Racó de sa Pujada", "Es Cavall d'en Borras", "Es Pas",
    "S'Espalmador", "Punta Prima", "Cala en Baster", "Cala Codolar", "Ses Illetes",
    "Llevant", "Trocadors", "Racó de sa Pujada", "Es Cavall", "Es Pas", "S'Alga"
]

DOMAINS = [
    "التقنية", "الأعمال", "التسويق", "التصميم", "البرمجة",
    "الأمن السيبراني", "تحسين محركات البحث", "التجارة الإلكترونية",
    "إدارة المشاريع", "المالية", "الاستثمار", "ريادة الأعمال"
]

TASKS = [
    "إدارة المهام", "تحليل البيانات", "تصميم المواقع", "كتابة المحتوى",
    "إدارة وسائل التواصل", "إنشاء التقارير", "مراقبة الأداء", "أتمتة العمليات",
    "تحويل الملفات", "ضغط الصور", "توليد كلمات المرور", "اختبار السرعة",
    "تحسين الإنتاجية", "تنظيم الجداول", "حساب التكاليف", "تتبع النفقات"
]

PROFESSIONALS = [
    "المطور", "المصمم", "مسوق", "رائد الأعمال", "محلل البيانات",
    "مدير المشروع", "كاتب المحتوى", "خبير SEO", "مستشار مالي", "مدير تقني"
]

FEATURES = [
    "التصدير المباشر", "المشاركة التعاونية", "التكامل مع التطبيقات", "التخصيص الكامل",
    "العمل بدون إنترنت", "التشفير التلقائي", "النسخ الاحتياطي", "التنبيهات الذكية"
]

CONCEPTS = [
    "أتمتة سير العمل", "تحليلات البيانات", "التكامل السحابي", "إدارة الموارد",
    "تحسين الأداء", "تقليل التكاليف", "زيادة الإيرادات", "تحسين تجربة العميل"
]

STRATEGIES = [
    "أتمتة المهام المتكررة", "استخدام الأدوات المجانية", "التركيز على الجودة",
    "ت delegating المهام", "تحليل البيانات بشكل دوري", "تحسين العمليات"
]

TOOL_TYPES = [
    "تحويل الملفات", "تحليل البيانات", "إدارة المشاريع", "تصميم الرسوميات",
    "تحسين الأداء", "الأمن", "النسخ الاحتياطي", "التعاون", "الحسابات", "التحويلات"
]

SAVINGS = ["100$", "200$", "500$", "50$", "300$", "150$"]

PERCENTS = ["30", "40", "50", "60", "70", "80", "90"]

# ===================== HELPERS =====================

def load_db():
    if DB_FILE.exists():
        with open(DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"tools": [], "articles": [], "meta": {"last_run": None, "tool_count": 0}}

def save_db(db):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def ensure_dirs():
    TOOLS_DIR.mkdir(parents=True, exist_ok=True)
    ARTICLES_DIR.mkdir(parents=True, exist_ok=True)

def generate_tool_name(index):
    """Generate a unique tool name using pools"""
    prefix = random.choice(TOOL_PREFIXES)
    base = TOOL_NAMES[index % len(TOOL_NAMES)]
    cat = random.choice(TOOL_CATEGORIES)
    return f"{prefix} {base} - {cat}", cat

def generate_tool_page(tool_id, name, category, description):
    slug = f"tool-{tool_id}"
    html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{name} | أداة مجانية</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="./tools/{slug}.html">
  <style>
    body {{ font-family: 'Segoe UI', Tahoma, sans-serif; background: #0f172a; color: #e2e8f0; margin: 0; padding: 0; }}
    .container {{ max-width: 800px; margin: 40px auto; padding: 20px; }}
    h1 {{ color: #38bdf8; }}
    .badge {{ background: #1e293b; padding: 4px 12px; border-radius: 20px; font-size: 0.85rem; color: #94a3b8; display: inline-block; margin-bottom: 20px; }}
    .desc {{ font-size: 1.1rem; line-height: 1.8; margin-bottom: 30px; }}
    .ad {{ background: linear-gradient(135deg, #1e293b, #334155); padding: 20px; border-radius: 12px; text-align: center; margin: 30px 0; border: 1px solid #475569; }}
    .ad a {{ color: #38bdf8; text-decoration: none; font-weight: bold; font-size: 1.1rem; }}
    .ad a:hover {{ text-decoration: underline; }}
    .back {{ display: inline-block; margin-top: 20px; color: #94a3b8; text-decoration: none; }}
    .back:hover {{ color: #38bdf8; }}
  </style>
</head>
<body>
  <div class="container">
    <span class="badge">{category}</span>
    <h1>{name}</h1>
    <p class="desc">{description}</p>
    <div class="ad">
      <p>🚀 اكتشف المزيد من الأدوات والفرص الرائعة</p>
      <a href="{AD_LINK}" target="_blank" rel="nofollow noopener">اضغط هنا للاستفادة من العرض المميز</a>
    </div>
    <a href="../index.html" class="back">← العودة للرئيسية</a>
  </div>
</body>
</html>'''
    return html

def generate_article(article_id):
    template = random.choice(ARTICLE_TEMPLATES)
    year = datetime.now().year
    count = random.choice([5, 7, 10, 12, 15])
    task = random.choice(TASKS)
    domain = random.choice(DOMAINS)
    topic = random.choice(TECH_TOPICS)
    tool_type = random.choice(TOOL_TYPES)
    professional = random.choice(PROFESSIONALS)
    feature = random.choice(FEATURES)
    concept = random.choice(CONCEPTS)
    strategy = random.choice(STRATEGIES)
    percent = random.choice(PERCENTS)
    saving = random.choice(SAVINGS)
    
    title = template["title"].format(
        count=count, task=task, year=year, topic=topic,
        tool_type=tool_type, domain=domain
    )
    
    intro = template["intro"].format(
        domain=domain, year=year, topic=topic, percent=percent,
        concept=concept, task=task
    )
    
    body = template["body"].format(
        tool_type=tool_type, domain=domain, year=year,
        professional=professional, feature=feature,
        concept=concept, strategy=strategy, percent=percent,
        task=task, saving=saving
    )
    
    outro = template["outro"]
    
    content = f"{intro}\n\n{body}\n\n{outro}"
    
    # Add ad link naturally in the article
    ad_insert = f"\n\n> 💡 **فرصة لا تُفوّت:** [اكتشف أدواتنا المجانية والعروض المميزة من هنا]({AD_LINK})\n\n"
    paragraphs = content.split("\n\n")
    insert_pos = len(paragraphs) // 2
    paragraphs.insert(insert_pos, ad_insert.strip())
    content = "\n\n".join(paragraphs)
    
    date_str = datetime.now().strftime("%Y-%m-%d")
    slug = f"article-{article_id}"
    
    html = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{intro[:150]}...">
  <meta name="keywords" content="{topic}, {domain}, أدوات مجانية, {year}">
  <link rel="canonical" href="./articles/{slug}.html">
  <style>
    body {{ font-family: 'Segoe UI', Tahoma, sans-serif; background: #0f172a; color: #e2e8f0; margin: 0; padding: 0; line-height: 1.8; }}
    .container {{ max-width: 800px; margin: 40px auto; padding: 20px; }}
    h1 {{ color: #38bdf8; font-size: 1.8rem; margin-bottom: 10px; }}
    .meta {{ color: #94a3b8; font-size: 0.9rem; margin-bottom: 30px; }}
    .content {{ font-size: 1.1rem; }}
    .content p {{ margin-bottom: 20px; }}
    .content a {{ color: #38bdf8; text-decoration: none; }}
    .content a:hover {{ text-decoration: underline; }}
    .ad-box {{ background: linear-gradient(135deg, #1e293b, #334155); padding: 20px; border-radius: 12px; text-align: center; margin: 30px 0; border: 1px solid #475569; }}
    .ad-box a {{ color: #fbbf24; font-weight: bold; font-size: 1.1rem; }}
    .back {{ display: inline-block; margin-top: 30px; color: #94a3b8; text-decoration: none; }}
    .back:hover {{ color: #38bdf8; }}
  </style>
</head>
<body>
  <div class="container">
    <h1>{title}</h1>
    <div class="meta">📅 {date_str} | 🏷️ {domain} | 📝 {topic}</div>
    <div class="content">
      {content.replace(chr(10)+chr(10), '</p><p>').replace('> ', '<blockquote>').replace('</p><p><blockquote>', '<blockquote>')}
    </div>
    <div class="ad-box">
      <p>🚀 استفد من أدواتنا المجانية وعزز إنتاجيتك</p>
      <a href="{AD_LINK}" target="_blank" rel="nofollow noopener">اضغط هنا للوصول للأدوات والعروض</a>
    </div>
    <a href="../index.html" class="back">← العودة للرئيسية</a>
  </div>
</body>
</html>'''
    
    # Fix blockquote closing
    html = html.replace('<blockquote>', '<blockquote>').replace('</p><p><blockquote>', '<blockquote>')
    
    return {
        "id": article_id,
        "slug": slug,
        "title": title,
        "date": date_str,
        "category": domain,
        "topic": topic,
        "content": content,
        "html": html
    }

def generate_tool(tool_id):
    name, category = generate_tool_name(tool_id)
    description = f"أداة {name} هي حل مجاني متكامل يتيح لك إنجاز مهام {category} بكفاءة عالية وسرعة فائقة. مصممة خصيصاً للمحترفين والمبتدئين على حد سواء."
    
    html = generate_tool_page(tool_id, name, category, description)
    slug = f"tool-{tool_id}"
    
    return {
        "id": tool_id,
        "slug": slug,
        "name": name,
        "category": category,
        "description": description,
        "html": html
    }

def write_tool_file(tool):
    path = TOOLS_DIR / f"{tool['slug']}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(tool["html"])

def write_article_file(article):
    path = ARTICLES_DIR / f"{article['slug']}.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(article["html"])

def update_index_html(db):
    """Regenerate index.html with fresh data from database"""
    tools_html = ""
    for t in db["tools"]:
        tools_html += f'''
      <div class="card" data-search="{t['name']} {t['category']} {t['description']}">
        <div class="card-badge">{t['category']}</div>
        <h3>{t['name']}</h3>
        <p>{t['description'][:80]}...</p>
        <a href="./tools/{t['slug']}.html" class="card-link">استخدم الأداة →</a>
      </div>'''
    
    articles_html = ""
    for a in db["articles"][-20:]:  # Show last 20 articles
        articles_html += f'''
      <div class="card article-card" data-search="{a['title']} {a['topic']} {a['category']}">
        <div class="card-meta">📅 {a['date']} | 🏷️ {a['category']}</div>
        <h3>{a['title']}</h3>
        <p>{a['content'][:100]}...</p>
        <a href="./articles/{a['slug']}.html" class="card-link">اقرأ المقال →</a>
      </div>'''
    
    index_content = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>إمبراطورية الويب | 500+ أداة مجانية ومقالات تقنية</title>
  <meta name="description" content="أكبر منصة عربية للأدوات المجانية والمقالات التقنية. {len(db['tools'])} أداة و{len(db['articles'])} مقال في مجالات التقنية والمال والأعمال.">
  <meta name="keywords" content="أدوات مجانية, مقالات تقنية, SEO, أدوات مطورين, تحويل ملفات, حاسبات, أدوات تصميم">
  <meta name="author" content="Empire Web">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="https://yourusername.github.io/repo-name/">
  <link rel="sitemap" type="application/xml" title="Sitemap" href="./sitemap.xml">
  <meta property="og:title" content="إمبراطورية الويب | 500+ أداة مجانية">
  <meta property="og:description" content="منصة شاملة للأدوات المجانية والمحتوى التقني">
  <meta property="og:type" content="website">
  <style>
    :root {{ --bg: #0f172a; --surface: #1e293b; --primary: #38bdf8; --accent: #fbbf24; --text: #e2e8f0; --muted: #94a3b8; }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: var(--bg); color: var(--text); line-height: 1.6; }}
    header {{ background: linear-gradient(135deg, #1e293b, #0f172a); padding: 40px 20px; text-align: center; border-bottom: 1px solid #334155; }}
    header h1 {{ font-size: 2.2rem; color: var(--primary); margin-bottom: 10px; }}
    header p {{ color: var(--muted); font-size: 1.1rem; }}
    .stats {{ display: flex; justify-content: center; gap: 30px; margin-top: 20px; flex-wrap: wrap; }}
    .stat {{ background: var(--surface); padding: 10px 20px; border-radius: 8px; border: 1px solid #334155; }}
    .stat span {{ color: var(--accent); font-weight: bold; font-size: 1.2rem; }}
    nav {{ background: var(--surface); padding: 15px; text-align: center; position: sticky; top: 0; z-index: 100; border-bottom: 1px solid #334155; }}
    nav button {{ background: transparent; border: 1px solid #475569; color: var(--text); padding: 8px 24px; margin: 0 5px; border-radius: 6px; cursor: pointer; transition: all 0.3s; }}
    nav button:hover, nav button.active {{ background: var(--primary); color: #0f172a; border-color: var(--primary); }}
    .search-box {{ max-width: 600px; margin: 30px auto; padding: 0 20px; }}
    .search-box input {{ width: 100%; padding: 14px 20px; border-radius: 10px; border: 1px solid #475569; background
