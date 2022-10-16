from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from escaneo.models import Escaneo
from escaneo.api.serializers import EscaneoSerializer

class EscaneoApiViewsSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = EscaneoSerializer
    queryset = Escaneo.objects.all()