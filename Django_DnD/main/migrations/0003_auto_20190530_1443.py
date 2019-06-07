# Generated by Django 2.1.7 on 2019-05-30 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190522_2145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name_plural': 'Classes'},
        ),
        migrations.AlterModelOptions(
            name='subclass',
            options={'verbose_name_plural': 'Subclasses'},
        ),
        migrations.RemoveField(
            model_name='spell',
            name='classCharacter',
        ),
        migrations.AddField(
            model_name='spell',
            name='classCharacter',
            field=models.ManyToManyField(to='main.Class'),
        ),
        migrations.RemoveField(
            model_name='spell',
            name='subclass',
        ),
        migrations.AddField(
            model_name='spell',
            name='subclass',
            field=models.ManyToManyField(to='main.Subclass'),
        ),
    ]