# AgentAIGenAI - Q&A Chatbot with LangChain

A powerful, interactive Q&A chatbot application built with **LangChain**, **Streamlit**, and advanced LLMs (Groq & OpenAI).

## 🚀 Features

- **Multi-Model Support**: Choose between Groq (fast & free) and OpenAI (GPT-4)
- **Interactive Chat Interface**: Built with Streamlit for a smooth user experience
- **Customizable System Prompts**: Adjust AI behavior to your needs
- **Temperature Control**: Fine-tune response creativity
- **Chat History**: Maintain conversation context
- **Environment-Based Configuration**: Easy API key management

## 📋 Prerequisites

- Python 3.13+
- Groq API Key (free at [console.groq.com](https://console.groq.com))
- OpenAI API Key (optional, from [platform.openai.com](https://platform.openai.com))

## 🔧 Installation & Setup

### 1. Clone or Navigate to Project
```bash
cd agentAIgenAI
```

### 2. Set Up Environment Variables
Copy the example environment file and add your API keys:
```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
```env
GROQ_API_KEY=your_groq_key_here
OPENAI_API_KEY=your_openai_key_here
```

### 3. Install Dependencies

Using UV (recommended):
```bash
uv sync
```

Or using pip:
```bash
pip install -r requirements.txt
```

## 🏃 Running the Application

### Using Streamlit directly:
```bash
streamlit run 1-LangchainBasics/Q&Achatbot.py
```

### Using the package entry point:
```bash
python -m agentaigenai
```

## 📁 Project Structure

```
agentAIgenAI/
├── 1-LangchainBasics/
│   ├── Q&Achatbot.py          # Main Streamlit application
│   └── langchain.ipynb         # Learning notebook
├── src/
│   └── agentaigenai/
│       ├── __init__.py         # Package entry point
│       ├── config.py           # Configuration & constants
│       ├── llm.py              # LLM initialization
│       └── prompts.py          # Prompt templates
├── .env.example                # Environment variables template
├── pyproject.toml              # Project metadata & dependencies
├── requirements.txt            # pip dependencies
└── README.md                   # This file
```

## 💡 Usage Guide

### 1. Start the Application
```bash
streamlit run 1-LangchainBasics/Q&Achatbot.py
```

### 2. Configure Settings (Sidebar)
- **Select Model**: Choose between Groq or OpenAI
- **Temperature**: Adjust creativity (0.0 = deterministic, 1.0 = creative)
- **System Prompt**: Customize AI behavior
- **Clear Chat**: Reset conversation history

### 3. Ask Questions
Type your questions in the chat input and press Enter. The AI will respond based on your selected model and settings.

## 🔑 API Keys

### Groq API Key
1. Visit [console.groq.com](https://console.groq.com)
2. Sign up for free account
3. Generate API key
4. Add to `.env` as `GROQ_API_KEY`

### OpenAI API Key
1. Visit [platform.openai.com](https://platform.openai.com)
2. Create account and add billing
3. Generate API key
4. Add to `.env` as `OPENAI_API_KEY`

## 📦 Dependencies

- **LangChain**: LLM framework for building applications
- **Streamlit**: Web UI framework
- **LangChain-Groq**: Groq integration
- **LangChain-OpenAI**: OpenAI integration
- **LanGraph**: State management for multi-step workflows
- **python-dotenv**: Environment variable management

## 🚀 Next Steps

- Explore advanced LangChain features (RAG, Agents, Chains)
- Integrate with document loaders for PDF/text processing
- Add memory for persistent conversations
- Build custom tools and functions
- Deploy to Streamlit Cloud

## 📝 License

This project is part of the AgentAI & GenAI learning initiative.

## 👨‍💻 Author

Created by: mynameisaditya26 (as8975630@gmail.com)

## 🆘 Troubleshooting

### "API key not found" error
- Ensure `.env` file exists in the project root
- Verify API keys are correctly set
- Restart the Streamlit app

### "Module not found" error
- Run `uv sync` or `pip install -r requirements.txt`
- Ensure you're in the project directory

### Slow responses
- Switch to Groq model (faster & free)
- Lower the temperature setting
- Check internet connection

## 🔗 Useful Resources

- [LangChain Documentation](https://python.langchain.com)
- [Streamlit Documentation](https://docs.streamlit.io)
- [Groq Console](https://console.groq.com)
- [OpenAI API Reference](https://platform.openai.com/docs)
