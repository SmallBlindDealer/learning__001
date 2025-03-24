from flask import Flask, request, jsonify
from celery import Celery
import time

app = Flask(__name__)

# Configure Celery
app.config['CELERY_BROKER_URL'] = 'redis://redis:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://redis:6379/0'
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task(bind=True)
def long_task(self, duration):
    for i in range(duration):
        time.sleep(1)
        self.update_state(state='PROGRESS', meta={'progress': (i + 1) * 100 / duration})
    return {'status': 'Task completed!', 'result': 42}

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    duration = data.get('duration', 10)
    task = long_task.apply_async(args=[duration])
    return jsonify({'task_id': task.id}), 202

@app.route('/task_status/<task_id>', methods=['GET'])
def task_status(task_id):
    task = long_task.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {'state': task.state, 'progress': 0}
    elif task.state == 'PROGRESS':
        response = {'state': task.state, 'progress': task.info.get('progress', 0)}
    elif task.state == 'SUCCESS':
        response = {'state': task.state, 'result': task.info.get('result', 0)}
    else:
        response = {'state': task.state, 'error': str(task.info)}
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
