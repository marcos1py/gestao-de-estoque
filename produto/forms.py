from django import forms
from .models import Produto


class ProdutoForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ['ncm', 'produto', 'preco', 'estoque', 'estoque_minimo', 'data', 'categoria']
