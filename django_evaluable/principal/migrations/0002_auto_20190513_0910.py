# Generated by Django 2.1.7 on 2019-05-13 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoNoticia',
            fields=[
                ('tipo', models.CharField(max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='noticia',
            name='tipoNoticia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.TipoNoticia'),
        ),
    ]
