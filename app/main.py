from consumer import Consumer
from aggregator import Aggregator

def manage() -> None:
    kafka_server = 'localhost:9092'
    topic_to_consume = 'data'
    topic_to_send = 'agg'
    consumer = Consumer(topic=topic_to_consume, servers=kafka_server)
    aggregator = Aggregator()

    print(f"Starting management of topic {topic_to_consume}")
    for data in consumer.consume():
        if not data:
            continue
        aggregated_data: dict = aggregator.add_data(data)
        print(f'Added aggregated data {aggregated_data}')
        if not aggregated_data:
            continue

def main():
    manage()

if __name__ == '__main__':
    main()