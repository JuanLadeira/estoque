from factory import Faker, SubFactory, LazyFunction, RelatedFactory
from factory.django import DjangoModelFactory


from projeto.estoque.models.estoque_model import Estoque
from projeto.core.tests.factories.user_factory import UserFactory

from django.utils import timezone


class EstoqueEntradaFactory(DjangoModelFactory):
    class Meta:
        model = Estoque

    funcionario = SubFactory(UserFactory)
    nf = Faker('random_int', min=1, max=999)
    movimento = 'e'
    processado = False
    data = Faker('date_time_this_month', before_now=True, after_now=False, tzinfo=timezone.get_current_timezone())
