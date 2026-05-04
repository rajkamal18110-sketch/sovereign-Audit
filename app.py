import os
import streamlit as st
from google import genai
from elevenlabs import ElevenLabs

# Sovereign Configuration
st.set_page_config(page_title="Pari Sovereign Elite", layout="wide")
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
ELEVEN_KEY = os.environ.get("ELEVENLABS_API_KEY")
MASTER_EMAIL = os.environ.get("MASTER_EMAIL")

client = genai.Client(api_key=GEMINI_KEY)
voice_client = ElevenLabs(api_key=ELEVEN_KEY)

st.title("👑 Pari Sovereign Elite")
st.write(f"Welcome, Sovereign Samraat ({MASTER_EMAIL})")

if st.button("📞 Connect Call"):
    greeting = "Sovereign Samraat, प्रणाम। मैं पूरी तरह से आपकी सेवा में हाज़िर हूँ। बताइए आज क्या आदेश है?"
    audio = voice_client.generate(text=greeting, voice="Pari", model="eleven_multilingual_v2")
    st.audio(audio, autoplay=True)
    st.success(greeting)

user_input = st.text_input("Speak your command...")
if user_input:
    response = client.models.generate_content(model="gemini-1.5-flash", contents=user_input)
    st.write(f"**Pari:** {response.text}")
