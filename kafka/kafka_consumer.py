#Apache Kafka producer consumer [lib (kafka-python)]

from kafka import KafkaConsumer

broker = ["localhost:9092","localhost:9093","localhost:9094"]

topic = "kafka_topic"

kafka_consumer = KafkaConsumer(topic,bootstrap_servers = broker,value_deserializer = lambda x : x.decode("utf-8"), group_id="test_group", auto_offset_reset="earliest",enable_auto_commit=True)

try:
    for message in kafka_consumer:
        print(message.value)
except Exception as exc:
    raise exc
