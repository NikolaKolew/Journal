# Generated by Django 4.0.3 on 2022-03-10 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0004_journal_picture_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]