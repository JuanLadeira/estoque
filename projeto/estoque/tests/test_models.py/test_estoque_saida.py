import pytest
from projeto.estoque.serializers.estoque_saida_serializer import EstoqueSaidaPostSerializer
from projeto.estoque.exceptions import ProdutoSaldoInsuficienteError

@pytest.mark.django_db
class TestEstoquesaida:
    def test_estoque_saida(self, produto_factory, user_factory):
        produto = produto_factory(estoque=1)
        produto_2 = produto_factory(estoque=2)
        funcionario = user_factory()
        dados_saida = {
                    'nf': 1,
                    'movimento': 's',
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
        estoque_saida_serializer_class = EstoqueSaidaPostSerializer
        serializer = estoque_saida_serializer_class(data=dados_saida)
        assert serializer.is_valid()
        if serializer.is_valid():
            estoque_saida = serializer.save()
        produto_2.refresh_from_db()
        produto.refresh_from_db()

        itens = estoque_saida.estoque_itens.all()

        assert itens.count() == 2

        produto_1 = estoque_saida.estoque_itens.first().produto
        item_1 = estoque_saida.estoque_itens.first()
        # Verificar os resultados
        assert estoque_saida.pk is not None
        assert estoque_saida.nf == dados_saida['nf']
        assert estoque_saida.movimento == dados_saida['movimento']
        assert estoque_saida.estoque_itens.count() == 2
        assert item_1.quantidade == 1
        assert produto_1.pk == produto.pk
        assert produto_1.estoque == 0
        assert produto_2.estoque == 0


    def test_estoque_saida_produto_saldo_insuficiente_error(self, produto_factory, user_factory):
        produto = produto_factory(estoque=0)
        produto_2 = produto_factory(estoque=0)
        funcionario = user_factory()
        dados_saida = {
                    'nf': 1,
                    'movimento': 's',
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
        estoque_saida_serializer_class = EstoqueSaidaPostSerializer
        serializer = estoque_saida_serializer_class(data=dados_saida)
        assert serializer.is_valid()
        with pytest.raises(ProdutoSaldoInsuficienteError):
            if serializer.is_valid():
                serializer.save()
        
        assert produto.estoque == 0