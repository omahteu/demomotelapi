# Generated by Django 4.0.2 on 2022-05-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tempos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('troca', models.CharField(blank=True, max_length=20)),
                ('desistencia', models.CharField(blank=True, max_length=20)),
                ('limpeza', models.CharField(blank=True, max_length=20)),
                ('faxina', models.CharField(blank=True, max_length=20)),
                ('manutencao', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]