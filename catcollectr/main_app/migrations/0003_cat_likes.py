# Generated by Django 2.0.5 on 2018-05-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cat_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
