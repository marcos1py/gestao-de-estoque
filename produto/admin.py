from django.contrib import admin


from .models import Produto, Categoria



@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'ncm',
        'preco' ,
        'estoque',
        'estoque_minimo',
        'data',
    )
    search_fields = ("produto",)
    
admin.site.register(Categoria)