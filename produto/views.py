from .models import Produto
from django.shortcuts import render
from .forms import ProdutoForm
from django.views.generic import CreateView, UpdateView
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
def produto_list(request):
    template_name = "produto_list.html"
    objects = Produto.objects.all()
    context = {
        'objects_list' : objects,
    }
    return render(request, template_name, context)
def produto_detail(request, pk):
    template_name = "produto_detail.html"
    obj = Produto.objects.get(pk=pk)
    context = {
        'object' : obj,
    }
    return render(request, template_name, context)

def produto_add(request):
    form = ProdutoForm(request.POST or None)
    template_name = 'produto_form2.html'
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('produto:produto_list'))

    context = {'form': form}
    return render(request, template_name, context)



class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm


class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produto_edit.html'
    form_class = ProdutoForm
    
def produto_json(request, pk):
    ''' Retorna o produto, id e estoque. '''
    produto = Produto.objects.filter(pk=pk)
    data = [item.to_dict_json() for item in produto]
    return JsonResponse({'data': data})