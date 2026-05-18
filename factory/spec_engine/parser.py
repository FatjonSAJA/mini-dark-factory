def parse_spec(spec_text: str):
    """
    Converts raw markdown spec → structured JSON
    """
    return {
        "features": [],
        "backend_requirements": [],
        "frontend_requirements": [],
        "rules": []
    }