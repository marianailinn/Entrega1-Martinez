# Generated by Django 4.0.3 on 2022-04-05 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_persona_delete_curso_delete_entregable_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.IntegerField(verbose_name='horarioEntrada')),
                ('salida', models.IntegerField(verbose_name='horarioSalida')),
            ],
        ),
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25, verbose_name='nombre')),
                ('stocknum', models.IntegerField(verbose_name='stocknum')),
                ('stock', models.CharField(max_length=30, verbose_name='stock')),
            ],
        ),
        migrations.AlterField(
            model_name='persona',
            name='fechaNac',
            field=models.DateField(blank=True, null=True, verbose_name='fechaNac'),
        ),
    ]