from django.db import models


class AdicionalInformation(models.Model):
  address = models.CharField('Endereço', max_length=100)
  phone = models.CharField('Telefone', max_length=20)
  email = models.EmailField('Email')
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)

  def __str__(self):
    return "Informações Adicionais"

  class Meta:
    verbose_name = "Informações Adicionais"
    verbose_name_plural = "Informações Adicionais"
    ordering = ['created_at']
