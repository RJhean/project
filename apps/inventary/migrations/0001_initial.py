# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-08-05 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cap_disco', models.IntegerField()),
                ('memoria', models.IntegerField()),
                ('procesador', models.CharField(max_length=100)),
                ('monitor', models.CharField(max_length=100)),
                ('perifericos', models.TextField(max_length=200)),
            ],
            options={
                'verbose_name': 'Computer',
                'verbose_name_plural': 'Computers',
            },
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Lugar',
                'verbose_name_plural': 'Lugares',
            },
        ),
        migrations.CreateModel(
            name='Oficina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventary.Lugar')),
            ],
            options={
                'verbose_name': 'Oficina',
                'verbose_name_plural': 'Oficinas',
            },
        ),
        migrations.AddField(
            model_name='computer',
            name='oficina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventary.Oficina'),
        ),
    ]
