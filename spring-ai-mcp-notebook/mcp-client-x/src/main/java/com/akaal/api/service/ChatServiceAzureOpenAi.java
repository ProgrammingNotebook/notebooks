package com.akaal.api.service;

import com.akaal.api.model.dto.UserPrompt;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.PromptTemplate;
import org.springframework.stereotype.Service;
import reactor.core.publisher.Flux;

import java.util.Map;

@Slf4j
@Service
@RequiredArgsConstructor
public class ChatServiceAzureOpenAi implements ChatService {

    private final ChatClient chatClient;

    @Override
    public Flux<String> process(UserPrompt userPrompt) {

        log.info("User prompt: {}", userPrompt);

        var SYSTEM_PROMPT = """
                    You are a helpful assistant.
                    Your task is to perform the task based on the user's prompt while making use of the available tools.
                    Message: {message}
                """;

        PromptTemplate promptTemplate = PromptTemplate.builder()
                .template(SYSTEM_PROMPT)
                .build();

        Prompt prompt = promptTemplate.create(Map.of("message", userPrompt.getMessage()));

        return chatClient
                .prompt(prompt)
                .stream()
                .content();
    }
}
