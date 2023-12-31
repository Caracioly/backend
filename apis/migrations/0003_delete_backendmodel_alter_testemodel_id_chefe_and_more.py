# Generated by Django 4.2.5 on 2023-09-27 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_testemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BackendModel',
        ),
        migrations.AlterField(
            model_name='testemodel',
            name='id_chefe',
            field=models.IntegerField(help_text='ID do chefe'),
        ),
        migrations.AlterField(
            model_name='testemodel',
            name='nome',
            field=models.TextField(help_text='Nome do usuário', max_length=255),
        ),
        migrations.AlterField(
            model_name='testemodel',
            name='score',
            field=models.TextField(help_text='Pontuação do usuário', max_length=255),
        ),
        migrations.AlterField(
            model_name='testemodel',
            name='senha',
            field=models.TextField(help_text='Senha do usuário', max_length=255),
        ),
    ]
