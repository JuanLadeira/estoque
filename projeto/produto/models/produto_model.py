from django.db import models
from django.urls import reverse_lazy
from projeto.produto.models.categoria_model import Categoria
from django_extensions.db.models import AutoSlugField

class Produto(models.Model):
    importado = models.BooleanField(default=False)
    ncm = models.CharField('NCM', max_length=8)
    produto = models.CharField(max_length=100, unique=True)
    slug = AutoSlugField(populate_from='produto', unique=True)
    preco = models.DecimalField('preço', max_digits=7, decimal_places=2)
    estoque = models.IntegerField('estoque atual')
    estoque_minimo = models.PositiveIntegerField('estoque mínimo', default=0)
    data = models.DateField(null=True, blank=True)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='produtos'
    )

    class Meta:
        ordering = ('produto',)

    def __str__(self):
        return self.produto

    def to_dict_json(self):
        return {
            'pk': self.pk,
            'produto': self.produto,
            'estoque': self.estoque,
        }

