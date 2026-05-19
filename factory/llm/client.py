import requests


OLLAMA_URL = "http://localhost:11434/api/generate"


class OllamaClient:

    def __init__(self, model="mistral"):
        self.model = model

    def generate(self, prompt: str):

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False
            }
        )

        data = response.json()

        return data["response"]