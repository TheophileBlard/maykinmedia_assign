# Generated by Django 2.0.3 on 2018-03-13 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('ID', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('cityID', models.CharField(max_length=3)),
                ('ID', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
    ]
