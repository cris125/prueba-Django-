"""Agencia_de_Viajes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from agenciaApp import views
urlpatterns = [
path('login/', TokenObtainPairView.as_view()),
path('refresh/', TokenRefreshView.as_view()),
path('user/', views.UserCreateView.as_view()),
path('user/<int:pk>/', views.UserDetailView.as_view()),
path('userCreate/', views.templates.singup,name='add'),
path('userlogin/', views.templates.login,name='login'),
path('user/home/', views.templates.loginHome,name='loginHome'),
path('Categoria/', views.CategoriasView.as_view()),
path('Categoria/<int:pk>/', views.CategoriasView.as_view()),
path('Subcategoria/', views.CategoriasView.as_view()),
path('Subcategoria/<int:pk>/', views.CategoriasView.as_view()),

path('Productos/', views.ProductosView.as_view()),
path('Productos/<int:pk>/', views.ProductosView.as_view()),

]
