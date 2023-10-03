# produto/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Produto
from .serializers import ProdutoSerializer
from django.shortcuts import render
from .forms import ProdutoForm
from django.views.generic import CreateView, UpdateView

class ProdutoListCreateView(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]

class ProdutoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]
    
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
    template_name = 'produto_form.html'
    return render(request, template_name)


class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm


class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produto_edit.html'
    form_class = ProdutoForm