# Generated by Django 2.0.7 on 2018-07-08 00:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('CTGerson', '0006_auto_20180707_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ocurrence',
            name='finish_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ocurrence',
            name='notes',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='ocurrence',
            name='response_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='ocurrence',
            name='successfull',
            field=models.BooleanField(default=False),
        ),
    ]
