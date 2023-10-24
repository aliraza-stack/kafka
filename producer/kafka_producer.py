from confluent_kafka import Producer, Consumer
import json
# Producer configuration
producer_config = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'my_producer'
}
producer = Producer(producer_config)

# Consumer configuration
consumer_config = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my_consumer',
    'auto.offset.reset': 'earliest'
}
consumer = Consumer(consumer_config)
ducer = Producer(producer_config)

def send_message(topic, message):
    producer.produce(topic, json.dumps(message).encode('utf-8'))
    producer.flush()
