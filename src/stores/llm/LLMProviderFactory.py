from .LLMEnums import LLMEnums
from .providers import CohereProvider , OpenAIProvider


class LLMProviderFactory:

    def __init__(self , config : dict):

        self.config = config

    def create(self , provider : str):
        if provider == LLMEnums.OPENAI.value:
            return OpenAIProvider(
                api_key= self.config.OPENAI_API_KEY,
                api_url=OPENAI_API_URL,
                default_generation_max_output_tokens=GENERATION_DEFAULT_MAX_TOKENS,
                default_generation_temperature=GENERATION_DEFAULT_TEMPERATURE,
                default_input_max_characters=INPUT_DEFAULT_MAX_CHARACTERS
            )

        if provider == LLMEnums.COHERE.value:
            return CohereProvider(
                api_key=COHERE_API_KEY,
                default_generation_max_output_tokens=GENERATION_DEFAULT_MAX_TOKENS,
                default_generation_temperature=GENERATION_DEFAULT_TEMPERATURE,
                default_input_max_characters=INPUT_DEFAULT_MAX_CHARACTERS
            )

        return None
