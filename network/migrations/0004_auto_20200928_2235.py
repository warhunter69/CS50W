# Generated by Django 3.0.9 on 2020-09-28 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_auto_20200928_2202'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likes',
            new_name='likers',
        ),
    ]
