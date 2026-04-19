
import streamlit as st
import base64, os

st.set_page_config(
    page_title="Raju Devnath | Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════
# GLOBAL STYLES
# ══════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

.main { background: #f0f4f9; }
.main .block-container { padding: 1.5rem 2.5rem 3rem 2.5rem; max-width: 1120px; }

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }

/* ── NAV BAR ── */
.topnav {
    display: flex; align-items: center; justify-content: center;
    gap: 8px; flex-wrap: wrap;
    background: #ffffff;
    border-radius: 50px;
    padding: 14px 28px;
    margin-bottom: 28px;
    box-shadow: 0 2px 16px rgba(0,0,0,0.07);
    border: 1px solid #e2eaf4;
}
.nav-btn {
    background: transparent; border: none;
    color: #3a5a8a; font-size: 1rem;      /* ← bigger font */
    font-weight: 700;                      /* ← bolder */
    padding: 9px 22px;                    /* ← more padding */
    border-radius: 30px; cursor: pointer;
    text-decoration: none; letter-spacing: 0.03em;
    transition: background 0.2s, color 0.2s;
    white-space: nowrap;
}
.nav-btn:hover { background: #e8f0fb; color: #1a3a6b; }

/* ── HERO CARD ── */
.hero-wrap {
    background: linear-gradient(135deg, #0d1b2a 0%, #1b3d72 100%);
    border-radius: 20px;
    padding: 36px 40px;
    margin-bottom: 24px;
    display: flex; align-items: flex-start;
    justify-content: space-between;
    gap: 32px; flex-wrap: wrap;
}
.hero-left { flex: 1; min-width: 260px; }
.hero-name {
    font-size: 2.6rem; font-weight: 800;
    color: #ffffff; line-height: 1.1; margin: 0 0 8px 0;
}
.hero-role { font-size: 0.98rem; color: #a8c4e8; font-weight: 400; margin-bottom: 6px; }
.hero-loc  { font-size: 0.83rem; color: #6888aa; margin-bottom: 16px; }
.hero-bio  { font-size: 0.92rem; color: #c0d4ec; line-height: 1.75; max-width: 500px; }
.hero-links {
    display: flex; gap: 10px; margin-top: 20px; flex-wrap: wrap;
}
.hlink {
    background: rgba(255,255,255,0.1);
    border: 1px solid rgba(255,255,255,0.18);
    color: #ffffff !important; font-size: 0.82rem; font-weight: 600;
    padding: 7px 18px; border-radius: 30px;
    text-decoration: none !important;
    transition: background 0.2s;
}
.hlink:hover { background: rgba(232,160,32,0.3); }

/* ── PROFILE PICTURE FRAME (middle column) ── */
.hero-center {
    display: flex; align-items: center; justify-content: center;
    min-width: 200px; flex: 0 0 200px;
}
.profile-frame {
    width: 190px; height: 240px;
    border-radius: 18px;
    border: 3px solid #e8a020;
    box-shadow: 0 0 0 6px rgba(232,160,32,0.18), 0 8px 32px rgba(0,0,0,0.35);
    overflow: hidden;
    background: linear-gradient(160deg, #1b3d72 0%, #0d1b2a 100%);
    display: flex; align-items: center; justify-content: center;
    position: relative;
}
.profile-frame img {
    width: 100%; height: 100%; object-fit: cover;
    display: block;
}
.profile-frame-placeholder {
    display: flex; flex-direction: column;
    align-items: center; justify-content: center;
    gap: 10px; color: #8aaac8;
}
.profile-frame-placeholder .avatar-icon {
    font-size: 5rem; line-height: 1;
    filter: drop-shadow(0 2px 8px rgba(0,0,0,0.4));
}
.profile-frame-placeholder .placeholder-txt {
    font-size: 0.72rem; color: #6888aa;
    letter-spacing: 0.08em; text-transform: uppercase;
    text-align: center; padding: 0 12px;
}
.profile-gold-badge {
    position: absolute; bottom: 10px; left: 50%; transform: translateX(-50%);
    background: #e8a020; color: #0d1b2a;
    font-size: 0.65rem; font-weight: 800; letter-spacing: 0.1em;
    text-transform: uppercase; padding: 4px 14px; border-radius: 20px;
    white-space: nowrap;
}

.hero-right {
    display: flex; flex-direction: column; gap: 12px;
    min-width: 180px;
}
.stat-box {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: 14px; padding: 14px 20px; text-align: center;
}
.stat-num { font-size: 1.9rem; font-weight: 800; color: #e8a020; line-height: 1; }
.stat-lbl { font-size: 0.72rem; color: #8aaac8; margin-top: 3px; letter-spacing: 0.06em; text-transform: uppercase; }

/* ── SECTION HEADERS ── */
.sec-hdr {
    font-size: 1.2rem; font-weight: 700; color: #0d1b2a;
    border-left: 4px solid #e8a020;
    padding-left: 12px;
    margin: 8px 0 20px 0;
}

/* ── CARDS — creamy white, slightly transparent ── */
.card {
    background: rgba(255, 252, 245, 0.88);   /* ← creamy + transparent */
    border-radius: 14px;
    padding: 20px 24px; margin-bottom: 14px;
    border: 1px solid #e8e0d0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    backdrop-filter: blur(4px);
}

/* ── PILLS ── */
.pill {
    display: inline-block;
    background: #e8f0fb; color: #1a3a6b;
    border-radius: 20px; padding: 4px 13px;
    font-size: 0.78rem; font-weight: 500; margin: 3px 2px;
}
.pill-gold { background: #fff3d6; color: #a06800; }
.pill-green { background: #e2f5ea; color: #1a6b3a; }
.pill-mono {
    background: #f0f4fa; color: #2a4a7a;
    font-family: monospace; font-size: 0.75rem;
    padding: 3px 10px; border-radius: 6px;
    display: inline-block; margin: 2px;
    border: 1px solid #d4e0f0;
}

/* ── EXPERIENCE CARD — creamy ── */
.exp-card {
    background: rgba(255, 252, 245, 0.88);
    border-radius: 14px;
    padding: 20px 24px; margin-bottom: 14px;
    border: 1px solid #e8e0d0;
    border-left: 5px solid #1a3a6b;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    backdrop-filter: blur(4px);
}
.exp-title { font-size: 1rem; font-weight: 700; color: #0d1b2a; }
.exp-org { color: #4a6a9a; font-size: 0.88rem; }
.exp-meta { font-size: 0.78rem; color: #8a9ab0; margin-top: 2px; }

/* ── PROJECT CARD — creamy ── */
.proj-card {
    background: rgba(255, 252, 245, 0.88);
    border-radius: 14px;
    padding: 20px 24px; margin-bottom: 14px;
    border: 1px solid #e8e0d0;
    border-top: 4px solid #1a3a6b;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    backdrop-filter: blur(4px);
}

/* ── CERT CARD — creamy ── */
.cert-card {
    background: rgba(255, 252, 245, 0.88);
    border-radius: 14px;
    padding: 20px 22px; margin-bottom: 14px;
    border: 1px solid #e8e0d0;
    border-top: 4px solid #e8a020;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    text-align: center;
    backdrop-filter: blur(4px);
}

/* ── VIDEO CARD — creamy ── */
.vid-card {
    background: rgba(255, 252, 245, 0.88);
    border-radius: 14px;
    padding: 20px 24px; margin-bottom: 14px;
    border: 1px solid #e8e0d0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
    overflow: hidden;
    backdrop-filter: blur(4px);
}
.vid-badge {
    display: inline-block;
    background: #e8f0fb; color: #1a3a6b;
    font-size: 0.7rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.1em;
    padding: 3px 10px; border-radius: 20px;
    margin-bottom: 8px;
}
.vid-thumb {
    width: 100%; border-radius: 10px;
    aspect-ratio: 16/9; object-fit: cover;
    background: #0d1b2a;
}
.vid-title { font-size: 0.95rem; font-weight: 700; color: #0d1b2a; margin: 10px 0 4px; }
.vid-desc  { font-size: 0.82rem; color: #5a6a7a; line-height: 1.6; }

/* ── CONTACT ── */
.contact-info-row {
    display: flex; align-items: center; gap: 10px;
    padding: 10px 0;
    border-bottom: 1px solid #f0f4f9;
    font-size: 0.9rem; color: #3a5a7a;
}
.contact-icon { font-size: 1.1rem; width: 28px; text-align: center; }

/* ── FOOTER ── */
.footer {
    text-align: center; padding: 24px 0 8px;
    color: #8a9ab0; font-size: 0.8rem;
    border-top: 1px solid #e2eaf4; margin-top: 40px;
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# TOP NAVIGATION BAR
# ══════════════════════════════════════════════
st.markdown("""
<div class="topnav">
    <a class="nav-btn" href="#about">👤 About</a>
    <a class="nav-btn" href="#skills">🛠 Skills</a>
    <a class="nav-btn" href="#experience">💼 Experience</a>
    <a class="nav-btn" href="#projects">🚀 Projects</a>
    <a class="nav-btn" href="#videos">🎬 Teaching Videos</a>
    <a class="nav-btn" href="#education">🎓 Education</a>
    <a class="nav-btn" href="#certifications">📜 Certifications</a>
    <a class="nav-btn" href="#contact">📬 Contact</a>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# LOAD PROFILE PICTURE (if present)
# ══════════════════════════════════════════════
def get_profile_img_html():
    """Returns img tag with base64 data if profile.jpg/png exists, else placeholder."""
    for fname in ["profilepic.jpg", "profilepic.jpeg", "profilepic.png", "photopic.jpg", "photopic.png"]:
        fpath = os.path.join(os.path.dirname(__file__), fname)
        if os.path.exists(fpath):
            with open(fpath, "rb") as f:
                data = base64.b64encode(f.read()).decode()
            ext = fname.rsplit(".", 1)[-1].replace("jpeg", "jpg")
            mime = "image/jpeg" if ext == "jpg" else "image/png"
            return f'<img src="data:{mime};base64,{data}" alt="Raju Devnath"/>'
    # Placeholder
    return """
        <div class="profile-frame-placeholder">
            <div class="avatar-icon">🧑‍💻</div>
            <div class="placeholder-txt">Replace with<br>your photo</div>
        </div>
    """

profile_content = get_profile_img_html()


# ══════════════════════════════════════════════
# HERO — Name + Bio | Profile Photo | Stats
# ══════════════════════════════════════════════
st.markdown(f"""
<div class="hero-wrap">
    <div class="hero-left">
        <div class="hero-name">Raju Devnath</div>
        <div class="hero-role">📊 Data Science Instructor &nbsp;·&nbsp; 🤖 AI/ML Mentor &nbsp;·&nbsp; 🐍 Python &amp; SQL Educator</div>
        <div class="hero-loc">📍 Guwahati, India &nbsp;·&nbsp; Open to Teaching &amp; Analyst Roles</div>
        <div class="hero-bio">
            Passionate educator &amp; practitioner with <strong style="color:#e8c87a;">4+ years</strong> of teaching
            and hands-on Data Science industry experience. Trained
            <strong style="color:#e8c87a;">2,000+ students</strong> across offline classrooms,
            online platforms, bootcamps &amp; corporate workshops —
            turning complex concepts into practical, job-ready skills.
        </div>
        <div class="hero-links">
            <a class="hlink" href="mailto:rjnath98@gmail.com">📧 Email Me</a>
            <a class="hlink" href="#">🔗 LinkedIn</a>
            <a class="hlink" href="#">💻 GitHub</a>
            <a class="hlink" href="#">🌐 Portfolio</a>
        </div>
    </div>

    <!-- ── PROFILE PICTURE FRAME ── -->
    <div class="hero-center">
        <div class="profile-frame">
            {profile_content}
            <div class="profile-gold-badge">Data Scientist</div>
        </div>
    </div>

    <div class="hero-right">
        <div class="stat-box"><div class="stat-num">2,000+</div><div class="stat-lbl">Students Taught</div></div>
        <div class="stat-box"><div class="stat-num">700+</div><div class="stat-lbl">Offline Learners</div></div>
        <div class="stat-box"><div class="stat-num">4+ Yrs</div><div class="stat-lbl">Teaching Exp.</div></div>
        <div class="stat-box"><div class="stat-num">5+</div><div class="stat-lbl">Subjects Taught</div></div>
    </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# ABOUT
# ══════════════════════════════════════════════
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.markdown('<div class="sec-hdr">👤 About Me</div>', unsafe_allow_html=True)

c1, c2 = st.columns([3, 2], gap="large")
with c1:
    st.markdown("""
    <div class="card">
        <p style="color:#3a4a5a; line-height:1.85; font-size:0.93rem; margin:0;">
        I'm a <strong>Data Science Instructor, AI/ML Mentor</strong>, and <strong>Data Analyst</strong>
        based in Guwahati, India. With a B.Tech in Computer Science from Lovely Professional University,
        I bridge the gap between academic learning and real-world industry practice.
        <br><br>
        As a <strong>Subject Matter Expert on CheggExpert</strong>, I've answered 1,000+ queries from students
        across universities in India, USA, and UK. Previously I personally taught
        <strong>700+ students offline</strong> in Mathematics and Computer Science fundamentals.
        <br><br>
        At <strong>Allsoft Solutions</strong>, I work as a Data Science Trainee — building ML models,
        writing optimised SQL queries, and creating BI dashboards — experience I bring directly into my teaching.
        <br><br>
        My philosophy: <em style="color:#1a3a6b;">"Learn by building real things."</em> Every session is
        project-driven, practical, and mapped to industry standards.
        </p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card" style="margin-bottom:14px;">
        <div style="font-weight:700; color:#1a3a6b; font-size:0.92rem; margin-bottom:12px;">🎯 What I Offer</div>
        <ul style="color:#3a5a7a; line-height:2; font-size:0.88rem; padding-left:18px; margin:0;">
            <li>Industry-standard practical curriculum</li>
            <li>Live coding with real datasets</li>
            <li>End-to-end project mentoring</li>
            <li>1-on-1 doubt resolution</li>
            <li>Bootcamp &amp; workshop design</li>
            <li>Corporate training delivery</li>
        </ul>
    </div>
    <div class="card" style="margin-bottom:0;">
        <div style="font-weight:700; color:#1a3a6b; font-size:0.92rem; margin-bottom:10px;">🏷 Core Domains</div>
        <span class="pill">Data Science</span><span class="pill">Machine Learning</span>
        <span class="pill">AI</span><span class="pill">Python</span><span class="pill">SQL</span>
        <span class="pill">Tableau</span><span class="pill">Excel</span><span class="pill">Statistics</span>
        <span class="pill">Mathematics</span><span class="pill">NLP</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# SKILLS
# ══════════════════════════════════════════════
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.markdown('<div class="sec-hdr">🛠 Technical Skills</div>', unsafe_allow_html=True)

skills = [
    ("🐍", "Languages",       ["Python", "SQL", "R", "HTML", "CSS", "JavaScript"]),
    ("📊", "Data Analysis",   ["Pandas", "NumPy", "EDA", "Data Wrangling", "Statistical Analysis"]),
    ("🤖", "ML / AI",         ["Scikit-learn", "XGBoost", "Regression", "Classification", "NLP", "Feature Engineering"]),
    ("📉", "Visualisation",   ["Tableau", "Power BI", "Matplotlib", "Seaborn", "Excel Dashboards"]),
    ("🗄", "Databases",       ["MySQL", "MongoDB", "PostgreSQL", "Query Optimisation", "DBMS"]),
    ("☁️", "Cloud & Tools",   ["AWS S3", "AWS EC2", "Git/GitHub", "Docker", "Streamlit", "Jupyter"]),
    ("🎓", "Teaching Tools",  ["Google Colab", "Zoom/Meet LMS", "Curriculum Design", "Assessment Design"]),
    ("🧮", "Mathematics",     ["Linear Algebra", "Probability", "Statistics", "Discrete Maths", "Calculus"]),
]

cols = st.columns(4, gap="small")
for i, (icon, cat, items) in enumerate(skills):
    with cols[i % 4]:
        pills = "".join([f'<span class="pill-mono">{p}</span>' for p in items])
        st.markdown(f"""
        <div class="card" style="min-height:170px; margin-bottom:12px;">
            <div style="font-size:1.5rem; margin-bottom:6px;">{icon}</div>
            <div style="font-size:0.7rem; text-transform:uppercase; letter-spacing:0.1em;
                        color:#e8a020; font-weight:700; margin-bottom:8px;">{cat}</div>
            <div>{pills}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# EXPERIENCE
# ══════════════════════════════════════════════
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.markdown('<div class="sec-hdr">💼 Work Experience</div>', unsafe_allow_html=True)

exps = [
    {
        "color": "#1a3a6b", "badge": "#e8f0fb", "badge_tc": "#1a3a6b", "type": "Industry",
        "role": "Data Science Trainee", "org": "Allsoft Solutions Pvt. Ltd.", "period": "March 2024 – Present",
        "points": [
            "Gathered & cleaned data from multiple sources ensuring high quality for ML modeling and analysis.",
            "Built and deployed ML models (regression, classification) improving business KPI forecast accuracy.",
            "Developed optimised SQL queries for large-scale dataset management and BI reporting.",
            "Created Tableau & Excel dashboards adopted by management for weekly data-driven reporting.",
            "Conducted internal Python, SQL, EDA & Tableau training sessions for junior team members.",
        ]
    },
    {
        "color": "#e8a020", "badge": "#fff3d6", "badge_tc": "#a06800", "type": "Teaching",
        "role": "Subject Matter Expert — Online Tutor", "org": "CheggExpert (Global Platform)", "period": "2021 – Present",
        "points": [
            "Resolved 1,000+ student queries in Python, SQL, Data Science & Maths across universities in India, USA & UK.",
            "Maintained top accuracy rating by delivering structured, step-by-step explanations for all levels.",
            "Built expertise translating complex ML and analytics concepts into easy, clear answers.",
        ]
    },
    {
        "color": "#2e8b57", "badge": "#e2f5ea", "badge_tc": "#1a6b3a", "type": "Teaching",
        "role": "Instructor — Maths & Computer Science", "org": "Independent / Community Teaching", "period": "May 2018 – Dec 2020",
        "points": [
            "Taught 700+ students across multiple offline batches in Mathematics, CS fundamentals & programming basics.",
            "Designed lesson plans, assessments, and hands-on practicals for varying skill levels.",
            "Conducted doubt-clearing sessions & mock tests — consistently rated highly by students and parents.",
        ]
    },
]

for e in exps:
    pts = "".join([f"<li style='margin-bottom:6px;color:#3a4a5a;font-size:0.88rem;'>{p}</li>" for p in e["points"]])
    st.markdown(f"""
    <div class="exp-card" style="border-left-color:{e['color']};">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-bottom:10px;">
            <div>
                <span class="exp-title">{e['role']}</span>
                <span class="exp-org"> &nbsp;·&nbsp; {e['org']}</span>
            </div>
            <div style="display:flex; gap:8px; align-items:center;">
                <span style="background:{e['badge']}; color:{e['badge_tc']}; padding:3px 12px;
                             border-radius:20px; font-size:0.72rem; font-weight:700;">{e['type']}</span>
                <span class="exp-meta">📅 {e['period']}</span>
            </div>
        </div>
        <ul style="padding-left:18px; margin:0;">{pts}</ul>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# PROJECTS
# ══════════════════════════════════════════════
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.markdown('<div class="sec-hdr">🚀 Projects</div>', unsafe_allow_html=True)

projects = [
    {
        "title": "Retail Sales Performance Dashboard",
        "cat": "Data Analyst Project", "year": "2024", "color": "#1a3a6b",
        "tech": ["Python", "MySQL", "Tableau", "Pandas", "EDA", "Time-Series"],
        "desc": "Analyzed 2+ years of retail transaction data (50K+ records) to uncover sales trends, customer segments, and revenue KPIs.",
        "points": [
            "Interactive Tableau dashboard tracking revenue growth, avg order value, top SKUs — adopted for weekly management reporting.",
            "Time-series forecasting achieved 92% accuracy, enabling data-driven inventory and budget planning.",
            "Automated Python + MySQL data pipeline reducing manual reporting effort by 60%.",
        ]
    },
    {
        "title": "Data Analytics Bootcamp — End-to-End Program",
        "cat": "Teaching / Training Project", "year": "2023–24", "color": "#e8a020",
        "tech": ["Curriculum Design", "Python", "SQL", "Tableau", "Excel", "Streamlit"],
        "desc": "Designed and conducted a 6-week Data Analytics Bootcamp for 80+ students and working professionals.",
        "points": [
            "Structured curriculum with real datasets and capstone project — 95% completion rate, 4.8/5 avg feedback.",
            "Live Zoom sessions + recorded modules + 1-on-1 mentoring.",
            "30+ participants secured data-related roles or promotions post-bootcamp.",
        ]
    },
    {
        "title": "Customer Churn Prediction — ML Pipeline",
        "cat": "Machine Learning", "year": "2024", "color": "#2e8b57",
        "tech": ["Python", "Scikit-learn", "XGBoost", "SMOTE", "SQL", "Streamlit"],
        "desc": "End-to-end ML pipeline predicting telecom customer churn on 100K+ records.",
        "points": [
            "87% accuracy, 0.91 AUC-ROC using XGBoost + SMOTE for class imbalance.",
            "Deployed as interactive Streamlit web app for real-time churn risk scoring.",
            "Automated retraining pipeline reducing manual intervention by 60%.",
        ]
    },
    {
        "title": "Pizza Sales Analytics Dashboard",
        "cat": "Data Visualisation", "year": "2023", "color": "#7b3fa0",
        "tech": ["EDA", "MySQL", "Tableau", "KPI", "Git"],
        "desc": "Analyzed 2-year Pizza Sales dataset (50K+ transactions) to uncover sales trends and KPIs.",
        "points": [
            "Dynamic Tableau dashboard tracking revenue, avg order value, best-selling SKUs.",
            "Sales forecasting with 92% accuracy for budget and inventory planning.",
            "Used as live classroom teaching material for EDA & visualisation storytelling.",
        ]
    },
    {
        "title": "WhatsApp Chat Sentiment Analyser",
        "cat": "NLP / Web App", "year": "2023", "color": "#c0392b",
        "tech": ["Python", "NLP", "Streamlit", "WordCloud", "Git"],
        "desc": "NLP-powered web app for sentiment analysis, emoji trends, and conversation pattern analysis.",
        "points": [
            "WordCloud visualisation and message frequency analysis for conversation insights.",
            "Deployed on Streamlit Cloud — 200+ active users.",
            "Used as student capstone demo for end-to-end data product development.",
        ]
    },
    {
        "title": "Coffee Shop Sales Dashboard",
        "cat": "Business Intelligence", "year": "2023", "color": "#d4890a",
        "tech": ["MS Excel", "Pivot Tables", "BeautifulSoup", "KPI"],
        "desc": "Multi-location sales performance dashboard covering 5 store locations.",
        "points": [
            "Scraped market data using BeautifulSoup; integrated with internal sales records.",
            "Identified peak sales windows and top-performing SKUs for marketing strategy.",
        ]
    },
]

c1, c2 = st.columns(2, gap="medium")
for i, p in enumerate(projects):
    col = c1 if i % 2 == 0 else c2
    with col:
        tech_html = "".join([f'<span class="pill-mono">{t}</span>' for t in p["tech"]])
        pts_html  = "".join([f"<li style='margin-bottom:5px;color:#3a4a5a;font-size:0.85rem;'>{x}</li>" for x in p["points"]])
        st.markdown(f"""
        <div class="proj-card" style="border-top-color:{p['color']};">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
                <span style="font-size:0.7rem; text-transform:uppercase; letter-spacing:0.1em;
                             color:{p['color']}; font-weight:700;">{p['cat']}</span>
                <span style="color:#8a9ab0; font-size:0.76rem;">📅 {p['year']}</span>
            </div>
            <div style="font-size:0.98rem; font-weight:700; color:#0d1b2a; margin-bottom:6px;">{p['title']}</div>
            <p style="color:#5a6a7a; font-size:0.85rem; line-height:1.6; margin-bottom:10px;">{p['desc']}</p>
            <div style="margin-bottom:10px;">{tech_html}</div>
            <ul style="padding-left:18px; margin:0;">{pts_html}</ul>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# INTRODUCTORY TEACHING VIDEOS
# ══════════════════════════════════════════════
st.markdown('<div id="videos"></div>', unsafe_allow_html=True)
st.markdown('<div class="sec-hdr">🎬 Introductory Teaching Videos</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card" style="margin-bottom:18px; background:rgba(248,251,255,0.9); border: 1px dashed #b0c8e8;">
    <p style="color:#3a5a7a; font-size:0.9rem; margin:0; line-height:1.7;">
    🎙 <strong>Watch me teach.</strong> These introductory sessions give you a taste of how I break down
    complex data science topics into simple, practical lessons. Each video is a standalone micro-lesson
    designed for beginners and working professionals alike.
    <br><span style="color:#8a9ab0; font-size:0.82rem;">
    💡 Replace the YouTube embed links below with your actual video URLs before publishing.</span>
    </p>
</div>
""", unsafe_allow_html=True)

videos = [
    {
        "badge": "Python Basics",
        "title": "Intro to Python for Data Science",
        "desc": "Learn variables, data types, loops, and functions in Python with hands-on examples using real datasets. Perfect for absolute beginners.",
        "duration": "⏱ 18 min", "level": "🟢 Beginner",
        "url": "https://www.youtube.com/embed/rfscVS0vtbw",
        "topics": ["Variables & Types", "Loops", "Functions", "Lists & Dicts"],
    },
    {
        "badge": "SQL Fundamentals",
        "title": "SQL for Data Analysis — Zero to Query",
        "desc": "Understand SELECT, WHERE, GROUP BY, JOINs and aggregations using a real sales database. Start writing useful queries in under 20 minutes.",
        "duration": "⏱ 22 min", "level": "🟢 Beginner",
        "url": "https://www.youtube.com/embed/HXV3zeQKqGY",
        "topics": ["SELECT & WHERE", "GROUP BY", "JOINs", "Aggregations"],
    },
    {
        "badge": "Machine Learning",
        "title": "Your First ML Model in Python",
        "desc": "Build and evaluate a classification model using Scikit-learn step by step — from loading data to measuring accuracy. No maths degree required.",
        "duration": "⏱ 25 min", "level": "🟡 Intermediate",
        "url": "https://www.youtube.com/embed/pqNCD_5r0IU",
        "topics": ["Scikit-learn", "Train/Test Split", "Logistic Regression", "Accuracy Score"],
    },
    {
        "badge": "Data Visualisation",
        "title": "Tableau Dashboard from Scratch",
        "desc": "Connect to a dataset, create charts, build KPIs, and publish a professional interactive dashboard in Tableau Public — all in one session.",
        "duration": "⏱ 20 min", "level": "🟢 Beginner",
        "url": "https://www.youtube.com/embed/jEgVto5QME8",
        "topics": ["Connecting Data", "Bar & Line Charts", "KPI Cards", "Filters & Dashboard"],
    },
    {
        "badge": "Pandas & EDA",
        "title": "Exploratory Data Analysis with Pandas",
        "desc": "Learn how to load, clean, explore, and summarise a real dataset using Pandas. Covers null handling, groupby, and visualising distributions.",
        "duration": "⏱ 20 min", "level": "🟢 Beginner",
        "url": "https://www.youtube.com/embed/vmEHCJofslg",
        "topics": ["read_csv", "describe()", "Null Handling", "groupby & plot"],
    },
    {
        "badge": "Excel for Analysts",
        "title": "Excel Pivot Tables & Dashboards",
        "desc": "Turn raw data into a management-ready dashboard using Pivot Tables, charts, slicers, and conditional formatting — no formulas panic.",
        "duration": "⏱ 16 min", "level": "🟢 Beginner",
        "url": "https://www.youtube.com/embed/m13o5aqeCbM",
        "topics": ["Pivot Tables", "Slicers", "Charts", "Conditional Formatting"],
    },
]

v_cols = st.columns(3, gap="medium")
for i, v in enumerate(videos):
    with v_cols[i % 3]:
        topic_pills = "".join([f'<span class="pill" style="font-size:0.72rem;">{t}</span>' for t in v["topics"]])
        st.markdown(f"""
        <div class="vid-card">
            <span class="vid-badge">{v['badge']}</span>
            <div style="position:relative; padding-bottom:56.25%; height:0; overflow:hidden; border-radius:10px; margin-bottom:12px;">
                <iframe src="{v['url']}"
                    style="position:absolute;top:0;left:0;width:100%;height:100%;border:none;border-radius:10px;"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen>
                </iframe>
            </div>
            <div class="vid-title">{v['title']}</div>
            <div style="display:flex; gap:8px; margin:6px 0 8px;">
                <span style="font-size:0.76rem; color:#5a7a9a;">{v['duration']}</span>
                <span style="font-size:0.76rem; color:#5a7a9a;">{v['level']}</span>
            </div>
            <div class="vid-desc">{v['desc']}</div>
            <div style="margin-top:10px;">{topic_pills}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# TEACHING HIGHLIGHTS
# ══════════════════════════════════════════════
st.markdown('<div class="sec-hdr">🏅 Teaching Expertise</div>', unsafe_allow_html=True)

c1, c2 = st.columns(2, gap="medium")
with c1:
    st.markdown("""
    <div class="card">
        <div style="font-weight:700; color:#1a3a6b; font-size:0.92rem; margin-bottom:12px;">📚 Subjects Taught</div>
        <span class="pill">Python Programming</span><span class="pill">SQL &amp; Databases</span>
        <span class="pill">Machine Learning</span><span class="pill">AI Fundamentals</span>
        <span class="pill">Data Analysis</span><span class="pill">Tableau</span>
        <span class="pill">MS Excel</span><span class="pill">Statistics</span>
        <span class="pill">Mathematics</span><span class="pill">NLP</span>
    </div>""", unsafe_allow_html=True)
with c2:
    st.markdown("""
    <div class="card">
        <div style="font-weight:700; color:#1a3a6b; font-size:0.92rem; margin-bottom:12px;">🎙 Delivery Modes</div>
        <span class="pill pill-gold">Online LMS</span>
        <span class="pill pill-gold">Live Zoom/Meet</span>
        <span class="pill pill-gold">Offline Classroom</span>
        <span class="pill pill-gold">Workshops</span>
        <span class="pill pill-gold">1-on-1 Mentoring</span>
        <span class="pill pill-gold">Corporate Training</span>
        <span class="pill pill-gold">Bootcamps</span>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# EDUCATION
# ══════════════════════════════════════════════
st.markdown('<div id="education"></div>', unsafe_allow_html=True)
st.markdown('<div class="sec-hdr">🎓 Education</div>', unsafe_allow_html=True)

st.markdown("""
<div class="exp-card" style="border-left-color:#1a3a6b;">
    <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:8px; margin-bottom:10px;">
        <div>
            <div class="exp-title">B.Tech — Computer Science &amp; Engineering</div>
            <div class="exp-org">🏛 Lovely Professional University, Phagwara, Punjab</div>
        </div>
        <div style="text-align:right;">
            <span style="background:#e8f0fb; color:#1a3a6b; padding:3px 12px;
                         border-radius:20px; font-size:0.76rem; font-weight:600;">2020 – 2024</span>
            <div style="color:#e8a020; font-weight:700; font-size:0.88rem; margin-top:6px;">CGPA: 7.2</div>
        </div>
    </div>
    <div>
        <span style="font-size:0.8rem; color:#5a6a7a; margin-right:4px;">Relevant Coursework:</span>
        <span class="pill">Data Structures</span><span class="pill">DBMS</span>
        <span class="pill">Machine Learning</span><span class="pill">Statistics</span>
        <span class="pill">Computer Networks</span><span class="pill">Software Engineering</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# CERTIFICATIONS
# ══════════════════════════════════════════════
st.markdown('<div id="certifications"></div>', unsafe_allow_html=True)
st.markdown('<div class="sec-hdr">📜 Certifications</div>', unsafe_allow_html=True)

certs = [
    ("📊", "Data Visualization with Tableau Specialization", "Coursera", "2023", "#1a3a6b"),
    ("📈", "Creating Charts & Dashboards in MS Excel",       "Coursera", "2023", "#2e8b57"),
    ("☕", "Summer Training in Java",                        "Hitbullseye", "2022", "#e8a020"),
]
cols = st.columns(3, gap="medium")
for i, (icon, name, issuer, year, color) in enumerate(certs):
    with cols[i]:
        st.markdown(f"""
        <div class="cert-card" style="border-top-color:{color};">
            <div style="font-size:2rem; margin-bottom:8px;">{icon}</div>
            <div style="font-weight:700; color:#0d1b2a; font-size:0.92rem; margin-bottom:6px; line-height:1.4;">{name}</div>
            <div style="color:#4a6a9a; font-size:0.82rem; margin-bottom:8px;">🏢 {issuer}</div>
            <span style="background:#f0f4fa; color:#4a5a7a; padding:3px 12px;
                         border-radius:20px; font-size:0.74rem;">📅 {year}</span>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)


# ══════════════════════════════════════════════
# CONTACT
# ══════════════════════════════════════════════
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.markdown('<div class="sec-hdr">📬 Contact Me</div>', unsafe_allow_html=True)

c1, c2 = st.columns([3, 2], gap="large")
with c1:
    st.markdown("""
    <div class="card" style="margin-bottom:14px;">
        <p style="color:#3a4a5a; line-height:1.8; font-size:0.92rem; margin:0;">
        Interested in having me as an <strong>instructor, mentor, or data analyst</strong>?
        Whether it's a teaching role, freelance analytics project, workshop, or full-time position
        — drop me a message and I'll get back to you within 24 hours.
        </p>
    </div>
    """, unsafe_allow_html=True)
    with st.form("contact_form"):
        n_col, e_col = st.columns(2)
        with n_col:
            name  = st.text_input("Your Name", placeholder="John Doe")
        with e_col:
            email = st.text_input("Your Email", placeholder="you@email.com")
        subj = st.selectbox("Purpose", [
            "Teaching / Instructor Role",
            "Data Analyst Role",
            "Workshop / Bootcamp",
            "1-on-1 Mentoring",
            "Corporate Training",
            "Other"
        ])
        msg = st.text_area("Message", height=110, placeholder="Tell me about the opportunity or what you need...")
        submitted = st.form_submit_button("✉️ Send Message", use_container_width=True)
        if submitted:
            if name and email and msg:
                st.success(f"✅ Thanks {name}! I'll get back to you at **{email}** soon.")
            else:
                st.warning("Please fill in all fields before sending.")

with c2:
    st.markdown("""
    <div class="card">
        <div style="font-weight:700; color:#1a3a6b; font-size:0.95rem; margin-bottom:16px;">📋 Contact Details</div>
        <div class="contact-info-row">
            <span class="contact-icon">📧</span>
            <a href="mailto:rjnath98@gmail.com" style="color:#1a3a6b; font-weight:500; text-decoration:none;">rjnath98@gmail.com</a>
        </div>
        <div class="contact-info-row">
            <span class="contact-icon">📞</span>
            <span>+91-7002141483</span>
        </div>
        <div class="contact-info-row">
            <span class="contact-icon">📍</span>
            <span>Guwahati, Assam, India</span>
        </div>
        <div class="contact-info-row" style="border:none;">
            <span class="contact-icon">🕐</span>
            <span style="color:#2e8b57; font-weight:600;">Available for new opportunities</span>
        </div>
        <div style="margin-top:16px; display:flex; flex-direction:column; gap:8px;">
            <a href="#" style="display:block; background:#0a66c2; color:white; text-align:center;
               padding:9px; border-radius:8px; text-decoration:none; font-size:0.85rem; font-weight:600;">
               🔗 LinkedIn Profile
            </a>
            <a href="#" style="display:block; background:#0d1b2a; color:white; text-align:center;
               padding:9px; border-radius:8px; text-decoration:none; font-size:0.85rem; font-weight:600;">
               💻 GitHub Profile
            </a>
            <a href="#" style="display:block; background:#e8a020; color:#0d1b2a; text-align:center;
               padding:9px; border-radius:8px; text-decoration:none; font-size:0.85rem; font-weight:600;">
               🌐 Full Portfolio Site
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════
st.markdown("""
<div class="footer">
    © 2024 Raju Devnath &nbsp;·&nbsp; Data Science Instructor &amp; Analyst &nbsp;·&nbsp; Built with Streamlit<br>
    <span style="font-size:0.75rem;">📍 Guwahati, India &nbsp;·&nbsp; 📧 rjnath98@gmail.com</span>
</div>
""", unsafe_allow_html=True)

################################################################################################################


# import streamlit as st

# st.set_page_config(
#     page_title="Raju Devnath | Portfolio",
#     page_icon="📊",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# # ══════════════════════════════════════════════
# # GLOBAL STYLES
# # ══════════════════════════════════════════════
# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

# html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

# .main { background: #f0f4f9; }
# .main .block-container { padding: 1.5rem 2.5rem 3rem 2.5rem; max-width: 1120px; }

# /* Hide Streamlit chrome */
# #MainMenu, footer, header { visibility: hidden; }

# /* ── NAV BAR ── */
# .topnav {
#     display: flex; align-items: center; justify-content: center;
#     gap: 6px; flex-wrap: wrap;
#     background: #ffffff;
#     border-radius: 50px;
#     padding: 10px 20px;
#     margin-bottom: 28px;
#     box-shadow: 0 2px 16px rgba(0,0,0,0.07);
#     border: 1px solid #e2eaf4;
# }
# .nav-btn {
#     background: transparent; border: none;
#     color: #3a5a8a; font-size: 0.82rem;
#     font-weight: 600; padding: 7px 16px;
#     border-radius: 30px; cursor: pointer;
#     text-decoration: none; letter-spacing: 0.03em;
#     transition: background 0.2s, color 0.2s;
#     white-space: nowrap;
# }
# .nav-btn:hover { background: #e8f0fb; color: #1a3a6b; }

# /* ── HERO CARD ── */
# .hero-wrap {
#     background: linear-gradient(135deg, #0d1b2a 0%, #1b3d72 100%);
#     border-radius: 20px;
#     padding: 36px 40px;
#     margin-bottom: 24px;
#     display: flex; align-items: flex-start;
#     justify-content: space-between;
#     gap: 32px; flex-wrap: wrap;
# }
# .hero-left { flex: 1; min-width: 260px; }
# .hero-name {
#     font-size: 2.6rem; font-weight: 800;
#     color: #ffffff; line-height: 1.1; margin: 0 0 8px 0;
# }
# .hero-role { font-size: 0.98rem; color: #a8c4e8; font-weight: 400; margin-bottom: 6px; }
# .hero-loc  { font-size: 0.83rem; color: #6888aa; margin-bottom: 16px; }
# .hero-bio  { font-size: 0.92rem; color: #c0d4ec; line-height: 1.75; max-width: 500px; }
# .hero-links {
#     display: flex; gap: 10px; margin-top: 20px; flex-wrap: wrap;
# }
# .hlink {
#     background: rgba(255,255,255,0.1);
#     border: 1px solid rgba(255,255,255,0.18);
#     color: #ffffff !important; font-size: 0.82rem; font-weight: 600;
#     padding: 7px 18px; border-radius: 30px;
#     text-decoration: none !important;
#     transition: background 0.2s;
# }
# .hlink:hover { background: rgba(232,160,32,0.3); }
# .hero-right {
#     display: flex; flex-direction: column; gap: 12px;
#     min-width: 180px;
# }
# .stat-box {
#     background: rgba(255,255,255,0.07);
#     border: 1px solid rgba(255,255,255,0.12);
#     border-radius: 14px; padding: 14px 20px; text-align: center;
# }
# .stat-num { font-size: 1.9rem; font-weight: 800; color: #e8a020; line-height: 1; }
# .stat-lbl { font-size: 0.72rem; color: #8aaac8; margin-top: 3px; letter-spacing: 0.06em; text-transform: uppercase; }

# /* ── SECTION HEADERS ── */
# .sec-hdr {
#     font-size: 1.2rem; font-weight: 700; color: #0d1b2a;
#     border-left: 4px solid #e8a020;
#     padding-left: 12px;
#     margin: 8px 0 20px 0;
# }

# /* ── CARDS ── */
# .card {
#     background: #ffffff; border-radius: 14px;
#     padding: 20px 24px; margin-bottom: 14px;
#     border: 1px solid #e2eaf4;
#     box-shadow: 0 2px 8px rgba(0,0,0,0.04);
# }

# /* ── PILLS ── */
# .pill {
#     display: inline-block;
#     background: #e8f0fb; color: #1a3a6b;
#     border-radius: 20px; padding: 4px 13px;
#     font-size: 0.78rem; font-weight: 500; margin: 3px 2px;
# }
# .pill-gold { background: #fff3d6; color: #a06800; }
# .pill-green { background: #e2f5ea; color: #1a6b3a; }
# .pill-mono {
#     background: #f0f4fa; color: #2a4a7a;
#     font-family: monospace; font-size: 0.75rem;
#     padding: 3px 10px; border-radius: 6px;
#     display: inline-block; margin: 2px;
#     border: 1px solid #d4e0f0;
# }

# /* ── EXPERIENCE CARD ── */
# .exp-card {
#     background: #ffffff; border-radius: 14px;
#     padding: 20px 24px; margin-bottom: 14px;
#     border: 1px solid #e2eaf4;
#     border-left: 5px solid #1a3a6b;
#     box-shadow: 0 2px 8px rgba(0,0,0,0.04);
# }
# .exp-title { font-size: 1rem; font-weight: 700; color: #0d1b2a; }
# .exp-org { color: #4a6a9a; font-size: 0.88rem; }
# .exp-meta { font-size: 0.78rem; color: #8a9ab0; margin-top: 2px; }

# /* ── PROJECT CARD ── */
# .proj-card {
#     background: #ffffff; border-radius: 14px;
#     padding: 20px 24px; margin-bottom: 14px;
#     border: 1px solid #e2eaf4;
#     border-top: 4px solid #1a3a6b;
#     box-shadow: 0 2px 8px rgba(0,0,0,0.04);
# }

# /* ── CERT CARD ── */
# .cert-card {
#     background: #ffffff; border-radius: 14px;
#     padding: 20px 22px; margin-bottom: 14px;
#     border: 1px solid #e2eaf4;
#     border-top: 4px solid #e8a020;
#     box-shadow: 0 2px 8px rgba(0,0,0,0.04);
#     text-align: center;
# }

# /* ── VIDEO CARD ── */
# .vid-card {
#     background: #ffffff; border-radius: 14px;
#     padding: 20px 24px; margin-bottom: 14px;
#     border: 1px solid #e2eaf4;
#     box-shadow: 0 2px 8px rgba(0,0,0,0.04);
#     overflow: hidden;
# }
# .vid-badge {
#     display: inline-block;
#     background: #e8f0fb; color: #1a3a6b;
#     font-size: 0.7rem; font-weight: 700;
#     text-transform: uppercase; letter-spacing: 0.1em;
#     padding: 3px 10px; border-radius: 20px;
#     margin-bottom: 8px;
# }
# .vid-thumb {
#     width: 100%; border-radius: 10px;
#     aspect-ratio: 16/9; object-fit: cover;
#     background: #0d1b2a;
# }
# .vid-title { font-size: 0.95rem; font-weight: 700; color: #0d1b2a; margin: 10px 0 4px; }
# .vid-desc  { font-size: 0.82rem; color: #5a6a7a; line-height: 1.6; }

# /* ── CONTACT ── */
# .contact-info-row {
#     display: flex; align-items: center; gap: 10px;
#     padding: 10px 0;
#     border-bottom: 1px solid #f0f4f9;
#     font-size: 0.9rem; color: #3a5a7a;
# }
# .contact-icon { font-size: 1.1rem; width: 28px; text-align: center; }

# /* ── FOOTER ── */
# .footer {
#     text-align: center; padding: 24px 0 8px;
#     color: #8a9ab0; font-size: 0.8rem;
#     border-top: 1px solid #e2eaf4; margin-top: 40px;
# }
# </style>
# """, unsafe_allow_html=True)


# # ══════════════════════════════════════════════
# # TOP NAVIGATION BAR
# # ══════════════════════════════════════════════
# st.markdown("""
# <div class="topnav">
#     <a class="nav-btn" href="#about">👤 About</a>
#     <a class="nav-btn" href="#skills">🛠 Skills</a>
#     <a class="nav-btn" href="#experience">💼 Experience</a>
#     <a class="nav-btn" href="#projects">🚀 Projects</a>
#     <a class="nav-btn" href="#videos">🎬 Teaching Videos</a>
#     <a class="nav-btn" href="#education">🎓 Education</a>
#     <a class="nav-btn" href="#certifications">📜 Certifications</a>
#     <a class="nav-btn" href="#contact">📬 Contact</a>
# </div>
# """, unsafe_allow_html=True)


# # ══════════════════════════════════════════════
# # HERO — Name + Bio on left | Quick Links + Stats on right
# # ══════════════════════════════════════════════
# st.markdown("""
# <div class="hero-wrap">
#     <div class="hero-left">
#         <div class="hero-name">Raju Devnath</div>
#         <div class="hero-role">📊 Data Science Instructor &nbsp;·&nbsp; 🤖 AI/ML Mentor &nbsp;·&nbsp; 🐍 Python &amp; SQL Educator</div>
#         <div class="hero-loc">📍 Guwahati, India &nbsp;·&nbsp; Open to Teaching &amp; Analyst Roles</div>
#         <div class="hero-bio">
#             Passionate educator &amp; practitioner with <strong style="color:#e8c87a;">4+ years</strong> of teaching
#             and hands-on Data Science industry experience. Trained
#             <strong style="color:#e8c87a;">2,000+ students</strong> across offline classrooms,
#             online platforms, bootcamps &amp; corporate workshops —
#             turning complex concepts into practical, job-ready skills.
#         </div>
#         <div class="hero-links">
#             <a class="hlink" href="mailto:rjnath98@gmail.com">📧 Email Me</a>
#             <a class="hlink" href="#">🔗 LinkedIn</a>
#             <a class="hlink" href="#">💻 GitHub</a>
#             <a class="hlink" href="#">🌐 Portfolio</a>
#         </div>
#     </div>
#     <div class="hero-right">
#         <div class="stat-box"><div class="stat-num">2,000+</div><div class="stat-lbl">Students Taught</div></div>
#         <div class="stat-box"><div class="stat-num">700+</div><div class="stat-lbl">Offline Learners</div></div>
#         <div class="stat-box"><div class="stat-num">4+ Yrs</div><div class="stat-lbl">Teaching Exp.</div></div>
#         <div class="stat-box"><div class="stat-num">5+</div><div class="stat-lbl">Subjects Taught</div></div>
#     </div>
# </div>
# """, unsafe_allow_html=True)


# # ══════════════════════════════════════════════
# # ABOUT
# # ══════════════════════════════════════════════
# st.markdown('<div id="about"></div>', unsafe_allow_html=True)
# st.markdown('<div class="sec-hdr">👤 About Me</div>', unsafe_allow_html=True)

# c1, c2 = st.columns([3, 2], gap="large")
# with c1:
#     st.markdown("""
#     <div class="card">
#         <p style="color:#3a4a5a; line-height:1.85; font-size:0.93rem; margin:0;">
#         I'm a <strong>Data Science Instructor, AI/ML Mentor</strong>, and <strong>Data Analyst</strong>
#         based in Guwahati, India. With a B.Tech in Computer Science from Lovely Professional University,
#         I bridge the gap between academic learning and real-world industry practice.
#         <br><br>
#         As a <strong>Subject Matter Expert on CheggExpert</strong>, I've answered 1,000+ queries from students
#         across universities in India, USA, and UK. Previously I personally taught
#         <strong>700+ students offline</strong> in Mathematics and Computer Science fundamentals.
#         <br><br>
#         At <strong>Allsoft Solutions</strong>, I work as a Data Science Trainee — building ML models,
#         writing optimised SQL queries, and creating BI dashboards — experience I bring directly into my teaching.
#         <br><br>
#         My philosophy: <em style="color:#1a3a6b;">"Learn by building real things."</em> Every session is
#         project-driven, practical, and mapped to industry standards.
#         </p>
#     </div>
#     """, unsafe_allow_html=True)

# with c2:
#     st.markdown("""
#     <div class="card" style="margin-bottom:14px;">
#         <div style="font-weight:700; color:#1a3a6b; font-size:0.92rem; margin-bottom:12px;">🎯 What I Offer</div>
#         <ul style="color:#3a5a7a; line-height:2; font-size:0.88rem; padding-left:18px; margin:0;">
#             <li>Industry-standard practical curriculum</li>
#             <li>Live coding with real datasets</li>
#             <li>End-to-end project mentoring</li>
#             <li>1-on-1 doubt resolution</li>
#             <li>Bootcamp &amp; workshop design</li>
#             <li>Corporate training delivery</li>
#         </ul>
#     </div>
#     <div class="card" style="margin-bottom:0;">
#         <div style="font-weight:700; color:#1a3a6b; font-size:0.92rem; margin-bottom:10px;">🏷 Core Domains</div>
#         <span class="pill">Data Science</span><span class="pill">Machine Learning</span>
#         <span class="pill">AI</span><span class="pill">Python</span><span class="pill">SQL</span>
#         <span class="pill">Tableau</span><span class="pill">Excel</span><span class="pill">Statistics</span>
#         <span class="pill">Mathematics</span><span class="pill">NLP</span>
#     </div>
#     """, unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)


# # ══════════════════════════════════════════════
# # SKILLS
# # ══════════════════════════════════════════════
# st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
# st.markdown('<div class="sec-hdr">🛠 Technical Skills</div>', unsafe_allow_html=True)

# skills = [
#     ("🐍", "Languages",       ["Python", "SQL", "R", "HTML", "CSS", "JavaScript"]),
#     ("📊", "Data Analysis",   ["Pandas", "NumPy", "EDA", "Data Wrangling", "Statistical Analysis"]),
#     ("🤖", "ML / AI",         ["Scikit-learn", "XGBoost", "Regression", "Classification", "NLP", "Feature Engineering"]),
#     ("📉", "Visualisation",   ["Tableau", "Power BI", "Matplotlib", "Seaborn", "Excel Dashboards"]),
#     ("🗄", "Databases",       ["MySQL", "MongoDB", "PostgreSQL", "Query Optimisation", "DBMS"]),
#     ("☁️", "Cloud & Tools",   ["AWS S3", "AWS EC2", "Git/GitHub", "Docker", "Streamlit", "Jupyter"]),
#     ("🎓", "Teaching Tools",  ["Google Colab", "Zoom/Meet LMS", "Curriculum Design", "Assessment Design"]),
#     ("🧮", "Mathematics",     ["Linear Algebra", "Probability", "Statistics", "Discrete Maths", "Calculus"]),
# ]

# cols = st.columns(4, gap="small")
# for i, (icon, cat, items) in enumerate(skills):
#     with cols[i % 4]:
#         pills = "".join([f'<span class="pill-mono">{p}</span>' for p in items])
#         st.markdown(f"""
#         <div class="card" style="min-height:170px; margin-bottom:12px;">
#             <div style="font-size:1.5rem; margin-bottom:6px;">{icon}</div>
#             <div style="font-size:0.7rem; text-transform:uppercase; letter-spacing:0.1em;
#                         color:#e8a020; font-weight:700; margin-bottom:8px;">{cat}</div>
#             <div>{pills}</div>
#         </div>""", unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)


# # ══════════════════════════════════════════════
# # EXPERIENCE
# # ══════════════════════════════════════════════
# st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
# st.markdown('<div class="sec-hdr">💼 Work Experience</div>', unsafe_allow_html=True)

# exps = [
#     {
#         "color": "#1a3a6b", "badge": "#e8f0fb", "badge_tc": "#1a3a6b", "type": "Industry",
#         "role": "Data Science Trainee", "org": "Allsoft Solutions Pvt. Ltd.", "period": "March 2024 – Present",
#         "points": [
#             "Gathered & cleaned data from multiple sources ensuring high quality for ML modeling and analysis.",
#             "Built and deployed ML models (regression, classification) improving business KPI forecast accuracy.",
#             "Developed optimised SQL queries for large-scale dataset management and BI reporting.",
#             "Created Tableau & Excel dashboards adopted by management for weekly data-driven reporting.",
#             "Conducted internal Python, SQL, EDA & Tableau training sessions for junior team members.",
#         ]
#     },
#     {
#         "color": "#e8a020", "badge": "#fff3d6", "badge_tc": "#a06800", "type": "Teaching",
#         "role": "Subject Matter Expert — Online Tutor", "org": "CheggExpert (Global Platform)", "period": "2021 – Present",
#         "points": [
#             "Resolved 1,000+ student queries in Python, SQL, Data Science & Maths across universities in India, USA & UK.",
#             "Maintained top accuracy rating by delivering structured, step-by-step explanations for all levels.",
#             "Built expertise translating complex ML and analytics concepts into easy, clear answers.",
#         ]
#     },
#     {
#         "color": "#2e8b57", "badge": "#e2f5ea", "badge_tc": "#1a6b3a", "type": "Teaching",
#         "role": "Instructor — Maths & Computer Science", "org": "Independent / Community Teaching", "period": "May 2018 – Dec 2020",
#         "points": [
#             "Taught 700+ students across multiple offline batches in Mathematics, CS fundamentals & programming basics.",
#             "Designed lesson plans, assessments, and hands-on practicals for varying skill levels.",
#             "Conducted doubt-clearing sessions & mock tests — consistently rated highly by students and parents.",
#         ]
#     },
# ]

# for e in exps:
#     pts = "".join([f"<li style='margin-bottom:6px;color:#3a4a5a;font-size:0.88rem;'>{p}</li>" for p in e["points"]])
#     st.markdown(f"""
#     <div class="exp-card" style="border-left-color:{e['color']};">
#         <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:8px; margin-bottom:10px;">
#             <div>
#                 <span class="exp-title">{e['role']}</span>
#                 <span class="exp-org"> &nbsp;·&nbsp; {e['org']}</span>
#             </div>
#             <div style="display:flex; gap:8px; align-items:center;">
#                 <span style="background:{e['badge']}; color:{e['badge_tc']}; padding:3px 12px;
#                              border-radius:20px; font-size:0.72rem; font-weight:700;">{e['type']}</span>
#                 <span class="exp-meta">📅 {e['period']}</span>
#             </div>
#         </div>
#         <ul style="padding-left:18px; margin:0;">{pts}</ul>
#     </div>""", unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)


# # ══════════════════════════════════════════════
# # PROJECTS
# # ══════════════════════════════════════════════
# st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
# st.markdown('<div class="sec-hdr">🚀 Projects</div>', unsafe_allow_html=True)

# projects = [
#     {
#         "title": "Retail Sales Performance Dashboard",
#         "cat": "Data Analyst Project", "year": "2024", "color": "#1a3a6b",
#         "tech": ["Python", "MySQL", "Tableau", "Pandas", "EDA", "Time-Series"],
#         "desc": "Analyzed 2+ years of retail transaction data (50K+ records) to uncover sales trends, customer segments, and revenue KPIs.",
#         "points": [
#             "Interactive Tableau dashboard tracking revenue growth, avg order value, top SKUs — adopted for weekly management reporting.",
#             "Time-series forecasting achieved 92% accuracy, enabling data-driven inventory and budget planning.",
#             "Automated Python + MySQL data pipeline reducing manual reporting effort by 60%.",
#         ]
#     },
#     {
#         "title": "Data Analytics Bootcamp — End-to-End Program",
#         "cat": "Teaching / Training Project", "year": "2023–24", "color": "#e8a020",
#         "tech": ["Curriculum Design", "Python", "SQL", "Tableau", "Excel", "Streamlit"],
#         "desc": "Designed and conducted a 6-week Data Analytics Bootcamp for 80+ students and working professionals.",
#         "points": [
#             "Structured curriculum with real datasets and capstone project — 95% completion rate, 4.8/5 avg feedback.",
#             "Live Zoom sessions + recorded modules + 1-on-1 mentoring.",
#             "30+ participants secured data-related roles or promotions post-bootcamp.",
#         ]
#     },
#     {
#         "title": "Customer Churn Prediction — ML Pipeline",
#         "cat": "Machine Learning", "year": "2024", "color": "#2e8b57",
#         "tech": ["Python", "Scikit-learn", "XGBoost", "SMOTE", "SQL", "Streamlit"],
#         "desc": "End-to-end ML pipeline predicting telecom customer churn on 100K+ records.",
#         "points": [
#             "87% accuracy, 0.91 AUC-ROC using XGBoost + SMOTE for class imbalance.",
#             "Deployed as interactive Streamlit web app for real-time churn risk scoring.",
#             "Automated retraining pipeline reducing manual intervention by 60%.",
#         ]
#     },
#     {
#         "title": "Pizza Sales Analytics Dashboard",
#         "cat": "Data Visualisation", "year": "2023", "color": "#7b3fa0",
#         "tech": ["EDA", "MySQL", "Tableau", "KPI", "Git"],
#         "desc": "Analyzed 2-year Pizza Sales dataset (50K+ transactions) to uncover sales trends and KPIs.",
#         "points": [
#             "Dynamic Tableau dashboard tracking revenue, avg order value, best-selling SKUs.",
#             "Sales forecasting with 92% accuracy for budget and inventory planning.",
#             "Used as live classroom teaching material for EDA & visualisation storytelling.",
#         ]
#     },
#     {
#         "title": "WhatsApp Chat Sentiment Analyser",
#         "cat": "NLP / Web App", "year": "2023", "color": "#c0392b",
#         "tech": ["Python", "NLP", "Streamlit", "WordCloud", "Git"],
#         "desc": "NLP-powered web app for sentiment analysis, emoji trends, and conversation pattern analysis.",
#         "points": [
#             "WordCloud visualisation and message frequency analysis for conversation insights.",
#             "Deployed on Streamlit Cloud — 200+ active users.",
#             "Used as student capstone demo for end-to-end data product development.",
#         ]
#     },
#     {
#         "title": "Coffee Shop Sales Dashboard",
#         "cat": "Business Intelligence", "year": "2023", "color": "#d4890a",
#         "tech": ["MS Excel", "Pivot Tables", "BeautifulSoup", "KPI"],
#         "desc": "Multi-location sales performance dashboard covering 5 store locations.",
#         "points": [
#             "Scraped market data using BeautifulSoup; integrated with internal sales records.",
#             "Identified peak sales windows and top-performing SKUs for marketing strategy.",
#         ]
#     },
# ]

# c1, c2 = st.columns(2, gap="medium")
# for i, p in enumerate(projects):
#     col = c1 if i % 2 == 0 else c2
#     with col:
#         tech_html = "".join([f'<span class="pill-mono">{t}</span>' for t in p["tech"]])
#         pts_html  = "".join([f"<li style='margin-bottom:5px;color:#3a4a5a;font-size:0.85rem;'>{x}</li>" for x in p["points"]])
#         st.markdown(f"""
#         <div class="proj-card" style="border-top-color:{p['color']};">
#             <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
#                 <span style="font-size:0.7rem; text-transform:uppercase; letter-spacing:0.1em;
#                              color:{p['color']}; font-weight:700;">{p['cat']}</span>
#                 <span style="color:#8a9ab0; font-size:0.76rem;">📅 {p['year']}</span>
#             </div>
#             <div style="font-size:0.98rem; font-weight:700; color:#0d1b2a; margin-bottom:6px;">{p['title']}</div>
#             <p style="color:#5a6a7a; font-size:0.85rem; line-height:1.6; margin-bottom:10px;">{p['desc']}</p>
#             <div style="margin-bottom:10px;">{tech_html}</div>
#             <ul style="padding-left:18px; margin:0;">{pts_html}</ul>
#         </div>""", unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)


# # ══════════════════════════════════════════════
# # INTRODUCTORY TEACHING VIDEOS
# # ══════════════════════════════════════════════
# st.markdown('<div id="videos"></div>', unsafe_allow_html=True)
# st.markdown('<div class="sec-hdr">🎬 Introductory Teaching Videos</div>', unsafe_allow_html=True)

# st.markdown("""
# <div class="card" style="margin-bottom:18px; background:#f8fbff; border: 1px dashed #b0c8e8;">
#     <p style="color:#3a5a7a; font-size:0.9rem; margin:0; line-height:1.7;">
#     🎙 <strong>Watch me teach.</strong> These introductory sessions give you a taste of how I break down
#     complex data science topics into simple, practical lessons. Each video is a standalone micro-lesson
#     designed for beginners and working professionals alike.
#     <br><span style="color:#8a9ab0; font-size:0.82rem;">
#     💡 Replace the YouTube embed links below with your actual video URLs before publishing.</span>
#     </p>
# </div>
# """, unsafe_allow_html=True)

# videos = [
#     {
#         "badge": "Python Basics",
#         "title": "Intro to Python for Data Science",
#         "desc": "Learn variables, data types, loops, and functions in Python with hands-on examples using real datasets. Perfect for absolute beginners.",
#         "duration": "⏱ 18 min", "level": "🟢 Beginner",
#         "url": "https://www.youtube.com/embed/rfscVS0vtbw",
#         "topics": ["Variables & Types", "Loops", "Functions", "Lists & Dicts"],
#     },
#     {
#         "badge": "SQL Fundamentals",
#         "title": "SQL for Data Analysis — Zero to Query",
#         "desc": "Understand SELECT, WHERE, GROUP BY, JOINs and aggregations using a real sales database. Start writing useful queries in under 20 minutes.",
#         "duration": "⏱ 22 min", "level": "🟢 Beginner",
#         "url": "https://www.youtube.com/embed/HXV3zeQKqGY",
#         "topics": ["SELECT & WHERE", "GROUP BY", "JOINs", "Aggregations"],
#     },
#     {
#         "badge": "Machine Learning",
#         "title": "Your First ML Model in Python",
#         "desc": "Build and evaluate a classification model using Scikit-learn step by step — from loading data to measuring accuracy. No maths degree required.",
#         "duration": "⏱ 25 min", "level": "🟡 Intermediate",
#         "url": "https://www.youtube.com/embed/pqNCD_5r0IU",
#         "topics": ["Scikit-learn", "Train/Test Split", "Logistic Regression", "Accuracy Score"],
#     },
#     {
#         "badge": "Data Visualisation",
#         "title": "Tableau Dashboard from Scratch",
#         "desc": "Connect to a dataset, create charts, build KPIs, and publish a professional interactive dashboard in Tableau Public — all in one session.",
#         "duration": "⏱ 20 min", "level": "🟢 Beginner",
#         "url": "https://www.youtube.com/embed/jEgVto5QME8",
#         "topics": ["Connecting Data", "Bar & Line Charts", "KPI Cards", "Filters & Dashboard"],
#     },
#     {
#         "badge": "Pandas & EDA",
#         "title": "Exploratory Data Analysis with Pandas",
#         "desc": "Learn how to load, clean, explore, and summarise a real dataset using Pandas. Covers null handling, groupby, and visualising distributions.",
#         "duration": "⏱ 20 min", "level": "🟢 Beginner",
#         "url": "https://www.youtube.com/embed/vmEHCJofslg",
#         "topics": ["read_csv", "describe()", "Null Handling", "groupby & plot"],
#     },
#     {
#         "badge": "Excel for Analysts",
#         "title": "Excel Pivot Tables & Dashboards",
#         "desc": "Turn raw data into a management-ready dashboard using Pivot Tables, charts, slicers, and conditional formatting — no formulas panic.",
#         "duration": "⏱ 16 min", "level": "🟢 Beginner",
#         "url": "https://www.youtube.com/embed/m13o5aqeCbM",
#         "topics": ["Pivot Tables", "Slicers", "Charts", "Conditional Formatting"],
#     },
# ]

# v_cols = st.columns(3, gap="medium")
# for i, v in enumerate(videos):
#     with v_cols[i % 3]:
#         topic_pills = "".join([f'<span class="pill" style="font-size:0.72rem;">{t}</span>' for t in v["topics"]])
#         st.markdown(f"""
#         <div class="vid-card">
#             <span class="vid-badge">{v['badge']}</span>
#             <div style="position:relative; padding-bottom:56.25%; height:0; overflow:hidden; border-radius:10px; margin-bottom:12px;">
#                 <iframe src="{v['url']}"
#                     style="position:absolute;top:0;left:0;width:100%;height:100%;border:none;border-radius:10px;"
#                     allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
#                     allowfullscreen>
#                 </iframe>
#             </div>
#             <div class="vid-title">{v['title']}</div>
#             <div style="display:flex; gap:8px; margin:6px 0 8px;">
#                 <span style="font-size:0.76rem; color:#5a7a9a;">{v['duration']}</span>
#                 <span style="font-size:0.76rem; color:#5a7a9a;">{v['level']}</span>
#             </div>
#             <div class="vid-desc">{v['desc']}</div>
#             <div style="margin-top:10px;">{topic_pills}</div>
#         </div>""", unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)


# # ══════════════════════════════════════════════
# # TEACHING HIGHLIGHTS
# # ══════════════════════════════════════════════
# st.markdown('<div class="sec-hdr">🏅 Teaching Expertise</div>', unsafe_allow_html=True)

# c1, c2 = st.columns(2, gap="medium")
# with c1:
#     st.markdown("""
#     <div class="card">
#         <div style="font-weight:700; color:#1a3a6b; font-size:0.92rem; margin-bottom:12px;">📚 Subjects Taught</div>
#         <span class="pill">Python Programming</span><span class="pill">SQL &amp; Databases</span>
#         <span class="pill">Machine Learning</span><span class="pill">AI Fundamentals</span>
#         <span class="pill">Data Analysis</span><span class="pill">Tableau</span>
#         <span class="pill">MS Excel</span><span class="pill">Statistics</span>
#         <span class="pill">Mathematics</span><span class="pill">NLP</span>
#     </div>""", unsafe_allow_html=True)
# with c2:
#     st.markdown("""
#     <div class="card">
#         <div style="font-weight:700; color:#1a3a6b; font-size:0.92rem; margin-bottom:12px;">🎙 Delivery Modes</div>
#         <span class="pill pill-gold">Online LMS</span>
#         <span class="pill pill-gold">Live Zoom/Meet</span>
#         <span class="pill pill-gold">Offline Classroom</span>
#         <span class="pill pill-gold">Workshops</span>
#         <span class="pill pill-gold">1-on-1 Mentoring</span>
#         <span class="pill pill-gold">Corporate Training</span>
#         <span class="pill pill-gold">Bootcamps</span>
#     </div>""", unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)


# # ══════════════════════════════════════════════
# # EDUCATION
# # ══════════════════════════════════════════════
# st.markdown('<div id="education"></div>', unsafe_allow_html=True)
# st.markdown('<div class="sec-hdr">🎓 Education</div>', unsafe_allow_html=True)

# st.markdown("""
# <div class="exp-card" style="border-left-color:#1a3a6b;">
#     <div style="display:flex; justify-content:space-between; align-items:flex-start; flex-wrap:wrap; gap:8px; margin-bottom:10px;">
#         <div>
#             <div class="exp-title">B.Tech — Computer Science &amp; Engineering</div>
#             <div class="exp-org">🏛 Lovely Professional University, Phagwara, Punjab</div>
#         </div>
#         <div style="text-align:right;">
#             <span style="background:#e8f0fb; color:#1a3a6b; padding:3px 12px;
#                          border-radius:20px; font-size:0.76rem; font-weight:600;">2020 – 2024</span>
#             <div style="color:#e8a020; font-weight:700; font-size:0.88rem; margin-top:6px;">CGPA: 7.2</div>
#         </div>
#     </div>
#     <div>
#         <span style="font-size:0.8rem; color:#5a6a7a; margin-right:4px;">Relevant Coursework:</span>
#         <span class="pill">Data Structures</span><span class="pill">DBMS</span>
#         <span class="pill">Machine Learning</span><span class="pill">Statistics</span>
#         <span class="pill">Computer Networks</span><span class="pill">Software Engineering</span>
#     </div>
# </div>
# """, unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)


# # ══════════════════════════════════════════════
# # CERTIFICATIONS
# # ══════════════════════════════════════════════
# st.markdown('<div id="certifications"></div>', unsafe_allow_html=True)
# st.markdown('<div class="sec-hdr">📜 Certifications</div>', unsafe_allow_html=True)

# certs = [
#     ("📊", "Data Visualization with Tableau Specialization", "Coursera", "2023", "#1a3a6b"),
#     ("📈", "Creating Charts & Dashboards in MS Excel",       "Coursera", "2023", "#2e8b57"),
#     ("☕", "Summer Training in Java",                        "Hitbullseye", "2022", "#e8a020"),
# ]
# cols = st.columns(3, gap="medium")
# for i, (icon, name, issuer, year, color) in enumerate(certs):
#     with cols[i]:
#         st.markdown(f"""
#         <div class="cert-card" style="border-top-color:{color};">
#             <div style="font-size:2rem; margin-bottom:8px;">{icon}</div>
#             <div style="font-weight:700; color:#0d1b2a; font-size:0.92rem; margin-bottom:6px; line-height:1.4;">{name}</div>
#             <div style="color:#4a6a9a; font-size:0.82rem; margin-bottom:8px;">🏢 {issuer}</div>
#             <span style="background:#f0f4fa; color:#4a5a7a; padding:3px 12px;
#                          border-radius:20px; font-size:0.74rem;">📅 {year}</span>
#         </div>""", unsafe_allow_html=True)

# st.markdown("<br>", unsafe_allow_html=True)


# # ══════════════════════════════════════════════
# # CONTACT
# # ══════════════════════════════════════════════
# st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
# st.markdown('<div class="sec-hdr">📬 Contact Me</div>', unsafe_allow_html=True)

# c1, c2 = st.columns([3, 2], gap="large")
# with c1:
#     st.markdown("""
#     <div class="card" style="margin-bottom:14px;">
#         <p style="color:#3a4a5a; line-height:1.8; font-size:0.92rem; margin:0;">
#         Interested in having me as an <strong>instructor, mentor, or data analyst</strong>?
#         Whether it's a teaching role, freelance analytics project, workshop, or full-time position
#         — drop me a message and I'll get back to you within 24 hours.
#         </p>
#     </div>
#     """, unsafe_allow_html=True)
#     with st.form("contact_form"):
#         n_col, e_col = st.columns(2)
#         with n_col:
#             name  = st.text_input("Your Name", placeholder="John Doe")
#         with e_col:
#             email = st.text_input("Your Email", placeholder="you@email.com")
#         subj = st.selectbox("Purpose", [
#             "Teaching / Instructor Role",
#             "Data Analyst Role",
#             "Workshop / Bootcamp",
#             "1-on-1 Mentoring",
#             "Corporate Training",
#             "Other"
#         ])
#         msg = st.text_area("Message", height=110, placeholder="Tell me about the opportunity or what you need...")
#         submitted = st.form_submit_button("✉️ Send Message", use_container_width=True)
#         if submitted:
#             if name and email and msg:
#                 st.success(f"✅ Thanks {name}! I'll get back to you at **{email}** soon.")
#             else:
#                 st.warning("Please fill in all fields before sending.")

# with c2:
#     st.markdown("""
#     <div class="card">
#         <div style="font-weight:700; color:#1a3a6b; font-size:0.95rem; margin-bottom:16px;">📋 Contact Details</div>
#         <div class="contact-info-row">
#             <span class="contact-icon">📧</span>
#             <a href="mailto:rjnath98@gmail.com" style="color:#1a3a6b; font-weight:500; text-decoration:none;">rjnath98@gmail.com</a>
#         </div>
#         <div class="contact-info-row">
#             <span class="contact-icon">📞</span>
#             <span>+91-7002141483</span>
#         </div>
#         <div class="contact-info-row">
#             <span class="contact-icon">📍</span>
#             <span>Guwahati, Assam, India</span>
#         </div>
#         <div class="contact-info-row" style="border:none;">
#             <span class="contact-icon">🕐</span>
#             <span style="color:#2e8b57; font-weight:600;">Available for new opportunities</span>
#         </div>
#         <div style="margin-top:16px; display:flex; flex-direction:column; gap:8px;">
#             <a href="#" style="display:block; background:#0a66c2; color:white; text-align:center;
#                padding:9px; border-radius:8px; text-decoration:none; font-size:0.85rem; font-weight:600;">
#                🔗 LinkedIn Profile
#             </a>
#             <a href="#" style="display:block; background:#0d1b2a; color:white; text-align:center;
#                padding:9px; border-radius:8px; text-decoration:none; font-size:0.85rem; font-weight:600;">
#                💻 GitHub Profile
#             </a>
#             <a href="#" style="display:block; background:#e8a020; color:#0d1b2a; text-align:center;
#                padding:9px; border-radius:8px; text-decoration:none; font-size:0.85rem; font-weight:600;">
#                🌐 Full Portfolio Site
#             </a>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)


# # ══════════════════════════════════════════════
# # FOOTER
# # ══════════════════════════════════════════════
# st.markdown("""
# <div class="footer">
#     © 2024 Raju Devnath &nbsp;·&nbsp; Data Science Instructor &amp; Analyst &nbsp;·&nbsp; Built with Streamlit<br>
#     <span style="font-size:0.75rem;">📍 Guwahati, India &nbsp;·&nbsp; 📧 rjnath98@gmail.com</span>
# </div>
# """, unsafe_allow_html=True)









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






