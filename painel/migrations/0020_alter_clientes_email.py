# Generated by Django 4.2.1 on 2023-05-26 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0019_clientes_senha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.TextField(default='', max_length=255, unique=True),
        ),
    ]
