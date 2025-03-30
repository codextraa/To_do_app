# Generated by Django 5.1.6 on 2025-03-26 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core_db", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BgImage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="others/bg-white.jpg", upload_to="others/"
                    ),
                ),
            ],
        ),
    ]
