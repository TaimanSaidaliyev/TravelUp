from django.db import models
from django.contrib.auth.models import User
from regions.models import Regions
from agent.models import Agent
from .dictionary import TOUR_DATE_STATUS
from services.models import Services
from locations.models import Locations


class Tours(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название')
    category = models.ManyToManyField('TourCategory', verbose_name='Категории')
    region = models.ForeignKey(Regions, on_delete=models.CASCADE, verbose_name='Местность')
    locations = models.ManyToManyField(Locations, verbose_name='Локации')
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, verbose_name='Тур агент')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания тура')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления тура')
    count_days = models.IntegerField(blank=True, verbose_name='Количество дней')
    count_people = models.IntegerField(blank=True, verbose_name='Максимальное количество туристов')
    description = models.TextField(blank=True, max_length=500, verbose_name='Описание')
    image = models.ImageField(upload_to='img/%Y/%m/%d', verbose_name='Изображение', blank=True)
    included_in_price = models.ManyToManyField(Services, blank=True, verbose_name='Входит в стоимость', related_name='services_included_in_price')
    not_included_price = models.ManyToManyField(Services, blank=True, verbose_name='Не входит в стоимость', related_name='services_not_included_in_price')
    additional_services = models.ManyToManyField(Services, blank=True, verbose_name='Дополнительно оплачивается', related_name='services_additional')
    additional_description = models.TextField(blank=True, max_length=500, verbose_name='Дополнительная информация')
    vip = models.BooleanField(blank=True, verbose_name='VIP тур')

    class Meta:
        verbose_name = 'Туры'
        verbose_name_plural = 'Туры'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class TourCategory(models.Model):
    title_ru = models.CharField(max_length=100, blank=True, verbose_name='Категория на русском')
    title_kz = models.CharField(max_length=100, blank=True, verbose_name='Категория на казахском')
    title_en = models.CharField(max_length=100, blank=True, verbose_name='Категория на английском')
    image = models.ImageField(upload_to='img/%Y/%m/%d', verbose_name='Изображение', blank=True)
    icon_name = models.CharField(max_length=100, blank=True, verbose_name='Иконка')
    icon_collection = models.CharField(max_length=100, blank=True, verbose_name='Коллекция иконок')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания тура')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления тура')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'
        ordering = ['-created_at']

    def __str__(self):
        return self.title_ru


class TourDates(models.Model):
    tour = models.ForeignKey('Tours', on_delete=models.CASCADE, blank=True, verbose_name='Тур')
    date = models.DateTimeField(blank=True, verbose_name='Дата тура')
    status = models.CharField(blank=True, max_length=3, choices=TOUR_DATE_STATUS)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Дата тура'
        verbose_name_plural = 'Дата тура'
        ordering = ['-created_at']

    def __str__(self):
        return self.title_ru


class TourProgram(models.Model):
    tour = models.ForeignKey('Tours', on_delete=models.CASCADE, blank=True, verbose_name='Тур')
    day = models.IntegerField(blank=True, verbose_name='День')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Программа тура'
        verbose_name_plural = 'Программа тура'
        ordering = ['-created_at']

    def __str__(self):
        return self.tour.title + ' - День ' + str(self.day)


class TourProgramSchedule(models.Model):
    tour_program = models.ForeignKey('TourProgram', on_delete=models.CASCADE, blank=True, verbose_name='Расписание')
    time = models.TimeField(blank=True, verbose_name='Время')
    description = models.CharField(max_length=100, blank=True, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Расписание тура'
        verbose_name_plural = 'Расписание тура'
        ordering = ['-created_at']

    def __str__(self):
        return self.tour_program.tour.title + ' - ' + str(self.time) + ' - ' + self.description
