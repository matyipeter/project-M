# Generated by Django 5.0.1 on 2024-02-21 13:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0004_service_filenev"),
    ]

    operations = [
        migrations.CreateModel(
            name="Message",
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
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("message", models.TextField(max_length=5000)),
            ],
        ),
    ]