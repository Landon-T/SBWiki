# Generated by Django 4.0 on 2022-01-19 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0013_abilities_disckey'),
    ]

    operations = [
        migrations.CreateModel(
            name='RaceBaseRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basekey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.baseclass')),
                ('racekey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.race')),
            ],
        ),
    ]
