# Generated by Django 4.2.2 on 2023-06-14 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_company_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_fiscal', models.IntegerField(default=1)),
            ],
        ),
    ]
