from projeto.estoque.managers.estoque_entrada_manager import EstoqueEntradaManager
from projeto.estoque.models.estoque_model import Estoque

class EstoqueEntrada(Estoque):
    objects = EstoqueEntradaManager()

    class Meta:
        proxy = True
        verbose_name = 'estoque entrada'
        verbose_name_plural = 'estoque entrada'
