# Generated by Django 5.1.5 on 2025-04-26 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_category_category_type_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titile', models.CharField(max_length=55, verbose_name='Заголовок')),
                ('description', models.CharField(max_length=220, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Инфо главная страница заголовок',
                'verbose_name_plural': 'Инфо главная страница заголовок',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=13, verbose_name='Номер телефона')),
                ('email', models.CharField(max_length=255, verbose_name='Почта')),
                ('social_link_insta', models.CharField(max_length=655, verbose_name='Ссылка на Instagram')),
                ('social_link_facebook', models.CharField(max_length=655, verbose_name='Ссылка на FaceBook')),
                ('social_link_whatsapp', models.CharField(max_length=655, verbose_name='Ссылка на WhatsApp')),
                ('social_link_telegram', models.CharField(max_length=655, verbose_name='Ссылка на Telegram')),
            ],
            options={
                'verbose_name': 'Инфо',
                'verbose_name_plural': 'Инфо',
            },
        ),
    ]
