# Generated by Django 2.2 on 2023-01-18 10:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateField(default=datetime.datetime(2023, 1, 18, 10, 44, 8, 188835, tzinfo=utc)),
        ),
    ]
