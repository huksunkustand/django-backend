from rest_framework.routers import DefaultRouter
from escaneo.api.views import EscaneoApiViewsSet

router_escaneo = DefaultRouter()

router_escaneo.register(
    prefix='escaneo', basename ='escaneo', viewset = EscaneoApiViewsSet
)