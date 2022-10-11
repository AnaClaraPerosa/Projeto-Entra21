from django.db import models
from django.contrib.auth.models import User

from usuarios.models import Perfil

#Create your models here.

def user_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'usuario_{0}/{1}'.format(instance.user.id, filename)

class Clientes(models.Model):
    cliente_apelido = models.CharField(max_length=100,verbose_name='Nome')
    cliente_ativo = models.CharField(max_length=1)
    cliente_criem = models.DateTimeField(auto_now_add=True)
    cliente_cripor = models.ForeignKey(Perfil,related_name='cliente',on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.cliente_apelido)

    class Meta:
        ordering = (['cliente_apelido'])
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
