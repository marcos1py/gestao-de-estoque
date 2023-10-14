# produto/urls.py
from django.urls import path
from . import views

app_name = "produto"

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('<int:pk>/', views.produto_detail, name='produto_detail'),
    path('<int:pk>/json/', views.produto_json, name='produto_json'),    
    path('add/', views.produto_add, name='produto_add'),  # Change the URL to use the function-based view
    path('<int:pk>/edit/', views.ProdutoUpdate.as_view(), name='produto_edit'),    
]
