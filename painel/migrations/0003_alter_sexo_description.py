# Generated by Django 4.2.1 on 2023-05-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('painel', '0002_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sexo',
            name='description',
            field=models.TextField(),
        ),
    ]