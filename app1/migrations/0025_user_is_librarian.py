# Generated by Django 4.2 on 2023-06-27 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0024_appliedinfo"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_librarian",
            field=models.BooleanField(default=False),
        ),
    ]