# Generated by Django 4.1.5 on 2023-07-17 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobapp", "0019_alter_jobs_end_date_alter_jobs_start_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="employer",
            name="photo",
            field=models.FileField(null=True, upload_to=""),
        ),
    ]
