# Generated by Django 5.1 on 2024-08-14 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pi_grow_dash', '0002_growreading_moisture_3'),
    ]

    operations = [
        migrations.RenameField(
            model_name='growreading',
            old_name='timestmap',
            new_name='timestamp',
        ),
    ]
