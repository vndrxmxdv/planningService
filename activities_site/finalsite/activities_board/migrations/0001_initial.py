# Generated by Django 3.2.8 on 2021-10-27 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Имя')),
                ('surename', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30, verbose_name='Пароль')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('start_time', models.DateTimeField(db_index=True, verbose_name='Время начала')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='Время окончания')),
                ('location', models.TextField(blank=True, null=True, verbose_name='Место проведения')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Время публикации')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='activities_board.category', verbose_name='Категория')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='activities_board.user', verbose_name='Организатор')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('body', models.TextField()),
                ('published', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='activities_board.event')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['published'],
            },
        ),
    ]
