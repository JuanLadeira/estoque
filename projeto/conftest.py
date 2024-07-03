import django
import pytest
from django.test import Client
from django.conf import settings
from pytest_factoryboy import register
from rest_framework.test import APIClient
from factory import Faker
from factory.django import DjangoModelFactory

from projeto.core.tests.factories.user_factory import UserFactory
from projeto.produto.tests.factories.produto_factory import ProdutoFactory
from projeto.produto.tests.factories.categoria_factory import CategoriaFactory
from projeto.estoque.tests.factories.estoque_entrada_factory import EstoqueEntradaFactory
from projeto.estoque.tests.factories.estoque_itens_factory import EstoqueItensFactory


django.setup()


from logging import getLogger


User = settings.AUTH_USER_MODEL
logger = getLogger("django")


@pytest.fixture
def admin_client():
    user = User.objects.create_superuser(
        username="admin", password="admin", email="admin@example.com"
    )
    client = Client()
    client.force_login(user)
    return client

@pytest.fixture
def api_client():
    return APIClient()


register(ProdutoFactory)
register(CategoriaFactory)
register(UserFactory)
register(EstoqueEntradaFactory)
register(EstoqueItensFactory)