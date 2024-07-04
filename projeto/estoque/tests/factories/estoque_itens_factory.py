
from factory import Faker, SubFactory, LazyFunction
from factory.django import DjangoModelFactory


from projeto.estoque.models.estoque_itens_model import EstoqueItens
from projeto.produto.tests.factories.produto_factory import ProdutoFactory
from projeto.core.tests.factories.user_factory import UserFactory

from django.utils import timezone


class EstoqueItensFactory(DjangoModelFactory):
    class Meta:
        model = EstoqueItens

    quantidade = Faker('random_int', min=1, max=999)
    produto = SubFactory(ProdutoFactory)
    saldo = 0 
