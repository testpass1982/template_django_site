# Generated by Django 2.1.5 on 2019-05-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20190515_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='org_main_phone',
            field=models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Второй телефон организации (используется в хедере)'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='org_main_phone_text',
            field=models.CharField(blank=True, default=None, max_length=30, null=True, verbose_name='Подпись под вторым телефоном в хедере, например "Бухгалтерия"'),
        ),
    ]
