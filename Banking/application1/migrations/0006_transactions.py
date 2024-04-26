# Generated by Django 5.0 on 2024-04-03 09:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application1', '0005_remove_account_currentbalance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=20)),
                ('Transaction_type', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Amount', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]