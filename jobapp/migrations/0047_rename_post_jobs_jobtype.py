# Generated by Django 4.1.5 on 2023-07-26 06:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobapp", "0046_jobs_apply"),
    ]

    operations = [
        migrations.RenameField(model_name="jobs", old_name="post", new_name="jobtype",),
    ]
