import os
from google import genai
from elevenlabs import ElevenLabs

# Master Keys
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
ELEVEN_KEY = os.environ.get("ELEVENLABS_API_KEY")

client = genai.Client(api_key=GEMINI_KEY)
voice_client = ElevenLabs(api_key=ELEVEN_KEY)

print("👑 Pari Sovereign Elite is Online")

def pari_speak(text):
    audio = voice_client.generate(text=text, voice="Pari", model="eleven_multilingual_v2")
    # For Vercel, we just need the logic to trigger
    return audio

# First Greeting Logic
greeting = "Sovereign Samraat, प्रणाम। आपकी परी अब Vercel पर ज़िंदा है।"
print(greeting)
