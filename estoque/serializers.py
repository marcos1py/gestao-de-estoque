# inventory/serializers.py
from rest_framework import serializers
from .models import Estoque, EstoqueItens

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estoque
        fields = '__all__'

class EstoqueItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstoqueItens
        fields = '__all__'
