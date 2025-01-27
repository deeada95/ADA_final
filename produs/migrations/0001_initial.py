# Generated by Django 5.1.5 on 2025-01-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenume', models.CharField(max_length=100)),
                ('nume', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefon', models.CharField(max_length=10)),
                ('adresa', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Produs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=100)),
                ('descriere', models.TextField()),
                ('pret', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]