# Generated by Django 5.1.5 on 2025-02-15 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="chatresponse",
            name="content",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
