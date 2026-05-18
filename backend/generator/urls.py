from django.urls import path
from .views import GenerateApp

urlpatterns = [
    path("generate/", GenerateApp.as_view()),
]