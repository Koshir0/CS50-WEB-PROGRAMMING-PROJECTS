# Generated by Django 3.0.8 on 2020-08-12 15:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0043_auto_20200810_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitems',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 12, 15, 56, 23, 714046, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='closed_auctions',
            name='closed_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 12, 15, 56, 23, 718045, tzinfo=utc)),
        ),
    ]