# Generated by Django 4.1.5 on 2023-07-18 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobapp", "0027_alter_jobs_end_date_alter_jobs_start_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobs",
            name="end_date",
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="jobs",
            name="start_date",
            field=models.CharField(max_length=50, null=True),
        ),
    ]