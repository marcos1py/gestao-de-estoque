# authentication/urls.py
from django.urls import path
from .views import CustomObtainJWTToken, CustomUserCreateView

urlpatterns = [
    path('token/', CustomObtainJWTToken.as_view(), name='token_obtain_pair'),
    path('signup/', CustomUserCreateView.as_view(), name='signup'),
    # ...
]
