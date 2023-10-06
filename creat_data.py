import os
import django
import string
import timeit
from random import random, randint, choice
from django.db import transaction
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from produto.models import Produto, Categoria

class ProdutoClass:
    @staticmethod
    def criar_categorias(categorias):
        Categoria.objects.all().delete()
        categorias_criadas = []

        for categoria_nome in categorias:
            categoria = Categoria(categoria=categoria_nome)
            categoria.save()
            categorias_criadas.append(categoria)

        return categorias_criadas

    @staticmethod
    def criar_produtos(quantidade_produtos, categorias):
        Produto.objects.all().delete()
        produtos_criados = []

        with transaction.atomic():
            for i in range(quantidade_produtos):
                produto_nome = f"Produto {i + 1}"  # Nome do produto com número sequencial
                ncm = ''.join(str(randint(0, 9)) for _ in range(8))
                preco = round(random() * randint(10, 50), 2)
                estoque = randint(10, 200)
                estoque_minimo = randint(0, 10)
                data = "2023-10-05"
                categoria = choice(categorias)
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

categorias = (
    'Bebidas Alcoólicas',
    'Bebidas Não Alcoólicas',
    'Alimentos',
    'Eletrônicos',
    'Roupas',
)
quantidade_produtos = 30

tic = timeit.default_timer()

categorias_criadas = ProdutoClass.criar_categorias(categorias)
produtos_criados = ProdutoClass.criar_produtos(quantidade_produtos, categorias_criadas)

toc = timeit.default_timer()
print(f'Tempo para criar {len(produtos_criados)} produtos: {toc - tic:.2f} segundos')
