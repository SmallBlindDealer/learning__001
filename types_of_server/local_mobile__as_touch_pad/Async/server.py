# from flask import Flask, send_from_directory
# from flask_socketio import SocketIO
# import pyautogui

# app = Flask(__name__)
# socketio = SocketIO(app, cors_allowed_origins="*")  # Enable WebSockets with CORS support

# @app.route('/')
# def serve_html():
#     return send_from_directory('.', 'index.html')  # Serve the HTML file

# @socketio.on('move')
# def handle_move(data):
#     """ Handle real-time mouse movement """
#     dx, dy = data['dx'], data['dy']
#     pyautogui.moveRel(dx * 2, dy * 2)  # Adjust speed by multiplying

# @socketio.on('click')
# def handle_click():
#     """ Handle mouse click event """
#     pyautogui.click()

# if __name__ == '__main__':
#     print("--:")
#     socketio.run(app, host='0.0.0.0', port=5000)
#     print("---")


from flask import Flask, send_from_directory
from flask_socketio import SocketIO
import pyautogui

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")  # Enable WebSockets with low latency

@app.route('/')
def serve_html():
    return send_from_directory('.', 'index.html')  # Serve the HTML file

@socketio.on('move')
def handle_move(data):
    """ Handle real-time mouse movement """
    dx, dy = data['dx'], data['dy']

    if abs(dx) > 3 or abs(dy) > 3:  # Ignore tiny movements (noise reduction)
        pyautogui.moveRel(dx * 4, dy * 4, _pause=False)  # Increase speed

@socketio.on('click')
def handle_click():
    """ Handle mouse click event """
    pyautogui.click()

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
