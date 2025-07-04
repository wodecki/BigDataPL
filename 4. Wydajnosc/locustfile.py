from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def load_test(self):
        self.client.get("/predict/BLACK%20VELVET")
