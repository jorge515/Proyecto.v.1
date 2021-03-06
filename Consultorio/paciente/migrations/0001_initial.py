# Generated by Django 3.1.3 on 2020-11-24 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=30)),
                ('apellido', models.TextField()),
            ],
            options={
                'verbose_name': 'medico ',
                'verbose_name_plural': 'medicos',
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('historia', models.TextField(verbose_name='Historial')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'paciente',
                'verbose_name_plural': 'pacientes',
            },
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('hora', models.TimeField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.medico')),
                ('paciente', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente')),
            ],
            options={
                'verbose_name': 'turno',
                'verbose_name_plural': 'turnos',
            },
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(max_length=30)),
                ('medico', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='paciente.medico')),
                ('pacient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente')),
            ],
            options={
                'verbose_name': 'historial',
                'verbose_name_plural': 'historial',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=30)),
                ('turno', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='paciente.turno')),
            ],
            options={
                'verbose_name': 'estado',
                'verbose_name_plural': 'estados',
            },
        ),
    ]
