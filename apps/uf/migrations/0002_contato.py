# Generated by Django 3.2.7 on 2021-09-10 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
            ],
        ),
    ]