# Generated by Django 4.2.6 on 2023-10-10 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0004_produto_funcionario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='funcionario',
        ),
    ]
