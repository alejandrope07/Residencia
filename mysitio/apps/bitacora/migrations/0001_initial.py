# Generated by Django 2.1.7 on 2019-04-17 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('modelo', models.CharField(max_length=50)),
                ('serie', models.CharField(max_length=15)),
                ('area', models.CharField(max_length=30)),
                ('pieza_cambiada', models.CharField(max_length=50)),
                ('serie_piezan', models.CharField(max_length=30)),
                ('motivo', models.CharField(max_length=70)),
            ],
        ),
    ]
