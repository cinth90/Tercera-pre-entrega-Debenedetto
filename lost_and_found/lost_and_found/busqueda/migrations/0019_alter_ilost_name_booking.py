# Generated by Django 5.0.6 on 2024-07-19 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0018_ilost_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ilost',
            name='name_booking',
            field=models.CharField(default='', max_length=60, null=True),
        ),
    ]
