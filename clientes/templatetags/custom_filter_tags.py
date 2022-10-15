from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, Clientes):
    group = Group.objects.get(name=Clientes)
    return group in user.groups.all()

# @register.filter(name='has_group')
# def has_group(user, Clientes):
#     return user.groups.filter(name=Clientes).exists()

# @register.filter(name='has_group')
# def has_group(user, Clientes):
#     try:
#         group = Group.objects.get(name=Clientes)
#         return True if group in user.groups.all() else False
#     except Group.DoesNotExist:
#         return False

# def multiple_groups(user):
#     return user.groups.filter(name__in=['Clientes', 'Fornecedores'])