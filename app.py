import streamlit as st

# ── PAGE CONFIG ──────────────────────────────────────────────
st.set_page_config(
    page_title="Raju Devnath | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── GLOBAL STYLES ────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0d1b2a;
    border-right: 1px solid #1e3a5f;
}
section[data-testid="stSidebar"] * { color: #c8d8e8 !important; }

/* Main bg */
.main { background: #f5f8fc; }

/* Section headers */
.sec-header {
    font-size: 1.4rem; font-weight: 700;
    color: #1a3a6b; border-left: 4px solid #e8a020;
    padding-left: 12px; margin-bottom: 20px; margin-top: 10px;
}

/* Cards */
.card {
    background: white; border-radius: 12px;
    padding: 20px 24px; margin-bottom: 16px;
    border: 1px solid #e2eaf4;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
}
.card:hover { box-shadow: 0 4px 16px rgba(0,0,0,0.1); }

/* Skill pill */
.pill {
    display: inline-block;
    background: #e8f0fb; color: #1a3a6b;
    border-radius: 20px; padding: 4px 14px;
    font-size: 0.82rem; font-weight: 500;
    margin: 4px 3px;
}
.pill-gold {
    background: #fff3d6; color: #a06800;
}
.pill-green {
    background: #e2f5ea; color: #1a6b3a;
}

/* Timeline dot */
.tl-dot {
    width: 12px; height: 12px; background: #e8a020;
    border-radius: 50%; display: inline-block; margin-right: 8px;
}

/* Stat box */
.stat-box {
    background: #0d1b2a; border-radius: 12px;
    padding: 20px; text-align: center;
}
.stat-num { font-size: 2.2rem; font-weight: 700; color: #e8a020; }
.stat-label { font-size: 0.8rem; color: #8aaac8; margin-top: 4px; }

/* Project card */
.proj-card {
    background: white; border-radius: 12px;
    padding: 22px; margin-bottom: 16px;
    border-left: 4px solid #1a3a6b;
    box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.proj-tag {
    display: inline-block;
    background: #f0f4fa; color: #1a3a6b;
    border-radius: 6px; padding: 3px 10px;
    font-size: 0.75rem; font-weight: 600;
    margin-right: 6px; margin-bottom: 4px;
}

/* Hero name */
.hero-name {
    font-size: 2.6rem; font-weight: 700;
    color: #0d1b2a; line-height: 1.1;
}
.hero-role { font-size: 1.1rem; color: #4a6a9a; font-weight: 400; margin-top: 6px; }
.hero-loc  { font-size: 0.9rem; color: #8a9ab0; margin-top: 4px; }

/* Hide streamlit branding */
#MainMenu, footer, header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ── SIDEBAR ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 📊 Raju Devnath")
    st.markdown("*Data Science Instructor & Analyst*")
    st.markdown("---")
    st.markdown("### Navigate")
    sections = ["🏠 Home", "👤 About", "🛠 Skills", "💼 Experience", "🚀 Projects", "🎓 Education", "📜 Certifications", "📬 Contact"]
    for s in sections:
        st.markdown(f"[{s}](#{s.split(' ',1)[1].lower().replace(' ','-')})" , unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### Connect")
    st.markdown("📧 rjnath98@gmail.com")
    st.markdown("📞 +91-7002141483")
    st.markdown("📍 Guwahati, India")
    st.markdown("")
    st.markdown("[🔗 LinkedIn](#) &nbsp; [💻 GitHub](#) &nbsp; [🌐 Portfolio](#)", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# HOME / HERO
# ══════════════════════════════════════════════════════════════
st.markdown('<a name="home"></a>', unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    <div class="card" style="border-left: 5px solid #e8a020; padding: 36px;">
        <div class="hero-name">Raju Devnath</div>
        <div class="hero-role">📊 Data Science Instructor &nbsp;|&nbsp; 🤖 AI/ML Mentor &nbsp;|&nbsp; 🐍 Python & SQL Educator</div>
        <div class="hero-loc">📍 Guwahati, India &nbsp;·&nbsp; Available for Teaching & Analyst Roles</div>
        <br>
        <p style="color:#4a5a7a; line-height:1.8; font-size:0.95rem;">
        Passionate educator and practitioner with <strong>4+ years</strong> of teaching experience and hands-on
        industry work in Data Science. I've trained <strong>2,000+ students</strong> across offline classrooms,
        online platforms, bootcamps, and workshops — turning complex concepts into practical,
        job-ready skills.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown('<br>', unsafe_allow_html=True)
    stats = [("2,000+", "Students Taught"), ("700+", "Offline Learners"), ("4+ Yrs", "Teaching Exp."), ("5+", "Subjects")]
    for num, label in stats:
        st.markdown(f"""
        <div class="stat-box" style="margin-bottom:10px;">
            <div class="stat-num">{num}</div>
            <div class="stat-label">{label}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# ABOUT
# ══════════════════════════════════════════════════════════════
st.markdown('<a name="about"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec-header">👤 About Me</div>', unsafe_allow_html=True)

col1, col2 = st.columns([3, 2])
with col1:
    st.markdown("""
    <div class="card">
        <p style="color:#4a5a7a; line-height:1.9; font-size:0.95rem;">
        I'm a <strong>Data Science Instructor, AI/ML Mentor</strong>, and <strong>Data Analyst</strong> based in Guwahati, India.
        With a B.Tech in Computer Science from Lovely Professional University, I bridge the gap between
        academic learning and real-world industry application.
        <br><br>
        As a <strong>Subject Matter Expert on CheggExpert</strong>, I've answered 1,000+ queries from students
        across the globe. Before that, I personally taught <strong>700+ students offline</strong> in Mathematics
        and Computer Science fundamentals.
        <br><br>
        At <strong>Allsoft Solutions</strong>, I work as a Data Science Trainee — building ML models, writing
        optimized SQL queries, and creating dashboards — experience I directly bring into my teaching.
        <br><br>
        My teaching philosophy: <em>"Learn by building real things."</em> Every session I run is
        project-driven, practical, and mapped to industry standards.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <p style="font-weight:600; color:#1a3a6b; margin-bottom:12px;">🎯 What I Offer</p>
        <ul style="color:#4a5a7a; line-height:2.1; font-size:0.9rem; padding-left:16px;">
            <li>Industry-standard, practical curriculum</li>
            <li>Live coding & real dataset sessions</li>
            <li>End-to-end project mentoring</li>
            <li>1-on-1 doubt resolution</li>
            <li>Bootcamp & workshop design</li>
            <li>Corporate training delivery</li>
        </ul>
    </div>
    <div class="card" style="margin-top:0;">
        <p style="font-weight:600; color:#1a3a6b; margin-bottom:10px;">🏷 Domains</p>
    """, unsafe_allow_html=True)
    tags = ["Data Science", "Machine Learning", "AI", "Python", "SQL", "Tableau", "Excel", "Statistics", "Mathematics", "NLP"]
    st.markdown("".join([f'<span class="pill">{t}</span>' for t in tags]) + "</div>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# SKILLS
# ══════════════════════════════════════════════════════════════
st.markdown('<a name="skills"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec-header">🛠 Technical Skills</div>', unsafe_allow_html=True)

skills_data = [
    ("🐍", "Languages", ["Python", "SQL", "R", "HTML", "CSS", "JavaScript"]),
    ("📊", "Data Analysis", ["Pandas", "NumPy", "EDA", "Data Wrangling", "Data Cleaning", "Statistical Analysis"]),
    ("🤖", "ML / AI", ["Scikit-learn", "Regression", "Classification", "Clustering", "NLP", "Feature Engineering", "XGBoost"]),
    ("📉", "Visualization", ["Tableau", "Power BI", "Matplotlib", "Seaborn", "Excel Dashboards", "KPI Reporting"]),
    ("🗄", "Databases", ["MySQL", "MongoDB", "PostgreSQL", "Query Optimization", "DBMS"]),
    ("☁️", "Cloud & DevOps", ["AWS S3", "AWS EC2", "Git/GitHub", "Docker", "Streamlit", "Jupyter Notebook"]),
    ("🎓", "Teaching Tools", ["Google Colab", "Zoom/Meet LMS", "PowerPoint", "Curriculum Design", "Assessment Design"]),
    ("🧮", "Mathematics", ["Linear Algebra", "Calculus", "Probability", "Statistics", "Discrete Maths"]),
]

cols = st.columns(4)
for i, (icon, category, items) in enumerate(skills_data):
    with cols[i % 4]:
        pills = "".join([f'<span class="pill">{p}</span>' for p in items])
        st.markdown(f"""
        <div class="card" style="min-height:180px;">
            <div style="font-size:1.6rem;">{icon}</div>
            <div style="font-size:0.72rem; text-transform:uppercase; letter-spacing:0.1em; color:#e8a020; font-weight:600; margin:6px 0 4px;">{category}</div>
            <div>{pills}</div>
        </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# EXPERIENCE
# ══════════════════════════════════════════════════════════════
st.markdown('<a name="experience"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec-header">💼 Work Experience</div>', unsafe_allow_html=True)

experiences = [
    {
        "role": "Data Science Trainee",
        "org": "Allsoft Solutions Pvt. Ltd.",
        "period": "March 2024 – Present",
        "type": "Industry",
        "color": "#1a3a6b",
        "points": [
            "Gathered and cleaned data from multiple sources, ensuring high data quality for analysis and ML modeling.",
            "Built and deployed machine learning models (regression, classification) to predict and improve business KPIs.",
            "Developed and optimized complex SQL queries for large-scale dataset management and reporting.",
            "Created Tableau & Excel dashboards for stakeholder reporting and data-driven decision making.",
            "Conducted internal training sessions on Python, SQL, EDA, and Tableau for junior team members.",
        ]
    },
    {
        "role": "Subject Matter Expert — Online Tutor",
        "org": "CheggExpert (Global Platform)",
        "period": "2021 – Present",
        "type": "Teaching",
        "color": "#e8a020",
        "points": [
            "Resolved 1,000+ student queries in Python, SQL, Data Science & Mathematics across universities in India, USA, and UK.",
            "Maintained top accuracy rating by delivering structured, step-by-step explanations tailored to student level.",
            "Built expertise in explaining complex Data Analytics and ML concepts clearly and concisely.",
        ]
    },
    {
        "role": "Offline Instructor — Maths & Computer Science",
        "org": "Independent / Community Teaching",
        "period": "May 2018 – Dec 2020",
        "type": "Teaching",
        "color": "#2e8b57",
        "points": [
            "Taught 700+ students across multiple offline batches in Mathematics, Computer Science, and programming fundamentals.",
            "Designed lesson plans, assessments, and hands-on practicals adapted for varying student skill levels.",
            "Conducted regular doubt-clearing sessions and mock tests — consistently rated highly by students and parents.",
        ]
    },
]

for exp in experiences:
    badge_color = "#e8f0fb" if exp["type"] == "Industry" else ("#fff3d6" if exp["type"] == "Teaching" else "#e2f5ea")
    badge_text  = "#1a3a6b" if exp["type"] == "Industry" else ("#a06800" if exp["type"] == "Teaching" else "#1a6b3a")
    points_html = "".join([f"<li style='margin-bottom:6px;'>{p}</li>" for p in exp["points"]])
    st.markdown(f"""
    <div class="card" style="border-left: 4px solid {exp['color']};">
        <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:8px;">
            <div>
                <span style="font-size:1.05rem; font-weight:700; color:#0d1b2a;">{exp['role']}</span>
                <span style="color:#4a6a9a; font-size:0.9rem;"> &nbsp;·&nbsp; {exp['org']}</span>
            </div>
            <div style="display:flex; gap:8px; align-items:center; flex-wrap:wrap;">
                <span style="background:{badge_color}; color:{badge_text}; padding:3px 12px; border-radius:20px; font-size:0.75rem; font-weight:600;">{exp['type']}</span>
                <span style="color:#8a9ab0; font-size:0.82rem;">📅 {exp['period']}</span>
            </div>
        </div>
        <ul style="color:#4a5a7a; line-height:1.8; font-size:0.9rem; margin-top:12px; padding-left:18px;">
            {points_html}
        </ul>
    </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# PROJECTS
# ══════════════════════════════════════════════════════════════
st.markdown('<a name="projects"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec-header">🚀 Projects</div>', unsafe_allow_html=True)

projects = [
    {
        "title": "Retail Sales Performance Dashboard",
        "category": "Data Analyst Project",
        "year": "2024",
        "tech": ["Python", "MySQL", "Tableau", "Pandas", "EDA", "Time-Series"],
        "desc": "Analyzed 2+ years of retail transaction data (50K+ records) to uncover sales trends, customer segments, and revenue KPIs.",
        "points": [
            "Built interactive Tableau dashboard tracking revenue growth, avg order value, and top SKUs — adopted for weekly management reporting.",
            "Applied time-series forecasting achieving 92% accuracy, enabling data-driven inventory and budget planning.",
            "Automated data pipeline using Python & MySQL reducing manual reporting effort by 60%.",
        ],
        "color": "#1a3a6b"
    },
    {
        "title": "Data Analytics Bootcamp — End-to-End Program",
        "category": "Teaching / Training Project",
        "year": "2023–24",
        "tech": ["Curriculum Design", "Python", "SQL", "Tableau", "Excel", "Streamlit"],
        "desc": "Designed and conducted a 6-week Data Analytics Bootcamp for 80+ participants including students and working professionals.",
        "points": [
            "Built structured curriculum with hands-on assignments, real datasets, and a capstone project — 95% completion rate, 4.8/5 avg feedback.",
            "Delivered live Zoom sessions, recorded video modules, and 1-on-1 mentoring.",
            "30+ participants secured data-related roles or promotions post-bootcamp.",
        ],
        "color": "#e8a020"
    },
    {
        "title": "Customer Churn Prediction — ML Pipeline",
        "category": "Machine Learning",
        "year": "2024",
        "tech": ["Python", "Scikit-learn", "XGBoost", "Pandas", "SQL", "Streamlit"],
        "desc": "End-to-end ML pipeline to predict customer churn for a telecom dataset with 100K+ records.",
        "points": [
            "Used Logistic Regression, Random Forest & XGBoost with SMOTE for class imbalance — 87% accuracy, 0.91 AUC-ROC.",
            "Deployed as an interactive Streamlit web app enabling real-time churn risk scoring.",
            "Automated preprocessing & model retraining pipeline reducing manual intervention by 60%.",
        ],
        "color": "#2e8b57"
    },
    {
        "title": "Pizza Sales Analytics Dashboard",
        "category": "Data Visualization",
        "year": "2023",
        "tech": ["EDA", "MySQL", "Tableau", "Git"],
        "desc": "Analyzed 2-year Pizza Sales dataset (50K+ transactions) to uncover sales trends and revenue KPIs.",
        "points": [
            "Built dynamic Tableau dashboards tracking avg order value, revenue growth, and best-selling SKUs.",
            "Applied time-series analysis for sales forecasting — 92% forecast accuracy.",
            "Used as live classroom teaching material for EDA and visualization storytelling.",
        ],
        "color": "#7b3fa0"
    },
    {
        "title": "WhatsApp Chat Sentiment Analyser",
        "category": "NLP / Web App",
        "year": "2023",
        "tech": ["Python", "NLP", "Streamlit", "WordCloud", "Git"],
        "desc": "NLP-powered web application for sentiment analysis, emoji trend detection, and conversation pattern analysis.",
        "points": [
            "Implemented WordCloud visualization and message frequency analysis.",
            "Deployed publicly on Streamlit Cloud — 200+ active users.",
            "Used as a student capstone demo to teach end-to-end data product development.",
        ],
        "color": "#c0392b"
    },
    {
        "title": "Coffee Shop Sales Dashboard",
        "category": "Business Intelligence",
        "year": "2023",
        "tech": ["MS Excel", "Pivot Tables", "BeautifulSoup", "KPI"],
        "desc": "Multi-location sales performance dashboard covering 5 store locations.",
        "points": [
            "Scraped supplementary market data using BeautifulSoup; integrated with internal sales records.",
            "Identified peak sales windows and top-performing SKUs for inventory and marketing strategy.",
        ],
        "color": "#d4890a"
    },
]

cols = st.columns(2)
for i, proj in enumerate(projects):
    with cols[i % 2]:
        tech_pills = "".join([f'<span class="proj-tag">{t}</span>' for t in proj["tech"]])
        points_html = "".join([f"<li style='margin-bottom:5px;'>{p}</li>" for p in proj["points"]])
        st.markdown(f"""
        <div class="proj-card" style="border-left-color:{proj['color']};">
            <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:6px;">
                <span style="font-size:0.72rem; text-transform:uppercase; letter-spacing:0.1em; color:{proj['color']}; font-weight:700;">{proj['category']}</span>
                <span style="color:#8a9ab0; font-size:0.78rem;">📅 {proj['year']}</span>
            </div>
            <div style="font-size:1.02rem; font-weight:700; color:#0d1b2a; margin-bottom:6px;">{proj['title']}</div>
            <p style="color:#5a6a7a; font-size:0.87rem; margin-bottom:10px; line-height:1.6;">{proj['desc']}</p>
            <div style="margin-bottom:10px;">{tech_pills}</div>
            <ul style="color:#4a5a7a; font-size:0.85rem; line-height:1.7; padding-left:16px;">{points_html}</ul>
        </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# EDUCATION
# ══════════════════════════════════════════════════════════════
st.markdown('<a name="education"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec-header">🎓 Education</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card" style="border-left: 4px solid #1a3a6b;">
    <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:8px;">
        <div>
            <div style="font-size:1.05rem; font-weight:700; color:#0d1b2a;">B.Tech — Computer Science & Engineering</div>
            <div style="color:#4a6a9a; font-size:0.9rem; margin-top:4px;">🏛 Lovely Professional University, Phagwara, Punjab</div>
        </div>
        <div style="text-align:right;">
            <span style="background:#e8f0fb; color:#1a3a6b; padding:3px 12px; border-radius:20px; font-size:0.78rem; font-weight:600;">2020 – 2024</span>
            <br><span style="color:#e8a020; font-weight:700; font-size:0.9rem; margin-top:6px; display:block;">CGPA: 7.2</span>
        </div>
    </div>
    <div style="margin-top:12px;">
        <span style="font-size:0.82rem; color:#4a5a7a;">Relevant Coursework: </span>
        <span class="pill">Data Structures</span>
        <span class="pill">DBMS</span>
        <span class="pill">Machine Learning</span>
        <span class="pill">Statistics</span>
        <span class="pill">Computer Networks</span>
        <span class="pill">Software Engineering</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# CERTIFICATIONS
# ══════════════════════════════════════════════════════════════
st.markdown('<a name="certifications"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec-header">📜 Certifications</div>', unsafe_allow_html=True)

certs = [
    ("📊", "Data Visualization with Tableau Specialization", "Coursera", "2023", "#1a3a6b"),
    ("📈", "Creating Charts & Dashboards in MS Excel", "Coursera", "2023", "#2e8b57"),
    ("☕", "Summer Training in Java", "Hitbullseye", "2022", "#e8a020"),
]
cols = st.columns(3)
for i, (icon, name, issuer, year, color) in enumerate(certs):
    with cols[i]:
        st.markdown(f"""
        <div class="card" style="border-top: 3px solid {color}; text-align:center; padding:24px 20px;">
            <div style="font-size:2rem; margin-bottom:8px;">{icon}</div>
            <div style="font-weight:700; color:#0d1b2a; font-size:0.95rem; margin-bottom:6px;">{name}</div>
            <div style="color:#4a6a9a; font-size:0.82rem;">🏢 {issuer}</div>
            <div style="margin-top:8px;">
                <span style="background:#f0f4fa; color:#4a5a7a; padding:3px 12px; border-radius:20px; font-size:0.75rem;">📅 {year}</span>
            </div>
        </div>""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# TEACHING HIGHLIGHTS
# ══════════════════════════════════════════════════════════════
st.markdown('<div class="sec-header">🏅 Teaching Highlights</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="card">
        <div style="font-weight:700; color:#1a3a6b; margin-bottom:12px; font-size:1rem;">📚 Subjects Taught</div>
        <span class="pill">Python Programming</span>
        <span class="pill">SQL & Databases</span>
        <span class="pill">Machine Learning</span>
        <span class="pill">AI Fundamentals</span>
        <span class="pill">Data Analysis</span>
        <span class="pill">Tableau</span>
        <span class="pill">MS Excel</span>
        <span class="pill">Statistics</span>
        <span class="pill">Mathematics</span>
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="card">
        <div style="font-weight:700; color:#1a3a6b; margin-bottom:12px; font-size:1rem;">🎙 Delivery Modes</div>
        <span class="pill pill-gold">Online LMS</span>
        <span class="pill pill-gold">Live Zoom/Meet</span>
        <span class="pill pill-gold">Offline Classroom</span>
        <span class="pill pill-gold">Workshops</span>
        <span class="pill pill-gold">1-on-1 Mentoring</span>
        <span class="pill pill-gold">Corporate Training</span>
        <span class="pill pill-gold">Bootcamps</span>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# CONTACT
# ══════════════════════════════════════════════════════════════
st.markdown('<a name="contact"></a>', unsafe_allow_html=True)
st.markdown('<div class="sec-header">📬 Contact Me</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown("""
    <div class="card">
        <p style="color:#4a5a7a; line-height:1.8; margin-bottom:16px;">
        Interested in having me as an <strong>instructor, mentor, or data analyst</strong>?
        I'd love to connect. Whether it's a teaching role, a freelance analytics project,
        a workshop, or a full-time position — feel free to reach out!
        </p>
    </div>
    """, unsafe_allow_html=True)
    with st.form("contact_form"):
        name  = st.text_input("Your Name")
        email = st.text_input("Your Email")
        subj  = st.selectbox("Purpose", ["Teaching/Instructor Role", "Data Analyst Role", "Workshop / Bootcamp", "Mentoring", "Other"])
        msg   = st.text_area("Message", height=120)
        submitted = st.form_submit_button("Send Message 🚀")
        if submitted:
            if name and email and msg:
                st.success(f"✅ Thanks {name}! Message received. I'll get back to you at {email} soon.")
            else:
                st.warning("Please fill in all fields.")

with col2:
    st.markdown("""
    <div class="card" style="text-align:center;">
        <div style="font-size:1rem; font-weight:700; color:#1a3a6b; margin-bottom:16px;">Quick Links</div>
        <div style="line-height:2.4; color:#4a5a7a; font-size:0.9rem;">
            📧 rjnath98@gmail.com<br>
            📞 +91-7002141483<br>
            📍 Guwahati, India<br><br>
            <a href="#" style="color:#1a3a6b; font-weight:600;">🔗 LinkedIn Profile</a><br>
            <a href="#" style="color:#1a3a6b; font-weight:600;">💻 GitHub Profile</a><br>
            <a href="#" style="color:#1a3a6b; font-weight:600;">🌐 Portfolio Site</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align:center; padding:32px 0 16px; color:#8a9ab0; font-size:0.82rem; border-top:1px solid #e2eaf4; margin-top:40px;">
    © 2024 Raju Devnath · Built with Streamlit · Data Science Instructor & Analyst
</div>
""", unsafe_allow_html=True)










######








# import streamlit as st
# # import pages.ContactMe
# from pages import home

# # Set page configuration
# st.set_page_config(layout="wide", initial_sidebar_state="collapsed")


# from streamlit_option_menu import option_menu
# st.header("Data Science Portfolio")

# selected_menu=option_menu("",
#             ["Home","About","Project","Contact Me"]
#             , orientation="horizontal",
#             icons=[ ],
#             default_index=0)
# if selected_menu=="Home":
#     home.app()


# # if selected_menu=="About":
# #     pages.About

# # if selected_menu=="Project":
# #    pages.Project

# # if selected_menu=="Contact Me":
# #     pages.ContactMe






