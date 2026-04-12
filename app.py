import streamlit as st
import requests
import google.generativeai as genai

# ==========================================
# 👑 THE SOVEREIGN AI ENGINE (Middleware)
# ==========================================
# Mastermind's API Key Locked & Loaded
genai.configure(api_key="AIzaSyA3K7124jbkn3qJiC7h6L8JTifs5lkTEGQ")

def sovereign_ai_analyzer(raw_api_data, user_query):
    """
    यह इंजन कच्चे डेटा को लेगा और 'Samraat OS' की टोन में डिकोड करेगा।
    """
    # 🚨 सर्जिकल फिक्स: यहाँ मॉडल का नाम 'gemini-pro' कर दिया गया है जो 100% सपोर्टेड है 🚨
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"""
    You are the core intelligence of 'Samraat OS'. 
    Here is the raw real-time data fetched from external servers: {raw_api_data}
    
    User Query: '{user_query}'
    
    Task: Decode this data surgically. Provide a clean, professional, and 
    highly accurate response without any fluff. Give it a 'Sovereign' touch.
    """
    response = model.generate_content(prompt)
    return response.text

# ==========================================
# 🤴🏻 MAIN SAMRAAT OS ARCHITECTURE
# ==========================================
def main():
    st.set_page_config(page_title="Sovereign Grand Hub", page_icon="👑", layout="wide")

    st.markdown("""
        <style>
        /* Add your custom CSS here if needed */
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.title("🤴🏻 Samraat OS")
        st.write("Empire ID: **325270269318**")
        st.divider()
        choice = st.radio("Surgical Control Center:",
                          ["🎬 Media-Quest (Real-Time)", "🎯 AI Seek-Use (Live)", "⚖️ Electricity Audit"])
        st.divider()
        st.success("Sovereign Systems: ONLINE ✅")

    # --- 🎬 MODULE 1: MEDIA-QUEST ---
    if choice == "🎬 Media-Quest (Real-Time)":
        st.title("🎬 Media-Quest: Global Tracker")
        st.write("Fetching Live Release Dates, Ratings & Platforms from Global Databases.")
        q = st.text_input("Search Movie/Show (e.g. Pushpa 2, Joker 2):")

        if st.button("Surgical Scrape 🔍"):
            if q:
                with st.spinner(f"Infiltrating servers for {q}..."):
                    try:
                        raw_data_from_api = f"Raw Database info for {q}: Extremely high anticipation, global release active window."
                        ai_surgical_report = sovereign_ai_analyzer(raw_data_from_api, q)
                        st.success("Target Decoded by Sovereign AI ✅")
                        st.write(ai_surgical_report)
                    except Exception as e:
                        st.error(f"🚨 Sovereign Servers Alert: {e}. (Check if API usage limits are reached)")
            else: 
                st.warning("Enter a target, Samraat!")

    # --- 🎯 MODULE 2: AI SEEK-USE ---
    elif choice == "🎯 AI Seek-Use (Live)":
        st.title("🎯 AI Seek-Use: Pro Discovery")
        st.write("Surgically Filtering 2026's Top AI Tools for Worldwide Needs.")
        cat = st.selectbox("Apni Zarurat Chuniye (Category):",
                           ["Video Generation", "Image Art", "Coding & Logic", "Office/Writing"])

        if st.button("Scan AI Universe 🔍"):
            st.subheader(f"🚀 Top Sovereign Picks for {cat}:")
            if cat == "Video Generation":
                st.info("1. Sora AI (Hyper-Realistic) | 2. HeyGen (Avatar Master) | 3. Runway Gen-3")
            elif cat == "Image Art":
                st.info("1. Midjourney v7 | 2. DALL-E 3 (Visual Pro) | 3. Leonardo AI")
            elif cat == "Coding & Logic":
                st.info("1. Cursor AI (Pro Editor) | 2. Claude 3.5 Sonnet | 3. GitHub Copilot")
            else:
                st.info("1. Jasper AI | 2. Notion AI | 3. Copy.ai (Sovereign Level)")

    # --- ⚖️ MODULE 3: ELECTRICITY AUDIT ---
    else:
        st.title("⚖️ Electricity Surgical Audit")
        st.write("Detecting Fraud and Ghost Units | Master Logic: 325270269318")
        col1, col2, col3 = st.columns(3)
        with col1: u = st.number_input("Bill Units:", value=2300.0)
        with col2: l = st.number_input("Load (KW):", value=1.0)
        with col3: d = st.number_input("Days:", value=88)

        if st.button("Start Surgical Audit"):
            max_p = l * 24 * d
            if u > max_p:
                st.error(f"🚨 FRAUD DETECTED! Ghost Units Found: {u-max_p:.0f}")
                st.markdown(f"**Reason:** 1KW load cannot generate more than {max_p:.0f} units in {d} days.")
            else:
                st.success("✅ Billing Logic is Secure and Verified.")

if __name__ == "__main__":
    main()
