# Generated by Django 4.0 on 2022-01-05 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_alter_baseclass_icon_alter_gameclass_icon_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=150)),
                ('icon', models.ImageField(upload_to='media')),
                ('effects', models.CharField(max_length=300)),
                ('items', models.CharField(max_length=300)),
                ('dropper', models.CharField(max_length=500)),
                ('trainer', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SkillLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=150)),
                ('level_granted', models.IntegerField()),
                ('is_mastery', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='WeaponPower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='WeaponPowerClassRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power_level', models.IntegerField()),
                ('basekey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.baseclass')),
                ('classkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.gameclass')),
                ('weaponkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.weaponpower')),
            ],
        ),
        migrations.CreateModel(
            name='Stance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=150)),
                ('powerlevel', models.IntegerField()),
                ('basekey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.baseclass')),
                ('classkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.gameclass')),
            ],
        ),
        migrations.CreateModel(
            name='SkillClassRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bonus', models.CharField(max_length=300)),
                ('resrictions', models.CharField(max_length=300)),
                ('classkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.gameclass')),
                ('skillkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.skillline')),
            ],
        ),
        migrations.CreateModel(
            name='DiscClassRaceRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basekey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.baseclass')),
                ('classkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.gameclass')),
                ('disckey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.discipline')),
                ('racekey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.race')),
            ],
        ),
        migrations.CreateModel(
            name='Abilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_text', models.CharField(max_length=150)),
                ('granted_level', models.IntegerField()),
                ('granted_rank', models.IntegerField()),
                ('type', models.CharField(max_length=150)),
                ('cost', models.IntegerField()),
                ('cast_time', models.IntegerField()),
                ('cooldown', models.IntegerField()),
                ('hitroll', models.BooleanField()),
                ('basekey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.baseclass')),
                ('classkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wiki.gameclass')),
            ],
        ),
    ]
