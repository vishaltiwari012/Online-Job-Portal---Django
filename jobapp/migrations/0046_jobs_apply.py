# Generated by Django 4.1.5 on 2023-07-26 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("jobapp", "0045_remove_jobs_employer_delete_apply_delete_jobs"),
    ]

    operations = [
        migrations.CreateModel(
            name="Jobs",
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
                ("firmname", models.CharField(max_length=100)),
                ("start_date", models.DateField(null=True)),
                ("end_date", models.DateField(null=True)),
                ("jobtitle", models.CharField(max_length=100)),
                ("img", models.FileField(null=True, upload_to="")),
                ("post", models.CharField(max_length=50)),
                ("jobdesc", models.TextField()),
                ("qualification", models.CharField(max_length=100)),
                ("experience", models.CharField(max_length=20)),
                ("location", models.CharField(max_length=100)),
                ("salarypa", models.IntegerField()),
                ("skills", models.CharField(max_length=100, null=True)),
                ("posteddate", models.CharField(max_length=30)),
                ("emailaddress", models.EmailField(max_length=50)),
                (
                    "employer",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jobapp.recruiter",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Apply",
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
                ("empemailaddress", models.EmailField(max_length=50, null=True)),
                ("resume", models.FileField(null=True, upload_to="")),
                ("applydate", models.DateField()),
                (
                    "job",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="jobapp.jobs"
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jobapp.jobseeker",
                    ),
                ),
            ],
        ),
    ]
