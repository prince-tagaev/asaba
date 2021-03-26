from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    title = models.CharField('Название новость', max_length=50, null=False)
    image = models.ImageField(null=True, blank=True, upload_to='images/', height_field=None, width_field=None,
                              max_length=100)
    text = models.TextField('Основной текст новость')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateTimeField('Дата', default=timezone.now)

    def __str__(self):
        return self.title
