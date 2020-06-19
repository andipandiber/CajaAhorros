# Generated by Django 3.0.7 on 2020-06-19 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('idSolicitud', models.AutoField(primary_key=True, serialize=False, verbose_name='idSolicitud')),
                ('fecha', models.DateField(verbose_name='fechaSolicitud')),
                ('idSocio', models.ManyToManyField(to='users.Socio')),
                ('idUsuario', models.ManyToManyField(to='users.Usuario')),
            ],
            options={
                'verbose_name': 'requests',
            },
        ),
    ]
