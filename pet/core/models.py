from django.db import models

class About(models.Model):
  title = models.TextField('Título', max_length=180)
  description = models.TextField('Descrição', max_length=550)

  def __str__(self):
    return self.title

  class Meta:
    verbose_name = "Sobre"

class Footer(models.Model):
  copyright = models.TextField('Rodapé', max_length=550)

  def __str__(self):
    return self.copyright

  class Meta:
    verbose_name = "Rodapé"
