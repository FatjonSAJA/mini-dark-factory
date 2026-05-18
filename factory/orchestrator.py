from .spec_engine.parser import parse_spec
from .planner_agent.planner import create_plan
from .backend_builder.builder import build_backend
from .frontend_builder.builder import build_frontend
from .tester_agent.tester import run_tests


def run_factory(spec_text):

    spec = parse_spec(spec_text)

    plan = create_plan(spec)

    backend = build_backend(plan["backend_tasks"])
    frontend = build_frontend(plan["frontend_tasks"])

    tests = run_tests()

    return {
        "spec": spec,
        "plan": plan,
        "backend": backend,
        "frontend": frontend,
        "tests": tests
    }