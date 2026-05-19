def build_frontend(tasks):

    generated = {}

    for task in tasks:

        if task["type"] == "component":

            generated[f"{task['name']}.jsx"] = f"""
export default function {task['name']}() {{
  return (
    <div>
      <h1>{task['name']}</h1>
    </div>
  );
}}
"""

        if task["type"] == "api_service":

            generated["carService.js"] = """
import axios from "axios";

const API = "http://localhost:8000/api/cars/";

export const getCars = () => axios.get(API);

export const createCar = (data) =>
  axios.post(API, data);

export const updateCar = (id, data) =>
  axios.put(`${API}${id}/`, data);

export const deleteCar = (id) =>
  axios.delete(`${API}${id}/`);
"""

    return generated