# Generated by Django 5.2 on 2025-04-15 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('professor', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=500)),
            ],
        ),
    ]
