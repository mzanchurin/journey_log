# Generated by Django 4.0.4 on 2022-05-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('reg_number', models.CharField(max_length=255)),
                ('label', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
