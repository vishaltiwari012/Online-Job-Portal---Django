# Generated by Django 4.1.5 on 2023-07-15 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobapp", "0013_employer_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="employer", old_name="image", new_name="image1",
        ),
    ]
