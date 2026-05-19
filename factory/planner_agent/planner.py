import json
from pathlib import Path

from factory.llm.client import OllamaClient


PROMPT_PATH = Path("factory/llm/prompts/planner.md")


def create_plan(spec_text: str):

    system_prompt = PROMPT_PATH.read_text()

    final_prompt = f"""
{system_prompt}

# SPECIFICATION

{spec_text}
"""

    llm = OllamaClient(model="mistral")

    response = llm.generate(final_prompt)

    return json.loads(response)