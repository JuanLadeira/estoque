from django.db import transaction
from rest_framework import serializers

from projeto.estoque.models.proxys.estoque_entrada import EstoqueEntrada
from projeto.estoque.models.estoque_itens_model import EstoqueItens
from projeto.estoque.serializers.inlines.estoque_itens_inline_serializer import EstoqueItensInlineCreateSerializer, EstoqueItensInlineGetSerializer

class EstoqueEntradaGetSerializer(serializers.ModelSerializer):
    itens = EstoqueItensInlineGetSerializer(many=True, source="estoque_itens") 
    
    class Meta:
        fields = '__all__'
        model = EstoqueEntrada

class EstoqueEntradaPostSerializer(serializers.ModelSerializer):
    itens = EstoqueItensInlineCreateSerializer(many=True, source="estoque_itens")
   
    class Meta:
        exclude = ['movimento']
        model = EstoqueEntrada
    
    @transaction.atomic
    def create(self, validated_data):
        """
        Recebe os dados validados e cria uma entrada de estoque com os seus itens.
        Receives the validated data and creates a stock entry with its items.
        """
        itens_data = validated_data.pop('estoque_itens')
        validated_data['movimento'] = 'e'  # Definindo o movimento
        estoque_entrada = super().create(validated_data)
        
        EstoqueItens.objects.bulk_create([
            EstoqueItens(estoque=estoque_entrada, **item_data) for item_data in itens_data
        ])
        return estoque_entrada
    
    @transaction.atomic
    def update(self, instance, validated_data):
        """
        Recebe uma instância e os dados validados e atualiza uma entrada de estoque com os seus itens.
        Receives an instance and the validated data and updates a stock entry with its items.
        """
        itens_data = validated_data.pop('estoque_itens', [])

        # Atualiza a instância com os dados validados, exceto os itens aninhados
        instance = super().update(instance, validated_data)

        # Deleta os itens aninhados existentes e cria os novos
        instance.estoque_itens.all().delete()
        EstoqueItens.objects.bulk_create([
            EstoqueItens(estoque=instance, **item_data) for item_data in itens_data
        ])

        return instance
