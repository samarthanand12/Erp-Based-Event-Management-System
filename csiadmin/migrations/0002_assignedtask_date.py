# Generated by Django 3.1.7 on 2021-05-25 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csiadmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignedtask',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
