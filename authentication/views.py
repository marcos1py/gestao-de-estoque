# authentication/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.conf import settings
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
User = get_user_model()

class CustomUserCreateView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)

        if user:
            # Gere um token de ativação (opcional)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            activation_link = settings.FRONTEND_BASE_URL + reverse(
                'user-activation',
                kwargs={'uidb64': uid, 'token': token},
            )

            # Envie um email de ativação (você pode personalizar esta parte)
            # Envie um link de ativação para o email do usuário
            # Implemente esta parte usando pacotes como Django's send_mail ou
            # qualquer serviço de envio de e-mails.

            return Response(
                {'message': 'Usuário registrado com sucesso. Verifique seu email para ativação.'},
                status=status.HTTP_201_CREATED
            )
# authentication/views.py


class CustomObtainJWTToken(APIView):
    def post(self, request):
        # Simplesmente gere um token de atualização e retorne-o como resposta
        refresh = RefreshToken.for_user(request.user)
        token = str(refresh.access_token)
        print(token,refresh)

        return Response({'token': token}, status=status.HTTP_200_OK)
