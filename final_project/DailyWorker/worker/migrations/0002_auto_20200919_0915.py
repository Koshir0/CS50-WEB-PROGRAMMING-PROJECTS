# Generated by Django 3.1.1 on 2020-09-19 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
