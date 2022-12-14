# Generated by Django 4.1.1 on 2022-09-27 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feira', '0004_alter_bancas_options_alter_leitura_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bancas',
            name='obs',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='leitura',
            name='banca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_query_name='bancas', to='feira.bancas'),
        ),
    ]
