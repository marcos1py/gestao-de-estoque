import os
import django
import os
import django
import string
import timeit
from random import random, randint
from django.db import transaction
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

import string
import timeit
from random import choice, random, randint
from produto.models import Produto, Categoria
class ProdutoClass:
    @staticmethod
    def criar_produtos(produtos):
        Produto.objects.all().delete()
        produtos_criados = []

        with transaction.atomic():
            for produto_nome in produtos:
                ncm = ''.join(str(randint(0, 9)) for _ in range(8))
                preco = round(random() * randint(10, 50), 2)
                estoque = randint(10, 200)
                estoque_minimo = randint(0, 10)  # Defina um valor de estoque mínimo adequado
                data = "2023-10-05"  # Defina a data conforme necessário
                categoria = Categoria.objects.get(pk=randint(1, Categoria.objects.count()))  # Escolha uma categoria existente aleatoriamente
                produto = Produto(
                    produto=produto_nome,
                    ncm=ncm,
                    preco=preco,
                    estoque=estoque,
                    estoque_minimo=estoque_minimo,
                    data=data,
                    categoria=categoria
                )
                produto.save()
                produtos_criados.append(produto)

        return produtos_criados

produtos = (
    'Coca-Cola',
    'Budweiser',
    'Chardonnay',
    'Whiskey',
    'Sprite',
    'Heineken',
    'Merlot',
    'Vodka',
    'Agua',
    'Suco de uva',
)

tic = timeit.default_timer()

produtos_criados = ProdutoClass.criar_produtos(produtos)

toc = timeit.default_timer()
print(f'Tempo para criar {len(produtos_criados)} produtos: {toc - tic:.2f} segundos')
