# Generated by Django 4.1.3 on 2023-02-26 01:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_historicaluser_role_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaluser',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'boss'), (2, 'assistant'), (3, 'seller')], default=3, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'boss'), (2, 'assistant'), (3, 'seller')], default=3, null=True),
        ),
    ]
