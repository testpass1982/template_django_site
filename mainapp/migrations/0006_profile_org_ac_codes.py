# Generated by Django 2.1.5 on 2019-05-14 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20190514_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='org_ac_codes',
            field=models.CharField(blank=True, default=None, help_text="В формате {'ACSP': 'СУР-12АЦ', 'ACSM': 'АЦСМ-12'}", max_length=100, null=True, verbose_name='Коды аттестационных центров'),
        ),
    ]
