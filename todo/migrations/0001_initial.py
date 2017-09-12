# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 14:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_text', models.CharField(max_length=300)),
                ('complete', models.BooleanField(default=False)),
                ('assigned_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(default='', blank=True, null=True)),
                ('completed_date', models.DateField(default='', blank=True, null=True)),
            ],
        ),
    ]
