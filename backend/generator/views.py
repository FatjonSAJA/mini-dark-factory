from rest_framework.views import APIView
from rest_framework.response import Response
from .ollama_client import call_ollama
import json
import re

def extract_json(text):
    try:
        # First attempt: normal parse
        return json.loads(text)
    except:
        # Second attempt: extract partial JSON
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if not match:
            raise Exception("No JSON found")

        try:
            return json.loads(match.group())
        except:
            raise Exception("Malformed JSON even after extraction")

def call_with_retry(prompt, max_retries=3):
    for i in range(max_retries):
        raw = call_ollama(prompt)

        try:
            return extract_json(raw)
        except:
            continue

    raise Exception("Model failed after retries")

def build_prompt(spec):
    return f"""
        You are a STRICT JSON generator.
        
        Return ONLY valid JSON.
        
        No markdown.
        No explanation.
        No extra text.
        
        If you fail, return: {{}}
        
        Schema:
        {{
          "model_name": "string",
          "fields": [
            {{"name": "string", "type": "string"}}
          ]
        }}
        
        Task:
        Create a Django model schema for: {spec}
        """

class GenerateApp(APIView):

    def post(self, request):
        spec = request.data.get("spec")

        prompt = build_prompt(spec)

        try:
            data = call_with_retry(prompt)
        except Exception as e:
            return Response({
                "error": str(e)
            }, status=400)

        return Response(data)