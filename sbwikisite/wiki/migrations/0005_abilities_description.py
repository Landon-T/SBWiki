# Generated by Django 4.0 on 2022-01-05 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0004_discipline_skillline_weaponpower_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='abilities',
            name='description',
            field=models.CharField(default=None, max_length=1500),
        ),
    ]
