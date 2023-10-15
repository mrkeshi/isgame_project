# Generated by Django 4.1.6 on 2023-03-21 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_alter_articletags_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategories',
            name='url',
            field=models.TextField(unique=True, verbose_name='آدرس دسته بندی'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='url',
            field=models.TextField(verbose_name='آدرس پست'),
        ),
        migrations.AlterField(
            model_name='articletags',
            name='url',
            field=models.TextField(unique=True, verbose_name='آدرس تگ'),
        ),
    ]
