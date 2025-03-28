from flask import Flask, request, send_from_directory
from flask_cors import CORS
import pyautogui

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/')
def serve_html():
    return send_from_directory('.', 'index.html')  # Serve the HTML file

@app.route('/move', methods=['POST'])
def move_mouse():
    data = request.json
    dx, dy = data['dx'], data['dy']
    pyautogui.moveRel(dx, dy)  # Move mouse relative to the previous position
    return "OK", 200

@app.route('/click', methods=['POST'])
def mouse_click():
    pyautogui.click()
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
