# Generated by Django 3.2.18 on 2024-02-04 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='incorrect_attempts',
            name='is_checked',
            field=models.BooleanField(default=False),
        ),
    ]
