# Generated by Django 4.0 on 2022-01-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0014_racebaserelationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discipline',
            name='effects',
            field=models.TextField(max_length=300),
        ),
    ]
