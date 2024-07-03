from factory import Faker, SubFactory, LazyFunction
from factory.django import DjangoModelFactory


from projeto.estoque.models.estoque_model import Estoque
from django.utils import timezone

class EstoqueEntradaFactory(DjangoModelFactory):
    class Meta:
        model = Estoque

    funcionario = SubFactory('projeto.produto.tests.factories.produto_factory.ProdutoFactory')