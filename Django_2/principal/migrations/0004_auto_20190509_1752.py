# Generated by Django 2.1.7 on 2019-05-09 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20190507_1248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pelicula',
            old_name='imbdID',
            new_name='imdbID',
        ),
        migrations.RenameField(
            model_name='pelicula',
            old_name='thdbID',
            new_name='tmbdID',
        ),
    ]