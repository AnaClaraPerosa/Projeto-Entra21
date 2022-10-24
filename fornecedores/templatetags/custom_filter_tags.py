from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='has_group')
def has_group(user, Fornecedores):
    group = Group.objects.get(name=Fornecedores)
    return group in user.groups.all()