package com.mycompany.myproducer;

import org.apache.kafka.clients.producer.KafkaProducer;
import org.apache.kafka.clients.producer.Producer;
import org.apache.kafka.clients.producer.ProducerRecord;

import java.util.Properties;

public class MyProducer {
    public static void main(String[] args) {
        // Set up Kafka producer configuration
        Properties props = new Properties();
        props.put("bootstrap.servers", "localhost:9092");
        props.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        props.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");

        // Create a Kafka producer with the provided configuration
        Producer<String, String> producer = new KafkaProducer<>(props);

        // Send a "Hello, World!" message to the "hello-world" topic
        producer.send(new ProducerRecord<>("hello-world", "key", "Hello, World!"));

        // Close the producer
        producer.close();
    }
}
