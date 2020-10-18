# Generated by Django 3.0.8 on 2020-08-06 16:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20200806_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitems',
            name='category',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='auctionitems',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 6, 16, 46, 42, 403237, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='auctionitems',
            name='description',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]