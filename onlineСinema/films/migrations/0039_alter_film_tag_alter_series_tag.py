# Generated by Django 4.1.2 on 2022-11-05 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0038_alter_series_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='tag',
            field=models.CharField(choices=[('1', 'Фильм'), ('2', 'Мультфильм')], default='Фильм', max_length=1, verbose_name='Тэг'),
        ),
        migrations.AlterField(
            model_name='series',
            name='tag',
            field=models.CharField(choices=[('1', 'Сериал'), ('2', 'Мультсериал')], default='Сериал', max_length=1, verbose_name='Тэг'),
        ),
    ]
