def build_frontend(tasks):
    output = {}

    for task in tasks:
        if task["type"] == "component":
            output[f"{task['name']}.jsx"] = generate_component(task["name"])

        if task["type"] == "api":
            output["api.js"] = generate_api()

    return output

def generate_component(name):
    return f"""
export default function {name}() {{
  return (
    <div>
      <h1>{name}</h1>
    </div>
  );
}}
"""