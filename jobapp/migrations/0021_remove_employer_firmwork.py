# Generated by Django 4.1.5 on 2023-07-17 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobapp", "0020_employer_photo"),
    ]

    operations = [
        migrations.RemoveField(model_name="employer", name="firmwork",),
    ]