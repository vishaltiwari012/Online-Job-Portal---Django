# Generated by Django 4.1 on 2022-09-05 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("jobapp", "0009_remove_feedback_fb_id_feedback_id"),
    ]

    operations = [
        migrations.RenameField(model_name="feedback", old_name="rate", new_name="rat",),
    ]