# Generated by Django 4.1.2 on 2022-11-02 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0025_alter_seriesvideo_series_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seasons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_index', models.IntegerField(default=0, verbose_name='Номер сезона')),
                ('season_ind', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.series')),
            ],
        ),
        migrations.AlterField(
            model_name='seriesvideo',
            name='series_ind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.seasons'),
        ),
    ]
