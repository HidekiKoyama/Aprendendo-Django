# Generated by Django 4.2.1 on 2023-05-25 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0003_alter_sexo_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sexo',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]
