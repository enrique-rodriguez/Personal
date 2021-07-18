# Generated by Django 3.2.5 on 2021-07-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210716_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLinkModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('name', models.CharField(max_length=20)),
                ('icon', models.CharField(max_length=100)),
            ],
        ),
    ]
