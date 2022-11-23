from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
   
from users.api.views import UserApiViewSet, UserView,DemoView,ServiceFacebookProfile,ServiceInstagramName,ServiceGoogleSearch,ServiceFacebookLocal,ServiceSelenium,ServiceAnalisiFoto,ServiceAnalisiPerfilSelenium,ServiceAnalisiPostTwitterSelenium,ServiceAnalisiGoogleSelenium,ServiceAnalisisPublicacioneFBSelenium,ServiceAnalisisInstagramPerfilSelenium,ServiceAnalisisInstagramPublicacionesSelenium

router_user = DefaultRouter()

router_user.register(
    prefix = 'users', basename='users', viewset = UserApiViewSet
)

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/me/',UserView.as_view()),
    path('auth/dni/<str:id>/',DemoView.as_view(),name='get_dni'),
    path('auth/fb/<str:idprofile>/',ServiceFacebookProfile.as_view(),name='get_info_fb'),
    # path('auth/searchname/<str:name>/',ServiceFacebookName.as_view(),name='get_facebook_search'),
    path('auth/searchnameinstagram/<str:name>/',ServiceInstagramName.as_view(),name='get_instagram_search'),
    path('auth/searchgoogle/<str:keyword>/',ServiceGoogleSearch.as_view(),name='get_google_search'),
    path('auth/searchFacebookLocal/<str:name>/',ServiceFacebookLocal.as_view(),name='get_facebook_local_search'),
    path('auth/searchKeyWorkFacebook/<str:profile>/',ServiceSelenium.as_view(),name='get_comment_facebook_sel'),
    path('auth/analisisFotos/<str:profile>/',ServiceAnalisiFoto.as_view(),name='get_photo_analysis'),
    path('auth/analisisPerfilSelenium/<str:nombres>/',ServiceAnalisiPerfilSelenium.as_view(),name='get_perfil_facebook_selenium'),
    path('auth/analisisPostTwitter/<str:nombres>/',ServiceAnalisiPostTwitterSelenium.as_view(),name='get_post_twitter_selenium'),
    path('auth/analisisGoogleSelenium/<str:nombres>/',ServiceAnalisiGoogleSelenium.as_view(),name='get_analysis_google_selenium'),
    path('auth/analisisPublicacionesFBSelenium/<str:nombres>/<str:profileId>/',ServiceAnalisisPublicacioneFBSelenium.as_view(),name='get_analysis_Publicaciones_fb_selenium'),
    path('auth/analisisInstagramPerfilSelenium/<str:name>/',ServiceAnalisisInstagramPerfilSelenium.as_view(),name='get_analysis_instagram_perfil_selenium'),
    path('auth/analisisInstagramPublicacionesSelenium/<str:profile>/',ServiceAnalisisInstagramPublicacionesSelenium.as_view(),name='get_analysis_instagram_publicaciones_selenium'),

]
