# Generated by Django 4.1.1 on 2022-09-21 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
    ]
