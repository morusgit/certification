from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Category(MPTTModel):
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children',
                            db_index=True, verbose_name='Родительская категория')

    class MPTTMeta:
        order_insertion_by = ['title']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Supplier(models.Model):
    """
    Модель поставщика
    """
    name = models.CharField(unique=True, max_length=200, verbose_name="Наименование", db_index=True)
    contacts = models.OneToOneField('Contacts', on_delete=models.CASCADE, verbose_name='Контакты')
    products = models.ManyToManyField('Product', verbose_name='Товар', db_index=True)
    category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='supplier', verbose_name='Категория')
    #provider = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Поставщик', null=True, blank=True)
    arrears = models.FloatField(null=True, verbose_name="Задолженность перед поставщиком")
    release_date = models.DateTimeField(auto_now_add=True, verbose_name="Время создания", db_index=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Contacts(models.Model):
    email = models.EmailField(unique=True, verbose_name="E-mail")
    country = models.CharField(max_length=200, verbose_name="Страна")
    city = models.CharField(max_length=200, verbose_name="Город")
    street = models.CharField(max_length=200, verbose_name="Улица")
    house = models.CharField(max_length=200, verbose_name="Дом")

    def __str__(self):
        return f"{self.country}, {self.city}, {self.street}. {self.house}, {self.email}"

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class Product(models.Model):
    name = models.CharField(unique=True, max_length=200, verbose_name="Наименование", db_index=True)
    model = models.CharField(unique=True, max_length=200, verbose_name="Модель", db_index=True)
    release_date = models.DateField(auto_now_add=True, verbose_name="Дата выхода продукта", db_index=True)

    def __str__(self):
        return f"{self.name} {self.model}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
