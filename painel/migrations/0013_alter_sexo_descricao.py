# Generated by Django 4.2.1 on 2023-05-26 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0012_rename_description_sexo_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sexo',
            name='descricao',
            field=models.TextField(max_length=50),
        ),
    ]
