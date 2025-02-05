# Generated by Django 4.2 on 2025-02-05 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produs', '0015_remove_comanda_client_remove_comanda_produse_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImaginiProdus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagine', models.ImageField(blank=True, null=True, upload_to='produse/')),
                ('produs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagini', to='produs.produs')),
            ],
        ),
    ]
