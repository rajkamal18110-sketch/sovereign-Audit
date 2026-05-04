from flask import Flask, request, jsonify
import os
from google import genai
from elevenlabs import ElevenLabs

app = Flask(__name__)

# Sovereign Keys
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
ELEVEN_KEY = os.environ.get("ELEVENLABS_API_KEY")

client = genai.Client(api_key=GEMINI_KEY)
voice_client = ElevenLabs(api_key=ELEVEN_KEY)

@app.route('/')
def home():
    return "👑 Pari Sovereign Elite is Online & Ready, Samraat!"

@app.route('/speak', methods=['POST'])
def speak():
    data = request.json
    text = data.get("text", "Sovereign Samraat, प्रणाम।")
    # Voice Logic
    audio = voice_client.generate(text=text, voice="Pari", model="eleven_multilingual_v2")
    return "Audio Generated Successfully"

# Vercel needs this
def handler(event, context):
    return app(event, context)
