def build_backend(tasks):

    generated = {}

    for task in tasks:

        if task["type"] == "model":

            generated["models.py"] = f"""
from django.db import models

class {task['name']}(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
"""

        if task["type"] == "serializer":

            generated["serializers.py"] = f"""
from rest_framework import serializers
from .models import {task['name']}

class {task['name']}Serializer(serializers.ModelSerializer):

    class Meta:
        model = {task['name']}
        fields = "__all__"
"""

        if task["type"] == "viewset":

            generated["views.py"] = f"""
from rest_framework.viewsets import ModelViewSet

from .models import {task['name']}
from .serializers import {task['name']}Serializer


class {task['name']}ViewSet(ModelViewSet):

    queryset = {task['name']}.objects.all()
    serializer_class = {task['name']}Serializer
"""

    return generated