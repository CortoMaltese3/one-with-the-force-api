# Generated by Django 4.2.16 on 2024-11-03 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="starship",
            name="pilots",
        ),
        migrations.AddField(
            model_name="starship",
            name="pilots",
            field=models.ManyToManyField(
                related_name="piloting_starships", to="api.character"
            ),
        ),
    ]
