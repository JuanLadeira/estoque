import django
from django.conf import settings
from factory import Faker
from factory.django import DjangoModelFactory


User = settings.AUTH_USER_MODEL


class UserFactory(DjangoModelFactory):
    username = Faker('user_name')
    password = Faker('password')
    is_superuser = False

    class Meta:
        model = User