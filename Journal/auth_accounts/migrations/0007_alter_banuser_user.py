# Generated by Django 4.0.3 on 2022-03-17 09:17

import annoying.fields
from django.conf import settings
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_accounts', '0006_banuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banuser',
            name='user',
            field=annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]