from django.shortcuts import render, redirect
from django.db.models import Max
from produto.models import Produto
from estoque.models import EstoqueItens
from django.contrib import auth, messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required



@login_required
def index(request):

    
    produtos_os_produtos = EstoqueItens.objects.annotate(max_quantidade=Max('estoque'))
    
    produto_mais_vendido = produtos_os_produtos.order_by('max_quantidade').first()

    produto1 = "Coca"
    produto2 = "Garana"
    produto3 = "H2o"
    
    
    context = {
        "produtoDestaque":f"{produto_mais_vendido}",
        "faturamentoMensal":"Agua",    
        "despesasMensal":"Agua",    
        "despesasMensal":"Agua", 
        "produtoMenosVendido":f"{produto_mais_vendido}",
        
        'produto1':produto1,
        'produto2':produto2,
        'produto3':produto3,
        }
    
    return render(request, 'dashbord.html',context)




def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Logado com sucesso!')
            return redirect('dashbord:index')
        messages.error(request, 'Login inválido')

    return render(
        request,
        'login.html',
        {
            'form': form
        }
    )


def logout_view(request):
    auth.logout(request)
    return redirect('dashbord:login')    