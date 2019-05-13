# Generated by Django 2.1.7 on 2019-05-13 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('nombre', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('apellidos', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Diario',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('pais', models.CharField(max_length=20)),
                ('idioma', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('titular', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('fechaNoticia', models.DateField()),
                ('resumen', models.TextField()),
                ('tipoNoticia', models.CharField(choices=[('Deportes', 'Deportes'), ('Cultura', 'Cultura'), ('Politica', 'Politica'), ('Economia', 'Economia'), ('Actualidad', 'Actualidad')], max_length=15)),
                ('autores', models.ManyToManyField(to='principal.Autor')),
                ('diario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.Diario')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nombreUsuario', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('passwd', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=20)),
                ('apellidos', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='noticia',
            name='usuarios',
            field=models.ManyToManyField(to='principal.Usuario'),
        ),
    ]
