# Generated by Django 5.0 on 2023-12-25 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="avatar",
            field=models.ImageField(
                blank=True, default="image/default.png", upload_to="image/"
            ),
        ),
    ]
