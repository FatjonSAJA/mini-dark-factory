from concurrent.futures import ThreadPoolExecutor
from factory.logger import log_message

def execute_node(node, context):
    try:

        print(f"🚀 Running node: {node.name}")

        if node.name == "planner":

            result = node.handler(
                context["input"]
            )
            log_message(
                f"{node.name}.log",
                result
            )
            context["plan"] = result

        elif node.name == "backend_builder":

            result = node.handler(
                context["plan"]["backend_tasks"]
            )
            log_message(
                f"{node.name}.log",
                result
            )
            context["backend"] = result

        elif node.name == "frontend_builder":

            result = node.handler(
                context["plan"]["frontend_tasks"]
            )
            log_message(
                f"{node.name}.log",
                result
            )
            context["frontend"] = result

        elif node.name == "tester":

            result = node.handler()
            log_message(
                f"{node.name}.log",
                result
            )
            context["tests"] = result

        node.result = result
        node.completed = True
        print(f"✅ Completed node: {node.name}")
    except Exception as e:

        log_message(
            f"{node.name}_errors.log",
            str(e)
        )

        print(f"❌ Node failed: {node.name}")

        print(str(e))

        node.completed = True

        raise

def execute_graph(nodes, initial_input):
    max_cycles = 50

    cycle = 0
    context = {
        "input": initial_input
    }

    while True:

        pending = [
            n for n in nodes.values()
            if not n.completed
        ]

        if not pending:
            break

        runnable = []

        for node in pending:

            dependencies_done = all(
                nodes[d].completed
                for d in node.dependencies
            )

            if dependencies_done:
                runnable.append(node)

        if not runnable:
            break

        with ThreadPoolExecutor() as executor:

            futures = [
                executor.submit(
                    execute_node,
                    node,
                    context
                )
                for node in runnable
            ]

            for future in futures:
                future.result()
        cycle += 1

        if cycle > max_cycles:
            raise Exception(
                "DAG executor exceeded max cycles"
            )
    return context