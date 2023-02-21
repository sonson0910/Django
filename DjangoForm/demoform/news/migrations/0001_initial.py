# Generated by Django 2.2 on 2023-01-16 09:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=1000)),
                ('time_create', models.DateField(default=datetime.datetime(2023, 1, 16, 9, 27, 46, 36920, tzinfo=utc))),
            ],
        ),
    ]
