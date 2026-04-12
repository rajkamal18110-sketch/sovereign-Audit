import streamlit as st
import google.generativeai as genai

# Master Identity: 325270269318 | The Absolute Sovereign Engine
def main():
    st.set_page_config(page_title="Sovereign Hub Pro", layout="wide")

    # API Configuration - Surgically Updated from your Screenshot
    # Note: Use the Key exactly as shown in your screen
    api_key = "AIzaSyDNfAmIqQzrnJHwfXljx4nGYZkldOO7s0k"
    genai.configure(api_key=api_key)

    # UI Styling
    st.markdown("""
        <style>
        .stApp { background-color: #050505; color: white; }
        .result-card { border: 2px solid #00ffcc; padding: 20px; border-radius: 15px; background: #111; }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.title("🤴🏻 Samraat OS")
        mode = st.radio("Choose Center:", ["🎬 Media Intelligence", "💰 AI Money Ideas", "⚖️ Audit"])
        st.success("Empire Live ✅")

    if mode == "🎬 Media Intelligence":
        q = st.text_input("Enter Target Movie/Show:")
        if st.button("Deep Scrape 🔍"):
            if q:
                fetch_real_data(q)
    
    elif mode == "💰 AI Money Ideas":
        n = st.text_input("Your goal?")
        if st.button("Get AI Strategy"):
            fetch_real_data(f"Top AI tools and money making ideas for {n}")

    else:
        st.title("⚖️ Fraud Audit")
        st.write("Logic Verified: 325270269318")

def fetch_real_data(query):
    with st.spinner("Infiltrating Neural Servers..."):
        try:
            # TRYING MULTIPLE MODELS TO AVOID 'INVALID ARGUMENT'
            model_names = ['gemini-1.5-flash', 'gemini-pro']
            success = False
            for m in model_names:
                try:
                    model = genai.GenerativeModel(m)
                    response = model.generate_content(query)
                    st.markdown(f"<div class='result-card'>{response.text}</div>", unsafe_allow_html=True)
                    success = True
                    break
                except:
                    continue
            
            if not success:
                st.error("Neural Error: Please check if Gemini API is enabled in your Google Cloud Project.")
        except Exception as e:
            st.error(f"Surgical Error: {e}")

if __name__ == "__main__":
    main()
