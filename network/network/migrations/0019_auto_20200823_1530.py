# Generated by Django 3.0.8 on 2020-08-23 15:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0018_auto_20200823_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 23, 15, 30, 1, 449347, tzinfo=utc)),
        ),
    ]
