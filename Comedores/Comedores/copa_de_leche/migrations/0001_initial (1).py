# Generated by Django 3.0.6 on 2020-06-17 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='escuela',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('establecimiento', models.CharField(max_length=60)),
                ('cue', models.CharField(max_length=9)),
                ('delegacion', models.CharField(max_length=30)),
                ('localidad', models.CharField(max_length=30)),
                ('nivel', models.CharField(max_length=20)),
                ('modalidad', models.CharField(max_length=20)),
                ('nro_cuenta', models.CharField(max_length=8)),
                ('responsable', models.CharField(max_length=30)),
                ('responsable_dni', models.CharField(max_length=10)),
                ('sub_responsable', models.CharField(max_length=30)),
                ('sub_responsable_dni', models.CharField(max_length=10)),
                ('reso', models.CharField(max_length=6)),
            ],
        ),
    ]
