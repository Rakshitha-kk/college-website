# Generated by Django 4.2 on 2023-06-05 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0014_alter_studentmark_s1"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentmark",
            name="s1",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="app1.student"
            ),
        ),
    ]
