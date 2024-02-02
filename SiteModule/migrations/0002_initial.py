# Generated by Django 3.2.18 on 2024-01-31 14:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SiteModule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmedialink',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='publicsettings',
            name='socialLinks',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SiteModule.socialmedialink'),
        ),
    ]