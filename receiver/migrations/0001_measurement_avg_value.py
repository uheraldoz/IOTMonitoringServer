# Generated by Django 4.1.1 on 2022-09-19 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("receiver", "to_timescale"),
    ]

    operations = [
        migrations.AddField(
            model_name="measurement",
            name="avg_value",
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]