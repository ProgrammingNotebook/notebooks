package com.akaal.api.configuration;

import org.springframework.ai.azure.openai.AzureOpenAiChatModel;
import org.springframework.ai.chat.client.ChatClient;
import org.springframework.ai.tool.ToolCallbackProvider;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ModelConfiguration {

    @Bean
    public ChatClient chatClient(AzureOpenAiChatModel azureOpenAiChatModel,
                                 ToolCallbackProvider toolCallbackProvider) {

        return ChatClient
                .builder(azureOpenAiChatModel)
                .defaultToolCallbacks(toolCallbackProvider)
                .build();
    }
}
