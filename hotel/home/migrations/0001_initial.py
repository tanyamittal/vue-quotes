# Generated by Django 2.0.5 on 2018-07-12 09:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('arr_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('dep_date', models.DateField(default=datetime.date.today, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField(default=0)),
                ('hotel_name', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Dates')),
            ],
        ),
    ]
