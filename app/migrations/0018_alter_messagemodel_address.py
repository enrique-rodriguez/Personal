# Generated by Django 3.2.5 on 2021-07-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20210723_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='address',
            field=models.CharField(blank=True, max_length=254, verbose_name='Email'),
        ),
    ]
