# Generated by Django 4.1.3 on 2023-02-23 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movement', '0002_remove_movement_report'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalmovement',
            name='stock',
        ),
        migrations.RemoveField(
            model_name='movement',
            name='stock',
        ),
    ]
