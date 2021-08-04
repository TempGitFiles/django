from django.db import models


class Tovar(models.Model):
    title = models.CharField('Название', max_length=255, unique=True)
    article = models.CharField('Арт.', max_length=16, null=True, blank=True)
    description = models.TextField('Описание', null=True, blank=True)
    count = models.PositiveIntegerField('Количество', default=0)

    def __str__(self):
        return f'{self.title} Арт.{self.article}' if self.article else f'{self.title} Арт.не найден'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
