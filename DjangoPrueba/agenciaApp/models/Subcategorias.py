from django.db import models

from .Categorias import Categorias

class Subcategorias(models.Model):
    id = models.AutoField(primary_key=True)
    nombreCategoria =  models.ForeignKey(Categorias, on_delete=models.CASCADE)
    nombre = models.CharField('subcategoria', max_length=50)
    descripción = models.CharField('descripción', max_length=50)



