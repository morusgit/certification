# Generated by Django 4.2.13 on 2024-05-08 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chain_stores', '0005_alter_supplier_parent_alter_supplier_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplier',
            name='level',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='lft',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='rght',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='tree_id',
        ),
        migrations.AlterField(
            model_name='supplier',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='chain_stores.supplier', verbose_name='Поставщик'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='type',
            field=models.CharField(choices=[('Завод', 'Zavod'), ('ИП', 'Ip'), ('Розничная сеть', 'Rc')], default='Завод', verbose_name='Тип'),
        ),
    ]
