from django.db import models


class Gallery(models.Model):
  title = models.CharField('Título', max_length=100)
  description = models.TextField('Descrição')
  recent_picture = models.BooleanField('Imagem mais recente', default=False)
  image = models.ImageField(upload_to='gallery', verbose_name='Imagem')
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Imagem'
    verbose_name_plural = 'Galeria de imagens'
    ordering = ['-created_at']
