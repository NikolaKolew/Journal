# Generated by Django 4.0.3 on 2022-03-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0002_alter_journal_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
