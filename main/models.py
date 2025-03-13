from django.db import models

CATEGORY_CHOICES = [
    ('lighting', 'Освещение'),
    ('ceilings', 'Потолки'),
    ('composition', 'Состав материала:'),
    ('material', 'Материалы из:'),
]

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Категория"
        verbose_name = 'Категория'

    name = models.CharField(max_length=255, unique=True, verbose_name='Название категории')
    category_type = models.CharField(max_length=40, choices=CATEGORY_CHOICES, verbose_name='Тип категории', default='lighting')

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name_plural = "Товар"
        verbose_name = "Товары"

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Подкатегория')
    name = models.CharField(max_length=255, verbose_name="Наименование продукта")
    description = models.TextField(verbose_name="Описание")
    warranty = models.CharField(max_length=50, verbose_name="Гарантия", default="Не указано")
    region = models.CharField(max_length=100, verbose_name="Регион", default="Не указан")
    material = models.CharField(max_length=100, verbose_name="Название материала", default="Не указан")
    material_composition = models.CharField(max_length=100, verbose_name="Состав материала", default="Не указан")

    retail_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Цена розничная")
    wholesale_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Цена крупнооптовая")
    bulk_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Цена оптовая")

    image1 = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Изображение 1")
    image2 = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Изображение 2")
    image3 = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Изображение 3")
    image4 = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Изображение 4")
    image5 = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Изображение 5")
    image6 = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Изображение 6")
    image7 = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Изображение 7")
    image8 = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Изображение 8")
    image9 = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Изображение 9")
    image10 = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Изображение 10")

    def __str__(self):
        return self.name


class Blog(models.Model):
    class Meta:
        verbose_name_plural = "Блог"
        verbose_name = 'Блоги'

    title = models.CharField(max_length=255, verbose_name='Описание')
    content = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    image = models.ImageField(upload_to='blog/', null=False, blank=True, verbose_name="Изображение")

    def __str__(self):
        return self.title


class Comment(models.Model):
    class Meta:
        verbose_name_plural = "Отзыв"
        verbose_name = "Отзывы"

    name = models.CharField(max_length=255, verbose_name='Имя')
    content = models.TextField(verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    image = models.ImageField(upload_to='comment/', null=False, blank=True, verbose_name="Изображение")

    def __str__(self):
        return self.name


class Request(models.Model):
    class Meta:
        verbose_name_plural = "Заявка"
        verbose_name = "Заявки"

    name = models.CharField(max_length=255, verbose_name='Имя')
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')
    comments = models.CharField(max_length=255, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')

    def __str__(self):
        return self.phone_number
