from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Publication(models.Model):
    name = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug')
    description = models.CharField(max_length=150, verbose_name='содержимое', **NULLABLE)
    image = models.ImageField(upload_to='img_publication', verbose_name='превью', **NULLABLE)
    created_at = models.DateField(verbose_name='дата создания', auto_now_add=True)
    publication_activ = models.BooleanField(verbose_name='признак публикации', default=True)
    counter = models.IntegerField(verbose_name='количество просмотров', default=0)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
