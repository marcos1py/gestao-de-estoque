from django.http import HttpResponseRedirect
from django.urls import reverse

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verifique se o usuário não está autenticado e se a página não é a de login.
        if not request.user.is_authenticated and request.path_info != reverse('login'):
            # Redirecione para a página de login.
            return HttpResponseRedirect(reverse('login'))

        response = self.get_response(request)
        return response
