from django.db import models

class Project(models.Model):
  title = models.CharField('Título', max_length=100)
  content = models.TextField('Conteúdo', max_length=1000)
  link = models.URLField('Google Driver', help_text='Link para o Google Driver', blank=True)
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = 'Projeto'
    verbose_name_plural = 'Projetos'
    ordering = ['-created_at']
