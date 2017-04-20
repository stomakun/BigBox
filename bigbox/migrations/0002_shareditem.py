# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-19 19:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bigbox', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(db_index=True, max_length=18)),
                ('name', models.TextField()),
                ('is_public', models.BooleanField()),
                ('is_folder', models.BooleanField()),
                ('item_id', models.TextField()),
                ('created_at', models.DateTimeField()),
                ('view_count', models.IntegerField()),
                ('download_count', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bigbox.StorageAccount')),
                ('readable_users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]