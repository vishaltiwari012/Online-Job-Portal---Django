# Generated by Django 4.1.5 on 2023-07-26 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobapp", "0038_apply_firmname"),
    ]

    operations = [
        migrations.RemoveField(model_name="apply", name="firmname",),
    ]
