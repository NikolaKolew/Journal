# Generated by Django 4.0.3 on 2022-03-14 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_accounts', '0004_profile_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
