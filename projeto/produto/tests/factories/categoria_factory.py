from factory import Faker, SubFactory, LazyFunction
from factory.django import DjangoModelFactory

from projeto.produto.models.categoria_model import Categoria
from django.utils import timezone

class CategoriaFactory(DjangoModelFactory):
    class Meta:
        model = Categoria

    categoria = Faker('word')
