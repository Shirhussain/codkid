# Generated by Django 3.0.2 on 2020-04-10 19:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Khodi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2020, 4, 10, 19, 54, 15, 496352, tzinfo=utc))),
            ],
        ),
    ]