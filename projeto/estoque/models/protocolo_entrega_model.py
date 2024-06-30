from django.contrib.auth.models import User
from django.db import models
from projeto.core.models import TimeStampedModel
from django.utils import timezone

class ProtocoloEntrega(TimeStampedModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estoque_atualizado = models.BooleanField(default=False)
    data_saida = models.DateTimeField('data de saída', blank=True, null=True)
    estoque_retornado = models.BooleanField(default=False)
    data_retorno = models.DateTimeField('data de retorno', blank=True, null=True)
    
    def __str__(self):
        return str(self.pk)

    def atualizar_estoque_saida(self):
        if not self.estoque_atualizado:
            for item in self.protocolo_entrega.all():
                item.produto.quantidade -= item.quantidade
                item.produto.save()
            self.estoque_atualizado = True
            self.data_saida = timezone.now()
            self.save()
    
    def atualizar_estoque_retorno(self):
        if not self.estoque_retornado:
            for item in self.protocolo_entrega.all():
                item.produto.quantidade += item.quantidade
                item.produto.save()
            self.estoque_retornado = True
            self.data_retorno = timezone.now()
            self.save()