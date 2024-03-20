from kafka import KafkaProducer
import json


class Producer:
    def __init__(
        self,
        servers: list[str],
        topic: str = "agg",
    ):
        self.__topic = topic
        self.__producer = KafkaProducer(
            bootstrap_servers=servers,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )

    def send(self, data: dict):
        self.send_to(data=data, topic=self.__topic)

    def send_to(self, data: dict, topic: str | None):
        to_send = topic or self.__topic
        print(f"Send to topic {to_send} with data {data}")
        self.__producer.send(to_send, data)
