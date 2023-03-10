# Generated by Django 4.0 on 2022-01-04 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_alter_gameclass_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseclass',
            name='icon',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='gameclass',
            name='icon',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='race',
            name='icon',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.CreateModel(
            name='ClassRaceRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.gameclass')),
                ('racekey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.race')),
            ],
        ),
    ]
