package com.akaal.api.service;

import com.akaal.api.model.dto.UserPrompt;
import reactor.core.publisher.Flux;

public interface ChatService {

    Flux<String> process(UserPrompt userPrompt);
}
