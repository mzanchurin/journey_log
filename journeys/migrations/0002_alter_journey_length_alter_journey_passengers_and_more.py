# Generated by Django 4.0.4 on 2022-05-11 08:14

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journeys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='length',
            field=models.DecimalField(decimal_places=1, max_digits=100),
        ),
        migrations.AlterField(
            model_name='journey',
            name='passengers',
            field=models.ManyToManyField(through='journeys.JourneyPassengers', to=settings.AUTH_USER_MODEL, verbose_name='users'),
        ),
        migrations.AlterField(
            model_name='journey',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
