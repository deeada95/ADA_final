# Generated by Django 4.2 on 2025-02-12 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produs', '0025_alter_produs_descriere'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('mesaj', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
