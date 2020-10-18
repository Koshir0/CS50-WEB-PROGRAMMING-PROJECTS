# Generated by Django 3.0.8 on 2020-08-19 15:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0005_auto_20200816_1021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='new_post',
            new_name='post',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='by_user',
        ),
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.ManyToManyField(blank=True, related_name='commentpost', to='network.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.ManyToManyField(blank=True, related_name='commentuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 15, 45, 56, 835463, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 19, 15, 45, 56, 829966, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.ManyToManyField(blank=True, related_name='likepost', to='network.Post')),
                ('user_id', models.ManyToManyField(blank=True, related_name='likeuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FollowerId', models.ManyToManyField(blank=True, related_name='follower', to=settings.AUTH_USER_MODEL)),
                ('UserId', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
