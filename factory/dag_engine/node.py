class TaskNode:

    def __init__(
        self,
        name,
        handler,
        dependencies=None
    ):

        self.name = name
        self.handler = handler
        self.dependencies = dependencies or []

        self.completed = False
        self.result = None