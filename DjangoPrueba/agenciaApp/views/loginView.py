from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from django.shortcuts import render, redirect
from django.contrib import messages

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == status.HTTP_200_OK:
            return redirect('pagina_administracion_usuario') 
        else:
            messages.error(request, 'Contraseña incorrecta. Inténtalo de nuevo.')
            return redirect('pagina_administracion_usuario') 
        return response  # Asegúrate de devolver la respuesta en caso de que el código de estado no sea 200 o 401.
        