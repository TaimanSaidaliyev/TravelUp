# Generated by Django 4.2.1 on 2023-05-30 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_tours_additional_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tours',
            name='category',
        ),
        migrations.AddField(
            model_name='tours',
            name='category',
            field=models.ManyToManyField(to='tours.tourcategory', verbose_name='Категории'),
        ),
    ]