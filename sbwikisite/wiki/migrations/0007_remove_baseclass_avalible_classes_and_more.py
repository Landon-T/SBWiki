# Generated by Django 4.0 on 2022-01-05 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0006_alter_abilities_basekey_alter_abilities_classkey_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='baseclass',
            name='avalible_classes',
        ),
        migrations.CreateModel(
            name='BaseGameClassRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basekey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.baseclass')),
                ('classkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.gameclass')),
            ],
        ),
    ]