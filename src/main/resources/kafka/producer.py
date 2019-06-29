from __future__ import absolute_import
from kafka import KafkaProducer, KafkaConsumer

KAFKA_TOPIC = 'dummy-topic'
KAFKA_BROKERS = '127.0.0.1:9092' # see step 1

producer = KafkaProducer(bootstrap_servers=KAFKA_BROKERS)

# Must send bytes
messages = [b'hello kafka', b'I am sending', b'3 test messages']

# Send the messages
for m in messages:
    producer.send(KAFKA_TOPIC, m)

consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_BROKERS,
                             auto_offset_reset='earliest')

try:
    for message in consumer:
        print(message.value)
except KeyboardInterrupt:
    sys.exit()