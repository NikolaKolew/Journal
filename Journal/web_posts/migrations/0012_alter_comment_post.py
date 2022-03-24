# Generated by Django 4.0.3 on 2022-03-23 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web_posts', '0011_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='web_posts.post'),
        ),
    ]