from rest_framework import serializers
from projeto.estoque.models.estoque_itens_model import EstoqueItens

class EstoqueItensGetSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = EstoqueItens

class EstoqueItensPostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = EstoqueItens