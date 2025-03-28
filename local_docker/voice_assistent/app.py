import os
import threading
import pyttsx3
from flask import Flask, request, jsonify
from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Initialize AI agent
agent = Agent(model=Groq(id="llama-3.3-70b-versatile"))

# Initialize text-to-speech engine
tts = pyttsx3.init(driverName="nsss")  # Use macOS voice engine


def save_audio(response_text, file_path):
    """Runs TTS in a separate thread to avoid Flask conflicts."""
    def tts_thread():
        tts.save_to_file(response_text, file_path)
        tts.runAndWait()

    thread = threading.Thread(target=tts_thread)
    thread.start()
    thread.join()  # Ensure it completes before returning


@app.route("/process_voice", methods=["POST"])
def process_voice():
    data = request.json
    user_input = data.get("text")

    if not user_input:
        return jsonify({"error": "No input received"}), 400

    # AI Processing
    ai_response = agent.run(user_input).content

    # Ensure `static/` directory exists
    os.makedirs("static", exist_ok=True)
    print("--", ai_response)

    # Define full file path
    audio_file_path = os.path.join("static", "asd.wave")

    # Generate and save speech
    save_audio(ai_response, audio_file_path)

    # Check if the file exists before returning response
    if not os.path.exists(audio_file_path):
        return jsonify({"error": "Failed to generate audio file"}), 500

    return jsonify({"response": ai_response, "audio_url": "/static/output.mp3"})


if __name__ == "__main__":
    app.run(debug=True)
