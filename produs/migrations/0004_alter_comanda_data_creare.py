# Generated by Django 5.1.5 on 2025-01-27 18:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produs', '0003_comanda_client_comanda_data_creare_comanda_produse_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data_creare',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 27, 20, 33, 33, 320156)),
        ),
    ]
