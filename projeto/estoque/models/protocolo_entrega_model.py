from django.conf import settings
from django.db import models, transaction
from projeto.core.models import TimeStampedModel
from projeto.estoque.models.estoque_itens_model import EstoqueItens
from projeto.estoque.models.proxys.estoque_saida import EstoqueSaida
from projeto.estoque.exceptions import ProtocoloProcessadoError

User = settings.AUTH_USER_MODEL

class ProtocoloEntrega(TimeStampedModel):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    estoque_atualizado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'protocolo de entrega'
        verbose_name_plural = 'protocolos de entrega'

    def __str__(self):
        return str(self.pk)

    def processar_protocolo(self, usuario: User):
        if self.estoque_atualizado:
            raise ProtocoloProcessadoError()
        
        with transaction.atomic():
            # Criar um EstoqueSaida
            estoque_saida = EstoqueSaida.objects.create(
                funcionario=usuario,
                movimento='s'
            )
            for item in self.protocolo_entrega_itens.all():
                # Criar um Estoque Saida Detail
                EstoqueItens.objects.create(
                    estoque=estoque_saida,
                    produto=item.produto,
                    quantidade=item.quantidade,
                    saldo=item.produto.estoque - item.quantidade
                )
                # Atualizar o estoque do produto
                item.produto.estoque -= item.quantidade
                item.produto.save()
            #Processando a saida.
            estoque_saida.processar()
            
            self.estoque_atualizado = True
            self.save()
    
 