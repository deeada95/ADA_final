# Generated by Django 4.2 on 2025-01-28 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produs', '0004_alter_comanda_data_creare'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='comanda',
            name='data_creare',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 28, 18, 22, 30, 971504)),
        ),
    ]
