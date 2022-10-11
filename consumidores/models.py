from django.db import models
from django.contrib.auth.models import User

from usuarios.models import Perfil

#Create your models here.

def user_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'usuario_{0}/{1}'.format(instance.user.id, filename)

class Consumidores(models.Model):
    apelido = models.CharField(max_length=100,verbose_name='Nome')
    cpf = models.CharField(max_length=20, verbose_name='CPF')
    ativo = models.CharField(max_length=1)
    criem = models.DateTimeField(auto_now_add=True)
    cripor = models.ForeignKey(Perfil,related_name='Consumidor',on_delete=models.CASCADE)

    def __str__(self):
        return '%s' % (self.apelido)

    class Meta:
        ordering = (['apelido'])
        verbose_name = 'Consumidor'
        verbose_name_plural = 'Consumidores'
