package com.programmingnotebook.controller;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.chat.client.advisor.MessageChatMemoryAdvisor;
import org.springframework.ai.chat.client.advisor.api.Advisor;
import org.springframework.ai.chat.client.advisor.vectorstore.QuestionAnswerAdvisor;
import org.springframework.ai.chat.memory.ChatMemory;
import org.springframework.ai.chat.memory.MessageWindowChatMemory;
import org.springframework.ai.chat.prompt.Prompt;
import org.springframework.ai.chat.prompt.PromptTemplate;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

import java.util.List;
import java.util.Map;

import static com.programmingnotebook.util.PromptUtil.COPILOT_PROMPT;

@Slf4j
@RestController
@RequiredArgsConstructor
public class CoPilotController {

    private final ChatClient chatClient;
    private final VectorStore vectorStore;

    @GetMapping("ai/chat/{id}")
    public Flux<String> chat(@RequestParam(value = "message", defaultValue = "Hi") String message,
                             @PathVariable(value = "id") String conversationId) {

        log.info("Generating code from co-pilot for users: {}", message);

        PromptTemplate promptTemplate = PromptTemplate.builder()
                .template(COPILOT_PROMPT)
                .build();

        Prompt prompt = promptTemplate.create(Map.of("message", message));

        ChatMemory chatMemory = MessageWindowChatMemory.builder().build();
        MessageChatMemoryAdvisor chatMemoryAdvisor = MessageChatMemoryAdvisor.builder(chatMemory)
                .conversationId(conversationId)
                .build();

        QuestionAnswerAdvisor questionAnswerAdvisor = new QuestionAnswerAdvisor(vectorStore);
        List<Advisor> advisors = List.of(chatMemoryAdvisor, questionAnswerAdvisor);

        return chatClient
                .prompt(prompt)
                .advisors(advisors)
                .stream()
                .content();
    }
}
