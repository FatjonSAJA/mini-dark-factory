from factory.spec_engine.repair import repair_spec


MAX_ITERATIONS = 5


def run_factory(spec_text):

    current_spec = spec_text

    for i in range(MAX_ITERATIONS):

        print(f"🔁 Iteration {i+1}")

        plan = create_plan(current_spec)

        backend = build_backend(plan["backend_tasks"])

        frontend = build_frontend(plan["frontend_tasks"])

        tests = run_tests()

        failures = [t for t in tests if not t["status"]]

        if not failures:
            return {
                "status": "SUCCESS",
                "plan": plan
            }

        current_spec = repair_spec(
            current_spec,
            failures
        )

    return {"status": "FAILED"}