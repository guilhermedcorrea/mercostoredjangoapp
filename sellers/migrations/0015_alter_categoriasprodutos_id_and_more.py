# Generated by Django 4.0.1 on 2022-01-31 05:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0014_alter_categoriasprodutos_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriasprodutos',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='googleshopping',
            name='dataatualizado',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 31, 2, 14, 46, 17167), null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='dataatualizado',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 31, 2, 14, 45, 977167), null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='idproduto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='seller',
            name='dataatualizado',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 31, 2, 14, 45, 961164), null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='idseller',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='idusuario',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
