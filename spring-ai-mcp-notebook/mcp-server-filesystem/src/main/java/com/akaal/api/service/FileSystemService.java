package com.akaal.api.service;

import lombok.extern.slf4j.Slf4j;
import org.springframework.ai.tool.annotation.Tool;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

@Slf4j
@Service
public class FileSystemService {

    @Tool(name = "Create File", description = "Create a file with the provided fileName on the file system")
    public String createFile(String fileName) {

        log.info("Request to create a file: {}", fileName);

        Path path = Paths.get(fileName);

        try {
            Files.createFile(path);
            log.info("File created: {}", path.toAbsolutePath());
            return "File [" + fileName + "] created successfully";
        } catch (IOException e) {
            log.error("Error creating file: {}", e.getMessage());
            return "File [" + fileName + "] already exists.";
        }
    }
}
