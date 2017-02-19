from django.db import models

class Team(models.Model):
  name = models.CharField('Nome', max_length=100)
  photo = models.ImageField(upload_to='photos', verbose_name='Fotos')
  description = models.TextField('Descrição')
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)

  def __str__(self):
   return self.name

  class Meta:
    verbose_name = 'Time'
    verbose_name_plural = 'Time'
    ordering = ['name']

