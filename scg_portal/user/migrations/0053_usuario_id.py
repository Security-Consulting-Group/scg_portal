# Generated by Django 5.0 on 2024-03-22 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0052_usuario_id_alter_tarea_loe'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
