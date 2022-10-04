from io import BytesIO
from django.db import models
from PIL import Image
from django.core.files import File
from django.db import models
from fornecedores.models import Fornecedores

#Create your models here.


class Categoria(models.Model):
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordem = models.IntegerField(default=0)

    
    class Meta:
        ordering = ['ordem']

    def __str__(self):
        return self.titulo


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(Fornecedores, related_name='produtos', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    data_add = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to ='uploads/', blank = True, null = True)
    thumbnail = models.ImageField(upload_to ='uploads/', blank = True, null = True)


    class Meta:
        ordering = ['-data_add']

    def __str__(self):
        return self.titulo

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.imagem:
                self.thumbnail = self.make_thumbnail(self.imagem)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

