# inventory/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Estoque, EstoqueItens
from .serializers import EstoqueSerializer, EstoqueItensSerializer
from django.shortcuts import render

class EstoqueListCreateView(generics.ListCreateAPIView):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
    permission_classes = [IsAuthenticated]

class EstoqueDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
    permission_classes = [IsAuthenticated]

class EstoqueItensListCreateView(generics.ListCreateAPIView):
    queryset = EstoqueItens.objects.all()
    serializer_class = EstoqueItensSerializer
    permission_classes = [IsAuthenticated]

class EstoqueItensDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EstoqueItens.objects.all()
    serializer_class = EstoqueItensSerializer
    permission_classes = [IsAuthenticated]


#
def estoque_entrada_list(request):
    template_name = "estoque_entrada_list.html"
    objects = Estoque.objects.filter(movimento='e')
    context = {'object_list': objects}
    return render(request,template_name,context)