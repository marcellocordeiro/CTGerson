# Generated by Django 2.0.7 on 2018-07-08 00:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CTGerson', '0002_auto_20180706_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ocurrence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('alert_time', models.TimeField(auto_now_add=True)),
                ('responded', models.BooleanField(default=False)),
                ('response_time', models.TimeField()),
                ('finish_time', models.TimeField()),
                ('successfull', models.BooleanField()),
                ('notes', models.TextField()),
                ('busid', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='CTGerson.Bus')),
                ('responder_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
