from django.urls import path

from dashbord import views
app_name = "dashbord"
urlpatterns = [
    path('', views.index, name='index'),
    

]
