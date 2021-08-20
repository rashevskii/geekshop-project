# Generated by Django 3.2.6 on 2021-08-20 13:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_alter_shopuser_activation_key_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expired',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 22, 13, 34, 27, 388202, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(default=18, verbose_name='возраст'),
        ),
    ]