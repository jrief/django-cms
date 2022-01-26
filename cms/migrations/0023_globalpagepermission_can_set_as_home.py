# Generated by Django 3.2 on 2022-01-25 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalpagepermission',
            name='can_set_as_home',
            field=models.BooleanField(default=False, help_text='Can set first tier pages as home page', verbose_name='Can set as home'),
        ),
    ]
