from pathlib import Path

from factory.llm.client import OllamaClient


PROMPT_PATH = Path("factory/llm/prompts/repair.md")


def repair_spec(spec_text, test_failures):

    system_prompt = PROMPT_PATH.read_text()

    final_prompt = f"""
{system_prompt}

# CURRENT SPEC

{spec_text}

# TEST FAILURES

{test_failures}
"""

    llm = OllamaClient(model="llama3")

    return llm.generate(final_prompt)