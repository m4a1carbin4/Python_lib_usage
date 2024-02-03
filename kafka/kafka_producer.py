#Apache Kafka producer producer lib (kafka-python)

from kafka import KafkaProducer

broker = ["localhost:9092","localhost:9093","localhost:9094"]

topic = "kafka_topic"

kafka_Producer = KafkaProducer(bootstrap_servers = broker,value_serializer = lambda x : x.encode("utf-8"), acks=0, api_version=(2,5,0),retries=3)

try :
    future = kafka_Producer.send(topic,"hello kafka world")

    kafka_Producer.flush()
    kafka_Producer.close()

    future.get(timeout=2)
    print({"status_code":200, "error":None})
except Exception as exc:
    raise exc
