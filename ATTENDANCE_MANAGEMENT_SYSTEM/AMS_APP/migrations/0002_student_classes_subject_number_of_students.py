# Generated by Django 4.1.7 on 2023-11-08 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AMS_APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='classes',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subject',
            name='number_of_students',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
