# Generated by Django 5.0 on 2023-12-24 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typeservice',
            name='user',
        ),
    ]