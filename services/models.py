from django.db import models


class Services(models.Model):
    title_ru = models.CharField(max_length=100, blank=True, verbose_name='Название на русском')
    title_kz = models.CharField(max_length=100, blank=True, verbose_name='Название на казахском')
    title_en = models.CharField(max_length=100, blank=True, verbose_name='Название на английском')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания тура')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления тура')
    icon_name = models.CharField(max_length=100, blank=True, verbose_name='Иконка')
    icon_collection = models.CharField(max_length=100, blank=True, verbose_name='Коллекция иконок')

    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуги'
        ordering = ['-created_at']

    def __str__(self):
        return self.title_ru