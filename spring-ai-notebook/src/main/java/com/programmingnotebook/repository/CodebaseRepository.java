package com.programmingnotebook.repository;

import org.springframework.ai.document.Document;

import java.util.List;

public interface CodebaseRepository {

    void loadCodebase(List<Document> documents);

}
