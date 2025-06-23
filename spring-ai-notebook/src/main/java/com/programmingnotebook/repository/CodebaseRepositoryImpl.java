package com.programmingnotebook.repository;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.ai.document.Document;
import org.springframework.ai.vectorstore.VectorStore;
import org.springframework.stereotype.Repository;

import java.util.List;

@Slf4j
@Repository
@RequiredArgsConstructor
public class CodebaseRepositoryImpl implements CodebaseRepository {

    private final VectorStore vectorStore;

    @Override
    public void loadCodebase(List<Document> documents) {
        log.info("Loading {} codebase documents into the vector database", documents.size());
        vectorStore.add(documents);
    }
}
