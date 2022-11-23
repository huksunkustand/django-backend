
import pandas as pd
import json
import requests

from xml.dom import NotFoundErr
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.hashers import make_password
from users.models import User
from users.api.serializers import UserSerializer
from urllib.request import urlopen
from django.http.response import JsonResponse

# Librerias para API
from facebook_scraper import get_profile
from core.facebookSearchTool import facebookSearchTool
from core.instagramSearchTool import instagramSearchTool
from core.searchGoogle import searchGoogle
from core.UPCAnalisisPost import getAnalisisPost
from core.UPCAnalisisFoto import getAnalisisFotos
from core.UPCAnalisisPerfilFB import getAnalisisPerfilSelenium
from core.UPCAnalisisPostTwitter import getAnalisisPostTwitter
from core.UPCAnalisisGoogle import getAnalisisGoogle
from core.UPCAnalisisPublicacionesFB import getAnalisisPublicacionesFBSelenium
from core.UPCAnalisisInstagramPerfilSelenium import getAnalisisInstagramPerfilSelenium
from core.UPCAnalisisInstagramPublicacionesSelenium import getAnalisisInstagramPublicacionesSelenium

class UserApiViewSet(ModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']
        if password:
            request.data['password'] = make_password(password)
        else:
            request.data['password'] = request.user.password
        return super().update(request, *args, **kwargs)

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class DemoView(APIView):
    def get(self, request, id=''):
        try:
            url = "https://api.apis.net.pe/v1/dni?numero=" + str(id)
            response = requests.get(url)
            # print(response.json())
            return Response(response.json())
        except:
            NotFound = {
                "nombres": "",
                "error": "DNI No encontrado"
            }
            return Response(NotFound)

class ServiceFacebookProfile(APIView):
    def get(self, request, idprofile=""):
        try:
            data = get_profile(idprofile)
            return Response(data)
        except:
            NotFound = {
                "service": "ServiceFacebookProfile",
                "error": "Servicio no disponible"
            }
            return Response(NotFound)

class ServiceInstagramName(APIView):
    def get(self, request, name):
        try:
            instatls = instagramSearchTool()
            instatls.searchInsta(name)
            accounts = instatls.accounts
            arrayData = []
            count = 0
            for account in accounts:
                url = "https://instagram.com/"+account
                response = instatls.getInfoInstagram(account)
                arrayData.append({
                'name': name, 
                'url_profile': url,
                'profile_picture_ins': response['data']['user']['profile_pic_url'] if response != '' and ('profile_pic_url' in response['data']['user']) else '',
                'id': response['data']['user']['id'] if response != '' and ('id' in response['data']['user']) else '',
                'full_name': response['data']['user']['full_name'] if response != '' and ('full_name' in response['data']['user']) else '',
                'biography': response['data']['user']['biography'] if response != '' and ('biography' in response['data']['user']) else '',
                'edge_follow': response['data']['user']['edge_follow']['count'] if response != '' and ('edge_follow' in response['data']['user']) else '',
                'edge_followed_by': response['data']['user']['edge_followed_by']['count'] if response != '' and ('edge_followed_by' in response['data']['user']) else '',
                'is_private': response['data']['user']['is_private'] if response != '' and ('is_private' in response['data']['user']) else '',
                })
            count += 1

            if count > 0:
                data = json.dumps(arrayData)
            return Response(data)
        except:
            NotFound = {
                "service": "ServiceInstagramName",
                "error": "Servicio no disponible"
            }
            return Response(NotFound)

class ServiceGoogleSearch(APIView):
    def get(self, request, keyword):
        try:
            url = "https://www.google.com/search?num=100&q=\\%s\\"
            url2 = "https://www.google.com/search?num=100&q=\\intitle:\"%s\"\\"
            requete = requests.get(url % (keyword))
            requete2 = requests.get(url2 % (keyword))
            result = searchGoogle(requete=requete, requete2=requete2)
            return Response(result)
        except:
            NotFound = {
                "service": "ServiceGoogleSearch",
                "error": "Servicio no disponible"
            }
            return Response(NotFound)

class ServiceFacebookLocal(APIView):
    def get(self, request, name):
        try:
            arrayData = []
            data = pd.read_table("D:\PNP\pnp_django\pnpbackend\core\dataFacebook.txt", delimiter=":", header=None, low_memory=False, na_filter=False)
            for cols in data.values: 
                    NombresCompletos = str(str(cols[2]) +" "+ str(cols[3]))
                    if name.lower() in NombresCompletos.lower():
                        arrayData.append({
                                        'Celular': cols[0],
                                        'Identificador': cols[1],
                                        'Nombres': cols[2],
                                        'Apellidos': cols[3],
                                        'Sexo': cols[4],
                                        'Distrito': cols[5],
                                        'Pais': cols[6],
                                        'Estado': cols[7],
                                        'Trabajo': cols[8],
                                        'Dato9': cols[9],
                                        'Dato10': cols[10],
                                        'Dato11': cols[11],
                                        'Correo': cols[12],
                                        'FechaNacimiento': cols[13],
                                    })
            result = json.dumps(arrayData)
            return Response(result)
        except:
            NotFound = {
                "service": "ServiceFacebookLocal",
                "error": "Servicio no disponible"
            }
            return Response(NotFound)

class ServiceSelenium(APIView):
    def get(self, request, profile=''):
        try:
            data = getAnalisisPost(None,profile)
            result = json.dumps(data)
            return Response(result)
        except:
            NotFound = {
                "service": "ServiceSelenium",
                "error": "Servicio ServiceSelenium no disponible"
            }
            return Response(NotFound)

class ServiceAnalisiFoto(APIView):
    def get(self, request, profile=''):
        try:
            print('Ingreso x1')
            dataFoto = getAnalisisFotos(None,profile)
            print('Ingreso x2')
            result = json.dumps(dataFoto)
            print('result:',result)
            return Response(result)
        except:
            NotFound = {
                "service": "ServiceAnalisiFoto",
                "error": "Servicio ServiceAnalisiFoto no disponible"
            }
            return Response(NotFound)

class ServiceAnalisiPerfilSelenium(APIView):
    def get(self, request, nombres=''):
        try:
            # print('Ingreso 1')
            data = getAnalisisPerfilSelenium(None,nombres)
            # print('data:',data)
            result = json.dumps(data)
            return Response(result)
        except:
            NotFound = {
                "service": "ServiceAnalisiPerfilSelenium",
                "error": "Servicio ServiceAnalisiPerfilSelenium no disponible"
            }
            return Response(NotFound)

class ServiceAnalisiPostTwitterSelenium(APIView):
    def get(self, request, nombres=''):
        try:
            print('Ingreso 1')
            data = getAnalisisPostTwitter(None,nombres)
            print('data:',data)
            result = json.dumps(data)
            return Response(result)
        except:
            NotFound = {
                "service": "ServiceAnalisiPostTwitterSelenium",
                "error": "Servicio ServiceAnalisiPostTwitterSelenium no disponible"
            }
            return Response(NotFound)

class ServiceAnalisiGoogleSelenium(APIView):
    def get(self, request, nombres=''):
        try:
            data = getAnalisisGoogle(None,nombres)
            result = json.dumps(data)
            return Response(result)
        except:
            NotFound = {
                "service": "ServiceAnalisiGoogleSelenium",
                "error": "Servicio ServiceAnalisiGoogleSelenium no disponible"
            }
            return Response(NotFound)

class ServiceAnalisisPublicacioneFBSelenium(APIView):
    def get(self, request, nombres='',profileId=''):
        try:
            data = getAnalisisPublicacionesFBSelenium(None,nombres,profileId)
            result = json.dumps(data)
            return Response(result)
        except:
            NotFound = {
                "service": "ServiceAnalisisPublicacioneFBSelenium",
                "error": "Servicio ServiceAnalisisPublicacioneFBSelenium no disponible"
            }
            return Response(NotFound)

class ServiceAnalisisInstagramPerfilSelenium(APIView):
    def get(self, request, name=''):
        try:
            data = getAnalisisInstagramPerfilSelenium(None,name)
            result = json.dumps(data)
            return Response(result)
        except:
            NotFound = {
                "service": "ServiceAnalisisInstagramPerfilSelenium",
                "error": "Servicio ServiceAnalisisInstagramPerfilSelenium no disponible"
            }
            return Response(NotFound)

class ServiceAnalisisInstagramPublicacionesSelenium(APIView):
    def get(self, request, profile=''):
        try:
            data = getAnalisisInstagramPublicacionesSelenium(None,profile)
            result = json.dumps(data)
            return Response(result)
        except:
            NotFound = {
                "service": "ServiceAnalisisInstagramPublicacionesSelenium",
                "error": "Servicio ServiceAnalisisInstagramPublicacionesSelenium no disponible"
            }
            return Response(NotFound)