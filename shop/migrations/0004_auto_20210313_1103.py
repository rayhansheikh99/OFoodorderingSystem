# Generated by Django 3.1.3 on 2021-03-13 05:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210313_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='orders',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]