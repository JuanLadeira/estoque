import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto.settings")
django.setup()

import string
import timeit
from random import choice, randint, random
from functools import wraps
from projeto.produto.models.produto_model import Produto

def cronometrize(func):
    def wrapper(*args, **kwargs):
        tic = timeit.default_timer()
        results = func(*args, **kwargs)
        toc = timeit.default_timer()
        print(f'Function {func.__name__} took {toc - tic} seconds to execute.')
        print(f'A função {func.__name__} levou {toc - tic } segundos ')
        return results
    return wrapper


class Utils:
    ''' Métodos genéricos. '''
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))


class ProdutoClass:

    @cronometrize
    @staticmethod
    def criar_produtos(produtos):
        Produto.objects.all().delete()
        aux = []
        for produto in produtos:
            data = dict(
                produto=produto,
                importado=choice((True, False)),
                ncm=Utils.gen_digits(8),
                preco=random() * randint(10, 50),
                estoque=randint(10, 200),
            )
            obj = Produto(**data)
            aux.append(obj)
        Produto.objects.bulk_create(aux)


produtos = (
    'Apontador',
    'Caderno 100 folhas',
    'Caderno capa dura 200 folhas',
    'Caneta esferográfica azul',
    'Caneta esferográfica preta',
    'Caneta esferográfica vermelha',
    'Durex',
    'Giz de cera 12 cores',
    'Lapiseira 0.3 mm',
    'Lapiseira 0.5 mm',
    'Lapiseira 0.7 mm',
    'Lápis de cor 24 cores',
    'Lápis',
    'Papel sulfite A4 pacote 100 folhas',
    'Pasta elástica',
    'Tesoura',
)



