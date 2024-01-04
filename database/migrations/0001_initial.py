# Generated by Django 4.2.7 on 2024-01-04 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50, verbose_name='Локация')),
                ('subdivision', models.CharField(max_length=50, verbose_name='Подразделение')),
                ('department', models.CharField(max_length=50, verbose_name='Отдел')),
                ('group', models.CharField(max_length=50, verbose_name='Группа')),
                ('position', models.CharField(max_length=50, verbose_name='Должность')),
                ('name', models.CharField(max_length=50, verbose_name='ФИО')),
                ('kindofwork', models.CharField(max_length=50, verbose_name='Тип работы')),
            ],
        ),
    ]
