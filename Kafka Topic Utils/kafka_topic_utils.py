from kafka.admin import KafkaAdminClient, NewTopic
from kafka import KafkaProducer, KafkaConsumer

# Function to create a Kafka topic
def create_topic(topic_name):
    try:
        admin_client = KafkaAdminClient(bootstrap_servers=["localhost:9092"])
        topic_list = []
        topic_list.append(NewTopic(name=topic_name, num_partitions=1, replication_factor=1))
        admin_client.create_topics(new_topics=topic_list, validate_only=False)
        print("Topic created successfully!")
    except Exception as ex:
        print(str(ex))

# Function to produce data into a Kafka topic
def produce_data(topic_name, message):
    try:
        producer = KafkaProducer(bootstrap_servers=["localhost:9092"])
        producer.send(topic_name, message.encode('utf-8'))
        producer.flush()
        print("Message sent successfully!")
    except Exception as ex:
        print(str(ex))

# Function to consume data from a Kafka topic
def consume_data(topic_name):
    try:
        consumer = KafkaConsumer(topic_name, bootstrap_servers=["localhost:9092"], auto_offset_reset='earliest', enable_auto_commit=True, group_id='my-group', value_deserializer=lambda x: x.decode('utf-8'))
        for message in consumer:
            print(message.value)
    except Exception as ex:
        print(str(ex))

# Example usage
topic_name = "my_topic"
create_topic(topic_name)
produce_data(topic_name, "This is a sample message.")
consume_data(topic_name)
