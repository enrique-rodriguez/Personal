# Generated by Django 3.2.5 on 2021-07-24 00:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_alter_messagemodel_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagemodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 7, 24, 0, 49, 46, 502344, tzinfo=utc), verbose_name='Created'),
            preserve_default=False,
        ),
    ]
