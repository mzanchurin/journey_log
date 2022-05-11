# Generated by Django 4.0.4 on 2022-05-10 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journey',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('length', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='JourneyPassengers',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('journey', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='journeys.journey')),
                ('passenger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='journey',
            name='passengers',
            field=models.ManyToManyField(blank=True, through='journeys.JourneyPassengers', to=settings.AUTH_USER_MODEL, verbose_name='users'),
        ),
        migrations.AddField(
            model_name='journey',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journeys', to='vehicles.vehicle', verbose_name='vehicle'),
        ),
    ]
