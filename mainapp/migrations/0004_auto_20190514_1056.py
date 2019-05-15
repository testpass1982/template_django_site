# Generated by Django 2.1.5 on 2019-05-14 10:56

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20190424_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChlenKomissii',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО Члена комиссии')),
                ('udost_type', models.CharField(choices=[('Персонал', 'Персонал'), ('Материалы', 'Материалы'), ('Оборудование', 'Оборудование'), ('Технологии', 'Технологии'), ('Оценка квалификации', 'Оценка квалификации')], default='Персонал', max_length=20, verbose_name='Тип удостоверения')),
                ('udost_number', models.CharField(max_length=20, verbose_name='Номер удостоверения')),
                ('udost_gtu', models.CharField(max_length=100, verbose_name='Область распространения (ГТУ)')),
                ('udost_sp_sv', models.CharField(max_length=200, verbose_name='Область аттестации(способы сварки, материалы и т.д.)')),
                ('tag', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.Tag')),
            ],
            options={
                'verbose_name_plural': 'Члены комиссии',
                'verbose_name': 'Член комиссии',
            },
        ),
        migrations.CreateModel(
            name='Chunk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Название вставки')),
                ('code', models.CharField(default='КОД_ВСТАВКИ', max_length=64, verbose_name='Уникальный код вставки')),
                ('html', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Форматирование вставки')),
            ],
            options={
                'verbose_name_plural': 'Вставки',
                'verbose_name': 'Вставка',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_short_name', models.CharField(blank=True, default=None, max_length=600, null=True, verbose_name='Краткое название организации')),
                ('org_full_name', models.CharField(blank=True, default=None, max_length=600, null=True, verbose_name='Полное название организации')),
                ('org_intro', models.CharField(blank=True, default=None, max_length=600, null=True, verbose_name='Текст для главной страницы')),
                ('org_phones', models.CharField(blank=True, default=None, max_length=600, null=True, verbose_name='Телефоны')),
                ('org_email', models.CharField(blank=True, default=None, max_length=600, null=True, verbose_name='Адрес электронной почты')),
                ('org_header_emails', models.CharField(blank=True, default=None, max_length=600, null=True, verbose_name='Адреса электронной почты (для хедера)')),
                ('org_header_phones', models.CharField(blank=True, default=None, max_length=600, null=True, verbose_name='Телефоны (для хедера)')),
                ('org_address', models.CharField(blank=True, default=None, max_length=600, null=True, verbose_name='Адрес местоположения организации')),
            ],
            options={
                'verbose_name_plural': 'Профили организации',
                'verbose_name': 'Профиль организации',
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
        migrations.RemoveField(
            model_name='document',
            name='category',
        ),
        migrations.AddField(
            model_name='document',
            name='url_code',
            field=models.CharField(blank=True, default='НЕ УКАЗАН', max_length=30, verbose_name='Код ссылки'),
        ),
    ]