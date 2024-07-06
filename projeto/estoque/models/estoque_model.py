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

    @transaction.atomic
    def processar(self):
        """
           Atualiza o estoque de acordo com o movimento. ou seja, entrada ou saída.
           Updates the stock according to the movement. that is, entry or exit.
        """
        log.info("Processando estoque METODO PROCESSAR DO MODEL")
        if not self.processado:
            log.info("chamando atualizar_estoque_entrada_ou_saida")
            self.atualizar_estoque_entrada_ou_saida()
            log.info("Chamando save do estoque")
            self.processado = True
            self.save()


    def atualizar_estoque_entrada_ou_saida(self):
        """
            Atualiza o estoque de acordo com a entrada ou saida, ou seja, incrementa ou decrementa o saldo dos produtos nessa entrada.
            Updates the stock according to the entry, that is, increments the balance of the products in this entry.
        """
        log.info("@atualizar_estoque_entrada_ou_saida - Atualizando estoque de acordo com a entrada ou saida")
        itens = self.estoque_itens.all()
        if not itens:
            log.info("@atualizar_estoque_entrada_ou_saida - Não há itens para atualizar")
        for item in itens:
            log.info(f"@atualizar_estoque_entrada_ou_saida - Atualizando saldo do produto {item.produto.produto}")
            saldo = item.produto.estoque
            log.info(f"Saldo atual do produto {item.produto.produto} é {saldo}")
            item.atualizar_saldo()
            saldo = item.produto.estoque
            log.info(f"Novo saldo do produto {item.produto.produto} é {saldo}")
            log.info(f"Produto {item.produto.produto} atualizado com sucesso")
        log.info("@atualizar_estoque_entrada_ou_saida - finalizando atualização do estoque ")