from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask App is Running!"

import time
if __name__ == '__main__':
    time.sleep(5)
    app.run(host='0.0.0.0', port=5000, debug=True)

"""

watchmedo auto-restart --directory=$(awk -F' = ' '/path/ {print $2}' watchdog.conf) --pattern=$(awk -F' = ' '/file_extensions/ {print $2}' watchdog.conf) --recursive -- python app.py

watchmedo auto-restart --pattern="*.py" --recursive -- python app.py

docker build -t flask-watchdog-app .

docker run -p 5000:5000 flask-watchdog-app

"""