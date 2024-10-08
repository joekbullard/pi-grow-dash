# Generated by Django 5.1 on 2024-08-18 14:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pi_grow_dash', '0004_rename_light_growreading_luminance_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=40)),
                ('uid', models.CharField(max_length=16)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('temperature', models.FloatField()),
                ('humidity', models.FloatField()),
                ('pressure', models.FloatField()),
                ('luminance', models.FloatField()),
                ('moisture_a', models.FloatField()),
                ('moisture_b', models.FloatField()),
                ('moisture_c', models.FloatField()),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pi_grow_dash.board')),
            ],
        ),
    ]
