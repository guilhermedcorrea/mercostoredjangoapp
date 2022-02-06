# Generated by Django 4.0.1 on 2022-01-31 03:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0004_alter_googleshopping_dataatualizado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriasprodutos',
            name='noemcategoria',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='categoriasprodutos',
            name='nomecategoria',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='categoriasprodutos',
            name='nomedepartamento',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='categoriasprodutos',
            name='urlcategoria',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='googleshopping',
            name='dataatualizado',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 31, 0, 45, 16, 129406), null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='categoriaproduto',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='dataatualizado',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 31, 0, 45, 16, 113405), null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='diferenca_preco',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='id_vtex',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='idcategoriaproduto',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='idseller',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='imagem',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='marcaproduto',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='nome_produto',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='perfilgoogle',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='perfilprod',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='preco_seller',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='ref_cod',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='ref_ean',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='sellermaiorpreco',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='sellermenorpreco',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='dataatualizado',
            field=models.DateField(default=datetime.datetime(2022, 1, 31, 0, 45, 16, 97407)),
        ),
    ]