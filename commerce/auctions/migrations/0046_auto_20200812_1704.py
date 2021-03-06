# Generated by Django 3.0.8 on 2020-08-12 17:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0045_auto_20200812_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionitems',
            name='category',
        ),
        migrations.AddField(
            model_name='categories',
            name='item',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auctionitems',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 12, 17, 4, 53, 242397, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='closed_auctions',
            name='closed_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 12, 17, 4, 53, 245438, tzinfo=utc)),
        ),
    ]
