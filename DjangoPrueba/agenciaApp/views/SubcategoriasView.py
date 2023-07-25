from rest_framework import status,views
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from agenciaApp.models.Subcategorias import Subcategorias
from agenciaApp.serializers.subcategoriasSerializer import SubcategoriasSerializer


class SubcategoriasView(views.APIView):
    queryset = Subcategorias.objects.all()
    Subcategorias_class = Subcategorias
    
    def post(self, request, *args, **kwargs):
        serializer = Subcategorias(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, *args, **kwargs):
        '''
        List all the branch for given requested user
        '''
        subcategorias = Subcategorias.objects.all()
        serializer = SubcategoriasSerializer(subcategorias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        '''
        Updates the branch item with given brach id if exists
        '''
        Subcategorias_instance = self.get_object(kwargs['pk'])
        if not Subcategorias_instance:
            return Response(
                {"res": "Object with branch id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
     
        serializer = SubcategoriasSerializer(instance =Subcategorias_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    def delete(self, request, *args, **kwargs):
        '''
        Deletes the branch item with given branch id if exists
        '''
        facturas_instance = self.get_object(kwargs['pk'])
        if not facturas_instance:
            return Response(
                {"res": "Object with branch id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        facturas_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )