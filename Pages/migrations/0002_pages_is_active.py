# Generated by Django 3.2.18 on 2024-02-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pages',
            name='is_active',
            field=models.BooleanField(choices=[(False, 'پیش نویس'), (True, 'نمایش عمومی')], default=False),
        ),
    ]
