from rest_framework import serializers
from projeto.produto.models.produto_model import Produto
from projeto.produto.models.categoria_model import Categoria
from projeto.produto.serializers.inlines.categoria_inline_serializer import CategoriaInlineSerializer

class ProdutoGetSerializer(serializers.ModelSerializer):
    categoria = CategoriaInlineSerializer()

    class Meta:
        fields = '__all__'
        model = Produto


class ProdutoPostSerializer(serializers.ModelSerializer):
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())

    class Meta:
        fields = '__all__'
        model = Produto