import pytest


@pytest.mark.django_db
class TestEstoqueEntrada:
    def test_estoque_entrada(self, estoque_entrada_factory, estoque_itens_factory, produto_factory):

        produto = produto_factory()
        estoque_entrada = estoque_entrada_factory().build()
        estoque_itens_factory(produto=produto, estoque_entrada=estoque_entrada).build()
        assert estoque_entrada.pk == 1
        assert estoque_entrada.funcionario.pk == 1
        assert estoque_entrada.nf == 1
        assert estoque_entrada.movimento == 'e'
        assert estoque_entrada.processado is False
        assert estoque_entrada.data is not None
        assert estoque_entrada.estoque_itens.count() == 1
        assert estoque_entrada.estoque_itens.first().quantidade == 1
        assert estoque_entrada.estoque_itens.first().produto.pk == 1


