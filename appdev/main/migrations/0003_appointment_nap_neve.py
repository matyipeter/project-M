# Generated by Django 5.0.1 on 2024-02-10 09:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_service"),
    ]

    operations = [
        migrations.AddField(
            model_name="appointment",
            name="nap_neve",
            field=models.CharField(default="hetfo", max_length=20),
        ),
    ]
