# Generated by Django 2.1.7 on 2019-06-04 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_character_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='subclass',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Subclass'),
        ),
    ]
