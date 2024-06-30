from django.contrib import admin

from projeto.estoque.models.proxys.estoque_entrada import EstoqueEntrada
from projeto.estoque.models.proxys.estoque_saida import EstoqueSaida
from projeto.estoque.models.estoque_itens_model import EstoqueItens
from projeto.estoque.models.protocolo_entrega_model import ProtocoloEntrega
from projeto.estoque.models.protocolo_entrega_itens_model import ProtocoloEntregaItens


class EstoqueItensInline(admin.TabularInline):
    model = EstoqueItens
    extra = 0


@admin.register(EstoqueEntrada)
class EstoqueEntradaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf', 'funcionario',)
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'


@admin.register(EstoqueSaida)
class EstoqueSaidaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf', 'funcionario',)
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'


class ProtocoloEntregaItensInline(admin.TabularInline):
    model = ProtocoloEntregaItens
    extra = 0


@admin.register(ProtocoloEntrega)
class ProtocoloEntregaAdmin(admin.ModelAdmin):
    inlines = (ProtocoloEntregaItensInline,)
    list_display = ('__str__', 'estoque_atualizado')
    list_filter = ('usuario',)
    date_hierarchy = 'created'
