# Generated by Django 4.0.2 on 2022-06-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(blank=True, max_length=5)),
                ('quarto', models.CharField(blank=True, max_length=3)),
                ('caixa', models.CharField(blank=True, max_length=50)),
                ('motivo', models.TextField()),
            ],
        ),
    ]