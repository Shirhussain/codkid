# Generated by Django 3.0.2 on 2020-04-11 10:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('khodi', '0002_auto_20200410_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khodi',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]