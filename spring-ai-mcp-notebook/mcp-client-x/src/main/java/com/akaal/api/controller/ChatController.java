package com.akaal.api.controller;

import com.akaal.api.model.dto.UserPrompt;
import com.akaal.api.service.ChatService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import reactor.core.publisher.Flux;

@Slf4j
@RestController
@RequiredArgsConstructor
public class ChatController {

    private final ChatService chatService;

    @PostMapping("/chat")
    public Flux<String> chat(@RequestBody UserPrompt userPrompt) {
        return chatService.process(userPrompt);
    }
}
