# Generated by Django 3.2.5 on 2021-08-24 07:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_auto_20210822_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expired',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 26, 7, 51, 40, 108287, tzinfo=utc)),
        ),
    ]
