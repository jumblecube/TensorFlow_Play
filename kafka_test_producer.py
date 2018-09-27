# Test kafka is running

from kafka import KafkaProducer
import json
import pprint

producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
    # , value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

for _ in range(100):
    producer.send('kafkatp1', b'34748389')

metrics = producer.metrics()
pprint.pprint(metrics)
