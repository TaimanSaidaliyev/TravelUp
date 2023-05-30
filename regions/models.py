from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


COUNTRIES = (
    ('kz', 'Казахстан'),
    ('ru', 'Россия'),
    ('uz', 'Узбекистан'),
    ('kg', 'Кыргызстан'),
)


class Regions(MPTTModel):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название местности')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')
    country = models.CharField(max_length=2, choices=COUNTRIES)
    longitude = models.CharField(max_length=100, blank=True, verbose_name='Ширина')
    latitude = models.CharField(max_length=100, blank=True, verbose_name='Долгота')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')
    image = models.ImageField(upload_to='media/regions/%Y/%m/%d', verbose_name='Изображение', blank=True)

    class Meta:
        verbose_name = 'Местность'
        verbose_name_plural = 'Местность'
        ordering = ['-created_at']

    def __str__(self):
        return self.title