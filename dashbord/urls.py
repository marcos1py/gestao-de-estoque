from django.urls import path

from dashbord import views
app_name = "dashbord"
urlpatterns = [
    path('', views.index, name='index'),
    path('user/login/', views.login_view, name='login'),
    path('user/register/', views.register, name='register'),

    path('user/logout/', views.logout_view, name='logout'),

]
