import streamlit as st
import google.generativeai as genai

# Master Identity: 325270269318 | The Neural Sovereign Engine
def main():
    st.set_page_config(page_title="Sovereign Neural Hub", page_icon="🧠", layout="wide")

    # API Configuration
    genai.configure(api_key="AIzaSyC_wJubQznptXowVLJOOCubka-zqUdQln8")
    model = genai.GenerativeModel('gemini-1.5-flash')

    # Cyber-Premium UI Styling
    st.markdown("""
        <style>
        .stApp { background-color: #020202; color: #e0e0e0; }
        .result-card { 
            background: rgba(0, 255, 204, 0.05); padding: 25px; border-radius: 15px; 
            border: 1px solid #00ffcc; box-shadow: 0 0 20px rgba(0, 255, 204, 0.2);
            margin-bottom: 20px; line-height: 1.6;
        }
        h1, h2, h3 { color: #00ffcc !important; text-shadow: 0 0 10px #00ffcc55; }
        .stButton>button {
            background: linear-gradient(45deg, #00ffcc, #0088ff);
            color: black; font-weight: bold; border-radius: 20px; border: none;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sidebar Navigation
    with st.sidebar:
        st.title("🤴🏻 Samraat OS")
        st.write("Master ID: 325270269318")
        st.divider()
        choice = st.radio("Surgical Command:", 
                         ["🎬 Media-Quest (Live AI)", "🎯 AI Seek-Use (Global)", "⚖️ Electricity Audit"])
        st.divider()
        st.success("Neural Link: ACTIVE ⚡")

    if choice == "🎬 Media-Quest (Live AI)":
        run_media_ai(model)
    elif choice == "🎯 AI Seek-Use (Global)":
        run_ai_finder(model)
    else:
        run_audit()

def run_media_ai(model):
    st.title("🎬 Media-Quest: Neural Search")
    q = st.text_input("Search Movie/Show (e.g. Pushpa 2, Squid Game S2):")
    
    if st.button("Surgical Scrape 🔍"):
        if q:
            with st.spinner(f"Gemini is infiltrating global databases for {q}..."):
                # Professional Prompting for Real Data
                prompt = f"""Act as a professional movie critic and database agent. 
                Provide details for '{q}' in this format:
                - Release Date: (Be specific)
                - IMDb Rating: (Estimate if not out)
                - Platforms: (Where to watch)
                - Category: (Genre)
                - Surgical Summary: (2 lines)
                Use professional tone."""
                
                try:
                    response = model.generate_content(prompt)
                    st.markdown(f"""
                    <div class="result-card">
                        <h2>🎬 REPORT: {q.upper()}</h2>
                        <div style="color:#ffffff;">{response.text.replace('-', '<br>✅')}</div>
                        <p style="color:#00ffcc; font-size:12px; margin-top:15px;">Verified by Sovereign Neural Logic | 325270269318</p>
                    </div>
                    """, unsafe_allow_html=True)
                except Exception as e:
                    st.error("Neural Link Error. API limits or key issue.")
        else: st.warning("Target enter karein!")

def run_ai_finder(model):
    st.title("🎯 AI Seek-Use: Pro Finder")
    needs = st.text_input("What do you want to achieve with AI? (e.g. Make viral reels, write code)")
    
    if st.button("Find Top Tools 🔍"):
        if needs:
            with st.spinner("Analyzing AI Market..."):
                prompt = f"List top 5 AI tools for '{needs}' with their main features and prices. Be professional."
                response = model.generate_content(prompt)
                st.markdown(f"<div class='result-card'>{response.text.replace('**', '')}</div>", unsafe_allow_html=True)
        else: st.warning("Need enter karein!")

def run_audit():
    st.title("⚖️ Electricity Surgical Audit")
    u = st.number_input("Units:", value=2300.0)
    l = st.number_input("Load (KW):", value=1.0)
    d = st.number_input("Days:", value=88)
    if st.button("Start Audit"):
        max_p = l * 24 * d
        if u > max_p: st.error(f"🚨 FRAUD! Ghost Units: {u-max_p:.0f}")
        else: st.success("✅ Billing Logic Secure.")

if __name__ == "__main__":
    main()
