# Generated by Django 4.2.1 on 2023-05-30 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regions', '0002_regions_level_regions_lft_regions_rght_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='regions',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/regions/%Y/%m/%d', verbose_name='Изображение'),
        ),
    ]