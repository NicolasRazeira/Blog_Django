# Generated by Django 5.0.1 on 2024-02-03 03:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=255)),
                ('titulo', models.CharField(max_length=255)),
                ('subtitle', models.CharField(max_length=255)),
                ('conteudo', models.TextField()),
                ('data_publicacao', models.DateTimeField(default=datetime.datetime(2024, 2, 3, 0, 52, 50, 743022))),
            ],
        ),
    ]
