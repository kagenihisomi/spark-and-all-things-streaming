from locust_plugins.users.kafka import KafkaUser
from locust import task, run_single_user
import os


class MyUser(KafkaUser):
    bootstrap_servers = 'localhost:9092'
    @task
    def t(self):
        self.client.send("hello-world", b"payload")
        # if you dont poll immediately after sending message your timings will be incorrect
        # (but if throughput is most important then you may want to delay it)
        self.client.producer.poll(1)

if __name__ == "__main__":
    run_single_user(MyUser)