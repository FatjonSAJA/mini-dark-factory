def generate_model(task):

    fields = []

    for field in task["fields"]:

        field_name = field["name"]
        field_type = field["type"]

        if field_type == "CharField":

            fields.append(
                f"    {field_name} = models.CharField(max_length=255)"
            )

        elif field_type == "IntegerField":

            fields.append(
                f"    {field_name} = models.IntegerField()"
            )

    return f"""
from django.db import models


class {task["name"]}(models.Model):

{chr(10).join(fields)}
"""


def generate_serializer(model_name):

    return f"""
from rest_framework import serializers

from .models import {model_name}


class {model_name}Serializer(serializers.ModelSerializer):

    class Meta:

        model = {model_name}

        fields = "__all__"
"""


def generate_viewset(model_name):

    return f"""
from rest_framework.viewsets import ModelViewSet

from .models import {model_name}
from .serializers import {model_name}Serializer


class {model_name}ViewSet(ModelViewSet):

    queryset = {model_name}.objects.all()

    serializer_class = {model_name}Serializer
"""


def generate_urls(model_name):

    return f"""
from rest_framework.routers import DefaultRouter

from .views import {model_name}ViewSet


router = DefaultRouter()

router.register(
    r"cars",
    {model_name}ViewSet
)

urlpatterns = router.urls
"""


def build_backend(tasks):

    generated = {}

    model_task = next(
        t for t in tasks
        if t["type"] == "model"
    )

    model_name = model_task["name"]

    generated["models.py"] = generate_model(
        model_task
    )

    generated["serializers.py"] = generate_serializer(
        model_name
    )

    generated["views.py"] = generate_viewset(
        model_name
    )

    generated["urls.py"] = generate_urls(
        model_name
    )

    return generated