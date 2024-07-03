from django.contrib.auth.models import User
from django.db import models, transaction
from projeto.core.models import TimeStampedModel
from django.db.models.signals import post_save
from django.dispatch import receiver


MOVIMENTO = (
    ('e', 'entrada'),
    ('s', 'saida'),
)

from logging import getLogger
import logging
logging.basicConfig(level=logging.DEBUG)

log = logging.getLogger("test_logger")
log.debug("Isso é um teste de logging.")

class Estoque(TimeStampedModel):
    funcionario = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    nf = models.PositiveIntegerField('nota fiscal', null=True, blank=True)
    movimento = models.CharField(max_length=1, choices=MOVIMENTO, blank=True)
    processado = models.BooleanField(default=False)
    data = models.DateField('data', auto_now_add=True, help_text='Data do movimento')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        if self.nf:
            return '{} - {} - {}'.format(self.pk, self.nf, self.created.strftime('%d-%m-%Y'))
        return '{} --- {}'.format(self.pk, self.created.strftime('%d-%m-%Y'))

    def nf_formated(self):
        if self.nf:
            return str(self.nf).zfill(3)
        return '---'

#     @transaction.atomic
#     def processar(self):
#         """
#            Atualiza o estoque de acordo com o movimento. ou seja, entrada ou saída.
#            Updates the stock according to the movement. that is, entry or exit.
#         """
#         log.info("Processando estoque")
#         if not self.processado:
#             if self.movimento == 'e':
#                 self.atualizar_entrada()
#                 log.info("atualizei entrada")
#             elif self.movimento == 's':
#                 self.atualizar_saida()
#                 log.info("atualizei saida")
#             self.processado = True
#             self.save()

    
#     def atualizar_entrada(self):
#         """
#             Atualiza o estoque de acordo com a entrada, ou seja, incrementa o saldo dos produtos nessa entrada.
#             Updates the stock according to the entry, that is, increments the balance of the products in this entry.
#         """
#         for item in self.estoque_itens.all():
#             log.info(f"Produto {item.produto.nome} - {item.quantidade}")
#             item.produto.estoque += item.quantidade
#             item.saldo = item.produto.estoque
#             item.produto.save()
#             log.info(f"Produto {item.produto.nome} atualizado com sucesso")

#     def atualizar_saida(self):
#         """
#             Atualiza o estoque de acordo com a saída, ou seja, decrementa o saldo dos produtos nessa saída.
#             Updates the stock according to the exit, that is, decrements the balance of the products in this exit.
#         """
#         for item in self.estoque_itens.all():
#             novo_saldo = item.produto.estoque - item.quantidade
#             if novo_saldo < 0:
#                 # Trata o caso em que o saldo seria negativo.
#                 # Você pode lançar uma exceção ou retornar um erro.
#                 raise ValueError(f"Não é possível realizar a saída de {item.produto.nome}. Saldo insuficiente.")
#             item.produto.estoque = novo_saldo
#             item.saldo = novo_saldo
#             item.produto.save()
#             log.info(f"Produto {item.produto.nome} atualizado com sucesso")


# @receiver(post_save, sender=Estoque)
# def processar_estoque(sender, instance, created, **kwargs):
#     """
#     Signal para processar o estoque após salvar uma entrada ou saida de Estoque.
#     """
#     log.info("Processando estoque")
#     if created:
#         instance.processar()