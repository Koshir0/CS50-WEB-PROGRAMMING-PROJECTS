# Generated by Django 3.0.8 on 2020-08-12 17:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0049_auto_20200812_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitems',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 12, 17, 18, 45, 791010, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='closed_auctions',
            name='closed_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 12, 17, 18, 45, 794967, tzinfo=utc)),
        ),
    ]