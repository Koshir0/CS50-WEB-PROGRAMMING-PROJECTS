# Generated by Django 3.1.1 on 2020-09-20 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0004_auto_20200919_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tools',
            name='is_rented',
            field=models.CharField(default='false', max_length=5, null=True),
        ),
    ]
