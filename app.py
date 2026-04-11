import streamlit as st

# Master Identity: 325270269318 | AI Seek-Use Global Portal
def main():
    st.set_page_config(page_title="Sovereign AI Seek-Use", page_icon="🎯", layout="wide")

    # Cool UI Styling (Fixing the previous error)
    st.markdown("""
        <style>
        .stApp { background-color: #0e1117; }
        .ai-card { 
            padding: 20px; 
            border-radius: 15px; 
            border: 2px solid #ff4b4b; 
            background-color: #1a1c24; 
            margin-bottom: 20px;
            box-shadow: 5px 5px 15px rgba(0,0,0,0.3);
        }
        h1, h3 { color: #ff4b4b !important; }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar Navigation
    with st.sidebar:
        st.title("🤴🏻 Samraat Menu")
        choice = st.radio("Option Chuniye:", ["AI Seek-Use (Global Search)", "Electricity Surgical Audit"])
        st.divider()
        st.write("**Master ID:** 325270269318")

    if choice == "AI Seek-Use (Global Search)":
        run_ai_hub()
    else:
        run_electricity_audit()

def run_ai_hub():
    st.title("🎯 AI Seek-Use: Global Discovery Engine")
    st.markdown("### 🌍 Worldwide Users Support | ID: 325270269318")
    st.write("Sahi AI chunne mein confusion? Sovereign Logic se 10 best tools payein. (Confused about AI? Get 10 best tools with Sovereign Logic.)")
    st.divider()

    # Database for 5 Categories (10 Tools Each)
    categories = {
        "YouTube/Video Creator": [
            ["InVideo AI", "⭐⭐⭐⭐⭐", "Free/Paid", "Generate videos from text"],
            ["CapCut", "⭐⭐⭐⭐", "Free", "Best mobile & PC editor"],
            ["ElevenLabs", "⭐⭐⭐⭐⭐", "Freemium", "Human-like AI voices"],
            ["HeyGen", "⭐⭐⭐⭐⭐", "Paid", "AI Avatars and lip-sync"],
            ["Adobe Podcast", "⭐⭐⭐⭐", "Free", "Clean voice from home"],
            ["Pictory", "⭐⭐⭐⭐", "Freemium", "Convert scripts to reels"],
            ["Veed.io", "⭐⭐⭐⭐", "Free/Paid", "Online subtitle/editing"],
            ["Descript", "⭐⭐⭐⭐⭐", "Paid", "Edit video by editing text"],
            ["Canva Magic", "⭐⭐⭐⭐", "Free", "Quick AI social media design"],
            ["Runway Gen-2", "⭐⭐⭐⭐⭐", "Freemium", "AI Text-to-Video magic"]
        ],
        "Academic/Children Study": [
            ["Perplexity AI", "⭐⭐⭐⭐⭐", "Free", "Direct answers with citations"],
            ["Khanmigo", "⭐⭐⭐⭐⭐", "Paid", "Personalized AI tutor"],
            ["Socratic", "⭐⭐⭐⭐", "Free", "Google's homework solver"],
            ["Grammarly", "⭐⭐⭐⭐⭐", "Free", "Writing and grammar help"],
            ["ChatPDF", "⭐⭐⭐⭐", "Freemium", "Chat and learn from books"],
            ["Quizlet", "⭐⭐⭐⭐", "Free", "AI flashcards for exams"],
            ["Wolfram Alpha", "⭐⭐⭐⭐⭐", "Free", "Advanced Math/Science solver"],
            ["Tome", "⭐⭐⭐⭐", "Freemium", "AI presentations for projects"],
            ["Duolingo", "⭐⭐⭐⭐⭐", "Free", "Language learning fun"],
            ["Consensus", "⭐⭐⭐⭐", "Free", "Research search engine"]
        ],
        "Coding/Professional Tech": [
            ["Cursor AI", "⭐⭐⭐⭐⭐", "Freemium", "AI-powered code editor"],
            ["Claude 3.5 Sonnet", "⭐⭐⭐⭐⭐", "Freemium", "Best coding and logic AI"],
            ["GitHub Copilot", "⭐⭐⭐⭐⭐", "Paid", "Complete code instantly"],
            ["Phind", "⭐⭐⭐⭐", "Free", "Search engine for coders"],
            ["Replit AI", "⭐⭐⭐⭐", "Paid", "Cloud-based coding platform"],
            ["Blackbox AI", "⭐⭐⭐⭐⭐", "Free", "Fastest code lookup"],
            ["Amazon CodeWhisperer", "⭐⭐⭐⭐", "Free", "AWS coding expert"],
            ["Vercel V0", "⭐⭐⭐⭐⭐", "Freemium", "UI design with AI"],
            ["Codiga", "⭐⭐⭐⭐", "Paid", "Code security and quality"],
            ["Tabnine", "⭐⭐⭐⭐", "Paid", "Private code assistant"]
        ],
        "Image/Art Magic": [
            ["Midjourney", "⭐⭐⭐⭐⭐", "Paid", "Highest quality AI art"],
            ["DALL-E 3", "⭐⭐⭐⭐⭐", "Paid/Free", "Understand complex prompts"],
            ["Leonardo.ai", "⭐⭐⭐⭐⭐", "Freemium", "Gaming & detailed art"],
            ["Adobe Firefly", "⭐⭐⭐⭐", "Freemium", "Professional photo editing"],
            ["Playground AI", "⭐⭐⭐⭐", "Free", "Unlimited creative images"],
            ["Stable Diffusion", "⭐⭐⭐⭐⭐", "Free", "Open-source power"],
            ["Krea.ai", "⭐⭐⭐⭐", "Free", "Real-time image enhancement"],
            ["Pixlr AI", "⭐⭐⭐⭐", "Free", "Online quick art tool"],
            ["Deep Dream", "⭐⭐⭐", "Free", "Artistic style transfer"],
            ["BlueWillow", "⭐⭐⭐⭐", "Free", "Midjourney alternative"]
        ],
        "Office/Business": [
            ["Jasper AI", "⭐⭐⭐⭐⭐", "Paid", "Marketing copy expert"],
            ["Copy.ai", "⭐⭐⭐⭐", "Freemium", "Quick email & ad writing"],
            ["Notion AI", "⭐⭐⭐⭐⭐", "Paid", "Docs and notes organizer"],
            ["Otter.ai", "⭐⭐⭐⭐", "Free", "Meeting notes recorder"],
            ["Beautiful.ai", "⭐⭐⭐⭐", "Paid", "Stunning business slides"],
            ["Fireflies.ai", "⭐⭐⭐⭐", "Freemium", "AI meeting assistant"],
            ["Zavvy", "⭐⭐⭐⭐", "Paid", "Employee training AI"],
            ["ClickUp Brain", "⭐⭐⭐⭐⭐", "Paid", "Project management AI"],
            ["Monica", "⭐⭐⭐⭐", "Freemium", "Browser AI assistant"],
            ["Loom AI", "⭐⭐⭐⭐", "Paid", "Summarize video messages"]
        ]
    }

    # Selection Logic
    cat_select = st.selectbox("Category Chuniye:", list(categories.keys()))
    
    if st.button("Surgical Analysis (Search 🔍)"):
        st.subheader(f"🚀 Top 10 Sovereign Recommendations for {cat_select}")
        for tool in categories[cat_select]:
            st.markdown(f"""
            <div class="ai-card">
                <h4 style="color:#ff4b4b;">🔗 {tool[0]}</h4>
                <p><b>Sovereign Rating:</b> {tool[1]} | <b>Price:</b> {tool[2]}</p>
                <p><b>Why use it:</b> {tool[3]}</p>
            </div>
            """, unsafe_allow_html=True)
        
        st.divider()
        st.markdown("### 👑 Sovereign Logic - Deep Analysis")
        st.info("Humare algorithms AI ki reliability aur usability check karte hain. (Our algorithms check for AI reliability and ease of use.)")

def run_electricity_audit():
    st.title("⚖️ Electricity Surgical Audit")
    st.write("Sovereign Logic to detect Ghost Units. (Master ID: 325270269318)")
    st.divider()
    u = st.number_input("Units as per bill:", value=2300.0)
    l = st.number_input("Connected Load (KW):", value=1.0)
    d = st.number_input("Days:", value=88)
    if st.button("Start Audit"):
        max_p = l * 24 * d
        if u > max_p:
            st.error(f"🚨 FRAUD DETECTED! Ghost Units Found: {u-max_p:.0f}")
        else:
            st.success("✅ Consumption is Logical.")

    st.caption("© 2026 Sovereign Audit | Created by Raj Kamal")

if __name__ == "__main__":
    main()
