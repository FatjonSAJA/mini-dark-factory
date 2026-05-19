# CAR CRUD FRONTEND - DARK FACTORY SPEC

## 1. PURPOSE
This spec defines a fully autonomous frontend generation system for a Car CRUD module.

The system MUST generate code directly into:
👉 frontend/src/cars

No manual UI coding is allowed inside this module.

---

## 2. OWNERSHIP RULE (CRITICAL)

The factory owns ONLY:

/src/cars/**

It MUST NOT modify:
- /src/app
- /src/shared
- routing outside /cars
- global state

---

## 3. DATA MODEL

Car:
- id: integer
- brand: string
- model: string
- year: integer
- price: float

---

## 4. API CONTRACT

GET    /api/cars/
POST   /api/cars/
GET    /api/cars/{id}/
PUT    /api/cars/{id}/
DELETE /api/cars/{id}/

---

## 5. GENERATED UI STRUCTURE

Factory MUST generate:

/src/cars/pages
- CarsListPage
- CarCreatePage
- CarEditPage

/src/cars/components
- CarTable
- CarForm
- DeleteModal

/src/cars/services
- carService.js

/src/cars/hooks
- useCars.js

---

## 6. UI REQUIREMENTS

- Full CRUD functionality
- Responsive layout
- Loading states
- Error states
- Optimistic UI updates
- No page reload required

---

## 7. VALIDATION SCENARIOS (FACTORY LOOP)

The build is INVALID unless ALL pass:

1. Create car → appears in list instantly
2. Edit car → persists after refresh
3. Delete car → removed immediately
4. API failure → shows error UI
5. Loading state visible on all API calls

---

## 8. ACCEPTANCE CRITERIA

✔ No console errors  
✔ All CRUD flows work  
✔ Matches API contract  
✔ No modifications outside /src/cars  
✔ All validation scenarios pass  

---

## 9. EXECUTION RULE

The frontend is NOT manually written.

It is generated via:
→ frontend_builder/builder.py

The builder MUST:
1. Parse this spec
2. Build modules
3. Write directly into /src/cars
4. Validate output
5. Retry until valid