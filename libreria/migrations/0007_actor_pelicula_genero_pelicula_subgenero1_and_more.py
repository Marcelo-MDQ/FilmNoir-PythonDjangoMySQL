# Generated by Django 4.1 on 2023-02-14 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0006_pelicula_imagenlocal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombreactor', models.CharField(max_length=100)),
                ('imagenactor', models.ImageField(null=True, upload_to='libreria/static/img', verbose_name='ImagenActor')),
            ],
        ),
        migrations.AddField(
            model_name='pelicula',
            name='genero',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='subgenero1',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='subgenero2',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='subgenero3',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='imagenlocal',
            field=models.ImageField(null=True, upload_to='libreria/static/img', verbose_name='ImagenLocal'),
        ),
    ]