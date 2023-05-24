from locust import HttpUser, task, between


class LocustDemo(HttpUser):
    host = "http://127.0.0.1:4000"

    def on_start(self):
        res = self.client.post(
            "/user/login", json={"username": "tang", "password": "123456"}
        )
        print(res.json())

    @task
    def get_mycomment(self):
        self.client.get("/comment/me")
