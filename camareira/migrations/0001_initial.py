# Generated by Django 4.0.2 on 2022-05-04 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camareira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=100)),
                ('codigo', models.CharField(blank=True, max_length=3)),
            ],
        ),
    ]
