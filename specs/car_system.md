name: Car System

backend:
  - model: Car
  - serializer: Car
  - viewset: CarViewSet

frontend:
  - component: CarTable
  - component: CarForm

tests:
  - api_health
  - create_car