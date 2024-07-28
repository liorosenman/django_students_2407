from django.contrib import admin
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.index),
    path('login/', views.TokenObtainPairView.as_view, name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('get_all_images/', views.getImages),
    path('upload_image/', views.APIViews.as_view),
    path('get_students/', views.get_students),
    path('create_student/', views.create_student),
    path('upd_student/<int:id>/', views.update_student)
    # path('login/', views.login)

]
