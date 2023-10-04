# inventory/urls.py
from django.urls import path
from estoque import views
app_name = 'estoque'
urlpatterns = [
    path('', views.estoque_entrada_list, name='estoque_entrada_list'),
    path('<int:pk>/', views.estoque_entrada_detail, name='estoque_entrada_detail'),
    path('add/', views.estoque_entrada_add, name='estoque_entrada_add'),
    path('saida/', views.estoque_saida_list, name='estoque_saida_list'),
    path('saida/<int:pk>/', views.estoque_saida_detail, name='estoque_saida_detail'),
    path('saida/add/', views.estoque_saida_add, name='estoque_saida_add'),
    
    
    path('api/estoque/', views.EstoqueListCreateView.as_view(), name='estoque-list-create'),
    path('api/estoque/<int:pk>/', views.EstoqueDetailView.as_view(), name='estoque-detail'),
    path('api/estoqueitens/', views.EstoqueItensListCreateView.as_view(), name='estoqueitens-list-create'),
    path('api/estoqueitens/<int:pk>/', views.EstoqueItensDetailView.as_view(), name='estoqueitens-detail'),
    # ...
]
