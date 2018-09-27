# Test kafka is running

from kafka import KafkaConsumer
import json

print('Making connection...')
consumer = KafkaConsumer('kafkatp2', bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest')

KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))

print('Getting message...')

i = 0

for message in consumer:
    print(str(message))
    print(i)
    i += 1

print('Done...')
