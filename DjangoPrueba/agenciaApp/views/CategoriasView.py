from rest_framework import status,views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from agenciaApp.models.Categorias import Categorias
from agenciaApp.serializers.CategoriasSerializer import CategoriasSerializer



class CategoriasView(views.APIView):
    queryset = Categorias.objects.all()
    Categorias_class = CategoriasSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = CategoriasSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        '''
        List all the branch for given requested user
        '''
        categorias = Categorias.objects.all()
        serializer = CategoriasSerializer(categorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        '''
        Updates the branch item with given brach id if exists
        '''
        Categorias_instance = self.get_object(kwargs['pk'])
        if not Categorias_instance:
            return Response(
                {"res": "Object with branch id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
     
        serializer = CategoriasSerializer(instance =Categorias_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, *args, **kwargs):
        '''
        Deletes the branch item with given branch id if exists
        '''
        Categorias_instance = self.get_object(kwargs['pk'])
        if not Categorias_instance:
            return Response(
                {"res": "Object with branch id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        Categorias_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )