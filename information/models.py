from django.db import models
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse

class Information(models.Model):
  title = models.CharField('Título', max_length=100)
  slug = models.SlugField('Identificador', max_length=100)
  content = models.TextField('Conteúdo', max_length=1000)
  tags = TaggableManager(blank=True)
  image = models.ImageField(upload_to='documents/information', verbose_name="Imagem", blank=True, null=True)
  link = models.URLField('Google Driver', help_text='Link para o Google Driver', blank=True)
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)

  def __str__(self):
    return self.title

  @models.permalink
  def get_absolute_url(self):
    return ('information:details', (), {'slug': self.slug})

  class Meta:
    verbose_name = 'Informação'
    verbose_name_plural = 'Informações'
    ordering = ['-created_at']
