# Generated by Django 3.2.9 on 2021-12-07 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_rename_edad_usuarios_dni'),
    ]

    operations = [
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('actividad', models.CharField(max_length=20)),
                ('fecha_turno', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='InformacionCliente',
        ),
    ]