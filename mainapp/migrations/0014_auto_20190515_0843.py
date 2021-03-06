# Generated by Django 2.1.5 on 2019-05-15 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20190515_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='org_acsm_reestr_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на реестр АЦСМ'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='org_acso_reestr_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на реестр АЦСО'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='org_acsp_reestr_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на реестр АЦСП'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='org_acst_reestr_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на реестр АЦСМ'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='org_cok_reestr_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на реестр ЦОК'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='org_csp_reestr_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на реестр ЦСП'),
        ),
    ]
