# Generated by Django 3.2.8 on 2021-12-11 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formulas', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='slug',
        ),
    ]