# Generated by Django 4.0.3 on 2022-03-11 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0005_alter_journal_picture_alter_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='AppUser',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]