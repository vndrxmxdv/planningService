# Generated by Django 3.2.8 on 2021-11-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities_board', '0012_auto_20211129_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userStatus',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=30, verbose_name='Никнейм'),
        ),
    ]
