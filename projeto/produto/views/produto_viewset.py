
from produto.models.produto_model import Produto
from rest_framework import viewsets, status
from rest_framework.response import Response

from django.db.models import Q

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


from produto.serializers.produto_serializer import ProdutoGetSerializer, ProdutoPostSerializer

@extend_schema(tags=["Produto"])
class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ProdutoGetSerializer
        return ProdutoPostSerializer

    @extend_schema(
        description="List all products or search for a product by name, description or category",
        parameters=[
            OpenApiParameter(
                name="search",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="Search for a product by name, description or category",
                examples=[
                    OpenApiExample(
                        name="Search by name",
                        value="name",
                    ),
                    OpenApiExample(
                        name="Search by description",
                        value="description",
                    ),
                    OpenApiExample(
                        name="Search by category",
                        value="category",
                    ),
                ],
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        search = request.query_params.get('search', None)
        if search:
            queryset = Produto.objects.filter(
                Q(produto__icontains=search) | Q(categoria__categoria__icontains=search)
            )
        else:
            queryset = Produto.objects.all()
        serializer = ProdutoGetSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    @extend_schema(
        description="Create a new product",
        request=ProdutoPostSerializer,
        responses={200: ProdutoGetSerializer},
    )
    def create(self, request, *args, **kwargs):
        serializer = ProdutoPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @extend_schema(
        description="Update a product",
        request=ProdutoPostSerializer,
        responses={200: ProdutoPostSerializer},
    )
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ProdutoPostSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @extend_schema(
        description="Delete a product",
        responses={204: None}
    )   
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)