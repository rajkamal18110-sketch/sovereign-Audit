from flask import Flask, request, send_file, render_template_string
import os
import io
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
    # ई सुंदर UI लोड करी
    return open('index.html').read()

@app.route('/speak', methods=['POST'])
def speak():
    data = request.json
    text = data.get("text", "Sovereign Samraat, प्रणाम।")
    
    # 1. AI Response (Gemini)
    response = client.models.generate_content(model="gemini-2.0-flash", contents=text)
    ai_text = response.text

    # 2. Voice Generation (ElevenLabs)
    audio = voice_client.generate(
        text=ai_text, 
        voice="Pari", # पक्का करा कि ElevenLabs में 'Pari' नाम का वॉइस बा
        model="eleven_multilingual_v2"
    )
    
    # Audio को सीधे ब्राउज़र पर भेजल जाई
    audio_stream = io.BytesIO()
    for chunk in audio:
        audio_stream.write(chunk)
    audio_stream.seek(0)
    
    return send_file(audio_stream, mimetype="audio/mpeg")
