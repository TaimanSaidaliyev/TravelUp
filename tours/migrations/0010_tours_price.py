# Generated by Django 4.2.1 on 2023-05-30 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0009_tours_locations'),
    ]

    operations = [
        migrations.AddField(
            model_name='tours',
            name='price',
            field=models.FloatField(blank=True, default=0, verbose_name='Цена тура'),
            preserve_default=False,
        ),
    ]
