from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response

from projeto.produto.models.categoria_model import Categoria
from projeto.produto.views.decorators.categoria_decorators import create_categoria_schema, list_categoria_schema, retrieve_categoria_schema,destroy_categoria_schema, partial_update_categoria_schema, update_categoria_schema
from projeto.produto.serializers.categoria_serializer import CategoriaGetSerializer, CategoriaPostSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    lookup_field = 'slug'
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CategoriaGetSerializer
        return CategoriaPostSerializer

    @retrieve_categoria_schema
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @list_categoria_schema
    def list(self, request, *args, **kwargs):
        search = request.query_params.get('search', None)
        if search:
            queryset = Categoria.objects.filter(
                Q(categoria__icontains=search) 
            )
        else:
            queryset = Categoria.objects.all()
        serializer = CategoriaGetSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @create_categoria_schema
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @update_categoria_schema
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @partial_update_categoria_schema
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @destroy_categoria_schema
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
