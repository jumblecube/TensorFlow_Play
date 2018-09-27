# Test kafka is running

from kafka import KafkaConsumer, TopicPartition

print('Making connection...')
consumer = KafkaConsumer(bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
consumer.subscribe(['kafkatp1'])

print('Getting message...')

for message in consumer:
    print(message)

print('Done...')
