# Generated by Django 4.1.5 on 2023-07-26 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobapp", "0037_remove_jobseeker_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="apply",
            name="firmname",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
