# Generated by Django 4.2.5 on 2023-10-04 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstoqueEntrada',
            fields=[
            ],
            options={
                'verbose_name': 'estoque entrada',
                'verbose_name_plural': 'estoque entrada',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('estoque.estoque',),
        ),
        migrations.CreateModel(
            name='EstoqueSaida',
            fields=[
            ],
            options={
                'verbose_name': 'estoque saída',
                'verbose_name_plural': 'estoque saída',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('estoque.estoque',),
        ),
        migrations.AlterField(
            model_name='estoqueitens',
            name='saldo',
            field=models.PositiveIntegerField(),
        ),
    ]
