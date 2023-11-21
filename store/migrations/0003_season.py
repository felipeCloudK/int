# Generated by Django 3.1.13 on 2023-09-26 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_buyer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('serial', models.CharField(max_length=120, unique=True)),
                ('quantity', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=220)),
                ('created_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
