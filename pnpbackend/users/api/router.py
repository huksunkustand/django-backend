from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
   
from users.api.views import UserApiViewSet, UserView,DemoView,ServiceFacebookProfile,ServiceFacebookName,ServiceInstagramName,ServiceGoogleSearch

router_user = DefaultRouter()

router_user.register(
    prefix = 'users', basename='users', viewset = UserApiViewSet
)

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/me/',UserView.as_view()),
    path('auth/dni/<int:id>/',DemoView.as_view(),name='get_dni'),
    path('auth/fb/<str:idprofile>/',ServiceFacebookProfile.as_view(),name='get_info_fb'),
    path('auth/searchname/<str:name>/',ServiceFacebookName.as_view(),name='get_facebook_search'),
    path('auth/searchnameinstagram/<str:name>/',ServiceInstagramName.as_view(),name='get_instagram_search'),
    path('auth/searchgoogle/<str:keyword>/',ServiceGoogleSearch.as_view(),name='get_google_search')
]