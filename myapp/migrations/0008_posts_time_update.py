# Generated by Django 4.2.13 on 2024-06-17 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_posts_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='time_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
