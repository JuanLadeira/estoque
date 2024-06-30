
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from projeto.estoque.models.proxys.estoque_saida import EstoqueSaida
from projeto.estoque.views.decorators.estoque_saida_decorators import (
    retrieve_estoque_saida_schema,
    create_estoque_saida_schema,
    list_estoque_saida_schema,
    update_estoque_saida_schema,
    partial_update_estoque_saida_schema,
    destroy_estoque_saida_schema,
    process_estoque_saida_schema
)

from projeto.estoque.serializers.estoque_saida_serializer import EstoqueSaidaGetSerializer, EstoqueSaidaPostSerializer

class EstoqueSaidaViewSet(viewsets.ModelViewSet):
    queryset = EstoqueSaida.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EstoqueSaidaGetSerializer
        return EstoqueSaidaPostSerializer

    @process_estoque_saida_schema
    @action(detail=True, methods=['post'])
    def processar(self, request, pk=None):
        """
        Process a stock out, this action will update the stock of the products.
        Processa uma saída de estoque, essa ação irá atualizar o estoque dos produtos.
        """
        estoque_saida = self.get_object()
        if estoque_saida.processado:
            return Response(
                {'detail': 'Saída no estoque já processado'},
                status=status.HTTP_400_BAD_REQUEST
            )
        estoque_saida.processar()
        return Response(
            {'detail': 'Saída no estoque processada com sucesso'},
            status=status.HTTP_200_OK
        )

    @retrieve_estoque_saida_schema
    def retrieve(self, request, *args, **kwargs):
        """
        Retrieve a stock out by id.
        Recupera uma saída de estoque pelo id.
        """
        return super().retrieve(request, *args, **kwargs)
    
    @list_estoque_saida_schema
    def list(self, request, *args, **kwargs):
        """
        List all stock outs or search for a estoque entry by product or 'nota fiscal' (nf)
        Lista todas as saídas de estoque ou busca uma saida de estoque por produto ou 'nota fiscal' (nf)
        """
        search = request.query_params.get('search', None)
        data_saida = request.query_params.get('data_saida', None)
        processado = request.query_params.get('processado', None)
        queryset = self.get_queryset()
        if processado:
            queryset = queryset.filter(processado=processado)
        if data_saida:
            queryset = queryset.filter(data=data_saida)
        if search:
            queryset = queryset.filter(
                Q(estoque_itens__produto__produto=search) | Q(nf=search)
            )
        serializer = EstoqueSaidaGetSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @create_estoque_saida_schema
    def create(self, request, *args, **kwargs):
        """
        Create a stock out.
        Cria uma saída de estoque.
        """
        return super().create(request, *args, **kwargs)

    @update_estoque_saida_schema
    def update(self, request, *args, **kwargs):
        """
        Update a stock out, only works if the stock entry is not processed.
        Atualiza uma saída de estoque, só funciona se a saida de estoque não estiver sido processada.
        """
        if self.get_object().processado:
            return Response(
                {'detail': 'Saída do Estoque já processada, não pode ser alterada'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().update(request, *args, **kwargs)

    @partial_update_estoque_saida_schema
    def partial_update(self, request, *args, **kwargs):
        """
        Partial update a stock out, only works if the stock entry is not processed.
        Atualiza parcialmente uma saída de estoque, só funciona se a saída de estoque não estiver sido processada.
        """
        if self.get_object().processado:
            return Response(
                {'detail': 'Saída de estoque já processada, não pode ser alterada'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().partial_update(request, *args, **kwargs)

    @destroy_estoque_saida_schema
    def destroy(self, request, *args, **kwargs):
        """
        Destroy a stock entry, only works if the stock entry is not processed.
        Destroi uma saida de estoque, só funciona se a saida de estoque não estiver sido process
        """
        if self.get_object().processado:
            return Response(
                {'detail': 'Saída de estoque já processada, não pode ser excluída'},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().destroy(request, *args, **kwargs)
