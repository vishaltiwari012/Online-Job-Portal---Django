# Generated by Django 4.1.5 on 2023-07-19 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("jobapp", "0035_alter_jobs_end_date_alter_jobs_start_date"),
    ]

    operations = [
        migrations.AddField(
            model_name="jobseeker",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
