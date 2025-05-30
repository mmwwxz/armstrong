# Generated by Django 5.1.5 on 2025-04-26 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_remove_info_adress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='titile',
        ),
        migrations.AddField(
            model_name='homepage',
            name='titile_1_line',
            field=models.CharField(default='Официальный дилер', max_length=20, verbose_name='Заголовок 1 линия'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='titile_2_line',
            field=models.CharField(default='ARMSTRONG в Кыргызстане', max_length=30, verbose_name='Заголовок 2 линия'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='description',
            field=models.CharField(default='Посетите ARMSTRONG BISHKEK в ТЦ Аю Грандa и узнайте, как мы можем помочь вам создать идеальные потолочные решения и освещение для вашего пространства!', max_length=220, verbose_name='Описание'),
        ),
    ]
