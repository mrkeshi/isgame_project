# Generated by Django 3.2.18 on 2024-03-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteModule', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urladbaner', models.URLField(blank=True, null=True)),
                ('imageurladbaner', models.URLField(blank=True, null=True)),
                ('statusadbaner', models.BooleanField(default=False)),
            ],
        ),
    ]
