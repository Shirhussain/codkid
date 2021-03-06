# Generated by Django 3.0.2 on 2020-04-11 15:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('khodi', '0003_auto_20200411_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khodi',
            name='title',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, unique=True)),
                ('content', models.TextField()),
                ('slug', models.SlugField(editable=False)),
                ('submitted', models.DateField(default=django.utils.timezone.now)),
                ('topic', models.CharField(max_length=20)),
                ('khodi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khodi.Khodi')),
            ],
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('code', models.TextField()),
                ('slug', models.SlugField(editable=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='khodi.Post')),
            ],
        ),
    ]
