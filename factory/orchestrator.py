from factory.dag_engine.graph import build_graph
from factory.dag_engine.executor import execute_graph
from factory.spec_engine.repair import repair_spec
from factory.logger import log_message

MAX_ITERATIONS = 5


def run_factory(spec_text):

    current_spec = spec_text

    for i in range(MAX_ITERATIONS):

        print(f"\n🔁 ITERATION {i+1}")

        graph = build_graph()

        context = execute_graph(
            graph,
            current_spec
        )

        failures = [
            t for t in context["tests"]
            if not t["status"]
        ]

        if not failures:

            return {
                "status": "SUCCESS",
                "context": context
            }

        current_spec = repair_spec(
            current_spec,
            failures
        )

        log_message(
            "iterations.log",
            {
                "iteration": i + 1,
                "tests": failures
            }
        )

    return {
        "status": "FAILED"
    }