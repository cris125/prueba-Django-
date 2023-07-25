from rest_framework import serializers
from agenciaApp.models.Categorias import Categorias

class CategoriasSerializer(serializers.ModelSerializer):
   class Meta:
       model = Categorias
       fields = ['id', 'nombre'] 
    


