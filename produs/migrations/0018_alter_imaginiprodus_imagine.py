# Generated by Django 4.2 on 2025-02-05 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produs', '0017_alter_imaginiprodus_imagine'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imaginiprodus',
            name='imagine',
            field=models.ImageField(upload_to='produse_imagini'),
        ),
    ]
