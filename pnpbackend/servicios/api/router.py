from rest_framework.routers import DefaultRouter
# from servicios.api.views import ServiciosApiViewSet,ServiciosFacebook
from django.urls import path

router_servicios = DefaultRouter()

# router_servicios.register(
#     prefix='servicios', basename ='servicios', viewset = ServiciosApiViewSet
# )

# urlpatterns = [
#     path('auth/fb/<str:idprofile>/',ServiciosFacebook.as_view(),name='get_info_fb')
# ]