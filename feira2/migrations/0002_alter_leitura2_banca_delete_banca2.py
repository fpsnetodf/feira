# Generated by Django 4.1.1 on 2022-09-24 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feira2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leitura2',
            name='banca',
            field=models.CharField(choices=[('01', '590/611'), ('02', '591 '), ('03', '592/594'), ('04', '593'), ('05', '595'), ('06', '596/605'), ('07', '597'), ('08', '598'), ('09', '599'), ('10', '600'), ('11', '601/603'), ('12', '602'), ('13', '604'), ('14', '606'), ('15', '607'), ('16', '608'), ('17', '609'), ('18', '612/610/640/641'), ('19', '613/615'), ('20', '614/616'), ('21', '618/637'), ('22', '626/633'), ('23', '628'), ('24', '630'), ('25', '631'), ('26', '632'), ('27', '635'), ('28', '636'), ('29', '638/639'), ('30', '642'), ('31', '643'), ('32', '644'), ('33', '645'), ('34', '646')], max_length=15, unique=True),
        ),
        migrations.DeleteModel(
            name='Banca2',
        ),
    ]
