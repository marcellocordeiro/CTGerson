# Generated by Django 2.0.7 on 2018-07-08 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CTGerson', '0018_auto_20180707_2257'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bus',
            options={'permissions': (('can_see_list', 'See bus list'),)},
        ),
    ]
