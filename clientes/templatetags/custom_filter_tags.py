from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, Clientes):
    group = Group.objects.get(name=Clientes)
    return group in user.groups.all()

# @register.filter(name='has_group')
# def has_group(user, Usuários):
#     group = Group.objects.get(name=Usuários)
#     return group in user.groups.all()

