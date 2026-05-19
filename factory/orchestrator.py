from factory.dag_engine.graph import build_graph
from factory.dag_engine.executor import execute_graph

from factory.spec_engine.repair import repair_spec

from factory.logger import log_message

# 🔥 NEW IMPORTS
from factory.artifact_writer.backend_writer import (
    write_backend_files
)

from factory.artifact_writer.frontend_writer import (
    write_frontend_files
)

from factory.runtime.django_runtime import (
    run_migrations
)

from factory.runtime.process_manager import (
    start_django,
    stop_django
)

from factory.runtime.healthcheck import (
    wait_for_backend
)


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

        # 🔥 WRITE GENERATED FILES
        write_backend_files(
            context["backend"]
        )

        write_frontend_files(
            context["frontend"]
        )

        # 🔥 RUN DJANGO MIGRATIONS
        run_migrations()

        # 🔥 START DJANGO
        start_django()

        # 🔥 WAIT FOR HEALTH
        healthy = wait_for_backend()

        if not healthy:

            print(
                "❌ Backend failed healthcheck"
            )

            continue

        failures = [
            t for t in context["tests"]
            if not t["status"]
        ]

        if not failures:

            stop_django()

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

    stop_django()

    return {
        "status": "FAILED"
    }