# Generated by Django 3.0.8 on 2020-08-05 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20200805_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionitems',
            name='image',
            field=models.CharField(default=2, max_length=400),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='auctionitems',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 5, 12, 2, 41, 579976)),
        ),
    ]
