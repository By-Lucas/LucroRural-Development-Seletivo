# Generated by Django 4.0.1 on 2022-05-26 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notafiscal', '0004_nota_fiscal_fornecedor_alter_nota_fiscal_categoria_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nota_fiscal',
            options={'verbose_name': 'Nota_Fiscal', 'verbose_name_plural': 'Notas_Fiscais'},
        ),
        migrations.AlterModelTable(
            name='nota_fiscal',
            table='Nota_Fiscal',
        ),
    ]
