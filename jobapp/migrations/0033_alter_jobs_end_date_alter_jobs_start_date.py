# Generated by Django 4.1.5 on 2023-07-19 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jobapp", "0032_apply_delete_appliedjobs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobs", name="end_date", field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="jobs", name="start_date", field=models.DateField(null=True),
        ),
    ]
