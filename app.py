import streamlit as st
import google.generativeai as genai

# Master ID: 325270269318 | Sovereign Empire Hub
def main():
    st.set_page_config(page_title="Sovereign Hub Pro", layout="wide")

    # API Configuration (Using your verified Key)
    api_key = "AIzaSyDNfAmIqQzrnJHwfXljx4nGYZkldOO7s0k"
    genai.configure(api_key=api_key)

    st.markdown("<style>.stApp { background-color: #050505; color: white; }</style>", unsafe_allow_html=True)

    with st.sidebar:
        st.title("🤴🏻 Samraat OS")
        st.write("ID: 325270269318")
        mode = st.radio("Surgical Center:", ["💰 Money-Making AI", "🎬 Live Media Search", "⚖️ Fraud Audit"])
        st.success("API: ACTIVE ⚡")

    if mode == "💰 Money-Making AI":
        run_ai_money()
    elif mode == "🎬 Live Media Search":
        run_live_media()
    else:
        run_audit_pro()

def run_ai_money():
    st.title("💰 AI Seek-Use: Affiliate Goldmine")
    needs = st.text_input("What do you want to build/do?")
    if st.button("Find Profit-Making Tools 🔍"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"List top 3 paid AI tools for {needs} that have affiliate programs. Be professional.")
        st.markdown(f"<div style='border:1px solid #00ffcc; padding:20px;'>{response.text}</div>", unsafe_allow_html=True)
        st.info("💡 Pro-Tip: Add your affiliate links to these results to start earning!")

def run_live_media():
    st.title("🎬 Media-Quest: Real-Time Intelligence")
    q = st.text_input("Enter Movie/Show Name:")
    if st.button("Deep Scrape 🔍"):
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(f"Official info for {q}: Release, Rating, Category, Streaming on. Source: 325270269318")
        st.write(response.text)

def run_audit_pro():
    st.title("⚖️ Sovereign Fraud Audit")
    u = st.number_input("Units:", value=2300.0)
    l = st.number_input("Load (KW):", value=1.0)
    d = st.number_input("Days:", value=88)
    if st.button("Start Surgical Audit"):
        max_p = l * 24 * d
        if u > max_p: 
            st.error(f"🚨 FRAUD DETECTED! Ghost Units: {u-max_p:.0f}")
            st.button("Buy Legal Draft Report (₹99)") # Money making idea
        else: st.success("✅ Billing Logic Secure.")

if __name__ == "__main__":
    main()
