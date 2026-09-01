"""agentaigenai - AI Agent and Q&A Chatbot Application."""

import sys
import subprocess

__version__ = "0.1.0"
__author__ = "mynameisaditya26"


def main() -> None:
    """Entry point for the application."""
    import streamlit.cli
    
    # Run the Streamlit chatbot application
    current_dir = __file__.replace("__init__.py", "")
    app_path = current_dir.replace("src/agentaigenai", "1-LangchainBasics/Q&Achatbot.py")
    
    # Use streamlit to run the app
    sys.argv = ["streamlit", "run", app_path]
    streamlit.cli.main()
