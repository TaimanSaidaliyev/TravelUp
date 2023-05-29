from django.db import models
from django.contrib.auth.models import User
import datetime


class Tours(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название')
    bdate = models.DateField(blank=True, null=True, verbose_name='Дата начала')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания тура')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления тура')
    description = models.TextField(blank=True, max_length=500, verbose_name='Описание')
    image = models.ImageField(upload_to='img/%Y/%m/%d', verbose_name='Изображение', blank=True)

    class Meta:
        verbose_name = 'Туры'
        verbose_name_plural = 'Туры'
        ordering = ['-created_at']

    def __str__(self):
        return self.title