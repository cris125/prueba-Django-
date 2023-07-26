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
"""path('login/', views.CustomTokenObtainPairView.as_view(), name='login'),"""
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from agenciaApp import views
urlpatterns = [


path('login/', views.CustomTokenObtainPairView.as_view(), name='login'),
path('refresh/', TokenRefreshView.as_view()),
path('user/', views.UserCreateView.as_view()),
path('user/<int:pk>/', views.UserDetailView.as_view()),
path('userCreate/', views.templates.singup,name='add'),
path('', views.templates.singup,name='add'),
path('userlogin/', views.templates.login,name='loginn'),
path('user/home/', views.templates.loginHome,name='pagina_administracion_usuario'),

path('Categoria/', views.CategoriasView.as_view(),name='Categoria'),
path('CategoriaPut/<int:pk>/', views.CategoriaView2.edicionP),
path('CategoriaPutGuardar/<int:pk>/', views.CategoriaView2.editarP),
path('CategoriaDelete/<int:pk>/', views.CategoriaView2.delete),
path('EditCategoria/', views.CategoriaView2.categoria),

path('Subcategoria/', views.SubcategoriasView.as_view()),
path('Subcategoria/<int:pk>/', views.CategoriasView.as_view()),
path('SubcategoriaiaPut/<int:pk>/', views.SubcategoriasView2.edicionP),
path('SubcategoriaPutGuardar/<int:pk>/', views.SubcategoriasView2.editarP),
path('SubcategoriaDelete/<int:pk>/', views.SubcategoriasView2.delete),
path('EditSubcategoria/', views.SubcategoriasView2.categoria),

path('Productos/', views.ProductosView.as_view()),
path('Productos/<int:pk>/', views.ProductosView.as_view()),
path('ProductosPut/<int:pk>/', views.ProductosView2.edicionP),
path('ProductosPutGuardar/<int:pk>/', views.ProductosView2.editarP),
path('ProductosDelete/<int:pk>/', views.ProductosView2.delete),
path('EditProductos/', views.ProductosView2.categoria),


]
