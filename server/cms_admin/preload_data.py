from django.contrib.auth.models import User, Permission
from users.models import *


def get_all_permissions():
    return Permission.objects.all()



permissions = get_all_permissions()
print(permissions)