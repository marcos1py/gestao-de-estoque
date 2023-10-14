# inventory/urls.py
from django.urls import path
from estoque import views
app_name = 'estoque'
urlpatterns = [
    path('', views.estoque_entrada_list, name='estoque_entrada_list'),
    path('<int:pk>/', views.EstoqueDetail.as_view(), name='estoque_detail'),
    path('add/', views.estoque_entrada_add, name='estoque_entrada_add'),
    path('saida/', views.estoque_saida_list, name='estoque_saida_list'),
    path('saida/<int:pk>/', views.estoque_saida_detail, name='estoque_saida_detail'),
    path('saida/add/', views.estoque_saida_add, name='estoque_saida_add'),
    # ...
]
