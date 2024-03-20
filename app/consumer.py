from kafka import KafkaConsumer
from typing import Iterator
import json
from datetime import datetime

from consts import WINDOW_SIZE



class Consumer:
    def __init__(
        self, 
        servers: list[str],
        topic: str = 'data',
        group_id: str = 'your_consumer_group',
    ):
        self.__topic = topic
        self.__consumer = KafkaConsumer(
            'data',
            group_id=group_id,
            bootstrap_servers=servers,
            value_deserializer=lambda v: json.loads(v.decode('utf-8'))
        )

    def consume(self) -> Iterator[dict]:
        for message in self.__consumer:
            print(f"GOT message on topic {self.__topic} with message: {message}")
            trade_data = message.value
            
            # Check if the message is within the 10 minute window
            current_time = datetime.now().timestamp()
            message_time = trade_data.get('InvoiceDate')
            if not message_time:    
                print(f"Invalid data {message_time} in trade_data")
                continue
            if current_time - message_time <= WINDOW_SIZE:
                yield trade_data

