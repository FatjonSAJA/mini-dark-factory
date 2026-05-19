
from rest_framework.viewsets import ModelViewSet

from .models import CarViewSet
from .serializers import CarViewSetSerializer


class CarViewSetViewSet(ModelViewSet):

    queryset = CarViewSet.objects.all()
    serializer_class = CarViewSetSerializer
