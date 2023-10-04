from django.contrib import admin
from django.urls import path, include  # Importe a função 'include'

urlpatterns = [
    path('', include('core.urls')),
    path('produto/', include('produto.urls')),
    path('estoque/', include('estoque.urls')),
    path('admin/', admin.site.urls),
    
    #path('api/', include('estoque.urls')),  # Inclua as URLs do aplicativo 'estoque'
    #path('api/', include('produto.urls')),  # Inclua as URLs do aplicativo 'produto'
    path('api/', include('authentication.urls')),  # Inclua as URLs do aplicativo 'produto'
    

]
