from django.shortcuts import render
from django.db.models import Max
from produto.models import Produto
from estoque.models import EstoqueItens




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
