# Generated by Django 4.2.5 on 2023-09-26 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TesteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=255)),
                ('score', models.TextField(max_length=255)),
                ('senha', models.TextField(max_length=255)),
                ('id_chefe', models.IntegerField()),
            ],
        ),
    ]