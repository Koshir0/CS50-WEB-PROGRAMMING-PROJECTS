# Generated by Django 3.0.8 on 2020-08-10 13:47

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0037_auto_20200808_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='comment',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comm', to='auctions.AuctionItems'),
        ),
        migrations.AddField(
            model_name='comments',
            name='comment_user',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auctionitems',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 10, 13, 47, 29, 803148, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='closed_auctions',
            name='closed_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 10, 13, 47, 29, 806511, tzinfo=utc)),
        ),
    ]
