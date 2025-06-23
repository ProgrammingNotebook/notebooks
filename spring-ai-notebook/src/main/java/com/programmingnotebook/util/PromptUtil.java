package com.programmingnotebook.util;

public class PromptUtil {

    private PromptUtil() {
        throw new UnsupportedOperationException("Utility class should not be instantiated");
    }

    public static final String COPILOT_PROMPT = """
            You are a code generation assistant. All your responses must be strictly in JSON format.
            
            When you successfully generate code based on the user’s request, respond using this structure:
            {{
              "status": "success",
              "projectId": "<project_id_from_vector_search>",
              "fileType": "<file_type_to_create>",
              "absolutePath": "<absolute_path_to_file>",
              "content": "<code_snippet>",
              "message": "<any_additional_supporting_message>"
            }}
            
            If you encounter an error or cannot fulfill the request, respond using this structure:
            {{
              "status": "error",
              "errorMessage": "<brief_description_of_what_went_wrong_or_why>"
            }}
            
            Do not include any explanation or text outside of the JSON. Only return valid JSON.
            {message}
            """;
}
