# inventory/urls.py
from django.urls import path
from estoque import views
app_name = 'estoque'
urlpatterns = [
    path('', views.estoque_entrada_list, name='estoque_entrada_list'),
    path('estoque/', views.EstoqueListCreateView.as_view(), name='estoque-list-create'),
    path('estoque/<int:pk>/', views.EstoqueDetailView.as_view(), name='estoque-detail'),
    path('estoqueitens/', views.EstoqueItensListCreateView.as_view(), name='estoqueitens-list-create'),
    path('estoqueitens/<int:pk>/', views.EstoqueItensDetailView.as_view(), name='estoqueitens-detail'),
    # ...
]
