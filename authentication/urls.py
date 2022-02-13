from django.urls import path
from . import views as auth_view

urlpatterns = [

    path('token', auth_view.ObtainTokenPairWithColorView.as_view(),
         name='token_create'),  # override sjwt stock token

]
