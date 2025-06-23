package com.programmingnotebook.service;

import lombok.RequiredArgsConstructor;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
@RequiredArgsConstructor
public class CodebaseLoaderService implements CommandLineRunner {

    private final CodebaseService codebaseService;

    @Override
    public void run(String... args) throws Exception {
        codebaseService.loadCodebaseInVectorDatabase();
    }
}
