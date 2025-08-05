package com.akaal.api.configuration;

import com.akaal.api.service.FileSystemService;
import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.ai.tool.method.MethodToolCallbackProvider;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ToolConfiguration {

    @Bean
    public ToolCallbackProvider tools(FileSystemService fileSystemService) {

        return MethodToolCallbackProvider.builder()
                .toolObjects(fileSystemService)
                .build();
    }
}
