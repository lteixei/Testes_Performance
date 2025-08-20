from locust import HttpUser, task, between

class MyWebsiteUser(HttpUser):
    wait_time = between(1, 3)  # espera entre 1 e 3 segundos entre as tarefas

    @task
    def load_homepage(self):
        self.client.get("/")  # Testa a página inicial
