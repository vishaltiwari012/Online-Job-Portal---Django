# Generated by Django 4.1.5 on 2023-07-19 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobapp", "0034_alter_jobs_end_date_alter_jobs_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobs", name="end_date", field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="jobs", name="start_date", field=models.DateField(null=True),
        ),
    ]
