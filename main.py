#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Empire Web Engine v3 — Global Edition
500 Real Functional Tools (HTML+CSS+JS) + Infinite Bilingual Articles
"""

import json
import os
import random
import hashlib
from datetime import datetime
from pathlib import Path

# ===================== CONFIG =====================
TOOLS_DIR = Path("./tools")
ARTICLES_DIR = Path("./articles")
DB_FILE = Path("./database.json")
MAX_TOOLS = 500
TOOLS_PER_CYCLE = 5
ARTICLES_PER_CYCLE = 2  # 1 AR + 1 EN
AD_LINK = "https://omg10.com/4/11349784"

# ===================== LANG DATA =====================
TOOL_PREFIXES = [
    "Smart","Pro","Ultra","Mega","Quick","Auto","Easy","Super","Fast","Instant",
    "Advanced","Dynamic","Global","Prime","Elite","Hyper","Nano","Cyber","Tech",
    "Cloud","Digital","Net","Web","Code","Data","Pixel","Byte","Core","Alpha",
    "Beta","Sigma","Omega","Delta","Gamma","Neo","Meta","Crypto","Quantum","AI",
    "Bot","Sync","Flux","Spark","Pulse","Wave","Nexus","Vertex","Horizon","Zenith"
]

TOOL_SUFFIXES = [
    "JSON Formatter","Base64 Tool","URL Encoder","Password Generator","Color Studio",
    "Unit Converter","Word Counter","Lorem Generator","QR Maker","Markdown Editor",
    "CSS Minifier","HTML Entities","Hash Generator","Case Converter","CSV Converter",
    "Image Base64","Base64 Image","Diff Checker","Regex Tester","Base Converter",
    "Percentage Calc","Loan Calculator","BMI Calculator","Age Calculator","Stopwatch",
    "Countdown Timer","Pomodoro","Random Number","UUID Maker","Slug Generator",
    "Duplicate Remover","Line Sorter","Text Reverser","Palindrome Check","IP Validator",
    "Email Checker","Card Validator","Barcode Maker","Morse Translator","Cipher Tool",
    "Binary Converter","Hex Converter","HTML Previewer","Shadow Generator","Flexbox Builder",
    "Gradient Maker","Radius Generator","Aspect Calc","Screen Info","Browser Stats",
    "Meta Generator","Robots Builder","Sitemap Maker","Twitter Card","OG Generator",
    "Favicon Maker","Placeholder Img","Meme Creator","Image Resizer","ASCII Art",
    "Typing Test","World Clock","Timezone Calc","Date Diff","Days Counter",
    "Invoice Maker","Receipt Builder","Password Check","Username Gen","Business Card",
    "Resume Builder","JSON Path","XML Formatter","YAML Parser","SQL Formatter",
    "Cron Parser","Timestamp Conv","Unix Time","Palette Gen","Fake Data",
    "API Tester","HTTP Builder","JWT Decoder","Table Maker","Chart Builder",
    "Mind Mapper","Flowchart","Certificate","Badge Maker","Leaderboard",
    "Quiz Builder","Poll Maker","Survey Tool","Todo List","Kanban Board",
    "Habit Tracker","Expense Log","Budget Planner","Pomodoro Pro","Focus Timer",
    "Tip Calculator","Split Bill","Tax Calculator","VAT Calc","ROI Calculator",
    "Currency Conv","Fuel Calc","Trip Planner","Mileage Log","Calendar Gen",
    "Prime Check","Fibonacci","Factorial","GCD LCM","Equation Solver",
    "Matrix Calc","Vector Calc","Stats Calc","Probability","Fraction Calc",
    "Ratio Calc","Root Calc","Log Calc","Trig Calc","Circle Calc",
    "Triangle Solver","Distance Calc","Slope Calc","Compound Interest","Retirement Calc",
    "Mortgage Calc","Car Loan","Savings Calc","Investment","Break-even",
    "Ohm Law","Power Calc","Resistor Calc","LED Resistor","Antenna Calc",
    "Subnet Calc","IP Subnet","CIDR Calc","Binary Calc","IPv6 Calc",
    "Hash MD5","Hash SHA1","Hash SHA256","Hash SHA512","Checksum",
    "Password Hash","HMAC Generator","UUID v4","UUID v5","NanoID",
    "Token Generator","Key Generator","CSR Generator","PEM Parser","SSL Checker",
    "Port Scanner","DNS Lookup","Whois Lookup","IP Geolocation","Blacklist Check",
    "URL Parser","URL Expander","Redirect Check","Header Check","SSL Info",
    "Cipher AES","Cipher DES","Cipher RSA","Cipher Blowfish","Steganography",
    "File Hash","String Hash","Compare Hash","Verify Hash","Hash Cracker",
    "Hex Editor","Bin Editor","Dec Editor","Oct Editor","Base32",
    "Base58","Base85","UUEncode","XXEncode","Quoted Printable",
    "Punycode","IDN Converter","URL Slug","URL Shortener","Deep Link",
    "UTM Builder","Campaign URL","Affiliate Link","Share Link","Embed Code",
    "Iframe Generator","Object Embed","PDF Embed","Audio Embed","Video Embed",
    "Playlist Maker","RSS Feed","Atom Feed","Sitemap XML","Sitemap HTML",
    "Breadcrumb","Pagination","Tag Cloud","Archive List","Calendar Widget",
    "Clock Widget","Counter Widget","Timer Widget","Progress Bar","Loading Spinner",
    "Skeleton Screen","Placeholder Text","Dummy Image","Avatar Generator","Identicon",
    "Robohash","Dice Bear","Gravatar URL","Profile Card","Social Card",
    "Preview Card","Link Preview","Rich Snippet","Schema Markup","Microdata",
    "RDFa Generator","JSON-LD Gen","Open Graph","Twitter Card","WhatsApp Share",
    "Facebook Share","LinkedIn Share","Pinterest Pin","Reddit Share","Telegram Share",
    "Email Share","SMS Share","QR Share","NFC Tag","Deep Link Gen",
    "App Link","Universal Link","Intent URL","Custom Scheme","WebAPK",
    "PWA Manifest","Service Worker","App Shell","Splash Screen","Theme Color",
    "Icon Generator","Maskable Icon","Adaptive Icon","Notification Icon","Badge Icon",
    "Shortcut Icon","Apple Touch","Favicon ICO","Favicon SVG","Favicon PNG",
    "Windows Tile","Safari Pin","Chrome Theme","Firefox Theme","Edge Theme",
    "Opera Theme","Vivaldi Theme","Brave Theme","Arc Theme","Safari Theme"
]

CATEGORIES = [
    "Developer","Designer","SEO","Security","Productivity",
    "Converter","Calculator","Analyzer","Generator","Formatter",
    "Tester","Monitor","Optimizer","Utility","Math"
]

AR_TOPICS = [
    "الذكاء الاصطناعي","التعلم الآلي","الحوسبة السحابية","الأمن السيبراني","تطوير التطبيقات",
    "تصميم المواقع","تحسين محركات البحث","التسويق الرقمي","التجارة الإلكترونية","إنترنت الأشياء",
    "البلوكتشين","العملات الرقمية","الحوسبة الكمية","الواقع المعزز","الواقع الافتراضي",
    "الروبوتات","الأتمتة","DevOps","الحاويات","APIs",
    "الرسوميات ثلاثية الأبعاد","معالجة اللغات الطبيعية","رؤية الحاسوب","الشبكات العصبية","التعلم العميق",
    "نمذجة البيانات","تحليل البيانات","علم البيانات","هندسة البيانات","أنظمة التوصية",
    "الشات بوتات","المساعدات الصوتية","التعرف على الكلام","التعرف على الوجوه","التحليلات التنبؤية",
    "إدارة المشاريع","العمل عن بُعد","الأدوات التعاونية","التخزين السحابي","النسخ الاحتياطي",
    "استعادة البيانات","مراقبة الأنظمة","سجلات الأحداث","إدارة الهوية","التحقق الثنائي",
    "التشفير","شهادات SSL","جدران الحماية","اختبار الاختراق","البحث عن الثغرات",
    "إدارة التصحيحات","الامتثال","حماية الخصوصية","GDPR","CCPA",
    "إدارة المخاطر","الاستمرارية","التعافي من الكوارث","توفر عالي","موازنة الحمل",
    "التخزين المؤقت","شبكات توصيل المحتوى","التسريع","ضغط البيانات","تحسين الصور",
    "التنسيقات الحديثة","الرسوميات المتجهة","الخطوط","الألوان","التباين",
    "إمكانية الوصول","تجربة المستخدم","واجهة المستخدم","التصميم المتجاوب","التصميم التكيفي",
    "الوضع المظلم","الرسوم المتحركة","التفاعلية","التصميم بدون كود","المنصات منخفضة الكود",
    "أتمتة سير العمل","التكامل","الويب هوك","زابير","ماك",
    "إنتجريت","أتمتة التسويق","إدارة علاقات العملاء","أنظمة ERP","إدارة الموارد",
    "التخطيط المالي","المحاسبة السحابية","الفواتير الإلكترونية","المدفوعات الرقمية","المحافظ الإلكترونية",
    "التحويلات الدولية","إدارة المخزون","سلسلة التوريد","الخدمات اللوجستية","تتبع الشحنات",
    "إدارة المستودعات","الجرد","الباركود","QR","RFID",
    "GPS","GIS","الخرائط الرقمية","التنقل","تحليل الموقع",
    "الجغرافيا","المدن الذكية","الطاقة المتجددة","الكفاءة الطاقية","البيئة",
    "الاستدامة","الاقتصاد الدائري","إعادة التدوير","المواد الخام","الطباعة ثلاثية الأبعاد",
    "الصناعة 4.0","التوأم الرقمي","المحاكاة","النماذج الأولية","الاختبار السريع",
    "التصميم التكراري","المنهجية الرشيقة","سكروم","كانبان","سداسي",
    "تطوير البرمجيات","البرمجة","الخوارزميات","هياكل البيانات","أنظمة التشغيل",
    "قواعد البيانات","SQL","NoSQL","NewSQL","قواعد البيانات الرسمية",
    "الرسوميات","الشبكات","بروتوكولات الإنترنت","TCP/IP","HTTP/3",
    "QUIC","WebSockets","gRPC","GraphQL","REST",
    "SOAP","XML","JSON","YAML","TOML",
    "INI","CSV","Parquet","ORC","Avro",
    "Protocol Buffers","Thrift","MessagePack","BSON","CBOR",
    "FlexBuffers","FlatBuffers","Cap'n Proto","ZeroMQ","RabbitMQ",
    "Kafka","Pulsar","Redis","Memcached","Cassandra",
    "MongoDB","DynamoDB","Firestore","Cosmos DB","CockroachDB",
    "TiDB","YugabyteDB","PlanetScale","Neon","Supabase",
    "Hasura","Prisma","Drizzle","TypeORM","Sequelize",
    "Mongoose","SQLAlchemy","Django ORM","Active Record","Hibernate",
    "Entity Framework","Dapper","NHibernate","MyBatis","jOOQ",
    "QueryDSL","JPA","JDBC","ODBC","ADO.NET",
    "PDO","mysqli","pg_query","sqlite3","LevelDB",
    "RocksDB","LMDB","Berkeley DB","Kyoto Cabinet","Tokyo Cabinet",
    "Tkrzw","UnQLite","Vedis","EJDB","Upscaledb",
    "ForestDB","Couchbase Lite","Realm","ObjectBox","Room",
    "Core Data","SQLite.swift","GRDB","FMDB","WCDB",
    "GreenDAO","SugarORM","ActiveAndroid","ORMLite","DBFlow",
    "Requery","SQLDelight","Exposed","Ktorm","Jdbi",
    "Spring Data","Micronaut Data","Quarkus Hibernate","Panache","ActiveJPA",
    "Ebean","JOOQ","Querydsl","MyBatis-Plus","TkMyBatis",
    "Fluent MyBatis","Custom Mapper","通用Mapper","MP","MyBatis-Flex",
    "MyBatis-Plus-Join","MyBatisX","MyBatis-Plus-Generator","代码生成器","逆向工程",
    "scaffolding","脚手架","模板引擎","Thymeleaf","FreeMarker",
    "Velocity","JSP","JSTL","Facelets","JSF",
    "PrimeFaces","RichFaces","IceFaces","MyFaces","Tomahawk",
    "Trinidad","Tobago","Portlet Bridge","Spring Faces","Spring Web Flow",
    "Web Flow","Flow","State Machine","Spring Statemachine","Squirrel",
    "Stateless4j","Easy States","State Machine","Mason","Stateless",
    "Automaton","JState","StateJ","State","Transition",
    "Event","Action","Guard","Context","State Pattern",
    "Strategy Pattern","Command Pattern","Observer Pattern","Pub/Sub","Event Sourcing",
    "CQRS","Event Store","Axon","Eventuate","NEventStore",
    "Marten","Streamstone","SQLStreamStore","GetEventStore","EventStoreDB",
    "LiteDB","RavenDB","Voron","Esent","Rocks",
    "FASTER","Trill","StreamInsight","Reactive Extensions","RxJava",
    "RxJS","RxSwift","RxKotlin","RxScala","RxRuby",
    "RxPHP","RxGo","RxRust","RxCpp","ReactiveUI",
    "Akka.NET","Akka","Vert.x","Quarkus","Micronaut",
    "Helidon","Ktor","Spring Boot","Spring Framework","Spring Cloud",
    "Spring Security","Spring Data","Spring Integration","Spring Batch","Spring Shell",
    "Spring HATEOAS","Spring REST Docs","Spring GraphQL","Spring Native","Spring WebFlux",
    "Project Reactor","RSocket","R2DBC","Spring R2DBC","Spring Cloud Gateway",
    "Spring Cloud Config","Eureka","Consul","Zookeeper","Nacos",
    "Etcd","Kubernetes","Docker","Podman","containerd",
    "CRI-O","Buildah","Skopeo","Kaniko","Jib",
    "Buildpacks","Cloud Native Buildpacks","Paketo","Heroku","Dokku",
    "Flynn","Deis","OpenShift","Rancher","K3s",
    "K3d","Kind","Minikube","MicroK8s","Docker Desktop",
    "Colima","Lima","Rancher Desktop","Podman Desktop","DevPod",
    "Gitpod","GitHub Codespaces","CodeSandbox","StackBlitz","Replit",
    "Glitch","CodePen","JSFiddle","JSBin","Plunker",
    "Dabblet","Liveweave","CSSDeck","Bootply","Runnable",
    "Codenvy","Cloud9","AWS Cloud9","Azure Cloud Shell","Google Cloud Shell",
    "Oracle Cloud Shell","IBM Cloud Shell","Alibaba Cloud Shell","Tencent Cloud Shell","Huawei Cloud Shell",
    "DigitalOcean Droplet","Linode","Vultr","Hetzner","UpCloud",
    "Scaleway","OVHcloud","Ionos","1&1","Namecheap",
    "GoDaddy","Bluehost","HostGator","SiteGround","DreamHost",
    "InMotion","A2 Hosting","GreenGeeks","HostPapa","iPage",
    "FatCow","JustHost","HostMonster","Netfirms","IPower",
    "Dotster","Domain.com","Register.com","Network Solutions","Enom",
    "Tucows","OpenSRS","ResellerClub","Name.com","NameSilo",
    "Porkbun","Dynadot","Google Domains","AWS Route 53","Cloudflare Registrar",
    "Azure DNS","Google Cloud DNS","DNSimple","NS1","Constellix",
    "Dyn","UltraDNS","EasyDNS","Hurricane Electric","DNS Made Easy",
    "ZoneEdit","No-IP","Dynu","FreeDNS","Afraid.org",
    "DuckDNS","YDNS","DNSExit","EntryDNS","Zonomi",
    "RcodeZero","CSC","MarkMonitor","BrandShelter","Safenames",
    "101domain","Gandi","OVH","GABIA","WhoisXML",
    "DomainTools","WHOIS","RDAP","IRIS","DAS",
    "Escrow","Aftermarket","Sedo","Afternic","Dan.com",
    "Uniregistry Market","BrandBucket","SquadHelp","Brandpa","Namerific",
    "Brandroot","Brandable","Atom","Novanym","Oyzta",
    "BrandDo","Brandwise","NamingForce","Crowdspring","99designs",
    "DesignCrowd","LogoMyWay","Hatchwise","ZillionDesigns","48hourslogo",
    "LogoTournament","LogoArena","Springboard","LogoLounge","Dribbble",
    "Behance","Coroflot","Portfoliobox","Carbonmade","Crevado",
    "Format","Squarespace","Wix","Weebly","Strikingly",
    "Tilda","Readymag","Webflow","Framer","Figma",
    "Sketch","Adobe XD","InVision","Proto.io","Marvel",
    "Principle","Flinto","Origami","Axure","Balsamiq",
    "Mockplus","ProtoPie","Kite","Lottie","Rive",
    "Haiku","Bodymovin","After Effects","Premiere Pro","DaVinci Resolve",
    "Final Cut Pro","Motion","Compressor","Cinema 4D","Blender",
    "Maya","3ds Max","Houdini","Nuke","Fusion",
    "Flame","Smoke","Mocha","Syntheyes","PFTrack",
    "Boujou","MatchMover","3DEqualizer","Autodesk","Adobe",
    "Maxon","SideFX","Foundry","Blackmagic Design","Apple",
    "Avid","Corel","Magix","CyberLink","Wondershare",
    "TechSmith","Camtasia","Snagit","Bandicam","OBS Studio",
    "Streamlabs","XSplit","vMix","Wirecast","Restream",
    "StreamYard","Melon","Riverside","SquadCast","Zencastr",
    "Anchor","Buzzsprout","Libsyn","Podbean","Transistor",
    "Captivate","Simplecast","Spreaker","SoundCloud","Mixcloud",
    "HearThis.at","Audiomack","Bandcamp","DistroKid","TuneCore",
    "CD Baby","LANDR","Amuse","RouteNote","ONErpm",
    "Symphonic","The Orchard","Believe","FUGA","Ditto Music",
    "ReverbNation","Soundrop","Level Music","UnitedMasters","Stem",
    "Vydia","Monstercat","Armada","Spinnin' Records","Anjunabeats",
    "A State of Trance","Above & Beyond","Armin van Buuren","Tiësto","Martin Garrix",
    "David Guetta","Calvin Harris","Swedish House Mafia","Alesso","Avicii",
    "Deadmau5","Skrillex","Diplo","Major Lazer","Jack Ü",
    "Zedd","Chainsmokers","Kygo","Alan Walker","Marshmello",
    "DJ Snake","Steve Aoki","Dimitri Vegas","Like Mike","Hardwell",
    "W&W","Afrojack","Nicky Romero","Sander van Doorn","Ferry Corsten",
    "Gareth Emery","Paul van Dyk","Paul Oakenfold","John Digweed","Sasha",
    "Carl Cox","Richie Hawtin","Adam Beyer","Nina Kraviz","Charlotte de Witte",
    "Amelie Lens","Peggy Gou","Helena Hauff","Annie Mac","Mary Anne Hobbs",
    "B.Traits","Maya Jane Coles","Jamie Jones","Seth Troxler","The Martinez Brothers",
    "Loco Dice","Marco Carola","Joseph Capriati","Maceo Plex","Tale of Us",
    "Mind Against","Afterlife","Drumcode","Klockworks","Ostgut Ton",
    "Berghain","Tresor","Watergate","About Blank","://about blank",
    "Sisyphos","Kater Blau","Else","Ritter Butzke","Gretchen",
    "KitKatClub","Insomnia","Tribehouse","Omen","Dorian Gray",
    "U60311","Cocoon","Amnesia","Pacha","Ushuaïa",
    "Hï Ibiza","DC-10","Privilege","Space","Sankeys",
    "Blue Marlin","Destino","Heart","Lío","Pacha",
    "Lio","Heart","Destino","Talamanca","Cala Jondal",
    "Es Cavallet","Las Salinas","Playa d'en Bossa","Figueretas","Cala Comte",
    "Cala Bassa","Cala Tarida","Cala d'Hort","Cala Vadella","Cala Carbo",
    "Cala Llentrisca","Cala d'en Serra","Portinatx","Sant Joan","Sant Antoni",
    "Santa Eulalia","Es Canar","Cala Llonga","S'Argamassa","Cala Pada",
    "Cala Martina","Es Figueral","Aigües Blanques","Cala Boix","Pou des Lleo",
    "Tagomago","Illa de es Vedrà","Sa Conillera","Illa des Bosc","S'Espalmador",
    "Formentera","La Savina","Es Pujols","Sant Francesc","El Pilar de la Mola",
    "Cap de Barbaria","Punta Rasa","Cala Saona","Migjorn","Es Arenals",
    "Es Calo","La Mola","Pilar","Es Pujols","La Savina",
    "Es Mal Pas","Es Marjals","Ses Salines","Es Trucadors","S'Alga",
    "Punta Prima","Cala en Baster","Cala Codolar","Platja de ses Illetes","Llevant",
    "Trocadors","Racó de sa Pujada","Es Cavall d'en Borras","Es Pas","S'Espalmador",
    "Punta Prima","Cala en Baster","Cala Codolar","Ses Illetes","Llevant",
    "Trocadors","Racó de sa Pujada","Es Cavall","Es Pas","S'Alga"
]

EN_TOPICS = [
    "Artificial Intelligence","Machine Learning","Big Data","Cloud Computing","Cybersecurity",
    "App Development","Web Design","SEO","Digital Marketing","E-commerce",
    "IoT","Blockchain","Cryptocurrency","Quantum Computing","Augmented Reality",
    "Virtual Reality","Robotics","Automation","DevOps","Containers",
    "Serverless","APIs","3D Graphics","NLP","Computer Vision",
    "Neural Networks","Deep Learning","Data Modeling","Data Analysis","Data Science",
    "Data Engineering","Recommender Systems","Chatbots","Voice Assistants","Speech Recognition",
    "Face Recognition","Predictive Analytics","Project Management","Remote Work","Collaboration Tools",
    "Cloud Storage","Backup","Data Recovery","System Monitoring","Event Logging",
    "Identity Management","2FA","Encryption","SSL Certificates","Firewalls",
    "Penetration Testing","Vulnerability Scanning","Patch Management","Compliance","Privacy",
    "GDPR","CCPA","Risk Management","Business Continuity","Disaster Recovery",
    "High Availability","Load Balancing","Caching","CDN","Acceleration",
    "Data Compression","Image Optimization","Modern Formats","Vector Graphics","Fonts",
    "Colors","Contrast","Accessibility","UX","UI",
    "Responsive Design","Adaptive Design","Dark Mode","Animations","Interactivity",
    "No-Code","Low-Code","Workflow Automation","Integration","Webhooks",
    "Zapier","Make","Integrately","Marketing Automation","CRM",
    "ERP","Resource Management","Financial Planning","Cloud Accounting","E-invoicing",
    "Digital Payments","E-wallets","International Transfers","Inventory Management","Supply Chain",
    "Logistics","Shipment Tracking","Warehouse Management","Stocktaking","Barcode",
    "QR Code","RFID","GPS","GIS","Digital Maps",
    "Navigation","Location Analytics","Geography","Smart Cities","Renewable Energy",
    "Energy Efficiency","Environment","Sustainability","Circular Economy","Recycling",
    "Raw Materials","3D Printing","Industry 4.0","Digital Twin","Simulation",
    "Prototyping","Rapid Testing","Iterative Design","Agile","Scrum",
    "Kanban","Hexagon","Software Development","Programming","Algorithms",
    "Data Structures","Operating Systems","Databases","SQL","NoSQL",
    "NewSQL","Graph Databases","Graphics","Networks","Internet Protocols",
    "TCP/IP","HTTP/3","QUIC","WebSockets","gRPC",
    "GraphQL","REST","SOAP","XML","JSON",
    "YAML","TOML","INI","CSV","Parquet",
    "ORC","Avro","Protocol Buffers","Thrift","MessagePack",
    "BSON","CBOR","FlexBuffers","FlatBuffers","Cap'n Proto",
    "ZeroMQ","RabbitMQ","Kafka","Pulsar","Redis",
    "Memcached","Cassandra","MongoDB","DynamoDB","Firestore",
    "Cosmos DB","CockroachDB","TiDB","YugabyteDB","PlanetScale",
    "Neon","Supabase","Hasura","Prisma","Drizzle",
    "TypeORM","Sequelize","Mongoose","SQLAlchemy","Django ORM",
    "Active Record","Hibernate","Entity Framework","Dapper","NHibernate",
    "MyBatis","jOOQ","QueryDSL","JPA","JDBC",
    "ODBC","ADO.NET","PDO","mysqli","pg_query",
    "sqlite3","LevelDB","RocksDB","LMDB","Berkeley DB",
    "Kyoto Cabinet","Tokyo Cabinet","Tkrzw","UnQLite","Vedis",
    "EJDB","Upscaledb","ForestDB","Couchbase Lite","Realm",
    "ObjectBox","Room","Core Data","SQLite.swift","GRDB",
    "FMDB","WCDB","GreenDAO","SugarORM","ActiveAndroid",
    "ORMLite","DBFlow","Requery","SQLDelight","Exposed",
    "Ktorm","Jdbi","Spring Data","Micronaut Data","Quarkus Hibernate",
    "Panache","ActiveJPA","Ebean","JOOQ","Querydsl",
    "MyBatis-Plus","TkMyBatis","Fluent MyBatis","Custom Mapper","MyBatis-Flex",
    "MyBatis-Plus-Join","MyBatisX","MyBatis-Plus-Generator","Code Generator","Reverse Engineering",
    "Scaffolding","Template Engine","Thymeleaf","FreeMarker","Velocity",
    "JSP","JSTL","Facelets","JSF","PrimeFaces",
    "RichFaces","IceFaces","MyFaces","Tomahawk","Trinidad",
    "Tobago","Portlet Bridge","Spring Faces","Spring Web Flow","Web Flow",
    "Flow","State Machine","Spring Statemachine","Squirrel","Stateless4j",
    "Easy States","State Machine","Mason","Stateless","Automaton",
    "JState","StateJ","State","Transition","Event",
    "Action","Guard","Context","State Pattern","Strategy Pattern",
    "Command Pattern","Observer Pattern","Pub/Sub","Event Sourcing","CQRS",
    "Event Store","Axon","Eventuate","NEventStore","Marten",
    "Streamstone","SQLStreamStore","GetEventStore","EventStoreDB","LiteDB",
    "RavenDB","Voron","Esent","Rocks","FASTER",
    "Trill","StreamInsight","Reactive Extensions","RxJava","RxJS",
    "RxSwift","RxKotlin","RxScala","RxRuby","RxPHP",
    "RxGo","RxRust","RxCpp","ReactiveUI","Akka.NET",
    "Akka","Vert.x","Quarkus","Micronaut","Helidon",
    "Ktor","Spring Boot","Spring Framework","Spring Cloud","Spring Security",
    "Spring Data","Spring Integration","Spring Batch","Spring Shell","Spring HATEOAS",
    "Spring REST Docs","Spring GraphQL","Spring Native","Spring WebFlux","Project Reactor",
    "RSocket","R2DBC","Spring R2DBC","Spring Cloud Gateway","Spring Cloud Config",
    "Eureka","Consul","Zookeeper","Nacos","Etcd",
    "Kubernetes","Docker","Podman","containerd","CRI-O",
    "Buildah","Skopeo","Kaniko","Jib","Buildpacks",
    "Cloud Native Buildpacks","Paketo","Heroku","Dokku","Flynn",
    "Deis","OpenShift","Rancher","K3s","K3d",
    "Kind","Minikube","MicroK8s","Docker Desktop","Colima",
    "Lima","Rancher Desktop","Podman Desktop","DevPod","Gitpod",
    "GitHub Codespaces","CodeSandbox","StackBlitz","Replit","Glitch",
    "CodePen","JSFiddle","JSBin","Plunker","Dabblet",
    "Liveweave","CSSDeck","Bootply","Runnable","Codenvy",
    "Cloud9","AWS Cloud9","Azure Cloud Shell","Google Cloud Shell","Oracle Cloud Shell",
    "IBM Cloud Shell","Alibaba Cloud Shell","Tencent Cloud Shell","Huawei Cloud Shell","DigitalOcean Droplet",
    "Linode","Vultr","Hetzner","UpCloud","Scaleway",
    "OVHcloud","Ionos","1&1","Namecheap","GoDaddy",
    "Bluehost","HostGator","SiteGround","DreamHost","InMotion",
    "A2 Hosting","GreenGeeks","HostPapa","iPage","FatCow",
    "JustHost","HostMonster","Netfirms","IPower","Dotster",
    "Domain.com","Register.com","Network Solutions","Enom","Tucows",
    "OpenSRS","ResellerClub","Name.com","NameSilo","Porkbun",
    "Dynadot","Google Domains","AWS Route 53","Cloudflare Registrar","Azure DNS",
    "Google Cloud DNS","DNSimple","NS1","Constellix","Dyn",
    "UltraDNS","EasyDNS","Hurricane Electric","DNS Made Easy","ZoneEdit",
    "No-IP","Dynu","FreeDNS","Afraid.org","DuckDNS",
    "YDNS","DNSExit","EntryDNS","Zonomi","RcodeZero",
    "CSC","MarkMonitor","BrandShelter","Safenames","101domain",
    "Gandi","OVH","GABIA","WhoisXML","DomainTools",
    "WHOIS","RDAP","IRIS","DAS","Escrow",
    "Aftermarket","Sedo","Afternic","Dan.com","Uniregistry Market",
    "BrandBucket","SquadHelp","Brandpa","Namerific","Brandroot",
    "Brandable","Atom","Novanym","Oyzta","BrandDo",
    "Brandwise","NamingForce","Crowdspring","99designs","DesignCrowd",
    "LogoMyWay","Hatchwise","ZillionDesigns","48hourslogo","LogoTournament",
    "LogoArena","Springboard","LogoLounge","Dribbble","Behance",
    "Coroflot","Portfoliobox","Carbonmade","Crevado","Format",
    "Squarespace","Wix","Weebly","Strikingly","Tilda",
    "Readymag","Webflow","Framer","Figma","Sketch",
    "Adobe XD","InVision","Proto.io","Marvel","Principle",
    "Flinto","Origami","Axure","Balsamiq","Mockplus",
    "ProtoPie","Kite","Lottie","Rive","Haiku",
    "Bodymovin","After Effects","Premiere Pro","DaVinci Resolve","Final Cut Pro",
    "Motion","Compressor","Cinema 4D","Blender","Maya",
    "3ds Max","Houdini","Nuke","Fusion","Flame",
    "Smoke","Mocha","Syntheyes","PFTrack","Boujou",
    "MatchMover","3DEqualizer","Autodesk","Adobe","Maxon",
    "SideFX","Foundry","Blackmagic Design","Apple","Avid",
    "Corel","Magix","CyberLink","Wondershare","TechSmith",
    "Camtasia","Snagit","Bandicam","OBS Studio","Streamlabs",
    "XSplit","vMix","Wirecast","Restream","StreamYard",
    "Melon","Riverside","SquadCast","Zencastr","Anchor",
    "Buzzsprout","Libsyn","Podbean","Transistor","Captivate",
    "Simplecast","Spreaker","SoundCloud","Mixcloud","HearThis.at",
    "Audiomack","Bandcamp","DistroKid","TuneCore","CD Baby",
    "LANDR","Amuse","RouteNote","ONErpm","Symphonic",
    "The Orchard","Believe","FUGA","Ditto Music","ReverbNation",
    "Soundrop","Level Music","UnitedMasters","Stem","Vydia",
    "Monstercat","Armada","Spinnin' Records","Anjunabeats","A State of Trance",
    "Above & Beyond","Armin van Buuren","Tiësto","Martin Garrix","David Guetta",
    "Calvin Harris","Swedish House Mafia","Alesso","Avicii","Deadmau5",
    "Skrillex","Diplo","Major Lazer","Jack Ü","Zedd",
    "Chainsmokers","Kygo","Alan Walker","Marshmello","DJ Snake",
    "Steve Aoki","Dimitri Vegas","Like Mike","Hardwell","W&W",
    "Afrojack","Nicky Romero","Sander van Doorn","Ferry Corsten","Gareth Emery",
    "Paul van Dyk","Paul Oakenfold","John Digweed","Sasha","Carl Cox",
    "Richie Hawtin","Adam Beyer","Nina Kraviz","Charlotte de Witte","Amelie Lens",
    "Peggy Gou","Helena Hauff","Annie Mac","Mary Anne Hobbs","B.Traits",
    "Maya Jane Coles","Jamie Jones","Seth Troxler","The Martinez Brothers","Loco Dice",
    "Marco Carola","Joseph Capriati","Maceo Plex","Tale of Us","Mind Against",
    "Afterlife","Drumcode","Klockworks","Ostgut Ton","Berghain",
    "Tresor","Watergate","About Blank","://about blank","Sisyphos",
    "Kater Blau","Else","Ritter Butzke","Gretchen","KitKatClub",
    "Insomnia","Tribehouse","Omen","Dorian Gray","U60311",
    "Cocoon","Amnesia","Pacha","Ushuaïa","Hï Ibiza",
    "DC-10","Privilege","Space","Sankeys","Blue Marlin",
    "Destino","Heart","Lío","Pacha","Lio",
    "Heart","Destino","Talamanca","Cala Jondal","Es Cavallet",
    "Las Salinas","Playa d'en Bossa","Figueretas","Cala Comte","Cala Bassa",
    "Cala Tarida","Cala d'Hort","Cala Vadella","Cala Carbo","Cala Llentrisca",
    "Cala d'en Serra","Portinatx","Sant Joan","Sant Antoni","Santa Eulalia",
    "Es Canar","Cala Llonga","S'Argamassa","Cala Pada","Cala Martina",
    "Es Figueral","Aigües Blanques","Cala Boix","Pou des Lleo","Tagomago",
    "Illa de es Vedrà","Sa Conillera","Illa des Bosc","S'Espalmador","Formentera",
    "La Savina","Es Pujols","Sant Francesc","El Pilar de la Mola","Cap de Barbaria",
    "Punta Rasa","Cala Saona","Migjorn","Es Arenals","Es Calo",
    "La Mola","Pilar","Es Pujols","La Savina","Es Mal Pas",
    "Es Marjals","Ses Salines","Es Trucadors","S'Alga","Punta Prima",
    "Cala en Baster","Cala Codolar","Platja de ses Illetes","Llevant","Trocadors",
    "Racó de sa Pujada","Es Cavall d'en Borras","Es Pas","S'Espalmador","Punta Prima",
    "Cala en Baster","Cala Codolar","Ses Illetes","Llevant","Trocadors",
    "Racó de sa Pujada","Es Cavall","Es Pas","S'Alga"
]

AR_ARTICLE_TEMPLATES = [
    {"title":"أفضل {count} أداة مجانية لتسريع {task} في {year}",
     "body":"في عالم {domain} المتسارع، يبحث الجميع عن حلول فعّالة. أدوات {tool_type} المجانية تتيح لك {feature} بدون تسجيل. جربها الآن ووفّر {saving} شهرياً."},
    {"title":"دليلك الشامل لـ {topic}: نصائح مالية وتقنية {year}",
     "body":"فهم {topic} يوفر عليك آلاف الدولارات. من خلال {strategy}، تقلل النفقات {percent}%. أدواتنا المجانية توفر كل ما تحتاجه للبدء فوراً."},
    {"title":"كيف تُضاعف إنتاجيتك باستخدام {tool_type} المجانية؟",
     "body":"{percent}% من المستخدمين يضيعون ساعات في مهام يمكن إنجازها بضغطة زر. بأدوات {domain}، تُنجز {task} في ثوانٍ وتوفّر {saving} شهرياً."},
    {"title":"{year}: سنة التحول الرقمي مع {topic}",
     "body":"لم يعد التحول الرقمي خياراً. مع {topic}، أصبحت أدوات {domain} متاحة للجميع مجاناً. ابدأ رحلتك الرقمية اليوم."},
    {"title":"5 أخطاء مالية يقع فيها رواد الأعمال وكيف تتجنبها بـ {tool_type}",
     "body":"{percent}% من الشركات الناشئة تفشل بسبب سوء إدارة المالية. أدوات {domain} المجانية تساعدك على تتبع كل قرش وإنجاز {task} بكفاءة."}
]

EN_ARTICLE_TEMPLATES = [
    {"title":"Top {count} Free Tools to Accelerate {task} in {year}",
     "body":"In the fast-paced world of {domain}, everyone seeks efficient solutions. Free {tool_type} tools let you {feature} without registration. Try them now and save {saving} monthly."},
    {"title":"The Ultimate Guide to {topic}: Financial & Tech Tips for {year}",
     "body":"Understanding {topic} saves you thousands annually. Through {strategy}, you reduce expenses by {percent}%. Our free tools provide everything you need to start immediately."},
    {"title":"How to Double Your Productivity Using Free {tool_type}",
     "body":"{percent}% of users waste hours on tasks doable in one click. With {domain} tools, you complete {task} in seconds and save {saving} per month."},
    {"title":"{year}: The Year of Digital Transformation with {topic}",
     "body":"Digital transformation is no longer optional. With {topic}, {domain} tools are now freely available to everyone. Start your digital journey today."},
    {"title":"5 Financial Mistakes Entrepreneurs Make & How to Avoid Them with {tool_type}",
     "body":"{percent}% of startups fail due to poor financial management. Free {domain} tools help you track every penny and accomplish {task} efficiently."}
]

# ===================== HELPERS =====================
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

def slugify(text):
    return text.lower().replace(" ", "-").replace("_", "-")[:50]

# ===================== FUNCTIONAL TOOL TEMPLATES =====================
# Each returns a complete, working HTML file. No backend needed.

def html_wrapper(title, desc, category, content_html, extra_scripts=""):
    return f'''<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — Free Online Tool</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{category}, free tool, online utility">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<style>
:root{{--bg:#0b1120;--surface:#151e32;--primary:#38bdf8;--accent:#f59e0b;--text:#f1f5f9;--muted:#94a3b8;--border:#334155;--radius:12px}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--text);line-height:1.7;min-height:100vh;padding:20px}}
.container{{max-width:900px;margin:0 auto}}
h1{{color:var(--primary);font-size:1.8rem;margin-bottom:10px}}
.badge{{display:inline-block;background:rgba(56,189,248,0.1);color:var(--primary);padding:4px 12px;border-radius:20px;font-size:0.8rem;font-weight:600;margin-bottom:20px;border:1px solid rgba(56,189,248,0.2)}}
.desc{{color:var(--muted);margin-bottom:24px}}
.card{{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:24px;margin-bottom:20px}}
input,textarea,select{{background:#0f172a;color:var(--text);border:1px solid var(--border);padding:10px 14px;border-radius:8px;font-family:inherit;font-size:1rem;width:100%;margin-bottom:12px}}
input:focus,textarea:focus,select:focus{{outline:none;border-color:var(--primary);box-shadow:0 0 0 3px rgba(56,189,248,0.15)}}
.btn{{background:var(--primary);color:#0f172a;border:none;padding:10px 24px;border-radius:8px;cursor:pointer;font-weight:700;font-size:1rem;transition:all .2s;display:inline-flex;align-items:center;gap:6px}}
.btn:hover{{background:#0ea5e9;transform:translateY(-1px)}}
.btn-secondary{{background:var(--surface);color:var(--text);border:1px solid var(--border)}}
.btn-secondary:hover{{background:#1e293b}}
.output{{background:#0f172a;border:1px solid var(--border);border-radius:8px;padding:16px;margin-top:16px;white-space:pre-wrap;font-family:monospace;font-size:0.95rem;min-height:80px;word-break:break-all;overflow-x:auto}}
.toolbar{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:16px}}
.ad{{background:linear-gradient(135deg,#1e293b,#334155);border:1px solid var(--border);border-radius:var(--radius);padding:24px;text-align:center;margin:30px 0;position:relative}}
.ad::after{{content:'AD';position:absolute;top:8px;left:8px;background:rgba(245,158,11,0.15);color:var(--accent);padding:2px 8px;border-radius:4px;font-size:0.65rem;font-weight:700}}
.ad a{{color:var(--accent);text-decoration:none;font-weight:700;font-size:1.05rem;display:inline-block;padding:8px 24px;background:rgba(245,158,11,0.1);border-radius:8px;border:1px solid rgba(245,158,11,0.3);transition:all .3s}}
.ad a:hover{{background:rgba(245,158,11,0.2);transform:scale(1.02)}}
.back{{display:inline-flex;align-items:center;gap:6px;color:var(--muted);text-decoration:none;margin-top:20px;transition:color .2s}}
.back:hover{{color:var(--primary)}}
.grid-2{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
@media(max-width:640px){{.grid-2{{grid-template-columns:1fr}}h1{{font-size:1.4rem}}}}
::webkit-scrollbar{{width:8px}}::webkit-scrollbar-track{{background:var(--bg)}}::webkit-scrollbar-thumb{{background:var(--border);border-radius:4px}}
</style>
</head>
<body>
<div class="container">
<span class="badge">{category}</span>
<h1>{title}</h1>
<p class="desc">{desc}</p>
<div class="card">
{content_html}
</div>
<div class="ad">
<p>🚀 Discover more free tools & exclusive offers</p>
<a href="{AD_LINK}" target="_blank" rel="nofollow noopener">Click here for the special offer</a>
</div>
<a href="../index.html" class="back">← Back to Home</a>
</div>
{extra_scripts}
</body>
</html>'''

def tool_json_formatter(name, desc, cat):
    content = '''
<div class="toolbar">
<button class="btn" onclick="format()">Pretty Print</button>
<button class="btn btn-secondary" onclick="minify()">Minify</button>
<button class="btn btn-secondary" onclick="validate()">Validate</button>
<button class="btn btn-secondary" onclick="copyOut()">Copy Result</button>
</div>
<textarea id="input" rows="8" placeholder="Paste your JSON here..."></textarea>
<div id="output" class="output">Result will appear here...</div>
<script>
function format(){try{const o=JSON.parse(document.getElementById('input').value);document.getElementById('output').textContent=JSON.stringify(o,null,2);document.getElementById('output').style.color='var(--text)';}catch(e){document.getElementById('output').textContent='❌ Error: '+e.message;document.getElementById('output').style.color='#ef4444';}}
function minify(){try{const o=JSON.parse(document.getElementById('input').value);document.getElementById('output').textContent=JSON.stringify(o);document.getElementById('output').style.color='var(--text)';}catch(e){document.getElementById('output').textContent='❌ Error: '+e.message;document.getElementById('output').style.color='#ef4444';}}
function validate(){try{JSON.parse(document.getElementById('input').value);document.getElementById('output').textContent='✅ Valid JSON';document.getElementById('output').style.color='#10b981';}catch(e){document.getElementById('output').textContent='❌ Error: '+e.message;document.getElementById('output').style.color='#ef4444';}}
function copyOut(){const t=document.getElementById('output').textContent;navigator.clipboard.writeText(t).then(()=>alert('Copied!'));}
</script>'''
    return html_wrapper(name, desc, cat, content)

def tool_base64(name, desc, cat):
    content = '''
<div class="toolbar">
<button class="btn" onclick="enc()">Encode</button>
<button class="btn btn-secondary" onclick="dec()">Decode</button>
<button class="btn btn-secondary" onclick="copyOut()">Copy</button>
</div>
<textarea id="input" rows="6" placeholder="Enter text or Base64..."></textarea>
<div id="output" class="output">Result will appear here...</div>
<script>
function enc(){const t=document.getElementById('input').value;try{document.getElementById('output').textContent=btoa(unescape(encodeURIComponent(t)));document.getElementById('output').style.color='var(--text)';}catch(e){document.getElementById('output').textContent='❌ Error: '+e.message;document.getElementById('output').style.color='#ef4444';}}
function dec(){const t=document.getElementById('input').value;try{document.getElementById('output').textContent=decodeURIComponent(escape(atob(t)));document.getElementById('output').style.color='var(--text)';}catch(e){document.getElementById('output').textContent='❌ Error: '+e.message;document.getElementById('output').style.color='#ef4444';}}
function copyOut(){navigator.clipboard.writeText(document.getElementById('output').textContent).then(()=>alert('Copied!'));}
</script>'''
    return html_wrapper(name, desc, cat, content)

def tool_url_encoder(name, desc, cat):
    content = '''
<div class="toolbar">
<button class="btn" onclick="enc()">URL Encode</button>
<button class="btn btn-secondary" onclick="dec()">URL Decode</button>
<button class="btn btn-secondary" onclick="copyOut()">Copy</button>
</div>
<textarea id="input" rows="5" placeholder="Enter text or URL..."></textarea>
<div id="output" class="output">Result will appear here...</div>
<script>
function enc(){document.getElementById('output').textContent=encodeURIComponent(document.getElementById('input').value);document.getElementById('output').style.color='var(--text)';}
function dec(){document.getElementById('output').textContent=decodeURIComponent(document.getElementById('input').value);document.getElementById('output').style.color='var(--text)';}
function copyOut(){navigator.clipboard.writeText(document.getElementById('output').textContent).then(()=>alert('Copied!'));}
</script>'''
    return html_wrapper(name, desc, cat, content)

def tool_password_generator(name, desc, cat):
    content = '''
<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px">
<label>Length: <input type="number" id="len" value="16" min="4" max="128" style="width:80px"></label>
<label><input type="checkbox" id="upper" checked style="width:auto"> Uppercase (A-Z)</label>
<label><input type="checkbox" id="lower" checked style="width:auto"> Lowercase (a-z)</label>
<label><input type="checkbox" id="nums" checked style="width:auto"> Numbers (0-9)</label>
<label><input type="checkbox" id="symb" checked style="width:auto"> Symbols (!@#...)</label>
</div>
<button class="btn" onclick="gen()">Generate Password</button>
<div id="output" class="output" style="font-size:1.3rem;text-align:center;word-break:break-all;margin-top:16px">Click Generate to create a password</div>
<div id="strength" style="margin-top:10px;padding:8px;border-radius:6px;text-align:center;font-weight:700"></div>
<script>
function gen(){
  const len=parseInt(document.getElementById('len').value);
  const u=document.getElementById('upper').checked,l=document.getElementById('lower').checked,n=document.getElementById('nums').checked,s=document.getElementById('symb').checked;
  let chars='';if(u)chars+='ABCDEFGHIJKLMNOPQRSTUVWXYZ';if(l)chars+='abcdefghijklmnopqrstuvwxyz';if(n)chars+='0123456789';if(s)chars+='!@#$%^&*()_+-=[]{}|;:,.<>?';
  if(!chars){alert('Select at least one type');return;}
  let pass='';for(let i=0;i<len;i++)pass+=chars.charAt(Math.floor(Math.random()*chars.length));
  document.getElementById('output').textContent=pass;navigator.clipboard.writeText(pass);
  let score=0;if(len>=12)score++;if(len>=16)score++;if(u&&l)score++;if(n)score++;if(s)score++;
  const labels=['Very Weak','Weak','Medium','Strong','Very Strong','Excellent'];
  const colors=['#ef4444','#f97316','#eab308','#84cc16','#22c55e','#10b981'];
  const el=document.getElementById('strength');el.textContent='Strength: '+labels[score];el.style.background=colors[score]+'22';el.style.color=colors[score];
}
</script>'''
    return html_wrapper(name, desc, cat, content)

def tool_color_converter(name, desc, cat):
    content = '''
<div class="grid-2">
<div><input id="hex" placeholder="#38bdf8" oninput="fromHex()"><label style="color:var(--muted);font-size:0.85rem">HEX</label></div>
<div><input id="rgb" placeholder="rgb(56,189,248)" oninput="fromRgb()"><label style="color:var(--muted);font-size:0.85rem">RGB</label></div>
<div><input id="hsl" placeholder="hsl(199,89%,60%)" oninput="fromHsl()"><label style="color:var(--muted);font-size:0.85rem">HSL</label></div>
<div><input id="cmyk" placeholder="cmyk(77,24,0,3)" oninput="fromCmyk()"><label style="color:var(--muted);font-size:0.85rem">CMYK</label></div>
</div>
<div id="preview" style="width:100%;height:80px;border-radius:12px;margin:16px 0;border:2px solid var(--border);background:#38bdf8;transition:background .3s"></div>
<div id="output" class="output">Enter a color value above</div>
<script>
function fromHex(){let h=document.getElementById('hex').value.trim();if(!h.match(/^#/))h='#'+h;if(!/^#[0-9A-Fa-f]{6}$/.test(h))return;const r=parseInt(h.slice(1,3),16),g=parseInt(h.slice(3,5),16),b=parseInt(h.slice(5,7),16);update(r,g,b,h);}
function fromRgb(){const m=document.getElementById('rgb').value.match(/(\d+),\s*(\d+),\s*(\d+)/);if(!m)return;update(parseInt(m[1]),parseInt(m[2]),parseInt(m[3]));}
function fromHsl(){const m=document.getElementById('hsl').value.match(/(\d+),\s*(\d+)%,\s*(\d+)%/);if(!m)return;let h=parseInt(m[1])/360,s=parseInt(m[2])/100,l=parseInt(m[3])/100;let r,g,b;if(s===0){r=g=b=l;}else{const hue2rgb=(p,q,t)=>{if(t<0)t+=1;if(t>1)t-=1;if(t<1/6)return p+(q-p)*6*t;if(t<1/2)return q;if(t<2/3)return p+(q-p)*(2/3-t)*6;return p;};const q=l<0.5?l*(1+s):l+s-l*s;const p=2*l-q;r=hue2rgb(p,q,h+1/3);g=hue2rgb(p,q,h);b=hue2rgb(p,q,h-1/3);}update(Math.round(r*255),Math.round(g*255),Math.round(b*255));}
function fromCmyk(){const m=document.getElementById('cmyk').value.match(/(\d+)[, ]+(\d+)[, ]+(\d+)[, ]+(\d+)/);if(!m)return;const c=parseInt(m[1])/100,m2=parseInt(m[2])/100,y=parseInt(m[3])/100,k=parseInt(m[4])/100;update(Math.round(255*(1-c)*(1-k)),Math.round(255*(1-m2)*(1-k)),Math.round(255*(1-y)*(1-k)));}
function update(r,g,b,hex=null){const h=hex||'#'+[r,g,b].map(x=>x.toString(16).padStart(2,'0')).join('');const hsl=rgbToHsl(r,g,b);const cmyk=rgbToCmyk(r,g,b);document.getElementById('hex').value=h;document.getElementById('rgb').value=`rgb(${r}, ${g}, ${b})`;document.getElementById('hsl').value=`hsl(${hsl.h}, ${hsl.s}%, ${hsl.l}%)`;document.getElementById('cmyk').value=`cmyk(${cmyk.c}, ${cmyk.m}, ${cmyk.y}, ${cmyk.k})`;document.getElementById('preview').style.background=h;document.getElementById('output').innerHTML=`HEX: ${h}<br>RGB: rgb(${r}, ${g}, ${b})<br>HSL: hsl(${hsl.h}, ${hsl.s}%, ${hsl.l}%)<br>CMYK: cmyk(${cmyk.c}, ${cmyk.m}, ${cmyk.y}, ${cmyk.k})`;}
function rgbToHsl(r,g,b){r/=255;g/=255;b/=255;const max=Math.max(r,g,b),min=Math.min(r,g,b);let h,s,l=(max+min)/2;if(max===min){h=s=0;}else{const d=max-min;s=l>0.5?d/(2-max-min):d/(max+min);switch(max){case r:h=(g-b)/d+(g<b?6:0);break;case g:h=(b-r)/d+2;break;case b:h=(r-g)/d+4;break;}h/=6;}return {h:Math.round(h*360),s:Math.round(s*100),l:Math.round(l*100)};}
function rgbToCmyk(r,g,b){let c=1-(r/255),m=1-(g/255),y=1-(b/255),k=Math.min(c,Math.min(m,y));c=(c-k)/(1-k)||0;m=(m-k)/(1-k)||0;y=(y-k)/(1-k)||0;return {c:Math.round(c*100),m:Math.round(m*100),y:Math.round(y*100),k:Math.round(k*100)};}
</script>'''
    return html_wrapper(name, desc, cat, content)

def tool_unit_converter(name, desc, cat):
    content = '''
<div class="grid-2">
<div><input type="number" id="val" value="1" step="any" placeholder="Value"></div>
<div>
<select id="from" style="margin-bottom:8px"><option value="m">Meter (m)</option><option value="km">Kilometer (km)</option><option value="cm">Centimeter (cm)</option><option value="mm">Millimeter (mm)</option><option value="ft">Foot (ft)</option><option value="in">Inch (in)</option><option value="yd">Yard (yd)</option><option value="mi">Mile (mi)</option></select>
<select id="to"><option value="km">Kilometer (km)</option><option value="m" selected>Meter (m)</option><option value="cm">Centimeter (cm)</option><option value="mm">Millimeter (mm)</option><option value="ft">Foot (ft)</option><option value="in">Inch (in)</option><option value="yd">Yard (yd)</option><option value="mi">Mile (mi)</option></select>
</div>
</div>
<button class="btn" onclick="convert()" style="margin-top:8px">Convert</button>
<div id="output" class="output">Enter a value and click Convert</div>
<script>
const rates={m:1,km:1000,cm:0.01,mm:0.001,ft:0.3048,in:0.0254,yd:0.9144,mi:1609.34};
function convert(){const v=parseFloat(document.getElementById('val').value);const f=document.getElementById('from').value;const t=document.getElementById('to').value;if(isNaN(v)){document.getElementById('output').textContent='Please enter a valid number';return;}const m=v*rates[f];const res=m/rates[t];document.getElementById('output').textContent=`${v} ${f} = ${res.toFixed(6)} ${t}`;}
</script>'''
    return html_wrapper(name, desc, cat, content)

def tool_word_counter(name, desc, cat):
    content = '''
<textarea id="text" rows="8" placeholder="Type or paste your text here..." oninput="count()"></textarea>
<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:12px;margin-top:16px">
<div class="card" style="text-align:center;padding:16px"><div style="font-size:1.8rem;font-weight:700;color:var(--primary)" id="words">0</div><div style="color:var(--muted);font-size:0.85rem">Words</div></div>
<div class="card" style="text-align:center;padding:16px"><div style="font-size:1.8rem;font-weight:700;color:var(--primary)" id="chars">0</div><div style="color:var(--muted);font-size:0.85rem">Characters</div></div>
<div class="card" style="text-align:center;padding:16px"><div style="font-size:1.8rem;font-weight:700;color:var(--primary)" id="charsNoSpace">0</div><div style="color:var(--muted);font-size:0.85rem">No Spaces</div></div>
<div class="card" style="text-align:center;padding:16px"><div style="font-size:1.8rem;font-weight:700;color:var(--primary)" id="sentences">0</div><div style="color:var(--muted);font-size:0.85rem">Sentences</div></div>
<div class="card" style="text-align:center;padding:16px"><div style="font-size:1.8rem;font-weight:700;color:var(--primary)" id="paragraphs">0</div><div style="color:var(--muted);font-size:0.85rem">Paragraphs</div></div>
<div class="card" style="text-align:center;padding:16px"><div style="font-size:1.8rem;font-weight:700;color:var(--primary)" id="reading">0</div><div style="color:var(--muted);font-size:0.85rem">Min Read</div></div>
</div>
<script>
function count(){const t=document.getElementById('text').value;document.getElementById('chars').textContent=t.length;document.getElementById('charsNoSpace').textContent=t.replace(/\s/g,'').length;const words=t.trim()===''?0:t.trim().split(/\s+/).length;document.getElementById('words').textContent=words;const sentences=t.split(/[.!?]+/).filter(s=>s.trim().length>0).length;document.getElementById('sentences').textContent=sentences;const paragraphs=t.split('\n').filter(p=>p.trim().length>0).length;document.getElementById('paragraphs').textContent=paragraphs;document.getElementById('reading').textContent=Math.ceil(words/200)||0;}
</script>'''
    return html_wrapper(name, desc, cat, content)

def tool_lorem_ipsum(name, desc, cat):
    content = '''
<div class="grid-2">
<div><label style="color:var(--muted);font-size:0.85rem">Paragraphs</label><input type="number" id="paras" value="3" min="1" max="50"></div>
<div><label style="color:var(--muted);font-size:0.85rem">Words per paragraph</label><input type="number" id="words" value="50" min="10" max="200"></div>
</div>
<label style="display:flex;align-items:center;gap:8px;margin:12px 0;color:var(--muted)"><input type="checkbox" id="html" checked style="width:auto"> Wrap in HTML &lt;p&gt; tags</label>
<div class="toolbar">
<button class="btn" onclick="generate()">Generate</button>
<button class="btn btn-secondary" onclick="copyOut()">Copy</button>
</div>
<div id="output" class="output" style="line-height:1.8">Click Generate to create text...</div>
<script>
const dict=["lorem","ipsum","dolor","sit","amet","consectetur","adipiscing","elit","sed","do","eiusmod","tempor","incididunt","ut","labore","et","dolore","magna","aliqua","ut","enim","ad","minim","veniam","quis","nostrud","exercitation","ullamco","laboris","nisi","ut","aliquip","ex","ea","commodo","consequat","duis","aute","irure","dolor","in","reprehenderit","in","voluptate","velit","esse","cillum","dolore","eu","fugiat","nulla","pariatur","excepteur","sint","occaecat","cupidatat","non","proident","sunt","in","culpa","qui","officia","deserunt","mollit","anim","id","est","laborum"];
function generate(){const p=parseInt(document.getElementById('paras').value);const w=parseInt(document.getElementById('words').value);const html=document.getElementById('html').checked;let out='';for(let i=0;i<p;i++){let para='';for(let j=0;j<w;j++)para+=dict[Math.floor(Math.random()*dict.length)]+' ';para=para.charAt(0).toUpperCase()+para.slice(1).trim()+'.';out+=html?'<p>'+para+'</p>\n\n':para+'\n\n';}document.getElementById('output').innerHTML=out.trim();}
function copyOut(){const t=document.getElementById('html').checked?document.getElementById('output').innerText:document.getElementById('output').textContent;navigator.clipboard.writeText(t).then(()=>alert('Copied!'));}
</script>'''
    return html_wrapper(name, desc, cat, content)

def tool_qr_generator(name, desc, cat):
    content = '''
<input id="qrText" placeholder="Enter text or URL to encode..." value="https://example.com">
<button class="btn" onclick="makeQR()" style="margin-top:8px">Generate QR Code</button>
<div id="qrcode" style="margin-top:20px;text-align:center;padding:20px;background:#fff;border-radius:12px;display:inline-block;width:100%"></div>
<div id="output" class="output" style="margin-top:16px">Enter text and click Generate</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
<script>
let qr=null;
function makeQR(){const text=document.getElementById('qrText').value;const container=document.getElementById('qrcode');container.innerHTML='';qr=new QRCode(container,{text:text,width:200,height:200,colorDark:'#000000',colorLight:'#ffffff',correctLevel:QRCode.CorrectLevel.H});document.getElementById('output').textContent='QR generated for: '+text;}
</script>'''
    return html_wrapper(name, desc, cat, content)

def tool_markdown_preview(name, desc, cat):
    content = '''
<div class="grid-2">
<textarea id="mdInput" rows="12" placeholder="# Hello World\n\nWrite **markdown** here..." oninput="render()"></textarea>
<div id="preview" style="background:#fff;color:#1e293b;padding:16px;border-radius:8px;overflow:auto;min-height:200px"></div>
</div>
<script>
function render(){let t=document.getElementById('mdInput').value;t=t.replace(/^### (.*$)/gim,'<h3>$1</h3>').replace(/^## (.*$)/gim,'<h2>$1</h2>').replace(/^# (.*$)/gim,'<h1>$1</h1>').replace(/\*\*(.*)\*\*/gim,'<b>$1</b>').replace(/\*(.*)\*/gim,'<i>$1</i>').replace(/!\[(.*?)\]\((.*?)\)/gim,"<img alt='$1' src='$2' style='max-width:100%'>").replace(/\[(.*?)\]\((.*?)\)/gim,"<a href='$2' target='_blank'>$1</a>").replace(/```([\s\S]*?)```/gim,'<pre style="background:#f1f5f9;padding:12px;border-radius:6px;overflow:auto"><code>$1</code></pre>').replace(/`([^`]+)`/gim,'<code style="background:#f1f5f9;padding:2px 4px;border-radius:4px">$1</code>').replace(/^> (.*$)/gim,'<blockquote style="border-right:4px solid #cbd5e1;padding-right:12px;color:#475569;margin:0">$1</blockquote>').replace(/\n/gim,'<br>');document.getElementById('preview').innerHTML=t;}
</script>'''
    return html_wrapper(name, desc, cat, content)

def tool_css_minifier(name, desc, cat):
    content = '''
<div class="toolbar">
<button class="btn" onclick="minify()">Minify CSS</button>
<button class="btn btn-secondary" onclick="beautify()">Beautify</button>
<button class="btn btn-secondary" onclick="copyOut()">Copy</button>
</div>
<textarea id="input" rows="10" placeholder="Paste CSS here..."></textarea>
<div id="output" class="output">Result will appear here...</div>
<script>
function minify(){let c=document.getElementById('input').value;c=c.replace(/\/\*[\s\S]*?\*\//g,'').replace(/\s+/g,' ').replace(/\s*([{}:;,])\s*/g,'$1').replace(/;}/g,'}').trim();document.getElementById('output').textContent=c;}
function beautify(){let c=document.getElementById('input').value;c=c.replace(/([{;])/g,'$1\n').replace(/}/g,'}\n').replace(/,/g,', ').replace(/\s+/g,' ').trim();document.getElementById('output').textContent=c;}
function copyOut(){navigator.clipboard.writeText(document.getElementById('output').textContent).then(()=>alert('Copied!'));}
</script>'''
    return html_wrapper(name, desc, cat, content)

def tool_html_entities(name, desc, cat):
    content = '''
