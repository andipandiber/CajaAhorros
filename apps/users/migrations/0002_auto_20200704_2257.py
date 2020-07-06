# Generated by Django 3.0.7 on 2020-07-05 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='IDCard',
            field=models.CharField(blank=True, max_length=45, unique=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=500, verbose_name='direccion'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateField(blank=True, verbose_name='fechaNacimiento'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='apellidos'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(blank=True, max_length=120, verbose_name='nombres'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=45, verbose_name='telefono'),
        ),
    ]