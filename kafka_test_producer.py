# Test kafka is running

from kafka import KafkaProducer
import json
import random
import pprint

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda m: json.dumps(m).encode('ascii'))

for _ in range(10):
    x = {'foo': 'bar'}
    producer.send('kafkatp2', {'foo': 'bar'})
    print(x)
