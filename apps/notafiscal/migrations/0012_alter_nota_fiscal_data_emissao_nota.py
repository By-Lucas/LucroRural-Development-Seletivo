# Generated by Django 4.0.1 on 2022-05-29 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notafiscal', '0011_alter_nota_fiscal_data_emissao_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota_fiscal',
            name='data_emissao_nota',
            field=models.DateField(verbose_name='%d/%m/%Y'),
        ),
    ]
