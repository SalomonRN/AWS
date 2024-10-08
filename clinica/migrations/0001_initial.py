# Generated by Django 5.1 on 2024-08-16 00:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('lastname', models.CharField(max_length=45)),
                ('specialization', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Doctor',
                'verbose_name_plural': 'Doctors',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Dueño',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('lastname', models.CharField(max_length=45)),
            ],
            options={
                'verbose_name': 'Dueño',
                'verbose_name_plural': 'Dueños',
                'db_table': 'TestDeDueño',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.dueño')),
            ],
            options={
                'verbose_name': 'Mascota',
                'verbose_name_plural': 'Mascotas',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=45)),
                ('date', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.doctor')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.dueño')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.mascota')),
            ],
            options={
                'verbose_name': 'Cita',
                'verbose_name_plural': 'Citas',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
