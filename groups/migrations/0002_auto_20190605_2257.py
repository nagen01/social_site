# Generated by Django 2.1 on 2019-06-05 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupmember',
            name='group',
            field=models.ForeignKey(on_delete='CASCADE', related_name='membership', to='groups.Group'),
        ),
    ]
