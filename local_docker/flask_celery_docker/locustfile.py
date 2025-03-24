from locust import HttpUser, task, between

class LoadTestUser(HttpUser):
    wait_time = between(1, 2)  # Random wait between requests

    @task
    def add_task(self):
        self.client.post("/add_task", json={"duration": 5})

# locust -f locustfile.py --host=http://localhost:5000 --users 60000 --spawn-rate 1000 --run-time 1m --headless
