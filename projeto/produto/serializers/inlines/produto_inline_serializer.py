from rest_framework import serializers
from projeto.produto.models.produto_model import Produto

class ProdutosInlineSerializer(serializers.ModelSerializer):
    class Meta:
        fields = [
            "pk",
            "importado",
            "ncm",
            "produto",
            "preco",
            "estoque",
            "estoque_minimo",
            "data",
        ]
        model = Produto

