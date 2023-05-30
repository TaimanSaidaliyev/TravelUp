from django.db import models
from regions.models import Regions


class Locations(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название')
    category = models.ManyToManyField('LocationCategory', blank=True, verbose_name='Категория')
    description = models.TextField(blank=True, verbose_name='Описание')
    attraction = models.ManyToManyField('Attractions', blank=True, verbose_name='Достопримечательности')
    region = models.ForeignKey(Regions, blank=True, on_delete=models.CASCADE, verbose_name='Регион')
    longitude = models.CharField(max_length=100, blank=True, verbose_name='Ширина')
    latitude = models.CharField(max_length=100, blank=True, verbose_name='Долгота')
    image = models.ImageField(upload_to='media/locations/%Y/%m/%d', verbose_name='Изображение', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Локации'
        verbose_name_plural = 'Локации'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class LocationCategory(models.Model):
    title_ru = models.CharField(max_length=100, blank=True, verbose_name='Название на русском')
    title_kz = models.CharField(max_length=100, blank=True, verbose_name='Название на казахском')
    title_en = models.CharField(max_length=100, blank=True, verbose_name='Название на английском')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Категории локаций'
        verbose_name_plural = 'Категории локаций'
        ordering = ['-created_at']

    def __str__(self):
        return self.title_ru


class Attractions(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название')
    image = models.ImageField(upload_to='media/attractions/%Y/%m/%d', verbose_name='Изображение', blank=True)
    longitude = models.CharField(max_length=100, blank=True, verbose_name='Ширина')
    latitude = models.CharField(max_length=100, blank=True, verbose_name='Долгота')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Достопримечательности'
        verbose_name_plural = 'Достопримечательности'
        ordering = ['-created_at']

    def __str__(self):
        return self.title