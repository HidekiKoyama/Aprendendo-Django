# Generated by Django 4.2.1 on 2023-05-26 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0025_alter_clientes_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id_cliente',
            field=models.IntegerField(),
        ),
    ]
