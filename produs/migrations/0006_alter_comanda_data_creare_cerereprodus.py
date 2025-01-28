# Generated by Django 4.2 on 2025-01-28 17:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('produs', '0005_category_alter_comanda_data_creare'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comanda',
            name='data_creare',
            field=models.DateTimeField(default=datetime.datetime(2025, 1, 28, 19, 10, 1, 258994)),
        ),
        migrations.CreateModel(
            name='CerereProdus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantitate', models.PositiveIntegerField()),
                ('data_cerere', models.DateTimeField(auto_now_add=True)),
                ('produs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produs.produs')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
