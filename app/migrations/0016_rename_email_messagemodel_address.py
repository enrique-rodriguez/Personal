# Generated by Django 3.2.5 on 2021-07-18 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_messagemodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagemodel',
            old_name='email',
            new_name='address',
        ),
    ]
