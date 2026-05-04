from flask import Flask, request, send_file
import os
import io
from google import genai
from gtts import gTTS

app = Flask(__name__)

# Sovereign Keys
GEMINI_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_KEY)

@app.route('/')
def home():
    return open('index.html').read()

@app.route('/speak', methods=['POST'])
def speak():
    try:
        data = request.json
        text = data.get("text", "Samraat, प्रणाम।")
        
        # 1. AI Response (Gemini)
        response = client.models.generate_content(model="gemini-2.0-flash", contents=text)
        ai_text = response.text

        # 2. Google Voice (No Keys, No Block, Pure Free)
        tts = gTTS(text=ai_text, lang='hi')
        audio_stream = io.BytesIO()
        tts.write_to_fp(audio_stream)
        audio_stream.seek(0)
        
        return send_file(audio_stream, mimetype="audio/mpeg")
    except Exception as e:
        return {"error": str(e)}, 500
