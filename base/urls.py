from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('', views.index),
    path('login/', views.TokenObtainPairView.as_view, name='token_obtain_pair'),
    path('get_all_images', views.getImages),
    path('upload_image/', views.APIViews.as_view),
    # path('get_products/', views.myProducts )
]
