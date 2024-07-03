from django.apps import AppConfig

from logging import getLogger

logger = getLogger("django")

class EstoqueConfig(AppConfig):
    name = 'projeto.estoque'
    default_auto_field = 'django.db.models.BigAutoField'

