# Generated by Django 5.1.4 on 2024-12-17 01:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car_brand', to='cars.brand'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=200),
        ),
    ]
