# Generated by Django 5.0.6 on 2024-07-20 05:57

import busqueda.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0020_alter_ilost_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilost',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='ilost',
            name='name_booking',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='ilost',
            name='room_number',
            field=models.IntegerField(blank=True, validators=[busqueda.models.validate_four_digits]),
        ),
    ]
