# Generated by Django 4.1.2 on 2022-11-02 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0030_remove_seriesvideo_series_season_ind'),
    ]

    operations = [
        migrations.AddField(
            model_name='seriesvideo',
            name='series_season_ind',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='films.series'),
            preserve_default=False,
        ),
    ]
