PLANNING_GRAPH = {
    "parse": ["plan_backend", "plan_frontend"],
    "plan_backend": ["build_backend"],
    "plan_frontend": ["build_frontend"],
    "build_backend": ["test"],
    "build_frontend": ["test"],
    "test": ["evaluate"],
    "evaluate": ["end", "repair"]
}