"""Configuration and constants for the application."""

import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Model configurations
DEFAULT_MODEL = "groq"
DEFAULT_TEMPERATURE = 0.7

# LLM Models
GROQ_MODELS = {
    "mixtral": "mixtral-8x7b-32768",
    "llama2": "llama2-70b-4096",
    "gemma": "gemma-7b-it",
}

OPENAI_MODELS = {
    "gpt4": "gpt-4",
    "gpt4_turbo": "gpt-4-turbo-preview",
    "gpt35": "gpt-3.5-turbo",
}

# Application settings
APP_TITLE = "Q&A Chatbot"
APP_DESCRIPTION = "Interactive Q&A chatbot powered by LangChain and advanced LLMs"
