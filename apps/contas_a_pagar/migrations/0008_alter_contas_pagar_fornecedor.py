# Generated by Django 4.0.1 on 2022-05-29 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0013_alter_fornecedor_id'),
        ('contas_a_pagar', '0007_remove_contas_pagar_fornecedor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contas_pagar',
            name='fornecedor',
            field=models.ForeignKey(db_column='fornecedor', null=True, on_delete=django.db.models.deletion.CASCADE, to='fornecedor.fornecedor'),
        ),
    ]
