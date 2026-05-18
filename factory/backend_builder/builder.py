def build_backend(tasks):
    files = {}

    for task in tasks:
        if task["type"] == "model":
            files["models.py"] = generate_model(task["name"])

        if task["type"] == "serializer":
            files["serializers.py"] = generate_serializer(task["name"])

        if task["type"] == "viewset":
            files["views.py"] = generate_viewset(task["name"])

    return files