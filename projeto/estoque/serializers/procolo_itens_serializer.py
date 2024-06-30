from rest_framework import serializers
from projeto.estoque.models.protocolo_entrega_itens_model import ProtocoloEntregaItens

class ProtocoloEntregaItensGetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProtocoloEntregaItens

class ProtocoloEntregaItensPostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProtocoloEntregaItens
