from dataclasses import dataclass

@dataclass
class FeatureSpec:
    name: str
    backend: list
    frontend: list
    tests: list