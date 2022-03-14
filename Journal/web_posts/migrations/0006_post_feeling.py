# Generated by Django 4.0.3 on 2022-03-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_posts', '0005_remove_comment_user_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='feeling',
            field=models.CharField(blank=True, choices=[('happy', 'happy'), ('excited', 'excited'), ('motivated', 'motivated'), ('thankful', 'thankful'), ('grateful', 'grateful')], max_length=9, null=True),
        ),
    ]