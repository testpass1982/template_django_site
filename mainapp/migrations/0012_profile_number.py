# Generated by Django 2.1.5 on 2019-05-15 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20190514_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='number',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Порядок сортировки'),
        ),
    ]
