from django.contrib.auth.models import User
from django.db import models, transaction
from logging import getLogger
from projeto.estoque.models.estoque_model import Estoque
from projeto.estoque.models.proxys.estoque_entrada import EstoqueEntrada
from projeto.estoque.models.proxys.estoque_saida import EstoqueSaida

from projeto.core.models import TimeStampedModel
from django.db.models.signals import post_save
from django.dispatch import receiver

log = getLogger("django")
