from django.db import models
from taggit.managers import TaggableManager
from django.core.urlresolvers import reverse

class Information(models.Model):
  title = models.CharField('Título', max_length=100)
  slug = models.SlugField('Identificador', max_length=100)
  content = models.TextField('Conteúdo', max_length=1000)
  tags = TaggableManager(blank=True)
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


class File(models.Model):
  title = models.CharField('Título', max_length=100)
  slug = models.SlugField('Identificador', max_length=100)
  document = models.FileField(upload_to='documents/information', verbose_name="Documentos", null=True, blank=True)
  information = models.ForeignKey(Information, on_delete=models.CASCADE, verbose_name="Informação", related_name="files")

  def __str__(self):
    return self.title

class Link(models.Model):
  title = models.CharField('Título', max_length=100)
  link = models.URLField('Link')
  information = models.ForeignKey(Information, on_delete=models.CASCADE, verbose_name="Informação", related_name="links")

  def __str__(self):
    return self.link
