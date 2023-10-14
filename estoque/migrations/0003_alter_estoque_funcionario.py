# Generated by Django 4.2.6 on 2023-10-13 05:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('estoque', '0002_alter_estoque_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estoque',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
