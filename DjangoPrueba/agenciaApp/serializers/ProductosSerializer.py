from rest_framework import serializers
from agenciaApp.models.Productos import Productos

class ProductosSerializer(serializers.ModelSerializer):
   class Meta:
       model = Productos
       fields = ['id', 'nombre','descripción','precio','foto','cantidad','subcategoria'] 
    


