from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.hashers import make_password

from users.models import User
from users.api.serializers import UserSerializer

from urllib.request import urlopen
import json
from django.http.response import JsonResponse
import requests

# Librerias para API
from facebook_scraper import get_profile
from core.facebookSearchTool import facebookSearchTool
from core.instagramSearchTool import instagramSearchTool
from core.searchGoogle import searchGoogle

import json


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
    def get(self, request, id=0):
        url = "https://api.apis.net.pe/v1/dni?numero=" + str(id)
        response = requests.get(url)
        return Response(response.json())


class ServiceFacebookProfile(APIView):
    def get(self, request, idprofile=""):
        data = get_profile(idprofile)
        return Response(data)


class ServiceFacebookName(APIView):
    def get(self, request, name=""):
        # Facebook search
        fbtool = facebookSearchTool()
        accountsFb = fbtool.searchFacebook(name)

        count = 0
        arrayData = []

        for a in accountsFb:
            count += 1
            username = a[0]
            name = a[1]

            if "people" in username:
                stringdata = username
                data_split = stringdata.split("/")
                data = get_profile(data_split[2])
            else:
                data = get_profile(username)

            arrayData.append({
                'name': name,
                'username': username,
                'url_profile': "https://facebook.com/" + username,
                'profile_picture': data['profile_picture'] if data != '' and ('profile_picture' in data) else '',
                'formacion_academica': data['Formación académica'] if data != '' and ('Formación académica' in data) else '',
                'lugar_residencia': data['Lugares de residencia'] if data != '' and ('Lugares de residencia' in data) else '',
                'empleo': data['Empleo'] if data != '' and ('Empleo' in data) else '',
            })

        if count > 0:
            result = json.dumps(arrayData)
        return Response(result)


class ServiceInstagramName(APIView):
    def get(self, request, name):
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


class ServiceGoogleSearch(APIView):
    def get(self, request, keyword):
        url = "https://www.google.com/search?num=100&q=\\%s\\"
        url2 = "https://www.google.com/search?num=100&q=\\intitle:\"%s\"\\"
        requete = requests.get(url % (keyword))
        requete2 = requests.get(url2 % (keyword))
        result = searchGoogle(requete=requete, requete2=requete2)
        return Response(result)
