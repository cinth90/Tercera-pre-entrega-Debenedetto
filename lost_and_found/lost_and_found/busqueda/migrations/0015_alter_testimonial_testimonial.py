# Generated by Django 5.0.6 on 2024-07-16 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0014_alter_ifound_photo_alter_ilost_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='testimonial',
            field=models.TextField(max_length=900),
        ),
    ]
