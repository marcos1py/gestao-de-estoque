from django.shortcuts import render, redirect
from django.db.models import Max
from produto.models import Produto
from estoque.models import EstoqueItens
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from collections import Counter
from estoque.models import (
    Estoque,
    EstoqueEntrada,
    EstoqueItens,
    EstoqueSaida,
    ProtocoloEntrega
)
from django.shortcuts import render, get_object_or_404, redirect
from .form import RegisterForm,CustomUserCreationForm
from datetime import date

from collections import defaultdict


@login_required
def index(request):
    current_user = request.user

    # Obtenha o mês atual
    mes_atual = date.today().month

    # Anote a contagem de ocorrências de cada produto no estoque
    produtos_do_estoque = EstoqueItens.objects.filter(estoque__funcionario=current_user)

    # Crie um dicionário para contar as ocorrências de cada produto
    produto_contagem = {}
    for produto in produtos_do_estoque:
        nome_produto = produto.produto.produto
        if nome_produto in produto_contagem:
            produto_contagem[nome_produto] += 1
        else:
            produto_contagem[nome_produto] = 1

    # Encontre o produto mais comum
    produtos_mais_aparecem = Counter(produto_contagem).most_common(3)

    # Inicialize variáveis para o nome e valor dos produtos mais comuns
    primeiroProduto = segundoProduto = terceiroProduto = " "
    valorProduto1 = valorProduto2 = valorProduto3 = 0

    if len(produtos_mais_aparecem) >= 1:
        primeiroProduto = produtos_mais_aparecem[0][0]
        valorProduto1 = produtos_mais_aparecem[0][1]

    if len(produtos_mais_aparecem) >= 2:
        segundoProduto = produtos_mais_aparecem[1][0]
        valorProduto2 = produtos_mais_aparecem[1][1]
    if len(produtos_mais_aparecem) >= 3:
        terceiroProduto = produtos_mais_aparecem[2][0]
        valorProduto3 = produtos_mais_aparecem[2][1]

    # Inicialize o faturamento total
    faturamentoTotal = 0

    for estoque_item in produtos_do_estoque:
        if estoque_item.estoque.movimento == "s":
            saldo = estoque_item.saldo
            faturamentoTotal += saldo

    # Filtrando Produto onde funcionário é igual ao usuário atual
    produtos_estoque_acabando = Produto.objects.filter(funcionario=current_user).annotate(max_quantidade=Max('estoque_minimo'))
    produtos_acabando = produtos_estoque_acabando.order_by('max_quantidade').first()

    # Inicialize o dicionário para armazenar o faturamento por mês
    faturamento_por_mes = defaultdict(int)
    registros = EstoqueItens.objects.filter(estoque__funcionario=current_user)

    for estoque_item, registro in zip(produtos_do_estoque, registros):
        # Use o mês da data de criação do estoque para registro
        mes = registro.estoque.created.month
        faturamento_por_mes[mes] += estoque_item.saldo

    # Criar uma lista de faturamento mensal
    faturamento_mensal = [faturamento_por_mes[i] for i in range(1, 13)]

    # Obtenha o faturamento do mês atual
    faturamento_mensal_atual = faturamento_por_mes.get(mes_atual, 0)

    context = {
        "produtoDestaque": primeiroProduto,
        "faturamentoMensal": faturamento_mensal_atual,
        "produtosAcabando": produtos_acabando,
        "contagens_mensais": faturamento_mensal,
        "contagem_por_mes_nome": faturamento_por_mes,
        "produto1": primeiroProduto,
        "produto2": segundoProduto,
        "produto3": terceiroProduto,
        "valorProduto1": valorProduto1,
        "valorProduto2": valorProduto2,
        "valorProduto3": valorProduto3,
        "faturamentoMensalAtual": faturamento_mensal_atual,
    }

    return render(request, 'dashbord.html', context)




def login_view(request):
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('dashbord:index')
        messages.error(request, 'Login inválido')

    return render(
        request,
        'login.html',
        {
            'titulo':'Login',
            'form': form
        }
    )


def logout_view(request):
    auth.logout(request)
    messages.error(request, 'Desconectado')
    return redirect('dashbord:login')    

def register(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado')
            return redirect('dashbord:login')

    return render(
        request,
        'register.html',
        {   
            'titulo':'registar',
            'form': form,
        }
    )