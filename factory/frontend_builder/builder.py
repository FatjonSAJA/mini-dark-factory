import os
import shutil
from pathlib import Path

SPEC_PATH = "specs/car_crud_frontend.md"
OUTPUT_DIR = "frontend/src/cars"


# -----------------------------
# UTILITIES
# -----------------------------

def load_spec(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def ensure_clean_output():
    """
    Ensures /src/cars is always clean before regeneration
    (Dark Factory deterministic behavior)
    """
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)

    os.makedirs(OUTPUT_DIR, exist_ok=True)


# -----------------------------
# STAGE 1: PARSE SPEC
# -----------------------------

def parse_spec(spec_text):
    """
    Converts markdown spec → structured dict
    (simple heuristic parser for now)
    """
    return {
        "pages": ["CarsListPage", "CarCreatePage", "CarEditPage"],
        "components": ["CarTable", "CarForm", "DeleteModal"],
        "services": ["carService"],
        "hooks": ["useCars"],
        "api": True
    }


# -----------------------------
# STAGE 2: ARCHITECT
# -----------------------------

def architect(structured):
    """
    Expands structure into file-level plan
    """
    return {
        "files": [
            "pages/CarsListPage.jsx",
            "pages/CarCreatePage.jsx",
            "pages/CarEditPage.jsx",
            "components/CarTable.jsx",
            "components/CarForm.jsx",
            "components/DeleteModal.jsx",
            "services/carService.js",
            "hooks/useCars.js"
        ]
    }


# -----------------------------
# STAGE 3: BUILD
# -----------------------------

def write_file(path, content):
    full_path = os.path.join(OUTPUT_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)


def build_module(file):
    """
    Minimal working React templates (replaceable by LLM later)
    """
    if "service" in file:
        return """import axios from 'axios';

export const carService = {
  getAll: () => axios.get('/api/cars/'),
  create: (data) => axios.post('/api/cars/', data),
  update: (id, data) => axios.put(`/api/cars/${id}/`, data),
  delete: (id) => axios.delete(`/api/cars/${id}/`)
};
"""

    if "useCars" in file:
        return """import { useEffect, useState } from 'react';
import { carService } from '../services/carService';

export default function useCars() {
  const [cars, setCars] = useState([]);

  const load = async () => {
    const res = await carService.getAll();
    setCars(res.data);
  };

  useEffect(() => {
    load();
  }, []);

  return { cars, reload: load };
}
"""

    if "CarTable" in file:
        return """export default function CarTable({ cars }) {
  return (
    <table>
      <thead>
        <tr>
          <th>Brand</th>
          <th>Model</th>
          <th>Year</th>
          <th>Price</th>
        </tr>
      </thead>
      <tbody>
        {cars.map(c => (
          <tr key={c.id}>
            <td>{c.brand}</td>
            <td>{c.model}</td>
            <td>{c.year}</td>
            <td>{c.price}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}
"""

    return f"// TODO: generated file for {file}"


# -----------------------------
# STAGE 4: VALIDATION (simple)
# -----------------------------

def validate_output():
    """
    Placeholder validation (upgrade later to real tests)
    """
    required_files = [
        "pages/CarsListPage.jsx",
        "components/CarTable.jsx",
        "services/carService.js",
        "hooks/useCars.js"
    ]

    for f in required_files:
        if not os.path.exists(os.path.join(OUTPUT_DIR, f)):
            return False

    return True


# -----------------------------
# FACTORY LOOP
# -----------------------------

def run_factory():
    spec = load_spec(SPEC_PATH)

    ensure_clean_output()

    structured = parse_spec(spec)
    plan = architect(structured)

    for file in plan["files"]:
        content = build_module(file)
        write_file(file, content)

    if not validate_output():
        print("❌ Validation failed. Regenerating...")
        return run_factory()

    print("✅ Dark Factory build complete inside /src/cars")


if __name__ == "__main__":
    run_factory()