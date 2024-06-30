from rest_framework import serializers
from projeto.estoque.models.protocolo_entrega_model import ProtocoloEntrega

class ProtocoloEntregaGetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProtocoloEntrega

class ProtocoloEntregaPostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = ProtocoloEntrega
