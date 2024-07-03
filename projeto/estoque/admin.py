from django.contrib import admin
from django import forms

from projeto.estoque.models.proxys.estoque_entrada import EstoqueEntrada
from projeto.estoque.models.proxys.estoque_saida import EstoqueSaida
from projeto.estoque.models.estoque_itens_model import EstoqueItens
from projeto.estoque.models.protocolo_entrega_model import ProtocoloEntrega
from projeto.estoque.models.protocolo_entrega_itens_model import ProtocoloEntregaItens


class EstoqueItensInline(admin.TabularInline):
    model = EstoqueItens
    extra = 0
    readonly_fields = ('saldo',)


@admin.register(EstoqueEntrada)
class EstoqueEntradaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf', 'funcionario',)
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'

    def get_form(self, request, obj=None, **kwargs):
            form = super(EstoqueEntradaAdmin, self).get_form(request, obj, **kwargs)
            # Definir o valor padrão para o campo 'movimento' como 'entrada', por exemplo
            form.base_fields['movimento'].initial = 'e'
            # Para ocultar o campo 'movimento' do formulário
            if 'movimento' in form.base_fields:
                form.base_fields['movimento'].widget = forms.HiddenInput()
            return form

@admin.register(EstoqueSaida)
class EstoqueSaidaAdmin(admin.ModelAdmin):
    inlines = (EstoqueItensInline,)
    list_display = ('__str__', 'nf', 'funcionario',)
    search_fields = ('nf',)
    list_filter = ('funcionario',)
    date_hierarchy = 'created'

    def get_form(self, request, obj=None, **kwargs):
            form = super(EstoqueSaidaAdmin, self).get_form(request, obj, **kwargs)
            # Definir o valor padrão para o campo 'movimento' como 'entrada', por exemplo
            form.base_fields['movimento'].initial = 's'
            # Para ocultar o campo 'movimento' do formulário
            if 'movimento' in form.base_fields:
                form.base_fields['movimento'].widget = forms.HiddenInput()
            return form



class ProtocoloEntregaItensInline(admin.TabularInline):
    model = ProtocoloEntregaItens
    extra = 0


@admin.register(ProtocoloEntrega)
class ProtocoloEntregaAdmin(admin.ModelAdmin):
    inlines = (ProtocoloEntregaItensInline,)
    list_display = ('__str__', 'estoque_atualizado')
    list_filter = ('usuario',)
    date_hierarchy = 'created'
