import { useState } from "react";
import axios from "axios";

function App() {
  const [form, setForm] = useState({
    brand: "",
    model: "",
    year: "",
    plate_number: "",
  });

  const handleChange = (e) => {
    setForm({
      ...form,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    await axios.post(
      "http://127.0.0.1:8000/api/cars/",
      form
    );

    alert("Car saved!");

    setForm({
      brand: "",
      model: "",
      year: "",
      plate_number: "",
    });
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Register Car</h1>

      <form onSubmit={handleSubmit}>
        <input
          name="brand"
          placeholder="Brand"
          value={form.brand}
          onChange={handleChange}
        />

        <br /><br />

        <input
          name="model"
          placeholder="Model"
          value={form.model}
          onChange={handleChange}
        />

        <br /><br />

        <input
          name="year"
          placeholder="Year"
          value={form.year}
          onChange={handleChange}
        />

        <br /><br />

        <input
          name="plate_number"
          placeholder="Plate Number"
          value={form.plate_number}
          onChange={handleChange}
        />

        <br /><br />

        <button type="submit">
          Save Car
        </button>
      </form>
    </div>
  );
}

export default App;