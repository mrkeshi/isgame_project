# Generated by Django 3.2.18 on 2024-02-07 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_downloadbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='downloadbox',
            name='Post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Post.articles'),
            preserve_default=False,
        ),
    ]