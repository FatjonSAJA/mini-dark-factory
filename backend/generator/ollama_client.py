import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def call_ollama(prompt, model="llama3:latest"):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": model,
            "prompt": prompt,
            "stream": False,
            "temperature": 0.1
        }
    )

    return response.json()["response"]