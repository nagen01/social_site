# Generated by Django 2.1 on 2019-05-26 14:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190526_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 5, 26, 14, 10, 56, 110696, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2019, 5, 26, 14, 10, 56, 110696, tzinfo=utc)),
        ),
    ]
