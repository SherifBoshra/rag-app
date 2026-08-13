from enum import Enum


class LLMEnums(Enum):

    OPENAI = "OPENAI"
    COHERE = "COHERE"


class OpenAIEnums(Enum):

    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"

class CohereEnums(Enum):

    USER = "USER"
    SYSTEM = "SYSTEM"
    ASSISTANT = "CHATBOT"

    DOCUMET = "search_document"
    QUERY = "search_query"


class DocumentTypeEnum(Enum):
    DOCUMET = "document"
    QUERY = "query"