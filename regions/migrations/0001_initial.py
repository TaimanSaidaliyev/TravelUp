# Generated by Django 4.2.1 on 2023-05-29 14:54

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='Название местности')),
                ('country', models.CharField(choices=[('kz', 'Казахстан'), ('ru', 'Россия'), ('uz', 'Узбекистан'), ('kg', 'Кыргызстан')], max_length=2)),
                ('longitude', models.CharField(blank=True, max_length=100, verbose_name='Ширина')),
                ('latitude', models.CharField(blank=True, max_length=100, verbose_name='Долгота')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='regions.regions')),
            ],
            options={
                'verbose_name': 'Местность',
                'verbose_name_plural': 'Местность',
                'ordering': ['-created_at'],
            },
        ),
    ]