# Generated by Django 3.0.7 on 2020-06-19 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('transaccion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id_cuenta', models.AutoField(primary_key=True, serialize=False, verbose_name='idCuenta')),
                ('fecha_apertura', models.DateField(verbose_name='fechaApertura')),
                ('id_Socio', models.ManyToManyField(to='users.Socio')),
                ('id_transaccion', models.ManyToManyField(to='transaccion.Transaccion')),
            ],
            options={
                'verbose_name': 'accounts',
            },
        ),
    ]
