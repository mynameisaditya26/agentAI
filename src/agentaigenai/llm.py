"""LLM initialization and management module."""

import os
from typing import Literal
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


def get_llm(
    model: Literal["groq", "openai"] = "groq",
    temperature: float = 0.7
):
    """
    Initialize and return an LLM instance.
    
    Args:
        model: Choice between "groq" or "openai"
        temperature: Temperature for response generation (0.0 to 1.0)
        
    Returns:
        Initialized LLM instance
        
    Raises:
        ValueError: If required API key is not found
    """
    if model == "groq":
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        return ChatGroq(
            model="mixtral-8x7b-32768",
            temperature=temperature,
            api_key=api_key
        )
    elif model == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        return ChatOpenAI(
            model="gpt-4",
            temperature=temperature,
            api_key=api_key
        )
    else:
        raise ValueError(f"Unknown model: {model}. Choose from 'groq' or 'openai'")
