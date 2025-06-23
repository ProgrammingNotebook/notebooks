package com.programmingnotebook.service;

import com.programmingnotebook.repository.CodebaseRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.ai.document.Document;
import org.springframework.ai.reader.tika.TikaDocumentReader;
import org.springframework.ai.transformer.splitter.TokenTextSplitter;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.core.io.FileSystemResource;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Stream;

@Slf4j
@Service
@RequiredArgsConstructor
public class CodebaseServiceImpl implements CodebaseService {

    private final CodebaseRepository codebaseRepository;

    @Value("${spring.app.sain.documents.folder.location}")
    private String documentFolderLocation;

    private static final List<String> allowedExtensions = List.of(".java", ".xml", ".yaml", ".yml");

    @Override
    public void loadCodebaseInVectorDatabase() {

        log.info("Loading codebase into the vector database");

        File baseDirectory = new File(documentFolderLocation);

        if (!baseDirectory.exists() || !baseDirectory.isDirectory()) {

            log.error("Invalid directory path: {}", documentFolderLocation);
            return;
        }

        List<Document> codebaseDocuments = readDocumentsFromDocumentFolder();
        if (codebaseDocuments.isEmpty()) {
            log.error("No files with allowed extensions: {} found in the directory: {}",
                    allowedExtensions, documentFolderLocation);
            return;
        }

        List<Document> chunkedDocuments = transformDocumentUsingTextSplitter(codebaseDocuments);

        List<String> documentIdsToLog = new ArrayList<>();
        if (!chunkedDocuments.isEmpty()) {

            for (Document chunkedDocument : chunkedDocuments) {
                documentIdsToLog.add(chunkedDocument.getId() + " (Source: " + chunkedDocument.getMetadata()
                        .getOrDefault("file_name", "Unknown") + ")");
            }

            log.info("Adding {} document chunk to codebase repository", chunkedDocuments.size());
            codebaseRepository.loadCodebase(chunkedDocuments);
            log.info("Successfully added {} document chunk to codebase repository", chunkedDocuments.size());

            log.info("--- Document IDs added to codebase repository ---");
            documentIdsToLog.forEach(log::info);
            log.info("--- End of Document IDs ---");

        } else {
            log.error("No document chunks were found.");
        }
    }

    private List<Document> readDocumentsFromDocumentFolder() {

        try (Stream<Path> pathStream = Files.walk(Paths.get(documentFolderLocation))) {

            List<Path> filePathsToProcess = pathStream
                    .filter(Files::isRegularFile)
                    .filter(path -> {
                        String fileName = path.getFileName().toString().toLowerCase();
                        return allowedExtensions.stream().anyMatch(fileName::endsWith);
                    })
                    .toList();

            if (filePathsToProcess.isEmpty()) return Collections.emptyList();

            log.info("Found {} files with allowed extensions", filePathsToProcess.size());
            return extractFilesWithMetadata(filePathsToProcess);

        } catch (IOException ioException) {
            log.error("Error walking the directory: {}. Error: {}", documentFolderLocation, ioException.getMessage());
        }

        return Collections.emptyList();
    }

    private List<Document> extractFilesWithMetadata(List<Path> filePathsToProcess) {

        List<Document> codebaseDocuments = new ArrayList<>();

        for (Path filePath : filePathsToProcess) {
            try {

                log.info("Processing file: {}", filePath);
                FileSystemResource fileSystemResource = new FileSystemResource(filePath);
                TikaDocumentReader tikaDocumentReader = new TikaDocumentReader(fileSystemResource);

                List<Document> documentsFromFile = tikaDocumentReader.get();

                if (documentsFromFile != null && !documentsFromFile.isEmpty()) {

                    // Enhance documents with metadata.
                    for (Document document : documentsFromFile) {
                        document.getMetadata().putIfAbsent("source_uri", filePath.toUri().toString());
                        document.getMetadata().putIfAbsent("file_name", filePath.getFileName().toString());
                    }

                    codebaseDocuments.addAll(documentsFromFile);
                    log.info("Successfully read {} document(s) from: {}", documentsFromFile.size(), filePath);
                } else {
                    log.warn("No documents were found.");
                }
            } catch (Exception e) {
                log.error("Failed to read or process file: {}. Error: {}", filePath, e.getMessage());
            }
        }

        return codebaseDocuments;
    }

    private List<Document> transformDocumentUsingTextSplitter(List<Document> allRawDocuments) {

        TokenTextSplitter tokenTextSplitter = new TokenTextSplitter(
                1000,
                50,
                10,
                10000,
                true);
        log.info("Applying text splitter to {} document object.", allRawDocuments.size());
        List<Document> chunkedDocuments = tokenTextSplitter.apply(allRawDocuments);

        log.info("Raw documents were chunked into: {} documents", chunkedDocuments.size());
        return chunkedDocuments;
    }
}
