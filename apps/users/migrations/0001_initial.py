# Generated by Django 3.0.7 on 2020-06-19 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('roles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=45, unique=True, verbose_name='cedula')),
                ('nombre', models.CharField(max_length=120, verbose_name='nombres')),
                ('apellido', models.CharField(max_length=120, verbose_name='apellidos')),
                ('direccion', models.CharField(max_length=500, verbose_name='direccion')),
                ('telefono', models.CharField(max_length=45, verbose_name='telefono')),
                ('date', models.DateField(verbose_name='fechaNacimiento')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('id_Socio', models.IntegerField(verbose_name='idSocio')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fechaInicio')),
                ('modificated', models.DateTimeField(auto_now=True, null=True, verbose_name='fechaFin')),
            ],
            options={
                'verbose_name': 'partner',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=45, unique=True, verbose_name='cedula')),
                ('nombre', models.CharField(max_length=120, verbose_name='nombres')),
                ('apellido', models.CharField(max_length=120, verbose_name='apellidos')),
                ('direccion', models.CharField(max_length=500, verbose_name='direccion')),
                ('telefono', models.CharField(max_length=45, verbose_name='telefono')),
                ('date', models.DateField(verbose_name='fechaNacimiento')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('id_Usuario', models.IntegerField(verbose_name='IdUsuario')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fechaInicio')),
                ('modificated', models.DateTimeField(auto_now=True, null=True, verbose_name='fechaFin')),
                ('id_role', models.ManyToManyField(to='roles.Role')),
            ],
            options={
                'verbose_name': 'user',
                'ordering': ['created_at'],
            },
        ),
    ]
