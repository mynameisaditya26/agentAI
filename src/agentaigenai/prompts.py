"""Prompt templates for various use cases."""

from langchain.prompts import ChatPromptTemplate

# General Q&A prompt
QA_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful and knowledgeable AI assistant. Answer questions accurately and concisely."),
    ("human", "{question}")
])

# Expert mode prompt
EXPERT_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """You are an expert AI assistant with deep knowledge across multiple domains. 
    Provide detailed, accurate, and well-reasoned answers. When appropriate, include:
    - Relevant background information
    - Key concepts and definitions
    - Examples and case studies
    - Potential limitations or considerations"""),
    ("human", "{question}")
])

# Summarization prompt
SUMMARIZE_PROMPT = ChatPromptTemplate.from_messages([
    ("system", "You are an expert summarizer. Create clear, concise summaries that capture the key points."),
    ("human", "Please summarize the following text:\n\n{text}")
])

# Creative writing prompt
CREATIVE_PROMPT = ChatPromptTemplate.from_messages([
    ("system", """You are a creative writing assistant. Generate imaginative, engaging, and original content.
    Be creative, descriptive, and engaging in your writing."""),
    ("human", "{prompt}")
])
