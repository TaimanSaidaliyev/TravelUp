# Generated by Django 4.2.1 on 2023-05-29 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Статус агента')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Статус агента',
                'verbose_name_plural': 'Статус агента',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='PartnerType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Тип')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Вид партнерства',
                'verbose_name_plural': 'Вид партнерства',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Название тур агентства')),
                ('logo', models.ImageField(blank=True, upload_to='media/agent/logo/%Y/%m/%d', verbose_name='Логотип компании')),
                ('background_image', models.ImageField(blank=True, upload_to='media/agent/background/%Y/%m/%d', verbose_name='Фоновое изображение')),
                ('web_site', models.CharField(blank=True, max_length=100, verbose_name='Веб-сайт')),
                ('email', models.CharField(blank=True, max_length=100, verbose_name='Email')),
                ('instagram', models.CharField(blank=True, max_length=100, verbose_name='Instagram')),
                ('facebook', models.CharField(blank=True, max_length=100, verbose_name='Facebook')),
                ('vk', models.CharField(blank=True, max_length=100, verbose_name='vk')),
                ('registered', models.BooleanField(blank=True, verbose_name='Доступ на сервис')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('agent_status', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='agent.agentstatus', verbose_name='Статус агента')),
                ('partner_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='agent.partnertype', verbose_name='Вид партнерства')),
            ],
            options={
                'verbose_name': 'Тур агенты',
                'verbose_name_plural': 'Тур агенты',
                'ordering': ['-created_at'],
            },
        ),
    ]
