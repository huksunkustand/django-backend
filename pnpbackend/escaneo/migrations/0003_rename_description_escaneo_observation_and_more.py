# Generated by Django 4.1.1 on 2022-10-02 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escaneo', '0002_escaneo_date_creation_escaneo_date_modify_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='escaneo',
            old_name='description',
            new_name='observation',
        ),
        migrations.AddField(
            model_name='escaneo',
            name='academic_training',
            field=models.CharField(default=None, max_length=150),
        ),
        migrations.AddField(
            model_name='escaneo',
            name='place_residence',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='escaneo',
            name='residence_address',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='escaneo',
            name='name',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
