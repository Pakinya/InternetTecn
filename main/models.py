from django.db import models

class Artiles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата и Время')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Нововсти'



class Goroskop(models.Model):
    title = models.CharField('Название', max_length=50)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата и Время')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Гороскоп'
        verbose_name_plural = 'Гороскопы'