# Generated by Django 5.0 on 2024-03-22 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0051_usuario_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='loe',
            field=models.FloatField(blank=True, max_length=100, null=True),
        ),
    ]
