def create_plan(spec):
    return {
        "backend_tasks": [
            {"type": "model", "name": "Car"},
            {"type": "serializer", "name": "Car"},
            {"type": "viewset", "name": "CarViewSet"}
        ],
        "frontend_tasks": [
            {"type": "component", "name": "CarTable"},
            {"type": "component", "name": "CarForm"},
            {"type": "api", "name": "carService"}
        ]
    }