# Python Kafka utils code
This code includes three functions to create, produce, and consume data in a Kafka topic.

To use this code, you need to install two libraries: kafka-python and confluent-kafka.

You can install these libraries using pip. Open a command prompt or terminal and run the following commands:

`pip install kafka-python`
`pip install confluent-kafka`

Now, let's look at the code in detail:

1. The `KafkaAdminClient` class is imported from `kafka.admin` library. It is used to create a Kafka topic with the given name using the `create_topic` function.
2. The `KafkaProducer` and `KafkaConsumer` classes are imported from `kafka` library. They are used to produce and consume data from a Kafka topic, respectively.
3. The `create_topic` function takes `topic_name` as input and creates a Kafka topic with the given name using `KafkaAdminClient`. It first creates a `topic_list` object, which contains a `NewTopic` object with the given `topic_name`, number of partitions, and replication factor. Then, it creates the topic using `admin_client.create_topics()` method.
4. The produce_data function takes `topic_name` and message as input and produces the message into the Kafka topic using `KafkaProducer`. It first creates a producer object and sends the message using `producer.send()` method.
5. The `consume_data` function takes `topic_name` as input and consumes messages from the Kafka topic using KafkaConsumer. It creates a consumer object and uses a for loop to print the messages using message.value attribute.
6. Finally, the code demonstrates the usage of these functions by creating a topic with name `my_topic`, producing a sample message into the topic, and consuming the messages from the same topic.
