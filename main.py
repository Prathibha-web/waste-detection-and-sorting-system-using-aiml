import streamlit as st
import app  # Make sure app.py has a function run_app()

st.set_page_config(
    page_title="🌱 EcoDetect - Smart Waste Detection",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="🌱"
)

# ------------------------------
# 🎨 Custom CSS Styling
# ------------------------------
def apply_custom_css():
    st.markdown("""
        <style>
        /* Hide Streamlit default elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}

        /* Main container styling */
        .main {
            padding: 0rem 0rem;
        }

        /* Top Banner Styling */
        .top-banner {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 1.5rem 2rem;
            margin: -1rem -1rem 0rem -1rem;
            color: white;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .banner-title {
            font-size: 2.5rem;
            font-weight: bold;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        .banner-subtitle {
            font-size: 1.2rem;
            margin: 0.5rem 0 0 0;
            opacity: 0.9;
        }

        /* Navigation Bar Styling */
        .navbar {
            background: linear-gradient(90deg, #4CAF50 0%, #2196F3 25%, #FF9800 50%, #9E9E9E 75%, #f44336 100%);
            padding: 0;
            margin: 0rem -1rem 2rem -1rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        .nav-button {
            background: transparent !important;
            border: none !important;
            color: white !important;
            font-weight: 600 !important;
            padding: 1rem 2rem !important;
            margin: 0 !important;
            border-radius: 0 !important;
            transition: all 0.3s ease !important;
            width: 100% !important;
        }

        .nav-button:hover {
            background: rgba(255,255,255,0.2) !important;
            transform: translateY(-2px);
        }

        /* Content Area Styling */
        .content-area {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 2rem;
            margin: 0rem -1rem;
            min-height: 70vh;
            border-radius: 10px;
            box-shadow: inset 0 2px 4px rgba(0,0,0,0.1);
            backgroundImage:
        }

        /* Smooth scrolling and page positioning */
        html {
            scroll-behavior: smooth;
        }

        .main .block-container {
            padding-top: 1rem;
            max-width: 100%;
        }

        /* Ensure content starts at top */
        .stApp > div:first-child {
            margin-top: 0;
        }

        /* Fix navbar positioning */
        .navbar {
            position: sticky;
            top: 0;
            z-index: 100;
        }

        /* Auto scroll to top on page change */
        .main {
            scroll-behavior: smooth;
        }

        /* Enhanced form visibility and positioning */
        #login-section, #signup-section, #contact-section, #about-section, #home-section {
            scroll-margin-top: 100px;
            padding-top: 20px;
        }

        /* Form highlighting on focus */
        [data-testid="stForm"] {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 2rem;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            margin: 1rem 0;
        }

        /* Input field enhancements */
        input[type="text"], input[type="password"], input[type="email"], textarea {
            transition: all 0.3s ease;
            border-radius: 8px !important;
        }

        input[type="text"]:focus, input[type="password"]:focus, input[type="email"]:focus, textarea:focus {
            box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.2) !important;
            border-color: #4CAF50 !important;
        }

        /* Card Styling */
        .info-card {
            background: white;
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0,0,0,0.1);
            margin: 1rem 0;
            border-left: 5px solid #4CAF50;
        }

        /* Button Styling */
        .stButton > button {
            background: linear-gradient(45deg, #4CAF50, #45a049);
            color: white;
            border: none;
            border-radius: 25px;
            padding: 0.75rem 2rem;
            font-weight: 600;
            transition: all 0.3s ease;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }

        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.3);
        }

        /* Input Styling */
        .stTextInput > div > div > input {
            border-radius: 10px;
            border: 2px solid #e0e0e0;
            padding: 0.75rem;
            transition: border-color 0.3s ease;
        }

        .stTextInput > div > div > input:focus {
            border-color: #4CAF50;
            box-shadow: 0 0 0 2px rgba(76, 175, 80, 0.2);
        }

        /* Status Messages */
        .stSuccess {
            background: linear-gradient(90deg, #4CAF50, #45a049);
            color: white;
            border-radius: 10px;
            padding: 1rem;
        }

        .stError {
            background: linear-gradient(90deg, #f44336, #d32f2f);
            color: white;
            border-radius: 10px;
            padding: 1rem;
        }

        .stWarning {
            background: linear-gradient(90deg, #FF9800, #f57c00);
            color: white;
            border-radius: 10px;
            padding: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

# ------------------------------
# 🏗️ Layout Components
# ------------------------------
def render_top_banner():
    st.markdown("""
        <div class="top-banner">
            <h1 class="banner-title">🌱 EcoDetect</h1>
            <p class="banner-subtitle">Smart Environmental Management Solution</p>
        </div>
    """, unsafe_allow_html=True)

def render_navbar():
    st.markdown('<div class="navbar">', unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("🏠 Home", key="home_nav", help="Go to Home Page"):
            st.session_state.page = "home"

    with col2:
        if st.button("🔐 Login", key="login_nav", help="Login to Access Detection"):
            st.session_state.page = "login"

    with col3:
        if st.button("📝 Sign Up", key="signup_nav", help="Create New Account"):
            st.session_state.page = "signup"

    with col4:
        if st.button("ℹ️ About", key="about_nav", help="Learn About EcoDetect"):
            st.session_state.page = "about"

    with col5:
        if st.button("📞 Contact", key="contact_nav", help="Get Support"):
            st.session_state.page = "contact"

    st.markdown('</div>', unsafe_allow_html=True)

def render_hero_image():
    # Empty hero section - no content displayed
    pass

def render_content_area(content_func):
    # Render content directly below navbar without extra spacing
    st.markdown("""
        <div class="content-area" style="
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 1.5rem;
            margin: 0.5rem 0;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            border: 1px solid rgba(255,255,255,0.8);
            min-height: 400px;">
    """, unsafe_allow_html=True)

    content_func()

    st.markdown("""
        </div>
    """, unsafe_allow_html=True)

# ------------------------------
# 📄 Page Content Functions
# ------------------------------
def home_content():
    # Add unique ID for home section
    st.markdown('<div id="home-section">', unsafe_allow_html=True)

    st.markdown("""
        <div class="info-card">
            <h2 style="color: #4CAF50; margin-top: 0;">🌿 Welcome to EcoDetect</h2>
            <p style="font-size: 1.1rem; line-height: 1.6;">
                Transform the way you handle waste with our cutting-edge AI technology.
                EcoDetect helps you identify, classify, and properly dispose of waste items
                for a cleaner, more sustainable future.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Login Status and Quick Actions
    if "logged_in" in st.session_state and st.session_state.logged_in:
        st.success("✅ Welcome back! You are successfully logged in.")

        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.button("🚀 Start Detection", key="quick_access", help="Go to Waste Detection App"):
                st.session_state.page = "app"

        with col2:
            if st.button("� View Dashboard", key="dashboard", help="View Detection History"):
                st.info("Dashboard feature coming soon!")
        with col3:
            if st.button("�🚪 Logout", key="logout_home", help="Sign Out"):
                st.session_state.logged_in = False
                st.success("Logged out successfully!")
    else:
        st.info("👋 Please login to access the waste detection features.")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔐 Login Now", key="login_prompt"):
                st.session_state.page = "login"
        with col2:
            if st.button("📝 Create Account", key="signup_prompt"):
                st.session_state.page = "signup"

    # Smart Detection Showcase with Image
    st.markdown("""
        <div class="info-card">
            <h3 style="color: #2196F3;">🤖 Smart Detection in Action</h3>
            <p style="font-size: 1.1rem; line-height: 1.6; margin-bottom: 1.5rem;">
                Experience the future of waste management with our advanced computer vision technology.
                Simply upload an image or use your camera, and our system instantly identifies and classifies
                waste items with detailed disposal recommendations.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Create columns for image and text
    st.markdown("""
    <div class="info-card" style="height: 100%; display: flex; flex-direction: column; justify-content: center;">
        <h4 style="color: #4CAF50; margin-top: 0;">🌟 Key Features</h4>
        <ul style="font-size: 1rem; line-height: 1.8;">
            <li><strong>🎯 Instant Recognition:</strong> Identify waste items in seconds</li>
            <li><strong>📊 Smart Classification:</strong> Categorize into 5+ waste types</li>
            <li><strong>💡 Disposal Guidance:</strong> Get specific disposal instructions</li>
            <li><strong>📱 Multi-Input Support:</strong> Upload images or use live camera</li>
            <li><strong>🌍 Environmental Impact:</strong> Track your eco-friendly actions</li>
        </ul>
        <div style="background: linear-gradient(90deg, #4CAF50, #45a049);
                   color: white; padding: 1rem; border-radius: 10px;
                   text-align: center; margin-top: 1rem;">
            <strong>🚀 Ready to make a difference?</strong><br>
            <span style="font-size: 0.9rem;">Join thousands of users creating a cleaner future!</span>
        </div>
    </div>
""", unsafe_allow_html=True)

    # Features Overview
    st.markdown("""
        <div class="info-card">
            <h3 style="color: #2196F3;">🎯 What We Detect</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
                <div style="text-align: center; padding: 1rem; background: #e8f5e8; border-radius: 10px;">
                    <div style="font-size: 2rem;">♻️</div>
                    <strong>Recyclable</strong>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Plastic bottles, cans, paper</p>
                </div>
                <div style="text-align: center; padding: 1rem; background: #fff3e0; border-radius: 10px;">
                    <div style="font-size: 2rem;">🚫</div>
                    <strong>Non-Recyclable</strong>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Styrofoam, diapers</p>
                </div>
                <div style="text-align: center; padding: 1rem; background: #ffebee; border-radius: 10px;">
                    <div style="font-size: 2rem;">☣️</div>
                    <strong>Hazardous</strong>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Batteries, chemicals</p>
                </div>
                <div style="text-align: center; padding: 1rem; background: #f3e5f5; border-radius: 10px;">
                    <div style="font-size: 2rem;">🍃</div>
                    <strong>Organic</strong>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Food scraps, peels</p>
                </div>
                <div style="text-align: center; padding: 1rem; background: #e0f2f1; border-radius: 10px;">
                    <div style="font-size: 2rem;">🌱</div>
                    <strong>Biodegradable</strong>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">Paper, cotton, organic waste</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Close home section
    st.markdown('</div>', unsafe_allow_html=True)

def login_content():
    # Check if already logged in
    if "logged_in" in st.session_state and st.session_state.logged_in:
        st.success("✅ You are already logged in!")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🚀 Go to Detection App", key="goto_app"):
                st.session_state.page = "app"
        with col2:
            if st.button("🚪 Logout", key="logout_login"):
                st.session_state.logged_in = False
                st.success("Logged out successfully!")
        return

    # Simple login header
    st.title("🔐 Login")

    # Login Form - appears directly below navbar
    with st.form("login_form"):
        username = st.text_input("👤 Username", placeholder="Enter your username")
        password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")

        submitted = st.form_submit_button("🚀 Login", use_container_width=True)

        if submitted:
            if username == "admin" and password == "123":
                st.session_state.logged_in = True
                st.success("Login successful! Redirecting to detection app...")
                st.session_state.page = "app"
            else:
                st.error("❌ Invalid username or password")

    # Demo credentials
    st.info("💡 **Demo:** Username: `admin` | Password: `123`")

def signup_page():
    st.title("📝 Sign Up")

    with st.form("signup_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("👤 Full Name", placeholder="Enter full name")
            username = st.text_input("🆔 Username", placeholder="Choose username")
            password = st.text_input("� Password", type="password", placeholder="Create password")
        with col2:
            email = st.text_input("� Email", placeholder="Enter email")
            confirm_password = st.text_input("🔒 Confirm Password", type="password", placeholder="Confirm password")

        submitted = st.form_submit_button("🚀 Create Account", use_container_width=True)

        if submitted:
            if not all([name, email, username, password, confirm_password]):
                st.warning("⚠️ Please fill in all fields.")
            elif password != confirm_password:
                st.warning("⚠️ Passwords do not match.")
            else:
                st.success("✅ Account created successfully! Please login.")
                st.session_state.page = "login"



def about_page():
    st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                   color: white; padding: 2rem; border-radius: 15px; margin-bottom: 2rem;">
            <h1 style="margin: 0; text-align: center;">ℹ️ About EcoDetect</h1>
            <p style="text-align: center; font-size: 1.2rem; margin: 0.5rem 0 0 0;">
                Smart Environmental Management Solution
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Mission Section
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.95); padding: 2rem; border-radius: 15px;
                   box-shadow: 0 8px 25px rgba(0,0,0,0.1); margin-bottom: 2rem;">
            <h2 style="color: #4CAF50; margin-top: 0;">🌍 Our Mission</h2>
            <p style="font-size: 1.1rem; line-height: 1.6; color: #333;">
                We aim to make waste management smarter and more efficient using cutting-edge
                smart classification technology. Our goal is to create a sustainable
                future by making proper waste disposal accessible to everyone through
                innovative AI-powered solutions.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Waste Categories Section
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.95); padding: 2rem; border-radius: 15px;
                   box-shadow: 0 8px 25px rgba(0,0,0,0.1); margin-bottom: 2rem;">
            <h2 style="color: #2196F3; margin-top: 0;">🚮 Waste Categories We Detect</h2>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    categories = [
        ("♻️", "Recyclable", "Plastic bottles, cans, paper, glass", "#e8f5e8"),
        ("🚫", "Non-Recyclable", "Styrofoam, diapers, mixed materials", "#ffebee"),
        ("☣️", "Hazardous", "Batteries, chemicals, electronics", "#fff3e0"),
        ("🍃", "Organic", "Food scraps, fruit peels, vegetables", "#f3e5f5"),
        ("🌱", "Biodegradable", "Paper, cotton, organic materials", "#e0f2f1")
    ]

    for i, (emoji, title, desc, color) in enumerate(categories):
        with [col1, col2, col3, col4, col5][i]:
            st.markdown(f"""
                <div style="background: {color}; padding: 1.5rem; border-radius: 10px;
                           text-align: center; height: 150px; display: flex;
                           flex-direction: column; justify-content: center;">
                    <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">{emoji}</div>
                    <strong style="color: #333; font-size: 1.1rem;">{title}</strong>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem; color: #666;">{desc}</p>
                </div>
            """, unsafe_allow_html=True)

    # Team Section
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.95); padding: 2rem; border-radius: 15px;
                   box-shadow: 0 8px 25px rgba(0,0,0,0.1); margin-bottom: 2rem;">
            <h2 style="color: #FF9800; margin-top: 0;">👩‍💻 Our Team</h2>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    team_members = [
        ("🎯", "Project Lead", "Anisha Verma"),
        ("🤖", "AI Engineer", "Rahul Mehta"),
        ("💻", "Frontend Developer", "Priya Sharma"),
        ("📊", "Data Scientist", "Vikram Singh")
    ]

    for i, (emoji, role, name) in enumerate(team_members):
        with [col1, col2, col3, col4][i]:
            st.markdown(f"""
                <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 10px;
                           text-align: center; border: 2px solid #e9ecef;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">{emoji}</div>
                    <strong style="color: #333; display: block; margin-bottom: 0.5rem;">{role}</strong>
                    <span style="color: #666;">{name}</span>
                </div>
            """, unsafe_allow_html=True)

    # Technology Section
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.95); padding: 2rem; border-radius: 15px;
                   box-shadow: 0 8px 25px rgba(0,0,0,0.1);">
            <h2 style="color: #9C27B0; margin-top: 0;">🔬 Technology Stack</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                       gap: 1rem; margin-top: 1rem;">
                <div style="background: #e3f2fd; padding: 1rem; border-radius: 8px; text-align: center;">
                    <strong>🧠 AI/ML</strong><br>
                    <span style="color: #666;">Deep Learning, Computer Vision</span>
                </div>
                <div style="background: #f3e5f5; padding: 1rem; border-radius: 8px; text-align: center;">
                    <strong>🐍 Python</strong><br>
                    <span style="color: #666;">Backend Processing</span>
                </div>
                <div style="background: #e8f5e8; padding: 1rem; border-radius: 8px; text-align: center;">
                    <strong>🌐 Streamlit</strong><br>
                    <span style="color: #666;">Web Interface</span>
                </div>
                <div style="background: #fff3e0; padding: 1rem; border-radius: 8px; text-align: center;">
                    <strong>📱 Responsive</strong><br>
                    <span style="color: #666;">Mobile Friendly</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

