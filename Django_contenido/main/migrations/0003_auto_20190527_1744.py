# Generated by Django 2.1.7 on 2019-05-27 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190527_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarioetiquetaartista',
            name='artista',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Artista'),
        ),
    ]