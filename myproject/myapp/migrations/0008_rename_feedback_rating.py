# Generated by Django 5.0 on 2024-04-26 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_user_feedback_user_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Feedback',
            new_name='Rating',
        ),
    ]