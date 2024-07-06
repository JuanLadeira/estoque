from django.core.management.base import BaseCommand, CommandError
from projeto.produto.create_data import ProdutoClass, produtos

class Command(BaseCommand):
    help = 'Cria produtos no banco de dados'

    def add_arguments(self, parser):
        ...
        # Adicione argumentos opcionais ou posicionais se necessário
        # parser.add_argument('sample_arg', type=str, help='Descrição do argumento')

    def handle(self, *args, **options):
        # Lógica do comando
        # sample_arg = options['sample_arg']
        ProdutoClass.criar_produtos(produtos=produtos)
        self.stdout.write(self.style.SUCCESS(f'Produtos foram criados.'))
