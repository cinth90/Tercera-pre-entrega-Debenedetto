# Generated by Django 5.0.6 on 2024-07-19 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0017_alter_ilost_color_alter_ilost_model_alter_ilost_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='ilost',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
