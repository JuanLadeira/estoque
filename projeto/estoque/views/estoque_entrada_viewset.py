
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from projeto.estoque.models.proxys.estoque_entrada import EstoqueEntrada
from projeto.estoque.views.decorators.estoque_entrada_decorators import (
    retrieve_estoque_entrada_schema,
    create_estoque_entrada_schema,
    list_estoque_entrada_schema,
    update_estoque_entrada_schema,
    partial_update_estoque_entrada_schema,
    destroy_estoque_entrada_schema,
    process_estoque_entrada_schema
)

from projeto.estoque.serializers.estoque_entrada_serializer import EstoqueEntradaGetSerializer, EstoqueEntradaPostSerializer

class EstoqueEntradaViewSet(viewsets.ModelViewSet):
    queryset = EstoqueEntrada.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EstoqueEntradaGetSerializer
        return EstoqueEntradaPostSerializer

    @process_estoque_entrada_schema
    @action(detail=True, methods=['post'])
    def processar(self, request, pk=None):
        """
        Process a stock entry, this action will update the stock of the products.
        Processa uma entrada de estoque, essa ação irá atualizar o estoque dos produtos.
        """
        estoque_entrada = self.get_object()
        if estoque_entrada.processado:
            return Response(
                {'detail': 'Entada no estoque já processado'},
                status=status.HTTP_400_BAD_REQUEST
            )
        estoque_entrada.processar()
        return Response(
            {'detail': 'Entrada no estoque processada com sucesso'},
            status=status.HTTP_200_OK
        )

    @retrieve_estoque_entrada_schema
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a stock entry by id.
        Recupera uma entrada de estoque pelo id.
        """
        return super().retrieve(request, *args, **kwargs)
    
    @list_estoque_entrada_schema
    def list(self, request, *args, **kwargs):
        """
        List all estoque entries or search for a estoque entry by product or 'nota fiscal' (nf)
        Lista todas as entradas de estoque ou busca uma entrada de estoque por produto ou 'nota fiscal' (nf)
        """
        search = request.query_params.get('search', None)
        data_entrada = request.query_params.get('data_entrada', None)
        processado = request.query_params.get('processado', None)
        queryset = self.get_queryset()
        if processado:
            queryset = queryset.filter(processado=processado)
        if data_entrada:
            queryset = queryset.filter(data=data_entrada)
        if search:
            queryset = queryset.filter(
                Q(estoque_itens__produto__produto=search) | Q(nf=search)
            )
        serializer = EstoqueEntradaGetSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @create_estoque_entrada_schema
    def create(self, request, *args, **kwargs):
        """
        Create a stock entry.
        Cria uma entrada de estoque.
        """
        return super().create(request, *args, **kwargs)

    @update_estoque_entrada_schema
    def update(self, request, *args, **kwargs):
        """
        Update a stock entry, only works if the stock entry is not processed.
        Atualiza uma entrada de estoque, só funciona se a entrada de estoque não estiver sido processada.
        """
        if self.get_object().processado:
            return Response(
                {'detail': 'Estoque já processado, não pode ser alterado'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().update(request, *args, **kwargs)

    @partial_update_estoque_entrada_schema
    def partial_update(self, request, *args, **kwargs):
        """
        Partial update a stock entry, only works if the stock entry is not processed.
        Atualiza parcialmente uma entrada de estoque, só funciona se a entrada de estoque não estiver sido processada.
        """
        if self.get_object().processado:
            return Response(
                {'detail': 'Estoque já processado, não pode ser alterado'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().partial_update(request, *args, **kwargs)

    @destroy_estoque_entrada_schema
    def destroy(self, request, *args, **kwargs):
        """
        Destroy a stock entry, only works if the stock entry is not processed.
        Destroi uma entrada de estoque, só funciona se a entrada de estoque não estiver sido process
        """
        if self.get_object().processado:
            return Response(
                {'detail': 'Estoque já processado, não pode ser excluído'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)
