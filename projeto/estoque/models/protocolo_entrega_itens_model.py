from django.db import models
from projeto.produto.models.produto_model import Produto
from projeto.estoque.models.protocolo_entrega_model import ProtocoloEntrega

class ProtocoloEntregaItens(models.Model):
    protocolo_entrega = models.ForeignKey(
        ProtocoloEntrega,
        on_delete=models.CASCADE,
        related_name='protocolo_entrega_itens'
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.protocolo_entrega.pk, self.produto)
