# Generated by Django 4.2.1 on 2023-05-29 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0002_agentpublications'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='agent_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agent.agentstatus', verbose_name='Статус агента'),
        ),
        migrations.AlterField(
            model_name='agent',
            name='partner_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='agent.partnertype', verbose_name='Вид партнерства'),
        ),
    ]
