from rest_framework.response import Response
from rest_framework.views import APIView
from facebook_scraper import get_profile
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

class ServiciosApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]

# class ServiciosFacebook(APIView):
#     def get(self, request, idprofile=""):
#         data = get_profile(idprofile)
#         return Response(data)