# Generated by Django 4.1.1 on 2022-09-27 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feira', '0005_bancas_obs_alter_leitura_banca'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bancas',
            name='obs',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
