# Generated by Django 3.2.6 on 2021-08-20 12:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_auto_20210820_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expired',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 22, 12, 59, 11, 70945, tzinfo=utc)),
        ),
    ]