# Generated by Django 3.0.8 on 2020-07-07 18:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0003_auto_20200707_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 7, 23, 59, 27, 593195), editable=False),
        ),
    ]