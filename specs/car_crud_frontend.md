# CAR CRUD FRONTEND SPEC

## 1. PURPOSE
Build a fully functional CRUD UI for managing cars.

This spec is the ONLY source of truth.
No manual UI implementation is allowed.

---

## 2. DATA MODEL (from backend API)

Car:
- id: integer
- brand: string
- model: string
- year: integer
- price: float

---

## 3. API CONTRACT

GET    /api/cars/       → list cars
POST   /api/cars/       → create car
GET    /api/cars/{id}/  → get car
PUT    /api/cars/{id}/  → update car
DELETE /api/cars/{id}/  → delete car

---

## 4. UI REQUIREMENTS

The agent must generate a React UI with:

### 4.1 Pages
- /cars → list page
- /cars/new → create page
- /cars/{id}/edit → edit page

### 4.2 Components
- CarTable
- CarForm
- DeleteConfirmationModal

---

## 5. UX RULES (IMPORTANT)

- Must be fully responsive
- Must show loading states
- Must show error states
- Must auto-refresh after CRUD actions
- Must NOT require page reload

---

## 6. VALIDATION RULES (HOLDOUT TESTS)

Agent must pass:

- Creating a car updates list immediately
- Editing car persists after refresh
- Deleting car removes row instantly
- API failure shows error UI

---

## 7. ACCEPTANCE CRITERIA

Build is valid ONLY if:

✔ All CRUD operations work  
✔ No console errors  
✔ UI matches API schema  
✔ Tests pass (see /tests/frontend)

---

## 8. AUTONOMY RULE

Human developers must NOT modify React code directly.

All changes must be generated via:
→ frontend_builder agent
→ validation agent loop