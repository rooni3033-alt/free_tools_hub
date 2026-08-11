#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Empire Web Engine v2 — 500 Functional Tools + Infinite Articles
Every tool is a real mini-app (HTML+CSS+JS). Zero backend required.
"""

import json
import os
import random
import hashlib
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
    "Tester", "Monitor", "Optimizer", "Utility", "Math"
]

TOOL_PREFIXES = [
    "Smart", "Pro", "Ultra", "Mega", "Quick", "Auto", "Easy", "Super",
    "Fast", "Instant", "Advanced", "Dynamic", "Global", "Prime", "Elite",
    "Hyper", "Nano", "Cyber", "Tech", "Cloud", "Digital", "Net", "Web",
    "Code", "Data", "Pixel", "Byte", "Bit", "Core", "Alpha", "Beta", "Sigma"
]

TOOL_SUFFIXES = [
    "JSON Formatter", "Base64 Tool", "URL Encoder", "Password Generator", "Color Studio",
    "Unit Converter", "Word Counter", "Lorem Generator", "QR Maker", "Markdown Editor",
    "CSS Minifier", "HTML Entities", "Hash Generator", "Case Converter", "CSV Converter",
    "Image Base64", "Base64 Image", "Diff Checker", "Regex Tester", "Base Converter",
    "Percentage Calc", "Loan Calculator", "BMI Calculator", "Age Calculator", "Stopwatch",
    "Countdown Timer", "Pomodoro", "Random Number", "UUID Maker", "Slug Generator",
    "Duplicate Remover", "Line Sorter", "Text Reverser", "Palindrome Check", "IP Validator",
    "Email Checker", "Card Validator", "Barcode Maker", "Morse Translator", "Cipher Tool",
    "Binary Converter", "Hex Converter", "HTML Previewer", "Shadow Generator", "Flexbox Builder",
    "Gradient Maker", "Radius Generator", "Aspect Calc", "Screen Info", "Browser Stats",
    "Meta Generator", "Robots Builder", "Sitemap Maker", "Twitter Card", "OG Generator",
    "Favicon Maker", "Placeholder Img", "Meme Creator", "Image Resizer", "ASCII Art",
    "Typing Test", "World Clock", "Timezone Calc", "Date Diff", "Days Counter",
    "Invoice Maker", "Receipt Builder", "Password Check", "Username Gen", "Business Card",
    "Resume Builder", "JSON Path", "XML Formatter", "YAML Parser", "SQL Formatter",
    "Cron Parser", "Timestamp Conv", "Unix Time", "Palette Gen", "Fake Data",
    "API Tester", "HTTP Builder", "JWT Decoder", "Table Maker", "Chart Builder",
    "Mind Mapper", "Flowchart", "Certificate", "Badge Maker", "Leaderboard",
    "Quiz Builder", "Poll Maker", "Survey Tool", "Todo List", "Kanban Board",
    "Habit Tracker", "Expense Log", "Budget Planner", "Pomodoro Pro", "Focus Timer",
    "Tip Calculator", "Split Bill", "Tax Calculator", "VAT Calc", "ROI Calculator",
    "Currency Conv", "Fuel Calc", "Trip Planner", "Mileage Log", "Calendar Gen",
    "Prime Check", "Fibonacci", "Factorial", "GCD LCM", "Equation Solver",
    "Matrix Calc", "Vector Calc", "Stats Calc", "Probability", "Fraction Calc",
    "Ratio Calc", "Root Calc", "Log Calc", "Trig Calc", "Circle Calc",
    "Triangle Solver", "Distance Calc", "Slope Calc", "Compound Interest", "Retirement Calc",
    "Mortgage Calc", "Car Loan", "Savings Calc", "Investment", "Break-even",
    "Ohm Law", "Power Calc", "Resistor Calc", "LED Resistor", "Antenna Calc",
    "Subnet Calc", "IP Subnet", "CIDR Calc", "Binary Calc", "IPv6 Calc",
    "Hash MD5", "Hash SHA1", "Hash SHA256", "Hash SHA512", "Checksum",
    "Password Hash", "HMAC Generator", "UUID v4", "UUID v5", "NanoID",
    "Token Generator", "Key Generator", "CSR Generator", "PEM Parser", "SSL Checker",
    "Port Scanner", "DNS Lookup", "Whois Lookup", "IP Geolocation", "Blacklist Check",
    "URL Parser", "URL Expander", "Redirect Check", "Header Check", "SSL Info",
    "Cipher AES", "Cipher DES", "Cipher RSA", "Cipher Blowfish", "Steganography",
    "File Hash", "String Hash", "Compare Hash", "Verify Hash", "Hash Cracker",
    "Hex Editor", "Bin Editor", "Dec Editor", "Oct Editor", "Base32",
    "Base58", "Base85", "UUEncode", "XXEncode", "Quoted Printable",
    "Punycode", "IDN Converter", "URL Slug", "URL Shortener", "Deep Link",
    "UTM Builder", "Campaign URL", "Affiliate Link", "Share Link", "Embed Code",
    "Iframe Generator", "Object Embed", "PDF Embed", "Audio Embed", "Video Embed",
    "Playlist Maker", "RSS Feed", "Atom Feed", "Sitemap XML", "Sitemap HTML",
    "Breadcrumb", "Pagination", "Tag Cloud", "Archive List", "Calendar Widget",
    "Clock Widget", "Counter Widget", "Timer Widget", "Progress Bar", "Loading Spinner",
    "Skeleton Screen", "Placeholder Text", "Dummy Image", "Avatar Generator", "Identicon",
    "Robohash", "Dice Bear", "Gravatar URL", "Profile Card", "Social Card",
    "Preview Card", "Link Preview", "Rich Snippet", "Schema Markup", "Microdata",
    "RDFa Generator", "JSON-LD Gen", "Open Graph", "Twitter Card", "WhatsApp Share",
    "Facebook Share", "LinkedIn Share", "Pinterest Pin", "Reddit Share", "Telegram Share",
    "Email Share", "SMS Share", "QR Share", "NFC Tag", "Deep Link Gen",
    "App Link", "Universal Link", "Intent URL", "Custom Scheme", "WebAPK",
    "PWA Manifest", "Service Worker", "App Shell", "Splash Screen", "Theme Color",
    "Icon Generator", "Maskable Icon", "Adaptive Icon", "Notification Icon", "Badge Icon",
    "Shortcut Icon", "Apple Touch", "Favicon ICO", "Favicon SVG", "Favicon PNG",
    "Windows Tile", "Safari Pin", "Chrome Theme", "Firefox Theme", "Edge Theme",
    "Opera Theme", "Vivaldi Theme", "Brave Theme", "Arc Theme", "Safari Theme"
]

ARTICLE_TEMPLATES = [
    {
        "title": "أفضل {count} أداة مجانية لتسريع {task} في {year}",
        "intro": "في عالم {domain} المتسارع، يبحث الجميع عن حلول فعّالة. إليك مجموعة من الأدوات المجانية التي ستغير طريقة عملك.",
        "body": "تُعدّ أدوات {tool_type} من أهم ما يحتاجه كل {professional}. من خلال تجربتنا، وجدنا أن الأدوات المجانية أحياناً تتفوّق على المدفوعة.\n\nإحدى الميزات الرائعة هي القدرة على {feature} بدون تسجيل. هذا يعني أنك تستطيع البدء فوراً.\n\nننصحك بزيارة أدواتنا المجانية المتخصصة في هذا المجال، فهي مصممة خصيصاً لمساعدتك في تحقيق أقصى إنتاجية.",
        "outro": "لا تنسَ مشاركة هذه الأدوات مع فريقك. ابدأ الآن واستفد من كل لحظة."
    },
    {
        "title": "دليلك الشامل لـ {topic}: نصائح مالية وتقنية {year}",
        "intro": "سواء كنت مبتدئاً أو محترفاً، فإن فهم {topic} يمكن أن يوفر عليك آلاف الدولارات سنوياً.",
        "body": "أولاً، يجب أن تفهم أن {concept} ليس مجرد مصطلح تقني، بل هو استثمار حقيقي. من خلال تطبيق {strategy}، ستتمكن من تقليل النفقات بنسبة تصل إلى {percent}%.\n\nثانياً، الأدوات المجانية المتوفرة على منصتنا توفر لك كل ما تحتاجه للبدء.\n\nثالثاً، سرعة الأعمال تبدأ من اتخاذ القرار الصحيح في الوقت المناسب.",
        "outro": "تذكر: النجاح يأتي من التراكم اليومي للتحسينات الصغيرة."
    },
    {
        "title": "كيف تُضاعف إنتاجيتك باستخدام {tool_type} المجانية؟",
        "intro": "الإنتاجية ليست عن العمل بجد، بل عن العمل بذكاء. وفي {year}، الذكاء يعني استخدام الأدوات الصحيحة.",
        "body": "لاحظنا أن {percent}% من المستخدمين يضيعون ساعات في مهام يمكن إنجازها بضغطة زر. هل أنت واحد منهم؟\n\nباستخدام أدوات {domain} المتوفرة لدينا، يمكنك:\n• إنجاز {task} في ثوانٍ بدلاً من ساعات\n• توفير {saving} شهرياً على الاشتراكات\n• تحسين جودة عملك بشكل ملحوظ",
        "outro": "جرب الأدوات الآن وانضم لآلاف المستخدمين الذين غيّروا طريقة عملهم."
    },
    {
        "title": "{year}: سنة التحول الرقمي مع {topic}",
        "intro": "لم يعد التحول الرقمي خياراً، بل أصبح ضرورة. ومع {topic}، يمكنك أن تكون في المقدمة دون إنفاق ثروة.",
        "body": "في السابق، كانت أدوات {domain} تتطلب ميزانيات ضخمة. أما اليوم، فبفضل التقنيات المفتوحة المصدر والأدوات المجانية، أصبح كل شيء متاحاً.\n\nنحن في منصتنا نؤمن بأن المعرفة يجب أن تكون متاحة. لذلك نوفر لك:\n- أدوات مجانية 100%\n- مقالات تقنية عميقة\n- نصائح مالية عملية\n- استراتيجيات تسريع الأعمال",
        "outro": "لا تنتظر الغد. ابدأ رحلتك الرقمية اليوم مع أدواتنا المجانية."
    },
    {
        "title": "5 أخطاء مالية يقع فيها رواد الأعمال وكيف تتجنبها بـ {tool_type}",
        "intro": "أظهرت الدراسات أن {percent}% من الشركات الناشئة تفشل بسبب سوء إدارة المالية. لكن الأدوات الصحيحة يمكن أن تغير هذه الإحصائية.",
        "body": "الخطأ الأول: الاعتماد على برامج مدفوعة قبل التحقق من البدائل المجانية. أدواتنا توفر نفس الوظائف بدون أي تكلفة.\n\nالخطأ الثاني: عدم تتبع المصروفات الصغيرة. باستخدام أدوات {domain}، يمكنك مراقبة كل قرش.\n\nالخطأ الثالث: إهمال {task}. هذا يكلفك وقتك، ووقتك = مال.",
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

# ===================== FUNCTIONAL TOOL TEMPLATES =====================
# Each returns a full HTML string with working JS

def tool_json_formatter(name, desc):
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>{name}</title>
<style>
body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: #0f172a; color: #e2e8f0; margin: 0; padding: 20px; }}
.container {{ max-width: 900px; margin: 0 auto; }}
h1 {{ color: #38bdf8; }}
textarea {{ width: 100%; height: 200px; background: #1e293b; color: #e2e8f0; border: 1px solid #334155; border-radius: 8px; padding: 12px; font-family: monospace; font-size: 14px; resize: vertical; }}
.btn {{ background: #38bdf8; color: #0f172a; border: none; padding: 10px 24px; border-radius: 6px; cursor: pointer; font-weight: bold; margin: 5px; }}
.btn:hover {{ background: #0ea5e9; }}
.output {{ background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 12px; margin-top: 15px; white-space: pre-wrap; font-family: monospace; min-height: 100px; overflow-x: auto; }}
.error {{ color: #ef4444; }}
.success {{ color: #10b981; }}
.ad {{ background: linear-gradient(135deg, #1e293b, #334155); padding: 20px; border-radius: 12px; text-align: center; margin: 30px 0; border: 1px solid #475569; }}
.ad a {{ color: #fbbf24; text-decoration: none; font-weight: bold; }}
.back {{ color: #94a3b8; text-decoration: none; }}
.back:hover {{ color: #38bdf8; }}
</style>
</head>
<body>
<div class="container">
<h1>🔧 {name}</h1>
<p>{desc}</p>
<textarea id="input" placeholder="الصق JSON هنا..."></textarea><br>
<button class="btn" onclick="format()">تنسيق Pretty</button>
<button class="btn" onclick="minify()">ضغط Minify</button>
<button class="btn" onclick="validate()">تحقق Validate</button>
<button class="btn" onclick="copyOut()">نسخ النتيجة</button>
<div id="output" class="output">النتيجة تظهر هنا...</div>
<div class="ad">
<p>🚀 اكتشف المزيد من الأدوات</p>
<a href="{AD_LINK}" target="_blank" rel="nofollow noopener">اضغط هنا للاستفادة من العرض المميز</a>
</div>
<a href="../index.html" class="back">← العودة للرئيسية</a>
</div>
<script>
function format() {{
  try {{
    const obj = JSON.parse(document.getElementById('input').value);
    document.getElementById('output').textContent = JSON.stringify(obj, null, 2);
    document.getElementById('output').className = 'output success';
  }} catch(e) {{ document.getElementById('output').textContent = '❌ خطأ: ' + e.message; document.getElementById('output').className = 'output error'; }}
}}
function minify() {{
  try {{
    const obj = JSON.parse(document.getElementById('input').value);
    document.getElementById('output').textContent = JSON.stringify(obj);
    document.getElementById('output').className = 'output success';
  }} catch(e) {{ document.getElementById('output').textContent = '❌ خطأ: ' + e.message; document.getElementById('output').className = 'output error'; }}
}}
function validate() {{
  try {{
    JSON.parse(document.getElementById('input').value);
    document.getElementById('output').textContent = '✅ JSON صالح تماماً'; document.getElementById('output').className = 'output success';
  }} catch(e) {{ document.getElementById('output').textContent = '❌ خطأ: ' + e.message; document.getElementById('output').className = 'output error'; }}
}}
function copyOut() {{
  const t = document.getElementById('output').textContent;
  navigator.clipboard.writeText(t).then(() => alert('تم النسخ!'));
}}
</script>
</body>
</html>'''

def tool_base64(name, desc):
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>{name}</title>
<style>
body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: #0f172a; color: #e2e8f0; margin: 0; padding: 20px; }}
.container {{ max-width: 800px; margin: 0 auto; }}
h1 {{ color: #38bdf8; }}
textarea {{ width: 100%; height: 150px; background: #1e293b; color: #e2e8f0; border: 1px solid #334155; border-radius: 8px; padding: 12px; font-family: monospace; font-size: 14px; }}
.btn {{ background: #38bdf8; color: #0f172a; border: none; padding: 10px 24px; border-radius: 6px; cursor: pointer; font-weight: bold; margin: 5px; }}
.btn:hover {{ background: #0ea5e9; }}
.output {{ background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 12px; margin-top: 15px; white-space: pre-wrap; font-family: monospace; min-height: 80px; word-break: break-all; }}
.ad {{ background: linear-gradient(135deg, #1e293b, #334155); padding: 20px; border-radius: 12px; text-align: center; margin: 30px 0; border: 1px solid #475569; }}
.ad a {{ color: #fbbf24; text-decoration: none; font-weight: bold; }}
.back {{ color: #94a3b8; text-decoration: none; }}
</style>
</head>
<body>
<div class="container">
<h1>🔧 {name}</h1>
<p>{desc}</p>
<textarea id="input" placeholder="أدخل النص أو Base64 هنا..."></textarea><br>
<button class="btn" onclick="encode()">تشفير Encode</button>
<button class="btn" onclick="decode()">فك تشفير Decode</button>
<button class="btn" onclick="copyOut()">نسخ</button>
<div id="output" class="output">النتيجة تظهر هنا...</div>
<div class="ad">
<p>🚀 اكتشف المزيد من الأدوات</p>
<a href="{AD_LINK}" target="_blank" rel="nofollow noopener">اضغط هنا للاستفادة من العرض المميز</a>
</div>
<a href="../index.html" class="back">← العودة للرئيسية</a>
</div>
<script>
function encode() {{
  const t = document.getElementById('input').value;
  try {{ document.getElementById('output').textContent = btoa(unescape(encodeURIComponent(t))); }}
  catch(e) {{ document.getElementById('output').textContent = '❌ خطأ: ' + e.message; }}
}}
function decode() {{
  const t = document.getElementById('input').value;
  try {{ document.getElementById('output').textContent = decodeURIComponent(escape(atob(t))); }}
  catch(e) {{ document.getElementById('output').textContent = '❌ خطأ: ' + e.message; }}
}}
function copyOut() {{
  navigator.clipboard.writeText(document.getElementById('output').textContent).then(() => alert('تم النسخ!'));
}}
</script>
</body>
</html>'''

def tool_url_encoder(name, desc):
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>{name}</title>
<style>
body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: #0f172a; color: #e2e8f0; margin: 0; padding: 20px; }}
.container {{ max-width: 800px; margin: 0 auto; }}
h1 {{ color: #38bdf8; }}
textarea {{ width: 100%; height: 120px; background: #1e293b; color: #e2e8f0; border: 1px solid #334155; border-radius: 8px; padding: 12px; font-family: monospace; }}
.btn {{ background: #38bdf8; color: #0f172a; border: none; padding: 10px 24px; border-radius: 6px; cursor: pointer; font-weight: bold; margin: 5px; }}
.output {{ background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 12px; margin-top: 15px; white-space: pre-wrap; font-family: monospace; word-break: break-all; }}
.ad {{ background: linear-gradient(135deg, #1e293b, #334155); padding: 20px; border-radius: 12px; text-align: center; margin: 30px 0; border: 1px solid #475569; }}
.ad a {{ color: #fbbf24; text-decoration: none; font-weight: bold; }}
.back {{ color: #94a3b8; text-decoration: none; }}
</style>
</head>
<body>
<div class="container">
<h1>🔧 {name}</h1>
<p>{desc}</p>
<textarea id="input" placeholder="أدخل النص أو الرابط هنا..."></textarea><br>
<button class="btn" onclick="enc()">تشفير URL Encode</button>
<button class="btn" onclick="dec()">فك تشفير URL Decode</button>
<button class="btn" onclick="copyOut()">نسخ</button>
<div id="output" class="output">النتيجة تظهر هنا...</div>
<div class="ad">
<p>🚀 اكتشف المزيد من الأدوات</p>
<a href="{AD_LINK}" target="_blank" rel="nofollow noopener">اضغط هنا للاستفادة من العرض المميز</a>
</div>
<a href="../index.html" class="back">← العودة للرئيسية</a>
</div>
<script>
function enc() {{ document.getElementById('output').textContent = encodeURIComponent(document.getElementById('input').value); }}
function dec() {{ document.getElementById('output').textContent = decodeURIComponent(document.getElementById('input').value); }}
function copyOut() {{ navigator.clipboard.writeText(document.getElementById('output').textContent).then(() => alert('تم النسخ!')); }}
</script>
</body>
</html>'''

def tool_password_generator(name, desc):
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>{name}</title>
<style>
body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: #0f172a; color: #e2e8f0; margin: 0; padding: 20px; }}
.container {{ max-width: 700px; margin: 0 auto; }}
h1 {{ color: #38bdf8; }}
.controls {{ background: #1e293b; padding: 20px; border-radius: 12px; margin: 20px 0; border: 1px solid #334155; }}
label {{ display: block; margin: 10px 0; }}
input[type="number"], input[type="text"] {{ background: #0f172a; color: #e2e8f0; border: 1px solid #334155; padding: 8px; border-radius: 6px; width: 80px; }}
input[type="checkbox"] {{ margin-left: 8px; transform: scale(1.2); }}
.btn {{ background: #38bdf8; color: #0f172a; border: none; padding: 12px 32px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 1.1rem; }}
.btn:hover {{ background: #0ea5e9; }}
.output {{ background: #1e293b; border: 2px solid #38bdf8; border-radius: 8px; padding: 16px; margin-top: 20px; font-family: monospace; font-size: 1.3rem; text-align: center; word-break: break-all; }}
.strength {{ margin-top: 10px; padding: 8px; border-radius: 6px; text-align: center; font-weight: bold; }}
.ad {{ background: linear-gradient(135deg, #1e293b, #334155); padding: 20px; border-radius: 12px; text-align: center; margin: 30px 0; border: 1px solid #475569; }}
.ad a {{ color: #fbbf24; text-decoration: none; font-weight: bold; }}
.back {{ color: #94a3b8; text-decoration: none; }}
</style>
</head>
<body>
<div class="container">
<h1>🔐 {name}</h1>
<p>{desc}</p>
<div class="controls">
<label>الطول: <input type="number" id="len" value="16" min="4" max="128"></label>
<label><input type="checkbox" id="upper" checked> أحرف كبيرة (A-Z)</label>
<label><input type="checkbox" id="lower" checked> أحرف صغيرة (a-z)</label>
<label><input type="checkbox" id="nums" checked> أرقام (0-9)</label>
<label><input type="checkbox" id="symb" checked> رموز (!@#$...)</label>
<button class="btn" onclick="gen()">توليد كلمة مرور</button>
</div>
<div id="output" class="output">اضغط "توليد" لإنشاء كلمة مرور</div>
<div id="strength" class="strength"></div>
<div class="ad">
<p>🚀 اكتشف المزيد من الأدوات</p>
<a href="{AD_LINK}" target="_blank" rel="nofollow noopener">اضغط هنا للاستفادة من العرض المميز</a>
</div>
<a href="../index.html" class="back">← العودة للرئيسية</a>
</div>
<script>
function gen() {{
  const len = parseInt(document.getElementById('len').value);
  const u = document.getElementById('upper').checked;
  const l = document.getElementById('lower').checked;
  const n = document.getElementById('nums').checked;
  const s = document.getElementById('symb').checked;
  let chars = '';
  if (u) chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  if (l) chars += 'abcdefghijklmnopqrstuvwxyz';
  if (n) chars += '0123456789';
  if (s) chars += '!@#$%^&*()_+-=[]{{}}|;:,.<>?';
  if (!chars) {{ alert('اختر نوعاً واحداً على الأقل'); return; }}
  let pass = '';
  for (let i = 0; i < len; i++) pass += chars.charAt(Math.floor(Math.random() * chars.length));
  document.getElementById('output').textContent = pass;
  navigator.clipboard.writeText(pass);
  // Strength
  let score = 0;
  if (len >= 12) score++; if (len >= 16) score++;
  if (u && l) score++; if (n) score++; if (s) score++;
  const el = document.getElementById('strength');
  const labels = ['ضعيفة جداً', 'ضعيفة', 'متوسطة', 'قوية', 'قوية جداً', 'ممتازة'];
  const colors = ['#ef4444','#f97316','#eab308','#84cc16','#22c55e','#10b981'];
  el.textContent = 'القوة: ' + labels[score];
  el.style.background = colors[score] + '22';
  el.style.color = colors[score];
}}
</script>
</body>
</html>'''

def tool_color_converter(name, desc):
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>{name}</title>
<style>
body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: #0f172a; color: #e2e8f0; margin: 0; padding: 20px; }}
.container {{ max-width: 700px; margin: 0 auto; }}
h1 {{ color: #38bdf8; }}
input {{ background: #1e293b; color: #e2e8f0; border: 1px solid #334155; padding: 10px; border-radius: 6px; width: 200px; margin: 5px; }}
.btn {{ background: #38bdf8; color: #0f172a; border: none; padding: 10px 24px; border-radius: 6px; cursor: pointer; font-weight: bold; margin: 5px; }}
.preview {{ width: 100%; height: 100px; border-radius: 12px; margin: 20px 0; border: 2px solid #334155; transition: background 0.3s; }}
.output {{ background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 16px; margin-top: 15px; font-family: monospace; }}
.ad {{ background: linear-gradient(135deg, #1e293b, #334155); padding: 20px; border-radius: 12px; text-align: center; margin: 30px 0; border: 1px solid #475569; }}
.ad a {{ color: #fbbf24; text-decoration: none; font-weight: bold; }}
.back {{ color: #94a3b8; text-decoration: none; }}
</style>
</head>
<body>
<div class="container">
<h1>🎨 {name}</h1>
<p>{desc}</p>
<div>
<input id="hex" placeholder="#38bdf8" oninput="fromHex()">
<input id="rgb" placeholder="rgb(56,189,248)" oninput="fromRgb()">
<input id="hsl" placeholder="hsl(199,89%,60%)" oninput="fromHsl()">
</div>
<div id="preview" class="preview" style="background:#38bdf8;"></div>
<div id="output" class="output">
HEX: #38bdf8<br>
RGB: rgb(56, 189, 248)<br>
HSL: hsl(199, 89%, 60%)
</div>
<div class="ad">
<p>🚀 اكتشف المزيد من الأدوات</p>
<a href="{AD_LINK}" target="_blank" rel="nofollow noopener">اضغط هنا للاستفادة من العرض المميز</a>
</div>
<a href="../index.html" class="back">← العودة للرئيسية</a>
</div>
<script>
function fromHex() {{
  let h = document.getElementById('hex').value.trim();
  if (!h.match(/^#/)) h = '#' + h;
  if (!/^#[0-9A-Fa-f]{{6}}$/.test(h)) return;
  const r = parseInt(h.slice(1,3),16), g = parseInt(h.slice(3,5),16), b = parseInt(h.slice(5,7),16);
  update(r,g,b,h);
}}
function fromRgb() {{
  const m = document.getElementById('rgb').value.match(/(\\d+),\\s*(\\d+),\\s*(\\d+)/);
  if (!m) return;
  update(parseInt(m[1]), parseInt(m[2]), parseInt(m[3]));
}}
function fromHsl() {{
  const m = document.getElementById('hsl').value.match(/(\\d+),\\s*(\\d+)%,\\s*(\\d+)%/);
  if (!m) return;
  let h=parseInt(m[1])/360, s=parseInt(m[2])/100, l=parseInt(m[3])/100;
  let r,g,b;
  if (s === 0) {{ r = g = b = l; }} else {{
    const hue2rgb = (p,q,t) => {{ if(t<0) t+=1; if(t>1) t-=1; if(t<1/6) return p+(q-p)*6*t; if(t<1/2) return q; if(t<2/3) return p+(q-p)*(2/3-t)*6; return p; }};
    const q = l < 0.5 ? l * (1 + s) : l + s - l * s;
    const p = 2 * l - q;
    r = hue2rgb(p, q, h + 1/3); g = hue2rgb(p, q, h); b = hue2rgb(p, q, h - 1/3);
  }}
  update(Math.round(r*255), Math.round(g*255), Math.round(b*255));
}}
function update(r,g,b,hex=null) {{
  const h = hex || '#' + [r,g,b].map(x => x.toString(16).padStart(2,'0')).join('');
  const hsl = rgbToHsl(r,g,b);
  document.getElementById('hex').value = h;
  document.getElementById('rgb').value = `rgb(${{r}}, ${{g}}, ${{b}})`;
  document.getElementById('hsl').value = `hsl(${{hsl.h}}, ${{hsl.s}}%, ${{hsl.l}}%)`;
  document.getElementById('preview').style.background = h;
  document.getElementById('output').innerHTML = `HEX: ${{h}}<br>RGB: rgb(${{r}}, ${{g}}, ${{b}})<br>HSL: hsl(${{hsl.h}}, ${{hsl.s}}%, ${{hsl.l}}%)`;
}}
function rgbToHsl(r,g,b) {{
  r/=255; g/=255; b/=255;
  const max=Math.max(r,g,b), min=Math.min(r,g,b);
  let h,s,l=(max+min)/2;
  if (max===min) {{ h=s=0; }} else {{
    const d=max-min; s=l>0.5?d/(2-max-min):d/(max+min);
    switch(max){{ case r:h=(g-b)/d+(g<b?6:0);break; case g:h=(b-r)/d+2;break; case b:h=(r-g)/d+4;break; }}
    h/=6;
  }}
  return {{h:Math.round(h*360),s:Math.round(s*100),l:Math.round(l*100)}};
}}
</script>
</body>
</html>'''

def tool_unit_converter(name, desc):
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>{name}</title>
<style>
body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: #0f172a; color: #e2e8f0; margin: 0; padding: 20px; }}
.container {{ max-width: 700px; margin: 0 auto; }}
h1 {{ color: #38bdf8; }}
select, input {{ background: #1e293b; color: #e2e8f0; border: 1px solid #334155; padding: 10px; border-radius: 6px; margin: 5px; font-size: 1rem; }}
.btn {{ background: #38bdf8; color: #0f172a; border: none; padding: 10px 24px; border-radius: 6px; cursor: pointer; font-weight: bold; }}
.output {{ background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 20px; margin-top: 20px; font-size: 1.2rem; text-align: center; }}
.ad {{ background: linear-gradient(135deg, #1e293b, #334155); padding: 20px; border-radius: 12px; text-align: center; margin: 30px 0; border: 1px solid #475569; }}
.ad a {{ color: #fbbf24; text-decoration: none; font-weight: bold; }}
.back {{ color: #94a3b8; text-decoration: none; }}
</style>
</head>
<body>
<div class="container">
<h1>📏 {name}</h1>
<p>{desc}</p>
<div>
<input type="number" id="val" value="1" step="any">
<select id="from">
<option value="m">متر (m)</option><option value="km">كيلومتر (km)</option><option value="cm">سنتيمتر (cm)</option>
<option value="mm">مليمتر (mm)</option><option value="ft">قدم (ft)</option><option value="in">بوصة (in)</option>
<option value="yd">ياردة (yd)</option><option value="mi">ميل (mi)</option>
</select>
<select id="to">
<option value="km">كيلومتر (km)</option><option value="m" selected>متر (m)</option><option value="cm">سنتيمتر (cm)</option>
<option value="mm">مليمتر (mm)</option><option value="ft">قدم (ft)</option><option value="in">بوصة (in)</option>
<option value="yd">ياردة (yd)</option><option value="mi">ميل (mi)</option>
</select>
<button class="btn" onclick="convert()">تحويل</button>
</div>
<div id="output" class="output">أدخل قيمة واضغط تحويل</div>
<div class="ad">
<p>🚀 اكتشف المزيد من الأدوات</p>
<a href="{AD_LINK}" target="_blank" rel="nofollow noopener">اضغط هنا للاستفادة من العرض المميز</a>
</div>
<a href="../index.html" class="back">← العودة للرئيسية</a>
</div>
<script>
const rates = {{ m:1, km:1000, cm:0.01, mm:0.001, ft:0.3048, in:0.0254, yd:0.9144, mi:1609.34 }};
function convert() {{
  const v = parseFloat(document.getElementById('val').value);
  const f = document.getElementById('from').value;
  const t = document.getElementById('to').value;
  if (isNaN(v)) {{ document.getElementById('output').textContent = 'أدخل رقماً صحيحاً'; return; }}
  const m = v * rates[f];
  const res = m / rates[t];
  document.getElementById('output').textContent = v + ' ' + f + ' = ' + res.toFixed(6) + ' ' + t;
}}
</script>
</body>
</html>'''

def tool_word_counter(name, desc):
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>{name}</title>
<style>
body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: #0f172a; color: #e2e8f0; margin: 0; padding: 20px; }}
.container {{ max-width: 800px; margin: 0 auto; }}
h1 {{ color: #38bdf8; }}
textarea {{ width: 100%; height: 250px; background: #1e293b; color: #e2e8f0; border: 1px solid #334155; border-radius: 8px; padding: 12px; font-size: 1rem; }}
.stats {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 15px; margin-top: 20px; }}
.stat-box {{ background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 16px; text-align: center; }}
.stat-box .num {{ font-size: 2rem; font-weight: bold; color: #38bdf8; }}
.stat-box .label {{ color: #94a3b8; font-size: 0.9rem; margin-top: 5px; }}
.ad {{ background: linear-gradient(135deg, #1e293b, #334155); padding: 20px; border-radius: 12px; text-align: center; margin: 30px 0; border: 1px solid #475569; }}
.ad a {{ color: #fbbf24; text-decoration: none; font-weight: bold; }}
.back {{ color: #94a3b8; text-decoration: none; }}
</style>
</head>
<body>
<div class="container">
<h1>📝 {name}</h1>
<p>{desc}</p>
<textarea id="text" placeholder="اكتب أو الصق النص هنا..." oninput="count()"></textarea>
<div class="stats">
<div class="stat-box"><div class="num" id="words">0</div><div class="label">كلمات</div></div>
<div class="stat-box"><div class="num" id="chars">0</div><div class="label">أحرف</div></div>
<div class="stat-box"><div class="num" id="charsNoSpace">0</div><div class="label">بدون مسافات</div></div>
<div class="stat-box"><div class="num" id="sentences">0</div><div class="label">جمل</div></div>
<div class="stat-box"><div class="num" id="paragraphs">0</div><div class="label">فقرات</div></div>
<div class="stat-box"><div class="num" id="reading">0</div><div class="label">دقيقة قراءة</div></div>
</div>
<div class="ad">
<p>🚀 اكتشف المزيد من الأدوات</p>
<a href="{AD_LINK}" target="_blank" rel="nofollow noopener">اضغط هنا للاستفادة من العرض المميز</a>
</div>
<a href="../index.html" class="back">← العودة للرئيسية</a>
</div>
<script>
function count() {{
  const t = document.getElementById('text').value;
  document.getElementById('chars').textContent = t.length;
  document.getElementById('charsNoSpace').textContent = t.replace(/\\s/g, '').length;
  const words = t.trim() === '' ? 0 : t.trim().split(/\\s+/).length;
  document.getElementById('words').textContent = words;
  const sentences = t.split(/[.!?]+/).filter(s => s.trim().length > 0).length;
  document.getElementById('sentences').textContent = sentences;
  const paragraphs = t.split('\\n').filter(p => p.trim().length > 0).length;
  document.getElementById('paragraphs').textContent = paragraphs;
  document.getElementById('reading').textContent = Math.ceil(words / 200) || 0;
}}
</script>
</body>
</html>'''

def tool_lorem_ipsum(name, desc):
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>{name}</title>
<style>
body {{ font-family: 'Segoe UI', system-ui, sans-serif; background: #0f172a; color: #e2e8f0; margin: 0; padding: 20px; }}
.container {{ max-width: 800px; margin: 0 auto; }}
h1 {{ color: #38bdf8; }}
.controls {{ background: #1e293b; padding: 20px; border-radius: 12px; margin: 20px 0; border: 1px solid #334155; }}
label {{ display: inline-block; margin: 8px 15px; }}
input[type="number"] {{ background: #0f172a; color: #e2e8f0; border: 1px solid #334155; padding: 6px; border-radius: 6px; width: 70px; }}
.btn {{ background: #38bdf8; color: #0f172a; border: none; padding: 10px 24px; border-radius: 6px; cursor: pointer; font-weight: bold; margin: 5px; }}
.output {{ background: #1e293b; border: 1px solid #334155; border-radius: 8px; padding: 16px; margin-top: 15px; line-height: 1.8; }}
.ad {{ background: linear-gradient(135deg, #1e293b, #334155); padding: 20px; border-radius: 12px; text-align: center; margin: 30px 0; border: 1px solid #475569; }}
.ad a {{ color: #fbbf24; text-decoration: none; font-weight: bold; }}
.back {{ color: #94a3b8; text-decoration: none; }}
</style>
</head>
<body>
<div class="container">
<h1>✍️ {name}</h1>
<p>{desc}</p>
<div class="controls">
<label>فقرات: <input type="number" id="paras" value="3" min="1" max="50"></label>
<label>كلمات/فقرة: <input type="number" id="words" value="50" min="10" max="200"></label>
<label><input type="checkbox" id="html" checked> تضمين HTML</label>
<button class="btn" onclick="generate()">توليد</button>
<button class="btn" onclick="copyOut()">نسخ</button>
</div>
<div id="output" class="output">اضغط "توليد" لإنشاء نص...</div>
<div class="ad">
<p>🚀 اكتشف المزيد من الأدوات</p>
<a href="{AD_LINK}" target="_blank" rel="nofollow noopener">اضغط هنا للاستفادة من العرض المميز</a>
</div>
<a href="../index.html" class="back">← العودة للرئيسية</a>
</div>
<script>
const words = ["لوريم","إيبسوم","دولار","سيت","أميت","كونسيكتيتور","أدايبيسيسينغ","إيليت","سيد","دو","إيوسمود","تيمبور","إنكيديدونت","يوت","لابور","إت","دولور","ماغنا","أليكا","يوت","إنيم","أد","مينيم","فينيام","كويس","نوسترود","إكسيرسيتاشين","يوللامكو","لابوريس","نيسي","يوت","أليكوب","إكس","إي","كومودو","كونسيكوات","دويس","أوتي","إيرور","دولور","إن","ريبرهينديريت","إن","فولوبتاتي","فيليت","إيسي","سيلوم","دولوري","يو","فيغيات","نولا","بارياتور","إكسيبتيور","سينت","أوكايكات","كيوبيداتات","نون","برويدينت","س
