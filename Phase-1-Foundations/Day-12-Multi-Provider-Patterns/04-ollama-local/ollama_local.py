"""
An Ollama provider function -- a model running locally, no API key.

Setup:
    1. Install Ollama from ollama.com
    2. ollama pull llama3.2
    pip install ollama
Run:
    python ollama_local.py
"""

import ollama


def ask_ollama(prompt: str) -> str:
    """Send a prompt to a local Ollama model, return the answer text."""
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
    )
    return response["message"]["content"].strip()


if __name__ == "__main__":
    # Requires the Ollama app running and the model pulled.
    print(ask_ollama("In one sentence, why run an LLM locally?"))
