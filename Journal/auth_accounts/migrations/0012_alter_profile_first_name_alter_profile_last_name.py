# Generated by Django 4.0.3 on 2022-03-21 16:28

import Journal.validators.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_accounts', '0011_alter_profile_first_name_alter_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=25, validators=[Journal.validators.validators.name_only_letters_validator, Journal.validators.validators.min_length_validator]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=25, validators=[Journal.validators.validators.name_only_letters_validator, Journal.validators.validators.min_length_validator]),
        ),
    ]
