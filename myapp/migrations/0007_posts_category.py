# Generated by Django 4.2.13 on 2024-06-16 19:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_сategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='myapp.category'),
        ),
    ]
