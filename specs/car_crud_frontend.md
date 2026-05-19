# FEATURE: Car CRUD Frontend (React)

## GOAL
Build a fully working React CRUD UI that connects to the Django API at:

http://127.0.0.1:8000/api/cars/

---

## DATA MODEL

Car object:

- id (integer)
- plate_number (string)
- brand (string)
- model (string)
- year (integer)

---

## API ENDPOINTS

- GET    /api/cars/        → list all cars
- POST   /api/cars/        → create car
- PUT    /api/cars/{id}/   → update car
- DELETE /api/cars/{id}/   → delete car

---

## FRONTEND REQUIREMENTS

### 1. API SERVICE (mandatory)

Create a centralized API file:

frontend/src/api/cars.js

It must include:

- getCars()
- createCar(data)
- updateCar(id, data)
- deleteCar(id)

All using axios.

---

### 2. COMPONENTS

Generate these React components:

#### CarTable.jsx
- Fetch and display list of cars
- Show:
  - plate_number
  - brand
  - model
  - year
- Include "Delete" button per row
- Refresh list after delete

---

#### CarForm.jsx
- Controlled form with fields:
  - plate_number
  - brand
  - model
  - year
- Submit button creates car via API
- Clears form after submit
- Refresh table after create

---

#### Optional (if needed by builder):
- EditCarModal.jsx (for updating cars)

---

### 3. STATE MANAGEMENT RULES

- Use React hooks only (useState, useEffect)
- No Redux
- No external state libraries

---

### 4. DATA FLOW

- CarForm → POST /api/cars/
- CarTable → GET /api/cars/
- Delete button → DELETE /api/cars/{id}/

---

### 5. UI RULES

- Simple table layout
- Minimal styling
- Functional over design
- Must be fully working CRUD, not mock UI

---

### 6. INTEGRATION RULE

All components must be connected via:

- frontend/src/App.jsx

App.jsx must:
- render CarForm
- render CarTable
- ensure state refresh between them

---

## SUCCESS CRITERIA

Frontend is considered complete if:

✔ Cars can be created  
✔ Cars are listed  
✔ Cars can be deleted  
✔ UI updates without refresh  
✔ No console errors  