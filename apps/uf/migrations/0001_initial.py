# Generated by Django 3.2.7 on 2021-09-10 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30, verbose_name='Título')),
                ('subtitulo', models.CharField(max_length=50, verbose_name='Subtítulo')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagemhome/', verbose_name='Imagem')),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_video', models.CharField(max_length=30, verbose_name='Título do vídeo')),
                ('descricaoupload', models.TextField(verbose_name='Descrição do upload')),
                ('descricaovideo', models.TextField(verbose_name='Descrição de assistir')),
            ],
        ),
        migrations.CreateModel(
            name='Sobre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(verbose_name='Descrição')),
            ],
        ),
    ]