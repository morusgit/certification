# Generated by Django 5.0.3 on 2024-05-08 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chain_stores', '0014_alter_supplier_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='type',
            field=models.CharField(choices=[('Завод', 'Zavod'), ('ИП', 'Ip'), ('Розничная сеть', 'Rc')], default='Завод', verbose_name='Тип'),
        ),
    ]
