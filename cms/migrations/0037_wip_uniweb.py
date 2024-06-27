# Generated by Django 4.2.13 on 2024-06-27 09:01

from django.db import migrations, models
import django.db.models.functions.text


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0035_auto_20230822_2208_squashed_0036_auto_20240311_1028'),
    ]

    operations_dummy = [
        migrations.AddField(
            model_name='globalpagepermission',
            name='can_set_as_home',
            field=models.BooleanField(default=False, help_text='can set first tier pages as home page', verbose_name='can set as home'),
        ),
        migrations.AlterField(
            model_name='pagecontent',
            name='in_navigation',
            field=models.BooleanField(db_index=True, default=False, verbose_name='in navigation'),
        ),
        migrations.AddConstraint(
            model_name='pageurl',
            constraint=models.CheckConstraint(check=models.Q(('slug', django.db.models.functions.text.Lower(models.F('slug')))), name='check_slug_lowercase'),
        ),
        migrations.AddConstraint(
            model_name='pageurl',
            constraint=models.UniqueConstraint(django.db.models.functions.text.Lower('path'), models.F('language'), name='unique_together_path_language'),
        ),
        migrations.AddConstraint(
            model_name='pageurl',
            constraint=models.UniqueConstraint(fields=('page', 'language'), name='unique_together_page_language'),
        ),
        migrations.AddConstraint(
            model_name='placeholder',
            constraint=models.UniqueConstraint(fields=('content_type', 'object_id', 'slot'), name='cms_placeholder_unique'),
        ),
    ]
    operations = []
