from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(host='host.docker.internal',port=6379,db=0)

def is_redis_available(r):
    try:
        r.ping()
        print("Successfully connected to redis")
    except (redis.exceptions.ConnectionError, ConnectionRefusedError):
        print("Redis connection error!")
        return False
    return True


@app.route('/')
def home():
    return "Flask App is Running!"

import time
if __name__ == '__main__':
    if is_redis_available(r):
        print("Yay!")
    time.sleep(5)
    app.run(host='0.0.0.0', port=5000, debug=True)

"""

watchmedo auto-restart --directory=$(awk -F' = ' '/path/ {print $2}' watchdog.conf) --pattern=$(awk -F' = ' '/file_extensions/ {print $2}' watchdog.conf) --recursive -- python app.py

watchmedo auto-restart --pattern="*.py" --recursive -- python app.py

docker build -t flask-watchdog-app .


docker run -p 5000:5000 flask-watchdog-app

"""