# Generated by Django 4.0.1 on 2022-01-31 04:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0013_alter_categoriasprodutos_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriasprodutos',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='googleshopping',
            name='dataatualizado',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 31, 1, 57, 54, 474229), null=True),
        ),
        migrations.AlterField(
            model_name='googleshopping',
            name='googleid',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='dataatualizado',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 31, 1, 57, 54, 472229), null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='idproduto',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='seller',
            name='dataatualizado',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 31, 1, 57, 54, 470228), null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='idseller',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='idusuario',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
