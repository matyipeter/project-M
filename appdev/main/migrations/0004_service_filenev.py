# Generated by Django 5.0.1 on 2024-02-11 13:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_appointment_nap_neve"),
    ]

    operations = [
        migrations.AddField(
            model_name="service",
            name="filenev",
            field=models.CharField(default="macska.jpg", max_length=50),
        ),
    ]