def contact_page():
    # Header Section
    st.markdown("""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                   color: white; padding: 2rem; border-radius: 15px; margin-bottom: 2rem;">
            <h1 style="margin: 0; text-align: center;">📞 Contact EcoDetect</h1>
            <p style="text-align: center; font-size: 1.2rem; margin: 0.5rem 0 0 0;">
                We're here to help! Reach out to us for any support, questions, or feedback.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Contact Information Section
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.95); padding: 2rem; border-radius: 15px;
                   box-shadow: 0 8px 25px rgba(0,0,0,0.1); margin-bottom: 2rem;">
            <h2 style="color: #4CAF50; margin-top: 0;">🌐 Get in Touch</h2>
        </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div style="background: #e3f2fd; padding: 1.5rem; border-radius: 10px;
                       border-left: 4px solid #2196F3;">
                <h3 style="color: #2196F3; margin-top: 0;">📧 Email Support</h3>
                <p style="margin: 0.5rem 0;"><strong>General Inquiries:</strong><br>
                <a href="mailto:support@ecodetect.com" style="color: #4CAF50; text-decoration: none;">
                support@ecodetect.com</a></p>
                <p style="margin: 0.5rem 0;"><strong>Technical Support:</strong><br>
                <a href="mailto:tech@ecodetect.com" style="color: #4CAF50; text-decoration: none;">
                tech@ecodetect.com</a></p>
                <p style="margin: 0.5rem 0;"><strong>Business Partnerships:</strong><br>
                <a href="mailto:business@ecodetect.com" style="color: #4CAF50; text-decoration: none;">
                business@ecodetect.com</a></p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="background: #f3e5f5; padding: 1.5rem; border-radius: 10px;
                       border-left: 4px solid #9C27B0;">
                <h3 style="color: #9C27B0; margin-top: 0;">📞 Phone Support</h3>
                <p style="margin: 0.5rem 0;"><strong>Customer Service:</strong><br>
                +1 (555) 123-4567</p>
                <p style="margin: 0.5rem 0;"><strong>Technical Support:</strong><br>
                +1 (555) 123-4568</p>
                <p style="margin: 0.5rem 0;"><strong>Business Hours:</strong><br>
                Monday - Friday: 9:00 AM - 6:00 PM EST</p>
            </div>
        """, unsafe_allow_html=True)

    # Office Location Section
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.95); padding: 2rem; border-radius: 15px;
                   box-shadow: 0 8px 25px rgba(0,0,0,0.1); margin-bottom: 2rem;">
            <h2 style="color: #FF9800; margin-top: 0;">🏢 Office Location</h2>
            <div style="background: #fff3e0; padding: 1.5rem; border-radius: 10px;
                       border-left: 4px solid #FF9800;">
                <p style="font-size: 1.1rem; margin: 0; line-height: 1.6;">
                    <strong>EcoDetect Headquarters</strong><br>
                    123 GreenTech Avenue<br>
                    Sustainability District<br>
                    Eco City, EC 12345<br>
                    Earth 🌍
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Contact Form Section
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.95); padding: 2rem; border-radius: 15px;
                   box-shadow: 0 8px 25px rgba(0,0,0,0.1); margin-bottom: 2rem;">
            <h2 style="color: #9C27B0; margin-top: 0;">💬 Quick Contact Form</h2>
            <p style="color: #666;">Send us a message and we'll get back to you within 24 hours!</p>
        </div>
    """, unsafe_allow_html=True)

    # Enhanced Contact Form
    with st.form("contact_form"):
        st.markdown("""
            <style>
            .stTextInput > div > div > input {
                background-color: #f8f9fa;
                border: 2px solid #e9ecef;
                border-radius: 8px;
                padding: 0.5rem;
            }
            .stTextInput > div > div > input:focus {
                border-color: #4CAF50;
                box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.1);
            }
            .stTextArea > div > div > textarea {
                background-color: #f8f9fa;
                border: 2px solid #e9ecef;
                border-radius: 8px;
            }
            .stTextArea > div > div > textarea:focus {
                border-color: #4CAF50;
                box-shadow: 0 0 0 3px rgba(76, 175, 80, 0.1);
            }
            </style>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("👤 Your Name", placeholder="Enter your full name")
            email = st.text_input("📧 Your Email", placeholder="Enter your email address")
        with col2:
            subject = st.text_input("📋 Subject", placeholder="What's this about?")
            priority = st.selectbox("⚡ Priority", ["Low", "Medium", "High", "Urgent"])

        message = st.text_area("💬 Message", placeholder="Tell us how we can help you...", height=120)

        # Custom styled submit button
        submitted = st.form_submit_button("📤 Send Message", use_container_width=True)

        if submitted:
            if name and email and subject and message:
                st.markdown("""
                    <div style="background: #d4edda; color: #155724; padding: 1rem;
                               border-radius: 8px; border: 1px solid #c3e6cb; margin-top: 1rem;">
                        <strong>✅ Success!</strong> Thank you for your message!
                        We'll get back to you within 24 hours.
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                    <div style="background: #fff3cd; color: #856404; padding: 1rem;
                               border-radius: 8px; border: 1px solid #ffeaa7; margin-top: 1rem;">
                        <strong>⚠️ Missing Information!</strong> Please fill in all required fields.
                    </div>
                """, unsafe_allow_html=True)

    # Additional Contact Options
    st.markdown("""
        <div style="background: rgba(255, 255, 255, 0.95); padding: 2rem; border-radius: 15px;
                   box-shadow: 0 8px 25px rgba(0,0,0,0.1); margin-top: 2rem;">
            <h2 style="color: #607D8B; margin-top: 0;">🚀 Other Ways to Connect</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                       gap: 1rem; margin-top: 1rem;">
                <div style="background: #e8f5e8; padding: 1rem; border-radius: 8px; text-align: center;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">💬</div>
                    <strong>Live Chat</strong><br>
                    <span style="color: #666;">Available 24/7</span>
                </div>
                <div style="background: #e3f2fd; padding: 1rem; border-radius: 8px; text-align: center;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">📱</div>
                    <strong>WhatsApp</strong><br>
                    <span style="color: #666;">+1 (555) 123-4569</span>
                </div>
                <div style="background: #f3e5f5; padding: 1rem; border-radius: 8px; text-align: center;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">🐦</div>
                    <strong>Twitter</strong><br>
                    <span style="color: #666;">@EcoDetectAI</span>
                </div>
                <div style="background: #fff3e0; padding: 1rem; border-radius: 8px; text-align: center;">
                    <div style="font-size: 2rem; margin-bottom: 0.5rem;">💼</div>
                    <strong>LinkedIn</strong><br>
                    <span style="color: #666;">EcoDetect Solutions</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ------------------------------
# 🔁 Session State & Routing
# ------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# Apply custom CSS
apply_custom_css()

# Check if we need to scroll to a specific section
if "scroll_to" in st.session_state and st.session_state.scroll_to:
    scroll_target = st.session_state.scroll_to
    st.session_state.scroll_to = None  # Clear the scroll target

    # Add JavaScript to scroll to the specific section
    st.markdown(f"""
        <script>
        // Function to scroll to target section
        function scrollToTarget() {{
            let targetElement;
            const target = '{scroll_target}';

            // Find the target element based on the page
            switch(target) {{
                case 'login':
                    targetElement = document.querySelector('#login-section') ||
                                  document.querySelector('input[placeholder*="username"]') ||
                                  document.querySelector('[data-testid="stForm"]') ||
                                  document.querySelector('.info-card');
                    break;
                case 'signup':
                    targetElement = document.querySelector('#signup-section') ||
                                  document.querySelector('input[placeholder*="full name"]') ||
                                  document.querySelector('[data-testid="stForm"]') ||
                                  document.querySelector('.info-card');
                    break;
                case 'contact':
                    targetElement = document.querySelector('#contact-section') ||
                                  document.querySelector('input[placeholder*="Your Name"]') ||
                                  document.querySelector('[data-testid="stForm"]') ||
                                  document.querySelector('.info-card');
                    break;
                case 'about':
                    targetElement = document.querySelector('#about-section') ||
                                  document.querySelector('.info-card');
                    break;
                case 'home':
                    targetElement = document.querySelector('#home-section') ||
                                  document.querySelector('.info-card');
                    break;
            }}

            if (targetElement) {{
                // Scroll with offset for better visibility
                const elementPosition = targetElement.getBoundingClientRect().top + window.pageYOffset;
                const offsetPosition = elementPosition - 80;

                window.scrollTo({{
                    top: offsetPosition,
                    behavior: 'smooth'
                }});

                // Highlight the target area briefly
                targetElement.style.transition = 'all 0.3s ease';
                targetElement.style.backgroundColor = 'rgba(76, 175, 80, 0.1)';
                setTimeout(() => {{
                    targetElement.style.backgroundColor = '';
                }}, 1000);
            }}
        }}

        // Try scrolling multiple times to ensure it works
        setTimeout(scrollToTarget, 100);
        setTimeout(scrollToTarget, 300);
        setTimeout(scrollToTarget, 500);
        setTimeout(scrollToTarget, 800);

        // Also scroll when DOM is fully loaded
        if (document.readyState === 'loading') {{
            document.addEventListener('DOMContentLoaded', scrollToTarget);
        }} else {{
            scrollToTarget();
        }}
        </script>
    """, unsafe_allow_html=True)

# Render layout based on current page
if st.session_state.page == "app":
    # Special layout for detection app
    app.run_app()
else:
    # Standard layout for other pages
    render_top_banner()
    render_navbar()

    # Content appears directly below navbar - no hero image or extra spacing
    if st.session_state.page == "home":
        # Show hero image only on home page
        render_hero_image()
        render_content_area(home_content)
    elif st.session_state.page == "login":
        # Login form appears directly below navbar
        login_content()
    elif st.session_state.page == "signup":
        # Signup form appears directly below navbar
        signup_page()
    elif st.session_state.page == "about":
        # About content appears directly below navbar
        about_page()
    elif st.session_state.page == "contact":
        # Contact form appears directly below navbar
        contact_page()
    else:
        st.error("Page not found.")
