# Generated by Django 4.0.3 on 2022-03-14 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_posts', '0009_remove_post_like_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]