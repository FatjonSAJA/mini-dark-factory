import yaml
from .schema import FeatureSpec

def parse_spec(file_path):
    with open(file_path, "r") as f:
        raw = yaml.safe_load(f)

    return FeatureSpec(
        name=raw["name"],
        backend=raw["backend"],
        frontend=raw["frontend"],
        tests=raw["tests"]
    )