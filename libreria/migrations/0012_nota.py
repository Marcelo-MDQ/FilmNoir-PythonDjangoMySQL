# Generated by Django 4.1 on 2023-03-30 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0011_alter_pelicula_resenia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100)),
                ('enlace', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100)),
                ('textocorto', models.TextField(blank=True, default='', null=True, verbose_name='TextoCorto')),
            ],
        ),
    ]
