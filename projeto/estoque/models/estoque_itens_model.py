from django.db import models, transaction


from projeto.produto.models.produto_model import Produto
from projeto.estoque.models.estoque_model import Estoque


class EstoqueItens(models.Model):
    estoque = models.ForeignKey(
        Estoque,
        on_delete=models.CASCADE,
        related_name='estoque_itens'
    )
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    saldo = models.PositiveIntegerField(blank=True)

    class Meta:
        ordering = ('pk',)

    def __str__(self):
        return '{} - {} - {}'.format(self.pk, self.estoque.pk, self.produto)

    @transaction.atomic
    def atualizar_saldo(self):
        # Atualiza o saldo do produto
        if self.estoque.movimento == 'e':
            saldo = self.produto.estoque + self.quantidade
        else:
            saldo = self.produto.estoque - self.quantidade
            if saldo < 0:
                raise ValueError(f"Não é possível realizar a saída de {self.produto.nome}. Saldo insuficiente.")
        return saldo

    def save(self, *args, **kwargs):
        # Atualiza o saldo do produto
        self.saldo = self.atualizar_saldo()
        self.produto.estoque = self.saldo
        self.produto.save()
        super(EstoqueItens, self).save(*args, **kwargs)