# Generated by Django 4.0.3 on 2022-03-21 16:39

import Journal.validators.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0007_alter_journal_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='title',
            field=models.CharField(max_length=50, validators=[Journal.validators.validators.min_length_validator]),
        ),
    ]
