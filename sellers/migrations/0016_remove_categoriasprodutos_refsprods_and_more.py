# Generated by Django 4.0.1 on 2022-01-31 07:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0015_alter_categoriasprodutos_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriasprodutos',
            name='refsprods',
        ),
        migrations.RemoveField(
            model_name='googleshopping',
            name='refgoogle',
        ),
        migrations.RemoveField(
            model_name='produtos',
            name='refidprodutos',
        ),
        migrations.AlterField(
            model_name='googleshopping',
            name='dataatualizado',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 31, 4, 16, 9, 692371), null=True),
        ),
        migrations.AlterField(
            model_name='produtos',
            name='dataatualizado',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 31, 4, 16, 9, 687371), null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='dataatualizado',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 1, 31, 4, 16, 9, 683371), null=True),
        ),
    ]
