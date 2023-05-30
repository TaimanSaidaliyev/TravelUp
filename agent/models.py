from django.db import models


class Agent(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Название тур агентства')
    logo = models.ImageField(upload_to='media/agent/logo/%Y/%m/%d', verbose_name='Логотип компании', blank=True)
    background_image = models.ImageField(upload_to='media/agent/background/%Y/%m/%d', verbose_name='Фоновое изображение', blank=True)
    web_site = models.CharField(max_length=100, blank=True, verbose_name='Веб-сайт')
    email = models.CharField(max_length=100, blank=True, verbose_name='Email')
    instagram = models.CharField(max_length=100, blank=True, verbose_name='Instagram')
    facebook = models.CharField(max_length=100, blank=True, verbose_name='Facebook')
    vk = models.CharField(max_length=100, blank=True, verbose_name='vk')
    partner_type = models.ForeignKey('PartnerType', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Вид партнерства')
    agent_status = models.ForeignKey('AgentStatus', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Статус агента')
    registered = models.BooleanField(blank=True, verbose_name='Доступ на сервис')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Тур агенты'
        verbose_name_plural = 'Тур агенты'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class PartnerType(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Тип')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Вид партнерства'
        verbose_name_plural = 'Вид партнерства'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class AgentStatus(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Статус агента')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Статус агента'
        verbose_name_plural = 'Статус агента'
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class AgentPublications(models.Model):
    title = models.CharField(max_length=100, blank=True, verbose_name='Статус агента')
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE, blank=True, verbose_name='Тур агент')
    description = models.TextField(blank=True, max_length=500, verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Дата обновления')
    image = models.ImageField(upload_to='media/agent/publications/%Y/%m/%d', verbose_name='Изображение', blank=True)

    class Meta:
        verbose_name = 'Публикации агента'
        verbose_name_plural = 'Публикации агента'
        ordering = ['-created_at']

    def __str__(self):
        return self.title