# Generated by Django 4.2.1 on 2023-05-29 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0003_alter_agent_agent_status_alter_agent_partner_type'),
        ('tours', '0005_alter_tourdates_options_tourdates_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tours',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.agent', verbose_name='Тур агент'),
        ),
    ]