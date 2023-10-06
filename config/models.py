from django.contrib.auth.models import User

# Adicione related_name aos campos de relacionamento reverso do User
User._meta.get_field('groups').related_name = 'user_groups'
User._meta.get_field('user_permissions').related_name = 'user_permissions'

# Certifique-se de que a classe CustomUser não está sobrescrevendo o User
from empresas.models import CustomUser
