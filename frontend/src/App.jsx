import CarTable from "./generated/CarTable";
import CarForm from "./generated/CarForm";

export default function App() {
  return (
    <div>
      <h1>Dark Factory - Car CRUD</h1>

      <CarForm />

      <CarTable />
    </div>
  );
}