# Generated by Django 4.2.2 on 2023-06-13 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=100)),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('cep', models.CharField(max_length=50)),
                ('logradouro', models.CharField(max_length=20)),
                ('numero', models.CharField(max_length=20)),
                ('complemento', models.CharField(max_length=20)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('pais', models.CharField(max_length=50)),
            ],
        ),
    ]
