from django.utils.deprecation import MiddlewareMixin

class DefaultJWTMiddleware(MiddlewareMixin):
    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        # Adicione o token JWT ao cabeçalho de autorização, se ele estiver disponível
        jwt_token = "4b370c1a5c0d926e57e05f86daaad572a771ba5d"
        if jwt_token:
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {jwt_token}'

        response = self.get_response(request)
        return response
