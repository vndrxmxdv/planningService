# Generated by Django 3.2.8 on 2021-11-24 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activities_board', '0009_rename_title_event_eventname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end_time',
            new_name='endTime',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='type',
            new_name='eventFormat',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='start_time',
            new_name='startTime',
        ),
    ]
