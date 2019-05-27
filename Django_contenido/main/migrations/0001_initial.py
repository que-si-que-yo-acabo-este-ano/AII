# Generated by Django 2.1.7 on 2019-05-27 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('idArtista', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('url', models.URLField()),
                ('pictureUrl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('idTag', models.IntegerField(primary_key=True, serialize=False)),
                ('tagValue', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioArtista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiempoEscucha', models.IntegerField()),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Artista')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioEtiquetaArtista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.IntegerField()),
                ('mes', models.IntegerField()),
                ('anyo', models.IntegerField()),
                ('artista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Artista')),
                ('etiqueta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Etiqueta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Usuario')),
            ],
        ),
    ]
