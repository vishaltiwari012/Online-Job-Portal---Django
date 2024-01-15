# Generated by Django 4.1.5 on 2023-07-19 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobapp", "0028_alter_jobs_end_date_alter_jobs_start_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="AppliedJobs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("empemailaddress", models.EmailField(max_length=50)),
                ("jobtitle", models.CharField(max_length=100)),
                ("post", models.CharField(max_length=50)),
                ("profile", models.FileField(null=True, upload_to="")),
                ("name", models.CharField(max_length=50)),
                ("gender", models.CharField(max_length=6)),
                ("address", models.TextField()),
                ("contactno", models.CharField(max_length=15)),
                ("emailaddress", models.EmailField(max_length=50)),
                ("dob", models.CharField(max_length=20)),
                ("qualification", models.CharField(max_length=100)),
                ("experience", models.CharField(max_length=20)),
                ("keyskills", models.TextField()),
                ("resume", models.FileField(null=True, upload_to="")),
                ("applydate", models.DateField()),
            ],
        ),
        migrations.DeleteModel(name="Apply",),
    ]