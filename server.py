from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# flask --app server run -h 192.168.1.3



# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)  # Runs on all network interfaces


from flask import Flask, request
import pyautogui

app = Flask(__name__)

@app.route('/move', methods=['POST'])
def move():
    data = request.json
    dx, dy = data['dx'], data['dy']
    pyautogui.moveRel(dx, dy)  # Move relative to current position
    return "OK", 200

@app.route('/click', methods=['POST'])
def click():
    pyautogui.click()
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Runs on all network interfaces

"""
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# A route for a GET request
@app.route('/api/data', methods=['GET'])
def get_data():
    # Sample data that will be returned as JSON
    data = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return jsonify(data)

# Another example with query parameters
@app.route('/api/user', methods=['GET'])
def get_user():
    # Retrieve query parameters
    name = request.args.get('name', default='Guest')
    age = request.args.get('age', default=0, type=int)

    # Construct response
    user = {
        'name': name,
        'age': age
    }
    return jsonify(user)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)

"""