from rest_framework import serializers
from agenciaApp.models.Subcategorias import Subcategorias

class SubcategoriasSerializer(serializers.ModelSerializer):
   class Meta:
       model = Subcategorias
       fields = ['id', 'nombre','nombreCategoria','descripción'] 
    

