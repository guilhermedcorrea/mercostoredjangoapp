# Generated by Django 4.0.1 on 2022-01-30 21:32

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('idseller', models.IntegerField(primary_key=True, serialize=False)),
                ('sellerid', models.CharField(max_length=255)),
                ('sellername', models.CharField(max_length=255)),
                ('selleremail', models.CharField(max_length=255)),
                ('bitAtivo', models.BooleanField()),
                ('sellerresponsavel', models.CharField(max_length=255)),
                ('senha', models.CharField(max_length=255)),
                ('logoseller', models.CharField(max_length=255)),
                ('dataatualizado', models.DateField(default=datetime.datetime(2022, 1, 30, 21, 32, 18, 379501, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('idusuario', models.IntegerField(primary_key=True, serialize=False)),
                ('sellernome', models.CharField(max_length=255, null=True)),
                ('idseller', models.CharField(max_length=255, null=True)),
                ('nome', models.CharField(max_length=255, null=True)),
                ('email', models.CharField(max_length=255, null=True)),
                ('senha', models.CharField(max_length=255, null=True)),
                ('perfil', models.CharField(max_length=1000, null=True)),
                ('logoseller', models.CharField(max_length=1000, null=True)),
                ('ref_idseller', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('idproduto', models.IntegerField(primary_key=True, serialize=False)),
                ('idseller', models.IntegerField(null=True)),
                ('id_vtex', models.IntegerField(null=True)),
                ('referenciaseller', models.CharField(blank=True, max_length=255)),
                ('nomeseller', models.CharField(blank=True, max_length=255)),
                ('ref_ean', models.CharField(max_length=255, null=True)),
                ('ref_cod', models.CharField(max_length=255, null=True)),
                ('nome_produto', models.CharField(max_length=255, null=True)),
                ('imagem', models.CharField(max_length=255, null=True)),
                ('perfilprod', models.CharField(max_length=255, null=True)),
                ('perfilgoogle', models.CharField(max_length=1000, null=True)),
                ('marcaproduto', models.CharField(max_length=255, null=True)),
                ('preco_seller', models.FloatField(null=True)),
                ('diferenca_preco', models.FloatField(null=True)),
                ('bitAtivo', models.BooleanField()),
                ('sellermenorpreco', models.CharField(max_length=255, null=True)),
                ('menorpreco', models.FloatField(null=True)),
                ('sellermaiorpreco', models.CharField(max_length=255, null=True)),
                ('maiorpreco', models.FloatField(null=True)),
                ('idcategoriaproduto', models.CharField(max_length=255, null=True)),
                ('categoriaproduto', models.CharField(max_length=255, null=True)),
                ('dataatualizado', models.DateField(default=datetime.datetime(2022, 1, 30, 21, 32, 18, 379501, tzinfo=utc))),
                ('refidprodutos', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sellers.seller')),
            ],
        ),
        migrations.CreateModel(
            name='Googleshopping',
            fields=[
                ('googleid', models.IntegerField(primary_key=True, serialize=False)),
                ('eangoogle', models.CharField(max_length=255)),
                ('urlgoogle', models.CharField(max_length=100)),
                ('sellermen', models.CharField(max_length=255)),
                ('menorpreco', models.FloatField(blank=True, null=True)),
                ('sellermai', models.CharField(max_length=255)),
                ('maiorpreco', models.CharField(max_length=255)),
                ('bitAtivo', models.BooleanField()),
                ('dataatualizado', models.DateField(default=datetime.datetime(2022, 1, 30, 21, 32, 18, 395089, tzinfo=utc))),
                ('refgoogle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sellers.seller')),
            ],
        ),
        migrations.CreateModel(
            name='CategoriasProdutos',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('iddepartamento', models.IntegerField(null=True)),
                ('nomedepartamento', models.CharField(max_length=255, null=True)),
                ('idcategoria', models.IntegerField(null=True)),
                ('noemcategoria', models.CharField(max_length=255, null=True)),
                ('urlcategoria', models.CharField(max_length=1000, null=True)),
                ('nomecategoria', models.CharField(max_length=255, null=True)),
                ('refsprods', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sellers.produtos')),
            ],
        ),
    ]