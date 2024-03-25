# Generated by Django 3.2.18 on 2024-03-25 11:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SiteModule', '0003_widget'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicsettings',
            name='information',
            field=models.TextField(default='بدون توضیحات'),
        ),
        migrations.AlterField(
            model_name='socialmedialink',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='social', to=settings.AUTH_USER_MODEL),
        ),
    ]