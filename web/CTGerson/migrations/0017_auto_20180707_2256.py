# Generated by Django 2.0.7 on 2018-07-08 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CTGerson', '0016_auto_20180707_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='occurrence',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='longitute',
            field=models.FloatField(default=0.0),
        ),
    ]