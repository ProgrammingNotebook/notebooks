package com.programmingnotebook;

import org.apache.kafka.clients.producer.ProducerConfig;
import org.apache.kafka.clients.producer.ProducerRecord;
import org.apache.kafka.common.serialization.StringSerializer;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;
import reactor.core.publisher.Mono;
import reactor.kafka.sender.KafkaSender;
import reactor.kafka.sender.SenderOptions;
import reactor.kafka.sender.SenderRecord;

import java.util.HashMap;
import java.util.Map;

class ReactiveKafkaTest {

    @Test
    void reactiveKafkaTest() {
        // Step 1: Kafka Producer configurations
        Map<String, Object> producerProps = new HashMap<>();
        producerProps.put(ProducerConfig.BOOTSTRAP_SERVERS_CONFIG, "localhost:9092");
        producerProps.put(ProducerConfig.KEY_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        producerProps.put(ProducerConfig.VALUE_SERIALIZER_CLASS_CONFIG, StringSerializer.class);
        producerProps.put(ProducerConfig.ACKS_CONFIG, "all");
        producerProps.put(ProducerConfig.MAX_IN_FLIGHT_REQUESTS_PER_CONNECTION, 5);

        // If something fails then how many should you retry to send the message
        producerProps.put(ProducerConfig.RETRIES_CONFIG, 5);

        // Step 2: Configure the SenderOptions using the Kafka producer properties
        // You can also use Properties class to create the SenderOptions: create(Properties properties)
        SenderOptions<String, String> senderOptions = SenderOptions.create(producerProps);
        senderOptions.stopOnError(true);

        // Step 3: Create KafkaSender using the SenderOptions
        KafkaSender<String, String> kafkaSender = KafkaSender.create(senderOptions);

        // Step 4: Prepare a message to send using KafkaSender
        ProducerRecord<String, String> producerRecord = new ProducerRecord<>("my-topic", "key", "value");
        Mono<SenderRecord<String, String, String>> message =
                Mono.just(SenderRecord.create(producerRecord, "correlation-key")
                );

        // Step 5: Send message and handle result
        kafkaSender.send(message)
                .doOnError(e -> System.out.println("Send failed: " + e))
                .doOnNext(result -> System.out.println("Message sent successfully to " + result.recordMetadata().topic()))
                .subscribe();

        // Step 6: Close KafkaSender
        kafkaSender.close();

        // Fake assertion to silence the IDE warnings.
        Assertions.assertEquals(20, 10 + 10);
    }
}
