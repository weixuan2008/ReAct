import os
from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()


class AzureLLMConfig:
    def __init__(self):
        self.llm = AzureChatOpenAI(
            deployment_name=os.getenv("azure_deployment_name"),  # Replace with your Azure deployment name
            model_name=os.getenv("azure_model_name"),  # Replace with your Azure model name
            azure_endpoint=os.getenv("azure_endpoint"),  # Replace with your Azure endpoint
            openai_api_key=os.getenv("azure_openai_api_key"),  # Replace with your Azure OpenAI API key
            openai_api_version=os.getenv("azure_openai_api_version"),  # Ensure this matches your API version
            temperature=0.1  # Deterministic
        )


class OpenAILLMConfig:
    def __init__(self):
        url = str(os.getenv("azure_endpoint")) + "openai/deployments/" + str(os.getenv("azure_deployment_name"))
        self.llm = OpenAI(
            api_key=os.getenv("azure_openai_api_key"),
            base_url=url,
            default_query={"api-version": "2025-01-01-preview"},
            default_headers={
                "api-key": os.getenv("azure_openai_api_key")
            }

        )


class Config:
    def __init__(self):
        self.azure_config = AzureLLMConfig()
        self.openai_config = OpenAILLMConfig()

# # Example usage
# config = Config()
