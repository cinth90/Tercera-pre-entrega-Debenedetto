# Generated by Django 5.0.6 on 2024-07-14 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busqueda', '0008_rename_return_owner_ifound_returned_owner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phoneNumber', models.IntegerField()),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]
