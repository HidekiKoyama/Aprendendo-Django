# Generated by Django 4.2.1 on 2023-05-26 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0022_alter_clientes_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='sexo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='painel.sexo', unique=True),
        ),
    ]
