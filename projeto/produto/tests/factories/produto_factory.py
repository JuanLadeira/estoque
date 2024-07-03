from factory import Faker, SubFactory, LazyFunction
from factory.django import DjangoModelFactory

from projeto.produto.tests.factories.categoria_factory import CategoriaFactory
from projeto.produto.models.produto_model import Produto
from django.utils import timezone

class ProdutoFactory(DjangoModelFactory):
    class Meta:
        model = Produto

    importado = Faker('boolean')
    ncm = Faker('numerify', text='########')
    produto = Faker('word')
    preco = Faker('random_number', digits=2)
    estoque = Faker('random_number', digits=2)
    estoque_minimo = Faker('random_number', digits=2)
    data = LazyFunction(timezone.now)

    categoria = SubFactory(CategoriaFactory)
    
