import django
import pytest
from django.test import Client
from django.conf import settings
from pytest_factoryboy import register
from rest_framework.test import APIClient
from factory import Faker
from factory.django import DjangoModelFactory


from projeto.produto.tests.factories.produto_factory import ProdutoFactory
from projeto.produto.tests.factories.categoria_factory import CategoriaFactory

django.setup()


from logging import getLogger


User = settings.AUTH_USER_MODEL
logger = getLogger("django")


class UserFactory(DjangoModelFactory):
    username = Faker('user_name')
    password = Faker('password')
    is_superuser = False

    class Meta:
        model = User


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