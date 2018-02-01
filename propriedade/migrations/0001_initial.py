# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-02-01 11:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Propriedade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('tipoPropriedade', models.IntegerField(choices=[(1, 'Apartamento'), (2, 'Casa'), (3, 'Comercio')], default=1, verbose_name='Tipo Propriedade')),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=150, verbose_name='Logradouro')),
                ('numero', models.IntegerField()),
                ('complemento', models.CharField(blank=True, max_length=150, null=True, verbose_name='Complemento')),
                ('bairro', models.CharField(max_length=30, verbose_name='Bairro')),
                ('cidade', models.CharField(max_length=30, verbose_name='Cidade')),
                ('estado', models.CharField(max_length=2, verbose_name='Estado')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa')),
            ],
        ),
    ]
