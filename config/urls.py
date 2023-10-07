from django.contrib import admin
from django.urls import path, include  # Importe a função 'include'

urlpatterns = [
    #path('', include('core.urls')),
    path('', include('dashbord.urls')),
    path('produto/', include('produto.urls')),
    path('estoque/', include('estoque.urls')),
    path('admin/', admin.site.urls),
]
