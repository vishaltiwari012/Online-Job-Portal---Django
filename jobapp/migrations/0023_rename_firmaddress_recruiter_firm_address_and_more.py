# Generated by Django 4.1.5 on 2023-07-18 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobapp", "0022_rename_employer_recruiter"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recruiter", old_name="firmaddress", new_name="firm_address",
        ),
        migrations.RenameField(
            model_name="recruiter", old_name="firmname", new_name="firm_name",
        ),
    ]
