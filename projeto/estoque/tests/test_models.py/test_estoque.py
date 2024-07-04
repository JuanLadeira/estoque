import pytest
from projeto.estoque.serializers.estoque_entrada_serializer import EstoqueEntradaPostSerializer

@pytest.mark.django_db
class TestEstoqueEntrada:
    def test_estoque_entrada(self, estoque_entrada_factory, estoque_itens_factory, produto_factory, user_factory):
        produto = produto_factory(estoque=0)
        produto_2 = produto_factory()
        funcionario = user_factory()
        dados_entrada = {
                    'nf': 1,
                    'movimento': 'e',
                    'funcionario': funcionario.pk,
                    'itens': [
                        {
                            'produto': produto.pk,
                            'quantidade': 1,
                        },
                        {
                            'produto': produto_2.pk,
                            'quantidade': 2,
                        }
                    
                    ]

                }

        # Usar o serializer
        estoque_entrada_serializer_class = EstoqueEntradaPostSerializer
        serializer = estoque_entrada_serializer_class(data=dados_entrada)
        assert serializer.is_valid()
        estoque_entrada = serializer.save()

        itens = estoque_entrada.estoque_itens.all()

        assert itens.count() == 2

        produto_1 = estoque_entrada.estoque_itens.first().produto
        item_1 = estoque_entrada.estoque_itens.first()
        # Verificar os resultados
        assert estoque_entrada.pk is not None
        assert estoque_entrada.nf == dados_entrada['nf']
        assert estoque_entrada.movimento == dados_entrada['movimento']
        assert estoque_entrada.estoque_itens.count() == 2
        assert item_1.quantidade == 1
        assert produto_1.pk == produto.pk
        assert produto_1.estoque == 1

