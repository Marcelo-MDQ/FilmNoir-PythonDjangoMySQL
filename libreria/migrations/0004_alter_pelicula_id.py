# Generated by Django 4.1 on 2022-11-27 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0003_alter_pelicula_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
