from factory.dag_engine.node import TaskNode

from factory.planner_agent.planner import create_plan
from factory.backend_builder.builder import build_backend
from factory.frontend_builder.builder import build_frontend
from factory.tester_agent.tester import run_tests


def build_graph():

    planner = TaskNode(
        name="planner",
        handler=create_plan
    )

    backend = TaskNode(
        name="backend_builder",
        handler=build_backend,
        dependencies=["planner"]
    )

    frontend = TaskNode(
        name="frontend_builder",
        handler=build_frontend,
        dependencies=["planner"]
    )

    tester = TaskNode(
        name="tester",
        handler=run_tests,
        dependencies=[
            "backend_builder",
            "frontend_builder"
        ]
    )

    return {
        "planner": planner,
        "backend_builder": backend,
        "frontend_builder": frontend,
        "tester": tester
    }