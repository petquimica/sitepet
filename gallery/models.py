from django.db import models


class HomeImages(models.Model):
    title = models.CharField('Título da imagem', max_length=100)
    image_url = models.CharField('Url da imagem', max_length=250)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Imagens da página principal'
        verbose_name_plural = 'Imagens da página principal'


class Gallery(models.Model):
    title = models.CharField('Título da pasta', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    background = models.CharField('URL da imagem da pasta', max_length=100)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('gallery:images', (), {'slug': self.slug})

    class Meta:
        verbose_name = 'Galeria de imagens'
        verbose_name_plural = 'Galerias de imagens'
        ordering = ['-created_at']


class Image(models.Model):
    image_url = models.CharField('Url da imagem', max_length=250)
    gallery = models.ForeignKey(
        'Gallery',
        on_delete=models.CASCADE,
        related_name="images"
    )

    def __str__(self):
        return self.image_url

    class Meta:
        verbose_name = 'Imagem'
        verbose_name_plural = 'Imagens'
