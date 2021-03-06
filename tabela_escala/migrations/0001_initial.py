# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 02:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Escala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '17'), ('19', '17'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')], max_length=2)),
                ('mes', models.CharField(choices=[('JAN', 'Janeiro'), ('FEV', 'Fevereiro'), ('MAR', 'Marco'), ('ABR', 'Abril'), ('MAI', 'Maio'), ('JUN', 'Junho'), ('JUL', 'Julho'), ('AGO', 'Agosto'), ('SET', 'Setembro'), ('OUT', 'Outubro'), ('NOV', 'Novembro'), ('DEZ', 'Dezembro')], max_length=3)),
                ('analista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analistas', to='tabela_escala.Analista')),
                ('ano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anos', to='tabela_escala.Ano')),
            ],
        ),
    ]
