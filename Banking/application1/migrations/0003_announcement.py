# Generated by Django 5.0 on 2024-03-28 07:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0002_account_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('title', models.CharField(max_length=25)),
                ('body', models.CharField(max_length=225)),
                ('last_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
