# Generated by Django 4.2.1 on 2023-05-26 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0017_remove_clientes_senha_alter_clientes_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='id_cliente',
            field=models.ForeignKey(default=99999, on_delete=django.db.models.deletion.CASCADE, to='painel.clientes'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='painel.sexo'),
        ),
    ]
