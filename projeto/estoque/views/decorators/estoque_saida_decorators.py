from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from projeto.estoque.serializers.estoque_saida_serializer import EstoqueSaidaGetSerializer, EstoqueSaidaPostSerializer

def create_estoque_saida_schema(view_func):
    decorator = extend_schema(
        tags=["Estoque - Saida"],
        summary="Create a stock out",
        description="Create a new stock out",
        request=EstoqueSaidaPostSerializer,
        responses={200: EstoqueSaidaPostSerializer},
    )
    return decorator(view_func)

def update_estoque_saida_schema(view_func):
    decorator = extend_schema(
        tags=["Estoque - Saida"],
        summary="Update a stock out",
        description="Update a stock out",
        request=EstoqueSaidaPostSerializer,
        responses={
            200: EstoqueSaidaPostSerializer,
            400: {"detail": "Estoque já processado, não pode ser alterado"},
            },
    )
    return decorator(view_func)

def partial_update_estoque_saida_schema(view_func):
    decorator = extend_schema(
        tags=["Estoque - Saida"],
        summary="Partial update a stock out",
        description="Partial update a estock out",
        request=EstoqueSaidaPostSerializer,
        responses={
            200: EstoqueSaidaPostSerializer,
            400: {"detail": "Estoque já processado, não pode ser alterado"},
        },
    )
    return decorator(view_func)

def retrieve_estoque_saida_schema(view_func):
    decorator = extend_schema(
        tags=["Estoque - Saida"],
        summary="Retrieve a estock out",
        description="Retrieve a stock by id",
        responses={
            200: EstoqueSaidaGetSerializer,
            404: {"detail": "Estoque não encontrado"},
        },
    )
    return decorator(view_func)

def list_estoque_saida_schema(view_func):
    decorator =  extend_schema(
        tags=["Estoque - Saida"],
        summary="List Estoques or search for a stock out by produto",
        description="List all stock entries or search for a stock out by produto",
        parameters=[
            OpenApiParameter(
                name="search",
                type=OpenApiTypes.STR,
                location=OpenApiParameter.QUERY,
                description="List or Search for a estoque out by produto or 'nota fiscal' (nf)",
                examples=[
                    OpenApiExample(
                        name="""
                        Search by a product name or 'nota fiscal' (nf)
                        Buscar saida de estoque por um nome de produto ou 'nota fiscal' (nf)
                        """,
                        value="name",
                    ),
                ],
            ),
            OpenApiParameter(
                name="data_saida",
                type=OpenApiTypes.DATE,
                location=OpenApiParameter.QUERY,
                description="""
                Filter by out date
                Filtrar por data de saida
                """,
            ),
            OpenApiParameter(
                name="processado",
                type=OpenApiTypes.BOOL,
                location=OpenApiParameter.QUERY,
                description="""
                Filter by processed status.
                True: Processed
                False: Not processed
                
                Filtrar por status de processamento.
                True: Processado
                False: Não processado     
                """,
            )
        ],
    )
    return decorator(view_func)


def destroy_estoque_saida_schema(view_func):
    decorator = extend_schema(
        tags=["Estoque - Saida"],
        summary="Delete an stock output",
        description="Delete a Estoque by id",
        responses={ 204: None,
                    404: {"detail": "Saida de Estoque não encontrada"},
                    400: {"detail": "Saida de Estoque já processada, não pode ser deletada"}, 
                   },
    )
    return decorator(view_func)