# Generated by Django 4.1.1 on 2022-09-15 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Escaneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('user_creation', models.CharField(max_length=100)),
                ('user_modify', models.CharField(max_length=100)),
            ],
        ),
    ]
