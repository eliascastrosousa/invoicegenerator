# Generated by Django 4.2.2 on 2023-06-17 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_endereco_salario'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Endereco',
            new_name='AdditionalData',
        ),
    ]
