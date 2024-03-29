# Generated by Django 2.0.7 on 2018-07-10 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CTGerson', '0026_auto_20180709_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='meshblu',
            name='bus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='CTGerson.Bus'),
        ),
        migrations.AddField(
            model_name='occurrence',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='occurrence',
            name='bus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='CTGerson.Bus'),
        ),
    ]
