# Generated by Django 3.0.8 on 2020-08-08 14:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0033_auto_20200808_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitems',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 8, 14, 39, 24, 911753, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bids',
            name='bid_item',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='bids',
            name='bid_price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='closed_auctions',
            name='closed_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 8, 14, 39, 24, 914600, tzinfo=utc)),
        ),
    ]
