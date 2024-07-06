from rest_framework import serializers
from projeto.estoque.models.protocolo_entrega_itens_model import ProtocoloEntregaItens

class ProtocoloEntregaItensInlineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProtocoloEntregaItens

